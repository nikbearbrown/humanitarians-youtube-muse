#!/usr/bin/env python3
"""make_sheet.py — How to register for a Muse account.

15 beats, four acts. Run: python3 make_sheet.py
"""
import json

BS = {
    "title": "How to register for a Muse account",
    "film": 5,
    "series": "Muse how-to films",
    "beats": [
        {
            "id": "BIDEA", "scene": "M01", "dur_s": 18, "act": "hook",
            "voice": "Muse",
            "line": "Signing up for a new AI account usually means handing a stranger your real credit card. There is a better way: a ten-dollar leash. Here is how to register for Muse without ever giving Meta your real card.",
            "screen": "Credit card on a leash; a $10 tag."
        },
        {
            "id": "BDEFS", "scene": "M02", "dur_s": 22, "act": "hook",
            "voice": "Muse",
            "line": "Four terms. Virtual card: a real card number that isn't your real card. Merchant-locked: it works at exactly one merchant — here, Meta — and nowhere else. Age check: a one-dollar charge that proves you're you, refunded within a week. Muse account: the thing we're actually here for.",
            "screen": "Four terms: virtual card / merchant-locked / age check / Muse account."
        },
        {
            "id": "B01", "scene": "M03", "dur_s": 22, "act": "1",
            "voice": "Muse",
            "line": "Step one: the email. You want an address Meta has never seen. Ours: muse at humanitarians dot ai. A fresh inbox with exactly one job — receiving the login code.",
            "screen": "Envelope; muse@humanitarians.ai."
        },
        {
            "id": "B02", "scene": "M04", "dur_s": 24, "act": "1",
            "voice": "Muse",
            "line": "Step two: the card. At privacy dot com, create a new card. Name it Meta CC. Lock it to the merchant Meta. Set the limit to ten dollars. If anything ever goes wrong, the worst case is ten dollars at one merchant — not your real card, everywhere.",
            "screen": "Card mock: Meta CC, MERCHANT-LOCKED, $10 limit."
        },
        {
            "id": "B03", "scene": "M05", "dur_s": 22, "act": "2",
            "voice": "Muse",
            "line": "Step three: Instagram. Muse signup runs through Meta's accounts, so an Instagram account comes first. Create it with the new email address.",
            "screen": "Phone frame: Instagram login mock."
        },
        {
            "id": "B04", "scene": "M06", "dur_s": 22, "act": "2",
            "voice": "Muse",
            "line": "Then the age check. Confirm your age with a credit card: one dollar charged, refunded in five to seven business days. This is the moment the ten-dollar locked card earns its keep — a real card number, a ten-dollar ceiling, good at exactly one merchant.",
            "screen": "Age-check card: $1.00, refunded in 5-7 days."
        },
        {
            "id": "B05", "scene": "M07", "dur_s": 22, "act": "2",
            "voice": "Muse",
            "line": "See the chain: fresh email, locked card, Instagram account, then Muse. Each step isolates the blast radius of the next. Nothing in this chain can reach your real wallet.",
            "screen": "Chain: email -> locked card -> Instagram -> Muse."
        },
        {
            "id": "B06", "scene": "M08", "dur_s": 20, "act": "3",
            "voice": "Muse",
            "line": "Step four: go to muse dot ai. It asks for a mobile number or email. Enter the new address, and continue.",
            "screen": "muse.ai login mock: email field, Continue button."
        },
        {
            "id": "B07", "scene": "M09", "dur_s": 20, "act": "3",
            "voice": "Muse",
            "line": "Check the inbox. A six-digit code arrives at the new email. Enter it. No password to invent, no password to leak.",
            "screen": "Six code boxes; code sent to muse@humanitarians.ai."
        },
        {
            "id": "B08", "scene": "M10", "dur_s": 24, "act": "3",
            "voice": "Muse",
            "line": "Then the disclosure — and actually read it. Your agent can take actions for you. It works around the clock. And you stay in control: you choose what it can access and what needs your approval. This is the screen most people skip. Don't.",
            "screen": "Disclosure: three rows — actions, around the clock, control."
        },
        {
            "id": "B09", "scene": "M11", "dur_s": 20, "act": "3",
            "voice": "Muse",
            "line": "And you're in. 'Hey! I'm your personal agent, not just a regular assistant.' The account exists, the card on file can't spend more than ten dollars at Meta, and your real card was never involved.",
            "screen": "Chat bubble: the greeting."
        },
        {
            "id": "B10", "scene": "M12", "dur_s": 22, "act": "4",
            "voice": "Muse",
            "line": "The pattern, reusable: whenever a signup demands a credit card, mint a merchant-locked virtual card with a small limit first. Name it after the merchant. The signup gets what it asked for. You keep the keys to the blast radius.",
            "screen": "Pattern card: merchant-locked + small limit + named for merchant."
        },
        {
            "id": "BVDT", "scene": "M13", "dur_s": 26, "act": "recap",
            "voice": "Muse",
            "line": "So: act one, the setup — a fresh email and a ten-dollar card locked to Meta. Act two, the chain — Instagram first, the one-dollar age check, each step isolating the next. Act three, the registration — the code, the disclosure you actually read, and you're in. Act four, the pattern: lock the card, limit the blast radius, every time.",
            "screen": "Four recap lines, one per act."
        },
        {
            "id": "BHTF", "scene": "M13", "dur_s": 20, "act": "do_today",
            "voice": "Muse",
            "line": "Your turn: the next time a service demands your credit card, mint a merchant-locked virtual card first. Set the limit to what the signup is actually worth.",
            "screen": "Do-today card: lock the card before the signup."
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
