"""scenes.py — Muse shows the output (Film 2).

13 Manim scenes, M01–M13. House conventions: 16:9, safe-area coords
(±6.3 x, ±3.4 y), each scene carries distinct non-text shapes, every
on-screen text is read aloud in its beat.
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
    g = VGroup(
        Line(ORIGIN, RIGHT * 0.5 + DOWN * 0.3, color=color, stroke_width=10),
        Line(RIGHT * 0.5 + DOWN * 0.3, RIGHT * 1.3 + UP * 0.4,
             color=color, stroke_width=10),
    ).scale(scale).move_to(pos)
    return g


def bullet(pos, color=ACCENT):
    return Circle(radius=0.09, fill_color=color, fill_opacity=1,
                  stroke_width=0).move_to(pos)


def brief_card(title, company, fit, why_lines, step, y_shift=0):
    card = RoundedRectangle(corner_radius=0.25, width=10.5, height=5.6,
                            fill_color=CARD, fill_opacity=1, stroke_color=INK)
    head = T(title, font_size=30, color=INK)
    co = T(f"{company} — fit {fit}  PURSUE", font_size=22, color=ACCENT)
    why = VGroup()
    for w in why_lines:
        dot = Circle(radius=0.09, fill_color=ACCENT, fill_opacity=1,
                     stroke_width=0)
        line = T(w, font_size=20, color=INK)
        row = VGroup(dot, line).arrange(RIGHT, buff=0.2, aligned_edge=ORIGIN)
        why.add(row)
    why.arrange(DOWN, aligned_edge=LEFT, buff=0.14)
    foot = T("Next: " + step, font_size=20, color=ACCENT)
    text = VGroup(head, co, why, foot).arrange(DOWN, aligned_edge=LEFT,
                                               buff=0.3)
    # tuck the whole text block inside the card: 0.7 left margin, centered
    text.move_to([card.get_left()[0] + 0.7 + text.width / 2, 0, 0])
    return VGroup(card, head, co, why, foot)


class M01_Bidea(Scene):
    def construct(self):
        desk = Rectangle(width=9, height=0.25, fill_color=INK,
                         fill_opacity=1, stroke_width=0).shift(DOWN * 2.2)
        wr = Circle(radius=0.55, fill_color=ACCENT, fill_opacity=1,
                    stroke_width=0).shift(LEFT * 3 + DOWN * 1.2)
        doc = Rectangle(width=3.2, height=4.2, fill_color=CARD, fill_opacity=1,
                        stroke_color=INK).shift(RIGHT * 2.5 + UP * 0.4)
        json_line = T('{ "jobs": [ ... ] }', font_size=22, color=GREY).move_to(
            doc.get_center())
        cap = T("raw JSON is not an output", font_size=34, color=INK).to_edge(
            UP, buff=0.8)
        x = Cross(scale_factor=0.5, color=ACCENT).move_to(doc.get_center())
        self.play(FadeIn(desk), FadeIn(wr), FadeIn(doc), FadeIn(json_line))
        self.play(Write(cap))
        self.play(Create(x))
        self.wait(1.2)


class M02_Bdefs(Scene):
    def construct(self):
        words = ["output", "digest", "brief", "proof"]
        defs = ["a file built for a human", "the one-page summary",
                "one role card:\nscore, reasons,\nlink, next step",
                "the run report\nthat shows the\nwork is real"]
        cards = VGroup()
        for i, (w, d) in enumerate(zip(words, defs)):
            x = -5.4 + i * 3.6
            box = RoundedRectangle(corner_radius=0.2, width=3.2, height=2.4,
                                   fill_color=CARD, fill_opacity=1,
                                   stroke_color=INK).move_to([x, 0, 0])
            t = T(w, font_size=30, color=ACCENT).move_to([x, 0.55, 0])
            s = T(d, font_size=16, color=INK).move_to([x, -0.45, 0])
            cards.add(VGroup(box, t, s))
        for c in cards:
            self.play(FadeIn(c, shift=UP * 0.3), run_time=0.7)
        self.wait(1.2)


class M03_B01Test(Scene):
    def construct(self):
        left_box = Rectangle(width=4.6, height=4.4, fill_color="#EDE8DA",
                             fill_opacity=1, stroke_color=GREY)
        left_lab = T("raw JSON", font_size=28, color=GREY)
        left = VGroup(left_lab, left_box).arrange(DOWN, buff=0.25)
        left_json = T('{ "jobs": [ ... ] }', font_size=18,
                      color=GREY).move_to(left_box.get_center())
        left.add(left_json)
        left.shift(LEFT * 3.4)
        right_box = RoundedRectangle(corner_radius=0.2, width=4.6, height=4.4,
                                     fill_color=CARD, fill_opacity=1,
                                     stroke_color=INK)
        right_lab = T("brief card", font_size=28, color=ACCENT)
        right = VGroup(right_lab, right_box).arrange(DOWN, buff=0.25)
        right_inner = VGroup(*[
            T("one sentence of why", font_size=18, color=INK),
            T("the posting link", font_size=18, color=INK),
            T("what to do next", font_size=18, color=INK),
        ]).arrange(DOWN, buff=0.2).move_to(right_box.get_center())
        right.add(right_inner)
        right.shift(RIGHT * 3.4)
        check = check_mark(right_box.get_center() + DOWN * 2.9, scale=1.0)
        cap = T("Could a non-technical person use it?", font_size=32,
                   color=INK).to_edge(UP, buff=0.7)
        self.play(FadeIn(left), FadeIn(right))
        self.play(Write(cap))
        self.play(Create(check))
        self.wait(1.2)


class M04_B02Flow(Scene):
    def construct(self):
        labels = ["Input\npostings", "Processing\nmatcher", "Output\ndigest + briefs",
                  "Proof\nrun report"]
        boxes = VGroup()
        for i, lab in enumerate(labels):
            x = -5.4 + i * 3.6
            b = RoundedRectangle(corner_radius=0.2, width=3.2, height=2.2,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK).move_to([x, 0, 0])
            t = T(lab, font_size=22, color=INK).move_to([x, 0, 0])
            boxes.add(VGroup(b, t))
        arrows = VGroup(*[Arrow([-4.0 + i * 3.6, -1.5, 0],
                                [-3.2 + i * 3.6, -1.5, 0],
                                color=ACCENT, buff=0.1) for i in range(3)])
        for b in boxes:
            self.play(FadeIn(b, shift=RIGHT * 0.3), run_time=0.6)
        self.play(*[GrowArrow(a) for a in arrows], run_time=0.9)
        self.wait(1.2)


class M05_B03Digest(Scene):
    def construct(self):
        page = RoundedRectangle(corner_radius=0.2, width=9.6, height=5.4,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK)
        head = T("Opportunity digest — 2026-10-03", font_size=30,
                    color=INK).move_to(UP * 2.05)
        rows = VGroup()
        for i, (t, f) in enumerate([("Developer Education Lead — Anthropic", "0.91"),
                                    ("Designer Advocate, Partnerships — Figma", "0.84"),
                                    ("Learning Experiences Creator — Replit", "0.75")]):
            sq = Square(side_length=0.18, fill_color=ACCENT, fill_opacity=1,
                        stroke_width=0)
            r = T(f"{t}  ({f})", font_size=22, color=INK)
            row = VGroup(sq, r).arrange(RIGHT, buff=0.25, aligned_edge=ORIGIN)
            rows.add(row)
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.25).move_to(UP * 0.35)
        badge = T("md  +  html", font_size=24, color=ACCENT).move_to(DOWN * 3.2)
        self.play(FadeIn(page))
        self.play(Write(head))
        for row in rows:
            self.play(FadeIn(row[0]), FadeIn(row[1], shift=RIGHT * 0.3),
                      run_time=0.5)
        self.play(FadeIn(badge))
        self.wait(1.2)


class M06_B04BriefAnthropic(Scene):
    def construct(self):
        card = brief_card(
            "Developer Education Lead, Claude Platform", "Anthropic", "0.91",
            ["title matches 'developer education' (1.0)",
             "text names audience: developer, community",
             "company demand 1.0"],
            "Draft the application.")
        self.play(FadeIn(card[0]))
        self.play(FadeIn(card[1], shift=UP * 0.2), FadeIn(card[2], shift=UP * 0.2))
        for row in card[3]:
            self.play(FadeIn(row, shift=RIGHT * 0.2), run_time=0.5)
        self.play(FadeIn(card[4], shift=UP * 0.2))
        self.wait(1.2)


class M07_B05BriefFigma(Scene):
    def construct(self):
        card = brief_card(
            "Designer Advocate, Partnerships", "Figma", "0.84",
            ["title matches 'advocate' (1.0)",
             "audience: community, customer, partner",
             "gap-close: design system, design token"],
            "Draft the application.")
        self.play(FadeIn(card[0]))
        self.play(FadeIn(card[1], shift=UP * 0.2), FadeIn(card[2], shift=UP * 0.2))
        for row in card[3]:
            self.play(FadeIn(row, shift=RIGHT * 0.2), run_time=0.5)
        self.play(FadeIn(card[4], shift=UP * 0.2))
        self.wait(1.2)


class M08_B06BriefReplit(Scene):
    def construct(self):
        card = brief_card(
            "Learning Experiences Creator", "Replit", "0.75",
            ["title matches 'learning experience' (1.0)",
             "materials: 'instructional design' + audience",
             "the bullseye recovered"],
            "Draft the application.")
        self.play(FadeIn(card[0]))
        self.play(FadeIn(card[1], shift=UP * 0.2), FadeIn(card[2], shift=UP * 0.2))
        for row in card[3]:
            self.play(FadeIn(row, shift=RIGHT * 0.2), run_time=0.5)
        self.play(FadeIn(card[4], shift=UP * 0.2))
        self.wait(1.2)


class M09_B07RunReport(Scene):
    def construct(self):
        head = T("run-report-2026-10-03.json", font_size=28,
                    color=INK).to_edge(UP, buff=0.7)
        stats = VGroup(
            T("714 postings scored in 3.1 s", font_size=26, color=INK),
            T("0 quarantined · 0 errors", font_size=26, color=ACCENT),
        ).arrange(DOWN, buff=0.25).move_to(UP * 1.2)
        dec = [("PURSUE", 22, ACCENT), ("NETWORK", 37, ACCENT),
               ("WATCH", 325, GREY), ("SKIP", 330, "#C9C4B5")]
        bars = VGroup()
        for i, (lab, n, col) in enumerate(dec):
            y = 0.4 - i * 0.85
            w = max(0.6, n / 330 * 8)
            bar = Rectangle(width=w, height=0.55, fill_color=col,
                            fill_opacity=1, stroke_width=0).move_to(
                [-5 + w / 2, y, 0])
            t = T(f"{lab}: {n}", font_size=20, color=INK).next_to(
                bar, LEFT, buff=0.2)
            bars.add(VGroup(bar, t))
        self.play(Write(head))
        self.play(FadeIn(stats, shift=DOWN * 0.2))
        for b in bars:
            self.play(GrowFromEdge(b[0], LEFT), run_time=0.4)
            self.play(FadeIn(b[1], shift=RIGHT * 0.15), run_time=0.3)
        self.wait(1.2)


class M10_B08Nontech(Scene):
    def construct(self):
        browser = RoundedRectangle(corner_radius=0.25, width=9.6, height=5.4,
                                   fill_color=CARD, fill_opacity=1,
                                   stroke_color=INK)
        bar = Rectangle(width=9.5, height=0.68, fill_color="#EDE8DA",
                        fill_opacity=1, stroke_width=0).move_to(
            browser.get_top() + DOWN * 0.35)
        url = T("digest-2026-10-03.html", font_size=20,
                   color=ACCENT).move_to(bar.get_center())
        checks = VGroup()
        for i, q in enumerate(["one sentence of why", "one link", "one next step"]):
            y = 1.2 - i * 0.9
            row = VGroup(
                T(q, font_size=24, color=INK).move_to([-1.5, y, 0]),
                check_mark([2.2, y, 0], scale=0.45),
            )
            checks.add(row)
        self.play(FadeIn(browser), FadeIn(bar), FadeIn(url))
        for row in checks:
            self.play(FadeIn(row[0], shift=RIGHT * 0.2), run_time=0.5)
            self.play(Create(row[1]), run_time=0.4)
        self.wait(1.2)


class M11_B09Gap(Scene):
    def construct(self):
        box = RoundedRectangle(corner_radius=0.2, width=8.6, height=3.6,
                               fill_color="#EDE8DA", fill_opacity=0.9,
                               stroke_color=GREY).move_to(UP * 0.4)
        t = T("scheduled delivery: approvals → weekly digest → email",
                 font_size=24, color=GREY).move_to(box.get_center() + UP * 0.5)
        stamp = T("TODO", font_size=44, color=ACCENT).move_to(
            box.get_center() + DOWN * 0.6)
        muse = Circle(radius=0.5, fill_color=ACCENT, fill_opacity=1,
                      stroke_width=0).shift(DOWN * 2.4 + LEFT * 2)
        cap = T("The honest gap", font_size=32, color=INK).to_edge(UP,
                                                                      buff=0.7)
        self.play(Write(cap))
        self.play(FadeIn(box), FadeIn(t))
        self.play(Write(stamp))
        self.play(FadeIn(muse, shift=UP * 0.3))
        self.wait(1.2)


class M12_B10Loop(Scene):
    def construct(self):
        stages = [("3,446\npostings\ncollected", 2.6),
                  ("714\nscored\nin one run", 2.2),
                  ("digest + 15 briefs\n+ run report", 3.4)]
        xs = [-4.6, -0.4, 3.6]
        for i, ((lab, w), x) in enumerate(zip(stages, xs)):
            c = Circle(radius=w / 2, fill_color=CARD, fill_opacity=1,
                       stroke_color=INK).move_to([x, 0, 0])
            t = T(lab, font_size=20, color=INK).move_to([x, 0, 0])
            self.play(FadeIn(c, scale=0.8), FadeIn(t), run_time=0.7)
            if i < 2:
                a = Arrow([x + w / 2 + 0.15, 0, 0],
                          [xs[i + 1] - stages[i + 1][1] / 2 - 0.15, 0, 0],
                          color=ACCENT, buff=0.1)
                self.play(GrowArrow(a), run_time=0.5)
        self.wait(1.2)


class M13_BvdtHtfOut(Scene):
    def construct(self):
        plate = RoundedRectangle(corner_radius=0.25, width=11.6, height=4.6,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK)
        recap = VGroup(*[
            T("1 · an output is a file a human can open", font_size=26,
                 color=INK),
            T("2 · the gallery: digest, 15 briefs, run report", font_size=26,
                 color=INK),
            T("3 · quality check passes; scheduled delivery is the gap",
                 font_size=26, color=INK),
            T("4 · the loop is closed: postings to usable files",
                 font_size=26, color=INK),
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to(ORIGIN)
        self.play(FadeIn(plate))
        for r in recap:
            self.play(FadeIn(r, shift=RIGHT * 0.3), run_time=0.6)
        self.wait(0.8)
        self.play(FadeOut(recap), FadeOut(plate))
        doplate = RoundedRectangle(corner_radius=0.25, width=10.4, height=3.8,
                                   fill_color="#EDE8DA", fill_opacity=1,
                                   stroke_color=ACCENT)
        do = VGroup(
            T("Your turn", font_size=34, color=ACCENT),
            T("Open the HTML digest. Pick one PURSUE brief.", font_size=24,
                 color=INK),
            T("Run the three-question test.", font_size=24, color=INK),
            T("Which brief would you act on first?", font_size=24,
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
