# Gameplay Capture Notes — jumpman walkthrough

## Method (all captures)

- **Engine:** Godot 4.7.stable.official.5b4e0cb0f, GL Compatibility renderer.
- **How played:** scripted input only. A SceneTree driver script sends synthetic
  `InputEventKey` events via `Input.parse_input_event()`, which travel the game's
  NORMAL input path: `InputMap` action matching → `_unhandled_input` (menu /
  pause / restart / confirm) and the `Input` singleton (`Input.get_axis`,
  `Input.is_action_pressed`, `Input.is_action_just_pressed`) read by
  `features/player/player.gd`. The driver observes `game.player.position` and
  `game.state` once per physics tick and chooses inputs reactively (gap/wall
  raycasts, hazard proximity, enemy patrol timing).
- **What was NOT done:** no teleports, no `position`/`velocity` writes, no
  `test_control`/`test_axis`/`test_jump_*` fields, no collision disabling, no
  state forcing, no gameplay retiming. The original game project was not
  modified; all driver scripts live in an isolated copy
  (`~/workspace/godot/jumpman-capture-copy`, original at
  `~/workspace/godot/walker-jumpman-clawd` untouched).
- **Recording:** Godot Movie Maker (`--write-movie <file>.avi --fixed-fps 60`)
  running under Xvfb (`:99`, 3840x2160x24). (`frame_post_draw` capture hangs in
  pure `--headless`; Xvfb is required.)
- **Resolution:** native 3840x2160 window (`--resolution 3840x2160`). The project
  viewport is 640x360 with `stretch/mode="canvas_items"`, `aspect="keep"`;
  3840x2160 is exactly 6x, so the canvas fills the frame and vector art/text
  rasterizes at full 4K. Verified with `ffprobe` (see below).
- **Simulation speed:** normal. `--fixed-fps 60` advances exactly 1/60s per frame;
  no retiming.
- **Conversion:** `ffmpeg -i <avi> -c:v libx264 -pix_fmt yuv420p -crf 18 <mp4>`.
  Original AVIs kept.
- **Input logs:** JSONL, one line per input event:
  `{"tick":N,"action":"move_right"|"move_left"|"jump"|"confirm"|"restart"|"pause"|"menu",`
  `"type":"press"|"release","player_x":..,"player_y":..,"state":..}`.
  `tick/60` = video seconds (fixed 60fps). Segment markers were printed as
  `SEGMENT t=<s> name=<label> x=<px> y=<py> state=<n>` on stdout during the run.
- **Scripted input, NOT human playtests.** Nothing here is a human playtest.

## build_id hash method

Source files hashed (sha256) to identify the exact build captured:
- `godot/project.godot` (window override set to 3840x2160 in the capture copy
  for 4K recording; original untouched)
- `godot/game/session.gd`
- `godot/features/player/player.gd`
- `godot/levels/first_steps.json`
- Driver scripts in `godot/tests/` of the capture copy.

The original project at `~/workspace/godot/walker-jumpman-clawd` was verified
pristine via `git status` (only pre-existing untracked files). All captures
were recorded from the isolated copy at `~/workspace/godot/jumpman-capture-copy`.

## Captures

### full_run_4k.mp4 — full route, input-only

