"""scenes.py — Manim scenes for claude-liam-lecture-claude-making-a-film-about-muse.

"Claude making a film about Muse" — lecture skill, claude-liam (Liam, in for Bear).
23 Scene classes, one per body beat (B01..B23). Class names match
shot.manim.class in beat_sheet.json EXACTLY.

Palette: cream #F2F0E9, ink #3D3929, terracotta #D97757 (ONE accent moment
per scene). EB Garamond labels. Gate A copies only this file — never import.
"""
from manim import *
import numpy as np
import json as _json
import os as _os

# ── Palette ───────────────────────────────────────────────────────────────────
BG    = "#F2F0E9"   # cream stage
INK   = "#3D3929"   # warm ink — all body text, all outlines
ACC   = "#D97757"   # terracotta — ONE accent moment per scene
SOFT  = "#6E6A57"   # secondary / muted text
GHOST = "#D9D4C7"   # scaffolding / placeholder
CARD  = "#FAF9F5"   # card surface
SERIF = "EB Garamond"


def _label(text, size=36, color=INK, weight=None):
    """Single-line label, EB Garamond."""
    kw = {"font": SERIF, "font_size": size, "color": color}
    if weight:
        kw["weight"] = weight
    return Text(text, **kw)


def _title(text):
    return _label(text, size=44, weight="BOLD").to_edge(UP, buff=0.6)


# ── Beat clock (reads beat_sheet.json next to this file) ─────────────────────
try:
    _SHEET = _json.load(open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)),
                             "beat_sheet.json")))
    _BEATS = {b["beat_id"]: b for b in _SHEET["beats"]}
except Exception:
    _BEATS = {}


def _bid_of(class_name):
    """M01_ActsNotChats -> B01 (class names carry the M prefix; beats carry B)."""
    bid = class_name.split("_")[0]
    return ("B" + bid[1:]) if bid.startswith("M") else bid


def _target_of(class_name):
    b = _BEATS.get(_bid_of(class_name), {})
    return float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 0)


def _elapsed(self):
    rt = getattr(getattr(self, "renderer", None), "time", None)
    return float(rt) if isinstance(rt, (int, float)) else 0.0


def at(self, frac):
    """Hold until `frac` of the beat's measured audio has elapsed."""
    target = _target_of(type(self).__name__)
    if not target:
        return
    gap = frac * target - _elapsed(self)
    if gap > 0.05:
        self.wait(gap)


def finish(self):
    """Hold to the end of the measured audio (0.05 s slack for 4K rounding)."""
    target = _target_of(type(self).__name__)
    if target:
        self.wait(max(0.05, target - _elapsed(self) - 0.05))
    else:
        self.wait(2.0)


