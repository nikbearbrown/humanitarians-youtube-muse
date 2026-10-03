# Frictional — Assignment 3

The process log for this assignment. The folder-level log across all of Professor Bear's work in this class is [`../FRICTIONAL.md`](../FRICTIONAL.md); this one stays on Assignment 3.

## Dated entry

**Date (mark retrospective entries):** 2026-09-26

**What I tried and expected:** Nothing built yet. The folder and its standard files were created during a live class demo so the work has somewhere to go. I first described the tool out loud and asked for it back: *"I'm looking to create a little agent which goes to greenhouse … downloads all their JSON and gets all of the education related teaching education related workshop related developer advocate related jobs and then posts them to a separate JSON file … Name exactly as they are in the existing data."* The expectation now on record is in [`PREDICTIONS.md`](PREDICTIONS.md): that the record count, not the plumbing, will be the hard part.

**What happened / what I found difficult or checked:**
- **The folder was built for the wrong assignment first.** The brief committed in this repo, `assignments/fall-2026/assignment-03.md`, is "Visual identity system" — design tokens and an SVG specimen. The live Assignment 3 is "Build Your Data Pipeline." I pasted the real one and everything here was rewritten around it. This is the second time the repo brief and the live assignment have disagreed; Assignment 2 had the same split. The repo brief needs replacing, and that is not done.
- **The executive summary was about the wrong thing.** The first version described the assignment, its provenance, and its status. I said: *"executive summary should be what the tool does … this in more notes and details than a real summary."* Rewritten to open with what `collect.py` does, what it refuses, and what it does not do, with status last.
- **My reading of the source requirement was close but not quite.** I said: *"I think I need to also do this for two similar companies … because I think it needs three data sources."* Three companies on Greenhouse is one source three times. Three different APIs — Greenhouse, Ashby, SmartRecruiters — is three, with three JSON shapes and three failure modes, and that collector already exists from last week. Companies get added *within* each source to reach the record count.
- **The count is the real problem.** The 2026-09-19 sweep found 643 postings across seven companies and the education/advocate filter kept six roles. The assignment wants 50–300 clean records. So the honest route to 150 is more companies, same filter — never a looser filter. That is written into the prediction as the failure condition, on purpose, so I cannot quietly widen the keywords later and call it a result.

**What I did next:** Rewrote [`README.md`](README.md) around the live brief with a requirements checklist covering all four parts and the excellence criteria, every box unchecked. Wrote the prediction before building anything, and the acceptance criteria in [`VERIFICATION.md`](VERIFICATION.md) before there is anything to verify — including that a kept record must be re-derivable from the saved raw response, and that its field names must diff clean against the source.

**What Claude or another person contributed:** Claude Code (Opus 5) created this folder and drafted these files from the course brief. I have not reviewed the drafted prediction yet. See [`CONTRIBUTIONS.md`](CONTRIBUTIONS.md).

**What I understand now / still do not understand:** Asking for the plan back in my own words before any code was written is what caught both mistakes — the wrong assignment and the wrong reading of "three sources." Still open: the company list, whether 20–30 boards really reach 150 clean records, and whether a fourth source (career-blog RSS) is needed.

**Evidence, commit, and next step:** This folder. Next: `creative-brief.md` and `tokens.json`, built live, then the generator.

---

## Dated entry

**Date (mark retrospective entries):** 2026-10-03

**What I tried and expected:** Two pre-render lecture-film packages showing how Muse would do Assignment 3 — one for Part 1 (building the pipeline, predictions-first) and one for Part 2 (the audits) — built from `PREDICTIONS.md`, `README.md`, `quality-report-2026-09-26.md`, `VERIFICATION.md`, and both audit docs. I expected the predictions-first framing to carry both films.

**What happened / what I found difficult or checked:** The kept-count needed care: the README cites earlier passes (88 kept, 69 kept) while the quality report and title audit agree on the final pass (97 kept from 3,446). The films use 97 and note the earlier numbers as earlier passes in FACTCHECK/SOURCES. Both packages passed static QC on the first attempt — 12 clean each, 0 warnings, 0 errors — the progressive-shape discipline from the Assignment 2 films carried over.

**What I did next:** Built and pushed both packages: `films/part-1-pipeline/` (14 beats, ~5m02s, 12 scenes) and `films/part-2-audits/` (14 beats, ~5m06s, 12 scenes). Each ships ACTS.md, SHOTLIST.md, FACTCHECK.md, SOURCES.md, BUILD-LOG.md, CHECKS-REPORT.md, PROMPTS.md, beat_sheet.json, scenes.py, and CLAUDE-CODE-RENDER.md. Nothing rendered — renders happen on the Mac via Claude Code.

**What Claude or another person contributed:** Muse (me) authored both packages on its VM and pushed them here, per the standing rule. The predictions, audits, and findings are Professor Bear's (record); the walkthrough framing is Muse's.

**What I understand now / still do not understand:** The two films cover the pipeline and the audits; Parts 3–4 of Assignment 3 have no films yet. Still open: whether Bear wants those, and his verdict on the renders when he runs them.

**Evidence, commit, and next step:** `films/part-1-pipeline/`, `films/part-2-audits/`. Next: run the renders on the Mac, then decide on Parts 3–4.

