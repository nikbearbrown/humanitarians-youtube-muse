# BUILD-LOG.md — "Claude making a film about Muse"

Reel: `muse/youtube/claude-liam-lecture-claude-making-a-film-about-muse/`
Built on Muse's Linux VM, 2026-10-03. No audio/video generated here.

## What was built

| File | Status |
|---|---|
| ACTS.md | coverage map: 6 acts, 23 body beats, whole-document pass |
| SHOTLIST.md | 23 body beats routed (all Manim), bookends library |
| FACTCHECK.md | Gate F: attribution map (Meta / third-party / Nik's take / doc figures) |
| make_sheet.py | beat sheet generator |
| beat_sheet.json | 28 beats, ~444 s estimated (~7.4 min) |
| scenes.py | 23 Manim classes M01–M23 |
| CLAUDE-CODE-RENDER.md | render prompt for Bear's Mac |
| SOURCES.md / PROMPTS.md / CHECKS-REPORT.md | paperwork |

## Decisions

- **Framing:** the film presents Bear and Claude's opinion, narrated by
  Liam. Contested claims stay attributed in voice and on screen.
- **Narration trim:** first draft estimated ~502 s; tightened 17 beats to
  land at ~444 s without dropping any section of the source.
- **M18 split:** business conflicts + platform dependence in one beat, the
  phone's permissions in its own — the triptych was too dense.
- **No paid generation:** all visuals are Manim or library Remotion
  components. No Higgsfield or other paid beats.

## Handoff

Bear pulls the repo and pastes `CLAUDE-CODE-RENDER.md` into Claude Code
on his Mac: Kokoro narration → `./art run` review cut → `./art final`
4K master. Never publish.

---

## 2026-10-04 update — "what a hundred million tokens means in real work"

Bear's asks: (1) update the film on what 100M tokens means in real work given 18% used and what that produced; (2) emphasize that the data-sharing API price is more than 10x cheaper because they are buying data and a user base, so be careful with your data; (3) emphasize that Muse's "one folder only" is a language model's promise, that Bear runs it only in the cloud, only on things like Google Drive, never locally.

- Edited `make_sheet.py` (source of record) and merged the new sheet over the old `beat_sheet.json`, carrying audio and build state forward for the 23 untouched beats. Beats: 28 → 36 (new B24–B31; revised B08, B13, B20, BDEFS, BVDT).
- `scenes.py`: M08 revised; M24–M31 added. Old M08/B13/B20 clips, audio and the previous master are in `_superseded/2026-10-04-pre-tokens-update/`.
- Numbers in B25–B28 are computed from files on disk (13 film packages in this repo, all committed 2026-10-03), Bear's stated 18%, and the document's prices. Every assumption is in FACTCHECK.md rows 23–38; the big ones: that the 18% went into those packages, and that Muse tokens count like ordinary tokens.
- Free build, no paid steps.
