# Guest Speaker Series — Event Templates

Editable templates for Northeastern **Guest Speaker Series** event graphics,
built from the *Fearless Genius* (Doug Menuez, Oct 10 2026) poster.

## Sizes

| File base | Size | Use |
|---|---|---|
| `poster-letter` | 8.5 × 11 in | Print flyer |
| `poster-16x9` | 1920 × 1080 | YouTube, X/Twitter, LinkedIn, Facebook landscape |
| `poster-9x16` | 1080 × 1920 | Stories, Reels, TikTok, Shorts |
| `poster-4x5` | 1080 × 1350 | Instagram / Facebook portrait post |
| `poster-1x1` | 1080 × 1080 | Instagram / Facebook / LinkedIn square post |

## Formats

- **`template-*.html`** — editable web templates. Open in a browser, edit the
  text, print to PDF for the flyer.
- **`poster-*.svg`** — XML vector templates. Open directly in **Adobe
  Illustrator** — all text stays live and editable, grouped in labeled layers
  (`editable-*` vs `fixed-*`).
- **`poster-letter.idml`** — InDesign package (zipped XML) for the print
  flyer. Open directly in **Adobe InDesign** CS4+. Includes paragraph styles,
  Northeastern swatches, and the photo placed from `Links/`.
- **`doug-menuez.png`** — sample speaker photo referenced by the templates.

## What stays vs. what changes

**LOCKED — Northeastern / series branding (do not change):**
Northeastern red `#C12925` + black, the `N` lockup,
"Guest Speaker Series", "LIVE ON MICROSOFT TEAMS", "Open to the SEIS community",
red frame.

**EDITABLE — per event (marked `EDIT` in every file):**
photo, event title, description, date/time, speaker name + role,
QR code (link to Teams/registration), course/host line.

## Regenerating

Edit the `EDIT:` values at the top of `build_svg.py` / `build_idml.py` and run:

```bash
python3 build_svg.py    # rebuilds all 5 SVGs
python3 build_idml.py   # rebuilds poster-letter.idml
```

The HTML templates are edited by hand — search for `EDIT:`.
