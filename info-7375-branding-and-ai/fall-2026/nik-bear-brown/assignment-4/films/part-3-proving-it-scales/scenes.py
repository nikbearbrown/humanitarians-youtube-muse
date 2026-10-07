"""scenes.py — Muse proves it scales (Film 3).

12 Manim scenes, M01–M12. House conventions: 16:9, safe-area coords
(±6.3 x, ±3.4 y), distinct non-text shapes per beat, every on-screen text
is read aloud in its beat.
"""
from manim import *

config.pixel_width = 1920
config.pixel_height = 1080
config.background_color = "#F2F0E9"

INK = "#3D3929"
PAPER = "#F7F3EA"
ACCENT = "#D97757"
GREY = "#8A8578"
CARD = "#FFFFFF"

def T(s, **kw):
    fs = kw.pop("font_size", 30)
    kw.setdefault("font", "EB Garamond")
    return Text(s, font_size=fs * 3, **kw).scale(1 / 3)


def title_card(title, sub=None):
    g = VGroup()
    t = T(title, font_size=40, color=INK).move_to(ORIGIN)
    g.add(t)
    if sub:
        s = T(sub, font_size=24, color=INK).next_to(t, DOWN, buff=0.3)
        g.add(s)
    return g


def check_mark(pos, scale=1.0, color=ACCENT):
    return VGroup(
        Line(ORIGIN, RIGHT * 0.5 + DOWN * 0.3, color=color, stroke_width=10),
        Line(RIGHT * 0.5 + DOWN * 0.3, RIGHT * 1.3 + UP * 0.4,
             color=color, stroke_width=10),
    ).scale(scale).move_to(pos)


class M01_Bidea(Scene):
    def construct(self):
        wall = Rectangle(width=10, height=5, fill_color="#EDE8DA",
                         fill_opacity=1, stroke_color=INK).move_to(ORIGIN)
        crack = VGroup(
            Line(UP * 2.2, UP * 0.8 + RIGHT * 0.3, color=INK, stroke_width=6),
            Line(UP * 0.8 + RIGHT * 0.3, DOWN * 0.6 + LEFT * 0.2, color=INK,
                 stroke_width=6),
            Line(DOWN * 0.6 + LEFT * 0.2, DOWN * 2.2 + RIGHT * 0.4, color=INK,
                 stroke_width=6),
        )
        q = T("will it break?", font_size=40, color=ACCENT).to_edge(
            UP, buff=0.7)
        self.play(FadeIn(wall))
        self.play(Create(crack), run_time=1.0)
        self.play(Write(q))
        self.wait(1.2)


class M02_Bdefs(Scene):
    def construct(self):
        words = ["scale", "breaking point", "measured", "estimated"]
        defs = ["how work grows with load", "the load where it stops working",
                "numbers from a real run", "honest arithmetic, labeled"]
        cards = VGroup()
        for i, (w, d) in enumerate(zip(words, defs)):
            x = -5.4 + i * 3.6
            box = RoundedRectangle(corner_radius=0.2, width=3.2, height=2.4,
                                   fill_color=CARD, fill_opacity=1,
                                   stroke_color=INK).move_to([x, 0, 0])
            t = T(w, font_size=28, color=ACCENT).move_to([x, 0.55, 0])
            s = T(d, font_size=16, color=INK).move_to([x, -0.35, 0])
            cards.add(VGroup(box, t, s))
        for c in cards:
            self.play(FadeIn(c, shift=UP * 0.3), run_time=0.7)
        self.wait(1.2)


