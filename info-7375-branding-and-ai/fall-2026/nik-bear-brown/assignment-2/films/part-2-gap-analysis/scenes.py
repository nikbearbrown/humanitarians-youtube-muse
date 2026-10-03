"""scenes.py — Muse closes the gap (Assignment 2, Part 2 film).

13 Manim scenes, M01–M13. House conventions: 16:9, safe-area coords
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
        cols = ["they ask", "I have", "to build"]
        boxes = VGroup()
        for i, c in enumerate(cols):
            x = -4.0 + i * 4.0
            head = RoundedRectangle(corner_radius=0.15, width=3.6, height=1.0,
                                    fill_color=INK, fill_opacity=1,
                                    stroke_width=0).move_to([x, 1.8, 0])
            ht = Text(c, font_size=24, color=CARD).move_to(head.get_center())
            body = RoundedRectangle(corner_radius=0.15, width=3.6, height=3.0,
                                    fill_color=CARD, fill_opacity=1,
                                    stroke_color=INK).move_to([x, -0.3, 0])
            boxes.add(VGroup(head, ht, body))
        cap = Text("three columns, filled in honestly", font_size=32,
                   color=INK).to_edge(UP, buff=0.7)
        self.play(Write(cap))
        for b in boxes:
            self.play(FadeIn(b[0]), FadeIn(b[1]), run_time=0.4)
            self.play(FadeIn(b[2], shift=UP * 0.2), run_time=0.4)
        self.wait(1.2)


class M02_Bdefs(Scene):
    def construct(self):
        words = ["gap", "evidence", "build", "link"]
        defs = ["posting wants, résumé lacks", "proof, not adjectives",
                "the thing you'll make", "already have it — just link"]
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


class M03_B01Gaps(Scene):
    def construct(self):
        gaps = [("never shipped a design", "system in Figma"),
                ("public speaking", "meetups + conferences"),
                ("travel", "up to 25%")]
        cards = VGroup()
        for i, (a, b) in enumerate(gaps):
            x = -4.2 + i * 4.2
            box = RoundedRectangle(corner_radius=0.2, width=3.8, height=2.6,
                                   fill_color=CARD, fill_opacity=1,
                                   stroke_color=ACCENT, stroke_width=3).move_to(
                [x, 0, 0])
            dot = Circle(radius=0.16, fill_color=ACCENT, fill_opacity=1,
                         stroke_width=0).move_to([x, 0.7, 0])
            ta = Text(a, font_size=22, color=INK).move_to([x, 0.0, 0])
            tb = Text(b, font_size=22, color=INK).move_to([x, -0.5, 0])
            cards.add(VGroup(box, dot, ta, tb))
        cap = Text("Part 1's honest findings", font_size=32,
                   color=INK).to_edge(UP, buff=0.7)
        note = Text("on the page already — no surprises", font_size=22,
                    color=GREY).to_edge(DOWN, buff=0.8)
        self.play(Write(cap))
        for c in cards:
            self.play(FadeIn(c[0]))
            self.play(FadeIn(c[1], scale=1.4))
            self.play(FadeIn(c[2], shift=RIGHT * 0.15),
                      FadeIn(c[3], shift=RIGHT * 0.15), run_time=0.4)
        self.play(FadeIn(note))
        self.wait(1.2)


class M04_B02SecondColumn(Scene):
    def construct(self):
        col1 = RoundedRectangle(corner_radius=0.15, width=3.6, height=4.0,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=BLUE, stroke_width=3).move_to(
            [-2.2, 0, 0])
        t1 = VGroup(Text("Figma", font_size=28, color=BLUE),
                    Text("Designer Advocate", font_size=18, color=INK)
                    ).arrange(DOWN, buff=0.1).move_to(col1.get_center())
        col2 = RoundedRectangle(corner_radius=0.15, width=3.6, height=4.0,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=GREEN, stroke_width=3).move_to(
            [2.2, 0, 0])
        t2 = VGroup(Text("Webflow", font_size=28, color=GREEN),
                    Text("Senior Dev Educator", font_size=18, color=INK)
                    ).arrange(DOWN, buff=0.1).move_to(col2.get_center())
        plus = Text("+", font_size=48, color=INK).move_to(ORIGIN)
        note = Text("one company: anecdote · two: pattern", font_size=24,
                    color=GREY).to_edge(DOWN, buff=0.8)
        cap = Text("the second column", font_size=34, color=INK).to_edge(
            UP, buff=0.7)
        self.play(Write(cap))
        self.play(FadeIn(col1), FadeIn(t1))
        self.play(FadeIn(plus, scale=1.5))
        self.play(FadeIn(col2, scale=0.9), FadeIn(t2))
        self.play(FadeIn(note, shift=UP * 0.2))
        self.wait(1.2)


class M05_B03Row1(Scene):
    def construct(self):
        row = RoundedRectangle(corner_radius=0.2, width=11.0, height=1.6,
                               fill_color=CARD, fill_opacity=1,
                               stroke_color=INK).move_to(UP * 1.6)
        rt = Text("row 1 · teaching material about the product", font_size=28,
                  color=INK).move_to(row.get_center())
        have = RoundedRectangle(corner_radius=0.15, width=5.2, height=2.2,
                                fill_color="#EDE8DA", fill_opacity=1,
                                stroke_width=0).move_to([-2.9, -1.2, 0])
        ht = VGroup(Text("have", font_size=22, color=GREEN),
                    Text("videos · MOOC · pipeline", font_size=18, color=INK)
                    ).arrange(DOWN, buff=0.1).move_to(have.get_center())
        build = RoundedRectangle(corner_radius=0.15, width=5.2, height=2.2,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=ACCENT, stroke_width=3).move_to(
            [2.9, -1.2, 0])
        bt = VGroup(Text("to build", font_size=22, color=ACCENT),
                    Text("tutorials about THEIR product", font_size=18,
                         color=INK)
                    ).arrange(DOWN, buff=0.1).move_to(build.get_center())
        arrow = Arrow([-0.2, -1.2, 0], [0.2, -1.2, 0], color=INK,
                      stroke_width=6, buff=0.05)
        cap = Text("the skill transfers; the subject doesn't", font_size=28,
                   color=INK).to_edge(UP, buff=0.7)
        self.play(Write(cap))
        self.play(FadeIn(row), FadeIn(rt))
        self.play(FadeIn(have), FadeIn(ht), run_time=0.5)
        self.play(GrowArrow(arrow), run_time=0.4)
        self.play(FadeIn(build), FadeIn(bt), run_time=0.5)
        self.wait(1.2)


class M06_B04Row2(Scene):
    def construct(self):
        cam = RoundedRectangle(corner_radius=0.2, width=3.4, height=2.4,
                               fill_color=INK, fill_opacity=1,
                               stroke_width=0).move_to([-3.2, 0, 0])
        lens = Circle(radius=0.5, stroke_color=CARD, stroke_width=4,
                      fill_opacity=0).move_to([-3.2, 0.3, 0])
        rec = Circle(radius=0.14, fill_color=ACCENT, fill_opacity=1,
                     stroke_width=0).move_to([-4.3, 0.9, 0])
        card = RoundedRectangle(corner_radius=0.2, width=6.4, height=2.4,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=ACCENT, stroke_width=3).move_to(
            [2.4, 0, 0])
        ct = VGroup(Text("3–5 min on-camera sample", font_size=24, color=INK),
                    Text("no synthetic narrator", font_size=20, color=ACCENT),
                    Text("one design-system idea", font_size=20, color=GREY)
                    ).arrange(DOWN, buff=0.12).move_to(card.get_center())
        cap = Text("row 2 · your own voice, because the job says so",
                   font_size=28, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(cap))
        self.play(FadeIn(cam))
        self.play(Create(lens), FadeIn(rec))
        self.play(FadeIn(card, shift=LEFT * 0.3))
        for t in ct:
            self.play(FadeIn(t, shift=UP * 0.15), run_time=0.4)
        self.wait(1.2)


class M07_B05Row3(Scene):
    def construct(self):
        sys1 = RoundedRectangle(corner_radius=0.15, width=4.6, height=3.0,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=BLUE, stroke_width=3).move_to(
            [-2.8, 0, 0])
        s1t = VGroup(Text("shipped Figma", font_size=24, color=BLUE),
                     Text("design system", font_size=24, color=BLUE),
                     Text("tokens + Dev Mode", font_size=18, color=GREY)
                     ).arrange(DOWN, buff=0.1).move_to(sys1.get_center())
        sys2 = RoundedRectangle(corner_radius=0.15, width=4.6, height=3.0,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=GREEN, stroke_width=3).move_to(
            [2.8, 0, 0])
        s2t = VGroup(Text("production", font_size=24, color=GREEN),
                     Text("Webflow site", font_size=24, color=GREEN),
                     Text("real, open", font_size=18, color=GREY)
                     ).arrange(DOWN, buff=0.1).move_to(sys2.get_center())
        star = Circle(radius=0.4, fill_color=ACCENT, fill_opacity=1,
                      stroke_width=0).move_to([0, 2.2, 0])
        note = Text("the biggest row — it gets its own project", font_size=24,
                    color=INK).to_edge(DOWN, buff=0.8)
        cap = Text("row 3 · hands-on depth", font_size=34, color=INK).to_edge(
            UP, buff=0.7)
        self.play(Write(cap))
        self.play(FadeIn(star, scale=1.5))
        self.play(FadeIn(sys1), FadeIn(s1t), run_time=0.6)
        self.play(FadeIn(sys2), FadeIn(s2t), run_time=0.6)
        self.play(FadeIn(note, shift=UP * 0.2))
        self.wait(1.2)


class M08_B06Row4(Scene):
    def construct(self):
        crowd = VGroup(*[Circle(radius=0.3, fill_color=BLUE, fill_opacity=0.6,
                                stroke_width=0).move_to(
            [-3.5 + (i % 4) * 0.9, 0.8 - (i // 4) * 0.9, 0])
            for i in range(8)])
        card = RoundedRectangle(corner_radius=0.2, width=6.0, height=2.6,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=ACCENT, stroke_width=3).move_to(
            [2.8, 0, 0])
        ct = VGroup(Text("speaking reel", font_size=26, color=INK),
                    Text("cut from existing recordings", font_size=20,
                         color=GREY),
                    Text("+ talk list", font_size=20, color=INK)
                    ).arrange(DOWN, buff=0.12).move_to(card.get_center())
        note = Text("the evidence exists; it needs editing", font_size=24,
                    color=GREY).to_edge(DOWN, buff=0.8)
        cap = Text("row 4 · community and speaking", font_size=32,
                   color=INK).to_edge(UP, buff=0.7)
        self.play(Write(cap))
        self.play(*[FadeIn(c, scale=0.6) for c in crowd], run_time=0.9)
        self.play(FadeIn(card, shift=LEFT * 0.3))
        for t in ct:
            self.play(FadeIn(t, shift=UP * 0.15), run_time=0.4)
        self.play(FadeIn(note, shift=UP * 0.2))
        self.wait(1.2)


class M09_B07Row5(Scene):
    def construct(self):
        card = RoundedRectangle(corner_radius=0.2, width=10.0, height=2.6,
                                fill_color="#EDE8DA", fill_opacity=1,
                                stroke_color=GREEN, stroke_width=3).move_to(
            ORIGIN)
        t = Text("row 5 · AI workflows, MCP, evals", font_size=30,
                 color=INK).move_to(UP * 0.5)
        v = Text("already covered — link, don't rebuild", font_size=28,
                 color=GREEN).move_to(DOWN * 0.4)
        link = VGroup(
            Line([-1.2, -0.4, 0], [-0.4, -0.4, 0], color=GREEN, stroke_width=8),
            Line([-0.4, -0.4, 0], [-0.4, 0.4, 0], color=GREEN, stroke_width=8),
            Line([-0.4, 0.4, 0], [-1.2, 0.4, 0], color=GREEN, stroke_width=8))
        link.move_to([-4.0, 0, 0])
        note = Text("knowing which rows need no work is part of the analysis",
                    font_size=22, color=GREY).to_edge(DOWN, buff=0.8)
        cap = Text("the free row", font_size=34, color=INK).to_edge(UP,
                                                                     buff=0.7)
        self.play(Write(cap))
        self.play(FadeIn(card))
        self.play(Create(link), run_time=0.5)
        self.play(FadeIn(t, shift=DOWN * 0.15))
        self.play(FadeIn(v, shift=UP * 0.15))
        self.play(FadeIn(note, shift=UP * 0.2))
        self.wait(1.2)


class M10_B08BuildList(Scene):
    def construct(self):
        items = ["tutorials about their products",
                 "one on-camera sample",
                 "one design system + one production site",
                 "one speaking reel"]
        rows = VGroup()
        for i, it in enumerate(items):
            y = 1.8 - i * 1.1
            sq = Square(side_length=0.3, stroke_color=ACCENT, stroke_width=4,
                        fill_opacity=0).move_to([-4.8, y, 0])
            t = Text(f"{i+1}. {it}", font_size=26, color=INK).move_to(
                [-1.6, y, 0])
            rows.add(VGroup(sq, t))
        note = Text("nothing on the list is decorative", font_size=24,
                    color=GREY).to_edge(DOWN, buff=0.8)
        cap = Text("the build list", font_size=34, color=INK).to_edge(UP,
                                                                      buff=0.7)
        self.play(Write(cap))
        for r in rows:
            self.play(FadeIn(r[0], scale=1.3))
            self.play(FadeIn(r[1], shift=RIGHT * 0.25), run_time=0.45)
        self.play(FadeIn(note, shift=UP * 0.2))
        self.wait(1.2)


class M11_B09Madison(Scene):
    def construct(self):
        proj = RoundedRectangle(corner_radius=0.25, width=8.0, height=3.6,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=BLUE, stroke_width=4).move_to(
            ORIGIN)
        t = Text("the Madison project", font_size=34, color=BLUE).move_to(
            UP * 0.7)
        s = Text("closes the Figma design-systems gap", font_size=26,
                 color=INK).move_to(DOWN * 0.1)
        s2 = Text("stated in Part 1, before any building", font_size=20,
                  color=GREY).move_to(DOWN * 0.9)
        bridge = DoubleArrow([-4.5, 2.2, 0], [4.5, 2.2, 0], color=INK,
                             buff=0.1, stroke_width=5)
        bl = Text("course project = job search, with a syllabus", font_size=22,
                  color=INK).move_to(UP * 2.7)
        cap = Text("the biggest gap already has its project", font_size=30,
                   color=INK).to_edge(UP, buff=0.7)
        self.play(Write(cap))
        self.play(FadeIn(bl, shift=DOWN * 0.2))
        self.play(GrowFromCenter(bridge), run_time=0.6)
        self.play(FadeIn(proj, scale=0.92))
        self.play(FadeIn(t, shift=DOWN * 0.15))
        self.play(FadeIn(s, shift=UP * 0.15))
        self.play(FadeIn(s2, shift=UP * 0.15))
        self.wait(1.2)


class M12_B10Honest(Scene):
    def construct(self):
        table = RoundedRectangle(corner_radius=0.2, width=9.6, height=3.4,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK).move_to(UP * 0.3)
        tt = Text("gaps and all — in the repo", font_size=30,
                  color=INK).move_to(table.get_center())
        eye = Circle(radius=0.6, stroke_color=GREEN, stroke_width=4,
                     fill_opacity=0).move_to(DOWN * 1.8)
        et = Text("gaps close by building, in the open", font_size=24,
                  color=GREEN).move_to(DOWN * 2.7)
        cap = Text("the honest column stays public", font_size=32,
                   color=INK).to_edge(UP, buff=0.7)
        self.play(Write(cap))
        self.play(FadeIn(table))
        self.play(FadeIn(tt, shift=DOWN * 0.15))
        self.play(Create(eye))
        self.play(FadeIn(et, shift=UP * 0.2))
        self.wait(1.5)


class M13_BvdtHtfOut(Scene):
    def construct(self):
        plate = RoundedRectangle(corner_radius=0.25, width=11.8, height=4.8,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK)
        recap = VGroup(*[
            Text("1 · name the gap: three findings + a second column",
                 font_size=26, color=INK),
            Text("2 · the five rows: ask / have / build — one free",
                 font_size=26, color=INK),
            Text("3 · the build list: four things; Madison closes the big one",
                 font_size=26, color=INK),
            Text("4 · the honest column: the table stays public",
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
            Text("Draw the three columns.", font_size=24, color=INK),
            Text("Fill every row from real postings.", font_size=24,
                 color=INK),
            Text("Find the free row.", font_size=24, color=INK),
        ).arrange(DOWN, buff=0.25).move_to(ORIGIN)
        self.play(FadeIn(doplate))
        for d in do:
            self.play(FadeIn(d, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)
        self.play(FadeOut(do), FadeOut(doplate))
        out = title_card("Muse, in for Bear", "@NikBearBrown")
        self.play(FadeIn(out))
        self.wait(1.5)
