# BUILD-LOG.md — "Muse making a film about Muse"

## 2026-10-03

- Project opened. Channel confirmed as claude-liam (Liam, in for Bear).
  Bear set the title: "Muse making a film about Muse".
- Reel: `muse/youtube/claude-liam-lecture-muse-making-a-film-about-muse/`
  in `nikbearbrown/humanitarians-youtube-muse` (pushed via GitHub API;
  SSH is blocked from the build VM).
- Paperwork: ACTS.md (4 acts, 17 body beats), SHOTLIST.md (GATE L asked;
  library hits were other films' content — built, not slated),
  FACTCHECK.md (17/17 claims doc-grounded; prices, tier names, model
  versions cut), SOURCES.md.
- `make_sheet.py` → `beat_sheet.json`: 22 beats (BIDEA, BDEFS, B01–B17,
  BVDT, BHTF, BOUT), estimated ~211 s (~3.5 min).
- `scenes.py`: 17 Manim Scene classes (M01–M17). Static gate: 17/17 clean.
  Two fixes during authoring: M15/M16 meter fills use Transform (morph)
  instead of animate-proxy width animation, which the static checker
  cannot see as a shape change.
- Lane histogram: Manim diagram ×11, Manim lesson ×3, Manim chart ×2,
  Manim timeline/clock ×1. Bookends: library Remotion (all verified
  renderable).
- Outstanding (Bear's side): narration MP3s (Kokoro) and MP4 renders,
  via the Claude Code prompt in CLAUDE-CODE-RENDER.md.

---

## 2026-10-04 — Muse mascot on the first beat

Bear: put the Muse logo clips on the first beat of the Muse films. First attempt used a 2:3 clip (arms cropped at the clip edge); Bear replaced the clips with 1:1 renders in which the whole character stays inside the frame. `books/muse/key_muse_logo.py` keys them to transparent video (`muse_logo/keyed/`), and `books/muse/apply_muse_logo.py` overlays `muse-logo-02` bottom-right of BIDEA (fade in 0.35 s, plays 5.2 s, fade out 0.45 s). The untouched render is `media/BIDEA.base.mp4`; `--undo` restores it. Beat length and audio unchanged. Placement is in `muse_logo.json`. If BIDEA is ever re-rendered from Remotion, re-run the script before the final cut.
