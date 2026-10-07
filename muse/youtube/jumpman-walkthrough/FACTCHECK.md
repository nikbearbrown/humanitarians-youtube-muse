# FACTCHECK — Walker Jumpman: Extended Walkthrough

Every factual claim the film makes, with its source and a verdict.
Verdicts: **confirmed** (source or test evidence in hand) /
**needs-capture-confirmation** (must be verified against the new 4K captures) /
**unverifiable** (no source; the claim must change).

All line references are to `~/workspace/godot/walker-jumpman-clawd/` unless noted.
The film reel folder is `~/workspace/film-render/jumpman-walkthrough/`.

## Claims from the narration drafts (beat_sheet.json)

### B01 — What was built
| Claim | Source | Verdict |
|---|---|---|
| "Extended the First Steps level from 960 to 1920 pixels" | `godot/levels/first_steps.json` (`"width":1920`); commit `37448a1` | confirmed |
| "The original tutorial yard is untouched" | `first_steps.json`: yard solids/hazards/spawn entries carry identical values to the pre-extension JSON (verified via `git show 37448a1`). **Nuance:** "byte-for-byte" in FRICTIONAL.md means identical entry values — the file itself was reformatted (pretty-printed → single line) and the finish moved 916 → 1884. | confirmed with nuance — say "the yard's geometry is unchanged", not "the file is byte-identical" |
| "green pipes to hop across" | `first_steps.json` solids `[1184,280,32,40]` and `[1256,280,32,40]` flanking the 40px spike bed | confirmed |
| "a staircase leading to a high platform" | `first_steps.json` solids `[1312,304,32,16]`, `[1344,288,32,32]`, `[1376,272,32,48]`, `[1408,256,32,64]` + platform `[1440,256,96,16]` | confirmed |
| "three question blocks that pay out coins when you bonk them from below" | `first_steps.json` `qblocks` (3 entries); `session.gd` `_check_bonks` (+1 coin, one-shot); `playtest_extended.gd` Mechanic 2 probe | confirmed |
| "twenty-three coins placed in arcs and risky spots" | `first_steps.json` `coins` array — counted 23 entries | confirmed |
| "a patrolling grumbler you can stomp" | `first_steps.json` `enemies[0]` (x 1620–1700, 55 px/s); `session.gd` `_check_enemies` stomp branch; `playtest_extended.gd` Mechanic 4 probe | confirmed |
| "a sixty-four pixel spike bed guarding the finish" | `first_steps.json` hazards `[1760,304,64,16]`; finish at x 1884 | confirmed |
| "one invisible block hiding five bonus coins" | `first_steps.json` `eblock [990,196,28,20]`; `session.gd` `_check_bonks` (+5 coins, toast); `playtest_extended.gd` Mechanic 3 probe | confirmed |

### B02 — Coins, blocks, pipes
| Claim | Source | Verdict |
|---|---|---|
| "The driver collects coins in the tutorial yard — see the counter top right" | `godot/ui/hud.gd` draws `COINS nn/23` top right; route driver collects on touch | confirmed |
| "Under the question blocks — bonk, there's a coin" | **No source.** The reactive route driver (`godot/tests/route_driver.gd`) jumps only for gaps, walls at torso height, the grumbler wait, and spike proximity — it runs *under* the floating qblocks without striking them. The completed route collected 20 world coins, 0 block payouts, 0 egg (see B04). | **needs-capture-confirmation** — verify the new `full_run_4k.mp4` actually shows a bonk; if not, this line needs a dedicated bonk take or a reword |

### B03 — Stairs, platform, grumbler
| Claim | Source | Verdict |
|---|---|---|
| "Up the stairs, across the high platform" | `route_driver.gd` wall-ray jump trigger; FRICTIONAL.md 2026-10-06 entry | confirmed |
| "it patrols back and forth. The driver waits for it to turn, then jumps clean over" | `route_driver.gd` grumbler wait logic (waits at x 1580–1620 until the enemy is mid-patrol moving left, then jumps past); `session.gd` `_update_enemies` | confirmed |

### B04 — Spikes, finish
| Claim | Source | Verdict |
|---|---|---|
| "The spike bed — sixty-four pixels" | `first_steps.json` hazards `[1760,304,64,16]` | confirmed |
| "Twelve point eight seconds, twenty coins, zero retries" | **Confirmed from footage:** the completion card in the existing route capture (`capture/full_run.mp4`, final frame) reads "12.8 seconds / 0 retries / 20 coins - Solid haul." FRICTIONAL.md independently records the reactive driver finishing with 0 deaths, 20 coins. | confirmed (on the 720p capture — re-verify the numbers on `full_run_4k.mp4`; a new driver run may differ slightly) |

