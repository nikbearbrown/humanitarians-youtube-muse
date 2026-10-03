"""scenes.py — Muse finds the dream job (Assignment 2, Part 1 film).

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
        student = Circle(radius=0.55, fill_color=ACCENT, fill_opacity=1,
                         stroke_width=0).shift(LEFT * 3 + DOWN * 0.5)
        shiny = RoundedRectangle(corner_radius=0.2, width=4.2, height=2.6,
                                 fill_color="#FFE9A8", fill_opacity=1,
                                 stroke_color=INK).shift(RIGHT * 2.5 + UP * 0.5)
        st = Text("shiniest posting", font_size=24, color=INK).move_to(
            shiny.get_center())
        flag = Polygon([0, 0, 0], [0, 1.6, 0], [1.1, 1.25, 0],
                       fill_color=ACCENT, fill_opacity=1,
                       stroke_width=0).move_to(RIGHT * 5.2 + UP * 1.2)
        cap = Text("don't pick the one that flatters you", font_size=34,
                   color=INK).to_edge(UP, buff=0.7)
        self.play(FadeIn(student))
        self.play(FadeIn(shiny), FadeIn(st))
        self.play(FadeIn(flag, scale=1.4))
        self.play(Write(cap))
        self.wait(1.2)


class M02_Bdefs(Scene):
    def construct(self):
        words = ["scheme", "flag", "rank", "override"]
        defs = ["written matching rules", "a posting the rules mark",
                "the machine's ordering", "the human overruling it"]
        cards = VGroup()
        for i, (w, d) in enumerate(zip(words, defs)):
            x = -5.4 + i * 3.6
            box = RoundedRectangle(corner_radius=0.2, width=3.2, height=2.4,
                                   fill_color=CARD, fill_opacity=1,
                                   stroke_color=INK).move_to([x, 0, 0])
            t = Text(w, font_size=28, color=ACCENT).move_to([x, 0.55, 0])
            s = Text(d, font_size=16, color=INK).move_to([x, -0.35, 0])
            cards.add(VGroup(box, t, s))
        for c in cards:
            self.play(FadeIn(c, shift=UP * 0.3), run_time=0.7)
        self.wait(1.2)


class M03_B01Method(Scene):
    def construct(self):
        skill = RoundedRectangle(corner_radius=0.2, width=4.6, height=2.6,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=BLUE, stroke_width=3).move_to(
            [-2.9, 0.4, 0])
        scheme = RoundedRectangle(corner_radius=0.2, width=4.6, height=2.6,
                                  fill_color=CARD, fill_opacity=1,
                                  stroke_color=ACCENT, stroke_width=3).move_to(
            [2.9, 0.4, 0])
        st = VGroup(Text("greenhouse-watch", font_size=26, color=BLUE),
                    Text("the skill", font_size=18, color=GREY)
                    ).arrange(DOWN, buff=0.15).move_to(skill.get_center())
        ct = VGroup(Text("bear-figma-0.1", font_size=26, color=ACCENT),
                    Text("the scheme", font_size=18, color=GREY)
                    ).arrange(DOWN, buff=0.15).move_to(scheme.get_center())
        link = DoubleArrow([-0.5, 0.4, 0], [0.5, 0.4, 0], color=INK,
                           buff=0.1, stroke_width=6)
        cap = Text("the method: skill + scheme", font_size=32,
                   color=INK).to_edge(UP, buff=0.7)
        note = Text("no scrolling the careers page", font_size=22,
                    color=GREY).to_edge(DOWN, buff=0.8)
        self.play(Write(cap))
        self.play(FadeIn(skill), FadeIn(st), run_time=0.6)
        self.play(FadeIn(scheme), FadeIn(ct), run_time=0.6)
        self.play(GrowArrow(link))
        self.play(FadeIn(note))
        self.wait(1.2)


class M04_B02Funnel(Scene):
    def construct(self):
        top = Circle(radius=1.9, fill_color=CARD, fill_opacity=1,
                     stroke_color=INK).move_to([-3.4, 0, 0])
        tt = VGroup(Text("152", font_size=44, color=INK),
                    Text("postings", font_size=20, color=GREY)
                    ).arrange(DOWN, buff=0.1).move_to(top.get_center())
        keep = Circle(radius=1.3, fill_color=GREEN, fill_opacity=0.2,
                      stroke_color=GREEN, stroke_width=4).move_to([1.8, 0.8, 0])
        kt = VGroup(Text("49", font_size=36, color=GREEN),
                    Text("flagged", font_size=18, color=INK)
                    ).arrange(DOWN, buff=0.1).move_to(keep.get_center())
        skip = Circle(radius=1.0, fill_color=GREY, fill_opacity=0.15,
                      stroke_color=GREY, stroke_width=3).move_to([1.8, -1.6, 0])
        st = VGroup(Text("103", font_size=30, color=GREY),
                    Text("skipped", font_size=18, color=GREY)
                    ).arrange(DOWN, buff=0.1).move_to(skip.get_center())
        arrow = Arrow([-1.3, 0, 0], [0.3, 0.6, 0], color=INK, buff=0.15,
                      stroke_width=6)
        note = Text("string-match rules — no model judgment", font_size=22,
                    color=GREY).to_edge(DOWN, buff=0.8)
        self.play(FadeIn(top), FadeIn(tt))
        self.play(GrowArrow(arrow))
        self.play(FadeIn(keep), FadeIn(kt), run_time=0.6)
        self.play(FadeIn(skip), FadeIn(st), run_time=0.6)
        self.play(FadeIn(note))
        self.wait(1.2)


class M05_B03TopScores(Scene):
    def construct(self):
        roles = ["AI Applied Scientist — 11.5",
                 "Forward Deployed Engineer — 11.5",
                 "Marketing Engineer — 11.5"]
        rows = VGroup()
        for i, r in enumerate(roles):
            y = 1.5 - i * 1.3
            bg = RoundedRectangle(corner_radius=0.15, width=9.6, height=1.0,
                                  fill_color=CARD, fill_opacity=1,
                                  stroke_color=INK).move_to([0, y, 0])
            t = Text(r, font_size=24, color=INK).move_to([-2.2, y, 0])
            x1 = Line([-0.2, y + 0.35, 0], [4.6, y - 0.35, 0], color=ACCENT,
                      stroke_width=8)
            rows.add(VGroup(bg, t, x1))
        cap = Text("the top scores were wrong for the goal", font_size=30,
                   color=INK).to_edge(UP, buff=0.7)
        note = Text("matched the skills, not the goal", font_size=22,
                    color=GREY).to_edge(DOWN, buff=0.8)
        self.play(Write(cap))
        for r in rows:
            self.play(FadeIn(r[0]), FadeIn(r[1], shift=RIGHT * 0.2),
                      run_time=0.5)
            self.play(Create(r[2]), run_time=0.4)
        self.play(FadeIn(note))
        self.wait(1.2)


class M06_B04Override(Scene):
    def construct(self):
        lst = RoundedRectangle(corner_radius=0.2, width=6.4, height=3.6,
                               fill_color=CARD, fill_opacity=1,
                               stroke_color=INK).move_to([-2.2, 0, 0])
        hand = Circle(radius=0.7, fill_color=ACCENT, fill_opacity=1,
                      stroke_width=0).move_to([2.8, 0.6, 0])
        pick = RoundedRectangle(corner_radius=0.15, width=4.4, height=1.4,
                                fill_color="#EDE8DA", fill_opacity=1,
                                stroke_color=GREEN, stroke_width=3).move_to(
            [2.8, -1.6, 0])
        pt = Text("Designer Advocate", font_size=24, color=GREEN).move_to(
            pick.get_center())
        arrow = Arrow([0.8, 0.6, 0], [1.9, 0.6, 0], color=INK, buff=0.1,
                      stroke_width=6)
        cap = Text("the human overruled the ranking", font_size=32,
                   color=INK).to_edge(UP, buff=0.7)
        note = Text("the ranking filtered the reading list — nothing more",
                     font_size=22, color=GREY).to_edge(DOWN, buff=0.8)
        self.play(Write(cap))
        self.play(FadeIn(lst))
        self.play(FadeIn(hand, scale=1.3))
        self.play(GrowArrow(arrow))
        self.play(FadeIn(pick), FadeIn(pt))
        self.play(FadeIn(note))
        self.wait(1.2)


class M07_B05Gap(Scene):
    def construct(self):
        card = RoundedRectangle(corner_radius=0.2, width=9.6, height=3.4,
                                fill_color="#EDE8DA", fill_opacity=1,
                                stroke_color=ACCENT, stroke_width=3).move_to(
            ORIGIN)
        t = Text("never shipped a design system in Figma", font_size=32,
                 color=INK).move_to(UP * 0.6)
        s = Text("the Madison project closes it — stated, not hidden",
                 font_size=24, color=GREY).move_to(DOWN * 0.4)
        plus = Text("+ public speaking · up to 25% travel", font_size=22,
                    color=GREY).move_to(DOWN * 1.2)
        badge = Circle(radius=0.4, fill_color=ACCENT, fill_opacity=1,
                       stroke_width=0).move_to([-4.0, 0.6, 0])
        bt = Text("!", font_size=36, color=CARD).move_to(badge.get_center())
        bar = Rectangle(width=0.3, height=3.4, fill_color=ACCENT,
                        fill_opacity=1, stroke_width=0).move_to([-4.6, 0, 0])
        cap = Text("the honesty, part one: the gap", font_size=32,
                   color=INK).to_edge(UP, buff=0.7)
        self.play(Write(cap))
        self.play(FadeIn(card))
        self.play(GrowFromEdge(bar, UP), run_time=0.4)
        self.play(FadeIn(badge, scale=1.4), FadeIn(bt))
        self.play(Write(t))
        self.play(FadeIn(s, shift=UP * 0.2))
        self.play(FadeIn(plus, shift=UP * 0.2))
        self.wait(1.2)


class M08_B06Disappointment(Scene):
    def construct(self):
        shelf = Rectangle(width=9.6, height=0.25, fill_color=INK,
                          fill_opacity=1, stroke_width=0).move_to(DOWN * 0.6)
        zero = Text("0", font_size=72, color=GREY).move_to(UP * 0.8)
        zl = Text("part-time / contract / freelance / consulting roles",
                  font_size=24, color=INK).move_to(DOWN * 0.05)
        missing = VGroup()
        for w in ["no “Education”", "no “Learning”", "no “Curriculum”",
                  "no “Content”"]:
            sq = Square(side_length=0.16, fill_color=GREY, fill_opacity=1,
                        stroke_width=0)
            t = Text(w, font_size=22, color=GREY)
            missing.add(VGroup(sq, t).arrange(RIGHT, buff=0.2,
                                              aligned_edge=ORIGIN))
        missing.arrange(RIGHT, buff=0.5).move_to(DOWN * 2.2)
        cap = Text("the honesty, part two: the disappointment", font_size=32,
                   color=INK).to_edge(UP, buff=0.7)
        self.play(Write(cap))
        self.play(FadeIn(shelf))
        self.play(FadeIn(zero, scale=1.3))
        self.play(FadeIn(zl, shift=UP * 0.2))
        for m in missing:
            self.play(FadeIn(m[0]), FadeIn(m[1], shift=UP * 0.15),
                      run_time=0.4)
        self.wait(1.2)


class M09_B07Answer(Scene):
    def construct(self):
        card = RoundedRectangle(corner_radius=0.25, width=9.6, height=4.4,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=GREEN, stroke_width=4).move_to(
            ORIGIN)
        t = Text("Designer Advocate, Figma", font_size=36, color=INK).move_to(
            UP * 1.1)
        pay = Text("$153K – $317K · full-time · US hubs", font_size=26,
                   color=GREEN).move_to(UP * 0.2)
        job = Text("making teaching material for the design community",
                   font_size=24, color=INK).move_to(DOWN * 0.7)
        d = Text("posted 2026-09-01", font_size=20, color=GREY).move_to(
            DOWN * 1.5)
        star = Circle(radius=0.42, fill_color=GREEN, fill_opacity=1,
                      stroke_width=0).move_to([-3.9, 1.1, 0])
        coin = Circle(radius=0.3, fill_color=GREEN, fill_opacity=0.35,
                      stroke_color=GREEN, stroke_width=4).move_to([-3.9, 0.2, 0])
        cap = Text("the answer", font_size=34, color=INK).to_edge(UP,
                                                                  buff=0.7)
        self.play(Write(cap))
        self.play(FadeIn(card, scale=0.92))
        self.play(FadeIn(star, scale=1.5), Write(t), run_time=0.8)
        self.play(FadeIn(coin, scale=1.3), FadeIn(pay, shift=UP * 0.2),
                  run_time=0.6)
        self.play(FadeIn(job, shift=UP * 0.2))
        self.play(FadeIn(d))
        self.wait(1.2)


class M10_B08RunnerUp(Scene):
    def construct(self):
        card = RoundedRectangle(corner_radius=0.2, width=9.6, height=3.6,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=BLUE, stroke_width=3).move_to(
            ORIGIN)
        t = Text("Researcher, Figma Agentic Experiences", font_size=30,
                 color=INK).move_to(UP * 0.7)
        s = Text("the one remote-OK role", font_size=24, color=BLUE).move_to(
            DOWN * 0.1)
        w = Text("wants 7+ years UX research — not on the résumé",
                 font_size=22, color=GREY).move_to(DOWN * 0.9)
        pin = Circle(radius=0.35, fill_color=BLUE, fill_opacity=1,
                     stroke_width=0).move_to([-4.0, 0.7, 0])
        flag2 = Polygon([0, 0, 0], [0, 0.9, 0], [0.65, 0.7, 0],
                        fill_color=BLUE, fill_opacity=1,
                        stroke_width=0).move_to([4.0, -0.9, 0])
        cap = Text("the runner-up, kept honestly", font_size=32,
                   color=INK).to_edge(UP, buff=0.7)
        self.play(Write(cap))
        self.play(FadeIn(card))
        self.play(FadeIn(pin, scale=1.4), FadeIn(t, shift=DOWN * 0.2),
                  run_time=0.7)
        self.play(FadeIn(s, shift=UP * 0.2))
        self.play(FadeIn(flag2, scale=1.3), FadeIn(w, shift=UP * 0.2),
                  run_time=0.6)
        self.wait(1.2)


class M11_BvdtHtfOut(Scene):
    def construct(self):
        plate = RoundedRectangle(corner_radius=0.25, width=11.8, height=4.8,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK)
        recap = VGroup(*[
            Text("1 · the method: one fetch, a written scheme, 49 flagged",
                 font_size=26, color=INK),
            Text("2 · the override: top scores wrong, human chose",
                 font_size=26, color=INK),
            Text("3 · the honesty: a real gap, a real disappointment",
                 font_size=26, color=INK),
            Text("4 · the answer: Designer Advocate, runner-up kept",
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
            Text("Write your matching scheme before you look.", font_size=24,
                 color=INK),
            Text("When the top score isn't your goal,", font_size=24,
                 color=INK),
            Text("overrule it — in writing.", font_size=24, color=INK),
        ).arrange(DOWN, buff=0.25).move_to(ORIGIN)
        self.play(FadeIn(doplate))
        for d in do:
            self.play(FadeIn(d, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)
        self.play(FadeOut(do), FadeOut(doplate))
        out = title_card("Muse, in for Bear", "@NikBearBrown")
        self.play(FadeIn(out))
        self.wait(1.5)
