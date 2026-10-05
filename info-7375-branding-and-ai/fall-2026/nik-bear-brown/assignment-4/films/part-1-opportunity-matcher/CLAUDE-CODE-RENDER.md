# CLAUDE-CODE-RENDER.md — "Muse builds the opportunity matcher"

Paste this whole prompt into Claude Code on Bear's Mac. It generates the
narration audio and renders the film. Nothing here publishes anything.

---

You are running on Bear's Mac. Your job: generate the narration audio and
render the lecture film "Muse builds the opportunity matcher" — review cut first,
then the final 4K master. **Never publish, upload, or stage anything.**

## Paths

- Toolkit: `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art`
- Film repo: the local clone of `nikbearbrown/humanitarians-youtube-muse`
  (if you don't know where Bear cloned it, ask him — do not guess)
- Reel: `<film-repo>/info-7375-branding-and-ai/fall-2026/nik-bear-brown/assignment-4/films/part-1-opportunity-matcher`

Call the reel path `$REEL` below.

## Film facts (do not invent more)

- 22 beats: BIDEA, BDEFS, B01–B17 (Manim, classes M01–M17 in `scenes.py`),
  BVDT, BHTF, BOUT. Channel claude-liam, voice Kokoro `am_onyx`.
- The narration text per beat is in `beat_sheet.json`.
- Every factual claim is verified in `FACTCHECK.md` against
  `assignment-4/FRICTIONAL.md` and the files it cites. If a visual fix tempts
  you to add a new claim, don't — fix the visual, not the script.

## Steps

1. **Sanity check.** Confirm `$REEL/beat_sheet.json` exists with 22 beats and
   `$REEL/scenes.py` compiles: `python3 -m py_compile $REEL/scenes.py`.

2. **Narration audio** (Kokoro — free, local):
   ```
   python3 /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/runtime/scripts/generate_audio_kokoro.py $REEL
   ```
   This writes MP3s into `$REEL/mp3/` and measures durations. If a beat
   mispronounces (names, acronyms), re-voice just that beat:
   `.../generate_audio_kokoro.py $REEL --only <BID>`.

3. **Review cut:**
   ```
   cd /Users/bear/Documents/CoWork/bear-textbooks/books
   ./brutalist.art/art run $REEL --height 2160
   ```
   If a gate fails, read the gate output, fix the cause (usually `scenes.py`),
   and re-run until every gate passes. Do not weaken or skip gates to pass.

4. **Watch it.** Look at the review cut (at minimum the qc-sheet / contact
   sheet). Fix anything visually wrong, re-run.

4b. **Muse mascot on the first beat** (Bear, 2026-10-04). Once `$REEL/media/BIDEA.mp4` exists:
   ```
   python3 /Users/bear/Documents/CoWork/bear-textbooks/books/muse/apply_muse_logo.py $REEL
   ```
   It overlays the mascot (`muse-logo-02`, keyed to transparent; the whole mascot stays inside its square) bottom-right of the first beat and keeps
   the untouched render as `media/BIDEA.base.mp4`, so running it twice is safe (`--undo` restores). Then re-run
   step 3 once (recompile only) before the final. The beat's length and audio do not change.

5. **Final 4K master** (only when the review cut is clean):
   ```
   ./brutalist.art/art final $REEL --height 2160 --out $REEL/exports/landscape
   ```

6. **Bookend check:**
   ```
   python3 /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/runtime/scripts/bookend_check.py $REEL
   ```
   Must pass.

7. **Report back:** the master MP4 path, runtime, resolution (expect
   3840×2160), and any warnings left standing. MP3s and MP4s stay on this
   Mac — they are git-ignored and never pushed.
