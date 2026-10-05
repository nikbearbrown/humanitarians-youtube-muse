# CLAUDE-CODE-RENDER.md — Muse audits itself

Render this film on the Mac with Claude Code + the brutalist.art toolkit.

## 0. Get the files

```
cd info-7375-branding-and-ai/fall-2026/nik-bear-brown/assignment-3/films/part-2-audits/
```

Files: `beat_sheet.json`, `scenes.py`, `ACTS.md`, `SHOTLIST.md`, `FACTCHECK.md`.

## 1. Narration (Kokoro, am_onyx)

For each beat in `beat_sheet.json`, synthesize the `line` field with Kokoro
voice `am_onyx`. Save as `audio/BIDEA.mp3` … `audio/BOUT.mp3` (14 files).
Persona: "Liam, in for Bear"; register: Teardown.

## 2. Review cut

```
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art
./art run --reel a3-audits \
  --beats <film-dir>/beat_sheet.json --scenes <film-dir>/scenes.py \
  --audio <film-dir>/audio/
```

## 2b. Muse mascot on the first beat

Bear, 2026-10-04: the Muse mascot (plush monster, the 1:1 clips in `books/muse/muse_logo/`) appears on the
first beat of every Muse film. After the review cut has rendered the first beat (`media/BIDEA.mp4` exists
in the reel's build folder, the one `art run` prints as `done →`), run:

```
python3 /Users/bear/Documents/CoWork/bear-textbooks/books/muse/apply_muse_logo.py <that reel folder>
```

It overlays `muse-logo-02` (keyed to transparent by `books/muse/key_muse_logo.py`; the whole mascot stays inside its square)
bottom-right of the first beat, and keeps the untouched render as `media/BIDEA.base.mp4`, so running it twice is safe (`--undo` restores).
Then re-run the review cut once (it only recompiles) before the final. The beat's length and audio do not change.

## 3. Final 4K master

```
./art final --reel a3-audits
```

## 4. Publish

Only on Nik's explicit instruction.

## Film facts

- 14 beats, ~5m06s. 12 scenes, all static-QC clean (first pass).
- No MP3/MP4 files are committed to the repo.
