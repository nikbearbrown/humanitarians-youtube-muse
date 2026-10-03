# FILM-BUILDER-HANDOFF.md

**Purpose:** turn a fresh Muse instance into a film-builder that works exactly
the way Muse (the original) does — building lecture films as pre-render
packages on `Humanitariansai/humanitarians-youtube-muse`.

**Read this whole file before touching anything.** Then read the four finished
film folders in the repo (see §11) — they are the pattern to copy.

---

## 1. What "building a film" means here

A "film" is **not a video file**. It is a **pre-render package**: everything
needed to render the video, except the narration audio and the rendered
video itself. You write:

- the script (beat sheet),
- the visuals (`scenes.py`, Manim),
- the docs (acts, shot list, fact check, sources, build log, QC report,
  prompts, render instructions),

and push all of it to GitHub. **Bear renders the narration (Kokoro TTS) and
the video (Manim) locally on his Mac** using Claude Code, following your
`CLAUDE-CODE-RENDER.md`. You never render. You never publish.

This split exists because: Bear can't see your VM, but he can see GitHub
(standing rule §5). GitHub is the shared surface.

## 2. The repos

| | Repo you write to | The original build repo |
|---|---|---|
| URL | `https://github.com/Humanitariansai/humanitarians-youtube-muse` | `https://github.com/nikbearbrown/humanitarians-youtube-muse` |
| Course root | `info-7375-branding-and-ai/fall-2026/nik-bear-brown/` | same path |

The other repo already mirrors the assignment-4 work, including four finished
film folders under `.../assignment-4/films/`. **Study those four folders
first.** They are complete, gated, pushed examples of exactly what you are
being asked to produce.

## 3. GitHub write access (do this first)

You need a token with **Contents: read + write** on
`Humanitariansai/humanitarians-youtube-muse`. Rules:

- Bear provisions the token. It is a **fine-grained personal access token
  scoped to that one repo**. Never ask Bear to paste a raw key in chat.
- The token is stored in the secure credential store and attached to
  requests at call time. **Never print, log, or persist the raw token.**
  Never put it in a file, an env var, or a command line.
- **SSH is blocked from the VM.** Use the HTTPS Contents API only
  (`https://api.github.com`). Do not try to work around this.
- The helper scripts live in `~/workspace/skills/github/bin/`:
  - `gh-put-file.py OWNER REPO PATH --file LOCALFILE` — create/update one file
  - `gh-mkdir.py OWNER REPO FOLDER` — create a folder (drops a README.md)
  - `gh-delete.py` — delete a file
- They authenticate via `add_surrogate_to_request(req, "custom.github",
  entry_name="access_token", allowed_hosts=["api.github.com"])` from
  `/opt/hatch/skills/skill-creator/bin/dynamic_credentials.py`.
- **Critical argument-order gotcha:** `gh-put-file.py` takes the local file
  as `--file`, not as a positional arg. Correct:
  `gh-put-file.py OWNER REPO REMOTE/PATH --file localfile`.
  Wrong (it errors): `gh-put-file.py OWNER REPO REMOTE/PATH localfile`.
- A 401/403 is a question about the *request* before the *key*: first check
  the credential was actually attached (a request built without the helper
  carries nothing and looks exactly like a bad token). Only then ask about
  the token.

## 4. The toolkit

Clone `https://github.com/nikbearbrown/brutalist.art` into your workspace.
What you need from it:

- The **`lecture` skill** (`skills/make/`): the film-making conventions —
  beats, acts, the Liam persona, QC pipeline.
- The **static QC checker**:
  `runtime/qc/static_scene_check.py`. This is your gate. It runs your
  scenes against a geometry stub (no Manim install needed) and checks:
  1. `construct()` runs with no Python error,
  2. no `generic_art` template,
  3. the on-screen **shapes actually change** beat to beat (not just text),
  4. all coordinates stay inside the 16:9 frame.
- Run it **per scene class**: `python3 static_scene_check.py scenes.py
  --class M01_Bidea`. Exit 0 = clean, 1 = warnings, 2 = errors.
  (The default class `BearsDoodlesVideo` won't exist in your file — always
  pass `--class`.)
- Also run `python3 -m py_compile` on every `.py` file.

Film identity (constant across films unless Bear changes it): channel
`claude-liam`, persona "Liam, in for Bear", Kokoro voice `am_onyx`,
Teardown register, watermark `@NikBearBrown`.