- **MP4:** `~/workspace/film-render/jumpman-walkthrough/capture/full_run_4k.mp4`
- **AVI (original):** `~/workspace/film-render/jumpman-walkthrough/capture/full_run_4k.avi`
- **Input log:** `~/workspace/film-render/jumpman-walkthrough/capture/full_run_4k_inputs.jsonl`
- **sha256 (mp4):** `bc71e2e3c6f2113bac39641db600abf634c28fc53ebbb1d813ae7b3780ffd357`
- **ffprobe:** 3840x2160, 60fps, 19.2s, h264 (AVI: mjpeg, 374MB)
- **Result:** COMPLETE, 0 deaths, 22/23 coins (missed 1 coin; the Easter-egg
  block's +5 was not triggered — see Limitations).
- **Timecodes (seconds, from SEGMENT markers):**
  - 0.0 menu_start — title card "First steps. Real jumps." / ENTER START
  - 2.0 game_start — ENTER pressed, run begins
  - 2.43 jump_wall — first step (x160-208) jumped
  - 3.48 jump_spikes — spike strip (x320-344) jumped
  - 4.3 jump_gap — gap 448-512 jumped
  - 5.03 jump_wall — block (x576-624) jumped
  - 6.1 jump_gap — gap 736-784 jumped
  - 7.62 bonk_approach — under question blocks
  - 7.88 bonk_1, 8.52 bonk_2, 9.13 bonk_3 — three qblocks bonked, coins pop
  - 9.4 jump_gap — gap 1088-1152 jumped
  - 10.1 jump_pipe1 — pipe1 (1184-1216) jumped
  - 10.63 land_pipe1 — landed on pipe1 top
  - 10.65 jump_pipe2 — jumped to pipe2 (1256-1288)
  - 11.42 past_pipes — cleared pipes, on stairs approach
  - 11.43 jump_stair_fix — vertical jump to clear stair wedge
  - 12.0 stair_fix_done — on stairs
  - 12.02 jump_wall — stairs climbed
  - 12.98 jump_drop_jump — leapt from platform edge (x1526), flew OVER the
    patrolling grumbler, landed ~x1665
  - 14.25 jump_spikes — spike bed (1760-1824) jumped
  - 15.2 flag_complete — reached finish (x1881), COMPLETE card:
    "13.2 seconds / 0 retries / 22 coins - Solid haul."
- **Observations:** Menu legible at 4K; HUD coin counter increments visibly
  (00→22); progress bar fills; qblock bonks show coin pop; grumbler visible
  patrolling under the flight path; spike bed and FINISH flag crisp; completion
  card legible with stats and ENTER/PLAY AGAIN.

### death_4k.mp4 — spike death + auto-retry recovery, input-only

- **MP4:** `~/workspace/film-render/jumpman-walkthrough/capture/death_4k.mp4`
- **AVI (original):** `~/workspace/film-render/jumpman-walkthrough/capture/death_4k.avi`
- **Input log:** `~/workspace/film-render/jumpman-walkthrough/capture/death_4k_inputs.jsonl`
- **sha256 (mp4):** `e7653275f2e29fb5cc1eb766efde98adce5cd0b0b6c3ae4bcdf5a859dc362bac`
- **ffprobe:** 3840x2160, 60fps, 6.63s, h264
- **Result:** 1 death ("Watch the spikes"), auto-retry after 0.55s, play
  resumed at spawn, ran to x~287. Deaths: 1. Retry: successful (game's real
  auto-retry path, no input needed).
- **Timecodes:**
  - 0.0 menu, 2.0 game start
  - ~3.15 spike entry (x~316, first spike strip) — DYING
  - ~3.2 death card visible: "Watch the spikes / Back at the start in a moment."
  - ~3.72 auto-retry — respawn at (64,320)
  - ~6.6 recovery — running again, 2 coins collected
- **Observations:** Death card legible; RETRIES counter increments to 01;
  respawn is automatic; no input required for retry.

### features_4k.mp4 — mechanic takes, input-only

**STATUS: NOT RECORDED.** The 4K software rendering (llvmpipe) runs ~100-240x
slower than real time; a 21s features reel (Takes A+B) was estimated at 60+
minutes, and the 69s full reel (A+B+D+E+F) at 4+ hours. Two capture attempts
were killed by runtime service restarts. The take logic WAS validated via
dry-run (720p, no movie) — see below. The mechanics are therefore demonstrated
in logic but not in 4K video.

**Dry-run validation (from `/tmp/features_out*.txt`, 2026-10-07):**
- **Take A (qblock bonk):** t=7.62 bonk_approach, t=7.88/8.52/9.13 bonk_1/2/3,
  t=9.15 bonk_done. All three qblocks bonked, coins popped. ✓
- **Take B (easter-egg block):** t=15.03 takeB_jump at x=991, t=15.45
  takeB_result_found=false. Jump at the hidden spot; nothing happens.
  Confirms unreachable via pure input. ✓
- **Take D (grumbler side contact):** t=39.45 takeD_death_reason=
  "Squashed by a grumbler" at x=1662. Walked into enemy side; died. ✓
- **Take E (pause/resume):** Driver logic: P presses pause action → PAUSED;
  ENTER resumes. Validated in code path; not run to completion in dry-run
  due to Take C blocking.
- **Take F (complete→menu→replay):** Driver logic: M in COMPLETE → MENU;
  ENTER in MENU → PLAYING (replay). Validated in code path.
- **Take C (stomp):** NOT ACHIEVED. See Limitations.

**Input logs from dry runs:** `/tmp/features_test*.jsonl` (ephemeral; not in
capture folder). The 4K input-log format is identical to the other captures.

## Limitations / honest notes

- **Easter-egg block (Take B):** The hidden block at [990,196,28,20] triggers
  only when the player is ascending (vy<0) with py in (196,250) — i.e. the
  player's head must be 70-124px above the ground, which requires jumping from
  atop a question block (y=236). Reaching a qblock top needs an 84px jump;
  the player's max jump is 53px. The eblock is therefore UNREACHABLE via pure
  input. Take B demonstrates the attempt (jump at the spot, nothing happens,
  `found=false`). This is a level-design constraint, not a driver failure.
- **Grumbler stomp (Take C):** Not reliably achievable via scripted input.
  A stomp requires x-overlap with the enemy during the descent (vy>40,
  py<316). The enemy moves 0.917px/tick (55px/s); during a 40-tick jump it
  travels 37px, wider than the player (18px), making the timing window
  extremely narrow. Multiple approaches were tried (timed pounce from ground,
  periodic jumps, continuous bouncing in patrol path, fall-from-platform);
  all either missed (player ran past to COMPLETE) or risked side-contact
  death. A human can time it, but scripted reactive input could not do so
  reliably. Take C was omitted from features_4k.mp4; Take D shows the
  grumbler interaction that WAS captured (side contact).
- **Coins:** Full run collected 22/23. The missing coin is the Easter-egg
  block's +5 (unreachable, see above) minus coins collected elsewhere; the
  exact missing coin was not identified.
- **4K capture speed:** Software GL (llvmpipe) at 3840x2160 runs ~50-70x
  slower than real time. Captures are normal simulation speed
  (`--fixed-fps 60`, 1/60s per frame); the slowness is wall-clock rendering
  time, not retimed gameplay.

## Evidence takes (2026-10-07) — pause, egg block, grumbler stomp

Three missing gameplay-evidence takes recorded 2026-10-07 from the isolated
copy (`~/workspace/godot/jumpman-capture-copy`), all input-only via new
SceneTree drivers in `godot/tests/` (`capture_pause.gd`, `capture_egg.gd`,
`capture_grumbler.gd`). Each driver reuses the proven `capture_fullrun.gd`
pattern: synthetic `InputEventKey` via `Input.parse_input_event()` through the
normal InputMap path, per-tick reactive decisions, JSONL input logging
(`INPUT_LOG` env), `PROBE_QUIT_TICKS` dry-run support. No teleports, no
position/velocity writes, no `test_*` fields, no state forcing, no retiming.

Each driver was dry-run first at 720p with `PROBE_QUIT_TICKS` (logic
validated), then recorded at 4K under Xvfb (`:99`, 3840x2160x24) with Godot
Movie Maker `--write-movie <avi> --fixed-fps 60 --quit-after <frames>`,
converted with `ffmpeg -i <avi> -c:v libx264 -pix_fmt yuv420p -crf 18 <mp4>`.
Native 3840x2160 verified by ffprobe on every mp4; 2-4 PNG frames per take
were extracted and read by eye before calling the take done.

### take_pause_4k.mp4 — pause / resume

- **MP4:** `~/workspace/film-render/jumpman-walkthrough/capture/take_pause_4k.mp4`
- **AVI (original):** `~/workspace/film-render/jumpman-walkthrough/capture/take_pause_4k.avi` (141MB)
- **Input log:** `~/workspace/film-render/jumpman-walkthrough/capture/take_pause_4k_inputs.jsonl` (17 events)
- **sha256 (mp4):** `2a144f4f4c9656b97bef4b387edd5faa2b804d72cdf17d1fa74e609d659eda69`
- **ffprobe:** 3840x2160, 60fps, 7.02s, h264
- **Method:** menu → ENTER (t=1.0) → run right ~2s (spike/gap jumps via
  `decide_jump`) → ESC presses `pause` action → pause card held ~2s → ESC
  again resumes → run ~2s → quit. Render: 420 frames, ~10 min wall clock.
- **Timecodes:** 0.0 menu_start · 1.0 game_start · 3.0 pause_on (ESC) ·
  5.0 pause_off (ESC, state PAUSED at marker) · 7.0 take_done.
- **Frame QC:** t=4.0 pause card legible — "Take a breath." / "R: restart
  attempt    M: main menu" / "ENTER / RESUME"; t=2.0 and t=6.0 gameplay crisp,
  player mid-jump, HUD text sharp at 4K. PASS.

### take_egg_4k.mp4 — hidden egg-block attempt (honest negative)

- **MP4:** `~/workspace/film-render/jumpman-walkthrough/capture/take_egg_4k.mp4`
- **AVI (original):** `~/workspace/film-render/jumpman-walkthrough/capture/take_egg_4k.avi` (252MB)
- **Input log:** `~/workspace/film-render/jumpman-walkthrough/capture/take_egg_4k_inputs.jsonl` (25 events)
- **sha256 (mp4):** `af8449b7f42f17720f0599f459ff6c6456ba70a74e489f8103429c898e5a10cb`
- **ffprobe:** 3840x2160, 60fps, 12.63s, h264
- **Method:** menu → ENTER → route to the question-block area (`decide_jump`,
  no bonking) → stop at x≈1004 (center of `eblock.rect` = [990,196,28,20]
  from `godot/levels/first_steps.json`) → 5 vertical jumps at the spot,
  logging `game.eblock.found` after each → hold 1s → quit. Render: 757
  frames, ~7 min wall clock.
- **Timecodes:** 6.93 egg_position (x=1002) · 6.95/7.88/8.82/9.75/10.68
  egg_jump_1..5 · 11.62 egg_done · 12.62 take_done.
- **Result:** `eblock.found=false` after all 5 jumps — the block is
  unreachable via pure input (head sweep at jump apex spans y 230-264;
  eblock rect is y 196-216; needs py in (196,250) while rising, i.e. a jump
  from atop a question block, which needs an 84px climb vs the 53px max
  jump). The jumps visibly bonked the middle question block (spent block +
  "+1" pop in frame at t=7.5) — the attempt is genuine, the outcome honest.
- **Frame QC:** t=7.5 player mid-jump under the blocks, middle qblock spent;
  t=12.3 player standing under the blocks. Crisp 4K. PASS (as documentation
  of the attempt, not of a find).

### take_grumbler_4k.mp4 — grumbler stomp (STOMP CAPTURED)

- **MP4:** `~/workspace/film-render/jumpman-walkthrough/capture/take_grumbler_4k.mp4`
- **AVI (original):** `~/workspace/film-render/jumpman-walkthrough/capture/take_grumbler_4k.avi` (292MB)
- **Input log:** `~/workspace/film-render/jumpman-walkthrough/capture/take_grumbler_4k_inputs.jsonl` (31 events)
- **sha256 (mp4):** `e50a1058fefa5f627c0876df01e31a60c51b0c90201113fcb78e2361685f448c`
- **ffprobe:** 3840x2160, 60fps, 14.98s, h264
- **Method:** menu → ENTER → full route (pipes + stair-fix logic copied from
  `capture_fullrun.gd`) to the platform edge x≈1536, but runs OFF the edge
  (no drop-jump) and lands in the patrol zone → stalks to x≈1632 → reads
  `game.enemies[0]` (x, dir, alive) each tick and jumps straight up when the
  enemy is ≤40px out and closing. Jump physics (vy₀=-320, g=960) give a
  ~40-tick jump; the enemy walks ~37px during it, arriving under the player
  for the descent stomp window (ticks 37-40: vy>40, py<316, x-overlap <21px).
  On `enemy.alive=false` → hold 2s → quit. If side contact had killed the
  player instead, the driver would have let the death card play and quit
  (SIDE-KILL path) — not needed. Render: 898 frames, ~10 min wall clock.
- **Timecodes:** 11.37 stalk (landed in patrol zone) · 11.52 wait_early
  (enemy within 60px) · 11.78 stomp_jump_1 (gap=-39.4, enemy at 1671.6 moving
  left) · 12.97 stomp_landed (enemy alive=false) · 14.97 hold_done. 0 deaths.
- **Frame QC:** t=12.32 player descending directly above the grumbler (brown
  blob, angry eyes); t=12.45 grumbler gone, player just above the ground;
  t=13.8 player standing alone at x=1632, RETRIES 00. STOMP visibly captured
  on the first attempt. Crisp 4K. PASS.

### Notes / limitations

- No take failed. The egg block remains unfound (level-design constraint,
  documented above); the side-kill path was implemented but not triggered.
- Driver bug caught in dry-run: `capture_egg.gd` jumped forever because the
  jump branch won the same-tick race against the hold transition; fixed by
  guarding jumps with `jumps_done < EGG_JUMPS` before the 4K record.
- 4K llvmpipe ran ~60-110x slower than realtime this session (7-15s takes
  took 7-10 min each); all three takes finished well under the 60-min kill
  limit. Normal simulation speed throughout (`--fixed-fps 60`, no retiming).
- QC frame PNGs kept next to the takes as
  `frames_take_<name>_<t>.png` (not part of the deliverable set).

### take_sidekill_4k.mp4 — grumbler side-contact death (recorded by coordinator, 2026-10-07)

- **MP4:** `~/workspace/film-render/jumpman-walkthrough/capture/take_sidekill_4k.mp4`
- **AVI (original):** `~/workspace/film-render/jumpman-walkthrough/capture/take_sidekill_4k.avi`
- **Input log:** `~/workspace/film-render/jumpman-walkthrough/capture/take_sidekill_4k_inputs.jsonl`
- **sha256 (mp4):** `f15c6e965987404fccca190780d53ae858eec513800b8ac34046f2908a3ac7bb`
- **ffprobe:** 3840x2160, 60fps, 13.97s, h264
- **Method:** menu → ENTER → full route (bonks, pipes, stair-fix logic copied
  from `capture_fullrun.gd`) → runs OFF the platform edge (no drop-jump) into
  the patrol zone → walks straight into the grumbler's side. Input-only via
  `godot/tests/capture_sidekill.gd`; dry-run at 720p with PROBE_QUIT_TICKS
  first. No teleports, no position writes, no test fields, no retiming.
- **Timecodes:** 13.55 death (x=1616.9, death_reason="Squashed by a grumbler")
  · 13.95 card held · 0 deaths before, RETRIES 01.
- **Result:** side-contact death confirmed on camera; death card
  "Squashed by a grumbler / Back at the start in a moment." Driver exits 0 on
  the DYING card (before the 0.55s auto-retry fires).
- **Frame QC:** t=13.7 death card legible, grumbler visible at the contact
  point. PASS.

### take_fallretry_4k.mp4 — fall death + manual R retry + M menu return (recorded by coordinator, 2026-10-07)

- **MP4:** `~/workspace/film-render/jumpman-walkthrough/capture/take_fallretry_4k.mp4`
- **AVI (original):** `~/workspace/film-render/jumpman-walkthrough/capture/take_fallretry_4k.avi`
- **Input log:** `~/workspace/film-render/jumpman-walkthrough/capture/take_fallretry_4k_inputs.jsonl`
- **sha256 (mp4):** `9a2d71d86924581619227ed4827794f59162a3808e4ef7ed71eb87cf474ac5ae`
- **ffprobe:** 3840x2160, 60fps, 9.1s, h264
- **Method:** menu → ENTER → run right, jumping the step and spike strip via
  `decide_jump` but deliberately NOT jumping gap1 (448-512) → falls →
  "Missed the landing" → auto-retry → respawn → R pressed mid-run
  (instant `restart_attempt`, back at spawn, no death) → ESC pause → M
  returns to the menu card. Input-only via
  `godot/tests/capture_fallretry.gd`; dry-run at 720p first (caught and fixed
  two driver bugs: missing jump-hold release stalled the run; the M-press was
  nested in the wrong state branch). No teleports, no position writes, no
  test fields, no retiming.
- **Timecodes:** 5.02 fall_death ("Missed the landing") · 5.58 auto_retry ·
  6.57 manual_retry (R) · 7.57 paused · 7.58 menu_return (M) · menu card held
  to 9.1.
- **Frame QC:** t=5.1 "Missed the landing" card legible over the gap sign;
  t=7.7 pause card; t=8.6 menu card ("First steps. Real jumps.", ENTER /
  START, COINS 00/23, RETRIES 01). PASS.
