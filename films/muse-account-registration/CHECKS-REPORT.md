# CHECKS-REPORT.md — How to register for a Muse account

Date: 2026-10-03. Checker:
`runtime/qc/static_scene_check.py` (render-free, per-class mode).

## Result: 13 clean · 0 warnings · 0 errors

| Scene | Result |
|-------|--------|
| M01_Bidea | clean |
| M02_Bdefs | clean |
| M03_B01Email | clean |
| M04_B02Card | clean |
| M05_B03Instagram | clean |
| M06_B04AgeCheck | clean |
| M07_B05Chain | clean |
| M08_B06MuseLogin | clean |
| M09_B07Code | clean |
| M10_B08Disclosure | clean |
| M11_B09In | clean |
| M12_B10Pattern | clean |
| M13_BvdtHtfOut | clean |

## Issues found and fixed (first pass)

1. M06_B04AgeCheck failed "shapes never change": one static card with
   text-only reveals. Fixed by adding a coin shape with the price and a
   refund badge with the refund line, revealed progressively.
2. M09_B07Code failed "shapes never change": all six code boxes appeared in
   a single play call (one shape-state). Fixed by revealing the boxes two at
   a time.

py_compile passes on scenes.py and make_sheet.py. beat_sheet.json validates
(15 beats, 10 body, totals 318 s).
