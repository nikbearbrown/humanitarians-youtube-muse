# SHOTLIST — Walker Jumpman: Extended Walkthrough

Per implemented feature: planned shot, source capture, what must be visible
on screen (precondition → input → outcome), run segment, and timecode.
**All timecodes are TO-FILL** — another worker measures them from the new
captures (`full_run_4k.mp4`, `death_4k.mp4`).

Capture contents (from the capture scripts):
- `full_run_4k.mp4` — expected: menu card → scripted full route (reactive
  driver: gap/wall raycasts, spike proximity, timed grumbler wait-and-jump)
  → completion card. The driver collects ~20 world coins, 0 block payouts,
  0 egg, 0 stomps — it jumps *over* the grumbler and *under* the qblocks.
- `death_4k.mp4` — expected: run starts → player walks into the first spike
  bed (no jump) → death card → auto-retry → running again from spawn.

Shots marked VERIFY may not exist in the captures; the driver never bonks,
never strikes the egg, never stomps, never pauses. The 12 automated probes in
`godot/tests/playtest_extended.gd` prove those mechanics — footage needs
dedicated takes (probe patterns are reusable as take drivers).

---

## Menu, HUD, player

**S01 — F_MENU: main menu card**
Source: `full_run_4k.mp4` (VERIFY — present if the capture starts at MENU)
Visible: title card "First steps. Real jumps." + "ENTER / START" button →
ENTER pressed (or button clicked) → card clears, Clawd at spawn, timer starts.
Segment: early (first frames). Timecode: TO-FILL.

**S02 — F_HUD: coin counter, progress bar, timer**
Source: `full_run_4k.mp4`
Visible: top bar "WALKER / JUMPMAN", controls line, "COINS nn/23" incrementing
on pickup; teal progress bar extending left→right; footer "No lives. Just
another try." + RETRIES/timer. Segment: throughout. Timecode: TO-FILL.

**S03 — F_PLAYER_MOVE / F_YARD: run and jump in the tutorial yard**
Source: `full_run_4k.mp4`
Visible: Clawd running right through x 0–960, world labels "01 / GET MOVING"
and "02 / MIND THE GAP", jump arcs clearing the 64px and 48px gaps, two steps.
Segment: early. Timecode: TO-FILL.

