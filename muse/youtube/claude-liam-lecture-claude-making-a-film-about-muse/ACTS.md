# ACTS.md — "Claude making a film about Muse" (claude-liam-lecture-claude-making-a-film-about-muse)

Lecture skill. Channel: claude-liam (Liam, in for Bear · Kokoro am_onyx · @NikBearBrown).
Title (exact, used verbatim in BOUT): "Claude making a film about Muse".

## Framing (read first)

This film presents **Bear and Claude's opinion** — their analysis of Meta Muse
as of October 3, 2026: what it does, what it costs, how Meta makes money on
it, and a twelve-point security critique plus how Bear resolved it for
himself. Liam narrates as Bear's stand-in; contested and third-party claims
stay attributed on screen and in voice ("they report", "their read", "in
Nik's experience") — the film never presents the document's opinions as the
narrator's own verified facts. See FACTCHECK.md for the attribution map.

Source: the document pasted by Bear on 2026-10-03 ("Meta Muse: What It Does,
Security Concerns, and Business Model"), itself citing Meta, Axios,
TechCrunch, CNBC, Malwarebytes, Pivot to AI, and others. Full list in
SOURCES.md.

## Bookends (fixed)

- **BIDEA** — hesitant writer. Liam's greeting ("Hallo. This is Liam, in for
  Bear."), then the topic: not the launch hype, but Bear and Claude's read.
  Correction pair: trigger "what Meta tells you" → replacement
  "what Bear and Claude think".
- **BDEFS** — "Terms In This Lecture", 5 terms, one plain line each:
  1. `agent` — a program that works for you on its own
  2. `connector` — a plug-in to an outside service
  3. `allow-list` — only named things get access
  4. `prompt injection` — hidden instructions steer it
  5. `intent layer` — where you say what you want
- **BVDT** — "Let's recap with Claude." 6 lines, one per act.
- **BHTF** — "Your turn." Prompt: audit what disk access your own AI apps
  hold — list them, and for each write down whether it's an allow-list or
  a deny-list. Two checks: you found every AI app with disk access; you can
  say for each which list model it uses.
- **BOUT** — ClaudeTitleOutro, @NikBearBrown.

## ACT I — What it is (doc §1)

1. A consumer AI agent, "built for everyone" — "personal superintelligence,"
   "AI That Hustles for You." Unlike a chatbot, it acts: goal → plan → steps,
   checking in before consequential actions.
2. Launched in the US on September 8, 2026; runs on Muse Spark. In Nik's
   experience, less capable than GPT-6 Astra, Claude Fable, or Claude Opus.
   Fast adoption: over 2.5 million US downloads in about two weeks.
   (Attribution: capability comparison is Nik's take; downloads per the doc.)

## ACT II — What it does (doc §2)

1. The machinery: every user gets a persistent Linux VM in Meta's cloud —
   browser, filesystem, terminal. Same architecture as Claude Cowork and
   Codex; they differ in audience and default permissions.
2. Consumer errands: travel, restaurants, appointments, shopping and
   checkout, forms, negotiating, subscriptions, tickets (Ticketmaster a
   launch partner). Strength is endurance, not intelligence.
3. Interfaces and connectors: web, iOS, Android, WhatsApp (glasses announced);
   customizable persona. Commerce-first connectors (Shopify, OpenTable,
   Ticketmaster, Duffel, Instacart, Expedia, Stripe; Amazon blocked it);
   productivity (Gmail, Docs, Notion, Figma, Asana, Canva, Slack, Zoom,
   GitHub, QuickBooks, Klaviyo); Meta-only (Instagram, Facebook, Threads,
   Messenger). No Blender/Higgsfield/DaVinci. Custom connectors unreviewed.
4. Small business (Sept 29): Business Manager, drafts posts and campaigns,
   reads QuickBooks, works Klaviyo/Shopify — nothing publishes/sends/spends
   without approval. Developer-ish: terminal → repos, code, PRs; sanctioned
   route is the Muse Spark API.

## ACT III — Money (doc §3 + §4)

1. Pricing: Free $0 / 100M Muse tokens weekly; Power $20/mo / 500M;
   Maximum $100/mo / 3B. Same features; you pay for volume. Card required
   even for free. "Muse tokens" may not map to raw tokens.
2. API pricing: $1.25/M input, $4.25/M output; $0.10/$0.20 with data sharing.
3. Stated model: transaction fees — Meta takes a small merchant-paid cut,
   like an affiliate commission. The generous free tier is a bet those fees
   pay off. Users never see a charge.
4. Secondary revenue: subscriptions, Spark API sales, the ads angle (no ads
   inside Muse, but it funnels businesses into Meta ads; browsing shapes
   ads elsewhere), training data (on by default, opt-out).
5. The strategic goal: own the intent layer — agents for shoppers and
   merchants, Meta in the middle. Skepticism: ~11 of 47 monthly payments
   automatable, so fees may not carry it; ads may come. Built for
   non-technical consumers and small business; technical free-tier users
   are pure cost — likeliest to feel the tightening.

## ACT IV — Security concerns (doc §5)

Twelve subsections, grouped into eight beats. All presented as Bear and
Claude's critique; third-party findings attributed.

1. Full Disk Access instead of folder-level (5.1): the whole disk; Meta's
   "only files you ask about" is a behavioral promise, not a technical
   boundary.
2. Deny-list, not allow-list (5.2) + "optional" in name only (5.3):
   fail-safe defaults (Saltzer and Schroeder, 1975) violated — forgotten
   folders, new folders, external drives exposed. macOS pickers could have
   done folder grants (like Cowork); the likely reason is Messages/Notes/
   Mail databases need Full Disk Access.
3. Known vulnerabilities (5.4): Malwarebytes zero-day (dictation redirect →
   auth token theft; needs local code execution first); researcher runtime
   export (~6.8 GB incl. SSH keys); early prompt-extraction reports.
4. Data handling is policy, not crypto (5.5) + credential exposure (5.6):
   training on by default; ad-system separation is a policy claim, no
   independent audit; employee access policy-gated until confidential mode;
   every file read is processed in Meta's cloud; tokens pasted into chat
   live in the cloud past expiry; OAuth scopes may be broad.
5. Prompt injection + approval fatigue (5.7, 5.8): untrusted content steers
   the agent; failure is adversarial, not random — downstream systems
   (reviewers, renderers) inherit the risk. Approvals only work if read;
   fatigue turns them into reflex.
6. Trust by design (5.9): the mascot/persona as trust shortcuts; a cute
   character reads as safe before earning it; "superintelligence" branding
   overpromises for an errand agent.
7. Business conflicts (5.10) + platform dependence (5.11): affordability
   advice from the company selling the ads; self-graded attribution;
   Meta-inventory-only spend advice; lock-in; shopper-optimized roadmap
   (developer features can vanish).
8. Phone exposure (5.12): mobile permissions (contacts, messages, health) —
   Nik won't use it.

## ACT V — How Bear resolved it (doc §6)

Governing principles: assume breach, bound the blast radius, enforce limits
outside the agent.

1. Removed the Mac app (signed out, deleted, revoked, cleared login items;
   verified with pgrep/LaunchAgents/mdfind). Web-only via muse.ai, ideally
   a dedicated browser profile. Not on the phone.
2. The film-drafting setup: Muse works only in its cloud VM on public
   sandbox repos; GitHub connector as a dedicated bot account, write to
   sandbox repos only, no pasted tokens; PRs only, branch protection,
   CODEOWNERS, Claude Code review + deterministic CI; a burner MacBook
   with no Muse renders; main Mac, Hetzner, and student/HAI/unpublished
   work never touch Muse.
3. General rules: an agent's access is the attacker's access; caps outside
   the agent (card limit, not instruction); irreversible actions get a
   human; protect the short list (email, money, credentials, public voice)
   with real walls; prefer "what should I access?" tools over "what should
   I avoid?" tools.

## ACT VI — Open questions (doc §7)

One beat: the six open questions — VM disk/compute limits; GitHub connector
OAuth scopes; Muse-token mapping; whether confidential mode ships and its
guarantees; how long the free tier stays generous; whether ads come to Muse.

## LEFT OUT (with reasons)

- The doc's Sources list as beats — it's credits; it lives in SOURCES.md.
- Fine-grained connector-by-connector detail beyond the headline names —
  the beat names the pattern (commerce-first, productivity, Meta-only).
- OmniRoute specifics (5.12 tail) — named once in the beat as "stay disabled";
  the mechanism detail doesn't teach the point.

## Runtime estimate (information only)

23 body beats, ~444 s estimated (~7.4 min).
Length is an output; no target.

---

## UPDATE 2026-10-04 — additions (Bear's requests, same day)

All additions stay inside the existing acts; beat ids B24–B31 are appended, order is the sheet's list order.

**ACT III — Money** now runs: B07 tiers → B08 API price (revised: "12.5x / 21x cheaper") → **B24 the discount is a bid** (more than 90% off; Meta gets what runs through it) → B09 transaction fees → B10 secondary streams → B11 intent layer → **B25 a hundred million tokens as real work** (Nik: 18% used; what's in his folder: 13 film packages, 212 beats, 8,149 words, about an hour) → **B26 at that pace** (about 72 packages, nearly six hours) → **B27 tokens measure effort** (the script is under 0.1% of the tokens) → **B28 priced like the API** ($125–$425 vs $10–$20) → **B29 the subsidy is the tell** (free tier buys a user base and your data; be careful what goes through it).

**ACT IV — Security** gains **B30 a promise is not a permission**: Muse told Nik it would only touch one folder; that is a language model's promise; Nik can't set a one-folder limit (whole disk or nothing). Placed after B13 (deny-list).

**ACT V — How Bear resolved it**: B20 reworded to lead with "nothing runs locally"; **B31 nothing runs locally**: Muse never runs on Nik's computer, only in the cloud, seeing only what he puts there (a Google Drive folder, a sandbox repo); the wall is where the files live, not what Muse promises. Placed after B20.

**Bookends**: BDEFS adds `token` (six terms); BVDT line 2 ("the cheapest tokens cost your data") and line 5 ("nothing local — cloud only, Drive and sandbox repos").

Cast: money act reuses the Meta dot and the ACC bar from B08; B24 and B29 both end on "your data" in terracotta.

New runtime: 36 beats, estimate in BUILD-LOG after the build.
