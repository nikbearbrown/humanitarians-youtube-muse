"""scenes.py — Manim scenes for part-1-opportunity-matcher.

"Muse builds the opportunity matcher" — lecture skill, claude-liam (Liam, in for Bear).
17 Scene classes, one per body beat (B01..B17). Class names match
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
    """Single-line label, EB Garamond (3x oversample: manimpango 0.18.1
    drops inter-word spaces at small sizes)."""
    kw = {"font": SERIF, "font_size": size * 3, "color": color}
    if weight:
        kw["weight"] = weight
    return Text(text, **kw).scale(1 / 3)


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
    """M01_WhichMatter -> B01 (class names carry the M prefix; beats carry B)."""
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
#  M01 — B01: 3,446 collected, 97 kept — which matter?
# ─────────────────────────────────────────────────────────────────────────────
class M01_WhichMatter(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("3,446 collected — which matter?")
        self.play(Write(title), run_time=0.7)

        pile = VGroup(*[Dot([np.random.uniform(-4.5, 4.5),
                             np.random.uniform(-1.8, 1.2), 0],
                            radius=0.09, color=SOFT)
                        for _ in range(60)])
        self.play(FadeIn(pile), run_time=0.7)
        at(self, 0.3)
        kept = VGroup(*[Dot([-1.5 + (i % 10) * 0.34, 0.6 - (i // 10) * 0.34, 0],
                            radius=0.11, color=INK)
                        for i in range(97)])
        self.play(FadeOut(pile),
                  FadeIn(kept), run_time=0.8)
        kl = _label("97 kept", size=30, color=SOFT).move_to([0, -1.3, 0])
        self.play(FadeIn(kl), run_time=0.4)
        at(self, 0.65)
        qm = _label("?", size=96, weight="BOLD", color=ACC).move_to([0, 2.2, 0])
        self.play(FadeIn(qm, scale=0.5), run_time=0.5)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M02 — B02: collect hands to judge; the stamp lands
# ─────────────────────────────────────────────────────────────────────────────
class M02_CollectJudge(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("Collect, then judge")
        self.play(Write(title), run_time=0.6)

        cbox = RoundedRectangle(corner_radius=0.2, width=2.8, height=1.6,
                               color=INK, stroke_width=2.5,
                               fill_color=CARD, fill_opacity=1
                               ).move_to([-3.4, 0.3, 0])
        cl = _label("collect", size=32).move_to([-3.4, 0.3, 0])
        jbox = RoundedRectangle(corner_radius=0.2, width=2.8, height=1.6,
                               color=INK, stroke_width=2.5,
                               fill_color=CARD, fill_opacity=1
                               ).move_to([3.4, 0.3, 0])
        jl = _label("judge", size=32).move_to([3.4, 0.3, 0])
        self.play(FadeIn(cbox), FadeIn(cl), FadeIn(jbox), FadeIn(jl),
                  run_time=0.7)

        doc = Square(side_length=0.5, color=SOFT, stroke_width=2.5,
                     fill_color=CARD, fill_opacity=1).move_to([-3.4, 0.3, 0])
        arrow = Arrow([-1.8, 0.3, 0], [1.8, 0.3, 0], color=SOFT, buff=0.1,
                      stroke_width=4)
        at(self, 0.35)
        self.play(FadeIn(doc), Create(arrow), run_time=0.4)
        self.play(doc.animate.move_to([3.4, 0.3, 0]), run_time=0.7)
        self.play(FadeOut(doc), run_time=0.2)

        stamp = _label("PURSUE", size=44, weight="BOLD", color=ACC
                       ).move_to([3.4, 0.3, 0])
        at(self, 0.7)
        self.play(FadeIn(stamp, scale=1.5), run_time=0.4)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M03 — B03: five weighted bars merge into one number
# ─────────────────────────────────────────────────────────────────────────────
class M03_FiveDimensions(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("Five dimensions, one score")
        self.play(Write(title), run_time=0.6)

        dims = [("role", 0.30), ("audience", 0.20), ("materials", 0.20),
                ("gap", 0.15), ("company", 0.15)]
        bars = []
        for i, (name, w) in enumerate(dims):
            y = 1.5 - i * 0.85
            bw = w * 14
            b = Rectangle(width=bw, height=0.45, color=INK, stroke_width=0,
                          fill_color=INK, fill_opacity=1
                          ).move_to([-5.5 + bw / 2, y, 0])
            l = _label(f"{name}  {w:.2f}", size=28, color=SOFT)
            l.next_to(b, RIGHT, buff=0.3)
            bars.append((b, l))
        for b, l in bars:
            self.play(FadeIn(b), FadeIn(l), run_time=0.3)

        at(self, 0.55)
        num = _label("0.91", size=96, weight="BOLD", color=ACC
                     ).move_to([2.5, -1.6, 0])
        self.play(*[FadeOut(m) for pair in bars for m in pair],
                  run_time=0.4)
        self.play(FadeIn(num, scale=0.6), run_time=0.6)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M04 — B04: the routing gauge
# ─────────────────────────────────────────────────────────────────────────────
class M04_Routing(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("Routing, not just scoring")
        self.play(Write(title), run_time=0.6)

        gauge = Line([0, -2.2, 0], [0, 2.0, 0], color=INK, stroke_width=5)
        self.play(Create(gauge), run_time=0.5)

        zones = [(0.65, "PURSUE", ACC), (0.45, "NETWORK", INK),
                 (0.25, "WATCH", SOFT)]
        at(self, 0.35)
        for v, name, color in zones:
            y = -2.2 + v * 4.2
            tick = Line([-0.5, y, 0], [0.5, y, 0], color=color, stroke_width=5)
            lbl = _label(f"{name}  {v}", size=30, color=color
                         ).move_to([2.2, y, 0])
            self.play(Create(tick), FadeIn(lbl), run_time=0.35)
        skip = _label("SKIP", size=30, color=SOFT).move_to([2.2, -2.0, 0])
        at(self, 0.7)
        self.play(FadeIn(skip), run_time=0.4)
        dot = Dot([0, -2.2 + 0.91 * 4.2, 0], radius=0.2, color=ACC)
        self.play(FadeIn(dot), run_time=0.3)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M05 — B05: the rationale types its evidence
# ─────────────────────────────────────────────────────────────────────────────
class M05_Rationale(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("Every score shows its work")
        self.play(Write(title), run_time=0.6)

        card = RoundedRectangle(corner_radius=0.25, width=4.6, height=1.4,
                                color=INK, stroke_width=2.5,
                                fill_color=CARD, fill_opacity=1
                                ).move_to([0, 1.6, 0])
        score = _label("0.91 → PURSUE", size=40, weight="BOLD"
                       ).move_to([0, 1.6, 0])
        self.play(FadeIn(card), FadeIn(score), run_time=0.5)

        evs = ["“title matches ‘developer education’”",
               "“rewards CV gap: certification”",
               "“Anthropic demand 1.0”"]
        at(self, 0.4)
        for i, ev in enumerate(evs):
            l = _label(ev, size=28, color=SOFT).move_to([0, 0.3 - i * 0.6, 0])
            ul = Line([-2.6, 0.05 - i * 0.6, 0], [2.6, 0.05 - i * 0.6, 0],
                      color=ACC, stroke_width=3)
            self.play(FadeIn(l), Create(ul), run_time=0.4)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M06 — B06: matcher.py — 714 postings, 3.1 seconds
# ─────────────────────────────────────────────────────────────────────────────
class M06_MatcherPy(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("matcher.py")
        self.play(Write(title), run_time=0.6)

        script = RoundedRectangle(corner_radius=0.2, width=2.2, height=2.8,
                                  color=INK, stroke_width=2.5,
                                  fill_color=CARD, fill_opacity=1
                                  ).move_to([-4.2, 0, 0])
        sl = _label("matcher.py", size=26, color=SOFT).move_to([-4.2, -1.9, 0])
        self.play(FadeIn(script), FadeIn(sl), run_time=0.5)

        docs = VGroup(*[Square(side_length=0.28, color=SOFT, stroke_width=2,
                               fill_color=CARD, fill_opacity=1
                               ).move_to([-6.2, 1.5 - (i % 8) * 0.42, 0])
                        for i in range(16)])
        self.play(FadeIn(docs), run_time=0.5)
        at(self, 0.4)
        self.play(*[d.animate.move_to([4.5, 1.5 - (i % 8) * 0.42, 0])
                     for i, d in enumerate(docs)],
                  run_time=1.0, rate_func=rate_functions.smooth)
        self.play(*[FadeOut(d) for d in docs], run_time=0.3)

        face = Circle(radius=1.0, color=INK, stroke_width=3
                      ).move_to([3.2, 0.2, 0])
        hand = Line([3.2, 0.2, 0], [3.2, 0.95, 0], color=ACC, stroke_width=5)
        t = _label("3.1 s", size=44, weight="BOLD", color=ACC
                   ).move_to([3.2, -1.4, 0])
        at(self, 0.7)
        self.play(FadeIn(face), FadeIn(hand), run_time=0.4)
        self.play(hand.animate.rotate(-TAU * 2.5, about_point=hand.get_start()),
                  FadeIn(t), run_time=0.9)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M07 — B07: the n8n chain
# ─────────────────────────────────────────────────────────────────────────────
class M07_N8n(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("The n8n equivalent")
        self.play(Write(title), run_time=0.6)

        nodes = ["schedule", "fetch", "normalize", "score", "route",
                 "briefs", "email"]
        boxes = []
        for i, name in enumerate(nodes):
            x = -5.4 + i * 1.8
            b = RoundedRectangle(corner_radius=0.15, width=1.6, height=0.9,
                                 color=INK, stroke_width=2.5,
                                 fill_color=CARD, fill_opacity=1
                                 ).move_to([x, 0.5, 0])
            l = _label(name, size=22).move_to([x, 0.5, 0])
            boxes.append((b, l))
        self.play(*[FadeIn(m) for pair in boxes for m in pair], run_time=0.7)

        at(self, 0.45)
        links = [Arrow([-5.4 + i * 1.8 + 0.85, 0.5, 0],
                       [-5.4 + (i + 1) * 1.8 - 0.85, 0.5, 0],
                       color=ACC, buff=0.05, stroke_width=4)
                 for i in range(6)]
        self.play(*[Create(ln) for ln in links], run_time=0.7)
        note = _label("same weights · same thresholds · same decisions",
                      size=28, color=SOFT).to_edge(DOWN, buff=0.6)
        at(self, 0.8)
        self.play(FadeIn(note), run_time=0.4)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M08 — B08: Anthropic's board fills; one posting rises
# ─────────────────────────────────────────────────────────────────────────────
class M08_AnthropicLive(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("Anthropic's board is live")
        self.play(Write(title), run_time=0.6)

        marks = VGroup(*[Square(side_length=0.22, color=SOFT, stroke_width=2,
                                fill_color=CARD, fill_opacity=1
                                ).move_to([-6 + (i % 24) * 0.52,
                                           1.4 - (i // 24) * 0.42, 0])
                         for i in range(120)])
        self.play(FadeIn(marks), run_time=0.8)
        cl = _label("640 postings", size=30, color=SOFT).move_to([0, -1.9, 0])
        self.play(FadeIn(cl), run_time=0.4)

        hero = Square(side_length=0.5, color=ACC, stroke_width=0,
                      fill_color=ACC, fill_opacity=1).move_to([-6, 1.4, 0])
        at(self, 0.55)
        self.play(FadeIn(hero), run_time=0.3)
        self.play(hero.animate.move_to([0, 0.2, 0]).scale(1.6),
                  run_time=0.8, rate_func=rate_functions.smooth)
        hl = _label("Developer Education Lead — 0.91", size=32, color=ACC,
                    weight="BOLD").move_to([0, -0.9, 0])
        self.play(FadeIn(hl), run_time=0.4)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M09 — B09: Meta's board is an empty shell
# ─────────────────────────────────────────────────────────────────────────────
class M09_MetaUnreadable(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("Meta: no readable feed")
        self.play(Write(title), run_time=0.6)

        browser = RoundedRectangle(corner_radius=0.2, width=6.4, height=3.6,
                                   color=INK, stroke_width=2.5,
                                   fill_color=CARD, fill_opacity=1
                                   ).move_to([0, 0, 0])
        bar = Line([-2.9, 1.4, 0], [2.9, 1.4, 0], color=SOFT, stroke_width=3)
        self.play(FadeIn(browser), FadeIn(bar), run_time=0.6)

        at(self, 0.45)
        shell = VGroup(*[Line([-2.4, 0.6 - i * 0.5, 0], [2.4, 0.6 - i * 0.5, 0],
                              color=GHOST, stroke_width=4) for i in range(4)])
        self.play(FadeIn(shell), run_time=0.5)
        nofeed = _label("no public JSON feed", size=32, color=ACC
                        ).move_to([0, -1.1, 0])
        self.play(FadeIn(nofeed), run_time=0.4)
        note = _label("recorded honestly, like Google", size=28, color=SOFT
                      ).to_edge(DOWN, buff=0.6)
        at(self, 0.8)
        self.play(FadeIn(note), run_time=0.4)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M10 — B10: the WATCH bucket overflows
# ─────────────────────────────────────────────────────────────────────────────
class M10_WatchFlood(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("633 in WATCH — noise")
        self.play(Write(title), run_time=0.6)

        names = ["PURSUE", "NETWORK", "WATCH", "SKIP"]
        buckets = []
        for i, name in enumerate(names):
            x = -4.8 + i * 3.2
            b = Rectangle(width=2.4, height=1.8, color=INK, stroke_width=2.5,
                          fill_color=CARD, fill_opacity=1).move_to([x, -0.6, 0])
            l = _label(name, size=28, color=SOFT).move_to([x, -1.9, 0])
            buckets.append((b, x))
        for (b, x), name in zip(buckets, names):
            l = _label(name, size=28, color=SOFT).move_to([x, -1.9, 0])
            self.play(FadeIn(b), FadeIn(l), run_time=0.3)

        drops = VGroup(*[Dot([np.random.uniform(-6, 6), 2.8, 0],
                             radius=0.1, color=SOFT) for _ in range(40)])
        self.play(FadeIn(drops), run_time=0.4)
        at(self, 0.45)
        watch_x = -4.8 + 2 * 3.2
        self.play(*[d.animate.move_to([watch_x + np.random.uniform(-0.9, 0.9),
                                       -0.6 + np.random.uniform(-0.6, 0.6), 0])
                     for d in drops],
                  run_time=0.9, rate_func=rate_functions.smooth)
        at(self, 0.7)
        over = _label("overflow", size=36, weight="BOLD", color=ACC
                      ).move_to([watch_x, 0.9, 0])
        self.play(FadeIn(over), run_time=0.4)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M11 — B11: the pairing rule — fade alone, light up paired
# ─────────────────────────────────────────────────────────────────────────────
class M11_PairingRule(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("The pairing rule")
        self.play(Write(title), run_time=0.6)

        weak = _label("“training”", size=44, weight="BOLD").move_to([-3.2, 0.6, 0])
        alone = _label("alone", size=28, color=SOFT).move_to([-3.2, -0.4, 0])
        badge_l = Circle(radius=1.15, color=GHOST, stroke_width=3
                         ).move_to([-3.2, 0.3, 0])
        self.play(FadeIn(badge_l), FadeIn(weak), FadeIn(alone), run_time=0.5)
        at(self, 0.35)
        self.play(weak.animate.set_opacity(0.25),
                  badge_l.animate.set_stroke(GHOST, opacity=0.4), run_time=0.6)

        badge_r = Circle(radius=1.15, color=GHOST, stroke_width=3
                         ).move_to([3.2, 0.1, 0])
        weak2 = _label("“training”", size=44, weight="BOLD"
                       ).move_to([3.2, 0.6, 0])
        plus = _label("+", size=44, color=SOFT).move_to([3.2, -0.2, 0])
        aud = _label("audience", size=32, color=SOFT).move_to([3.2, -1.1, 0])
        self.play(FadeIn(badge_r), FadeIn(weak2), FadeIn(plus), FadeIn(aud),
                  run_time=0.5)
        at(self, 0.65)
        self.play(weak2.animate.set_color(ACC),
                  aud.animate.set_color(ACC),
                  badge_r.animate.set_stroke(ACC, width=5),
                  run_time=0.5)
        note = _label("weak words need confirmation", size=28, color=SOFT
                      ).to_edge(DOWN, buff=0.6)
        self.play(FadeIn(note), run_time=0.4)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M12 — B12: the bullseye — needle swings 0.46 → 0.66
# ─────────────────────────────────────────────────────────────────────────────
class M12_Bullseye(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("The bullseye: 0.46 → 0.66")
        self.play(Write(title), run_time=0.6)

        arc = Arc(radius=2.2, angle=PI * 0.9, color=INK, stroke_width=5
                  ).move_to([0, -0.6, 0])
        self.play(Create(arc), run_time=0.5)

        pline = Line([-1.6, 1.35, 0], [-1.1, 1.75, 0], color=ACC, stroke_width=5)
        pl = _label("PURSUE 0.65", size=28, color=ACC).move_to([-2.6, 1.9, 0])
        self.play(Create(pline), FadeIn(pl), run_time=0.4)

        needle = Line([0, -0.6, 0], [-1.9, -0.35, 0], color=INK, stroke_width=6)
        nv = _label("0.46", size=36, weight="BOLD").move_to([0, -2.2, 0])
        self.play(FadeIn(needle), FadeIn(nv), run_time=0.5)

        phrase = _label("“own the documentation”", size=32, color=SOFT
                        ).move_to([0, 2.6, 0])
        at(self, 0.45)
        self.play(FadeIn(phrase), run_time=0.4)
        self.play(phrase.animate.move_to([0, 1.0, 0]).set_color(ACC),
                  run_time=0.5)

        at(self, 0.7)
        needle2 = Line([0, -0.6, 0], [-1.35, 1.55, 0], color=ACC, stroke_width=6)
        nv2 = _label("0.66", size=36, weight="BOLD", color=ACC
                     ).move_to([0, -2.2, 0])
        self.play(Transform(needle, needle2), Transform(nv, nv2), run_time=0.7)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M13 — B13: four buckets fill to proportion
# ─────────────────────────────────────────────────────────────────────────────
class M13_Final(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("22 · 37 · 325 · 330")
        self.play(Write(title), run_time=0.6)

        data = [("PURSUE", 22, ACC), ("NETWORK", 37, INK),
                ("WATCH", 325, SOFT), ("SKIP", 330, GHOST)]
        total = 714
        y = 1.6
        for name, n, color in data:
            w = max(0.4, n / total * 11)
            b = Rectangle(width=w, height=0.55, color=color, stroke_width=0,
                          fill_color=color, fill_opacity=1
                          ).move_to([-5.5 + w / 2, y, 0])
            l = _label(f"{name}  {n}", size=28,
                       color=SOFT if color == GHOST else INK)
            l.next_to(b, RIGHT, buff=0.3)
            self.play(FadeIn(b), FadeIn(l), run_time=0.45)
            y -= 0.95
        note = _label("most of the board is not actionable — honestly shown",
                      size=28, color=SOFT).to_edge(DOWN, buff=0.6)
        at(self, 0.8)
        self.play(FadeIn(note), run_time=0.4)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M14 — B14: the outputs land as files
# ─────────────────────────────────────────────────────────────────────────────
class M14_Outputs(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("Files, not JSON")
        self.play(Write(title), run_time=0.6)

        files = ["digest.md", "digest.html", "15 briefs", "run report"]
        for i, name in enumerate(files):
            x = -4.5 + i * 3.0
            f = RoundedRectangle(corner_radius=0.15, width=2.4, height=1.5,
                                 color=INK, stroke_width=2.5,
                                 fill_color=CARD, fill_opacity=1
                                 ).move_to([x, 3.2, 0])
            l = _label(name, size=26).move_to([x, 3.2, 0])
            self.play(FadeIn(f), FadeIn(l), run_time=0.3)
            self.play(f.animate.move_to([x, 0.3, 0]),
                      l.animate.move_to([x, 0.3, 0]),
                      run_time=0.45, rate_func=rate_functions.smooth)
        at(self, 0.75)
        stamp = _label("human-openable", size=32, color=ACC
                       ).to_edge(DOWN, buff=0.6)
        self.play(FadeIn(stamp), run_time=0.4)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M15 — B15: fetch fails, retries, falls back; bad records quarantined
# ─────────────────────────────────────────────────────────────────────────────
class M15_Errors(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("When things break")
        self.play(Write(title), run_time=0.6)

        cloud = RoundedRectangle(corner_radius=0.4, width=2.6, height=1.6,
                                 color=INK, stroke_width=2.5,
                                 fill_color=CARD, fill_opacity=1
                                 ).move_to([-3.8, 1.0, 0])
        cl = _label("board API", size=28, color=SOFT).move_to([-3.8, -0.2, 0])
        self.play(FadeIn(cloud), FadeIn(cl), run_time=0.5)

        x1 = Line([0.2, 0.7, 0], [1.0, 1.4, 0], color=ACC, stroke_width=7)
        x2 = Line([0.2, 1.4, 0], [1.0, 0.7, 0], color=ACC, stroke_width=7)
        at(self, 0.3)
        self.play(Create(x1), Create(x2), run_time=0.35)

        loop = CurvedArrow([-0.5, 0.2, 0], [-0.5, -0.9, 0], color=SOFT,
                           stroke_width=4)
        rl = _label("retry ×3", size=28, color=SOFT).move_to([-2.2, -0.6, 0])
        self.play(Create(loop), FadeIn(rl), run_time=0.5)

        cache = RoundedRectangle(corner_radius=0.2, width=2.6, height=1.4,
                                 color=INK, stroke_width=2.5,
                                 fill_color=CARD, fill_opacity=1
                                 ).move_to([3.8, -0.4, 0])
        cal = _label("cached data", size=28).move_to([3.8, -0.4, 0])
        at(self, 0.6)
        self.play(FadeIn(cache), FadeIn(cal), run_time=0.5)
        flag = _label("flagged", size=28, color=ACC).move_to([3.8, -1.5, 0])
        self.play(FadeIn(flag), run_time=0.3)

        bad = Square(side_length=0.4, color=SOFT, stroke_width=2.5,
                     fill_color=CARD, fill_opacity=1).move_to([-3.8, -1.8, 0])
        qbox = Rectangle(width=2.2, height=1.0, color=ACC, stroke_width=3,
                         fill_color=CARD, fill_opacity=1).move_to([0.5, -1.8, 0])
        ql = _label("quarantine", size=26, color=ACC).move_to([0.5, -1.8, 0])
        at(self, 0.8)
        self.play(FadeIn(bad), FadeIn(qbox), FadeIn(ql), run_time=0.4)
        self.play(bad.animate.move_to([0.5, -1.8, 0]), run_time=0.5)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M16 — B16: the evaluation checklist ticks
# ─────────────────────────────────────────────────────────────────────────────
class M16_Evaluation(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("Evaluating Muse")
        self.play(Write(title), run_time=0.6)

        items = ["wrote the scripts", "pulled the boards",
                 "tuned from evidence", "pushed to the repo"]
        at(self, 0.25)
        for i, name in enumerate(items):
            y = 1.4 - i * 0.9
            box = Square(side_length=0.45, color=INK, stroke_width=2.5,
                         fill_color=CARD, fill_opacity=1).move_to([-4.6, y, 0])
            lbl = _label(name, size=32).move_to([-2.2, y, 0])
            self.play(FadeIn(box), FadeIn(lbl), run_time=0.35)
            tick = VGroup(
                Line([-4.72, y, 0], [-4.62, y - 0.12, 0],
                     color=ACC, stroke_width=6),
                Line([-4.62, y - 0.12, 0], [-4.44, y + 0.12, 0],
                     color=ACC, stroke_width=6))
            self.play(FadeIn(tick), run_time=0.3)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M17 — B17: 25 files fall, the wrench turns, 25 rise
# ─────────────────────────────────────────────────────────────────────────────
class M17_PushBug(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("What failed: the push bug")
        self.play(Write(title), run_time=0.6)

        cloud = RoundedRectangle(corner_radius=0.4, width=3.0, height=1.6,
                                 color=INK, stroke_width=2.5,
                                 fill_color=CARD, fill_opacity=1
                                 ).move_to([0, 1.8, 0])
        cl = _label("GitHub", size=30, color=SOFT).move_to([0, 1.8, 0])
        self.play(FadeIn(cloud), FadeIn(cl), run_time=0.5)

        files = VGroup(*[Square(side_length=0.3, color=SOFT, stroke_width=2,
                                fill_color=CARD, fill_opacity=1
                                ).move_to([-4.4 + (i % 13) * 0.72,
                                           -0.6 - (i // 13) * 0.6, 0])
                         for i in range(25)])
        self.play(FadeIn(files), run_time=0.5)

        at(self, 0.35)
        self.play(*[f.animate.move_to([(-4.4 + (i % 13) * 0.72) * 0.3, 1.2, 0])
                     for i, f in enumerate(files)],
                  run_time=0.7, rate_func=rate_functions.rush_into)
        self.play(*[f.animate.move_to([-4.4 + (i % 13) * 0.72,
                                       -0.6 - (i // 13) * 0.6, 0])
                     for i, f in enumerate(files)],
                  run_time=0.7)

        wrench = _label("fix", size=40, weight="BOLD", color=ACC
                        ).move_to([0, -2.2, 0])
        at(self, 0.65)
        self.play(FadeIn(wrench), run_time=0.3)
        self.play(*[f.animate.move_to([(-4.4 + (i % 13) * 0.72) * 0.1, 1.8, 0])
                     .set_stroke(ACC)
                     for i, f in enumerate(files)],
                  run_time=0.8, rate_func=rate_functions.smooth)
        ok = _label("25 / 25 landed", size=32, color=ACC, weight="BOLD"
                    ).move_to([0, -2.2, 0])
        self.play(FadeOut(wrench), FadeIn(ok), run_time=0.4)
        finish(self)