**S04 — F_CONTROLS: bindings on screen**
Source: `full_run_4k.mp4` + narration overlay
Visible: HUD controls line ("A/D or arrows: move · Space: jump · R: retry ·
Esc: pause") while the driver moves (D/right), jumps (Space), and would retry
(R). Full binding list lives in `session.gd` `_setup_input`; not all bindings
are exercised on camera. Segment: early. Timecode: TO-FILL.

## Coins and blocks

**S05 — F_COINS: coin pickup**
Source: `full_run_4k.mp4`
Visible: gold coin arc ahead → player touches coin → coin vanishes, HUD
counter increments by 1. Segment: early (tutorial-yard arcs). Timecode: TO-FILL.

**S06 — F_QBLOCKS + F_BONK: question-block bonk** (VERIFY)
Source: `full_run_4k.mp4` — expected ABSENT (driver runs under the blocks;
see FACTCHECK.md). Needs a dedicated bonk take if the film shows it.
Visible: player under an orange "?" block (x 960–1048) → jump, head strikes
from below → block dims, "+1" float-up animates, coin counter +1.
Segment: early-mid. Timecode: TO-FILL.

**S07 — F_EASTER: hidden block reveal** (VERIFY)
Source: dedicated take required — expected ABSENT from both captures.
Probe pattern: `playtest_extended.gd` Mechanic 3 (jump from atop the middle
qblock at x≈1004).
Visible: empty air above the qblocks → rising jump → faint block appears,
toast "EASTER EGG: Clawd's midnight snack! +5 coins", counter +5.
Segment: n/a (dedicated). Timecode: TO-FILL.

## Enemy

**S08 — F_GRUMBLER: patrol**
Source: `full_run_4k.mp4`
Visible: brown grumbler with eyes/angry brows patrolling x 1620–1700 →
driver holds at x≈1580–1620, waits for the enemy mid-patrol moving left,
then jumps clean over it. Segment: mid-late. Timecode: TO-FILL.

**S09 — F_STOMP: stomp kill** (VERIFY)
Source: dedicated take required — the driver never stomps (it jumps over).
Probe pattern: `playtest_extended.gd` Mechanic 4 (drop onto the grumbler
from above).
Visible: player falling onto the grumbler → enemy vanishes, player bounces
up (−240 px/s), run continues, coin counter unchanged. Segment: n/a
(dedicated). Timecode: TO-FILL.

**S10 — F_ENEMY_DAMAGE: side contact kills** (VERIFY)
Source: dedicated take required — `death_4k.mp4` covers a *spike* death, not
an enemy death. Probe pattern: `playtest_extended.gd` Mechanic 5.
Visible: player walks into the grumbler's side → death card reads "Squashed
by a grumbler". Segment: n/a (dedicated). Timecode: TO-FILL.

## Hazards, death, retry

**S11 — F_SPIKES: spike beds**
Source: `full_run_4k.mp4` (mid: 40px bed between the pipes at x 1216;
late: 64px bed at x 1760, cleared in one jump) and `death_4k.mp4` (24px bed
at x 320, walked into deliberately).
Visible: red triangular beds → contact = death (route) or cleared by jump
(route, late bed). Segment: mid + late. Timecode: TO-FILL.

**S12 — F_DEATHCARD + F_RETRY_AUTO: death and auto-retry**
Source: `death_4k.mp4`
Visible: spike contact → card "Watch the spikes" + "Back at the start in a
moment." → ~0.55 s later player is back at spawn running, RETRIES 01.
Segment: all of `death_4k.mp4`. Timecode: TO-FILL.

**S13 — F_FALL: fall death** — no capture planned (driver never falls;
verified in code via `fall_y = 430`). Mention in narration only, or stage a
take. **S14 — F_RETRY_MANUAL (R key) / F_PAUSE (Esc)** — no capture planned;
keyboard probes in `test_keyboard.gd` verify them. Mention only, or stage
takes.

## Finish and ranking

**S15 — F_FINISH: flag touch and completion**
Source: `full_run_4k.mp4`
Visible: player reaches the green flag (x 1884) → "Course complete." card
with "ENTER / PLAY AGAIN". Segment: late (final frames). Timecode: TO-FILL.

**S16 — F_RANK: coin ranking**
Source: `full_run_4k.mp4`
Visible: completion-card detail line, e.g. "12.8 seconds / 0 retries /
20 coins - Solid haul." (values from the 720p capture — re-verify on 4K).
Segment: late. Timecode: TO-FILL.

## Terrain features

**S17 — F_PIPES: pipe hop with spikes between**
Source: `full_run_4k.mp4`
Visible: two 32×40 pipe solids (teal rims) at x 1184 and 1256, 40px spike bed
between → player hops rim to rim without touching the bed. Segment: mid.
Timecode: TO-FILL.

**S18 — F_STAIRS: staircase and high platform**
Source: `full_run_4k.mp4`
Visible: 4-step staircase (x 1312–1440) → 96px high platform → safe drop off
the far edge (x 1536–1584 gap). Segment: mid. Timecode: TO-FILL.

**S19 — F_GAPS: gap jumps**
Source: `full_run_4k.mp4`
Visible: committed jumps over the 64px extension gap (x 1088–1152, just past
the question blocks) and the tutorial-yard gaps. Segment: early + mid.
Timecode: TO-FILL.

---

## Shots with no planned capture (narration-only unless takes are staged)

F_FALL (fall death), F_RETRY_MANUAL (R restart), F_PAUSE (Esc + focus-loss),
F_ENEMY_DAMAGE (grumbler side-kill card), F_STOMP, F_QBLOCKS bonk, F_EASTER
reveal. All are proven by `playtest_extended.gd` probes; footage requires
dedicated takes reusing those probe patterns.
