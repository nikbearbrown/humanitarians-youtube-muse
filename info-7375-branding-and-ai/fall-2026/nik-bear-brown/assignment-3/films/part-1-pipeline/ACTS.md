# ACTS.md — Muse builds the pipeline

Assignment 3, Part 1 film: how Muse would build the data-collection pipeline
— predictions written before the run, the three-step collector, 18 boards,
what the filter refuses, the moved target, the missed bullseye, and the
acceptance criteria fixed before checking.

**Exact title:** Muse builds the pipeline

**Core promise:** By the end, the viewer knows the assignment's real
discipline: write the predictions before you run anything, fix the failure
condition in writing, and let the run embarrass you.

**Structure:** Four acts.

- Act I — Predictions first (2 beats): write before you run; the failure
  condition.
- Act II — The pipeline (3 beats): download, filter, write; three ATSs;
  what it refuses.
- Act III — The run (3 beats): 3,446 → 97; the target moved; the bullseye
  missed by one word.
- Act IV — Verification (1 beat): acceptance criteria fixed before checking.

**Tone:** engineering discipline, dry humor about the filter's mistakes.

**What this film is not:** not a collect.py code walkthrough line by line;
not "data pipelines are easy." It's about the honesty machinery around the
pipeline.

**Source facts** (from `assignment-3/`):
- PREDICTIONS.md written 2026-09-26 before anything ran: (1) record count
  is the problem, need 20–30 companies; (2) false positives from culture
  blurbs, > quarter; (3) false negatives are title-only matches; (4)
  SmartRecruiters slowest/most fragile.
- Measurable failure condition: "Loosening the filter to hit a record count
  is the specific dishonesty this prediction exists to catch."
- Three steps: download (3 ATSs, raw responses saved dated), filter (role
  words, topic words, flexible terms), write (jobs-of-interest.json + .csv).
- Final pass: 18 boards, 3,446 postings, 97 kept (quality-report-2026-09-26;
  the README cites earlier passes at 88 and 69).
- Field names are the source's own; the script's decisions go under one
  `matched` key.
- Refuses: no title/link/date → not written; dead source doesn't kill the
  run; duplicates collapse on source + id.
- Target became "any job whose product is teaching materials" (Anthropic
  Technical Documentation and Content Engineer, Claude Docs, as the model).
- Bullseye missed: Replit Learning Experiences Creator — filter had
  "learning designer", not "learning experiences". One word.
- VERIFICATION.md: 9 acceptance criteria fixed before checking (re-derivable,
  field names unchanged, completeness, duplicates, dead source, dates,
  counted not estimated, two hand checks, rejects read).
