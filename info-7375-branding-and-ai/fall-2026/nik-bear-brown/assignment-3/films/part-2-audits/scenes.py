"""scenes.py — Muse audits itself (Assignment 3, Part 2 film).

12 Manim scenes, M01–M12. House conventions: 16:9, safe-area coords
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
        kept = RoundedRectangle(corner_radius=0.2, width=4.6, height=3.4,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=GREEN, stroke_width=3).move_to(
            [-3.0, 0, 0])
        kt = VGroup(Text("kept", font_size=28, color=GREEN),
                    Text("measured", font_size=20, color=GREY)
                    ).arrange(DOWN, buff=0.15).move_to(kept.get_center())
        rej = RoundedRectangle(corner_radius=0.2, width=4.6, height=3.4,
                               fill_color="#2A2A2A", fill_opacity=1,
                               stroke_color=GREY).move_to([3.0, 0, 0])
        rt = VGroup(Text("rejected", font_size=28, color=GREY),
                    Text("unmeasured", font_size=20, color=GREY)
                    ).arrange(DOWN, buff=0.15).move_to(rej.get_center())
        eye = Circle(radius=0.5, stroke_color=ACCENT, stroke_width=4,
                     fill_opacity=0).move_to([3.0, 0, 0])
        cap = Text("what the filter threw away", font_size=34,
                   color=INK).to_edge(UP, buff=0.7)
        self.play(FadeIn(kept), FadeIn(kt))
        self.play(FadeIn(rej), FadeIn(rt))
        self.play(Create(eye))
        self.play(Write(cap))
        self.wait(1.2)


class M02_Bdefs(Scene):
    def construct(self):
        words = ["family", "false positive", "false negative", "judge"]
        defs = ["titles grouped by job", "kept, family says reject",
                "rejected, family says keep", "only a person can split"]
        cards = VGroup()
        for i, (w, d) in enumerate(zip(words, defs)):
            x = -5.4 + i * 3.6
            box = RoundedRectangle(corner_radius=0.2, width=3.2, height=2.4,
                                   fill_color=CARD, fill_opacity=1,
                                   stroke_color=INK).move_to([x, 0, 0])
            t = Text(w, font_size=24, color=ACCENT).move_to([x, 0.55, 0])
            s = Text(d, font_size=15, color=INK).move_to([x, -0.35, 0])
            cards.add(VGroup(box, t, s))
        for c in cards:
            self.play(FadeIn(c, shift=UP * 0.3), run_time=0.7)
        self.wait(1.2)


class M03_B01Families(Scene):
    def construct(self):
        big = Text("3,446", font_size=56, color=INK).move_to(UP * 1.6)
        fams = VGroup(*[RoundedRectangle(corner_radius=0.1, width=1.1,
                                         height=0.8, fill_color=BLUE,
                                         fill_opacity=0.7, stroke_width=0)
                        for _ in range(21)]).arrange_in_grid(
            rows=3, cols=7, buff=0.25).move_to(UP * 0.1)
        rules = Text("20 family rules", font_size=30, color=BLUE).move_to(
            DOWN * 1.3)
        dis = Text("read only the disagreements", font_size=24,
                   color=ACCENT).move_to(DOWN * 2.2)
        arrow1 = Arrow([0, 1.0, 0], [0, 0.75, 0], color=INK, buff=0.08,
                       stroke_width=6)
        arrow2 = Arrow([0, -0.45, 0], [0, -0.85, 0], color=INK, buff=0.08,
                       stroke_width=6)
        cap = Text("don't read 3,446 postings", font_size=32,
                   color=INK).to_edge(UP, buff=0.7)
        self.play(Write(cap))
        self.play(FadeIn(big, scale=1.2))
        self.play(GrowArrow(arrow1), run_time=0.4)
        self.play(*[FadeIn(f, scale=0.6) for f in fams], run_time=1.0)
        self.play(GrowArrow(arrow2), run_time=0.4)
        self.play(FadeIn(rules, shift=UP * 0.2))
        self.play(FadeIn(dis, shift=UP * 0.2))
        self.wait(1.2)


class M04_B02FalsePositives(Scene):
    def construct(self):
        rows = VGroup()
        data = [("TECH_ENABLEMENT", "7 kept", "engineering jobs", ACCENT),
                ("RECRUITING", "2 kept", "campus recruiting", ACCENT),
                ("MARKETING", "3 kept", "wrong family", BLUE),
                ("ENGINEERING", "4 kept", "wrong family", BLUE)]
        for i, (fam, n, why, col) in enumerate(data):
            y = 1.7 - i * 1.15
            bg = RoundedRectangle(corner_radius=0.15, width=10.4, height=0.95,
                                  fill_color=CARD, fill_opacity=1,
                                  stroke_color=col, stroke_width=3).move_to(
                [0, y, 0])
            dot = Circle(radius=0.14, fill_color=col, fill_opacity=1,
                         stroke_width=0).move_to([-4.5, y, 0])
            tf = Text(fam, font_size=24, color=INK).move_to([-2.9, y + 0.14, 0])
            tn = Text(f"{n} — {why}", font_size=19, color=GREY).move_to(
                [-2.85, y - 0.28, 0])
            rows.add(VGroup(bg, dot, tf, tn))
        total = Text("23 false positives", font_size=30, color=ACCENT).to_edge(
            DOWN, buff=0.8)
        cap = Text("kept, but the family says reject", font_size=32,
                   color=INK).to_edge(UP, buff=0.7)
        self.play(Write(cap))
        for r in rows:
            self.play(FadeIn(r[0]))
            self.play(FadeIn(r[1]), FadeIn(r[2], shift=RIGHT * 0.2),
                      FadeIn(r[3], shift=RIGHT * 0.2), run_time=0.5)
        self.play(FadeIn(total, shift=UP * 0.2))
        self.wait(1.2)


class M05_B03TrainingSplit(Scene):
    def construct(self):
        word = Text("“training”", font_size=54, color=INK).move_to(UP * 1.6)
        left = RoundedRectangle(corner_radius=0.2, width=4.8, height=2.4,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=GREEN, stroke_width=3).move_to(
            [-3.0, -0.6, 0])
        right = RoundedRectangle(corner_radius=0.2, width=4.8, height=2.4,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=ACCENT, stroke_width=3).move_to(
            [3.0, -0.6, 0])
        lt = VGroup(Text("teaching", font_size=26, color=GREEN),
                    Text("a person", font_size=18, color=GREY)
                    ).arrange(DOWN, buff=0.1).move_to(left.get_center())
        rt = VGroup(Text("ML training", font_size=26, color=ACCENT),
                    Text("a model", font_size=18, color=GREY)
                    ).arrange(DOWN, buff=0.1).move_to(right.get_center())
        split = Line([0, 0.6, 0], [0, -1.8, 0], color=INK, stroke_width=4)
        cap = Text("at an AI company, training means training a model",
                   font_size=28, color=INK).to_edge(UP, buff=0.7)
        note = Text("27 'education' jobs — all ML roles", font_size=22,
                    color=GREY).to_edge(DOWN, buff=0.8)
        self.play(Write(cap))
        self.play(FadeIn(word, scale=1.1))
        self.play(Create(split), run_time=0.5)
        self.play(FadeIn(left), FadeIn(lt), run_time=0.5)
        self.play(FadeIn(right), FadeIn(rt), run_time=0.5)
        self.play(FadeIn(note, shift=UP * 0.2))
        self.wait(1.2)


class M06_B04AuditWrong(Scene):
    def construct(self):
        audit = RoundedRectangle(corner_radius=0.2, width=5.2, height=2.8,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=ACCENT, stroke_width=4).move_to(
            [-3.0, 0, 0])
        filt = RoundedRectangle(corner_radius=0.2, width=5.2, height=2.8,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=GREEN, stroke_width=4).move_to(
            [3.0, 0, 0])
        aw = Text("WRONG", font_size=40, color=ACCENT).move_to(
            audit.get_center() + UP * 0.3)
        al = Text("the audit", font_size=20, color=GREY).move_to(
            audit.get_center() + DOWN * 0.6)
        fw = Text("RIGHT", font_size=40, color=GREEN).move_to(
            filt.get_center() + UP * 0.3)
        fl = Text("the filter", font_size=20, color=GREY).move_to(
            filt.get_center() + DOWN * 0.6)
        rule = Text("ML_TRAINING is now family rule #1", font_size=24,
                    color=INK).to_edge(DOWN, buff=0.8)
        cap = Text("the audit caught itself", font_size=34, color=INK).to_edge(
            UP, buff=0.7)
        self.play(Write(cap))
        self.play(FadeIn(audit, scale=0.9))
        self.play(Write(aw), FadeIn(al))
        self.play(FadeIn(filt, scale=0.9))
        self.play(Write(fw), FadeIn(fl))
        self.play(FadeIn(rule, shift=UP * 0.2))
        self.wait(1.2)


class M07_B05TwoSamples(Scene):
    def construct(self):
        dice = RoundedRectangle(corner_radius=0.2, width=4.8, height=3.2,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=BLUE, stroke_width=3).move_to(
            [-3.0, 0, 0])
        pips = VGroup(*[Circle(radius=0.16, fill_color=BLUE, fill_opacity=1,
                               stroke_width=0).move_to(
            [-3.9 + (i % 3) * 0.9, 0.6 - (i // 3) * 0.9, 0])
            for i in range(6)])
        dt = Text("100 random", font_size=26, color=BLUE).move_to([-3.0, -1.1, 0])
        ds = Text("seed 20260926", font_size=18, color=GREY).move_to([-3.0, -1.55, 0])
        close = RoundedRectangle(corner_radius=0.2, width=4.8, height=3.2,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=ACCENT, stroke_width=3).move_to(
            [3.0, 0, 0])
        bars = VGroup(*[Rectangle(width=0.5, height=0.6 + i * 0.35,
                                  fill_color=ACCENT, fill_opacity=0.7,
                                  stroke_width=0).move_to(
            [1.7 + i * 0.7, -0.2 + (0.6 + i * 0.35) / 2 - 0.3, 0])
            for i in range(4)])
        ct = Text("63 closest calls", font_size=26, color=ACCENT).move_to(
            [3.0, -1.1, 0])
        cs = Text("two words, bar was three", font_size=18,
                  color=GREY).move_to([3.0, -1.55, 0])
        note = Text("part one gives the rate; part two is where a miss hides",
                     font_size=22, color=GREY).to_edge(DOWN, buff=0.8)
        cap = Text("two samples", font_size=34, color=INK).to_edge(UP,
                                                                   buff=0.7)
        self.play(Write(cap))
        self.play(FadeIn(dice))
        self.play(*[FadeIn(p, scale=1.5) for p in pips], run_time=0.8)
        self.play(FadeIn(dt), FadeIn(ds))
        self.play(FadeIn(close))
        self.play(*[GrowFromEdge(b, DOWN) for b in bars], run_time=0.7)
        self.play(FadeIn(ct), FadeIn(cs))
        self.play(FadeIn(note, shift=UP * 0.2))
        self.wait(1.2)


class M08_B06Boilerplate(Scene):
    def construct(self):
        big = Text("618 / 618", font_size=64, color=ACCENT).move_to(UP * 1.2)
        footer = RoundedRectangle(corner_radius=0.15, width=9.6, height=1.4,
                                  fill_color="#EDE8DA", fill_opacity=1,
                                  stroke_width=0).move_to(DOWN * 0.2)
        ft = Text("“Minimum education: Bachelor's degree…”", font_size=24,
                  color=GREY).move_to(footer.get_center())
        hl = Rectangle(width=9.6, height=1.4, stroke_color=ACCENT,
                       stroke_width=4).move_to(DOWN * 0.2)
        verdict = Text("boilerplate — carries no information", font_size=26,
                       color=ACCENT).move_to(DOWN * 1.6)
        cap = Text("the word 'education' at Anthropic", font_size=32,
                   color=INK).to_edge(UP, buff=0.7)
        self.play(Write(cap))
        self.play(FadeIn(big, scale=1.3))
        self.play(FadeIn(footer), FadeIn(ft))
        self.play(Create(hl), run_time=0.6)
        self.play(FadeIn(verdict, shift=UP * 0.2))
        self.wait(1.2)


class M09_B07Recruiters(Scene):
    def construct(self):
        roles = ["Stripe — University Recruiter ×3",
                 "Notion — Head of Early Career Recruiting",
                 "OpenAI — Youth Culture Marketing"]
        cards = VGroup()
        for i, r in enumerate(roles):
            y = 1.6 - i * 1.4
            bg = RoundedRectangle(corner_radius=0.15, width=9.6, height=1.1,
                                  fill_color=CARD, fill_opacity=1,
                                  stroke_color=ACCENT, stroke_width=3).move_to(
                [0, y, 0])
            pin = Circle(radius=0.22, fill_color=ACCENT, fill_opacity=1,
                         stroke_width=0).move_to([-4.2, y, 0])
            t = Text(r, font_size=24, color=INK).move_to([-0.8, y, 0])
            cards.add(VGroup(bg, pin, t))
        verdict = Text("recruiters, not teachers", font_size=30,
                       color=ACCENT).to_edge(DOWN, buff=0.8)
        words = Text("university · campus · student", font_size=24,
                     color=GREY).move_to(UP * 2.6)
        cap = Text("the topic words kept", font_size=32, color=INK).to_edge(
            UP, buff=0.7)
        self.play(Write(cap))
        self.play(FadeIn(words, shift=DOWN * 0.2))
        for c in cards:
            self.play(FadeIn(c[0]))
            self.play(FadeIn(c[1], scale=1.4))
            self.play(FadeIn(c[2], shift=RIGHT * 0.2), run_time=0.45)
        self.play(FadeIn(verdict, shift=UP * 0.2))
        self.wait(1.2)


class M10_B08Reversal(Scene):
    def construct(self):
        before = Text("13 errors", font_size=40, color=GREY).move_to(
            LEFT * 3 + UP * 0.4)
        after = Text("13 kept", font_size=40, color=GREEN).move_to(
            RIGHT * 3 + UP * 0.4)
        arrow = Arrow([-1.2, 0.4, 0], [1.2, 0.4, 0], color=INK,
                      stroke_width=8, buff=0.15)
        strike = Line([-4.5, 0.4, 0], [-1.5, 0.4, 0], color=ACCENT,
                      stroke_width=6)
        quote = Text("“train their own people would be a great fit”",
                     font_size=24, color=INK).move_to(DOWN * 1.2)
        attr = Text("— Bear's ruling", font_size=20, color=GREY).move_to(
            DOWN * 1.9)
        cap = Text("the reversal", font_size=34, color=INK).to_edge(UP,
                                                                     buff=0.7)
        self.play(Write(cap))
        self.play(FadeIn(before, shift=RIGHT * 0.3))
        self.play(Create(strike), run_time=0.4)
        self.play(GrowArrow(arrow), run_time=0.5)
        self.play(FadeIn(after, scale=1.2))
        self.play(FadeIn(quote, shift=UP * 0.2))
        self.play(FadeIn(attr, shift=UP * 0.15))
        self.wait(1.2)


class M11_B09Lesson(Scene):
    def construct(self):
        card = RoundedRectangle(corner_radius=0.25, width=10.6, height=3.6,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=INK).move_to(ORIGIN)
        t = Text("an audit that can't find its own mistakes", font_size=30,
                 color=INK).move_to(UP * 0.5)
        t2 = Text("is theater", font_size=36, color=ACCENT).move_to(
            DOWN * 0.4)
        mirror = Circle(radius=0.5, stroke_color=INK, stroke_width=4,
                        fill_opacity=0).move_to(RIGHT * 4.2 + UP * 0.5)
        cap = Text("the lesson", font_size=34, color=INK).to_edge(UP,
                                                                  buff=0.7)
        self.play(Write(cap))
        self.play(FadeIn(card, scale=0.94))
        self.play(FadeIn(mirror, scale=1.3))
        self.play(Write(t))
        self.play(Write(t2))
        self.wait(1.5)


class M12_BvdtHtfOut(Scene):
    def construct(self):
        plate = RoundedRectangle(corner_radius=0.25, width=11.8, height=4.8,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK)
        recap = VGroup(*[
            Text("1 · the title audit: 20 rules, 23 false positives",
                 font_size=26, color=INK),
            Text("2 · the audit's bug: training = ML, filter was right",
                 font_size=26, color=INK),
            Text("3 · the reject audit: 618/618 boilerplate; recruiters",
                 font_size=26, color=INK),
            Text("4 · the reversal: 13 kept by ruling", font_size=26,
                 color=INK),
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
            Text("Read 100 rejects and the closest calls.", font_size=24,
                 color=INK),
            Text("Then ask which of your audit's", font_size=24, color=INK),
            Text("rules is wrong.", font_size=24, color=INK),
        ).arrange(DOWN, buff=0.25).move_to(ORIGIN)
        self.play(FadeIn(doplate))
        for d in do:
            self.play(FadeIn(d, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)
        self.play(FadeOut(do), FadeOut(doplate))
        out = title_card("Muse, in for Bear", "@NikBearBrown")
        self.play(FadeIn(out))
        self.wait(1.5)