### B05 — Death and recovery
| Claim | Source | Verdict |
|---|---|---|
| "Walk into the spikes and you're back at the start in half a second" | `session.gd`: `retry_remaining = 0.55` in `resolve_contacts`; `_physics_process` DYING branch calls `restart_attempt()`. `capture/death.mp4` (2.55 s) shows the death card then auto-restart. "Half a second" is 0.55 s rounded. | confirmed |
| "No lives, just another try" | `godot/ui/hud.gd` footer text; GDD.md boundary ("no lives, checkpoints, health bars") | confirmed |

### B06 — Verdict
| Claim | Source | Verdict |
|---|---|---|
| "every mechanic — coins, blocks, stomp, spikes, finish" (works) | `godot/tests/playtest_extended.gd`: 12 mechanic probes, all pass (coin, qblock bonk, egg, stomp, side-kill, spikes, finish). BUT the route captures do **not** show the stomp, the bonk, or the egg — the driver jumps over the grumbler and under the blocks. | **needs-capture-confirmation** — true of the *tests*, not of the *route footage*. Either show dedicated takes or scope the claim to "every mechanic passes its probe" |
| "The reactive driver proves the course is beatable" | FRICTIONAL.md 2026-10-06 entry; commit `37448a1` message ("completes course, 0 deaths"); `route_driver.gd` | confirmed |
| "What's untested: human feel" | FRICTIONAL.md: "No human playtest occurred; scripted routes are not human playtests." AGENTS.md: never invent human playtests. | confirmed — keep this line exactly; it is the honest boundary |
| "The Easter egg is real" | `playtest_extended.gd` Mechanic 3 probe (hidden block found, +5 coins, toast armed) | confirmed |

### B00 / B08
| Claim | Source | Verdict |
|---|---|---|
| B00 reconstructed Walker prompt | Illustrative reconstruction (see PROMPTS.md). There is no saved historical transcript of this prompt; the real brief was Bear's "extend the level... have fun with it" (FRICTIONAL.md 2026-10-06). | confirmed as reconstruction — must stay labeled as such on screen |
| Engine: Godot 4.7 | `godot/project.godot` `config/features=PackedStringArray("4.7", "GL Compatibility")`; BUILD-REPORT.md records 4.7.2.stable | confirmed |
| "scripted input route, zero deaths" | FRICTIONAL.md 2026-10-06; commit `37448a1`; `route_driver.gd` uses `test_control` (scripted), never human input | confirmed |

## Flags and corrections

1. **Stale test comment.** `godot/tests/playtest_extended.gd` says "Full-route beatability is proven by tests/route_reactive.gd" — that file does not exist; the driver is `godot/tests/route_driver.gd`. Comment-only issue, not a game bug, but do not cite `route_reactive.gd` in narration or docs.
2. **"Coin master." rank is unreachable.** `session.gd` `coin_rank()`: the first branch (`coins_collected >= coins_total`, i.e. ≥ 23) catches every value ≥ 23, so the `>= 24 → "Coin master."` branch is dead code. Do not claim or show this rank. Related quirk: "PERFECT - every coin!" can trigger without all 23 world coins, because block (+1 each) and egg (+5) payouts count toward the same total. Observed in footage: 20 coins → "Solid haul."
3. **B01 audio mismatch.** The existing `mp3/b01_built.mp3` is ~14 s; the new BUILD-PROMPT.md text is written for ~25–30 s spoken. If the new text is adopted, the audio must be re-recorded (not this worker's call — flagging for the parent).
4. **Beat sheet still points at 720p captures.** `beat_sheet.json` clip references are `full_run.mp4`/`death.mp4` (1280×720). The new captures are `full_run_4k.mp4`/`death_4k.mp4`; clip ranges and timecodes are TO-FILL (see SHOTLIST.md).
5. **No human playtest exists for any claim.** All "it works / it's beatable" statements rest on scripted probes and the reactive driver (FRICTIONAL.md, AGENTS.md). The grumbler-plus-spike-bed difficulty is explicitly unjudged — "a human playtester should judge the difficulty" (FRICTIONAL.md 2026-10-06).
