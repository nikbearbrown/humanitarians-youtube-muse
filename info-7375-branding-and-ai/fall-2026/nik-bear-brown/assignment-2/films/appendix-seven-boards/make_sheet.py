#!/usr/bin/env python3
"""make_sheet.py — Muse widens the search (Assignment 2 appendix film).

13 beats, four acts. Run: python3 make_sheet.py
"""
import json

BS = {
    "title": "Muse widens the search",
    "film": "A2-2",
    "series": "Branding and AI — how Muse would do the assignments",
    "beats": [
        {
            "id": "BIDEA", "scene": "M01", "dur_s": 18, "act": "hook",
            "voice": "Muse",
            "line": "The assignment says find one real job posting. The trap in that sentence is the word one. A student who picks the first plausible posting has done Part 1. A student who looks at the field first has done Part 1 and Part 2's homework.",
            "screen": "One board vs seven boards; the trap."
        },
        {
            "id": "BDEFS", "scene": "M02", "dur_s": 22, "act": "hook",
            "voice": "Muse",
            "line": "Four terms. ATS: the applicant-tracking system behind a careers page. Feed: its public JSON of open postings — no key, no login. Blurb: the company boilerplate that poisons keyword matching. Sweep: all of it, in one afternoon.",
            "screen": "Four terms: ATS / feed / blurb / sweep."
        },
        {
            "id": "B01", "scene": "M03", "dur_s": 24, "act": "1",
            "voice": "Muse",
            "line": "Three systems, one script. Greenhouse: Figma, Webflow, Miro — one call, full ad text. Ashby: Writer, Notion, Jasper — one call, though the names can have spaces. SmartRecruiters: Canva — paged, a hundred at a time, and no ad text in the feed.",
            "screen": "Three ATS cards with their companies."
        },
        {
            "id": "B02", "scene": "M04", "dur_s": 22, "act": "1",
            "voice": "Muse",
            "line": "SmartRecruiters was the new work. No description in the listing feed means one extra call per posting. Canva had two hundred forty-eight open jobs: three minutes thirty-eight seconds, two hundred fifty-one requests to one host. Not hard — just patient.",
            "screen": "Canva build: 248 jobs, 3m38s, 251 requests."
        },
        {
            "id": "B03", "scene": "M05", "dur_s": 22, "act": "2",
            "voice": "Muse",
            "line": "The field, side by side. Figma one-fifty-two, Writer fifty-one, Canva two-forty-eight, Notion one-twenty-eight, Webflow twenty-nine, Miro twenty-eight, Jasper seven. Six hundred forty-three postings, word-matched against the same résumé.",
            "screen": "Seven company bars with posting counts."
        },
        {
            "id": "B04", "scene": "M06", "dur_s": 22, "act": "2",
            "voice": "Muse",
            "line": "And the failure every student should expect. At Writer the first pass flagged fifty-one of fifty-one — because generative AI, AI agents, and learning are in every posting's company blurb. Ignoring those three words — a change to the rules, not the résumé — brought it to twenty-four. Write it down.",
            "screen": "Writer: 51/51, three words crossed out, 24."
        },
        {
            "id": "B05", "scene": "M07", "dur_s": 22, "act": "3",
            "voice": "Muse",
            "line": "What changed: the wider look found a better fit than Figma alone. Webflow's Senior Developer Educator — a new position, US remote, one-thirteen to one-fifty-five K, on camera, building the reference sites behind Webflow University. The Figma pick stands, but the gap analysis gets a second column.",
            "screen": "Better-fit card: Webflow Senior Developer Educator."
        },
        {
            "id": "B06", "scene": "M08", "dur_s": 20, "act": "3",
            "voice": "Muse",
            "line": "And it changed the search word. Not Advocate — Educator. Two of the six best matches never use the word Advocate at all. The sweep didn't just find roles; it taught the searcher what to call them.",
            "screen": "The word swap: Advocate -> Educator."
        },
        {
            "id": "B07", "scene": "M09", "dur_s": 20, "act": "4",
            "voice": "Muse",
            "line": "What it did not find: a part-time, contract, or consulting education role in the US at any of the seven companies. Canva posts twenty-three contract roles and Writer one — the shape exists. It just isn't being posted for this work, in this geography, this month.",
            "screen": "Empty shelf: no part-time education roles at 7 companies."
        },
        {
            "id": "B08", "scene": "M10", "dur_s": 20, "act": "4",
            "voice": "Muse",
            "line": "And three companies couldn't be read this way at all. Framer hand-builds its job pages. Adobe is on Workday, which needs a different scraper. Sketch, InVision, and Mural are unconfirmed. Saying so is part of the answer.",
            "screen": "Three greyed cards: Framer, Adobe, the unconfirmed."
        },
        {
            "id": "BVDT", "scene": "M11", "dur_s": 26, "act": "recap",
            "voice": "Muse",
            "line": "So: act one, three systems — and the patient build of the third. Act two, the field — six hundred forty-three postings, and the blurb failure written down. Act three, what changed — a better fit and a better word. Act four, what it didn't find — no part-time anywhere, and three companies unreadable, stated plainly.",
            "screen": "Four recap lines, one per act."
        },
        {
            "id": "BHTF", "scene": "M11", "dur_s": 20, "act": "do_today",
            "voice": "Muse",
            "line": "Your turn. Pick your seven companies. Before you trust a single match, read the company blurb — and ask what it's poisoning.",
            "screen": "Do-today card: pick seven; read the blurb first."
        },
        {
            "id": "BOUT", "scene": "M11", "dur_s": 14, "act": "outro",
            "voice": "Muse",
            "line": "Muse, in for Bear. Thanks for watching. Next: building the pipeline.",
            "screen": "Nik Bear Brown watermark card."
        }
    ]
}

if __name__ == "__main__":
    assert len(BS["beats"]) == 13, len(BS["beats"])
    acts = [b["id"] for b in BS["beats"] if b["act"] in ("1", "2", "3", "4")]
    assert len(acts) == 8, len(acts)
    total = sum(b["dur_s"] for b in BS["beats"])
    print(f"beats={len(BS['beats'])} body={len(acts)} total={total}s (~{total//60}m{total%60:02d}s)")
    with open("beat_sheet.json", "w") as f:
        json.dump(BS, f, indent=2)
    print("beat_sheet.json written")