class M03_B01Lanes(Scene):
    def construct(self):
        lanes = VGroup()
        for i, (lab, n) in enumerate([("1x", "640"), ("10x", "6,400"),
                                      ("50x", "32,000")]):
            y = 1.8 - i * 1.8
            lane = RoundedRectangle(corner_radius=0.2, width=9.6, height=1.3,
                                    fill_color=CARD, fill_opacity=1,
                                    stroke_color=INK).move_to([0, y, 0])
            t = T(f"{lab}  —  {n} records", font_size=28,
                     color=INK).move_to([0, y, 0])
            lanes.add(VGroup(lane, t))
        cap = T("three lanes, one pipeline", font_size=32,
                   color=INK).to_edge(UP, buff=0.7)
        self.play(Write(cap))
        for ln in lanes:
            self.play(FadeIn(ln, shift=RIGHT * 0.4), run_time=0.6)
        self.wait(1.2)


class M04_B02Method(Scene):
    def construct(self):
        src = RoundedRectangle(corner_radius=0.15, width=2.6, height=1.6,
                               fill_color=CARD, fill_opacity=1,
                               stroke_color=ACCENT).move_to([-4.5, 0, 0])
        st = T("real record", font_size=20, color=INK).move_to(src.get_center())
        grid = VGroup()
        for r in range(3):
            for c in range(4):
                cell = RoundedRectangle(corner_radius=0.1, width=1.7,
                                        height=1.0, fill_color="#EDE8DA",
                                        fill_opacity=1,
                                        stroke_color=GREY).move_to(
                    [-0.5 + c * 1.9, 1.1 - r * 1.15, 0])
                grid.add(cell)
        cap = T("same shape, unique ids", font_size=28,
                   color=INK).to_edge(UP, buff=0.7)
        caveat = T("the load is synthetic — stated up front", font_size=22,
                      color=GREY).to_edge(DOWN, buff=0.8)
        self.play(Write(cap))
        self.play(FadeIn(src), FadeIn(st))
        self.play(*[FadeIn(cell, scale=0.8) for cell in grid], run_time=1.2)
        self.play(FadeIn(caveat))
        self.wait(1.2)


class M05_B03Table(Scene):
    def construct(self):
        head = T("measured, not modeled", font_size=30,
                    color=INK).to_edge(UP, buff=0.7)
        rows = [("640 records", "2.37 s"), ("6,400 records", "23.8 s"),
                ("32,000 records", "119.1 s"), ("per record", "3.72 ms"),
                ("peak memory", "52–65 MB")]
        table = VGroup()
        for i, (a, b) in enumerate(rows):
            y = 1.6 - i * 0.85
            bg = Rectangle(width=9.6, height=0.7,
                           fill_color=CARD if i % 2 == 0 else "#EDE8DA",
                           fill_opacity=1, stroke_width=0).move_to([0, y, 0])
            ta = T(a, font_size=24, color=INK).move_to([-2.8, y, 0])
            tb = T(b, font_size=24, color=ACCENT).move_to([2.8, y, 0])
            table.add(VGroup(bg, ta, tb))
        self.play(Write(head))
        for row in table:
            self.play(FadeIn(row[0]), FadeIn(row[1], shift=RIGHT * 0.15),
                      FadeIn(row[2], shift=RIGHT * 0.15), run_time=0.45)
        self.wait(1.2)


class M06_B04Linear(Scene):
    def construct(self):
        axes = Axes(x_range=[0, 35000, 10000], y_range=[0, 130, 30],
                    x_length=9, y_length=4.5,
                    axis_config={"color": INK}).shift(DOWN * 0.3)
        pts = [(640, 2.37), (6400, 23.8), (32000, 119.1)]
        dots = VGroup(*[Dot(axes.c2p(x, y), color=ACCENT, radius=0.12)
                        for x, y in pts])
        line = Line(axes.c2p(0, 0), axes.c2p(33000, 123), color=ACCENT,
                    stroke_width=5)
        lab = T("linear — 3.72 ms / record", font_size=26,
                   color=ACCENT).to_edge(UP, buff=0.7)
        self.play(Create(axes), run_time=0.8)
        self.play(Write(lab))
        self.play(Create(line), run_time=1.0)
        self.play(*[FadeIn(d, scale=1.5) for d in dots], run_time=0.6)
        self.wait(1.2)


