"""scenes.py — Muse widens the search (Assignment 2 appendix film).

11 Manim scenes, M01–M11. House conventions: 16:9, safe-area coords
(±6.3 x, ±3.4 y), distinct non-text shapes per beat, every on-screen text
is read aloud in its beat.
"""
from manim import *

config.pixel_width = 1920
config.pixel_height = 1080

INK = "#111111"
PAPER = "#F7F3EA"
ACCENT = "#B8472F"
BLUE = "#2F6BB8"
GREEN = "#2E8B57"
GREY = "#8A8578"
CARD = "#FFFFFF"


def title_card(title, sub=None):
    g = VGroup()
    t = Text(title, font_size=40, color=INK).move_to(ORIGIN)
    g.add(t)
    if sub:
        s = Text(sub, font_size=24, color=GREY).next_to(t, DOWN, buff=0.3)
        g.add(s)
    return g


class M01_Bidea(Scene):
    def construct(self):
        one = RoundedRectangle(corner_radius=0.2, width=3.4, height=4.4,
                               fill_color=CARD, fill_opacity=1,
                               stroke_color=INK).move_to([-3.6, 0, 0])
        seven = VGroup(*[RoundedRectangle(corner_radius=0.12, width=1.9,
                                          height=2.6, fill_color=CARD,
                                          fill_opacity=1, stroke_color=BLUE)
                         for _ in range(7)]).arrange(RIGHT, buff=0.25).move_to(
            [2.2, 0, 0])
        trap = Text("the trap is the word “one”", font_size=30,
                    color=ACCENT).to_edge(UP, buff=0.7)
        self.play(FadeIn(one))
        self.play(*[FadeIn(s, shift=UP * 0.25) for s in seven],
                  run_time=1.2)
        self.play(Write(trap))
        self.wait(1.2)


class M02_Bdefs(Scene):
    def construct(self):
        words = ["ATS", "feed", "blurb", "sweep"]
        defs = ["the system behind the page", "public JSON, no key",
                "boilerplate that poisons matching", "all of it, one afternoon"]
        cards = VGroup()
        for i, (w, d) in enumerate(zip(words, defs)):
            x = -5.4 + i * 3.6
            box = RoundedRectangle(corner_radius=0.2, width=3.2, height=2.4,
                                   fill_color=CARD, fill_opacity=1,
                                   stroke_color=INK).move_to([x, 0, 0])
            t = Text(w, font_size=28, color=ACCENT).move_to([x, 0.55, 0])
            s = Text(d, font_size=15, color=INK).move_to([x, -0.35, 0])
            cards.add(VGroup(box, t, s))
        for c in cards:
            self.play(FadeIn(c, shift=UP * 0.3), run_time=0.7)
        self.wait(1.2)


class M03_B01ThreeATS(Scene):
    def construct(self):
        data = [("Greenhouse", "Figma · Webflow · Miro", BLUE,
                 "one call, full ad text"),
                ("Ashby", "Writer · Notion · Jasper", GREEN,
                 "one call; watch the spaces"),
                ("SmartRecruiters", "Canva", ACCENT,
                 "paged; no ad text")]
        cards = VGroup()
        for i, (name, cos, col, note) in enumerate(data):
            y = 1.8 - i * 1.8
            box = RoundedRectangle(corner_radius=0.2, width=10.4, height=1.5,
                                   fill_color=CARD, fill_opacity=1,
                                   stroke_color=col, stroke_width=3).move_to(
                [0, y, 0])
            bar = Rectangle(width=0.28, height=1.5, fill_color=col,
                            fill_opacity=1, stroke_width=0).move_to(
                [-5.05, y, 0])
            tn = Text(name, font_size=28, color=col).move_to([-3.4, y + 0.2, 0])
            tc = Text(cos, font_size=20, color=INK).move_to([-3.35, y - 0.35, 0])
            td = Text(note, font_size=20, color=GREY).move_to([2.6, y, 0])
            cards.add(VGroup(box, bar, tn, tc, td))
        cap = Text("three systems, one script", font_size=32,
                   color=INK).to_edge(UP, buff=0.7)
        self.play(Write(cap))
        for c in cards:
            self.play(FadeIn(c[0]))
            self.play(GrowFromEdge(c[1], UP), run_time=0.3)
            self.play(FadeIn(c[2], shift=RIGHT * 0.2),
                      FadeIn(c[3], shift=RIGHT * 0.2),
                      FadeIn(c[4], shift=RIGHT * 0.2), run_time=0.5)
        self.wait(1.2)


