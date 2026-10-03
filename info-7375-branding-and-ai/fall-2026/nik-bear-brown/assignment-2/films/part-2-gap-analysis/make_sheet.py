#!/usr/bin/env python3
"""make_sheet.py — Muse closes the gap (Assignment 2, Part 2 film).

15 beats, four acts. Run: python3 make_sheet.py
"""
import json

BS = {
    "title": "Muse closes the gap",
    "film": "A2-3",
    "series": "Branding and AI — how Muse would do the assignments",
    "beats": [
        {
            "id": "BIDEA", "scene": "M01", "dur_s": 18, "act": "hook",
            "voice": "Muse",
            "line": "A gap analysis is not a confession and not a plan. It's a table with three columns: what they ask for, what you have, and what you'll build. Here's how to fill it in — honestly.",
            "screen": "Empty 3-column table: they ask / I have / to build."
        },
        {
            "id": "BDEFS", "scene": "M02", "dur_s": 22, "act": "hook",
            "voice": "Muse",
            "line": "Four terms. Gap: what the posting wants that the résumé doesn't have. Evidence: proof, not adjectives. Build: the thing you'll make to close it. Link: the row where you already have it — don't rebuild, just link.",
            "screen": "Four terms: gap / evidence / build / link."
        },
        {
            "id": "B01", "scene": "M03", "dur_s": 22, "act": "1",
            "voice": "Muse",
            "line": "Start from Part 1's honest findings. Gap one: deep, hands-on Figma design-systems expertise — never shipped a design system in Figma. Gap two: public speaking at meetups and conferences. Gap three: travel up to twenty-five percent. All three were on the page in Part 1, so none of them are surprises.",
            "screen": "Three gap cards from Part 1."
        },
        {
            "id": "B02", "scene": "M04", "dur_s": 20, "act": "1",
            "voice": "Muse",
            "line": "Then add the second column. The seven-board sweep found Webflow's Senior Developer Educator — US remote, on camera — so the gap analysis now compares two postings, not one. A gap against one company is an anecdote; against two, it's a pattern.",
            "screen": "Table gains a second column: Figma vs Webflow."
        },
        {
            "id": "B03", "scene": "M05", "dur_s": 22, "act": "2",
            "voice": "Muse",
            "line": "Row one: written, visual, and video teaching material about the product. Have: hundreds of course videos, the deep-explainer pipeline, a Coursera MOOC. To build: tutorials about their product — Figma design systems plus MCP, a Webflow University-style build-along, a Notion API walkthrough. The skill transfers; the subject doesn't.",
            "screen": "Row 1: teaching material about the product."
        },
        {
            "id": "B04", "scene": "M06", "dur_s": 22, "act": "2",
            "voice": "Muse",
            "line": "Row two: on camera, in your own voice. Writer says so explicitly; Webflow says present on camera. Have: lecture recordings, studio work. To build: one three-to-five-minute on-camera sample — no synthetic narrator — teaching a single design-system idea. The voice has to be yours because the job says so.",
            "screen": "Row 2: on camera, own voice."
        },
        {
            "id": "B05", "scene": "M07", "dur_s": 24, "act": "2",
            "voice": "Muse",
            "line": "Row three: hands-on depth in the tool. Figma design systems, tokens, Dev Mode; Webflow production sites. Have: Figma boards in class, a master's in information design. To build: one shipped Figma design system with tokens and a Dev Mode handoff, plus one production Webflow site — both open, both real. This is the biggest row, and it gets its own project.",
            "screen": "Row 3: hands-on depth."
        },
        {
            "id": "B06", "scene": "M08", "dur_s": 20, "act": "2",
            "voice": "Muse",
            "line": "Row four: community and public speaking. Have: a hundred fifty plus Fellows, an AI bootcamp for five hundred plus, conference talks. To build: a speaking reel cut from existing recordings, and a list of talks given. The evidence exists; it just needs editing.",
            "screen": "Row 4: community and speaking."
        },
        {
            "id": "B07", "scene": "M09", "dur_s": 20, "act": "2",
            "voice": "Muse",
            "line": "Row five: comfort with AI-assisted workflows, MCP, evals. Have: the Prompt Engineering and Computational Skepticism courses, twenty-five plus deployed course bots. To build: nothing. Already covered — link, don't rebuild. Knowing which rows need no work is part of the analysis.",
            "screen": "Row 5: link, don't rebuild."
        },
        {
            "id": "B08", "scene": "M10", "dur_s": 22, "act": "3",
            "voice": "Muse",
            "line": "The build list, then — four things to make. Tutorials about their products. One on-camera sample. One shipped design system and one production site. One speaking reel. Each one maps to a row; each row maps to a posting requirement. Nothing on the list is decorative.",
            "screen": "The build list: four things to make."
        },
        {
            "id": "B09", "scene": "M11", "dur_s": 22, "act": "3",
            "voice": "Muse",
            "line": "And the biggest gap already has its project: the Madison project exists to close the Figma design-systems gap. That was stated in Part 1, before any building started. The course project isn't separate from the job search — it is the job search, with a syllabus.",
            "screen": "Madison project card closing the Figma gap."
        },
        {
            "id": "B10", "scene": "M12", "dur_s": 22, "act": "3",
            "voice": "Muse",
            "line": "The honest column stays public. This table lives in the repo, gaps and all — because a gap analysis you hide is just a résumé with extra steps. Gaps close by building, in the open, where the next posting can check your work.",
            "screen": "The table stays public; gaps close by building."
        },
        {
            "id": "BVDT", "scene": "M13", "dur_s": 26, "act": "recap",
            "voice": "Muse",
            "line": "So: act one, name the gap — three honest findings, then a second column to compare against. Act two, the five rows — what they ask, what you have, what you'll build, including the row that needs nothing. Act three, the build list — four things to make, and the Madison project closing the biggest gap. Act four, the honest column — the table stays public.",
            "screen": "Four recap lines, one per act."
        },
        {
            "id": "BHTF", "scene": "M13", "dur_s": 20, "act": "do_today",
            "voice": "Muse",
            "line": "Your turn. Draw the three columns. Fill every row from real postings. And find the one row that says link, don't rebuild — it's the easiest win on the page.",
            "screen": "Do-today card: draw the table; find the free row."
        },
        {
            "id": "BOUT", "scene": "M13", "dur_s": 14, "act": "outro",
            "voice": "Muse",
            "line": "Muse, in for Bear. Thanks for watching.",
            "screen": "Nik Bear Brown watermark card."
        }
    ]
}

if __name__ == "__main__":
    assert len(BS["beats"]) == 15, len(BS["beats"])
    acts = [b["id"] for b in BS["beats"] if b["act"] in ("1", "2", "3", "4")]
    assert len(acts) == 10, len(acts)
    total = sum(b["dur_s"] for b in BS["beats"])
    print(f"beats={len(BS['beats'])} body={len(acts)} total={total}s (~{total//60}m{total%60:02d}s)")
    with open("beat_sheet.json", "w") as f:
        json.dump(BS, f, indent=2)
    print("beat_sheet.json written")
