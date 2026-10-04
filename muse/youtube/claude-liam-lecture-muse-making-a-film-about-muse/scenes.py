"""scenes.py — Manim scenes for claude-liam-lecture-muse-making-a-film-about-muse.

"Muse making a film about Muse" — lecture skill, claude-liam (Liam, in for Bear).
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
    """M01_OwnAgent -> B01 (class names carry the M prefix; beats carry B)."""
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
#  M01 — B01: everyone gets their own agent on its own dedicated computer
# ─────────────────────────────────────────────────────────────────────────────
class M01_OwnAgent(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("One agent, one computer")
        self.play(Write(title), run_time=0.7)

        you_c = Circle(radius=0.35, color=INK, stroke_width=3).move_to([-3.5, 0.2, 0])
        you_l = _label("you", size=30, color=SOFT).move_to([-3.5, -0.55, 0])
        comp = Rectangle(width=1.5, height=1.05, color=INK, stroke_width=2.5,
                         fill_color=CARD, fill_opacity=1).move_to([3.5, 0.2, 0])
        comp_l = _label("your computer", size=30, color=SOFT).move_to([3.5, -0.75, 0])
        self.play(FadeIn(you_c), FadeIn(you_l), FadeIn(comp), FadeIn(comp_l),
                  run_time=0.8)

        link = Line([-3.0, 0.2, 0], [2.6, 0.2, 0], color=ACC, stroke_width=6)
        self.play(Create(link), run_time=0.8)
        at(self, 0.65)
        self.play(link.animate.set_stroke(width=10), run_time=0.35)
        self.play(link.animate.set_stroke(width=6), run_time=0.35)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M02 — B02: strictly personal — no group or shared chats
# ─────────────────────────────────────────────────────────────────────────────
class M02_StrictlyPersonal(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("Strictly personal")
        self.play(Write(title), run_time=0.7)

        a = Dot([-2.5, 0.3, 0], radius=0.28, color=INK)
        la = _label("you", size=30).move_to([-2.5, -0.55, 0])
        b = Dot([2.5, 0.3, 0], radius=0.28, color=INK)
        lb = _label("your agent", size=30).move_to([2.5, -0.55, 0])
        link = Line([-2.1, 0.3, 0], [2.1, 0.3, 0], color=INK, stroke_width=4)
        self.play(FadeIn(a), FadeIn(b), FadeIn(la), FadeIn(lb), Create(link),
                  run_time=0.9)

        at(self, 0.35)
        c = Dot([0, 2.0, 0], radius=0.28, color=SOFT)
        lc = _label("anyone else", size=30, color=SOFT).move_to([1.3, 2.0, 0])
        clink = Line([-0.12, 1.72, 0], [-1.7, 0.5, 0], color=SOFT, stroke_width=3)
        self.play(FadeIn(c), FadeIn(lc), Create(clink), run_time=0.7)

        x1 = Line([-1.05, 1.35, 0], [-0.45, 0.85, 0], color=ACC, stroke_width=8)
        x2 = Line([-1.05, 0.85, 0], [-0.45, 1.35, 0], color=ACC, stroke_width=8)
        self.play(Create(x1), Create(x2), run_time=0.4)
        at(self, 0.8)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M03 — B03: powered by Muse Spark, Meta's Muse model family
# ─────────────────────────────────────────────────────────────────────────────
class M03_MuseSpark(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("Muse Spark")
        self.play(Write(title), run_time=0.6)

        levels = [("Meta", 1.8, INK), ("Muse model family", 0.6, INK),
                  ("Muse Spark", -0.6, ACC), ("Muse", -1.8, INK)]
        prev_y = None
        for name, y, col in levels:
            d = Dot([-2.8, y, 0], radius=0.22, color=col)
            l = _label(name, size=30, color=INK if col == ACC else col).move_to([0.4, y, 0])
            self.play(FadeIn(d), FadeIn(l), run_time=0.35)
            if prev_y is not None:
                ln = Line([-2.8, prev_y, 0], [-2.8, y, 0],
                          color=GHOST, stroke_width=3)
                self.play(Create(ln), run_time=0.2)
            prev_y = y
        at(self, 0.7)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M04 — B04: launched September 8, 2026; US and Canada
# ─────────────────────────────────────────────────────────────────────────────
class M04_LaunchDate(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("September 8, 2026")
        self.play(Write(title), run_time=0.6)

        line = Line([-5.5, -0.5, 0], [5.5, -0.5, 0], color=INK, stroke_width=3)
        self.play(Create(line), run_time=0.5)
        tick = Line([0, -0.95, 0], [0, -0.05, 0], color=ACC, stroke_width=7)
        self.play(Create(tick), run_time=0.35)
        date = _label("September 8, 2026", size=36, weight="BOLD").move_to([0, 0.75, 0])
        self.play(FadeIn(date), run_time=0.4)
        at(self, 0.55)
        us = _label("US", size=32, color=SOFT).move_to([-1.4, -1.75, 0])
        ca = _label("Canada", size=32, color=SOFT).move_to([1.4, -1.75, 0])
        self.play(FadeIn(us), FadeIn(ca), run_time=0.5)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M05 — B05: chat is the front door on every surface
# ─────────────────────────────────────────────────────────────────────────────
class M05_ChatFrontDoor(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("Chat is the front door")
        self.play(Write(title), run_time=0.7)

        agent = Dot([0, -0.2, 0], radius=0.38, color=INK)
        albl = _label("Muse", size=30).move_to([0, -1.0, 0])
        spots = [([-4.6, 1.6, 0], "web"), ([4.6, 1.6, 0], "phone"),
                 ([-4.6, -2.2, 0], "Mac"), ([4.6, -2.2, 0], "WhatsApp")]
        marks = []
        for (x, y, _), name in spots:
            m = Circle(radius=0.3, color=SOFT, stroke_width=2.5).move_to([x, y, 0])
            l = _label(name, size=28, color=SOFT).move_to([x, y - 0.62, 0])
            marks.append((m, l))
        self.play(FadeIn(agent), FadeIn(albl),
                  *[FadeIn(m) for pair in marks for m in pair], run_time=0.8)

        bubbles = []
        for (x, y, _), _ in spots:
            b = Circle(radius=0.17, color=ACC, stroke_width=0,
                       fill_color=ACC, fill_opacity=1).move_to([x, y, 0])
            bubbles.append(b)
        self.play(*[FadeIn(b) for b in bubbles], run_time=0.3)
        at(self, 0.45)
        self.play(*[b.animate.move_to([0, -0.2, 0]) for b in bubbles],
                  run_time=0.9, rate_func=rate_functions.smooth)
        self.play(*[FadeOut(b) for b in bubbles],
                  agent.animate.scale(1.25), run_time=0.4)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M06 — B06: it remembers across chats
# ─────────────────────────────────────────────────────────────────────────────
class M06_ItRemembers(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("It remembers")
        self.play(Write(title), run_time=0.7)

        chat1 = Rectangle(width=2.6, height=1.7, color=INK, stroke_width=2,
                          fill_color=CARD, fill_opacity=1).move_to([-3.9, 0.6, 0])
        l1 = _label("chat one", size=28, color=SOFT).move_to([-3.9, 1.85, 0])
        store = Rectangle(width=1.9, height=1.3, color=INK, stroke_width=2,
                          fill_color=CARD, fill_opacity=1).move_to([0, -1.3, 0])
        ls = _label("memory", size=28, color=SOFT).move_to([0, -2.25, 0])
        chat2 = Rectangle(width=2.6, height=1.7, color=INK, stroke_width=2,
                          fill_color=CARD, fill_opacity=1).move_to([3.9, 0.6, 0])
        l2 = _label("chat two", size=28, color=SOFT).move_to([3.9, 1.85, 0])
        self.play(*[FadeIn(m) for m in (chat1, l1, store, ls, chat2, l2)],
                  run_time=0.9)

        chip = Square(side_length=0.42, color=ACC, stroke_width=0,
                      fill_color=ACC, fill_opacity=1).move_to([-3.9, 0.6, 0])
        self.play(FadeIn(chip), run_time=0.3)
        at(self, 0.4)
        self.play(chip.animate.move_to([0, -1.3, 0]),
                  run_time=0.8, rate_func=rate_functions.smooth)
        self.play(chip.animate.move_to([3.9, 0.6, 0]),
                  run_time=0.8, rate_func=rate_functions.smooth)
        at(self, 0.85)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M07 — B07: it uses tools — mail, calendar, shopping, media, devices
# ─────────────────────────────────────────────────────────────────────────────
class M07_UsesTools(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("It uses tools")
        self.play(Write(title), run_time=0.7)

        hub = Dot([0, 0.2, 0], radius=0.34, color=INK)
        hlbl = _label("Muse", size=30).move_to([0, 0.8, 0])
        self.play(FadeIn(hub), FadeIn(hlbl), run_time=0.5)

        tools = [("mail", -4.4, 1.9), ("calendar", 4.4, 1.9),
                 ("shopping", -4.4, -1.9), ("media", 4.4, -1.9),
                 ("devices", 0, -2.5)]
        nodes, links = [], []
        for name, x, y in tools:
            n = Square(side_length=0.55, color=INK, stroke_width=2.5,
                       fill_color=CARD, fill_opacity=1).move_to([x, y, 0])
            l = _label(name, size=26, color=SOFT).move_to([x, y - 0.62, 0])
            ln = Line([0, 0.2, 0], [x, y, 0], color=GHOST, stroke_width=3)
            nodes.append((n, l))
            links.append(ln)
        self.play(*[FadeIn(n) for pair in nodes for n in pair],
                  *[Create(ln) for ln in links], run_time=0.9)

        at(self, 0.5)
        for ln in links:
            self.play(ln.animate.set_color(ACC).set_stroke(width=5),
                      run_time=0.28)
        at(self, 0.85)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M08 — B08: it builds artifacts — documents, pages, apps
# ─────────────────────────────────────────────────────────────────────────────
class M08_BuildsThings(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("It builds things")
        self.play(Write(title), run_time=0.7)

        stations = [(-4.2, "document"), (0, "page"), (4.2, "app")]
        for x, name in stations:
            parts = VGroup(*[
                Rectangle(width=0.9, height=0.65, color=SOFT, stroke_width=2,
                          fill_color=CARD, fill_opacity=1
                          ).move_to([x + dx, 1.6, 0])
                for dx in (-0.7, 0.7)])
            lbl = _label(name, size=28, color=SOFT).move_to([x, -1.5, 0])
            whole = Rectangle(width=1.7, height=1.3, color=INK, stroke_width=2.5,
                              fill_color=CARD, fill_opacity=1).move_to([x, 0.1, 0])
            self.play(FadeIn(parts), FadeIn(lbl), run_time=0.4)
            self.play(FadeOut(parts), FadeIn(whole), run_time=0.45)
            if name == "app":
                dot = Dot([x, 0.1, 0], radius=0.18, color=ACC)
                self.play(FadeIn(dot), run_time=0.25)
        at(self, 0.8)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M09 — B09: it keeps your stuff — files and Library
# ─────────────────────────────────────────────────────────────────────────────
class M09_KeepsYourStuff(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("Your Library")
        self.play(Write(title), run_time=0.7)

        shelf = Rectangle(width=3.4, height=2.5, color=INK, stroke_width=2.5,
                          fill_color=CARD, fill_opacity=1).move_to([1.6, -0.2, 0])
        slbl = _label("Library", size=30).move_to([1.6, 1.45, 0])
        flbl = _label("files", size=28, color=SOFT).move_to([-4.6, 1.9, 0])
        self.play(FadeIn(shelf), FadeIn(slbl), FadeIn(flbl), run_time=0.7)

        slots = [[-0.4 + c * 1.0, 0.55 - r * 0.8, 0]
                 for r in range(3) for c in range(3)]
        files = []
        for i, (sx, sy, _) in enumerate(slots[:6]):
            f = Rectangle(width=0.72, height=0.55, color=INK, stroke_width=1.5,
                          fill_color=CARD, fill_opacity=1).move_to([-5.2, 1.2 - i * 0.35, 0])
            files.append((f, [sx + 1.6, sy - 0.2, 0]))
        self.play(*[FadeIn(f) for f, _ in files], run_time=0.4)
        at(self, 0.45)
        self.play(*[f.animate.move_to(dest) for f, dest in files],
                  run_time=1.0, rate_func=rate_functions.smooth)
        at(self, 0.85)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M10 — B10: it works while you're away
# ─────────────────────────────────────────────────────────────────────────────
class M10_WorksWhileAway(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("While you're away")
        self.play(Write(title), run_time=0.7)

        you_c = Circle(radius=0.32, color=SOFT, stroke_width=2.5).move_to([-5.3, 2.0, 0])
        you_l = _label("you", size=26, color=SOFT).move_to([-5.3, 1.35, 0])
        clock = Circle(radius=1.15, color=INK, stroke_width=3).move_to([-3.6, -0.3, 0])
        hand = Line([-3.6, -0.3, 0], [-3.6, 0.65, 0], color=ACC, stroke_width=5)
        self.play(FadeIn(you_c), FadeIn(you_l), FadeIn(clock), FadeIn(hand),
                  run_time=0.7)
        self.play(FadeOut(you_c), FadeOut(you_l), run_time=0.4)

        tasks = []
        for i, name in enumerate(["scheduled check", "Feed post", "goal done"]):
            card = Rectangle(width=2.5, height=0.85, color=INK, stroke_width=2,
                             fill_color=CARD, fill_opacity=1
                             ).move_to([0.6 + i * 0.0, 1.3 - i * 1.25, 0])
            lbl = _label(name, size=26).move_to(card.get_center())
            tasks.append((card, lbl))
        self.play(*[FadeIn(c) for pair in tasks for c in pair], run_time=0.6)
        at(self, 0.5)
        self.play(hand.animate.rotate(-TAU * 0.75, about_point=[-3.6, -0.3, 0]),
                  *[lbl.animate.set_color(SOFT) for _, lbl in tasks],
                  run_time=1.2, rate_func=rate_functions.linear)
        at(self, 0.85)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M11 — B11: on the web, at muse.ai
# ─────────────────────────────────────────────────────────────────────────────
class M11_WebApp(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("muse.ai")
        self.play(Write(title), run_time=0.6)

        win = Rectangle(width=7.0, height=4.0, color=INK, stroke_width=2.5,
                        fill_color=CARD, fill_opacity=1).move_to([0, -0.4, 0])
        bar = Line([-3.5, 1.1, 0], [3.5, 1.1, 0], color=INK, stroke_width=2)
        url = _label("muse.ai", size=28, color=SOFT).move_to([0, 1.3, 0])
        self.play(FadeIn(win), Create(bar), FadeIn(url), run_time=0.8)

        at(self, 0.35)
        lines = []
        for i, w in enumerate([4.6, 3.4, 5.2, 2.6]):
            ln = Line([-3.0, 0.35 - i * 0.62, 0], [-3.0 + w, 0.35 - i * 0.62, 0],
                      color=INK, stroke_width=5)
            lines.append(ln)
        for ln in lines:
            self.play(Create(ln), run_time=0.35)
        at(self, 0.85)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M12 — B12: iPhone and Android apps
# ─────────────────────────────────────────────────────────────────────────────
class M12_MobileApps(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("iPhone and Android")
        self.play(Write(title), run_time=0.7)

        phones, line_sets = [], []
        for x, name in [(-2.4, "iPhone"), (2.4, "Android")]:
            p = Rectangle(width=1.7, height=3.1, color=INK, stroke_width=2.5,
                          fill_color=CARD, fill_opacity=1).move_to([x, -0.1, 0])
            l = _label(name, size=28, color=SOFT).move_to([x, -2.05, 0])
            lines = [Line([x - 0.6, 0.9 - i * 0.55, 0], [x - 0.6 + w, 0.9 - i * 0.55, 0],
                          color=INK, stroke_width=4)
                     for i, w in enumerate([0.9, 1.2, 0.7])]
            phones.append((p, l))
            line_sets.append(lines)
        self.play(*[FadeIn(m) for pair in phones for m in pair], run_time=0.7)
        at(self, 0.4)
        for i in range(3):
            self.play(*[Create(ls[i]) for ls in line_sets], run_time=0.35)
        at(self, 0.85)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M13 — B13: Mac app pairs your Mac
# ─────────────────────────────────────────────────────────────────────────────
class M13_MacApp(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("Your Mac, paired")
        self.play(Write(title), run_time=0.7)

        desk = Rectangle(width=2.3, height=1.5, color=INK, stroke_width=2.5,
                         fill_color=CARD, fill_opacity=1).move_to([-3.2, 0.2, 0])
        dlbl = _label("your Mac", size=30, color=SOFT).move_to([-3.2, -0.95, 0])
        agent = Dot([3.2, 0.2, 0], radius=0.34, color=INK)
        albl = _label("Muse", size=30).move_to([3.2, -0.6, 0])
        self.play(FadeIn(desk), FadeIn(dlbl), FadeIn(agent), FadeIn(albl),
                  run_time=0.8)

        pair = Line([-1.9, 0.2, 0], [2.7, 0.2, 0], color=ACC, stroke_width=5)
        self.play(Create(pair), run_time=0.7)
        at(self, 0.6)
        self.play(pair.animate.set_stroke(width=9), run_time=0.3)
        self.play(pair.animate.set_stroke(width=5), run_time=0.3)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M14 — B14: WhatsApp as a messaging channel
# ─────────────────────────────────────────────────────────────────────────────
class M14_WhatsApp(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("WhatsApp")
        self.play(Write(title), run_time=0.6)

        phone = Rectangle(width=1.7, height=3.0, color=INK, stroke_width=2.5,
                          fill_color=CARD, fill_opacity=1).move_to([-3.4, 0, 0])
        plbl = _label("WhatsApp", size=28, color=SOFT).move_to([-3.4, -2.0, 0])
        agent = Dot([3.4, 0, 0], radius=0.34, color=INK)
        albl = _label("Muse", size=30).move_to([3.4, -0.75, 0])
        self.play(FadeIn(phone), FadeIn(plbl), FadeIn(agent), FadeIn(albl),
                  run_time=0.8)

        b1 = Circle(radius=0.2, color=ACC, stroke_width=0,
                    fill_color=ACC, fill_opacity=1).move_to([-3.4, 0.6, 0])
        b2 = Circle(radius=0.2, color=INK, stroke_width=0,
                    fill_color=INK, fill_opacity=1).move_to([3.4, -0.1, 0])
        self.play(FadeIn(b1), FadeIn(b2), run_time=0.3)
        at(self, 0.45)
        self.play(b1.animate.move_to([2.6, 0.6, 0]),
                  b2.animate.move_to([-2.6, -0.1, 0]),
                  run_time=0.9, rate_func=rate_functions.smooth)
        at(self, 0.85)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M15 — B15: free access with a usage limit
# ─────────────────────────────────────────────────────────────────────────────
class M15_FreeTier(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("Free")
        self.play(Write(title), run_time=0.6)

        track = Rectangle(width=8.0, height=0.7, color=GHOST, stroke_width=2.5,
                          fill_color=CARD, fill_opacity=1).move_to([0, -0.5, 0])
        fill = Rectangle(width=0.1, height=0.5, color=INK, stroke_width=0,
                         fill_color=INK, fill_opacity=1
                         ).move_to([-3.9, -0.5, 0])
        limit = Line([1.0, -1.0, 0], [1.0, 0.0, 0], color=INK, stroke_width=5)
        llim = _label("usage limit", size=30, color=SOFT).move_to([1.0, 0.55, 0])
        lfree = _label("free", size=30, color=SOFT).move_to([-3.9, 0.55, 0])
        self.play(FadeIn(track), FadeIn(limit), FadeIn(llim), FadeIn(lfree),
                  FadeIn(fill), run_time=0.7)

        at(self, 0.35)
        fill_big = Rectangle(width=4.5, height=0.5, color=INK, stroke_width=0,
                             fill_color=INK, fill_opacity=1).move_to([-1.5, -0.5, 0])
        self.play(Transform(fill, fill_big),
                  run_time=1.0, rate_func=rate_functions.smooth)
        at(self, 0.8)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M16 — B16: paid subscription lifts the cap
# ─────────────────────────────────────────────────────────────────────────────
class M16_Subscription(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("Subscription")
        self.play(Write(title), run_time=0.6)

        track = Rectangle(width=8.0, height=0.7, color=GHOST, stroke_width=2.5,
                          fill_color=CARD, fill_opacity=1).move_to([0, -0.5, 0])
        fill = Rectangle(width=4.5, height=0.5, color=INK, stroke_width=0,
                         fill_color=INK, fill_opacity=1).move_to([-1.5, -0.5, 0])
        limit = Line([1.0, -1.0, 0], [1.0, 0.0, 0], color=INK, stroke_width=5)
        llim = _label("old limit", size=30, color=SOFT).move_to([1.0, 0.55, 0])
        self.play(FadeIn(track), FadeIn(fill), FadeIn(limit), FadeIn(llim),
                  run_time=0.7)

        at(self, 0.4)
        limit2 = Line([3.2, -1.0, 0], [3.2, 0.0, 0], color=INK, stroke_width=5)
        llim2 = _label("new limit", size=30, color=SOFT).move_to([3.2, 0.55, 0])
        fill2 = Rectangle(width=6.5, height=0.5, color=INK, stroke_width=0,
                          fill_color=INK, fill_opacity=1).move_to([-0.4, -0.5, 0])
        self.play(Transform(limit, limit2), Transform(llim, llim2), run_time=0.6)
        self.play(Transform(fill, fill2),
                  run_time=0.8, rate_func=rate_functions.smooth)
        at(self, 0.85)
        finish(self)


# ─────────────────────────────────────────────────────────────────────────────
#  M17 — B17: subscribe at muse.ai, App Store, Google Play; renews monthly
# ─────────────────────────────────────────────────────────────────────────────
class M17_WhereToSubscribe(Scene):

    def construct(self):
        self.camera.background_color = BG
        title = _title("Subscribe")
        self.play(Write(title), run_time=0.6)

        spots = [(-4.2, "muse.ai"), (0, "App Store"), (4.2, "Google Play")]
        marks = []
        for x, name in spots:
            r = Rectangle(width=2.2, height=1.1, color=INK, stroke_width=2.5,
                          fill_color=CARD, fill_opacity=1).move_to([x, -0.9, 0])
            l = _label(name, size=28).move_to([x, -1.65, 0])
            marks.append((r, l))
        self.play(*[FadeIn(m) for pair in marks for m in pair], run_time=0.8)

        arc = Arc(radius=1.1, start_angle=PI / 2, angle=-TAU * 0.85,
                  color=ACC, stroke_width=6).move_to([0, 0.8, 0])
        arrow = Triangle(color=ACC, fill_opacity=1, stroke_width=0
                         ).scale(0.14).move_to([0, 0.8, 0])
        albl = _label("monthly", size=28, color=SOFT).move_to([0, 2.35, 0])
        self.play(FadeIn(albl), Create(arc), FadeIn(arrow), run_time=0.7)
        at(self, 0.55)
        self.play(Rotate(VGroup(arc, arrow), -TAU * 0.5, about_point=[0, 0.8, 0]),
                  run_time=1.0, rate_func=rate_functions.linear)
        at(self, 0.9)
        finish(self)