## 5. Standing rules (non-negotiable)

1. **Push everything to GitHub immediately.** Bear can't see your VM.
   Make the change, push it, he decides whether to download it locally.
2. **Never publish a film.** No uploads, no staging for publishing, without
   Bear's explicit instruction.
3. **Never commit MP3/MP4/WAV.** Narration and renders live on Bear's Mac
   only. If `__pycache__`/`.pyc` files appear, delete them; never push them.
4. **Mac file boundary:** on Bear's Mac, all file activity stays inside
   `/Users/bear/Documents/CoWork/bear-textbooks/books/` and subfolders.
   Never read/write/list/search outside it. (Your VM workspace is yours.)
5. **Course log rules** (from the repo's `CLAUDE.md`): every substantive
   change gets a `FRICTIONAL.md` entry with seven fields (see §10); label
   every value `record`, `judgment`, or `your input`; JSON is indented and
   human-readable; the repo is public — **no contact details, private names,
   or absolute local paths**.
6. **Keep working.** Bear's standing instruction: keep running through your
   tasks until they are done; when you finish, he gives you new tasks.

## 6. The film package (11 files per film)

Each film lives in its own folder, e.g.
`.../assignment-4/films/part-2-showing-the-output/`, containing:

| File | What it is |
|---|---|
| `ACTS.md` | Structure: exact title, core promise, acts, tone, what the film is not, source facts |
| `SHOTLIST.md` | Scene table: scene → beat → what the viewer sees → data source |
| `FACTCHECK.md` | Every claim checked: **Verified (record)** / **Judgments (judgment)** / **Cut or disclosed**. Unverifiable claims are cut, not filmed |
| `make_sheet.py` | Generates `beat_sheet.json`; asserts beat counts and totals |
| `beat_sheet.json` | The script: 13–22 beats, generated, indented |
| `scenes.py` | The visuals: Manim scenes M01–Mxx |
| `SOURCES.md` | Fact → source-file table |
| `BUILD-LOG.md` | Dated build steps, including failures |
| `CHECKS-REPORT.md` | QC results per scene + issues found and fixed |
| `PROMPTS.md` | The prompts (from Bear) that shaped the film, in order |
| `CLAUDE-CODE-RENDER.md` | Render instructions for Bear's Mac (see §9) |

Plus the `README.md` that `gh-mkdir.py` drops in the folder.

## 7. Build order (follow it)

1. **Read the source material first.** If the film is about project outputs,
   read the actual outputs before writing a word. Every beat must cite a
   real file. This is what catches script errors (e.g. claiming files that
   don't exist) before they become scenes.
2. Write `ACTS.md`, `SHOTLIST.md`, `FACTCHECK.md`.
3. Write `make_sheet.py`; run it; verify `beat_sheet.json`.
4. Write `scenes.py`.
5. `py_compile`, then the static checker **per class**. Fix until **0
   errors, 0 warnings** (see §8 for the failure catalog).
6. Write `SOURCES.md`, `BUILD-LOG.md`, `CHECKS-REPORT.md`, `PROMPTS.md`,
   `CLAUDE-CODE-RENDER.md`.
7. `gh-mkdir.py` the film folder, then `gh-put-file.py` each file
   (**`--file` flag**). Push the 11 files.
8. **Verify** via the Contents API that the files are live.
9. Log the film in `FRICTIONAL.md` (seven fields) and push that too.

## 8. Beat sheet conventions

Beat IDs and their jobs:

- `BIDEA` — the hook (one sharp line, the film's question).
- `BDEFS` — 3–4 key terms, defined.
- `B01`–`Bnn` — the body, grouped into **acts** (2–6 beats each).
- `BVDT` — the recap: **one line per act** (4 acts → 4 lines; 6 acts → 6).
- `BHTF` — "your turn": one concrete thing for the viewer to do today.
- `BOUT` — outro: "Muse, in for Bear. Thanks for watching." (+ next-film teaser).

Each beat: `id`, `scene` (M01…), `dur_s`, `act`, `voice` (`"Muse"`), `line`
(the exact spoken narration, ~150 wpm), `screen` (what the viewer sees).
**Every word on screen is read aloud in the same beat.** No silent text.

Durations: speech at ~150 wpm plus small pauses; body beats run 12–30 s.
Total film: ~4.5–7 minutes. `make_sheet.py` must assert the beat count and
print the total.

## 9. `scenes.py` conventions and the QC gate

- One class per scene: `M01_Bidea(Scene)`, `M02_Bdefs(Scene)`, …
- `config.pixel_width = 1920`, `config.pixel_height = 1080` (16:9).
- **Safe area: keep all coordinates within ±6.3 x, ±3.4 y**
  (hard frame: ±7.12, ±4.05). Outside safe area = warning.
- House palette: `INK #111111`, `PAPER #F7F3EA`, `ACCENT #B8472F`,
  `BLUE #2F6BB8`, `GREEN #2E8B57`, `GREY #8A8578`, `CARD #FFFFFF`.
- The checker's binding rule: **non-text shapes must evolve across the
  beat.** A scene where only text fades in fails with "shapes never change".
  Fix pattern: reveal a small shape (dot, square, coin, bar) alongside each
  text reveal; grow bars one at a time; sequence cards with arrows.
- `Checkmark` does **not** exist in the checker's stub. Use a custom helper:
  ```python
  def check_mark(pos, scale=1.0, color=GREEN):
      return VGroup(
          Line(ORIGIN, RIGHT*0.5 + DOWN*0.3, color=color, stroke_width=10),
          Line(RIGHT*0.5 + DOWN*0.3, RIGHT*1.3 + UP*0.4, color=color, stroke_width=10),
      ).scale(scale).move_to(pos)
  ```
- A text-only scene warns ("no shapes recorded"). Fix: put a background
  plate (`RoundedRectangle`) behind the text.
- Gate: `py_compile` clean **and** every scene class `0 clean · 0 warn ·
  0 error`. Record the per-scene table in `CHECKS-REPORT.md`, including what
  the first pass flagged and how you fixed it. Do not hide QC failures.

## 10. Logging (`FRICTIONAL.md`)

Assignment-level `FRICTIONAL.md` gets one entry per film (and per substantive
build), with all seven fields:

1. Date and what I was working on
2. I tried / expected
3. What happened (including failures and reversals)
4. What I did
5. What Claude or another person contributed (credit Bear's decisions; be
   honest about AI contributions)
6. What I understand now / still do not understand
7. Evidence and next step

Label values `record` / `judgment` / `your input`. Record failures (bad
pushes, QC errors, script corrections) — the log is where the work is
judged, and hidden failures corrupt it.

## 11. The render handoff (Bear's step, your instructions)

`CLAUDE-CODE-RENDER.md` tells Bear, on his Mac:

1. Pull the repo; `cd` into the film folder.
2. Synthesize each beat's `line` with **Kokoro voice `am_onyx`** → one MP3
   per beat (`audio/BIDEA.mp3` … `audio/BOUT.mp3`).
3. Review cut: from the toolkit dir
   (`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art`):
   `./art run --reel <reel-name> --beats <film>/beat_sheet.json --scenes
   <film>/scenes.py --audio <film>/audio/`
4. Final 4K master: `./art final --reel <reel-name>`
5. Publish only on his explicit instruction.

Include the film facts (beat count, duration, scene count, QC status) and
the "no MP3/MP4 committed" note.

## 12. Gotcha catalog (earned the hard way)

- `gh-put-file.py` needs `--file` for the local path; positional order is
  `OWNER REPO REMOTE_PATH`.
- A failed push script can report "25 files failed, 0 pushed" — read the
  error, fix the bug, re-push, and log it. Don't pretend it didn't happen.
- `python -m py_compile` creates `__pycache__/`; a stray `.pyc` pushed to
  GitHub must be deleted via the API (`gh-delete.py`). Push specific files
  only.
- Always verify with a Contents API read after pushing. A script that says
  "created" is a claim; the API read is the proof.
- The Contents API creates one commit per file — that's fine and expected.
- Reels are named `part-N-<slug>`; beat audio files are `audio/<BEAT>.mp3`.
- When a script fact turns out wrong (e.g. files that don't exist), fix the
  script — the film must never claim what the repo doesn't prove.

## 13. Where you start

1. Get your GitHub token provisioned (§3) and confirm write access with one
   test push.
2. Clone `brutalist.art`; confirm the checker runs.
3. Read all four finished film folders in
   `info-7375-branding-and-ai/fall-2026/nik-bear-brown/assignment-4/films/`
   end to end — they are your spec.
4. Read `ACTS.md` → `FACTCHECK.md` → `beat_sheet.json` → `scenes.py` in that
   order for one film, so you see how the layers connect.
5. Ask Bear what the next film is about. Then follow §7.
