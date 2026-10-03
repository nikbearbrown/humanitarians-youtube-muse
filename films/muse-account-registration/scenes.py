"""scenes.py — How to register for a Muse account (Film 5).

13 Manim scenes, M01–M13. House conventions: 16:9, safe-area coords
(±6.3 x, ±3.4 y), distinct non-text shapes per beat, every on-screen text
is read aloud in its beat. Screenshots replicated as simplified mockups;
private info excluded (only muse@humanitarians.ai is shown).
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
        card = RoundedRectangle(corner_radius=0.2, width=5.6, height=3.4,
                                fill_color=BLUE, fill_opacity=1,
                                stroke_color=INK).move_to([-1.5, 0.3, 0])
        leash = Line([1.3, 0.3, 0], [4.6, 0.3, 0], color=INK, stroke_width=6)
        tag = RoundedRectangle(corner_radius=0.15, width=2.2, height=1.2,
                               fill_color=CARD, fill_opacity=1,
                               stroke_color=ACCENT, stroke_width=3).move_to(
            [5.2, 0.3, 0])
        tt = Text("$10", font_size=34, color=ACCENT).move_to(tag.get_center())
        lock = Circle(radius=0.35, fill_color=ACCENT, fill_opacity=1,
                      stroke_width=0).move_to([-1.5, 2.0, 0])
        q = Text("a ten-dollar leash", font_size=36, color=INK).to_edge(
            UP, buff=0.7)
        self.play(FadeIn(card))
        self.play(GrowFromEdge(leash, LEFT), run_time=0.6)
        self.play(FadeIn(tag), FadeIn(tt))
        self.play(FadeIn(lock, scale=1.5))
        self.play(Write(q))
        self.wait(1.2)


class M02_Bdefs(Scene):
    def construct(self):
        words = ["virtual card", "merchant-locked", "age check", "Muse account"]
        defs = ["a real number, not your card", "one merchant only: Meta",
                "$1 charged, refunded in days", "the thing we're here for"]
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


class M03_B01Email(Scene):
    def construct(self):
        env = RoundedRectangle(corner_radius=0.2, width=6.4, height=4.0,
                               fill_color=CARD, fill_opacity=1,
                               stroke_color=INK).move_to(UP * 0.3)
        flap = Polygon([-3.2, 2.3, 0], [3.2, 2.3, 0], [0, 0.6, 0],
                       fill_color="#EDE8DA", fill_opacity=1,
                       stroke_color=INK).move_to(UP * 0.3)
        addr = Text("muse@humanitarians.ai", font_size=30, color=BLUE).move_to(
            DOWN * 1.1)
        badge = Text("fresh — Meta has never seen it", font_size=22,
                     color=GREEN).move_to(DOWN * 2.1)
        cap = Text("step one: the email", font_size=32, color=INK).to_edge(
            UP, buff=0.7)
        self.play(Write(cap))
        self.play(FadeIn(env))
        self.play(FadeIn(flap, shift=DOWN * 0.2))
        self.play(Write(addr))
        self.play(FadeIn(badge, shift=UP * 0.2))
        self.wait(1.2)


class M04_B02Card(Scene):
    def construct(self):
        card = RoundedRectangle(corner_radius=0.25, width=7.2, height=4.2,
                                fill_color=BLUE, fill_opacity=1,
                                stroke_color=INK).move_to(UP * 0.4)
        name = Text("Meta CC", font_size=32, color=CARD).move_to(
            [-2.6, 1.5, 0])
        lockb = RoundedRectangle(corner_radius=0.12, width=3.6, height=0.9,
                                 fill_color=CARD, fill_opacity=0.9,
                                 stroke_width=0).move_to([1.6, 1.5, 0])
        lockt = Text("MERCHANT-LOCKED", font_size=20, color=BLUE).move_to(
            lockb.get_center())
        lim = Text("$10 limit", font_size=30, color=CARD).move_to(
            [-2.6, -0.4, 0])
        worst = Text("worst case: $10 at one merchant", font_size=24,
                     color=INK).move_to(DOWN * 2.4)
        cap = Text("step two: the card", font_size=32, color=INK).to_edge(
            UP, buff=0.7)
        self.play(Write(cap))
        self.play(FadeIn(card))
        self.play(FadeIn(name, shift=RIGHT * 0.2))
        self.play(FadeIn(lockb), FadeIn(lockt))
        self.play(FadeIn(lim, shift=RIGHT * 0.2))
        self.play(FadeIn(worst, shift=UP * 0.2))
        self.wait(1.2)


class M05_B03Instagram(Scene):
    def construct(self):
        phone = RoundedRectangle(corner_radius=0.4, width=4.4, height=6.4,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK, stroke_width=3).move_to(
            ORIGIN)
        lens = Circle(radius=0.5, stroke_color=INK, stroke_width=4,
                      fill_opacity=0).move_to(UP * 1.6)
        dot = Dot(UP * 1.6, color=ACCENT, radius=0.16)
        field1 = RoundedRectangle(corner_radius=0.15, width=3.4, height=0.7,
                                  fill_color="#EDE8DA", fill_opacity=1,
                                  stroke_width=0).move_to(DOWN * 0.2)
        field2 = RoundedRectangle(corner_radius=0.15, width=3.4, height=0.7,
                                  fill_color="#EDE8DA", fill_opacity=1,
                                  stroke_width=0).move_to(DOWN * 1.2)
        btn = RoundedRectangle(corner_radius=0.3, width=3.4, height=0.8,
                               fill_color=BLUE, fill_opacity=1,
                               stroke_width=0).move_to(DOWN * 2.3)
        bt = Text("Log in", font_size=22, color=CARD).move_to(btn.get_center())
        cap = Text("step three: Instagram first", font_size=32,
                   color=INK).to_edge(UP, buff=0.6)
        self.play(Write(cap))
        self.play(FadeIn(phone))
        self.play(Create(lens), FadeIn(dot))
        self.play(FadeIn(field1), FadeIn(field2))
        self.play(FadeIn(btn), FadeIn(bt))
        self.wait(1.2)


class M06_B04AgeCheck(Scene):
    def construct(self):
        card = RoundedRectangle(corner_radius=0.2, width=9.6, height=3.6,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=INK).move_to(UP * 0.4)
        t = Text("Confirm your age", font_size=34, color=INK).move_to(
            UP * 1.4)
        price = Text("$1.00 charged", font_size=30, color=ACCENT).move_to(
            UP * 0.4)
        ref = Text("refunded in 5–7 business days", font_size=24,
                   color=GREEN).move_to(DOWN * 0.5)
        earn = Text("the ten-dollar card earns its keep", font_size=24,
                    color=INK).move_to(DOWN * 2.2)
        coin = Circle(radius=0.4, fill_color=ACCENT, fill_opacity=1,
                      stroke_width=0).move_to([-3.6, 0.4, 0])
        refund = RoundedRectangle(corner_radius=0.12, width=2.6, height=0.8,
                                 fill_color=GREEN, fill_opacity=1,
                                 stroke_width=0).move_to([3.6, -0.5, 0])
        cap = Text("the age check", font_size=32, color=INK).to_edge(
            UP, buff=0.7)
        self.play(Write(cap))
        self.play(FadeIn(card))
        self.play(FadeIn(t, shift=DOWN * 0.2))
        self.play(FadeIn(coin, scale=1.4), Write(price), run_time=0.7)
        self.play(FadeIn(refund, scale=1.2), FadeIn(ref, shift=UP * 0.2),
                  run_time=0.6)
        self.play(FadeIn(earn, shift=UP * 0.2))
        self.wait(1.2)


class M07_B05Chain(Scene):
    def construct(self):
        labels = ["fresh email", "locked card", "Instagram", "Muse"]
        cols = [BLUE, ACCENT, INK, GREEN]
        boxes = VGroup()
        for i, (lab, col) in enumerate(zip(labels, cols)):
            x = -5.4 + i * 3.6
            b = RoundedRectangle(corner_radius=0.2, width=3.2, height=1.8,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=col, stroke_width=3).move_to(
                [x, 0.6, 0])
            t = Text(lab, font_size=22, color=col).move_to([x, 0.6, 0])
            boxes.add(VGroup(b, t))
        arrows = VGroup(*[Arrow([-3.7 + i * 3.6, 0.6, 0],
                                [-2.1 + i * 3.6, 0.6, 0],
                                color=INK, buff=0.1, stroke_width=6)
                          for i in range(3)])
        shield = Circle(radius=0.8, fill_color=GREEN, fill_opacity=0.15,
                        stroke_color=GREEN, stroke_width=3).move_to(
            DOWN * 2.0)
        st = Text("your real wallet: untouched", font_size=22,
                  color=GREEN).move_to(DOWN * 2.0)
        cap = Text("the chain isolates the blast radius", font_size=30,
                   color=INK).to_edge(UP, buff=0.7)
        self.play(Write(cap))
        for b in boxes:
            self.play(FadeIn(b, shift=RIGHT * 0.3), run_time=0.5)
        self.play(*[GrowArrow(a) for a in arrows], run_time=0.8)
        self.play(FadeIn(shield), FadeIn(st))
        self.wait(1.2)


class M08_B06MuseLogin(Scene):
    def construct(self):
        logo = Text("Muse", font_size=54, color=BLUE).move_to(UP * 1.8)
        sub = Text("AI that manages calendars", font_size=26,
                   color=INK).move_to(UP * 1.0)
        field = RoundedRectangle(corner_radius=0.3, width=6.4, height=0.9,
                                 fill_color="#EDE8DA", fill_opacity=1,
                                 stroke_width=0).move_to(DOWN * 0.2)
        ft = Text("muse@humanitarians.ai", font_size=22, color=INK).move_to(
            field.get_center())
        btn = RoundedRectangle(corner_radius=0.4, width=6.4, height=0.9,
                               fill_color=BLUE, fill_opacity=1,
                               stroke_width=0).move_to(DOWN * 1.5)
        bt = Text("Continue", font_size=24, color=CARD).move_to(
            btn.get_center())
        cap = Text("step four: muse.ai", font_size=32, color=INK).to_edge(
            UP, buff=0.7)
        self.play(Write(cap))
        self.play(FadeIn(logo, scale=1.2))
        self.play(FadeIn(sub, shift=UP * 0.2))
        self.play(FadeIn(field), FadeIn(ft, shift=RIGHT * 0.2))
        self.play(FadeIn(btn), FadeIn(bt))
        self.wait(1.2)


class M09_B07Code(Scene):
    def construct(self):
        boxes = VGroup(*[RoundedRectangle(corner_radius=0.15, width=0.9,
                                          height=1.1, fill_color=CARD,
                                          fill_opacity=1, stroke_color=BLUE,
                                          stroke_width=3).move_to(
            [-2.5 + i * 1.0, 0.6, 0]) for i in range(6)])
        sent = Text("code sent to muse@humanitarians.ai", font_size=24,
                    color=GREY).move_to(DOWN * 1.0)
        nopw = Text("no password to invent, no password to leak", font_size=24,
                    color=GREEN).move_to(DOWN * 2.0)
        cap = Text("the six-digit code", font_size=32, color=INK).to_edge(
            UP, buff=0.7)
        self.play(Write(cap))
        for i in range(0, 6, 2):
            self.play(*[FadeIn(b, shift=UP * 0.2) for b in boxes[i:i+2]],
                      run_time=0.5)
        self.play(FadeIn(sent, shift=UP * 0.2))
        self.play(FadeIn(nopw, shift=UP * 0.2))
        self.wait(1.2)


class M10_B08Disclosure(Scene):
    def construct(self):
        rows = VGroup()
        items = [("Can take actions for you", "with your approval", BLUE),
                 ("Works around the clock", "even with the app closed", INK),
                 ("Stay in control", "you choose what it can access", GREEN)]
        for i, (h, s, col) in enumerate(items):
            y = 1.6 - i * 1.5
            bg = RoundedRectangle(corner_radius=0.15, width=10.4, height=1.2,
                                  fill_color=CARD, fill_opacity=1,
                                  stroke_color=INK).move_to([0, y, 0])
            bar = Rectangle(width=0.28, height=1.2, fill_color=col,
                            fill_opacity=1, stroke_width=0).move_to(
                [-5.05, y, 0])
            th = Text(h, font_size=26, color=INK).move_to([-3.5, y + 0.14, 0])
            ts = Text(s, font_size=19, color=GREY).move_to([-3.45, y - 0.28, 0])
            rows.add(VGroup(bg, bar, th, ts))
        cap = Text("read the disclosure", font_size=32, color=INK).to_edge(
            UP, buff=0.7)
        skip = Text("the screen most people skip — don't", font_size=22,
                    color=ACCENT).to_edge(DOWN, buff=0.8)
        self.play(Write(cap))
        for r in rows:
            self.play(FadeIn(r[0]))
            self.play(GrowFromEdge(r[1], LEFT), run_time=0.35)
            self.play(FadeIn(r[2], shift=RIGHT * 0.2),
                      FadeIn(r[3], shift=RIGHT * 0.2), run_time=0.45)
        self.play(FadeIn(skip))
        self.wait(1.2)


class M11_B09In(Scene):
    def construct(self):
        bubble = RoundedRectangle(corner_radius=0.3, width=9.6, height=2.6,
                                  fill_color="#EDE8DA", fill_opacity=1,
                                  stroke_width=0).move_to(UP * 0.6)
        b1 = Text("Hey! I'm your personal agent,", font_size=28,
                  color=INK).move_to(UP * 1.0)
        b2 = Text("not just a regular assistant.", font_size=28,
                  color=INK).move_to(UP * 0.25)
        check = VGroup(
            Text("account: live", font_size=24, color=GREEN),
            Text("card on file: $10 max, Meta only", font_size=24,
                 color=GREEN),
            Text("real card: never involved", font_size=24, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).move_to(DOWN * 1.6)
        dots = VGroup(*[Circle(radius=0.1, fill_color=GREEN, fill_opacity=1,
                               stroke_width=0).move_to([-4.4, -0.9 - i * 0.55, 0])
                        for i in range(3)])
        cap = Text("you're in", font_size=36, color=INK).to_edge(UP,
                                                                 buff=0.7)
        self.play(Write(cap))
        self.play(FadeIn(bubble, shift=UP * 0.3))
        self.play(FadeIn(b1, shift=RIGHT * 0.2), FadeIn(b2, shift=RIGHT * 0.2))
        for d, c in zip(dots, check):
            self.play(FadeIn(d), FadeIn(c, shift=RIGHT * 0.2), run_time=0.45)
        self.wait(1.2)


class M12_B10Pattern(Scene):
    def construct(self):
        card = RoundedRectangle(corner_radius=0.25, width=10.6, height=4.0,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=ACCENT, stroke_width=4).move_to(
            ORIGIN)
        head = Text("the pattern, reusable", font_size=32, color=INK).move_to(
            UP * 1.2)
        items = VGroup(*[
            Text("1 · mint a merchant-locked virtual card", font_size=26,
                 color=INK),
            Text("2 · set the limit to what the signup is worth", font_size=26,
                 color=INK),
            Text("3 · name it after the merchant", font_size=26, color=INK),
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.25).move_to(DOWN * 0.3)
        dots = VGroup(*[Circle(radius=0.1, fill_color=ACCENT, fill_opacity=1,
                               stroke_width=0).move_to([-4.5, 0.35 - i * 0.62, 0])
                        for i in range(3)])
        self.play(FadeIn(card, scale=0.92))
        self.play(Write(head))
        for d, it in zip(dots, items):
            self.play(FadeIn(d), FadeIn(it, shift=RIGHT * 0.2), run_time=0.5)
        self.wait(1.5)


class M13_BvdtHtfOut(Scene):
    def construct(self):
        plate = RoundedRectangle(corner_radius=0.25, width=11.8, height=4.8,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK)
        recap = VGroup(*[
            Text("1 · the setup: fresh email + $10 card locked to Meta",
                 font_size=26, color=INK),
            Text("2 · the chain: Instagram, the $1 age check, blast radius",
                 font_size=26, color=INK),
            Text("3 · the registration: code, disclosure, you're in",
                 font_size=26, color=INK),
            Text("4 · the pattern: lock the card, every time", font_size=26,
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
            Text("Next signup that demands your card:", font_size=24,
                 color=INK),
            Text("mint the locked card first.", font_size=24, color=INK),
            Text("Set the limit to what it's worth.", font_size=24,
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
