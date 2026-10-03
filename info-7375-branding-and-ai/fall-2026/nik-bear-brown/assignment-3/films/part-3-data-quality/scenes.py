"""scenes.py — Muse measures quality (Assignment 3, Part 3 film).

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
        card = RoundedRectangle(corner_radius=0.2, width=7.2, height=3.6,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=INK).move_to(UP * 0.3)
        t = Text("“high quality!”", font_size=44, color=INK).move_to(
            UP * 0.9)
        stamp = Text("UNMEASURED", font_size=36, color=ACCENT).move_to(
            DOWN * 0.5)
        frame = Rectangle(width=5.6, height=1.1, stroke_color=ACCENT,
                          stroke_width=4).move_to(DOWN * 0.5)
        cap = Text("quality isn't a claim", font_size=34, color=INK).to_edge(
            UP, buff=0.7)
        self.play(Write(cap))
        self.play(FadeIn(card))
        self.play(FadeIn(t, shift=DOWN * 0.2))
        self.play(FadeIn(frame), Write(stamp))
        self.wait(1.2)


class M02_Bdefs(Scene):
    def construct(self):
        words = ["completeness", "reject reason", "duplicate", "validator"]
        defs = ["essential fields present", "why each reject was rejected",
                "same job twice, counted once", "a check before shipping"]
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


class M03_B01Gate(Scene):
    def construct(self):
        gate = VGroup(
            Line([-5.0, 1.2, 0], [5.0, 1.2, 0], color=INK, stroke_width=6),
            *[Line([x, 1.2, 0], [x, -0.4, 0], color=INK, stroke_width=4)
              for x in [-3.0, -1.0, 1.0, 3.0]])
        reqs = VGroup(*[Text(w, font_size=28, color=GREEN) for w in
                        ["title", "link", "date"]]).arrange(
            RIGHT, buff=1.2).move_to(DOWN * 0.2)
        badge = Text("100% — by construction", font_size=30,
                     color=GREEN).move_to(DOWN * 1.8)
        seal = Circle(radius=0.45, fill_color=GREEN, fill_opacity=1,
                      stroke_width=0).move_to([4.6, -1.8, 0])
        cap = Text("the writer refuses anything less", font_size=32,
                   color=INK).to_edge(UP, buff=0.7)
        self.play(Write(cap))
        self.play(Create(gate), run_time=0.8)
        for r in reqs:
            self.play(FadeIn(r, shift=UP * 0.2), run_time=0.4)
        self.play(FadeIn(seal, scale=1.4))
        self.play(FadeIn(badge, shift=UP * 0.2))
        self.wait(1.2)


class M04_B02RealNumber(Scene):
    def construct(self):
        enforced = RoundedRectangle(corner_radius=0.15, width=8.0, height=1.4,
                                    fill_color="#EDE8DA", fill_opacity=1,
                                    stroke_width=0).move_to(UP * 1.2)
        et = Text("enforced fields: 100% (measures the gate)", font_size=24,
                  color=GREY).move_to(enforced.get_center())
        real = RoundedRectangle(corner_radius=0.15, width=8.0, height=1.8,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=ACCENT, stroke_width=4).move_to(
            DOWN * 0.6)
        rt = Text("optional fields: the real number", font_size=28,
                  color=ACCENT).move_to(real.get_center())
        arrow = Arrow([0, 0.5, 0], [0, 0.3, 0], color=INK, buff=0.08,
                      stroke_width=6)
        cap = Text("report the number the gate doesn't enforce", font_size=30,
                   color=INK).to_edge(UP, buff=0.7)
        self.play(Write(cap))
        self.play(FadeIn(enforced), FadeIn(et))
        self.play(GrowArrow(arrow), run_time=0.4)
        self.play(FadeIn(real, scale=0.95), FadeIn(rt))
        self.wait(1.2)


class M05_B03Rejects(Scene):
    def construct(self):
        data = [("no keyword match", 2341), ("1 topic word", 945),
                ("2 topic words", 63)]
        bars = VGroup()
        for i, (lab, n) in enumerate(data):
            x = -4.0 + i * 4.0
            h = max(0.6, n / 2341 * 3.2)
            bar = Rectangle(width=2.2, height=h, fill_color=ACCENT,
                            fill_opacity=0.75, stroke_width=0).move_to(
                [x, -1.8 + h / 2, 0])
            tv = Text(str(n), font_size=28, color=ACCENT).move_to(
                [x, -1.8 + h + 0.3, 0])
            tl = Text(lab, font_size=20, color=INK).move_to([x, -2.3, 0])
            bars.add(VGroup(bar, tv, tl))
        total = Text("3,349 rejects — a table, not a shrug", font_size=26,
                     color=INK).to_edge(DOWN, buff=0.8)
        cap = Text("every reject carries its reason", font_size=32,
                   color=INK).to_edge(UP, buff=0.7)
        self.play(Write(cap))
        for b in bars:
            self.play(GrowFromEdge(b[0], DOWN), run_time=0.5)
            self.play(FadeIn(b[1]), FadeIn(b[2]), run_time=0.3)
        self.play(FadeIn(total, shift=UP * 0.2))
        self.wait(1.2)


class M06_B04Dedup(Scene):
    def construct(self):
        j1 = RoundedRectangle(corner_radius=0.15, width=4.4, height=2.0,
                              fill_color=CARD, fill_opacity=1,
                              stroke_color=BLUE, stroke_width=3).move_to(
            [-2.8, 0.4, 0])
        j2 = RoundedRectangle(corner_radius=0.15, width=4.4, height=2.0,
                              fill_color=CARD, fill_opacity=1,
                              stroke_color=BLUE, stroke_width=3).move_to(
            [2.8, 0.4, 0])
        t1 = Text("same job", font_size=24, color=BLUE).move_to(j1.get_center())
        t2 = Text("same job", font_size=24, color=BLUE).move_to(j2.get_center())
        key = Text("key: source + posting id", font_size=24,
                   color=INK).move_to(DOWN * 1.6)
        zero = Text("collapsed this run: 0", font_size=28,
                    color=GREEN).move_to(DOWN * 2.5)
        merge = Arrow([-0.4, 0.4, 0], [0.4, 0.4, 0], color=INK,
                      stroke_width=8, buff=0.1)
        cap = Text("seen twice, counted once", font_size=32,
                   color=INK).to_edge(UP, buff=0.7)
        self.play(Write(cap))
        self.play(FadeIn(j1), FadeIn(t1), run_time=0.5)
        self.play(FadeIn(j2), FadeIn(t2), run_time=0.5)
        self.play(GrowArrow(merge), run_time=0.5)
        self.play(FadeIn(key, shift=UP * 0.2))
        self.play(FadeIn(zero, shift=UP * 0.2))
        self.wait(1.2)


class M07_B05Dates(Scene):
    def construct(self):
        shapes = VGroup(*[
            Text("Jan 5, 2026", font_size=24, color=GREY),
            Text("2026-01-05T09:00:00Z", font_size=24, color=GREY),
            Text("01/05/2026", font_size=24, color=GREY),
        ]).arrange(DOWN, buff=0.3).move_to([-3.4, 0, 0])
        arrow = Arrow([-1.0, 0, 0], [0.6, 0, 0], color=INK, buff=0.1,
                      stroke_width=6)
        out = RoundedRectangle(corner_radius=0.15, width=4.6, height=1.6,
                               fill_color=CARD, fill_opacity=1,
                               stroke_color=GREEN, stroke_width=3).move_to(
            [3.2, 0.4, 0])
        ot = Text("2026-01-05", font_size=30, color=GREEN).move_to(
            out.get_center() + UP * 0.2)
        os_ = Text("+ original kept", font_size=18, color=GREY).move_to(
            out.get_center() + DOWN * 0.45)
        cap = Text("three shapes in, one column out", font_size=32,
                   color=INK).to_edge(UP, buff=0.7)
        self.play(Write(cap))
        for s in shapes:
            self.play(FadeIn(s, shift=RIGHT * 0.2), run_time=0.4)
        self.play(GrowArrow(arrow), run_time=0.5)
        self.play(FadeIn(out, scale=0.92))
        self.play(FadeIn(ot, shift=UP * 0.1))
        self.play(FadeIn(os_, shift=UP * 0.1))
        self.wait(1.2)


class M08_B06Validators(Scene):
    def construct(self):
        checks = ["non-empty title", "parseable date", "well-formed URL",
                  "count asserted vs API"]
        rows = VGroup()
        for i, c in enumerate(checks):
            y = 1.6 - i * 1.05
            bg = Rectangle(width=9.6, height=0.85, fill_color=CARD,
                           fill_opacity=1, stroke_width=0).move_to([0, y, 0])
            box = Square(side_length=0.32, stroke_color=INK, stroke_width=4,
                         fill_opacity=0).move_to([-4.4, y, 0])
            tick = VGroup(
                Line([-4.52, y, 0], [-4.38, y - 0.12, 0], color=GREEN,
                     stroke_width=8),
                Line([-4.38, y - 0.12, 0], [-4.18, y + 0.14, 0], color=GREEN,
                     stroke_width=8))
            t = Text(c, font_size=24, color=INK).move_to([-2.6, y, 0])
            rows.add(VGroup(bg, box, tick, t))
        note = Text("each one a mistake that already happened once",
                    font_size=22, color=GREY).to_edge(DOWN, buff=0.8)
        cap = Text("checks that catch mistakes", font_size=32,
                   color=INK).to_edge(UP, buff=0.7)
        self.play(Write(cap))
        for r in rows:
            self.play(FadeIn(r[0]), FadeIn(r[1]))
            self.play(Create(r[2]), run_time=0.35)
            self.play(FadeIn(r[3], shift=RIGHT * 0.2), run_time=0.35)
        self.play(FadeIn(note, shift=UP * 0.2))
        self.wait(1.2)


class M09_B07Counted(Scene):
    def construct(self):
        table = RoundedRectangle(corner_radius=0.15, width=8.0, height=3.4,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK).move_to(UP * 0.4)
        rows = VGroup(*[
            Text("fetched ......... 3,446", font_size=24, color=INK),
            Text("kept ............... 97", font_size=24, color=GREEN),
            Text("rejected ...... 3,349", font_size=24, color=INK),
            Text("duplicates ......... 0", font_size=24, color=INK),
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.18).move_to(
            table.get_center())
        pen = Line([-4.5, -2.2, 0], [-3.5, -1.4, 0], color=ACCENT,
                   stroke_width=10)
        hand = Text("the script writes this", font_size=24,
                    color=ACCENT).move_to(DOWN * 2.4)
        cap = Text("counted, not estimated", font_size=34, color=INK).to_edge(
            UP, buff=0.7)
        self.play(Write(cap))
        self.play(FadeIn(table))
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.25), run_time=0.45)
        self.play(Create(pen), run_time=0.5)
        self.play(FadeIn(hand, shift=UP * 0.2))
        self.wait(1.2)


class M10_B08Problems(Scene):
    def construct(self):
        srcs = VGroup()
        for i, name in enumerate(["Greenhouse", "Ashby", "SmartRecruiters"]):
            x = -4.2 + i * 4.2
            b = RoundedRectangle(corner_radius=0.15, width=3.8, height=1.8,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=BLUE, stroke_width=3).move_to(
                [x, 0.8, 0])
            t = Text(name, font_size=22, color=BLUE).move_to(b.get_center())
            srcs.add(VGroup(b, t))
        dead = Circle(radius=0.9, stroke_color=ACCENT, stroke_width=4,
                      fill_opacity=0).move_to([4.2, 0.8, 0])
        dx = VGroup(
            Line([3.9, 1.1, 0], [4.5, 0.5, 0], color=ACCENT, stroke_width=8),
            Line([3.9, 0.5, 0], [4.5, 1.1, 0], color=ACCENT, stroke_width=8))
        state = RoundedRectangle(corner_radius=0.15, width=6.4, height=1.2,
                                 fill_color="#EDE8DA", fill_opacity=1,
                                 stroke_width=0).move_to(DOWN * 1.8)
        st = Text("state file: never written on a failed run", font_size=22,
                  color=INK).move_to(state.get_center())
        cap = Text("a dead source doesn't kill the run", font_size=30,
                   color=INK).to_edge(UP, buff=0.7)
        self.play(Write(cap))
        for s in srcs:
            self.play(FadeIn(s, shift=DOWN * 0.2), run_time=0.4)
        self.play(Create(dead), run_time=0.5)
        self.play(Create(dx), run_time=0.4)
        self.play(FadeIn(state))
        self.play(FadeIn(st, shift=UP * 0.15))
        self.wait(1.2)


class M11_B09Replicate(Scene):
    def construct(self):
        cmd = RoundedRectangle(corner_radius=0.15, width=7.2, height=1.4,
                               fill_color=INK, fill_opacity=1,
                               stroke_width=0).move_to(UP * 1.0)
        ct = Text("python3 collect.py", font_size=28, color=CARD).move_to(
            cmd.get_center())
        nokey = Text("no keys", font_size=24, color=GREEN).move_to(DOWN * 0.2)
        raw = RoundedRectangle(corner_radius=0.15, width=7.2, height=1.4,
                               fill_color=CARD, fill_opacity=1,
                               stroke_color=INK).move_to(DOWN * 1.4)
        rt = Text("dated raw/ responses ship too", font_size=24,
                  color=INK).move_to(raw.get_center())
        peer = Circle(radius=0.5, fill_color=BLUE, fill_opacity=1,
                      stroke_width=0).move_to(RIGHT * 5.0 + DOWN * 0.2)
        cap = Text("a peer can redo all of it", font_size=32,
                   color=INK).to_edge(UP, buff=0.7)
        self.play(Write(cap))
        self.play(FadeIn(cmd), FadeIn(ct))
        self.play(FadeIn(nokey, scale=1.2))
        self.play(FadeIn(raw), FadeIn(rt))
        self.play(FadeIn(peer, scale=1.4))
        self.wait(1.2)


class M12_BvdtHtfOut(Scene):
    def construct(self):
        plate = RoundedRectangle(corner_radius=0.25, width=11.8, height=4.8,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK)
        recap = VGroup(*[
            Text("1 · completeness: enforced at write, reported on optional",
                 font_size=26, color=INK),
            Text("2 · the counts: rejects by reason, 0 dupes, dates clean",
                 font_size=26, color=INK),
            Text("3 · validators: four checks; script counts everything",
                 font_size=26, color=INK),
            Text("4 · excellence: problems handled; peer can replicate",
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
            Text("Replace one quality claim", font_size=24, color=INK),
            Text("with a number your script writes.", font_size=24,
                 color=INK),
            Text("Put it where someone can check it.", font_size=24,
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
