# TYPECHECK.md — GATE T

Reel: `muse-account-registration`  |  Checked: 2026-10-04T20:28  |  Overall: **FAIL**  |  Beats checked: 15  |  FAILs: 2

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| BIDEA | ? | light | min-size §8.1: no text blobs detected — GATE T could not verify this frame; absence of mea… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| BDEFS | ? | light | min-size §8.1: min text-run height 54px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B01 | ? | light | min-size §8.1: no text-run blobs above noise threshold — the filter discarded every candid… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B02 | ? | light | min-size §8.1: min text-run height 62px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B03 | ? | light | min-size §8.1: min text-run height 61px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B04 | ? | light | min-size §8.1: min text-run height 65px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B05 | ? | light | min-size §8.1: min text-run height 58px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B06 | ? | light | min-size §8.1: min text-run height 43px >= floor 41px | PASS | — |
| B07 | ? | light | min-size §8.1: min text-run height 68px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B08 | ? | light | min-size §8.1: min text-run height 56px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B09 | ? | light | min-size §8.1: min text-run height 44px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B10 | ? | light | min-size §8.1: min text-run height 61px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| BVDT | ? | light | min-size §8.1: min text-run height 51px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| BHTF | ? | light | min-size §8.1: min text-run height 43px >= floor 41px | PASS | — |
| BOUT | ? | light | min-size §8.1: min text-run height 73px >= floor 41px (individual-char fallback at 2×) | PASS | — |

---

## Failures requiring action before cut

### BIDEA (?)
- **min-size §8.1**: no text blobs detected — GATE T could not verify this frame; absence of measurement is not compliance (SHOW-LESS.md)
- **Fix:** Increase font_size in scenes.py or Remotion component

### B01 (?)
- **min-size §8.1**: no text-run blobs above noise threshold — the filter discarded every candidate, which is what sub-floor type looks like; cannot verify (SHOW-LESS.md)
- **Fix:** Increase font_size in scenes.py or Remotion component

---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 0 | 0 |
| min-size §8.1 | 15 | 2 |
| overflow §8.2 | 15 | 0 |
| contrast §8.3 | 15 | 0 |
| contrast-local §8.3b | 15 | 0 |
| bbox-overlap §8.6b | 15 | 0 |
| card-clip §8.13 | 15 | 0 |
| kerning §8.4 | 15 | 0 |
| redundancy §8.10 (advisory) | 0 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
