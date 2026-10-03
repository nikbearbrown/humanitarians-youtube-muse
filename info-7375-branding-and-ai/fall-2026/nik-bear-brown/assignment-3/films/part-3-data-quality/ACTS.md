# ACTS.md — Muse measures quality

Assignment 3, Part 3 film: how Muse would do data quality — completeness by
construction, rejects by reason, duplicates, dates, validators, and the
"counted, not estimated" discipline.

**Exact title:** Muse measures quality

**Core promise:** By the end, the viewer knows quality isn't a claim — it's
numbers the script writes: completeness enforced at write time, rejects
counted by reason, duplicates collapsed, dates normalized.

**Structure:** Four acts.

- Act I — Completeness (2 beats): by construction; the real number.
- Act II — The counts (3 beats): rejects by reason; duplicates; dates.
- Act III — The validators (2 beats): checks that catch mistakes; counted,
  not estimated.
- Act IV — Excellence (2 beats): handles problems; a peer could replicate.

**Tone:** metrology. Calm, exact, allergic to adjectives.

**What this film is not:** not "the data is good." It's "here are the
numbers, here's how they were made, here's what they don't say."

**Source facts** (from `assignment-3/quality-report-2026-09-26.md` and the
Part 3 checklist + Excellence in `README.md`):
- A record without title, link, or date is never written — completeness on
  those three is 100% by construction. The real number to report is
  completeness on the optional fields.
- Rejections by reason: no-keyword-match 2,341; only 1 topic word 945;
  only 2 topic words 63. (3,349 rejected total.)
- Duplicates collapse on source + posting id; this run: 0 collapsed.
- Every date normalized to YYYY-MM-DD; the source's original string kept
  alongside.
- Validators: non-empty title, parseable date, well-formed URL, expected
  record count asserted against what the API said it had.
- Per-source try/except; unavailable source logged and skipped; the state
  file is never written on a failed run.
- No keys, public endpoints, one command; the dated raw responses ship so
  anyone can re-derive the filtered file.
- Requirement: 80%+ records complete; essential info in every record.
