# CLAUDE-CODE-RENDER.md — Muse builds the pipeline

Render this film on the Mac with Claude Code + the brutalist.art toolkit.

## 0. Get the files

```
cd info-7375-branding-and-ai/fall-2026/nik-bear-brown/assignment-3/films/part-1-pipeline/
```

Files: `beat_sheet.json`, `scenes.py`, `ACTS.md`, `SHOTLIST.md`, `FACTCHECK.md`.

## 1. Narration (Kokoro, am_onyx)

For each beat in `beat_sheet.json`, synthesize the `line` field with Kokoro
voice `am_onyx`. Save as `audio/BIDEA.mp3` … `audio/BOUT.mp3` (14 files).
Persona: "Liam, in for Bear"; register: Teardown.

## 2. Review cut

```
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art
./art run --reel a3-pipeline \
  --beats <film-dir>/beat_sheet.json --scenes <film-dir>/scenes.py \
  --audio <film-dir>/audio/
```

## 3. Final 4K master

```
./art final --reel a3-pipeline
```

## 4. Publish

Only on Nik's explicit instruction.

## Film facts

- 14 beats, ~5m02s. 12 scenes, all static-QC clean (first pass).
- No MP3/MP4 files are committed to the repo.