class M07_B05Fetch(Scene):
    def construct(self):
        pipe = RoundedRectangle(corner_radius=0.6, width=9.6, height=1.8,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=INK).move_to(UP * 0.4)
        flow = VGroup(*[Circle(radius=0.22, fill_color=ACCENT, fill_opacity=1,
                               stroke_width=0).move_to([-3.5 + i * 1.4, 0.4, 0])
                        for i in range(6)])
        stats = VGroup(
            T("640 jobs · 9.2 MB · 6.2 s", font_size=28, color=INK),
            T("HTTP 200 — no rate limit", font_size=24, color=ACCENT),
        ).arrange(DOWN, buff=0.2).move_to(DOWN * 1.8)
        cap = T("the fetch side, measured live", font_size=30,
                   color=INK).to_edge(UP, buff=0.7)
        self.play(Write(cap))
        self.play(FadeIn(pipe))
        self.play(*[FadeIn(f, shift=RIGHT * 0.5) for f in flow], run_time=1.0)
        for s in stats:
            self.play(FadeIn(s, shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)


class M08_B06NoBreak(Scene):
    def construct(self):
        lens = Circle(radius=1.6, stroke_color=INK, stroke_width=5,
                      fill_opacity=0).move_to(ORIGIN)
        handle = Line([1.1, -1.1, 0], [2.4, -2.4, 0], color=INK,
                      stroke_width=14)
        stamp = T("breaking point: NOT FOUND", font_size=36,
                     color=ACCENT).move_to(DOWN * 2.2)
        frame = Rectangle(width=7.2, height=3.6, stroke_color=ACCENT,
                          stroke_width=4).move_to(DOWN * 2.2)
        cap = T("fifty times the load — and it worked", font_size=30,
                   color=INK).to_edge(UP, buff=0.7)
        self.play(Write(cap))
        self.play(Create(lens), Create(handle))
        self.wait(0.6)
        self.play(FadeIn(frame), Write(stamp), run_time=0.8)
        self.wait(1.2)


class M09_B07Cost(Scene):
    def construct(self):
        tag = RoundedRectangle(corner_radius=0.2, width=6.4, height=3.4,
                               fill_color=CARD, fill_opacity=1,
                               stroke_color=INK).move_to(UP * 0.3)
        price = T("$0.00", font_size=64, color=ACCENT).move_to(
            tag.get_center() + UP * 0.4)
        per = T("per month", font_size=24, color=GREY).move_to(
            tag.get_center() + DOWN * 0.7)
        why = VGroup()
        for w in ["zero API calls", "zero LLM calls",
                  "estimated — from a measured zero"]:
            coin = Circle(radius=0.16, fill_color=ACCENT, fill_opacity=1,
                          stroke_width=0)
            t = T(w, font_size=22, color=INK)
            why.add(VGroup(coin, t).arrange(RIGHT, buff=0.25,
                                            aligned_edge=ORIGIN))
        why.arrange(DOWN, aligned_edge=LEFT, buff=0.25).move_to(DOWN * 2.0)
        self.play(FadeIn(tag))
        self.play(Write(price))
        self.play(FadeIn(per))
        for w in why:
            self.play(FadeIn(w[0]), FadeIn(w[1], shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)


class M10_B08Readiness(Scene):
    def construct(self):
        items = [("scoring", "ready at any realistic volume", ACCENT, True),
                 ("fetching", "wants retry + backoff per board", "#C98A1B", None),
                 ("delivery", "unimplemented — the blocker", ACCENT, False)]
        rows = VGroup()
        for i, (name, note, col, ok) in enumerate(items):
            y = 1.6 - i * 1.5
            bg = RoundedRectangle(corner_radius=0.15, width=10.4, height=1.2,
                                  fill_color=CARD, fill_opacity=1,
                                  stroke_color=INK).move_to([0, y, 0])
            mark = check_mark([-4.3, y, 0], scale=0.55, color=col) if ok is not False else \
                T("✗", font_size=36, color=col).move_to([-4.3, y, 0])
            if ok is None:
                mark = T("~", font_size=40, color=col).move_to([-4.3, y, 0])
            tn = T(name, font_size=28, color=INK).move_to([-2.9, y + 0.2, 0])
            td = T(note, font_size=20, color=GREY).move_to([-2.9, y - 0.35, 0])
            rows.add(VGroup(bg, mark, tn, td))
        cap = T("production readiness, judged", font_size=30,
                   color=INK).to_edge(UP, buff=0.7)
        self.play(Write(cap))
        for row in rows:
            self.play(FadeIn(row[0]))
            self.play(Create(row[1]) if isinstance(row[1], VGroup) else FadeIn(row[1]),
                      FadeIn(row[2], shift=RIGHT * 0.2),
                      FadeIn(row[3], shift=RIGHT * 0.2), run_time=0.6)
        self.wait(1.2)


class M11_B09Verdict(Scene):
    def construct(self):
        left = RoundedRectangle(corner_radius=0.2, width=4.6, height=2.6,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=ACCENT).move_to([-3.1, 0, 0])
        lt = T("scale: boring", font_size=26, color=ACCENT).move_to(
            left.get_center())
        right = RoundedRectangle(corner_radius=0.2, width=4.6, height=2.6,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=ACCENT, stroke_width=4).move_to(
            [3.1, 0, 0])
        rt = T("delivery:\nthe blocker", font_size=26, color=ACCENT).move_to(
            right.get_center())
        arrow = Arrow([-0.6, 0, 0], [0.6, 0, 0], color=INK, buff=0.1,
                      stroke_width=8)
        cap = T("the verdict", font_size=32, color=INK).to_edge(UP,
                                                                   buff=0.7)
        self.play(Write(cap))
        self.play(FadeIn(left), FadeIn(lt), run_time=0.6)
        self.play(GrowArrow(arrow), run_time=0.5)
        self.play(FadeIn(right, scale=0.9), FadeIn(rt), run_time=0.7)
        self.wait(1.5)


class M12_BvdtHtfOut(Scene):
    def construct(self):
        plate = RoundedRectangle(corner_radius=0.25, width=11.6, height=4.6,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK)
        recap = VGroup(*[
            T("1 · the test: 1x to 50x on real record shapes", font_size=26,
                 color=INK),
            T("2 · linear at 3.72 ms/record; fetch 6 s a board", font_size=26,
                 color=INK),
            T("3 · no breaking point; cost zero; gaps named", font_size=26,
                 color=INK),
            T("4 · verdict: scale is boring, delivery is the blocker",
                 font_size=26, color=INK),
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to(ORIGIN)
        self.play(FadeIn(plate))
        for r in recap:
            self.play(FadeIn(r, shift=RIGHT * 0.3), run_time=0.6)
        self.wait(0.8)
        self.play(FadeOut(recap), FadeOut(plate))
        doplate = RoundedRectangle(corner_radius=0.25, width=10.4, height=3.6,
                                   fill_color="#EDE8DA", fill_opacity=1,
                                   stroke_color=ACCENT)
        do = VGroup(
            T("Your turn", font_size=34, color=ACCENT),
            T("Run three lanes: 1x, 10x, 50x.", font_size=24, color=INK),
            T("Find your per-record cost.", font_size=24, color=INK),
            T("Is your blocker scale — or something else?", font_size=24,
                 color=INK),
        ).arrange(DOWN, buff=0.25).move_to(ORIGIN)
        self.play(FadeIn(doplate))
        for d in do:
            self.play(FadeIn(d, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)
        self.play(FadeOut(do), FadeOut(doplate))
        out = title_card("Muse, in for Bear", "@NikBearBrown")
        self.play(FadeIn(out))
        self.wait(1.5)
