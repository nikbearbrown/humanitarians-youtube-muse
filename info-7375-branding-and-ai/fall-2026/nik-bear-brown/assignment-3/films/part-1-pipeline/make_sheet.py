#!/usr/bin/env python3
"""make_sheet.py — Muse builds the pipeline (Assignment 3, Part 1 film).

14 beats, four acts. Run: python3 make_sheet.py
"""
import json

BS = {
    "title": "Muse builds the pipeline",
    "film": "A3-1",
    "series": "Branding and AI — how Muse would do the assignments",
    "beats": [
        {
            "id": "BIDEA", "scene": "M01", "dur_s": 18, "act": "hook",
            "voice": "Muse",
            "line": "Before the pipeline runs, you write down what you expect it to do — and what would prove it failed. Sealed, dated, before a single posting is fetched. That envelope is the whole assignment.",
            "screen": "Sealed envelope labeled predictions; pipeline behind it."
        },
        {
            "id": "BDEFS", "scene": "M02", "dur_s": 22, "act": "hook",
            "voice": "Muse",
            "line": "Four terms. Prediction: what you expect, written before the run. Filter: the rules that keep or reject each posting. Kept: the records worth your time. Re-derivable: the run reproduced from saved raw data, byte-identical — or it isn't evidence.",
            "screen": "Four terms: prediction / filter / kept / re-derivable."
        },
        {
            "id": "B01", "scene": "M03", "dur_s": 24, "act": "1",
            "voice": "Muse",
            "line": "The predictions, written September twenty-sixth, before anything ran. One: the record count will be the problem, not the plumbing — expect to need twenty to thirty companies. Two: culture blurbs will cause more than a quarter of false positives. Three: the false negatives will be title-only matches you never see. Four: SmartRecruiters will be the slowest and most fragile source.",
            "screen": "Four prediction cards, dated before the run."
        },
        {
            "id": "B02", "scene": "M04", "dur_s": 22, "act": "1",
            "voice": "Muse",
            "line": "And the failure condition, fixed in writing: if the filter keeps fewer than fifty records after widening to twenty companies, the approach has failed — and loosening the filter to hit a record count is, quote, 'the specific dishonesty this prediction exists to catch.'",
            "screen": "The failure condition, stamped."
        },
        {
            "id": "B03", "scene": "M05", "dur_s": 22, "act": "2",
            "voice": "Muse",
            "line": "The pipeline itself, three steps. Download: every open posting from each board, raw response saved, dated, untouched. Filter: role words in titles, topic words in bodies, flexible-terms phrases. Write: the matches to jobs-of-interest — JSON and CSV.",
            "screen": "Three-step pipeline: download -> filter -> write."
        },
        {
            "id": "B04", "scene": "M06", "dur_s": 22, "act": "2",
            "voice": "Muse",
            "line": "Three applicant-tracking systems, three JSON shapes, three normalizers: Greenhouse, Ashby, SmartRecruiters. No key, no login, no account for any of them. The field names stay the source's own — the script's decisions go under one separate key called matched, so you can always tell what the company said from what the script decided.",
            "screen": "Three ATS cards feeding one file; the matched key."
        },
        {
            "id": "B05", "scene": "M07", "dur_s": 22, "act": "2",
            "voice": "Muse",
            "line": "What it refuses. A posting with no title, no link, or no date is not written — those three fields are what make a record usable. A dead source is logged as unavailable while the other two keep going. Duplicates collapse on source plus id. Refusal is a feature.",
            "screen": "Refusal list: three cards."
        },
        {
            "id": "B06", "scene": "M08", "dur_s": 22, "act": "3",
            "voice": "Muse",
            "line": "The run. Eighteen boards, three thousand four hundred forty-six postings, ninety-seven kept. Every kept record names the words that matched and the field they matched in. Every rejected one carries its reason.",
            "screen": "Funnel: 3,446 -> 97 kept."
        },
        {
            "id": "B07", "scene": "M09", "dur_s": 22, "act": "3",
            "voice": "Muse",
            "line": "What the target became. It started as advocate or educator roles. It's now any job whose product is teaching materials — for universities, the public, or the company's own staff. Anthropic's Technical Documentation and Content Engineer for Claude Docs is the model the new rule was built around.",
            "screen": "Target card morphs to the new definition."
        },
        {
            "id": "B08", "scene": "M10", "dur_s": 22, "act": "3",
            "voice": "Muse",
            "line": "The one that should not have been missed. Replit's Learning Experiences Creator — as close to a bullseye as the boards had. The filter rejected it because the list held 'learning designer' and not 'learning experiences.' One word. It's in the quality report, with the blame attached.",
            "screen": "One word highlighted: learning experiences vs learning designer."
        },
        {
            "id": "B09", "scene": "M11", "dur_s": 24, "act": "4",
            "voice": "Muse",
            "line": "And the acceptance criteria — fixed before checking, in VERIFICATION dot md. Nine of them: re-derivable, field names unchanged, completeness enforced, duplicates, dead sources, dates, counted not estimated, two records checked by hand, rejects read not just counted. The file opens with 'Nothing has been verified yet.' That's the discipline.",
            "screen": "Nine checklist rows."
        },
        {
            "id": "BVDT", "scene": "M12", "dur_s": 26, "act": "recap",
            "voice": "Muse",
            "line": "So: act one, predictions first — four expectations and a failure condition, sealed before the run. Act two, the pipeline — download, filter, write, across three systems, with refusals built in. Act three, the run — three thousand four hundred forty-six to ninety-seven, a moved target, a bullseye missed by one word. Act four, verification — nine criteria, fixed before checking.",
            "screen": "Four recap lines, one per act."
        },
        {
            "id": "BHTF", "scene": "M12", "dur_s": 20, "act": "do_today",
            "voice": "Muse",
            "line": "Your turn. Before your next pipeline runs, write the prediction and the failure condition. Date it. Then let the run embarrass you.",
            "screen": "Do-today card: write the prediction; date it."
        },
        {
            "id": "BOUT", "scene": "M12", "dur_s": 14, "act": "outro",
            "voice": "Muse",
            "line": "Muse, in for Bear. Thanks for watching. Next: auditing the pipeline.",
            "screen": "Nik Bear Brown watermark card."
        }
    ]
}

if __name__ == "__main__":
    assert len(BS["beats"]) == 14, len(BS["beats"])
    acts = [b["id"] for b in BS["beats"] if b["act"] in ("1", "2", "3", "4")]
    assert len(acts) == 9, len(acts)
    total = sum(b["dur_s"] for b in BS["beats"])
    print(f"beats={len(BS['beats'])} body={len(acts)} total={total}s (~{total//60}m{total%60:02d}s)")
    with open("beat_sheet.json", "w") as f:
        json.dump(BS, f, indent=2)
    print("beat_sheet.json written")
