# YouTube Playlist Reorder

Reorders your YouTube playlists (newcomer-first viewing order), removes
duplicates and dead videos — via the YouTube Data API, run on your machine
with your credentials. Nothing leaves your computer except the API calls.

## Files

- `reorder_playlists.py` — the script. Dry run by default; changes nothing
  unless you pass `--apply`.
- `playlist_order_spec.json` — the per-playlist plan: which videos go in what
  order, what gets removed. Review it before applying.
- `README.md` — this file.

## Setup (one time, ~5 minutes)

1. Install the libraries:
   ```
   pip install google-api-python-client google-auth-oauthlib
   ```
2. Google Cloud Console (console.cloud.google.com):
   - Create (or pick) a project, enable **YouTube Data API v3**
     (APIs & Services > Library).
   - APIs & Services > Credentials > Create Credentials > **OAuth client ID**,
     type **Desktop app**. Download the JSON, save it in this folder as
     `client_secret.json`.
3. Run the dry run (below). A browser window opens for Google sign-in the
   first time; the token is cached as `token.json` afterwards.

## Use

Dry run — prints exactly what WOULD change, per playlist:
```
python3 reorder_playlists.py --spec playlist_order_spec.json
```

Apply for real (asks per playlist; `--yes` skips the prompts):
```
python3 reorder_playlists.py --spec playlist_order_spec.json --apply
```

One playlist only:
```
python3 reorder_playlists.py --spec playlist_order_spec.json --apply --only "Walker (Game AI)"
```

## What it does per playlist

1. Fetches every item (handles pagination).
2. Deletes items whose video is deleted/private/unavailable (auto-detected).
3. De-duplicates — keeps the first occurrence of each video.
4. Applies explicit removals from the spec.
5. Reorders to the spec's `order` list (first = top). Videos not named keep
   their relative order at the end.
6. Updates playlist title/description if the spec provides them.

Re-running the same spec is a no-op. Quota is tiny (~50 units per write
call against a 10,000/day default).

## Spec format

```json
{
  "playlists": {
    "Exact Playlist Title": {
      "order": ["First video title", "Second video title"],
      "remove": ["Video title to drop"],
      "note": "human note, ignored by the script"
    }
  }
}
```

Titles must match YouTube exactly. Same-title videos are disambiguated as
`"Title [m:ss]"`.
