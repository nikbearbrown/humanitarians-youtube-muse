# FACTCHECK.md — "Claude making a film about Muse" (Gate F)

Source of truth: the document Bear pasted on 2026-10-03 ("Meta Muse: What
It Does, Security Concerns, and Business Model"). The film presents the
document's content AS Bear and Claude's opinion — Liam narrates their
analysis; he does not assert it as his own verified fact.

## Attribution map (how each claim class is voiced)

| Class | Examples | Voicing |
|---|---|---|
| Doc's own framing/analysis | "personal superintelligence" as framing; endurance-not-intelligence; intent layer; skepticism | "Bear and Claude's read", "their analysis" |
| Attributed to Meta | launch date, tagline "AI That Hustles for You", "first step" quote, no ads inside Muse | "Meta says" |
| Third-party reports | Malwarebytes zero-day; Pivot to AI critique; "one analysis" (11/47); "widely expected" (Marketplace) | "researchers report", "one analysis estimates", "widely expected" — never as established fact |
| Nik's experience/take | capability vs GPT-6 Astra / Claude Fable / Opus; phone discomfort | "in Nik's experience" |
| Cross-checked with Muse docs | Sept 8 2026 launch; US/Canada; Muse Spark; surfaces | solid — matches `~/docs/muse.md` |
| Numbers from the doc only | 2.5M downloads; pricing tiers; $1.25/$4.25 API; 6.8 GB export | "the document reports" — not independently verified |

## Beat-by-beat claims

| # | Beat | Claim | Verdict | Fix |
|---|---|---|---|---|
| 1 | B01 | Agent that acts: goal → plan → steps, approval before consequential actions | doc's framing of the product | voice as their read |
| 2 | B02 | Launched Sept 8 2026 (Meta); Muse Spark (cross-checked); < GPT-6 Astra etc. (Nik's take); 2.5M downloads (doc reports) | mixed attribution | keep each attribution separate |
| 3 | B03 | Persistent Linux VM per user; same architecture as Cowork/Codex | doc's technical description | voice as their read |
| 4 | B04 | Errand list; Ticketmaster launch partner; "endurance, not intelligence" | doc's analysis | voice as their read |
| 5 | B05 | Interfaces + connector lists; Amazon blocked (CNBC per doc); custom connectors unreviewed | third-party + doc | attribute the block; rest as their read |
| 6 | B06 | Small business (Sept 29, TechCrunch per doc); nothing publishes without approval (Meta per doc); Spark API as sanctioned dev route | mixed | attribute |
| 7 | B07 | Pricing tiers + weekly allowances; card required even for free | doc reports | "the document reports" |
| 8 | B08 | API pricing with/without data sharing | doc reports | "the document reports" |
| 9 | B09 | Transaction fees, merchant-paid; free tier as a bet (Zuckerberg per doc) | attributed | attribute the Zuckerberg line |
| 10 | B10 | Subs/API/ads-angle/training-data as secondary revenue | doc's analysis | voice as their read; "Meta says no ads inside Muse" attributed |
| 11 | B11 | Intent layer strategy; 11-of-47 skepticism ("one analysis"); who it's for | analysis | attribute the 11/47; the rest as their read |
| 12 | B12 | Full Disk Access covers the whole disk; behavioral promise vs technical boundary | doc's critique | voice as their critique |
| 13 | B13 | Deny-list violates fail-safe defaults (Saltzer & Schroeder 1975); folder pickers were possible; Messages/Notes/Mail need FDA | doc's critique | voice as their critique |
| 14 | B14 | Malwarebytes zero-day (needs local execution); 6.8 GB runtime export; prompt-extraction reports | third-party reports | attribute each; keep the "needs local execution" qualifier |
| 15 | B15 | Training on by default; policy-not-crypto; cloud processing; token exposure | doc's critique | voice as their critique |
| 16 | B16 | Prompt injection adversarial risk; approval fatigue | doc's analysis | voice as their analysis |
| 17 | B17 | Mascot as trust shortcut (BU professor cited); superintelligence branding overpromises | doc's critique | attribute the professor |
| 18 | B18 | Ad-business conflicts; self-graded attribution; Meta-only advice; lock-in; roadmap risk; phone permissions | doc's analysis | voice as their analysis |
| 19 | B19 | Bear removed the Mac app; verified via pgrep/LaunchAgents/mdfind; web-only | Bear's reported actions | voice as what he did |
| 20 | B20 | The VM/PR/CI/burner pipeline setup | Bear's reported setup | voice as what he did |
| 21 | B21 | General rules (assume breach, caps outside the agent, etc.) | Bear's stated rules | voice as his rules |
| 22 | B22 | Six open questions | doc's list | voice as open questions |

## Deliberately cut / never claimed

- **Prices as established fact** — my product docs don't list them; the film
  attributes all pricing to the document.
- **"Muse is a security disaster" as narrator fact** — it's the document's
  critique (and Pivot to AI's headline); the film voices it as their view.
- **Any claim about what Meta will do** (ads coming, free tier tightening) —
  voiced as the document's expectation, never as fact.
- **OmniRoute executor details** — named once as "stays disabled"; the
  mechanism is not the film's business.

## PROMPTS.md

No paid generation prompts. All visuals are Manim (free) or library Remotion
components (free). No Higgsfield or other paid beats.

---

# UPDATE 2026-10-04 — tokens-in-real-work, the data discount, the cloud-only rule (Gate F)

Bear's additions (his words, 2026-10-04): the 100M-token allowance in terms of real work (he reports 18% used); emphasize that the API's data-sharing price is more than ten times cheaper because Meta is buying data and a user base; emphasize that Muse's "one folder only" is a language model's promise, not a boundary, and that Bear runs Muse only in the cloud and only on things like Google Drive. IDs below are the CURRENT beat ids (the older table above numbers some Act IV/V rows one off; it is left as written).

| # | Beat | Claim | Verdict | Source | Fix / voicing |
|---|---|---|---|---|---|
| 23 | B08 | $1.25 in / $4.25 out per M tokens; $0.10 / $0.20 with data sharing | the document reports (not independently verified) | Bear's pasted doc | voiced "the API is priced separately…"; unchanged from before |
| 24 | B08 | "12.5x cheaper on input, 21x on output" | **computed**: 1.25/0.10 = 12.5; 4.25/0.20 = 21.25 | arithmetic on row 23 | spoken "twelve and a half… twenty-one" |
| 25 | B24 | "More than ninety percent off" | **computed**: input 92%, output 95.3% | arithmetic | OK |
| 26 | B24 | "that gap is a bid; Meta gets whatever you run through it: usage, appointments, purchases, tickets" | **Bear and Claude's read**, not a documented fact. Appointments and tickets are errands Muse is documented to do (ACT II); that training on that content is what the discount pays for is inference | Bear 2026-10-04 + doc's errand list | voiced "Bear and Claude's read"; never "Meta says" |
| 27 | B25 | Bear is "eighteen percent through this week's free allowance" | **Bear's own figure**, as of Oct 4 | Bear, chat, 2026-10-04 | voiced "Nik says"; on screen "Nik's count, Oct 4" |
| 28 | B25 | 13 film packages, 212 beats, 8,149 words of narration, about an hour of film | **measured** from `beat_sheet.json` of the 13 Muse film packages in this repo; film length = 3 measured + 10 estimated from the sheets (3,698 s = 61.6 min); all 13 packages were committed 2026-10-03, 12:55 to 17:45 | repo files + `git log` | voiced "roughly an hour"; screen "≈ 62 min". NOT verified: that every one of the 18% went into these packages (other Muse use in the window is possible) |
| 29 | B26 | "About 72 film packages a week, nearly six hours" | **computed**: 13 x 100/18 = 72.2; 61.6 min x 100/18 = 5.7 h; straight-line, one week | arithmetic on rows 27-28 | spoken "straight-line math from one week; a different week would look different" |
| 30 | B27 | The script is about 11,000 tokens, under a tenth of a percent of 18M | **estimate**: 8,149 words / 0.75 words per token = 10.9k tokens; 10.9k / 18M = 0.06%. Assumes Muse tokens count like ordinary tokens; the document says Muse tokens may not map to raw tokens | arithmetic + rule of thumb | voiced "if Muse tokens count like ordinary ones"; same caveat on screen |
| 31 | B27 | "The rest is the agent re-reading its own work" | **Claude's read** of how agent loops spend tokens; not measured for Muse | general agent behavior | voiced "Claude's read" |
| 32 | B28 | 100M tokens = $125 to $425 at the standard API rate, $10 to $20 shared | **computed**: 100 x $1.25 = $125 (all input), 100 x $4.25 = $425 (all output); 100 x $0.10 = $10, 100 x $0.20 = $20 | arithmetic on row 23 | caveat spoken and on screen: "if the tokens compare — nobody can confirm" |
| 33 | B29 | The free tier is a subsidy; Meta is buying a user base and data | **their read** (and Bear's); consistent with the document's "generous free tier is a bet" framing | Bear 2026-10-04 + doc | voiced "Their read" |
| 34 | B30 | "Muse told Nik it would only touch one folder"; Nik can't set a one-folder limit — whole disk or nothing | **Bear's report** of what Muse said, and of the Mac app's permission model (Full Disk Access, deny-list, doc 5.1-5.3) | Bear 2026-10-04 + doc | voiced "Muse told Nik"; not a quote on screen ("Muse: only this folder" is a paraphrase label) |
| 35 | B30 | Language models hallucinate | general fact | well established | OK |
| 36 | B31 | Nik runs Muse only in the cloud, never locally; it sees only what he puts there, e.g. a Google Drive folder, a sandbox repo | **Bear's stated practice** (2026-10-04). Not verified: the actual OAuth scope of the Drive connector (open question in the last act) | Bear | voiced as what Nik does; "the wall is where the files live" is the design point, not a guarantee about connector scopes |
| 37 | BDEFS | token = a word-sized chunk of text | simplification (about 3/4 of an English word) | standard | OK |
| 38 | BVDT | recap lines for the above | recap only, nothing new | | |

Stripped: nothing spoken as a date except "this week" and the on-screen "Oct 4" tag (the 18% will go stale; that tag is the datable item, by design).
