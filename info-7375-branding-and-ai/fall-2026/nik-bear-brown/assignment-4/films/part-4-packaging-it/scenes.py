"""scenes.py — Muse packages it (Film 4).

11 Manim scenes, M01–M11. House conventions: 16:9, safe-area coords
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


class M01_Bidea(Scene):
    def construct(self):
        box = RoundedRectangle(corner_radius=0.2, width=6.4, height=4.2,
                               fill_color=CARD, fill_opacity=1,
                               stroke_color=INK).move_to(ORIGIN)
        ribbon_v = Rectangle(width=0.5, height=4.2, fill_color=ACCENT,
                             fill_opacity=1, stroke_width=0).move_to(ORIGIN)
        ribbon_h = Rectangle(width=6.4, height=0.5, fill_color=ACCENT,
                             fill_opacity=1, stroke_width=0).move_to(ORIGIN)
        bow = Circle(radius=0.45, fill_color=ACCENT, fill_opacity=1,
                     stroke_width=0).move_to(UP * 2.1)
        q = T("would you show this to a client?", font_size=34,
                 color=INK).to_edge(UP, buff=0.7)
        self.play(FadeIn(box))
        self.play(FadeIn(ribbon_v), FadeIn(ribbon_h))
        self.play(FadeIn(bow, scale=1.6))
        self.play(Write(q))
        self.wait(1.2)


class M02_Bdefs(Scene):
    def construct(self):
        words = ["package", "executive summary", "architecture", "demo"]
        defs = ["everything a stranger needs", "one page: problem to value",
                "how it fits — and fails", "the walkthrough that proves it"]
        cards = VGroup()
        for i, (w, d) in enumerate(zip(words, defs)):
            x = -5.4 + i * 3.6
            box = RoundedRectangle(corner_radius=0.2, width=3.2, height=2.4,
                                   fill_color=CARD, fill_opacity=1,
                                   stroke_color=INK).move_to([x, 0, 0])
            t = T(w, font_size=24, color=ACCENT).move_to([x, 0.55, 0])
            s = T(d, font_size=15, color=INK).move_to([x, -0.35, 0])
            cards.add(VGroup(box, t, s))
        for c in cards:
            self.play(FadeIn(c, shift=UP * 0.3), run_time=0.7)
        self.wait(1.2)


class M03_B01Summary(Scene):
    def construct(self):
        page = RoundedRectangle(corner_radius=0.2, width=9.6, height=5.8,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=INK)
        head = T("Executive summary — one page", font_size=30,
                    color=INK).to_edge(UP, buff=0.9)
        secs = VGroup()
        for i, s in enumerate(["problem: 3,446 postings is a pile",
                               "solution: 5 dimensions, 2 impls, 1 spec",
                               "results: 714 scored, 22 to pursue",
                               "value: a 22-item action list"]):
            sq = Square(side_length=0.18, fill_color=ACCENT, fill_opacity=1,
                        stroke_width=0)
            t = T(s, font_size=24, color=INK)
            secs.add(VGroup(sq, t).arrange(RIGHT, buff=0.25,
                                           aligned_edge=ORIGIN))
        secs.arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to(UP * 0.2)
        badge = T("Built with n8n + Python", font_size=22,
                     color=ACCENT).to_edge(DOWN, buff=0.9)
        self.play(FadeIn(page))
        self.play(Write(head))
        for sec in secs:
            self.play(FadeIn(sec[0]), FadeIn(sec[1], shift=RIGHT * 0.3),
                      run_time=0.5)
        self.play(FadeIn(badge))
        self.wait(1.2)


class M04_B02Arch(Scene):
    def construct(self):
        labels = ["sources", "fetch", "normalize", "SCORE", "route", "outputs"]
        boxes = VGroup()
        cols = [INK, INK, INK, ACCENT, INK, INK]
        for i, (lab, col) in enumerate(zip(labels, cols)):
            x = -5.5 + i * 2.2
            b = RoundedRectangle(corner_radius=0.15, width=2.0, height=1.6,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=col,
                                 stroke_width=4 if lab == "SCORE" else 2)
            b.move_to([x, 0.6, 0])
            t = T(lab, font_size=20, color=col).move_to([x, 0.6, 0])
            boxes.add(VGroup(b, t))
        arrows = VGroup(*[Arrow([-4.35 + i * 2.2, 0.6, 0],
                                [-3.65 + i * 2.2, 0.6, 0],
                                color=INK, buff=0.08, stroke_width=6)
                          for i in range(5)])
        dashed = DashedLine([-5.5, -1.6, 0], [5.5, -1.6, 0], color=GREY,
                            dash_length=0.25)
        dl = T("delivery — specified, not built", font_size=22,
                  color=GREY).next_to(dashed, DOWN, buff=0.2)
        cap = T("the architecture, honestly drawn", font_size=30,
                   color=INK).to_edge(UP, buff=0.7)
        self.play(Write(cap))
        for b in boxes:
            self.play(FadeIn(b, shift=RIGHT * 0.25), run_time=0.5)
        self.play(*[GrowArrow(a) for a in arrows], run_time=0.8)
        self.play(Create(dashed), FadeIn(dl))
        self.wait(1.2)


class M05_B03Failures(Scene):
    def construct(self):
        main = RoundedRectangle(corner_radius=0.2, width=9.6, height=1.6,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=INK).move_to(UP * 1.2)
        mt = T("score → route → outputs", font_size=26,
                  color=INK).move_to(main.get_center())
        fails = VGroup()
        for i, f in enumerate([("malformed → quarantine", "logged, never dropped"),
                               ("fetch fails → cached fallback", "flagged in report"),
                               ("scoring error → quarantine", "logged, never dropped")]):
            y = -0.4 - i * 1.15
            bg = RoundedRectangle(corner_radius=0.15, width=9.6, height=0.95,
                                  fill_color=CARD, fill_opacity=1,
                                  stroke_color=ACCENT, stroke_width=3).move_to([0, y, 0])
            dot = Circle(radius=0.14, fill_color=ACCENT, fill_opacity=1,
                         stroke_width=0).move_to([-4.2, y, 0])
            t1 = T(f[0], font_size=22, color=ACCENT).move_to([-1.2, y + 0.16, 0])
            t2 = T(f[1], font_size=18, color=GREY).move_to([-1.2, y - 0.24, 0])
            fails.add(VGroup(bg, dot, t1, t2))
        cap = T("how it fails — by design", font_size=30,
                   color=INK).to_edge(UP, buff=0.7)
        self.play(Write(cap))
        self.play(FadeIn(main), FadeIn(mt))
        for f in fails:
            self.play(FadeIn(f[0]))
            self.play(FadeIn(f[1]), FadeIn(f[2], shift=RIGHT * 0.2),
                      FadeIn(f[3], shift=RIGHT * 0.2), run_time=0.5)
        self.wait(1.2)


class M06_B04TwoImpls(Scene):
    def construct(self):
        py = RoundedRectangle(corner_radius=0.2, width=4.8, height=2.8,
                              fill_color=CARD, fill_opacity=1,
                              stroke_color=ACCENT, stroke_width=3).move_to([-2.9, 0.4, 0])
        n8n = RoundedRectangle(corner_radius=0.2, width=4.8, height=2.8,
                               fill_color=CARD, fill_opacity=1,
                               stroke_color=ACCENT, stroke_width=3).move_to([2.9, 0.4, 0])
        pt = VGroup(T("Python", font_size=28, color=ACCENT),
                    T("batch scoring + briefs", font_size=18, color=INK)
                    ).arrange(DOWN, buff=0.15).move_to(py.get_center())
        nt = VGroup(T("n8n", font_size=28, color=ACCENT),
                    T("scheduling + delivery", font_size=18, color=INK)
                    ).arrange(DOWN, buff=0.15).move_to(n8n.get_center())
        spec = T("one spec — identical scores", font_size=26,
                    color=INK).move_to(DOWN * 2.2)
        link = DoubleArrow([-0.4, 0.4, 0], [0.4, 0.4, 0], color=INK,
                           buff=0.1, stroke_width=6)
        cap = T("integration points", font_size=30, color=INK).to_edge(
            UP, buff=0.7)
        self.play(Write(cap))
        self.play(FadeIn(py), FadeIn(pt), run_time=0.6)
        self.play(FadeIn(n8n), FadeIn(nt), run_time=0.6)
        self.play(GrowArrow(link))
        self.play(Write(spec))
        self.wait(1.2)


class M07_B05Demo(Scene):
    def construct(self):
        steps = ["show the digest — 22 pursue roles",
                 "open a brief — score, reasons, link, next step",
                 "open the run report — every number traced",
                 "open the architecture — point at the dashed lane"]
        rows = VGroup()
        for i, s in enumerate(steps):
            y = 1.8 - i * 1.15
            num = Circle(radius=0.32, fill_color=ACCENT, fill_opacity=1,
                         stroke_width=0).move_to([-4.6, y, 0])
            nt = T(str(i + 1), font_size=26, color=CARD).move_to(num.get_center())
            t = T(s, font_size=24, color=INK).move_to([-0.6, y, 0])
            rows.add(VGroup(num, nt, t))
        cap = T("the demo walkthrough", font_size=30, color=INK).to_edge(
            UP, buff=0.7)
        trust = T("a demo that shows the gap is a demo you can trust",
                     font_size=22, color=GREY).to_edge(DOWN, buff=0.8)
        self.play(Write(cap))
        for r in rows:
            self.play(FadeIn(r[0]), FadeIn(r[1]))
            self.play(FadeIn(r[2], shift=RIGHT * 0.25), run_time=0.5)
        self.play(FadeIn(trust))
        self.wait(1.2)


class M08_B06Pitch(Scene):
    def construct(self):
        card = RoundedRectangle(corner_radius=0.25, width=10.6, height=4.4,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=INK).move_to(UP * 0.2)
        nums = VGroup(*[
            T("3.72 ms / record — linear to 32,000", font_size=26, color=INK),
            T("$0.00 / month — zero API, zero LLM calls", font_size=26,
                 color=INK),
            T("15 briefs a non-technical user can open", font_size=26,
                 color=INK),
            T("1 diagram a client can read", font_size=26, color=INK),
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.25).move_to(UP * 0.2)
        dots = VGroup(*[Circle(radius=0.1, fill_color=ACCENT, fill_opacity=1,
                               stroke_width=0).move_to([-4.6, 1.35 - i * 0.62, 0])
                        for i in range(4)])
        cap = T("the pitch, in numbers", font_size=30, color=INK).to_edge(
            UP, buff=0.7)
        self.play(Write(cap))
        self.play(FadeIn(card))
        for d, n in zip(dots, nums):
            self.play(FadeIn(d), FadeIn(n, shift=RIGHT * 0.2), run_time=0.5)
        self.wait(1.2)


class M09_B07Todo(Scene):
    def construct(self):
        card = RoundedRectangle(corner_radius=0.2, width=9.6, height=3.2,
                                fill_color="#EDE8DA", fill_opacity=1,
                                stroke_color=ACCENT, stroke_width=4).move_to(ORIGIN)
        t = T("scheduled delivery", font_size=32, color=INK).move_to(
            UP * 0.6)
        s = T("approval gate → weekly digest → email — specified, not built",
                 font_size=22, color=GREY).move_to(DOWN * 0.3)
        stamp = T("THE BLOCKER", font_size=30, color=ACCENT).move_to(
            DOWN * 1.1)
        frame = Rectangle(width=4.6, height=1.0, stroke_color=ACCENT,
                          stroke_width=3).move_to(DOWN * 1.1)
        cap = T("the gap, disclosed", font_size=30, color=INK).to_edge(
            UP, buff=0.7)
        self.play(Write(cap))
        self.play(FadeIn(card))
        self.play(FadeIn(t, shift=UP * 0.2))
        self.play(FadeIn(s, shift=UP * 0.2))
        self.play(FadeIn(frame), Write(stamp))
        self.wait(1.2)


class M10_B08Eval(Scene):
    def construct(self):
        dims = [("scripting", "strong — it all runs", ACCENT),
                ("agents", "useful, supervised", ACCENT),
                ("analysis", "strongest — from measurement", ACCENT),
                ("repo work", "solid — one failure owned", ACCENT),
                ("film production", "packages gated — you judge the cut", GREY)]
        rows = VGroup()
        for i, (name, note, col) in enumerate(dims):
            y = 2.0 - i * 1.15
            bg = RoundedRectangle(corner_radius=0.15, width=10.6, height=0.95,
                                  fill_color=CARD, fill_opacity=1,
                                  stroke_color=INK).move_to([0, y, 0])
            bar = Rectangle(width=0.28, height=0.95, fill_color=col,
                            fill_opacity=1, stroke_width=0).move_to([-5.15, y, 0])
            tn = T(name, font_size=26, color=INK).move_to([-3.6, y + 0.14, 0])
            td = T(note, font_size=19, color=GREY).move_to([-3.55, y - 0.26, 0])
            rows.add(VGroup(bg, bar, tn, td))
        cap = T("Muse evaluates Muse", font_size=32, color=INK).to_edge(
            UP, buff=0.6)
        self.play(Write(cap))
        for r in rows:
            self.play(FadeIn(r[0]))
            self.play(GrowFromEdge(r[1], LEFT), run_time=0.35)
            self.play(FadeIn(r[2], shift=RIGHT * 0.2),
                      FadeIn(r[3], shift=RIGHT * 0.2), run_time=0.45)
        self.wait(1.2)


class M11_BvdtHtfOut(Scene):
    def construct(self):
        plate = RoundedRectangle(corner_radius=0.25, width=11.8, height=4.8,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK)
        recap = VGroup(*[
            T("1 · the package: summary + honest architecture", font_size=26,
                 color=INK),
            T("2 · failure paths, one spec, a demo that shows the gap",
                 font_size=26, color=INK),
            T("3 · linear, zero-cost, client-ready — blocker disclosed",
                 font_size=26, color=INK),
            T("4 · the evaluation: graded, with the failure owned",
                 font_size=26, color=INK),
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to(ORIGIN)
        self.play(FadeIn(plate))
        for r in recap:
            self.play(FadeIn(r, shift=RIGHT * 0.3), run_time=0.6)
        self.wait(0.8)
        self.play(FadeOut(recap), FadeOut(plate))
        doplate = RoundedRectangle(corner_radius=0.25, width=10.8, height=3.6,
                                   fill_color="#EDE8DA", fill_opacity=1,
                                   stroke_color=ACCENT)
        do = VGroup(
            T("Your turn", font_size=34, color=ACCENT),
            T("Package one of your projects: summary, diagram, demo plan.",
                 font_size=24, color=INK),
            T("Draw the failure paths in.", font_size=24, color=INK),
            T("What's the gap you'd have to disclose?", font_size=24,
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
