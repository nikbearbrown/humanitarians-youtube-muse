"""scenes.py — Muse builds the pipeline (Assignment 3, Part 1 film).

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
        env = RoundedRectangle(corner_radius=0.2, width=5.6, height=3.8,
                               fill_color=CARD, fill_opacity=1,
                               stroke_color=ACCENT, stroke_width=4).move_to(
            [-2.5, 0, 0])
        seal = Circle(radius=0.5, fill_color=ACCENT, fill_opacity=1,
                      stroke_width=0).move_to([-2.5, 0.4, 0])
        et = Text("predictions", font_size=26, color=INK).move_to([-2.5, -1.0, 0])
        pipe = VGroup(*[RoundedRectangle(corner_radius=0.15, width=1.6,
                                         height=1.2, fill_color="#EDE8DA",
                                         fill_opacity=1, stroke_width=0)
                        for _ in range(3)]).arrange(RIGHT, buff=0.3).move_to(
            [3.4, 0, 0])
        cap = Text("sealed before a single posting is fetched", font_size=32,
                   color=INK).to_edge(UP, buff=0.7)
        self.play(FadeIn(env))
        self.play(FadeIn(seal, scale=1.5))
        self.play(FadeIn(et, shift=UP * 0.2))
        self.play(*[FadeIn(p, shift=LEFT * 0.3) for p in pipe],
                  run_time=0.9)
        self.play(Write(cap))
        self.wait(1.2)


class M02_Bdefs(Scene):
    def construct(self):
        words = ["prediction", "filter", "kept", "re-derivable"]
        defs = ["expected, written first", "rules that keep or reject",
                "records worth your time", "reproduced byte-identical"]
        cards = VGroup()
        for i, (w, d) in enumerate(zip(words, defs)):
            x = -5.4 + i * 3.6
            box = RoundedRectangle(corner_radius=0.2, width=3.2, height=2.4,
                                   fill_color=CARD, fill_opacity=1,
                                   stroke_color=INK).move_to([x, 0, 0])
            t = Text(w, font_size=26, color=ACCENT).move_to([x, 0.55, 0])
            s = Text(d, font_size=15, color=INK).move_to([x, -0.35, 0])
            cards.add(VGroup(box, t, s))
        for c in cards:
            self.play(FadeIn(c, shift=UP * 0.3), run_time=0.7)
        self.wait(1.2)


class M03_B01Predictions(Scene):
    def construct(self):
        preds = ["record count is the problem, not plumbing",
                 "culture blurbs: > 1/4 false positives",
                 "false negatives: title-only matches",
                 "SmartRecruiters: slowest, most fragile"]
        cards = VGroup()
        for i, p in enumerate(preds):
            y = 1.8 - i * 1.25
            box = RoundedRectangle(corner_radius=0.15, width=10.4, height=1.0,
                                   fill_color=CARD, fill_opacity=1,
                                   stroke_color=BLUE, stroke_width=2).move_to(
                [0, y, 0])
            dot = Circle(radius=0.14, fill_color=BLUE, fill_opacity=1,
                         stroke_width=0).move_to([-4.6, y, 0])
            t = Text(p, font_size=22, color=INK).move_to([-0.6, y, 0])
            cards.add(VGroup(box, dot, t))
        date = Text("written 2026-09-26 — before anything ran", font_size=24,
                    color=ACCENT).to_edge(DOWN, buff=0.8)
        cap = Text("four predictions, sealed first", font_size=32,
                   color=INK).to_edge(UP, buff=0.7)
        self.play(Write(cap))
        for c in cards:
            self.play(FadeIn(c[0]))
            self.play(FadeIn(c[1]), FadeIn(c[2], shift=RIGHT * 0.2),
                      run_time=0.5)
        self.play(FadeIn(date, shift=UP * 0.2))
        self.wait(1.2)


class M04_B02FailureCondition(Scene):
    def construct(self):
        doc = RoundedRectangle(corner_radius=0.2, width=10.4, height=3.2,
                               fill_color=CARD, fill_opacity=1,
                               stroke_color=INK).move_to(UP * 0.4)
        t = Text("loosening the filter to hit a record count", font_size=28,
                 color=INK).move_to(UP * 1.0)
        t2 = Text("is the specific dishonesty this prediction exists to catch",
                  font_size=24, color=ACCENT).move_to(UP * 0.2)
        stamp = Text("FAILURE CONDITION", font_size=30, color=ACCENT).move_to(
            DOWN * 1.6)
        frame = Rectangle(width=5.4, height=1.0, stroke_color=ACCENT,
                          stroke_width=4).move_to(DOWN * 1.6)
        cap = Text("fixed in writing", font_size=34, color=INK).to_edge(
            UP, buff=0.7)
        self.play(Write(cap))
        self.play(FadeIn(doc))
        self.play(FadeIn(t, shift=DOWN * 0.2))
        self.play(FadeIn(t2, shift=DOWN * 0.2))
        self.play(FadeIn(frame), Write(stamp))
        self.wait(1.2)


class M05_B03ThreeSteps(Scene):
    def construct(self):
        labels = ["download", "filter", "write"]
        subs = ["raw saved, dated", "role + topic words", "json + csv"]
        boxes = VGroup()
        for i, (lab, sub) in enumerate(zip(labels, subs)):
            x = -4.4 + i * 4.4
            b = RoundedRectangle(corner_radius=0.2, width=4.0, height=2.4,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK).move_to([x, 0.4, 0])
            t = Text(lab, font_size=30, color=BLUE).move_to([x, 0.9, 0])
            s = Text(sub, font_size=18, color=GREY).move_to([x, -0.2, 0])
            boxes.add(VGroup(b, t, s))
        arrows = VGroup(*[Arrow([-2.1 + i * 4.4, 0.4, 0],
                                [-1.5 + i * 4.4, 0.4, 0],
                                color=INK, buff=0.1, stroke_width=6)
                          for i in range(2)])
        cap = Text("three steps, once a day", font_size=32,
                   color=INK).to_edge(UP, buff=0.7)
        self.play(Write(cap))
        for b in boxes:
            self.play(FadeIn(b, shift=RIGHT * 0.3), run_time=0.6)
        self.play(*[GrowArrow(a) for a in arrows], run_time=0.7)
        self.wait(1.2)


class M06_B04ThreeATS(Scene):
    def construct(self):
        atss = [("Greenhouse", BLUE), ("Ashby", GREEN),
                ("SmartRecruiters", ACCENT)]
        tops = VGroup()
        for i, (name, col) in enumerate(atss):
            x = -4.4 + i * 4.4
            b = RoundedRectangle(corner_radius=0.15, width=3.8, height=1.6,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=col, stroke_width=3).move_to(
                [x, 1.2, 0])
            t = Text(name, font_size=24, color=col).move_to([x, 1.2, 0])
            tops.add(VGroup(b, t))
        file = RoundedRectangle(corner_radius=0.2, width=8.0, height=1.6,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=INK).move_to(DOWN * 1.6)
        ft = Text("jobs-of-interest.json", font_size=26, color=INK).move_to(
            file.get_center() + UP * 0.25)
        mk = Text('+ one "matched" key — the script\'s decisions',
                  font_size=20, color=BLUE).move_to(file.get_center() +
                                                    DOWN * 0.4)
        conns = VGroup(*[Line([-4.4 + i * 4.4, 0.4, 0], [-2.5 + i * 1.6, -0.8, 0],
                              color=GREY, stroke_width=3) for i in range(3)])
        cap = Text("three shapes in, one file out", font_size=32,
                   color=INK).to_edge(UP, buff=0.7)
        self.play(Write(cap))
        for t in tops:
            self.play(FadeIn(t, shift=DOWN * 0.25), run_time=0.5)
        self.play(*[Create(c) for c in conns], run_time=0.7)
        self.play(FadeIn(file))
        self.play(FadeIn(ft, shift=UP * 0.15))
        self.play(FadeIn(mk, shift=UP * 0.15))
        self.wait(1.2)


class M07_B05Refusals(Scene):
    def construct(self):
        items = [("no title / link / date", "not written", ACCENT),
                 ("a dead source", "logged; others keep going", BLUE),
                 ("duplicates", "collapse on source + id", GREEN)]
        rows = VGroup()
        for i, (h, s, col) in enumerate(items):
            y = 1.6 - i * 1.5
            bg = RoundedRectangle(corner_radius=0.15, width=10.4, height=1.2,
                                  fill_color=CARD, fill_opacity=1,
                                  stroke_color=col, stroke_width=3).move_to(
                [0, y, 0])
            x = VGroup(
                Line([-4.5, y + 0.2, 0], [-4.1, y - 0.2, 0], color=col,
                     stroke_width=8),
                Line([-4.5, y - 0.2, 0], [-4.1, y + 0.2, 0], color=col,
                     stroke_width=8))
            th = Text(h, font_size=26, color=INK).move_to([-2.6, y + 0.14, 0])
            ts = Text(s, font_size=19, color=GREY).move_to([-2.55, y - 0.28, 0])
            rows.add(VGroup(bg, x, th, ts))
        cap = Text("refusal is a feature", font_size=34, color=INK).to_edge(
            UP, buff=0.7)
        self.play(Write(cap))
        for r in rows:
            self.play(FadeIn(r[0]))
            self.play(Create(r[1]), run_time=0.4)
            self.play(FadeIn(r[2], shift=RIGHT * 0.2),
                      FadeIn(r[3], shift=RIGHT * 0.2), run_time=0.45)
        self.wait(1.2)


class M08_B06Funnel(Scene):
    def construct(self):
        top = Circle(radius=1.9, fill_color=CARD, fill_opacity=1,
                     stroke_color=INK).move_to([-3.4, 0, 0])
        tt = VGroup(Text("3,446", font_size=44, color=INK),
                    Text("postings", font_size=20, color=GREY)
                    ).arrange(DOWN, buff=0.1).move_to(top.get_center())
        keep = Circle(radius=1.2, fill_color=GREEN, fill_opacity=0.2,
                      stroke_color=GREEN, stroke_width=4).move_to([2.2, 0, 0])
        kt = VGroup(Text("97", font_size=40, color=GREEN),
                    Text("kept", font_size=20, color=INK)
                    ).arrange(DOWN, buff=0.1).move_to(keep.get_center())
        arrow = Arrow([-1.3, 0, 0], [0.8, 0, 0], color=INK, buff=0.15,
                      stroke_width=6)
        note = Text("every kept record names its matched words",
                    font_size=22, color=GREY).to_edge(DOWN, buff=0.8)
        boards = Text("18 boards", font_size=24, color=BLUE).move_to(
            [-3.4, -2.5, 0])
        self.play(FadeIn(top), FadeIn(tt))
        self.play(FadeIn(boards, shift=UP * 0.2))
        self.play(GrowArrow(arrow))
        self.play(FadeIn(keep), FadeIn(kt))
        self.play(FadeIn(note))
        self.wait(1.2)


class M09_B07Target(Scene):
    def construct(self):
        old = RoundedRectangle(corner_radius=0.2, width=9.6, height=1.8,
                               fill_color="#EDE8DA", fill_opacity=1,
                               stroke_color=GREY).move_to(UP * 1.2)
        ot = Text("advocate or educator roles", font_size=28,
                  color=GREY).move_to(old.get_center())
        new = RoundedRectangle(corner_radius=0.2, width=9.6, height=2.2,
                               fill_color=CARD, fill_opacity=1,
                               stroke_color=GREEN, stroke_width=4).move_to(
            DOWN * 1.0)
        nt = Text("any job whose product is teaching materials", font_size=28,
                  color=GREEN).move_to(new.get_center() + UP * 0.3)
        ns = Text("model: Anthropic's Claude Docs role", font_size=20,
                  color=GREY).move_to(new.get_center() + DOWN * 0.55)
        arrow = Arrow([0, 0.3, 0], [0, 0.1, 0], color=INK, buff=0.1,
                      stroke_width=6)
        morph = Circle(radius=0.35, fill_color=GREEN, fill_opacity=1,
                       stroke_width=0).move_to([4.2, 0.2, 0])
        cap = Text("what the target became", font_size=32, color=INK).to_edge(
            UP, buff=0.7)
        self.play(Write(cap))
        self.play(FadeIn(old), FadeIn(ot))
        self.play(FadeIn(morph, scale=1.4))
        self.play(GrowArrow(arrow), run_time=0.5)
        self.play(FadeIn(new, scale=0.95))
        self.play(FadeIn(nt, shift=UP * 0.15))
        self.play(FadeIn(ns, shift=UP * 0.15))
        self.wait(1.2)


class M10_B08Bullseye(Scene):
    def construct(self):
        target = VGroup(*[Circle(radius=1.5 - i * 0.4, stroke_color=ACCENT,
                                 stroke_width=3, fill_opacity=0)
                          for i in range(3)]).move_to([-2.5, 0, 0])
        words = VGroup(
            Text("“learning designer”", font_size=26, color=GREY),
            Text("“learning experiences”", font_size=26, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).move_to([3.2, 0.4, 0])
        x = Line([1.3, 0.75, 0], [5.1, 0.05, 0], color=ACCENT, stroke_width=6)
        check = VGroup(
            Line([1.3, -0.35, 0], [1.7, 0.05, 0], color=GREEN, stroke_width=8),
            Line([1.7, 0.05, 0], [2.6, -0.75, 0], color=GREEN, stroke_width=8))
        role = Text("Replit — Learning Experiences Creator", font_size=22,
                    color=INK).move_to([3.2, -1.6, 0])
        blame = Text("one word. it's in the report, with the blame attached.",
                     font_size=20, color=GREY).move_to([3.2, -2.3, 0])
        cap = Text("the bullseye, missed", font_size=34, color=INK).to_edge(
            UP, buff=0.7)
        self.play(Write(cap))
        self.play(*[Create(c) for c in target], run_time=0.9)
        self.play(FadeIn(words[0], shift=RIGHT * 0.2))
        self.play(Create(x), run_time=0.4)
        self.play(FadeIn(words[1], shift=RIGHT * 0.2))
        self.play(Create(check), run_time=0.4)
        self.play(FadeIn(role, shift=UP * 0.15))
        self.play(FadeIn(blame, shift=UP * 0.15))
        self.wait(1.2)


class M11_B09Verification(Scene):
    def construct(self):
        crits = ["re-derivable", "field names unchanged", "completeness",
                 "duplicates", "dead sources", "dates",
                 "counted, not estimated", "two hand checks", "rejects read"]
        rows = VGroup()
        for i, c in enumerate(crits):
            y = 2.2 - i * 0.62
            bg = Rectangle(width=9.6, height=0.5, fill_color=CARD,
                           fill_opacity=1, stroke_width=0).move_to([0, y, 0])
            sq = Square(side_length=0.22, stroke_color=INK, stroke_width=3,
                        fill_opacity=0).move_to([-4.4, y, 0])
            t = Text(f"{i+1}. {c}", font_size=20, color=INK).move_to(
                [-2.6, y, 0])
            rows.add(VGroup(bg, sq, t))
        head = Text("“Nothing has been verified yet.”", font_size=28,
                    color=ACCENT).to_edge(UP, buff=0.6)
        sub = Text("acceptance criteria, fixed before checking", font_size=22,
                   color=GREY).next_to(head, DOWN, buff=0.15)
        self.play(Write(head))
        self.play(FadeIn(sub, shift=DOWN * 0.15))
        for r in rows:
            self.play(FadeIn(r[0]), FadeIn(r[1]), FadeIn(r[2], shift=RIGHT * 0.15),
                      run_time=0.35)
        self.wait(1.2)


class M12_BvdtHtfOut(Scene):
    def construct(self):
        plate = RoundedRectangle(corner_radius=0.25, width=11.8, height=4.8,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK)
        recap = VGroup(*[
            Text("1 · predictions first: sealed before the run", font_size=26,
                 color=INK),
            Text("2 · the pipeline: download, filter, write + refusals",
                 font_size=26, color=INK),
            Text("3 · the run: 3,446 to 97; target moved; one word missed",
                 font_size=26, color=INK),
            Text("4 · verification: nine criteria, fixed before checking",
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
            Text("Write the prediction and the failure condition.", font_size=24,
                 color=INK),
            Text("Date it. Then let the run", font_size=24, color=INK),
            Text("embarrass you.", font_size=24, color=INK),
        ).arrange(DOWN, buff=0.25).move_to(ORIGIN)
        self.play(FadeIn(doplate))
        for d in do:
            self.play(FadeIn(d, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)
        self.play(FadeOut(do), FadeOut(doplate))
        out = title_card("Muse, in for Bear", "@NikBearBrown")
        self.play(FadeIn(out))
        self.wait(1.5)
