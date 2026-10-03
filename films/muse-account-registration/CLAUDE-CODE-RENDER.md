# CLAUDE-CODE-RENDER.md — How to register for a Muse account

Render this film on the Mac with Claude Code + the brutalist.art toolkit.

## 0. Get the files

Clone or pull `https://github.com/nikbearbrown/humanitarians-youtube-muse`,
then:

```
cd films/muse-account-registration/
```

Files: `beat_sheet.json`, `scenes.py`, `ACTS.md`, `SHOTLIST.md`, `FACTCHECK.md`.

## 1. Narration (Kokoro, am_onyx)

For each beat in `beat_sheet.json`, synthesize the `line` field with Kokoro
voice `am_onyx`. Save as `audio/BIDEA.mp3` … `audio/BOUT.mp3` (15 files).
Persona: "Liam, in for Bear"; register: Teardown.

## 2. Review cut

```
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art
./art run --reel muse-account-registration \
  --beats <film-dir>/beat_sheet.json --scenes <film-dir>/scenes.py \
  --audio <film-dir>/audio/
```

Watch the review slate. Check: the email reads as muse@humanitarians.ai
(no other personal info on screen); the card mock shows "Meta CC",
MERCHANT-LOCKED, $10; the six code boxes are legible.

## 3. Final 4K master

```
./art final --reel muse-account-registration
```

## 4. Publish

Only on Nik's explicit instruction.

## Film facts

- 15 beats, ~5m18s. 13 scenes, all static-QC clean.
- No MP3/MP4 files are committed to the repo.
- Staged in this repo; intended home is
  `Humanitariansai/humanitarians-youtube-muse` (copy the folder there when
  ready).
