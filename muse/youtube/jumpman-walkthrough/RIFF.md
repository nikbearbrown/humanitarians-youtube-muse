# RIFF.md — Liam's commentary notes (inspected captures, 2026-10-06/07)

Voice: Liam, in for Bear. Teardown register. Every note below comes from
watching the actual 4K captures frame by frame, cross-checked against
`godot/game/session.gd`. Nothing here is a human playtest — all runs are
scripted input through the normal Input path.

---

## B02 — full_run_4k, 0.0–7.0s — menu, start, tutorial yard

**On screen:** The menu card reads "First steps. Real jumps." over a dimmed
level view: "Gaps, spikes, blocks, a grumbler. Reach the flag. One jump. No
double jump. Unlimited retries." ENTER / START button, controls row (A/D or
arrows, Space, R retry, Esc pause), COINS 00/23, RETRIES 00, "No lives. Just
another try." ENTER starts the run at t=2.0. The yard: coin arcs, a single
step (t=2.43), the first spike bed cleared with a short hop (t=3.48), two
gaps (t=4.3, 6.1).

**Mechanism:** `session.gd` runs a state machine (MENU → PLAYING on the
`confirm` action). The yard geometry is unchanged from the original 960px
level — same entry values, finish moved from x=916 to x=1884.

**Trade-off:** The whole game is taught in one card — no tutorial walls, no
popups mid-run. The risk is the usual one: players who don't read cards hit
the first spike blind. The retry is half a second, so the tuition is cheap.

## B03 — full_run_4k, 7.0–13.0s — question blocks, pipes, stairs

**On screen:** Three question blocks at t=7.88 / 8.52 / 9.13 — each bonk
pops a coin with a "+1" tick and the HUD counter climbs (05/23 visible
mid-sequence). The sign reads "03 / BONK THE BLOCKS — Jump into them. Trust
me." Then gap three (t=9.4), the green pipes (t=10.1, 10.65 — hop on, hop
across, spikes between), the staircase fix (t=11.43) and climb (t=12.0) to
the high platform.

**Mechanism:** `_check_bonks()` sweeps a head rect while the player is
rising (`velocity.y < -50`) — bonking is about jumping *into* the block, not
touching it. Used blocks flip to the spent gray sprite.

**Trade-off:** The head-sweep is generous — near misses still pay out, which
feels good. But one jump does everything here: the 53px max jump height is
the level's whole difficulty budget. Every obstacle is a variation on "jump
exactly this far," which keeps controls trivial and caps design ambition.

## B04 — full_run_4k, 13.0–19.2s — grumbler, spike bed, finish

**On screen:** The grumbler patrols its beat (t=12.98) — brown, angry eyes,
55px/s between x=1620 and x=1700. This run jumps clean over it off the
platform edge and lands past. The 64-pixel spike bed (t=14.25) takes one
committed jump. Flag at t=15.2: "Course complete." card — "13.2 seconds /
0 retries / 22 coins - Solid haul." ENTER / PLAY AGAIN.

**Mechanism:** `_check_enemies()` stomps only when the player is falling
fast (`velocity.y > 40`) and above the enemy's top; anything else is "Squashed
by a grumbler." The completion rank comes from `coin_rank()` on the HUD
count — note the count includes bonk payouts, so "Solid haul." can fire
without every world coin.

**Trade-off:** Jumping *over* the grumbler is the safe line; stomping is the
greedy line — same enemy, two risk profiles, player's choice. The spike bed
is pure commitment: 64px at this jump's range leaves no room for a
correction hop, so it reads as the level's exam question.

## B05 — death_4k, 0.0–6.63s — spike death and auto-retry

**On screen:** From spawn, straight into the first spikes — no jump
(t≈3.15). Death card: "Watch the spikes / Back at the start in a moment."
RETRIES ticks to 01. At ~0.55s the run auto-retries with no input; the
player is back at spawn running with 2 coins by t=6.6.

**Mechanism:** Hazards are Area2Ds; overlap while PLAYING (after the
contact-settle grace) sets fatal, shows the card, and `retry_remaining`
counts down to `restart_attempt()`.

**Trade-off:** No lives, instant retry — the design buys experimentation and
spends tension. Dying costs half a second and nothing else, so the game
never punishes curiosity. A roguelike this is not, and it knows it.

## B06 — feature takes (pause / egg / grumbler)

**Pause (take_pause_4k):** ESC freezes the sim mid-run; the pause card holds;
ESC (or ENTER) resumes exactly where it stopped. Precondition → input →
outcome, no state lost. The trade-off of a hard freeze: trivially correct,
zero drama.

**Egg (take_egg_4k):** The hidden block is real — `eblock.rect` exists in
the level data and `_check_bonks()` arms it on a rising head-sweep. But the
spot needs an 84px climb from the question-block tops and the jump peaks at
53px. Jumping the exact spot finds nothing. This is a genuine defect, not a
secret: a bonus no legitimate play can reach. (Verdict covers it.)

**Grumbler (take_grumbler_4k):** Stomp = falling fast onto the enemy's top;
side contact = "Squashed by a grumbler." Same enemy, two outcomes, decided
by your vertical velocity at contact. High risk, high clarity.

## What the riffs deliberately don't do

No claims about fun, fairness, or feel — the human judges those, and no
human has played this. No invented mechanics: moving platforms, checkpoints,
double jump, and lives are planned or absent, never implied present.
