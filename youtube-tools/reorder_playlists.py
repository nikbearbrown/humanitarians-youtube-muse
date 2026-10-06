#!/usr/bin/env python3
"""Reorder YouTube playlists (and clean them) via the YouTube Data API v3.

Runs on YOUR machine with YOUR OAuth client. Nothing leaves your computer
except the API calls you approve.

Setup:
  1. pip install google-api-python-client google-auth-oauthlib
  2. Put your OAuth client as client_secret.json in this folder
     (Google Cloud Console > APIs & Services > Credentials > OAuth client ID,
      type "Desktop app"; enable "YouTube Data API v3" for the project)
  3. Review playlist_order_spec.json (the desired orders)
  4. python3 reorder_playlists.py --spec playlist_order_spec.json        # dry run
  5. python3 reorder_playlists.py --spec playlist_order_spec.json --apply # for real

What it does per playlist in the spec (spec is keyed by playlist TITLE):
  1. Resolves the playlist title to its id via the API (warns on ambiguity).
  2. Fetches every playlist item (handles pagination).
  3. Removes items whose video is deleted/private/unavailable (auto-detected).
  4. De-duplicates: keeps the FIRST occurrence of each video, removes the rest.
  5. Applies explicit removals from the spec (by video title).
  6. Reorders items to the spec's "order" list (video titles, first = top of the
     playlist). Videos not named in the list keep their current relative order
     and go after the named ones. Disambiguate same-title videos as
     "Title [m:ss]".
  7. Updates the playlist's title/description if the spec provides them.

Safety:
  - Dry run is the default. Nothing changes without --apply.
  - With --apply it still asks for confirmation per playlist (skip with --yes).
  - Every action is logged; re-running the same spec is a no-op.
  - Quota: ~1 unit per list call, 50 per write. 38 playlists is well within
    the default 10,000/day.
"""

import argparse
import json
import os
import sys
import time

SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]
TOKEN_FILE = "token.json"
CLIENT_FILE = "client_secret.json"


def get_service():
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build

    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(CLIENT_FILE):
                sys.exit(
                    f"Missing {CLIENT_FILE}. Create an OAuth client (Desktop app) "
                    "in Google Cloud Console and save it as client_secret.json here."
                )
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, "w") as f:
            f.write(creds.to_json())
    return build("youtube", "v3", credentials=creds)


def fetch_items(yt, playlist_id):
    items = []
    token = None
    while True:
        r = (
            yt.playlistItems()
            .list(
                part="snippet,contentDetails",
                playlistId=playlist_id,
                maxResults=50,
                pageToken=token or "",
            )
            .execute()
        )
        items.extend(r.get("items", []))
        token = r.get("nextPageToken")
        if not token:
            break
    return items


def is_dead(item):
    """Deleted/private/unavailable videos have degraded snippet data."""
    sn = item.get("snippet", {})
    title = sn.get("title", "")
    desc = sn.get("description", "")
    vid = sn.get("resourceId", {}).get("videoId", "")
    return (
        title in ("Deleted video", "Private video")
        or not vid
        or "unavailable" in desc.lower()
    )


def parse_title(spec_title):
    """Split "Title [m:ss]" into (title, duration-or-None)."""
    import re
    m = re.match(r"^(.*)\s+\[(\d+:\d+)\]$", spec_title.strip())
    if m:
        return m.group(1).strip(), m.group(2)
    return spec_title.strip(), None