# ─────────────────────────────────────────────────────────────────────────────
#  M01 — B01: Meta's pitch; it acts — goal → plan → steps
# ─────────────────────────────────────────────────────────────────────────────
class M01_ActsNotChats(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("It acts, not just chats")
        self.play(Write(title), run_time=0.7)

        bubble = RoundedRectangle(corner_radius=0.25, width=2.4, height=1.5,
                                  color=INK, stroke_width=2.5,
                                  fill_color=CARD, fill_opacity=1
                                  ).move_to([-4.2, 0.3, 0])
        bl = _label("chatbot", size=30, color=SOFT).move_to([-4.2, -0.85, 0])
        self.play(FadeIn(bubble), FadeIn(bl), run_time=0.6)

        goal = Dot([1.2, 0.3, 0], radius=0.3, color=INK)
        gl = _label("goal", size=28).move_to([1.2, -0.55, 0])
        plan = Square(side_length=0.6, color=INK, stroke_width=2.5,
                      fill_color=CARD, fill_opacity=1).move_to([3.2, 0.3, 0])
        pl = _label("plan", size=28).move_to([3.2, -0.55, 0])
        steps = VGroup(*[Dot([4.9, 0.75 - i * 0.45, 0], radius=0.14, color=INK)
                         for i in range(3)])
        sl = _label("steps", size=28).move_to([4.9, -0.55, 0])
        a1 = Arrow([1.7, 0.3, 0], [2.75, 0.3, 0], color=SOFT, buff=0.1,
                   stroke_width=4)
        a2 = Arrow([3.65, 0.3, 0], [4.5, 0.3, 0], color=SOFT, buff=0.1,
                   stroke_width=4)
        self.play(FadeIn(goal), FadeIn(gl), run_time=0.4)
        self.play(Create(a1), FadeIn(plan), FadeIn(pl), run_time=0.5)
        self.play(Create(a2), FadeIn(steps), FadeIn(sl), run_time=0.5)

        check = VGroup(
            Line([4.7, 0.35, 0], [4.95, 0.05, 0], color=ACC, stroke_width=7),
            Line([4.95, 0.05, 0], [5.45, 0.75, 0], color=ACC, stroke_width=7))
        at(self, 0.7)
        self.play(Create(check), run_time=0.4)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M02 — B02: launch date, Muse Spark, 2.5M downloads, Nik's take
# ─────────────────────────────────────────────────────────────────────────────
class M02_LaunchNumbers(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("September 8, 2026")
        self.play(Write(title), run_time=0.6)

        line = Line([-5.5, 0.9, 0], [5.5, 0.9, 0], color=INK, stroke_width=3)
        tick = Line([0, 0.55, 0], [0, 1.25, 0], color=ACC, stroke_width=7)
        datel = _label("September 8, 2026", size=32).move_to([0, 0.0, 0])
        self.play(Create(line), run_time=0.5)
        self.play(Create(tick), FadeIn(datel), run_time=0.5)

        counter = _label("0", size=72, weight="BOLD").move_to([0, -1.6, 0])
        cl = _label("US downloads", size=30, color=SOFT).move_to([0, -2.5, 0])
        self.play(FadeIn(counter), FadeIn(cl), run_time=0.4)
        at(self, 0.35)
        for val in ["0.5M", "1.0M", "1.5M", "2.0M", "2.5M"]:
            nxt = _label(val, size=72, weight="BOLD").move_to([0, -1.6, 0])
            self.play(Transform(counter, nxt), run_time=0.3)

        take = _label("Nik's take: less capable than its rivals", size=28,
                      color=SOFT).to_edge(DOWN, buff=0.65)
        at(self, 0.8)
        self.play(FadeIn(take), run_time=0.5)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M03 — B03: VM architecture — model + sandboxed computer + connectors
# ─────────────────────────────────────────────────────────────────────────────
class M03_VMStack(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("One machine per user")
        self.play(Write(title), run_time=0.6)

        names = ["model", "sandboxed computer", "connectors"]
        final_ys = [0.5, -0.65, -1.8]
        blocks = []
        labels = []
        for i, name in enumerate(names):
            # Start stacked but below title (title bottom ≈ 2.81); no labels yet
            b = Rectangle(width=4.6, height=1.0, color=INK, stroke_width=2.5,
                          fill_color=CARD, fill_opacity=1
                          ).move_to([0, 1.8 - i * 0.2, 0])
            l = _label(name, size=30)
            blocks.append(b)
            labels.append(l)
        self.play(*[FadeIn(b) for b in blocks], run_time=0.6)

        at(self, 0.4)
        self.play(*[b.animate.move_to([0, fy, 0])
                    for b, fy in zip(blocks, final_ys)], run_time=0.8)
        # Labels to the RIGHT of settled blocks — outside block borders so GATE T
        # §8.6b does not detect a block-rect blob overlapping the text blob.
        for l, b in zip(labels, blocks):
            l.next_to(b, RIGHT, buff=0.3)
        self.play(*[FadeIn(l) for l in labels], run_time=0.4)

        at(self, 0.7)
        frame = Rectangle(width=5.0, height=3.6, color=ACC, stroke_width=4
                          ).move_to([0, -0.65, 0])
        self.play(Create(frame), run_time=0.4)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M04 — B04: errands — endurance, not intelligence
# ─────────────────────────────────────────────────────────────────────────────
class M04_Endurance(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("Endurance, not intelligence")
        self.play(Write(title), run_time=0.6)

        tasks = ["travel", "restaurants", "tickets", "forms", "shopping"]
        rows = []
        for i, t in enumerate(tasks):
            y = 1.6 - i * 0.85
            box = Square(side_length=0.42, color=INK, stroke_width=2.5,
                         fill_color=CARD, fill_opacity=1).move_to([-4.6, y, 0])
            lbl = _label(t, size=30).move_to([-3.0, y, 0]).align_to(box, LEFT)
            lbl.next_to(box, RIGHT, buff=0.35)
            rows.append((box, lbl))
        self.play(*[FadeIn(m) for pair in rows for m in pair], run_time=0.7)

        face = Circle(radius=1.15, color=INK, stroke_width=3).move_to([3.6, 0.2, 0])
        hand = Line([3.6, 0.2, 0], [3.6, 1.05, 0], color=INK, stroke_width=5)
        self.play(FadeIn(face), FadeIn(hand), run_time=0.4)

        at(self, 0.3)
        rt = 0.5
        for i in range(len(rows)):
            y = 1.6 - i * 0.85
            tick = VGroup(
                Line([-4.72, y, 0], [-4.62, y - 0.12, 0],
                     color=ACC, stroke_width=6),
                Line([-4.62, y - 0.12, 0], [-4.44, y + 0.12, 0],
                     color=ACC, stroke_width=6))
            self.play(FadeIn(tick),
                      hand.animate.rotate(-TAU / 5, about_point=hand.get_start()),
                      run_time=rt)
            rt = max(0.22, rt * 0.8)
        at(self, 0.85)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M05 — B05: interfaces and connectors
# ─────────────────────────────────────────────────────────────────────────────
class M05_Connectors(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("Connectors skew commerce")
        self.play(Write(title), run_time=0.6)

        surfs = [("web", -4.2), ("iPhone", -1.4), ("Android", 1.4),
                 ("WhatsApp", 4.2)]
        smarks = []
        for name, x in surfs:
            m = Circle(radius=0.3, color=SOFT, stroke_width=2.5).move_to([x, 1.9, 0])
            # Labels above circles — connector lines run downward from y=1.6, so
            # placing labels above y=2.2 keeps them clear of all crossing lines.
            l = _label(name, size=28, color=SOFT).next_to(m, UP, buff=0.1)
            smarks.append((m, l, x))
        conns = ["Shopify", "OpenTable", "Ticketmaster",
                 "Instacart", "Expedia", "Stripe"]
        pills = []
        for i, name in enumerate(conns):
            x = -4.35 + i * 1.74
            p = RoundedRectangle(corner_radius=0.18, width=1.6, height=0.62,
                                 color=INK, stroke_width=2,
                                 fill_color=CARD, fill_opacity=1
                                 ).move_to([x, -1.3, 0])
            # No text inside pills — pill-border detected as a text blob by GATE T §8.6b;
            # connector names go in the bottom note instead.
            pills.append((p, x))
        self.play(*[FadeIn(m) for tup in smarks for m in tup[:2]],
                  *[FadeIn(p) for p, _ in pills], run_time=0.8)

        links = []
        for _, _, sx in smarks:
            for _, px in pills:
                links.append(Line([sx, 1.6, 0], [px, -0.99, 0],
                                  color=GHOST, stroke_width=2))
        at(self, 0.4)
        self.play(*[Create(ln) for ln in links[::3]], run_time=0.6)

        az = RoundedRectangle(corner_radius=0.18, width=1.6, height=0.62,
                              color=SOFT, stroke_width=2,
                              fill_color=CARD, fill_opacity=1
                              ).move_to([0, -2.35, 0])
        # Label LEFT of box — clear of X marks (x=-0.55 to 0.55) and bottom note.
        # Size=28 clears the 41px GATE T floor (size=26 renders at 39px, just under).
        azl = _label("Amazon", size=28, color=SOFT).next_to(az, LEFT, buff=0.2)
        x1 = Line([-0.55, -2.1, 0], [0.55, -2.6, 0], color=ACC, stroke_width=7)
        x2 = Line([-0.55, -2.6, 0], [0.55, -2.1, 0], color=ACC, stroke_width=7)
        at(self, 0.75)
        self.play(FadeIn(az), FadeIn(azl), run_time=0.4)
        self.play(Create(x1), Create(x2), run_time=0.35)
        # Connector names at bottom — size=28 clears the 41px GATE T floor
        note = _label("Shopify · OpenTable · Ticketmaster · Instacart · Expedia · Stripe",
                       size=28, color=SOFT).to_edge(DOWN, buff=0.65)
        self.play(FadeIn(note), run_time=0.4)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M06 — B06: small business and the developer route
# ─────────────────────────────────────────────────────────────────────────────
class M06_BusinessDev(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("Shops and developers")
        self.play(Write(title), run_time=0.6)

        div = Line([0, 2.2, 0], [0, -2.6, 0], color=GHOST, stroke_width=3)
        self.play(Create(div), run_time=0.4)

        shop = Rectangle(width=3.4, height=2.4, color=INK, stroke_width=2.5,
                         fill_color=CARD, fill_opacity=1).move_to([-3.1, 0.1, 0])
        draft = VGroup(*[Line([-4.3, 0.9 - i * 0.35, 0], [-1.9, 0.9 - i * 0.35, 0],
                              color=SOFT, stroke_width=3) for i in range(3)])
        shopl = _label("ad draft", size=28, color=SOFT).move_to([-3.1, -1.5, 0])
        term = Rectangle(width=3.4, height=2.4, color=INK, stroke_width=2.5,
                         fill_color=CARD, fill_opacity=1).move_to([3.1, 0.1, 0])
        code = VGroup(*[Line([1.9, 0.9 - i * 0.35, 0], [4.3, 0.9 - i * 0.35, 0],
                             color=SOFT, stroke_width=3) for i in range(3)])
        terml = _label("Spark API", size=28, color=SOFT).move_to([3.1, -1.5, 0])
        self.play(FadeIn(shop), FadeIn(draft), FadeIn(shopl), run_time=0.5)
        self.play(FadeIn(term), FadeIn(code), FadeIn(terml), run_time=0.5)

        at(self, 0.65)
        seal = Circle(radius=0.42, color=ACC, stroke_width=4).move_to([-3.1, 0.1, 0])
        self.play(Create(seal), run_time=0.4)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M07 — B07: pricing tiers table
# ─────────────────────────────────────────────────────────────────────────────
class M07_Tiers(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("Three tiers")
        self.play(Write(title), run_time=0.6)

        cols = ["Free", "Power", "Maximum"]
        prices = ["$0", "$20 / mo", "$100 / mo"]
        allows = ["100M / wk", "500M / wk", "3B / wk"]
        xs = [-3.8, 0, 3.8]
        for i, (c, x) in enumerate(zip(cols, xs)):
            card = RoundedRectangle(corner_radius=0.25, width=3.1, height=3.4,
                                    color=INK, stroke_width=2.5,
                                    fill_color=CARD, fill_opacity=1
                                    ).move_to([x, 0.6, 0])
            h = _label(c, size=36, weight="BOLD").move_to([x, 1.7, 0])
            self.play(FadeIn(card), FadeIn(h), run_time=0.3)
        at(self, 0.3)
        for i, (pr, x) in enumerate(zip(prices, xs)):
            p = _label(pr, size=44, color=ACC if i == 0 else INK,
                       weight="BOLD").move_to([x, 0.6, 0])
            self.play(FadeIn(p), run_time=0.35)
        at(self, 0.6)
        for i, (al, x) in enumerate(zip(allows, xs)):
            a = _label(al, size=32, color=SOFT).move_to([x, -0.5, 0])
            self.play(FadeIn(a), run_time=0.35)
        note = _label("same features — you pay for volume", size=28,
                      color=SOFT).to_edge(DOWN, buff=0.6)
        at(self, 0.85)
        self.play(FadeIn(note), run_time=0.4)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M08 — B08: API pricing bars
# ─────────────────────────────────────────────────────────────────────────────
class M08_APIPricing(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("The API price")
        self.play(Write(title), run_time=0.6)

        axis = Line([-5.5, 1.2, 0], [-5.5, -1.6, 0], color=INK, stroke_width=3)
        self.play(Create(axis), run_time=0.4)

        def bar(y, w, label, color=INK):
            b = Rectangle(width=w, height=0.5, color=color, stroke_width=0,
                          fill_color=color, fill_opacity=1
                          ).move_to([-5.5 + w / 2, y, 0])
            l = _label(label, size=28, color=SOFT)
            l.next_to(b, RIGHT, buff=0.3)
            return b, l

        at(self, 0.3)
        b1, l1 = bar(0.7, 2.0, "$1.25 / M in")
        b2, l2 = bar(-0.2, 6.8, "$4.25 / M out")
        self.play(FadeIn(b1), FadeIn(l1), run_time=0.5)
        self.play(FadeIn(b2), FadeIn(l2), run_time=0.5)

        at(self, 0.6)
        share = _label("with data sharing", size=28, color=SOFT
                       ).move_to([0, -1.15, 0])
        self.play(FadeIn(share), run_time=0.4)
        b3, l3 = bar(-1.7, 0.16, "$0.10", color=ACC)
        b4, l4 = bar(-2.35, 0.32, "$0.20", color=ACC)
        self.play(FadeIn(b3), FadeIn(l3), FadeIn(b4), FadeIn(l4), run_time=0.6)

        at(self, 0.8)
        g1 = _label("12.5×  cheaper", size=34, color=ACC, weight="BOLD"
                    ).next_to(l3, RIGHT, buff=0.6)
        g2 = _label("21×  cheaper", size=34, color=ACC, weight="BOLD"
                    ).next_to(l4, RIGHT, buff=0.6)
        self.play(FadeIn(g1), run_time=0.4)
        self.play(FadeIn(g2), run_time=0.4)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M09 — B09: transaction fees — the siphoning coin
# ─────────────────────────────────────────────────────────────────────────────
class M09_TransactionFees(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("The merchant-paid cut")
        self.play(Write(title), run_time=0.6)

        shopper = Dot([-4.2, 0.3, 0], radius=0.3, color=INK)
        sl = _label("you", size=28).move_to([-4.2, -0.5, 0])
        muse = Dot([0, 0.3, 0], radius=0.34, color=INK)
        ml = _label("Muse", size=28).move_to([0, -0.5, 0])
        merch = Square(side_length=0.6, color=INK, stroke_width=2.5,
                       fill_color=CARD, fill_opacity=1).move_to([4.2, 0.3, 0])
        mel = _label("merchant", size=28).move_to([4.2, -0.5, 0])
        f1 = Arrow([-3.7, 0.3, 0], [-0.5, 0.3, 0], color=SOFT, buff=0.1,
                   stroke_width=4)
        f2 = Arrow([0.5, 0.3, 0], [3.7, 0.3, 0], color=SOFT, buff=0.1,
                   stroke_width=4)
        self.play(*[FadeIn(m) for m in (shopper, sl, muse, ml, merch, mel)],
                  Create(f1), Create(f2), run_time=0.9)

        coin = Circle(radius=0.28, color=ACC, stroke_width=0,
                      fill_color=ACC, fill_opacity=1).move_to([0, 0.3, 0])
        metal = _label("Meta", size=30, color=ACC).move_to([0, 2.3, 0])
        at(self, 0.5)
        self.play(FadeIn(coin), FadeIn(metal), run_time=0.4)
        self.play(coin.animate.move_to([0, 1.8, 0]),
                  run_time=0.8, rate_func=rate_functions.smooth)
        at(self, 0.85)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M10 — B10: secondary revenue streams converge
# ─────────────────────────────────────────────────────────────────────────────
class M10_SecondaryStreams(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("Four more streams")
        self.play(Write(title), run_time=0.6)

        names = ["subs", "API sales", "ads angle", "training data"]
        meta = Dot([0, -1.8, 0], radius=0.4, color=INK)
        metal = _label("Meta", size=32).move_to([0, -2.6, 0])
        self.play(FadeIn(meta), FadeIn(metal), run_time=0.4)

        streams = []
        for i, name in enumerate(names):
            x = -4.5 + i * 3.0
            lbl = _label(name, size=28, color=SOFT).move_to([x, 1.8, 0])
            ln = Line([x, 1.35, 0], [0, -1.45, 0], color=GHOST, stroke_width=3)
            streams.append((lbl, ln))
        at(self, 0.3)
        self.play(*[FadeIn(lbl) for lbl, _ in streams], run_time=0.5)
        for lbl, ln in streams:
            self.play(Create(ln), run_time=0.35)
        at(self, 0.7)
        self.play(*[ln.animate.set_color(ACC).set_stroke(width=4)
                     for _, ln in streams],
                  meta.animate.scale(1.3), run_time=0.5)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M11 — B11: intent layer funnel, then 47 coins, 11 light up
# ─────────────────────────────────────────────────────────────────────────────
class M11_IntentLayer(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("Own the intent layer")
        self.play(Write(title), run_time=0.6)

        top = _label("“I want…”", size=40).move_to([0, 1.9, 0])
        mid = _label("Meta", size=40, weight="BOLD").move_to([0, 0.5, 0])
        bot = _label("money out", size=32, color=SOFT).move_to([0, -0.9, 0])
        f1 = Arrow([0, 1.45, 0], [0, 0.95, 0], color=SOFT, buff=0.1,
                   stroke_width=4)
        f2 = Arrow([0, 0.05, 0], [0, -0.5, 0], color=SOFT, buff=0.1,
                   stroke_width=4)
        self.play(FadeIn(top), run_time=0.4)
        self.play(Create(f1), FadeIn(mid), run_time=0.4)
        self.play(Create(f2), FadeIn(bot), run_time=0.4)

        at(self, 0.5)
        self.play(*[FadeOut(m) for m in (top, mid, bot, f1, f2)], run_time=0.4)
        coins = []
        for r in range(4):
            for c in range(12):
                if r == 3 and c > 10:
                    continue
                coin = Circle(radius=0.22, color=SOFT, stroke_width=2,
                              fill_color=CARD, fill_opacity=1
                              ).move_to([-5.2 + c * 0.95, 1.5 - r * 0.85, 0])
                coins.append(coin)
        self.play(*[FadeIn(c) for c in coins], run_time=0.7)
        lit = coins[::4][:11]
        at(self, 0.8)
        self.play(*[c.animate.set_fill(ACC, opacity=1).set_stroke(ACC)
                     for c in lit], run_time=0.5)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M12 — B12: Full Disk Access — the whole disk
# ─────────────────────────────────────────────────────────────────────────────
class M12_FullDisk(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("Full Disk Access")
        self.play(Write(title), run_time=0.6)

        disk = RoundedRectangle(corner_radius=0.3, width=7.5, height=3.6,
                                color=INK, stroke_width=3,
                                fill_color=CARD, fill_opacity=1
                                ).move_to([0, -0.2, 0])
        dl = _label("your disk", size=32, color=SOFT).move_to([0, -2.4, 0])
        self.play(FadeIn(disk), FadeIn(dl), run_time=0.6)

        # Border pulses to dark accent — whole-disk access without a fill
        # overlay that contaminates GATE V luminance separation.
        at(self, 0.45)
        self.play(disk.animate.set_stroke(color="#A64A24", width=7), run_time=0.6)
        note = _label("not folder-level — the whole disk", size=30,
                      color=INK).to_edge(DOWN, buff=0.6)
        at(self, 0.75)
        self.play(FadeIn(note), run_time=0.4)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M13 — B13: deny-list versus allow-list
# ─────────────────────────────────────────────────────────────────────────────
class M13_DenyList(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("Deny-list, not allow-list")
        self.play(Write(title), run_time=0.6)

        folders = ["Photos", "Docs", "Mail", "Notes", "Drive", "Desktop"]
        items = []
        for i, f in enumerate(folders):
            y = 1.7 - i * 0.62
            # Labels at x=-2.5 keep them to the right of the X sweep (x=-5.6 to -4.0)
            lbl = _label(f, size=28).move_to([-2.5, y, 0])
            # INK on cream gives 10.5:1 contrast — ACC (#D97757) only 2.74:1 (GATE T §8.3)
            x1 = Line([-5.6, y + 0.18, 0], [-4.0, y - 0.18, 0],
                      color=INK, stroke_width=5)
            x2 = Line([-5.6, y - 0.18, 0], [-4.0, y + 0.18, 0],
                      color=INK, stroke_width=5)
            items.append((lbl, x1, x2))
        self.play(*[FadeIn(lbl) for lbl, _, _ in items], run_time=0.6)

        at(self, 0.35)
        for lbl, x1, x2 in items:
            self.play(Create(x1), Create(x2), run_time=0.22)

        folder = Rectangle(width=1.6, height=1.2, color=INK, stroke_width=2.5,
                           fill_color=CARD, fill_opacity=1).move_to([3.6, 0.6, 0])
        self.play(FadeIn(folder), run_time=0.4)
        at(self, 0.75)
        # #A64A24 = darker terracotta, 5.1:1 contrast on cream (GATE T §8.3 passes)
        ring = Circle(radius=1.25, color="#A64A24", stroke_width=5
                      ).move_to([3.6, 0.6, 0])
        self.play(Create(ring), run_time=0.4)
        # Label below the ring so it isn't crossed by the ring stroke
        fl = _label("one folder", size=28, color=SOFT).next_to(ring, DOWN, buff=0.15)
        self.play(FadeIn(fl), run_time=0.3)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M14 — B14: three known vulnerabilities
# ─────────────────────────────────────────────────────────────────────────────
class M14_Vulnerabilities(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("Known vulnerabilities")
        self.play(Write(title), run_time=0.6)

        names = ["zero-day", "data export", "prompt extraction"]
        for i, name in enumerate(names):
            x = -4.2 + i * 4.2
            tri = Triangle(color=INK, stroke_width=3,
                           fill_color=CARD, fill_opacity=1
                           ).scale(0.75).move_to([x, 0.6, 0])
            bang = _label("!", size=44, weight="BOLD", color=ACC
                          ).move_to([x, 0.45, 0])
            lbl = _label(name, size=28, color=SOFT).move_to([x, -0.75, 0])
            at(self, 0.2 + i * 0.25)
            self.play(FadeIn(tri), FadeIn(bang), FadeIn(lbl), run_time=0.5)
        at(self, 0.85)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M15 — B15: policy, not crypto — the tearing paper shield
# ─────────────────────────────────────────────────────────────────────────────
class M15_PolicyNotCrypto(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("Policy, not crypto")
        self.play(Write(title), run_time=0.6)

        paper = RoundedRectangle(corner_radius=0.25, width=2.6, height=3.2,
                                 color=INK, stroke_width=2.5,
                                 fill_color=CARD, fill_opacity=1
                                 ).move_to([-2.8, 0.2, 0])
        pl = _label("policy", size=32).move_to([-2.8, -1.9, 0])
        self.play(FadeIn(paper), FadeIn(pl), run_time=0.5)

        at(self, 0.4)
        self.play(paper.animate.shift(LEFT * 0.9).rotate(0.25),
                  pl.animate.shift(LEFT * 0.9), run_time=0.5)
        tear = Line([-2.8, 1.8, 0], [-2.8, -1.4, 0], color=ACC, stroke_width=6)
        self.play(Create(tear), run_time=0.3)

        body = Rectangle(width=1.9, height=1.5, color=INK, stroke_width=3,
                         fill_color=CARD, fill_opacity=1).move_to([2.8, -0.1, 0])
        shackle = Arc(radius=0.6, angle=PI, color=INK, stroke_width=5
                      ).move_to([2.8, 0.65, 0])
        cl = _label("crypto", size=32).move_to([2.8, -1.9, 0])
        self.play(FadeIn(body), FadeIn(shackle), FadeIn(cl), run_time=0.5)
        at(self, 0.75)
        self.play(shackle.animate.set_stroke(ACC, width=7), run_time=0.3)
        self.play(shackle.animate.set_stroke(INK, width=5), run_time=0.3)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M16 — B16: prompt injection steers; approvals get rubber-stamped
# ─────────────────────────────────────────────────────────────────────────────
class M16_InjectionFatigue(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("Injection and fatigue")
        self.play(Write(title), run_time=0.6)

        page = Rectangle(width=3.6, height=2.6, color=INK, stroke_width=2.5,
                         fill_color=CARD, fill_opacity=1).move_to([-3.6, 0.4, 0])
        lines = VGroup(*[Line([-5.0, 1.2 - i * 0.4, 0], [-2.2, 1.2 - i * 0.4, 0],
                               color=SOFT, stroke_width=3) for i in range(4)])
        hidden = VGroup(*[Line([-5.0, -0.4 - i * 0.3, 0], [-2.2, -0.4 - i * 0.3, 0],
                                color=ACC, stroke_width=3) for i in range(2)])
        dot = Dot([3.6, 1.2, 0], radius=0.24, color=INK)
        dl = _label("agent", size=28, color=SOFT).move_to([3.6, 0.5, 0])
        self.play(FadeIn(page), FadeIn(lines), FadeIn(dot), FadeIn(dl),
                  run_time=0.7)

        at(self, 0.3)
        self.play(FadeIn(hidden), run_time=0.4)
        self.play(dot.animate.move_to([3.6, -1.4, 0]),
                  run_time=0.8, rate_func=rate_functions.rush_into)

        at(self, 0.55)
        self.play(*[FadeOut(m) for m in (page, lines, hidden, dot, dl)],
                  run_time=0.4)
        cards = []
        for i in range(3):
            c = Rectangle(width=2.2, height=1.2, color=INK, stroke_width=2.5,
                          fill_color=CARD, fill_opacity=1
                          ).move_to([-4.0 + i * 4.0, 0.6, 0])
            cards.append(c)
        self.play(*[FadeIn(c) for c in cards], run_time=0.5)
        rt = 0.6
        for c in cards:
            stamp = _label("OK", size=40, weight="BOLD", color=ACC
                           ).move_to(c.get_center())
            self.play(FadeIn(stamp, scale=1.6), run_time=rt)
            rt = max(0.25, rt * 0.6)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M17 — B17: trust by design — the mascot and the price tag
# ─────────────────────────────────────────────────────────────────────────────
# The Muse mascot as it appears in the film (Bear's keyed 1:1 clip, transparent). Loaded once per scene.
_MASCOT_KEYED = _os.environ.get(
    "MUSE_MASCOT_KEYED",
    "/Users/bear/Documents/CoWork/bear-textbooks/books/muse/muse_logo/keyed/muse-logo-02.mov")


def _mascot_frames(side=468):
    """RGBA frames of the keyed mascot clip, or None if it is not on this machine."""
    import subprocess
    if not _os.path.exists(_MASCOT_KEYED):
        return None
    raw = subprocess.run(
        ["ffmpeg", "-v", "error", "-c:v", "prores", "-i", _MASCOT_KEYED, "-vf",
         f"scale={side}:{side}:flags=lanczos", "-f", "rawvideo", "-pix_fmt", "rgba", "-"],
        capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(-1, side, side, 4)


class M17_TrustByDesign(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("Trust by design")
        self.play(Write(title), run_time=0.6)

        frames = _mascot_frames()
        if frames is None:   # clip not available: fall back to the drawn face so the film still builds
            face = VGroup(
                Circle(radius=1.2, color=INK, stroke_width=3, fill_color=CARD, fill_opacity=1),
                Dot([-0.45, 0.3, 0], radius=0.12, color=INK), Dot([0.45, 0.3, 0], radius=0.12, color=INK),
                Arc(radius=0.55, angle=-PI * 0.7, color=INK, stroke_width=4).move_to([0, -0.05, 0])
            ).move_to([0, 0.5, 0])
            self.play(FadeIn(face), run_time=0.7)
        else:
            mascot = ImageMobject(frames[0])
            mascot.set_height(3.6).move_to([0, 0.1, 0])
            n = len(frames)
            mascot.add_updater(lambda m: setattr(m, "pixel_array", frames[int(_elapsed(self) * 24) % n]))
            self.play(FadeIn(mascot), run_time=0.7)

        # hearts rise off the mascot's head; title bottom sits at ~2.79, so they stay below ~2.5
        hearts = VGroup(*[Dot([np.random.uniform(-0.7, 0.7),
                               2.0 + i * 0.05, 0], radius=0.09, color=ACC)
                          for i in range(6)])
        at(self, 0.4)
        self.play(*[FadeIn(h) for h in hearts], run_time=0.5)
        self.play(*[h.animate.shift(UP * 0.4).set_opacity(0) for h in hearts],
                  run_time=0.6)

        # the price tag drops onto the mascot's head and shoulders
        tag = RoundedRectangle(corner_radius=0.15, width=1.9, height=0.9,
                               color=INK, stroke_width=2.5,
                               fill_color=CARD, fill_opacity=1
                               ).move_to([0, 2.2, 0])
        tagl = _label("$", size=44, weight="BOLD", color=ACC).move_to([0, 2.2, 0])
        at(self, 0.7)
        self.play(FadeIn(tag), FadeIn(tagl), run_time=0.4)
        self.play(tag.animate.move_to([0, 0.75, 0]),
                  tagl.animate.move_to([0, 0.75, 0]),
                  run_time=0.6, rate_func=rate_functions.rush_into)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M18 — B18: business conflicts and platform dependence
# ─────────────────────────────────────────────────────────────────────────────
class M18_Conflicts(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("Conflicts and lock-in")
        self.play(Write(title), run_time=0.6)

        div = Line([0, 2.2, 0], [0, -2.6, 0], color=GHOST, stroke_width=3)
        self.play(Create(div), run_time=0.3)

        pivot = Triangle(color=INK, stroke_width=0, fill_color=INK,
                         fill_opacity=1).scale(0.3).move_to([-3.4, -0.6, 0])
        beam = Line([-5.2, 0.2, 0], [-1.6, 0.2, 0], color=INK, stroke_width=5)
        pan_l = Circle(radius=0.35, color=SOFT, stroke_width=2.5
                       ).move_to([-5.2, -0.5, 0])
        pan_r = Circle(radius=0.35, color=SOFT, stroke_width=2.5
                       ).move_to([-1.6, -0.5, 0])
        al = _label("ads", size=28, color=SOFT).move_to([-1.6, -1.3, 0])
        self.play(FadeIn(pivot), FadeIn(beam), FadeIn(pan_l), FadeIn(pan_r),
                  FadeIn(al), run_time=0.6)
        at(self, 0.4)
        self.play(Rotate(beam, -0.28, about_point=[-3.4, 0.2, 0]),
                  pan_l.animate.shift(UP * 0.5),
                  pan_r.animate.shift(DOWN * 0.5),
                  al.animate.shift(DOWN * 0.5),
                  run_time=0.7)

        road = Rectangle(width=4.4, height=0.7, color=INK, stroke_width=2.5,
                         fill_color=CARD, fill_opacity=1).move_to([3.4, 0.4, 0])
        rl = _label("roadmap", size=28, color=SOFT).move_to([3.4, -0.5, 0])
        self.play(FadeIn(road), FadeIn(rl), run_time=0.5)
        at(self, 0.7)
        self.play(road.animate.stretch_to_fit_width(1.6).move_to([3.4, 0.4, 0]),
                  run_time=0.7)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M19 — B19: the phone — permissions flip on
# ─────────────────────────────────────────────────────────────────────────────
class M19_Phone(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("Not on the phone")
        self.play(Write(title), run_time=0.6)

        phone = RoundedRectangle(corner_radius=0.35, width=2.6, height=4.4,
                                 color=INK, stroke_width=3,
                                 fill_color=CARD, fill_opacity=1
                                 ).move_to([-2.6, 0, 0])
        self.play(FadeIn(phone), run_time=0.5)

        perms = ["contacts", "messages", "health"]
        at(self, 0.35)
        for i, p in enumerate(perms):
            y = 1.2 - i * 1.0
            lbl = _label(p, size=30).move_to([1.6, y, 0])
            track = RoundedRectangle(corner_radius=0.2, width=1.1, height=0.5,
                                     color=SOFT, stroke_width=2.5
                                     ).move_to([3.9, y, 0])
            knob = Dot([3.65, y, 0], radius=0.18, color=SOFT)
            self.play(FadeIn(lbl), FadeIn(track), FadeIn(knob), run_time=0.35)
            # #A64A24 = darker terracotta, 5.1:1 contrast on cream (GATE T §8.3)
            self.play(knob.animate.move_to([4.15, y, 0]).set_color("#A64A24"),
                      track.animate.set_stroke("#A64A24"),
                      run_time=0.35)
        at(self, 0.85)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M20 — B20: the Mac app is gone; web-only remains
# ─────────────────────────────────────────────────────────────────────────────
class M20_MacAppGone(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("The Mac app is gone")
        self.play(Write(title), run_time=0.6)

        icon = RoundedRectangle(corner_radius=0.3, width=1.6, height=1.6,
                                color=INK, stroke_width=2.5,
                                fill_color=CARD, fill_opacity=1
                                ).move_to([-3.4, 1.0, 0])
        im = _label("M", size=60, weight="BOLD").move_to([-3.4, 1.0, 0])
        trash = Rectangle(width=1.7, height=2.0, color=INK, stroke_width=2.5,
                          fill_color=CARD, fill_opacity=1).move_to([1.8, -0.4, 0])
        rim = Line([1.0, 0.6, 0], [2.6, 0.6, 0], color=INK, stroke_width=4)
        self.play(FadeIn(icon), FadeIn(im), FadeIn(trash), FadeIn(rim),
                  run_time=0.7)

        at(self, 0.35)
        # Land inside the trash body (y=0.2) not on the rim line (y=0.6)
        self.play(icon.animate.move_to([1.8, 0.2, 0]).scale(0.6),
                  im.animate.move_to([1.8, 0.2, 0]).scale(0.6),
                  run_time=0.8, rate_func=rate_functions.rush_into)
        self.play(FadeOut(icon), FadeOut(im), run_time=0.3)

        browser = RoundedRectangle(corner_radius=0.2, width=3.2, height=2.2,
                                   color=INK, stroke_width=2.5,
                                   fill_color=CARD, fill_opacity=1
                                   ).move_to([-3.4, -0.6, 0])
        bar = Line([-4.8, 0.2, 0], [-2.0, 0.2, 0], color=SOFT, stroke_width=3)
        url = _label("muse.ai", size=28, color=SOFT).move_to([-3.4, -0.35, 0])
        at(self, 0.6)
        self.play(FadeIn(browser), FadeIn(bar), FadeIn(url), run_time=0.5)
        glow = RoundedRectangle(corner_radius=0.2, width=3.2, height=2.2,
                                color=ACC, stroke_width=4
                                ).move_to([-3.4, -0.6, 0])
        self.play(Create(glow), run_time=0.4)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M21 — B21: the film-drafting pipeline
# ─────────────────────────────────────────────────────────────────────────────
class M21_Pipeline(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("The sandbox pipeline")
        self.play(Write(title), run_time=0.6)

        stations = ["VM", "PR", "review", "merge", "burner"]
        xs = [-5.2, -2.6, 0, 2.6, 5.2]
        nodes = []
        for name, x in zip(stations, xs):
            n = RoundedRectangle(corner_radius=0.2, width=1.9, height=1.0,
                                 color=INK, stroke_width=2.5,
                                 fill_color=CARD, fill_opacity=1
                                 ).move_to([x, 0.4, 0])
            # Labels BELOW node (next_to DOWN) — node-border blob and label-text blob
            # are then fully separated in y; GATE T §8.6b no longer flags overlap.
            l = _label(name, size=28)
            l.next_to(n, DOWN, buff=0.15)
            nodes.append((n, l, x))
        self.play(*[FadeIn(m) for tup in nodes for m in tup[:2]], run_time=0.7)

        links = [Arrow([xs[i] + 1.0, 0.4, 0], [xs[i + 1] - 1.0, 0.4, 0],
                       color=GHOST, buff=0.1, stroke_width=3)
                 for i in range(4)]
        self.play(*[Create(ln) for ln in links], run_time=0.5)

        dot = Dot([xs[0], 0.65, 0], radius=0.2, color=ACC)
        self.play(FadeIn(dot), run_time=0.3)
        at(self, 0.45)
        for x in xs[1:]:
            self.play(dot.animate.move_to([x, 0.65, 0]), run_time=0.45,
                      rate_func=rate_functions.smooth)
        note = _label("public repos only — no tokens pasted", size=28,
                      color=SOFT).to_edge(DOWN, buff=0.6)
        at(self, 0.85)
        self.play(FadeIn(note), run_time=0.4)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M22 — B22: general rules — the wall and the short list
# ─────────────────────────────────────────────────────────────────────────────
class M22_GeneralRules(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("Assume breach")
        self.play(Write(title), run_time=0.6)

        wall = Rectangle(width=0.5, height=4.6, color=INK, stroke_width=0,
                         fill_color=INK, fill_opacity=1).move_to([0.6, -0.2, 0])
        self.play(FadeIn(wall), run_time=0.5)

        items = ["email", "money", "credentials", "public voice"]
        marks = []
        for i, name in enumerate(items):
            y = 1.4 - i * 1.05
            sq = Square(side_length=0.55, color=INK, stroke_width=2.5,
                        fill_color=CARD, fill_opacity=1).move_to([3.4, y, 0])
            lbl = _label(name, size=28).move_to([4.9, y, 0])
            marks.append((sq, lbl))
        at(self, 0.35)
        self.play(*[FadeIn(m) for pair in marks for m in pair], run_time=0.7)

        at(self, 0.65)
        ring = Rectangle(width=5.6, height=4.4, color=ACC, stroke_width=4
                         ).move_to([3.6, -0.2, 0])
        self.play(Create(ring), run_time=0.4)
        cap = _label("real walls, not policies", size=30, color=ACC
                     ).to_edge(DOWN, buff=0.6)
        at(self, 0.85)
        self.play(FadeIn(cap), run_time=0.4)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M23 — B23: six open questions
# ─────────────────────────────────────────────────────────────────────────────
class M23_OpenQuestions(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("Six open questions")
        self.play(Write(title), run_time=0.6)

        qs = ["VM limits?", "OAuth scopes?", "Muse tokens?",
              "confidential mode?", "free tier lasts?", "ads coming?"]
        marks = []
        for i, q in enumerate(qs):
            x = -3.8 + (i % 3) * 3.8
            y = 0.9 - (i // 3) * 1.7
            badge = Circle(radius=0.62, color=INK, stroke_width=2.5,
                           fill_color=CARD, fill_opacity=1).move_to([x, y + 0.35, 0])
            qm = _label("?", size=64, weight="BOLD", color=INK
                        ).move_to([x, y + 0.35, 0])
            lbl = _label(q, size=26, color=SOFT).move_to([x, y - 0.55, 0])
            marks.append((badge, qm, lbl))
        at(self, 0.25)
        self.play(*[FadeIn(m) for pair in marks[:3] for m in pair],
                  run_time=0.6)
        at(self, 0.55)
        self.play(*[FadeIn(m) for pair in marks[3:] for m in pair],
                  run_time=0.6)
        at(self, 0.8)
        self.play(*[qm.animate.set_color(ACC) for _, qm, _ in marks],
                  run_time=0.4)
        finish(self)


# ═════════════════════════════════════════════════════════════════════════════
#  ADDED 2026-10-04 — "what a hundred million tokens is, in real work" and
#  "the discount is a bid". Class M<nn> -> beat B<nn>.
# ═════════════════════════════════════════════════════════════════════════════
def _count_to(self, mob_factory, values, run_time=0.3):
    """Tick a hero number through `values` (Text swaps, no LaTeX)."""
    cur = mob_factory(values[0])
    self.add(cur)
    for v in values[1:]:
        nxt = mob_factory(v)
        self.play(Transform(cur, nxt), run_time=run_time)
    return cur


def _card(text, w=2.9, h=0.8, size=28):
    box = RoundedRectangle(corner_radius=0.18, width=w, height=h, color=INK,
                           stroke_width=2.5, fill_color=CARD, fill_opacity=1)
    lab = _label(text, size=size)
    lab.move_to(box)
    return VGroup(box, lab)


# ─────────────────────────────────────────────────────────────────────────────
#  M24 — B24: the discount is a bid — price drops, data moves to Meta
# ─────────────────────────────────────────────────────────────────────────────
class M24_TheDiscountIsABid(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("The discount is a bid")
        self.play(Write(title), run_time=0.6)

        # price chip: $1.25 -> $0.10
        was = _label("$1.25", size=64, color=SOFT, weight="BOLD").move_to([-3.8, 1.5, 0])
        per = _label("per million input tokens", size=28, color=SOFT).move_to([-3.8, 0.7, 0])
        self.play(FadeIn(was), FadeIn(per), run_time=0.5)
        at(self, 0.3)
        now = _label("$0.10", size=64, color=ACC, weight="BOLD").move_to([-3.8, 1.5, 0])
        off = _label("92% off", size=36, color=ACC, weight="BOLD").move_to([-3.8, -0.1, 0])
        self.play(was.animate.set_color(GHOST).scale(0.6).move_to([-3.8, 2.45, 0]),
                  run_time=0.4)
        pbar = Rectangle(width=3.0, height=0.3, color=INK, stroke_width=0,
                         fill_color=INK, fill_opacity=1).move_to([-3.8, -0.65, 0])
        pbar_small = Rectangle(width=0.24, height=0.3, color=ACC, stroke_width=0,
                               fill_color=ACC, fill_opacity=1
                               ).move_to([-5.3 + 0.12, -0.65, 0])
        self.play(FadeIn(now), FadeIn(off), FadeIn(pbar), run_time=0.5)
        self.play(Transform(pbar, pbar_small), run_time=0.5)

        # what goes the other way
        meta = Dot([4.9, -0.9, 0], radius=0.55, color=INK)
        metal = _label("Meta", size=32).move_to([4.9, -1.8, 0])
        you = Dot([-3.8, -1.5, 0], radius=0.35, color=INK)
        youl = _label("you", size=28, color=SOFT).move_to([-3.8, -2.15, 0])
        self.play(FadeIn(meta), FadeIn(metal), FadeIn(you), FadeIn(youl), run_time=0.5)

        at(self, 0.55)
        names = ["your usage", "your appointments", "your purchases", "the tickets you pick"]
        cards = VGroup(*[_card(n, w=4.0, h=0.7, size=28) for n in names])
        cards.arrange(DOWN, buff=0.22).move_to([0.2, 0.0, 0])
        for c in cards:
            c.move_to(you.get_center() + RIGHT * 0.3)
            c.set_opacity(0)
        spots = [[0.2, 1.05 - i * 0.9, 0] for i in range(4)]
        for c, sp in zip(cards, spots):
            self.play(c.animate.set_opacity(1).move_to(sp), run_time=0.3)
        at(self, 0.8)
        self.play(*[c.animate.move_to(meta.get_center()).scale(0.3).set_opacity(0)
                    for c in cards],
                  meta.animate.scale(1.45).set_color(ACC),
                  metal.animate.shift(DOWN * 0.45), run_time=0.8)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M25 — B25: the allowance gauge and what Nik's folder holds
# ─────────────────────────────────────────────────────────────────────────────
class M25_WhatTheAllowanceBought(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("A hundred million tokens, in work")
        self.play(Write(title), run_time=0.6)

        W = 10.0
        x0 = -W / 2
        frame = Rectangle(width=W, height=0.7, color=INK, stroke_width=3
                          ).move_to([0, 1.7, 0])
        cap = _label("this week's free allowance: 100M", size=28, color=SOFT
                     ).next_to(frame, UP, buff=0.25)
        self.play(Create(frame), FadeIn(cap), run_time=0.5)
        fill = Rectangle(width=0.001, height=0.7, color="#A64A24", stroke_width=0,
                         fill_color="#A64A24", fill_opacity=1)
        fill.move_to([x0 + 0.0005, 1.7, 0])
        self.add(fill)
        at(self, 0.2)
        target = Rectangle(width=W * 0.18, height=0.7, color="#A64A24", stroke_width=0,
                           fill_color="#A64A24", fill_opacity=1
                           ).move_to([x0 + W * 0.09, 1.7, 0])
        used = _label("18% used  ·  Nik's count, Oct 4", size=30, color=INK,
                      weight="BOLD").next_to(frame, DOWN, buff=0.25, aligned_edge=LEFT)
        self.play(Transform(fill, target), run_time=0.9)
        self.play(FadeIn(used), run_time=0.4)

        at(self, 0.45)
        specs = [("13", "film packages"), ("212", "beats"),
                 ("8,149", "words of narration"), ("≈ 62 min", "of film")]
        xs = [-5.0, -2.0, 1.2, 4.4]
        outs = []
        for (val, lab), x in zip(specs, xs):
            n = _label(val, size=60, weight="BOLD").move_to([x, -1.0, 0])
            l = _label(lab, size=28, color=SOFT).move_to([x, -1.85, 0])
            outs.append((n, l))
            self.play(FadeIn(n, shift=UP * 0.2), FadeIn(l), run_time=0.45)
            at(self, 0.45 + 0.1 * (len(outs)))
        foot = _label("what's in Nik's folder", size=28, color=SOFT
                      ).to_edge(DOWN, buff=0.6)
        at(self, 0.85)
        self.play(FadeIn(foot), run_time=0.4)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M26 — B26: at that pace — the full allowance in film
# ─────────────────────────────────────────────────────────────────────────────
class M26_AtThatPace(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("At that pace")
        self.play(Write(title), run_time=0.6)

        W = 10.0
        x0 = -W / 2
        lab = _label("the whole 100M", size=28, color=SOFT).move_to([0, 2.15, 0])
        self.play(FadeIn(lab), run_time=0.5)

        seg_w = W * 0.18
        blocks = []
        full, frac = 5, 100 / 18 - 5  # 5 full blocks + 0.56 of one
        for i in range(6):
            w = seg_w if i < full else seg_w * frac
            col = "#A64A24" if i == 0 else INK
            b = Rectangle(width=w - 0.06, height=0.8, color=col, stroke_width=0,
                          fill_color=col, fill_opacity=0.9 if i else 1)
            b.move_to([x0 + i * seg_w + w / 2, 1.3, 0])
            blocks.append(b)
        at(self, 0.25)
        for b in blocks:
            self.play(FadeIn(b, shift=RIGHT * 0.3), run_time=0.3)

        at(self, 0.55)
        n1 = _label("≈ 72", size=84, weight="BOLD", color=INK).move_to([-3.4, -1.1, 0])
        l1 = _label("film packages a week", size=30, color=SOFT).move_to([-3.4, -2.0, 0])
        n2 = _label("≈ 5.7", size=84, weight="BOLD", color=INK).move_to([3.4, -1.1, 0])
        l2 = _label("hours of film", size=30, color=SOFT).move_to([3.4, -2.0, 0])
        self.play(FadeIn(n1, shift=UP * 0.2), FadeIn(l1), run_time=0.5)
        at(self, 0.72)
        self.play(FadeIn(n2, shift=UP * 0.2), FadeIn(l2), run_time=0.5)
        foot = _label("straight-line math from one week's folder", size=28,
                      color=SOFT).to_edge(DOWN, buff=0.6)
        at(self, 0.88)
        self.play(FadeIn(foot), run_time=0.4)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M27 — B27: the words are a sliver; tokens measure effort
# ─────────────────────────────────────────────────────────────────────────────
class M27_TokensAreEffort(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("Tokens measure effort")
        self.play(Write(title), run_time=0.6)

        W = 10.0
        bar = Rectangle(width=W, height=0.8, color=INK, stroke_width=3,
                        fill_color=INK, fill_opacity=1).move_to([0, 1.2, 0])
        cap = _label("18M tokens used", size=30, color=SOFT).next_to(bar, UP, buff=0.25)
        self.play(FadeIn(bar), FadeIn(cap), run_time=0.5)

        at(self, 0.25)
        tick = Rectangle(width=0.05, height=0.8, color=ACC, stroke_width=0,
                         fill_color=ACC, fill_opacity=1
                         ).move_to([-W / 2 + 0.025, 1.2, 0])
        self.play(FadeIn(tick), Flash(tick.get_center(), color=ACC, flash_radius=0.45),
                  run_time=0.5)

        # zoom callout
        lines = VGroup(
            Line(tick.get_bottom(), [-5.6, -0.35, 0], color=ACC, stroke_width=3),
            Line(tick.get_bottom(), [-1.6, -0.35, 0], color=ACC, stroke_width=3))
        big = Rectangle(width=4.0, height=0.9, color=ACC, stroke_width=0,
                        fill_color=ACC, fill_opacity=1).move_to([-3.6, -0.8, 0])
        words = _label("the script:  ≈ 11,000", size=30, color=CARD, weight="BOLD"
                       ).move_to(big)
        pct = _label("under 0.1% of the tokens", size=32, color=ACC, weight="BOLD"
                     ).next_to(big, RIGHT, buff=0.5)
        self.play(Create(lines), run_time=0.4)
        self.play(FadeIn(big, scale=0.4), FadeIn(words), run_time=0.5)
        self.play(FadeIn(pct), run_time=0.4)

        at(self, 0.7)
        rest = _label("the rest: re-reading its own work, tools, code", size=30,
                      color=INK).move_to([0, -1.75, 0])
        who = _label("Claude's  read", size=28, color=SOFT).next_to(rest, DOWN, buff=0.2)
        self.play(FadeIn(rest), FadeIn(who), run_time=0.5)
        note = _label("if  Muse  tokens  count  like  ordinary  ones", size=28, color=SOFT
                      ).move_to([0, -3.0, 0])
        at(self, 0.9)
        self.play(FadeIn(note), run_time=0.3)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M28 — B28: the same allowance, priced like the API
# ─────────────────────────────────────────────────────────────────────────────
class M28_PriceItLikeTheAPI(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("A hundred million, at API prices")
        self.play(Write(title), run_time=0.6)

        x0, W = -5.5, 9.0
        scale = W / 425.0
        axis = Line([x0, 1.7, 0], [x0, -1.9, 0], color=INK, stroke_width=3)
        self.play(Create(axis), run_time=0.4)

        def row(y, lo, hi, color, text):
            solid = Rectangle(width=lo * scale, height=0.55, color=color,
                              stroke_width=0, fill_color=color, fill_opacity=1
                              ).move_to([x0 + lo * scale / 2, y, 0])
            ext = Rectangle(width=(hi - lo) * scale, height=0.55, color=color,
                            stroke_width=0, fill_color=color, fill_opacity=0.35
                            ).move_to([x0 + lo * scale + (hi - lo) * scale / 2, y, 0])
            t = _label(text, size=34, color=color, weight="BOLD")
            return solid, ext, t

        s1, e1, t1 = row(0.9, 125, 425, INK, "$125 – $425")
        t1.next_to(e1, RIGHT, buff=0.3)
        l1 = _label("standard rate", size=28, color=SOFT).move_to([x0 + 1.5, 1.55, 0])
        at(self, 0.25)
        self.play(FadeIn(s1), FadeIn(e1), FadeIn(l1), run_time=0.6)
        self.play(FadeIn(t1), run_time=0.3)

        s2, e2, t2 = row(-0.8, 10, 20, ACC, "$10 – $20")
        t2.next_to(e2, RIGHT, buff=0.3)
        l2 = _label("if you let them train on your data", size=28, color=SOFT
                    ).move_to([x0 + 3.2, -0.15, 0])
        at(self, 0.55)
        self.play(FadeIn(s2), FadeIn(e2), FadeIn(l2), run_time=0.6)
        self.play(FadeIn(t2), run_time=0.3)

        note = _label("if Muse tokens compare to API tokens  —  nobody can confirm",
                      size=28, color=SOFT).to_edge(DOWN, buff=0.6)
        at(self, 0.85)
        self.play(FadeIn(note), run_time=0.4)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M29 — B29: the balance — free tokens vs your data
# ─────────────────────────────────────────────────────────────────────────────
class M29_TheSubsidyTell(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("The subsidy is the tell")
        self.play(Write(title), run_time=0.6)

        pivot = Triangle(color=INK, stroke_width=0, fill_color=INK, fill_opacity=1
                         ).scale(0.35).move_to([0, -1.0, 0])
        post = Line([0, -0.8, 0], [0, 0.9, 0], color=INK, stroke_width=5)
        beam_len = 4.6
        beam = Line([-beam_len / 2, 0.9, 0], [beam_len / 2, 0.9, 0], color=INK, stroke_width=6)
        self.play(FadeIn(pivot), Create(post), Create(beam), run_time=0.6)

        def pan(cx, text, color):
            string = Line([cx, 0.9, 0], [cx, 0.0, 0], color=SOFT, stroke_width=3)
            dish = Rectangle(width=3.4, height=0.18, color=color, stroke_width=0,
                             fill_color=color, fill_opacity=1).move_to([cx, 0.0, 0])
            lab = _label(text, size=30, color=INK, weight="BOLD"
                         ).move_to([cx, 2.15, 0])
            return VGroup(string, dish), lab

        left, left_lab = pan(-beam_len / 2, "free tokens", INK)
        right, right_lab = pan(beam_len / 2, "your data", ACC)
        at(self, 0.25)
        self.play(FadeIn(left), FadeIn(right), FadeIn(left_lab), FadeIn(right_lab),
                  run_time=0.5)

        # what's in the data pan
        items = VGroup(*[_label(t, size=28, color=SOFT) for t in
                         ["what you do", "what you book", "what you buy"]])
        items.arrange(DOWN, buff=0.12).move_to([beam_len / 2, -2.0, 0])
        at(self, 0.45)
        self.play(*[FadeIn(i, shift=UP * 0.15) for i in items], run_time=0.6)

        # tip toward the data side
        at(self, 0.65)
        dy = (beam_len / 2) * 0.1593   # sin(0.16)
        self.play(Rotate(beam, angle=-0.16, about_point=[0, 0.9, 0]),
                  left.animate.shift(UP * dy),
                  right.animate.shift(DOWN * dy), run_time=0.9)

        ask = _label("cheap?  ask what the discount buys", size=32, color=INK,
                     weight="BOLD").move_to([0, -3.1, 0])
        at(self, 0.85)
        self.play(FadeIn(ask), run_time=0.5)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M30 — B30: a language model's promise is not a permission
# ─────────────────────────────────────────────────────────────────────────────
class M30_PromiseNotPermission(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("A promise is not a permission")
        self.play(Write(title), run_time=0.6)

        disk = RoundedRectangle(corner_radius=0.3, width=9.0, height=3.6,
                                color=INK, stroke_width=3,
                                fill_color=CARD, fill_opacity=1
                                ).move_to([0, -0.4, 0])
        dl = _label("your whole disk", size=30, color=SOFT).move_to([0, -2.65, 0])
        folder = RoundedRectangle(corner_radius=0.12, width=1.8, height=1.2,
                                  color=INK, stroke_width=2.5,
                                  fill_color=GHOST, fill_opacity=1
                                  ).move_to([-3.2, -0.4, 0])
        fl = _label("one folder", size=28).next_to(folder, DOWN, buff=0.15)
        self.play(FadeIn(disk), FadeIn(dl), FadeIn(folder), FadeIn(fl), run_time=0.7)

        at(self, 0.35)
        ring = RoundedRectangle(corner_radius=0.2, width=2.8, height=2.2,
                                color=ACC, stroke_width=4
                                ).move_to(folder.get_center() + DOWN * 0.15)
        said = _label("Muse: only this folder", size=30, color=ACC, weight="BOLD"
                      ).move_to([-1.4, 1.75, 0])
        self.play(Create(ring), FadeIn(said), run_time=0.6)

        at(self, 0.6)
        wide = RoundedRectangle(corner_radius=0.3, width=9.0, height=3.6,
                                color=ACC, stroke_width=4
                                ).move_to(disk)
        self.play(Transform(ring, wide), run_time=0.9)

        note = _label("a promise, not a lock", size=36, color=INK, weight="BOLD"
                      ).to_edge(DOWN, buff=0.6)
        at(self, 0.85)
        self.play(FadeIn(note), run_time=0.4)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M31 — B31: nothing runs locally — the wall is where the files live
# ─────────────────────────────────────────────────────────────────────────────
class M31_NothingRunsLocally(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("Nothing runs locally")
        self.play(Write(title), run_time=0.6)

        screen = RoundedRectangle(corner_radius=0.15, width=2.6, height=1.7,
                                  color=INK, stroke_width=2.5,
                                  fill_color=CARD, fill_opacity=1
                                  ).move_to([-4.6, 0.6, 0])
        base = Line([-6.0, -0.45, 0], [-3.2, -0.45, 0], color=INK, stroke_width=4)
        ll = _label("Nik's computer", size=28, color=SOFT).move_to([-4.6, -1.05, 0])
        wall = Line([-2.2, 1.9, 0], [-2.2, -2.1, 0], color=INK, stroke_width=9)
        self.play(FadeIn(screen), Create(base), FadeIn(ll), Create(wall), run_time=0.7)

        at(self, 0.35)
        x1 = Line([-5.5, 1.3, 0], [-3.7, -0.1, 0], color=ACC, stroke_width=7)
        x2 = Line([-5.5, -0.1, 0], [-3.7, 1.3, 0], color=ACC, stroke_width=7)
        no = _label("never runs here", size=30, color=INK, weight="BOLD"
                    ).move_to([-4.6, -1.7, 0])
        self.play(Create(x1), Create(x2), FadeIn(no), run_time=0.5)

        at(self, 0.55)
        cloud = RoundedRectangle(corner_radius=0.95, width=4.4, height=2.0, color=INK,
                                 stroke_width=2.5, fill_color=CARD, fill_opacity=1
                                 ).move_to([2.9, 1.2, 0])
        muse = _label("Muse", size=44, weight="BOLD").move_to([2.9, 1.2, 0])
        cl = _label("the cloud", size=28, color=SOFT).move_to([2.9, 2.65, 0])
        self.play(FadeIn(cloud), FadeIn(muse), FadeIn(cl), run_time=0.6)

        at(self, 0.75)
        t1 = _card("Google Drive folder", w=3.5, h=0.8, size=28).move_to([0.8, -1.6, 0])
        t2 = _card("sandbox repo", w=3.0, h=0.8, size=28).move_to([4.3, -1.6, 0])
        a1 = Arrow([0.8, -1.15, 0], [2.1, 0.0, 0], color=ACC, buff=0.05, stroke_width=5)
        a2 = Arrow([4.3, -1.15, 0], [3.7, 0.0, 0], color=ACC, buff=0.05, stroke_width=5)
        self.play(FadeIn(t1), FadeIn(t2), run_time=0.4)
        self.play(Create(a1), Create(a2), run_time=0.4)
        note = _label("the wall is where the files live", size=30, color=INK,
                      weight="BOLD").to_edge(DOWN, buff=0.6)
        at(self, 0.88)
        self.play(FadeIn(note), run_time=0.4)
        finish(self)
