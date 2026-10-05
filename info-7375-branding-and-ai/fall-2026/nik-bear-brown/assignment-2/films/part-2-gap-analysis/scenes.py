"""scenes.py — Muse closes the gap (Assignment 2, Part 2 film).

13 Manim scenes, M01–M13. House conventions: 16:9, safe-area coords
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
    # 3x oversample: 2x still drops inter-word spaces at small sizes
    # (verified: raw fs=40 drops spaces in "cut from", "resume lacks"...;
    #  raw fs>=56 / 3x oversample is pixel-clean on all tested strings)
    return Text(s, font_size=fs * 3, **kw).scale(1 / 3)


def title_card(title, sub=None):
    g = VGroup()
    t = T(title, font="EB Garamond", font_size=40, color=INK).move_to(ORIGIN)
    g.add(t)
    if sub:
        s = T(sub, font="EB Garamond", font_size=24, color=INK).next_to(t, DOWN, buff=0.3)
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
            ht = T(c, font="EB Garamond", font_size=24, color=CARD).move_to(head.get_center())
            body = RoundedRectangle(corner_radius=0.15, width=3.6, height=3.0,
                                    fill_color=CARD, fill_opacity=1,
                                    stroke_color=INK).move_to([x, -0.3, 0])
            boxes.add(VGroup(head, ht, body))
        cap = T("three columns, filled in honestly", font="EB Garamond", font_size=32,
                   color=INK).to_edge(UP, buff=0.7)
        self.play(FadeIn(cap))
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
            t = T(w, font="EB Garamond", font_size=28, color=ACCENT).move_to([x, 0.55, 0])
            s = T(d, font="EB Garamond", font_size=15, color=INK).move_to([x, -0.35, 0])
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
            ta = T(a, font="EB Garamond", font_size=22, color=INK).move_to([x, 0.0, 0])
            tb = T(b, font="EB Garamond", font_size=22, color=INK).move_to([x, -0.5, 0])
            cards.add(VGroup(box, dot, ta, tb))
        cap = T("Part 1's honest findings", font="EB Garamond", font_size=32,
                   color=INK).to_edge(UP, buff=0.7)
        note = T("on the page already — no surprises", font="EB Garamond", font_size=22,
                    color=INK).to_edge(DOWN, buff=0.8)
        self.play(FadeIn(cap))
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
                                stroke_color=INK, stroke_width=3).move_to(
            [-2.2, 0, 0])
        t1 = VGroup(T("Figma", font="EB Garamond", font_size=28, color=INK),
                    T("Designer Advocate", font="EB Garamond", font_size=18, color=INK)
                    ).arrange(DOWN, buff=0.1).move_to(col1.get_center())
        col2 = RoundedRectangle(corner_radius=0.15, width=3.6, height=4.0,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=ACCENT, stroke_width=3).move_to(
            [2.2, 0, 0])
        t2 = VGroup(T("Webflow", font="EB Garamond", font_size=28, color=ACCENT),
                    T("Senior Dev Educator", font="EB Garamond", font_size=18, color=INK)
                    ).arrange(DOWN, buff=0.1).move_to(col2.get_center())
        plus = T("+", font="EB Garamond", font_size=48, color=INK).move_to(ORIGIN)
        note = T("one company: anecdote · two: pattern", font="EB Garamond", font_size=24,
                    color=INK).to_edge(DOWN, buff=0.8)
        cap = T("the second column", font="EB Garamond", font_size=34, color=INK).to_edge(
            UP, buff=0.7)
        self.play(FadeIn(cap))
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
        rt = T("row 1 · teaching material about the product", font="EB Garamond", font_size=28,
                  color=INK).move_to(row.get_center())
        have = RoundedRectangle(corner_radius=0.15, width=5.2, height=2.2,
                                fill_color="#EDE8DA", fill_opacity=1,
                                stroke_width=0).move_to([-2.9, -1.2, 0])
        ht = VGroup(T("have", font="EB Garamond", font_size=22, color=INK),
                    T("videos · MOOC · pipeline", font="EB Garamond", font_size=18, color=INK)
                    ).arrange(DOWN, buff=0.1).move_to(have.get_center())
        build = RoundedRectangle(corner_radius=0.15, width=5.2, height=2.2,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=ACCENT, stroke_width=3).move_to(
            [2.9, -1.2, 0])
        bt = VGroup(T("to build", font="EB Garamond", font_size=22, color=ACCENT),
                    T("tutorials about THEIR product", font="EB Garamond", font_size=18,
                         color=INK)
                    ).arrange(DOWN, buff=0.1).move_to(build.get_center())
        arrow = Arrow([-0.2, -1.2, 0], [0.2, -1.2, 0], color=INK,
                      stroke_width=6, buff=0.05)
        cap = T("the skill transfers; the subject doesn't", font="EB Garamond", font_size=28,
                   color=INK).to_edge(UP, buff=0.7)
        self.play(FadeIn(cap))
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
        ct = VGroup(T("3–5 min on-camera sample", font="EB Garamond", font_size=24, color=INK),
                    T("no synthetic narrator", font="EB Garamond", font_size=20, color=ACCENT),
                    T("one design-system idea", font="EB Garamond", font_size=20, color=INK)
                    ).arrange(DOWN, buff=0.12).move_to(card.get_center())
        cap = T("row 2 · your own voice, because the job says so",
                   font="EB Garamond", font_size=28, color=INK).to_edge(UP, buff=0.7)
        self.play(FadeIn(cap))
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
                                stroke_color=INK, stroke_width=3).move_to(
            [-2.8, 0, 0])
        s1t = VGroup(T("shipped Figma", font="EB Garamond", font_size=24, color=INK),
                     T("design system", font="EB Garamond", font_size=24, color=INK),
                     T("tokens + Dev Mode", font="EB Garamond", font_size=18, color=INK)
                     ).arrange(DOWN, buff=0.1).move_to(sys1.get_center())
        sys2 = RoundedRectangle(corner_radius=0.15, width=4.6, height=3.0,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=GREY, stroke_width=3).move_to(
            [2.8, 0, 0])
        s2t = VGroup(T("production", font="EB Garamond", font_size=24, color=GREY),
                     T("Webflow site", font="EB Garamond", font_size=24, color=GREY),
                     T("real, open", font="EB Garamond", font_size=18, color=INK)
                     ).arrange(DOWN, buff=0.1).move_to(sys2.get_center())
        star = Circle(radius=0.4, fill_color=ACCENT, fill_opacity=1,
                      stroke_width=0).move_to([0, 2.2, 0])
        note = T("the biggest row — it gets its own project", font="EB Garamond", font_size=24,
                    color=INK).to_edge(DOWN, buff=0.8)
        cap = T("row 3 · hands-on depth", font="EB Garamond", font_size=34, color=INK).to_edge(
            UP, buff=0.7)
        self.play(FadeIn(cap))
        self.play(FadeIn(star, scale=1.5))
        self.play(FadeIn(sys1), FadeIn(s1t), run_time=0.6)
        self.play(FadeIn(sys2), FadeIn(s2t), run_time=0.6)
        self.play(FadeIn(note, shift=UP * 0.2))
        self.wait(1.2)


class M08_B06Row4(Scene):
    def construct(self):
        crowd = VGroup(*[Circle(radius=0.3, fill_color=INK, fill_opacity=0.6,
                                stroke_width=0).move_to(
            [-3.5 + (i % 4) * 0.9, 0.8 - (i // 4) * 0.9, 0])
            for i in range(8)])
        card = RoundedRectangle(corner_radius=0.2, width=6.0, height=2.6,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=ACCENT, stroke_width=3).move_to(
            [2.8, 0, 0])
        ct = VGroup(T("speaking reel", font="EB Garamond", font_size=26, color=INK),
                    T("cut from existing recordings", font="EB Garamond", font_size=20,
                         color=INK),
                    T("+ talk list", font="EB Garamond", font_size=20, color=INK)
                    ).arrange(DOWN, buff=0.12).move_to(card.get_center())
        note = T("the evidence exists; it needs editing", font="EB Garamond", font_size=24,
                    color=INK).to_edge(DOWN, buff=0.8)
        cap = T("row 4 · community and speaking", font="EB Garamond", font_size=32,
                   color=INK).to_edge(UP, buff=0.7)
        self.play(FadeIn(cap))
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
                                stroke_color=ACCENT, stroke_width=3).move_to(
            ORIGIN)
        t = T("row 5 · AI workflows, MCP, evals", font="EB Garamond", font_size=30,
                 color=INK).move_to(UP * 0.5)
        v = T("already covered — link, don't rebuild", font="EB Garamond", font_size=28,
                 color=ACCENT).move_to(DOWN * 0.4)
        link = VGroup(
            Line([-1.2, -0.4, 0], [-0.4, -0.4, 0], color=ACCENT, stroke_width=8),
            Line([-0.4, -0.4, 0], [-0.4, 0.4, 0], color=ACCENT, stroke_width=8),
            Line([-0.4, 0.4, 0], [-1.2, 0.4, 0], color=ACCENT, stroke_width=8))
        link.move_to([-4.0, 0, 0])
        note = T("knowing which rows need no work is part of the analysis",
                    font="EB Garamond", font_size=22, color=INK).to_edge(DOWN, buff=0.8)
        cap = T("the free row", font="EB Garamond", font_size=34, color=INK).to_edge(UP,
                                                                     buff=0.7)
        self.play(FadeIn(cap))
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
            t = T(f"{i+1}. {it}", font="EB Garamond", font_size=26, color=INK).move_to(
                [-1.6, y, 0])
            rows.add(VGroup(sq, t))
        note = T("nothing on the list is decorative", font="EB Garamond", font_size=24,
                    color=INK).to_edge(DOWN, buff=0.8)
        cap = T("the build list", font="EB Garamond", font_size=34, color=INK).to_edge(UP,
                                                                      buff=0.7)
        self.play(FadeIn(cap))
        for r in rows:
            self.play(FadeIn(r[0], scale=1.3))
            self.play(FadeIn(r[1], shift=RIGHT * 0.25), run_time=0.45)
        self.play(FadeIn(note, shift=UP * 0.2))
        self.wait(1.2)


class M11_B09Madison(Scene):
    def construct(self):
        proj = RoundedRectangle(corner_radius=0.25, width=8.0, height=3.6,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=ACCENT, stroke_width=4).move_to(
            ORIGIN)
        t = T("the Madison project", font="EB Garamond", font_size=34, color=ACCENT).move_to(
            UP * 0.7)
        s = T("closes the Figma design-systems gap", font="EB Garamond", font_size=26,
                 color=INK).move_to(DOWN * 0.1)
        s2 = T("stated in Part 1, before any building", font="EB Garamond", font_size=20,
                  color=INK).move_to(DOWN * 0.9)
        bridge = DoubleArrow([-4.5, 2.2, 0], [4.5, 2.2, 0], color=INK,
                             buff=0.1, stroke_width=5)
        bl = T("course project = job search, with a syllabus", font="EB Garamond", font_size=22,
                  color=INK).move_to(UP * 2.7)
        cap = T("the biggest gap already has its project", font="EB Garamond", font_size=30,
                   color=INK).to_edge(UP, buff=0.7)
        self.play(FadeIn(cap))
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
        tt = T("gaps and all — in the repo", font="EB Garamond", font_size=30,
                  color=INK).move_to(table.get_center())
        eye = Circle(radius=0.6, stroke_color=ACCENT, stroke_width=4,
                     fill_opacity=0).move_to(DOWN * 1.8)
        et = T("gaps close by building, in the open", font="EB Garamond", font_size=24,
                  color=ACCENT).move_to(DOWN * 2.7)
        cap = T("the honest column stays public", font="EB Garamond", font_size=32,
                   color=INK).to_edge(UP, buff=0.7)
        self.play(FadeIn(cap))
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
            T("1 · name the gap: three findings + a second column",
                 font="EB Garamond", font_size=26, color=INK),
            T("2 · the five rows: ask / have / build — one free",
                 font="EB Garamond", font_size=26, color=INK),
            T("3 · the build list: four things; Madison closes the big one",
                 font="EB Garamond", font_size=26, color=INK),
            T("4 · the honest column: the table stays public",
                 font="EB Garamond", font_size=26, color=INK),
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
            T("Your turn", font="EB Garamond", font_size=34, color=ACCENT),
            T("Draw the three columns.", font="EB Garamond", font_size=24, color=INK),
            T("Fill every row from real postings.", font="EB Garamond", font_size=24,
                 color=INK),
            T("Find the free row.", font="EB Garamond", font_size=24, color=INK),
        ).arrange(DOWN, buff=0.25).move_to(ORIGIN)
        self.play(FadeIn(doplate))
        for d in do:
            self.play(FadeIn(d, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)
        self.play(FadeOut(do), FadeOut(doplate))
        out = title_card("Muse, in for Bear", "@NikBearBrown")
        self.play(FadeIn(out))
        self.wait(1.5)