def iso_to_ms(iso):
    import re
    m = re.match(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", iso or "")
    if not m:
        return None
    h, mi, s = (int(x) if x else 0 for x in m.groups())
    total = h * 3600 + mi * 60 + s
    return f"{total // 60}:{total % 60:02d}"


def make_matcher(yt):
    dur_cache = {}

    def durations(video_ids):
        missing = [v for v in video_ids if v not in dur_cache]
        for i in range(0, len(missing), 50):
            batch = missing[i:i + 50]
            r = yt.videos().list(part="contentDetails", id=",".join(batch)).execute()
            for v in r.get("items", []):
                dur_cache[v["id"]] = iso_to_ms(v["contentDetails"]["duration"])
        return dur_cache

    def match_one(unmatched, spec_title):
        want, dur = parse_title(spec_title)
        cands = [it for it in unmatched if it["snippet"]["title"] == want]
        if dur and len(cands) > 1:
            durs = durations([it["snippet"]["resourceId"]["videoId"] for it in cands])
            cands = [it for it in cands
                     if durs.get(it["snippet"]["resourceId"]["videoId"]) == dur]
        if len(cands) == 1:
            unmatched.remove(cands[0])
            return cands[0]
        return None  # ambiguous or missing: leave in place, warn

    return match_one


def plan_playlist(yt, pid, spec, match_one):
    items = fetch_items(yt, pid)
    actions = []  # (kind, detail, playlistItemId)

    # 1. dead items
    dead = [it for it in items if is_dead(it)]
    for it in dead:
        actions.append(("delete", f"dead item '{it['snippet'].get('title')}'", it["id"]))

    live = [it for it in items if it not in dead]

    # 2. dedupe (keep first occurrence by current position)
    seen = {}
    for it in sorted(live, key=lambda x: x["snippet"].get("position", 0)):
        vid = it["snippet"]["resourceId"]["videoId"]
        if vid in seen:
            actions.append(("delete", f"duplicate of '{it['snippet']['title']}'", it["id"]))
        else:
            seen[vid] = it
    live = [seen[v] for v in seen]  # first occurrences only, in position order

    # helper: match a spec title to one live item
    unmatched = list(live)

    # 3. explicit removals from spec
    for st in spec.get("remove", []):
        it = match_one(unmatched, st)
        if it:
            actions.append(("delete", f"spec removal '{it['snippet']['title']}'", it["id"]))
            live.remove(it)
        else:
            print(f"  [warn] removal target not found or ambiguous: {st!r}")

    # 4. reorder
    new_order = []
    for st in spec.get("order", []):
        it = match_one(unmatched, st)
        if it:
            new_order.append(it)
        else:
            print(f"  [warn] order target not found or ambiguous: {st!r} (left in place)")
    new_order.extend(unmatched)  # unnamed videos keep relative order at the end

    current_ids = [it["id"] for it in live]
    target_ids = [it["id"] for it in new_order]
    moves = target_ids if current_ids != target_ids else []

    # 5. playlist metadata
    meta = {k: spec[k] for k in ("title", "description") if k in spec}

    return actions, moves, new_order, meta


def resolve_playlists(yt, wanted_titles):
    """Map wanted playlist titles -> ids via playlists.list(mine=true)."""
    found = {}
    token = None
    while True:
        r = yt.playlists().list(part="snippet", mine=True, maxResults=50,
                                pageToken=token or "").execute()
        for p in r.get("items", []):
            found.setdefault(p["snippet"]["title"], p["id"])
        token = r.get("nextPageToken")
        if not token:
            break
    resolved = {}
    for t in wanted_titles:
        if t in found:
            resolved[t] = found[t]
        else:
            print(f"[warn] playlist not found: {t!r}")
    return resolved


def apply_playlist(yt, pid, title, actions, moves, new_order, meta, dry, yes):
    print(f"\n=== {title} ({pid}) ===")
    if not actions and not moves and not meta:
        print("  no changes needed")
        return
    for kind, detail, _ in actions:
        print(f"  [{kind}] {detail}")
    if moves:
        print(f"  [reorder] {len(moves)} videos -> new top-to-bottom order:")
        for i, it in enumerate(new_order[:8]):
            print(f"    {i+1}. {it['snippet']['title']}")
        if len(new_order) > 8:
            print(f"    ... and {len(new_order)-8} more")
    for k, v in meta.items():
        print(f"  [meta] set {k} ({len(v)} chars)")
    if dry:
        return
    if not yes:
        ans = input("  Apply these changes? [y/N] ").strip().lower()
        if ans != "y":
            print("  skipped")
            return
    for kind, detail, pli_id in actions:
        if kind == "delete":
            yt.playlistItems().delete(id=pli_id).execute()
            time.sleep(0.2)
    if moves:
        # reposition from the end backwards to avoid position collisions
        id_by_video = {it["snippet"]["resourceId"]["videoId"]: it["id"]
                       for it in new_order}
        for pos, it in enumerate(new_order):
            yt.playlistItems().update(
                part="snippet",
                body={
                    "id": it["id"],
                    "snippet": {
                        "playlistId": pid,
                        "position": pos,
                        "resourceId": {
                            "kind": "youtube#video",
                            "videoId": it["snippet"]["resourceId"]["videoId"],
                        },
                    },
                },
            ).execute()
            time.sleep(0.3)
    if meta:
        pl = yt.playlists().list(part="snippet", id=pid).execute()["items"][0]
        sn = pl["snippet"]
        if "title" in meta:
            sn["title"] = meta["title"]
        if "description" in meta:
            sn["description"] = meta["description"]
        yt.playlists().update(part="snippet", body={"id": pid, "snippet": sn}).execute()
    print("  applied.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--spec", required=True, help="playlist_order_spec.json")
    ap.add_argument("--apply", action="store_true", help="execute changes (default: dry run)")
    ap.add_argument("--yes", action="store_true", help="skip per-playlist confirmation")
    ap.add_argument("--only", help="only process the playlist with this title")
    args = ap.parse_args()

    spec = json.load(open(args.spec))
    yt = get_service()
    match_one = make_matcher(yt)
    id_by_title = resolve_playlists(yt, spec["playlists"].keys())
    for ptitle, pspec in spec["playlists"].items():
        if args.only and ptitle != args.only:
            continue
        pid = id_by_title.get(ptitle)
        if not pid:
            continue
        actions, moves, new_order, meta = plan_playlist(yt, pid, pspec, match_one)
        apply_playlist(yt, pid, pspec.get("label", ptitle), actions, moves,
                       new_order, meta, dry=not args.apply, yes=args.yes)


if __name__ == "__main__":
    main()
