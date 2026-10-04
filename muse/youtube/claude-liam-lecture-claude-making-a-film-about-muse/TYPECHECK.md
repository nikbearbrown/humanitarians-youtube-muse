# TYPECHECK.md — GATE T

Reel: `claude-liam-lecture-claude-making-a-film-about-muse`  |  Checked: 2026-10-04T12:58  |  Overall: PASS  |  Beats checked: 36  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

> **§8.10 REDUNDANCY (advisory — does not block cut):**
> Narration should DISCUSS on-screen text, not recite it.
> Exception: LITERAL beats (viewer types/copies/runs the text) are exempt.

> - §8.10 [BVDT] narration recites the card (0.94) — discuss it, don't read it

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| BIDEA | bookend | light | min-size §8.1: min text-run height 61px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| BDEFS | bookend | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B01 | manim | light | min-size §8.1: min text-run height 55px >= floor 41px | PASS | — |
| B02 | manim | light | min-size §8.1: min text-run height 46px >= floor 41px | PASS | — |
| B03 | manim | light | min-size §8.1: min text-run height 47px >= floor 41px | PASS | — |
| B04 | manim | light | min-size §8.1: min text-run height 48px >= floor 41px | PASS | — |
| B05 | manim | light | min-size §8.1: min text-run height 43px >= floor 41px | PASS | — |
| B06 | manim | light | min-size §8.1: min text-run height 70px >= floor 41px | PASS | — |
| B07 | manim | light | min-size §8.1: min text-run height 59px >= floor 41px | PASS | — |
| B08 | manim | light | min-size §8.1: min text-run height 116px >= floor 41px | PASS | — |
| B24 | manim | light | min-size §8.1: min text-run height 116px >= floor 41px | PASS | — |
| B09 | manim | light | min-size §8.1: min text-run height 43px >= floor 41px | PASS | — |
| B10 | manim | light | min-size §8.1: min text-run height 70px >= floor 41px | PASS | — |
| B11 | manim | light | min-size §8.1: min text-run height 63px >= floor 41px | PASS | — |
| B25 | manim | light | min-size §8.1: min text-run height 42px >= floor 41px | PASS | — |
| B26 | manim | light | min-size §8.1: min text-run height 43px >= floor 41px | PASS | — |
| B27 | manim | light | min-size §8.1: min text-run height 73px >= floor 41px | PASS | — |
| B28 | manim | light | min-size §8.1: min text-run height 73px >= floor 41px | PASS | — |
| B29 | manim | light | min-size §8.1: min text-run height 42px >= floor 41px | PASS | — |
| B12 | manim | light | min-size §8.1: min text-run height 49px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B13 | manim | light | min-size §8.1: min text-run height 74px >= floor 41px | PASS | — |
| B30 | manim | light | min-size §8.1: min text-run height 46px >= floor 41px | PASS | — |
| B14 | manim | light | min-size §8.1: min text-run height 74px >= floor 41px | PASS | — |
| B15 | manim | light | min-size §8.1: min text-run height 45px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B16 | manim | light | min-size §8.1: min text-run height 43px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B17 | manim | light | min-size §8.1: min text-run height 63px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B18 | manim | light | min-size §8.1: min text-run height 195px >= floor 41px | PASS | — |
| B19 | manim | light | min-size §8.1: min text-run height 47px >= floor 41px | PASS | — |
| B20 | manim | light | min-size §8.1: min text-run height 116px >= floor 41px | PASS | — |
| B31 | manim | light | min-size §8.1: min text-run height 43px >= floor 41px | PASS | — |
| B21 | manim | light | min-size §8.1: min text-run height 43px >= floor 41px | PASS | — |
| B22 | manim | light | min-size §8.1: min text-run height 44px >= floor 41px | PASS | — |
| B23 | manim | light | min-size §8.1: min text-run height 41px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| BVDT | bookend | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| BHTF | bookend | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| BOUT | bookend | light | min-size §8.1: min text-run height 64px >= floor 41px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 1 | 0 |
| min-size §8.1 | 36 | 0 |
| overflow §8.2 | 36 | 0 |
| contrast §8.3 | 36 | 0 |
| contrast-local §8.3b | 36 | 0 |
| bbox-overlap §8.6b | 36 | 0 |
| card-clip §8.13 | 36 | 0 |
| kerning §8.4 | 31 | 0 |
| redundancy §8.10 (advisory) | 1 | 1 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
