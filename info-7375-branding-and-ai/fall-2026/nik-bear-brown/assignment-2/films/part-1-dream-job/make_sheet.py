#!/usr/bin/env python3
"""make_sheet.py — Muse finds the dream job (Assignment 2, Part 1 film).

13 beats, four acts. Run: python3 make_sheet.py
"""
import json

BS = {
    "title": "Muse finds the dream job",
    "film": "A2-1",
    "series": "Branding and AI — how Muse would do the assignments",
    "beats": [
        {
            "id": "BIDEA", "scene": "M01", "dur_s": 18, "act": "hook",
            "voice": "Muse",
            "line": "The assignment says: find one real job posting you could apply to in six to twelve months. The trap is picking the posting that flatters you. Here's how to do it honestly — machine ranks, human decides.",
            "screen": "Student reaching for the shiniest posting; a red flag."
        },
        {
            "id": "BDEFS", "scene": "M02", "dur_s": 22, "act": "hook",
            "voice": "Muse",
            "line": "Four terms. Scheme: the written matching rules between your résumé and the postings. Flag: a posting the rules mark relevant. Rank: the machine's ordering. Override: the human overruling it — which is the whole point.",
            "screen": "Four terms: scheme / flag / rank / override."
        },
        {
            "id": "B01", "scene": "M03", "dur_s": 22, "act": "1",
            "voice": "Muse",
            "line": "The method. No scrolling the careers page. Run the greenhouse-watch skill against Figma's public Greenhouse board with a matching scheme — version bear-figma-0.1 — written for this pass. One fetch, every open posting, raw response saved.",
            "screen": "Skill + scheme cards: greenhouse-watch, bear-figma-0.1."
        },
        {
            "id": "B02", "scene": "M04", "dur_s": 20, "act": "1",
            "voice": "Muse",
            "line": "One hundred fifty-two open postings in. Forty-nine flagged relevant, one hundred three skipped. Every flag is a string-match rule between a named résumé field and a named posting field. No model judgment anywhere in the loop.",
            "screen": "Funnel: 152 -> 49 flagged, 103 skipped."
        },
        {
            "id": "B03", "scene": "M05", "dur_s": 22, "act": "2",
            "voice": "Muse",
            "line": "And here is where it gets interesting. The top scores — eleven point five — are AI Applied Scientist, Forward Deployed Engineer, and Marketing Engineer. Full-time engineering roles. They match the skills. They do not match the goal.",
            "screen": "Three top-scoring roles, crossed out."
        },
        {
            "id": "B04", "scene": "M06", "dur_s": 22, "act": "2",
            "voice": "Muse",
            "line": "The machine stops there. Choosing among the forty-nine was the human's call — and the choice is not the top score. The ranking did its job: it filtered the reading list. The decision was never the ranking's to make.",
            "screen": "A hand overruling the ranked list; Designer Advocate chosen."
        },
        {
            "id": "B05", "scene": "M07", "dur_s": 22, "act": "3",
            "voice": "Muse",
            "line": "The honesty, part one: the gap. The posting wants deep, hands-on Figma design-systems expertise. The honest answer: never shipped a design system in Figma. The Madison project exists to close exactly that gap — stated on the page, not hidden.",
            "screen": "Gap card: never shipped a design system in Figma."
        },
        {
            "id": "B06", "scene": "M08", "dur_s": 22, "act": "3",
            "voice": "Muse",
            "line": "The honesty, part two: the disappointment. Zero part-time, contract, freelance, or consulting roles on the entire board. No Education, Learning, Curriculum, or Content titles at all. The dream job is full-time, hub-only — and the page says so.",
            "screen": "Empty shelf: 0 part-time roles; missing titles."
        },
        {
            "id": "B07", "scene": "M09", "dur_s": 22, "act": "4",
            "voice": "Muse",
            "line": "The answer: Designer Advocate, Figma. Full-time, US hubs, one hundred fifty-three to three hundred seventeen thousand dollars, posted September first. The job is making written, visual, and video teaching material for the design community — which is already the day job.",
            "screen": "Answer card: Designer Advocate, $153K-$317K."
        },
        {
            "id": "B08", "scene": "M10", "dur_s": 20, "act": "4",
            "voice": "Muse",
            "line": "The runner-up, kept for later: Researcher, Figma Agentic Experiences. The one remote-OK role, about evaluating AI where 'did it work' is a judgment call. It wants seven-plus years of UX research — which is not on the résumé. Honesty again.",
            "screen": "Runner-up card: Researcher, Agentic Experiences."
        },
        {
            "id": "BVDT", "scene": "M11", "dur_s": 26, "act": "recap",
            "voice": "Muse",
            "line": "So: act one, the method — one fetch, a written scheme, forty-nine flagged, no model judgment. Act two, the override — the top scores were wrong for the goal, and the human chose. Act three, the honesty — a real gap, a real disappointment, both on the page. Act four, the answer — Designer Advocate, with a runner-up kept honestly.",
            "screen": "Four recap lines, one per act."
        },
        {
            "id": "BHTF", "scene": "M11", "dur_s": 20, "act": "do_today",
            "voice": "Muse",
            "line": "Your turn. Write your matching scheme before you look at a single posting. Then, when the top score isn't your goal, overrule it — in writing.",
            "screen": "Do-today card: write the scheme first; overrule in writing."
        },
        {
            "id": "BOUT", "scene": "M11", "dur_s": 14, "act": "outro",
            "voice": "Muse",
            "line": "Muse, in for Bear. Thanks for watching. Next: widening the search.",
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
