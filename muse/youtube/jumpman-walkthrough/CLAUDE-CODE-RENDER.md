# Claude Code Render Prompt — Jumpman Extended: Full Godot Walkthrough

Paste this into Claude Code on a machine with the brutalist.art toolkit
checked out and the render dependencies installed.

## What this is

A complete Godot walkthrough film (walker mode) for the Jumpman extension:
**"Jumpman Extended: Full Godot Walkthrough"** — 136.4s, 11 beats, 4K.

- Voice: Kokoro `am_onyx`, persona "Liam, in for Bear" (channel `claude-liam`)
- Pipeline: `godot-waikthrough` skill (note the canonical misspelling),
  `./art godot-waikthrough --check REEL` passes (23 implemented features,
  9 planned, 25 evidence intervals, 7 scripted-input 4K captures)
- Slate cut (review): `slate/jumpman-walkthrough-slate.mp4` — has burnt-in
  timecode + beat labels. The `./art final` 4K master is clean.

## Render steps

```bash
cd ~/workspace/brutalist.art

# 1. Narration (Kokoro; durations are ground truth and written back)
/home/hatch/workspace/render-venv/bin/python runtime/scripts/generate_audio_kokoro.py \
  /home/hatch/workspace/film-render/jumpman-walkthrough

# 2. Bookends (Remotion; needs node_modules + a working headless browser)
python3 runtime/scripts/remotion_scenes.py \
  /home/hatch/workspace/film-render/jumpman-walkthrough

# 3. Validate
./art godot-waikthrough --check /home/hatch/workspace/film-render/jumpman-walkthrough

# 4. Assemble (review/slate cut)
bash runtime/scripts/run.sh /home/hatch/workspace/film-render/jumpman-walkthrough
```

Gameplay media (`media/B02.mp4` … `media/B06B.mp4`) is pre-trimmed frame-exact
from the 4K captures — the compiler retimes ±5% silently, so media durations
must already equal the narration durations exactly. Never retime gameplay to
fit audio; regenerate the narration instead.

## Reproducing the captures (optional)

All captures are scripted input (synthetic `InputEventKey` via
`Input.parse_input_event` — the normal input path, no teleports) recorded
from an isolated copy of the game (`jumpman-capture-copy`; the original
`walker-jumpman-clawd` was never modified) under Xvfb at 3840x2160 with
Godot Movie Maker `--write-movie --fixed-fps 60`.

Drivers live in `godot/tests/` of the capture copy:
`capture_fullrun.gd`, `capture_death.gd`, `capture_pause.gd`,
`capture_egg.gd`, `capture_grumbler.gd`, `capture_sidekill.gd`,
`capture_fallretry.gd`. Each was dry-run at 720p with `PROBE_QUIT_TICKS`
before its 4K record. JSONL input logs sit next to the MP4s.

Known defects documented on camera (not hidden):
- The hidden Easter-egg block is unreachable (84px climb needed, 53px max
  jump) — `take_egg_4k.mp4` shows the genuine failed attempt.
- The "Coin master" completion rank is a dead branch and is never claimed.
- Captures are scripted input, never human playtests — labeled as such.

## Package contents

- `beat_sheet.json` — 11 beats (B00–B09 + B06B), validator-compliant
- `coverage.json` — skill schema v1 evidence map (sha256-pinned captures)
- `CAPTURE.md` — method, timecodes, per-take QC notes
- `RIFF.md` — narration commentary per beat
- `SHOTLIST.md`, `FACTCHECK.md`, `PROMPTS.md`, `BUILD-PROMPT.md`
- `feature-inventory.json` — 32 features (23 implemented, 9 planned)
- `capture/*_inputs.jsonl` — input logs (tick/60 = video seconds)

Media (MP4/MP3/WAV/AVI) is never committed; the slate cut lives in
Drive `00-muse`.