class M04_B02CanvaBuild(Scene):
    def construct(self):
        host = RoundedRectangle(corner_radius=0.2, width=9.6, height=1.6,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=INK).move_to(UP * 1.4)
        ht = Text("one host: api.smartrecruiters.com", font_size=26,
                  color=INK).move_to(host.get_center())
        reqs = VGroup(*[Circle(radius=0.14, fill_color=ACCENT, fill_opacity=1,
                               stroke_width=0).move_to(
            [-4.5 + (i % 25) * 0.38, 0.2 - (i // 25) * 0.38, 0])
            for i in range(50)])
        stats = VGroup(
            Text("248 jobs", font_size=30, color=INK),
            Text("3m 38s · 251 requests", font_size=26, color=ACCENT),
            Text("not hard — just patient", font_size=22, color=GREY),
        ).arrange(DOWN, buff=0.2).move_to(DOWN * 1.9)
        cap = Text("building the third reader", font_size=32,
                   color=INK).to_edge(UP, buff=0.7)
        self.play(Write(cap))
        self.play(FadeIn(host), FadeIn(ht))
        self.play(*[FadeIn(r, scale=0.5) for r in reqs], run_time=1.4)
        for s in stats:
            self.play(FadeIn(s, shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)


class M05_B03Field(Scene):
    def construct(self):
        cos = [("Figma", 152), ("Writer", 51), ("Canva", 248),
               ("Notion", 128), ("Webflow", 29), ("Miro", 28), ("Jasper", 7)]
        bars = VGroup()
        for i, (name, n) in enumerate(cos):
            x = -5.4 + i * 1.8
            h = max(0.5, n / 248 * 3.4)
            bar = Rectangle(width=1.2, height=h, fill_color=BLUE,
                            fill_opacity=0.75, stroke_width=0).move_to(
                [x, -2.2 + h / 2, 0])
            tn = Text(name, font_size=18, color=INK).move_to([x, -2.6, 0])
            tv = Text(str(n), font_size=20, color=ACCENT).move_to(
                [x, -2.2 + h + 0.25, 0])
            bars.add(VGroup(bar, tn, tv))
        total = Text("643 postings, one résumé", font_size=30,
                     color=INK).to_edge(UP, buff=0.7)
        self.play(Write(total))
        for b in bars:
            self.play(GrowFromEdge(b[0], DOWN), run_time=0.4)
            self.play(FadeIn(b[1]), FadeIn(b[2]), run_time=0.25)
        self.wait(1.2)


class M06_B04WriterBlurb(Scene):
    def construct(self):
        big = Text("51 / 51", font_size=64, color=ACCENT).move_to(UP * 1.2)
        words = VGroup()
        for w in ["generative AI", "AI agents", "learning"]:
            bg = RoundedRectangle(corner_radius=0.12, width=4.6, height=0.8,
                                  fill_color="#EDE8DA", fill_opacity=1,
                                  stroke_width=0)
            t = Text(w, font_size=22, color=INK)
            x = Line([-2.0, 0.3, 0], [2.0, -0.3, 0], color=ACCENT,
                     stroke_width=6)
            words.add(VGroup(bg, t, x))
        words.arrange(DOWN, buff=0.25).move_to(DOWN * 0.3)
        fixed = Text("→ 24  (a change to the rules, not the résumé)",
                     font_size=26, color=GREEN).move_to(DOWN * 2.3)
        cap = Text("the blurb failure — write it down", font_size=30,
                   color=INK).to_edge(UP, buff=0.7)
        self.play(Write(cap))
        self.play(FadeIn(big, scale=1.3))
        for w in words:
            self.play(FadeIn(w[0]), FadeIn(w[1], shift=RIGHT * 0.15),
                      run_time=0.4)
            self.play(Create(w[2]), run_time=0.35)
        self.play(FadeIn(fixed, shift=UP * 0.2))
        self.wait(1.2)


class M07_B05BetterFit(Scene):
    def construct(self):
        card = RoundedRectangle(corner_radius=0.25, width=9.6, height=4.4,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=GREEN, stroke_width=4).move_to(
            ORIGIN)
        t = Text("Senior Developer Educator, Webflow", font_size=34,
                 color=INK).move_to(UP * 1.1)
        pay = Text("$113K – $155K · US remote · new", font_size=26,
                   color=GREEN).move_to(UP * 0.2)
        job = Text("on camera, behind Webflow University", font_size=24,
                   color=INK).move_to(DOWN * 0.7)
        col2 = Text("the gap analysis gets a second column", font_size=22,
                    color=GREY).move_to(DOWN * 1.5)
        badge = Circle(radius=0.42, fill_color=GREEN, fill_opacity=1,
                       stroke_width=0).move_to([-3.9, 1.1, 0])
        cap = Text("the better fit", font_size=34, color=INK).to_edge(
            UP, buff=0.7)
        self.play(Write(cap))
        self.play(FadeIn(card, scale=0.92))
        self.play(FadeIn(badge, scale=1.5), Write(t), run_time=0.8)
        self.play(FadeIn(pay, shift=UP * 0.2))
        self.play(FadeIn(job, shift=UP * 0.2))
        self.play(FadeIn(col2, shift=UP * 0.2))
        self.wait(1.2)


class M08_B06Word(Scene):
    def construct(self):
        old = Text("Advocate", font_size=54, color=GREY).move_to(
            LEFT * 3 + UP * 0.4)
        new = Text("Educator", font_size=54, color=ACCENT).move_to(
            RIGHT * 3 + UP * 0.4)
        arrow = Arrow([-1.2, 0.4, 0], [1.2, 0.4, 0], color=INK,
                      stroke_width=8, buff=0.15)
        note = Text("2 of the 6 best never say “Advocate”", font_size=24,
                    color=INK).move_to(DOWN * 1.4)
        sub = Text("the sweep taught the searcher what to call them",
                   font_size=22, color=GREY).move_to(DOWN * 2.2)
        cap = Text("the changed word", font_size=34, color=INK).to_edge(
            UP, buff=0.7)
        strike = Line([-4.6, 0.4, 0], [-1.4, 0.4, 0], color=ACCENT,
                      stroke_width=8)
        halo = RoundedRectangle(corner_radius=0.2, width=4.4, height=1.6,
                                fill_color=ACCENT, fill_opacity=0.12,
                                stroke_color=ACCENT, stroke_width=3).move_to(
            RIGHT * 3 + UP * 0.4)
        self.play(Write(cap))
        self.play(FadeIn(old, shift=RIGHT * 0.3))
        self.play(Create(strike), run_time=0.5)
        self.play(GrowArrow(arrow), run_time=0.6)
        self.play(FadeIn(halo, scale=1.2), FadeIn(new, scale=1.1),
                  run_time=0.7)
        self.play(FadeIn(note, shift=UP * 0.2))
        self.play(FadeIn(sub, shift=UP * 0.2))
        self.wait(1.2)


class M09_B07NotFound(Scene):
    def construct(self):
        shelf = Rectangle(width=9.6, height=0.25, fill_color=INK,
                          fill_opacity=1, stroke_width=0).move_to(DOWN * 0.4)
        zero = Text("0", font_size=72, color=GREY).move_to(UP * 0.9)
        zl = Text("part-time / contract / consulting education roles",
                  font_size=24, color=INK).move_to(UP * 0.0)
        z2 = Text("in the US, at any of the seven", font_size=24,
                  color=INK).move_to(DOWN * -0.55 + UP * 0.35)
        shape = Text("the shape exists — just not for this work",
                     font_size=22, color=GREY).move_to(DOWN * 2.2)
        empty = DashedLine([-4.8, 1.9, 0], [4.8, 1.9, 0], color=GREY,
                           dash_length=0.3)
        empty_box = Rectangle(width=9.6, height=2.2, stroke_color=GREY,
                              stroke_width=2).move_to(UP * 0.8)
        cap = Text("what it did not find", font_size=34, color=INK).to_edge(
            UP, buff=0.7)
        self.play(Write(cap))
        self.play(Create(empty_box))
        self.play(FadeIn(shelf))
        self.play(FadeIn(zero, scale=1.3))
        self.play(Create(empty), run_time=0.4)
        self.play(FadeIn(zl, shift=UP * 0.2))
        self.play(FadeIn(z2, shift=UP * 0.2))
        self.play(FadeIn(shape, shift=UP * 0.2))
        self.wait(1.2)


class M10_B08Unreadable(Scene):
    def construct(self):
        data = [("Framer", "hand-built pages"), ("Adobe", "Workday"),
                ("Sketch · InVision · Mural", "unconfirmed")]
        cards = VGroup()
        for i, (name, why) in enumerate(data):
            y = 1.6 - i * 1.7
            box = RoundedRectangle(corner_radius=0.2, width=9.6, height=1.4,
                                   fill_color="#EDE8DA", fill_opacity=0.85,
                                   stroke_color=GREY, stroke_width=2).move_to(
                [0, y, 0])
            lock = Circle(radius=0.28, fill_color=GREY, fill_opacity=1,
                          stroke_width=0).move_to([-4.0, y, 0])
            tn = Text(name, font_size=26, color=GREY).move_to([-2.4, y + 0.18, 0])
            tw = Text(why, font_size=20, color=GREY).move_to([-2.35, y - 0.32, 0])
            cards.add(VGroup(box, lock, tn, tw))
        cap = Text("unreadable — stated, not hidden", font_size=32,
                   color=INK).to_edge(UP, buff=0.7)
        self.play(Write(cap))
        for c in cards:
            self.play(FadeIn(c[0]))
            self.play(FadeIn(c[1], scale=1.3))
            self.play(FadeIn(c[2], shift=RIGHT * 0.2),
                      FadeIn(c[3], shift=RIGHT * 0.2), run_time=0.5)
        self.wait(1.2)


class M11_BvdtHtfOut(Scene):
    def construct(self):
        plate = RoundedRectangle(corner_radius=0.25, width=11.8, height=4.8,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK)
        recap = VGroup(*[
            Text("1 · three systems — and the patient third build",
                 font_size=26, color=INK),
            Text("2 · the field: 643 postings, the blurb failure",
                 font_size=26, color=INK),
            Text("3 · what changed: a better fit, a better word",
                 font_size=26, color=INK),
            Text("4 · not found: no part-time; three unreadable",
                 font_size=26, color=INK),
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to(ORIGIN)
        self.play(FadeIn(plate))
        for r in recap:
            self.play(FadeIn(r, shift=RIGHT * 0.3), run_time=0.6)
        self.wait(0.8)
        self.play(FadeOut(recap), FadeOut(plate))
        doplate = RoundedRectangle(corner_radius=0.25, width=10.8, height=3.4,
                                   fill_color="#EDE8DA", fill_opacity=1,
                                   stroke_color=ACCENT)
        do = VGroup(
            Text("Your turn", font_size=34, color=ACCENT),
            Text("Pick your seven companies.", font_size=24, color=INK),
            Text("Before you trust one match,", font_size=24, color=INK),
            Text("read the company blurb first.", font_size=24, color=INK),
        ).arrange(DOWN, buff=0.25).move_to(ORIGIN)
        self.play(FadeIn(doplate))
        for d in do:
            self.play(FadeIn(d, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)
        self.play(FadeOut(do), FadeOut(doplate))
        out = title_card("Muse, in for Bear", "@NikBearBrown")
        self.play(FadeIn(out))
        self.wait(1.5)
