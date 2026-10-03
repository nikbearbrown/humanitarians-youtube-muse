# ACTS.md — Muse audits itself

Assignment 3, Part 2 film: how Muse would audit the pipeline — the title
audit (20 rules instead of 3,446 readings), the audit's own bug, the reject
audit (100 random + 63 closest calls), and the sales-enablement reversal.

**Exact title:** Muse audits itself

**Core promise:** By the end, the viewer knows that every accuracy number so
far described only what the filter kept — and has seen the machinery that
checks what it threw away, including the audit catching its own mistake.

**Structure:** Four acts.

- Act I — The title audit (2 beats): 20 rules, not 3,446 readings; 23 false
  positives.
- Act II — The audit's own bug (2 beats): "training" means ML; the filter
  was right.
- Act III — The reject audit (3 beats): 100 random + 63 closest calls;
  `education` in 618 of 618; recruiters, not teachers.
- Act IV — The reversal (2 beats): sales enablement kept; the lesson.

**Tone:** detective story, self-deprecating. The hero moment is the audit
being wrong.

**What this film is not:** not "the filter works." It's "here's how we
check, and here's what the checking found — including about itself."

**Source facts** (from `assignment-3/`):
- Title audit (2026-09-27): 3,446 postings, 21 job families, 3,082 distinct
  titles. Judge 20 family rules, read only the disagreements.
- 23 kept from families that should never keep (false positives); 1
  rejected from a keep family (candidate false negative); 555 in judge
  families.
- The audit's bug: first version treated "training" as a teaching word →
  27 rejected "education" jobs that were Pre-training, Post-Training,
  Training Runtime, Researcher Training — ML jobs. The filter had been
  right; the audit was wrong. ML_TRAINING is now the first family rule.
- False friends: TECH_ENABLEMENT (7 kept, engineering jobs), RECRUITING
  (2 kept — university/campus/student are recruiting vocabulary).
- Reject audit: Part 1 = uniform random 100 (seed 20260926, reproducible);
  Part 2 = all 63 closest calls (two teaching words, bar was three).
- Finding 1: `education` appears in 618 of 618 Anthropic postings — the
  logistics footer ("Minimum education: Bachelor's degree…"). Boilerplate.
- Finding 2: topic words kept recruiters, not teachers — Stripe University
  Recruiter ×3, Notion Head of Early Career Recruiting, OpenAI Youth Culture
  marketing.
- 950 rejects matched exactly one teaching word — counted, not read.
- Sales-enablement reversal: Bear ruled "developing materials… to train
  their own people would be a great fit" — 13 kept (not errors); 9
  education-sales roles moved to judge.
