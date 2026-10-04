#!/usr/bin/env python3
"""build_svg.py — Generate 5 editable SVG templates for the Northeastern
Guest Speaker Series. SVG is XML: Illustrator opens it natively with live,
editable text and vectors.

LOCKED: Northeastern colors (#C12925 / #111), series branding.
EDITABLE: photo, event title, description, date/time, speaker, QR, course line.
Each is marked with an XML comment.
"""
import os

RED = "#C12925"
BLACK = "#111111"
WHITE = "#ffffff"
GREY_BG = "#dddddd"
FAM = "'Helvetica Neue',Helvetica,Arial,sans-serif"

# EDIT: change these for each event. Everything else is series branding.
EVENT_TITLE = ["Fearless", "Genius"]
EVENT_TITLE_1LINE = "Fearless Genius"
EVENT_DESC = "A conversation on Silicon Valley, creativity, and technological change."
EVENT_DATE = "SATURDAY, OCT. 10, 2026"
EVENT_DATE_SHORT = "SAT, OCT. 10, 2026"
EVENT_TIME = "12:00\u20131:30 PM ET"
SPEAKER = "Doug Menuez"
SPEAKER_ROLE = ["Documentary Photographer", "Author of Fearless Genius"]
SPEAKER_ROLE_1LINE = "Documentary Photographer \u00b7 Author of Fearless Genius"
COURSE = "INFO 7375: Branding & AI"
HOSTS = "Prof. Nina Harris and Prof. Nik Bear Brown"
PHOTO = "doug-menuez.png"

OUT = os.path.dirname(os.path.abspath(__file__))


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def doc(w, h, body, name):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<!-- ======================================================================
  NORTHEASTERN GUEST SPEAKER SERIES — {name}
  LOCKED: Northeastern colors, series branding, SEIS/Teams labels, red frame.
  EDITABLE: items marked EDIT — photo, title, description, date/time,
  speaker, QR code, course/host line.
====================================================================== -->
<rect x="0" y="0" width="{w}" height="{h}" fill="{WHITE}"/>
{body}
</svg>
"""


def frame(w, h, sw=30):
    o = sw / 2
    return f'<rect x="{o}" y="{o}" width="{w-sw}" height="{h-sw}" fill="none" stroke="{RED}" stroke-width="{sw}"/>'


def t(x, y, s, size, weight=900, fill=BLACK, anchor="start", ls=0, gid=None):
    g1 = f'<g id="{gid}">' if gid else ""
    g2 = "</g>" if gid else ""
    return (f'{g1}<text x="{x}" y="{y}" font-family="{FAM}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" '
            f'letter-spacing="{ls}">{esc(s)}</text>{g2}')


def vtext(cx, cy, s, size, fill=WHITE, ls=3):
    # vertical text reading bottom-to-top
    return (f'<text transform="translate({cx},{cy}) rotate(-90)" font-family="{FAM}" '
            f'font-size="{size}" font-weight="700" fill="{fill}" text-anchor="middle" '
            f'letter-spacing="{ls}">{esc(s)}</text>')


def photo_box(pid, x, y, w, h):
    return f"""<g id="{pid}">
<!-- EDIT: speaker/event photo — replace {PHOTO} -->
<clipPath id="{pid}-clip"><rect x="{x}" y="{y}" width="{w}" height="{h}"/></clipPath>
<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{GREY_BG}"/>
<g clip-path="url(#{pid}-clip)">
<image xlink:href="{PHOTO}" href="{PHOTO}" x="{x}" y="{y}" width="{w}" height="{h}" preserveAspectRatio="xMidYMid slice"/>
</g>
</g>"""


def qr_box(x, y, s):
    return f"""<g id="editable-qr">
<!-- EDIT: replace with the event's QR code (link to Teams/registration) -->
<rect x="{x}" y="{y}" width="{s}" height="{s}" fill="none" stroke="{BLACK}" stroke-width="3" stroke-dasharray="10,7"/>
<text x="{x+s/2}" y="{y+s/2+6}" font-family="{FAM}" font-size="15" font-weight="700" fill="{BLACK}" text-anchor="middle">QR CODE</text>
</g>"""


def lockup(x, y, n_size, name_size, gid="fixed-nu-lockup"):
    return f"""<g id="{gid}">
<!-- FIXED: Northeastern lockup -->
<text x="{x}" y="{y}" font-family="{FAM}" font-size="{n_size}" font-weight="900" fill="{RED}">N</text>
<text x="{x+n_size*1.15}" y="{y-n_size*0.62}" font-family="{FAM}" font-size="{name_size}" font-weight="700" fill="{BLACK}">Northeastern University</text>
<text x="{x+n_size*1.15}" y="{y-n_size*0.62+name_size*1.3}" font-family="{FAM}" font-size="{name_size}" font-weight="700" fill="{BLACK}">Software Engineering</text>
<text x="{x+n_size*1.15}" y="{y-n_size*0.62+name_size*2.6}" font-family="{FAM}" font-size="{name_size}" font-weight="700" fill="{BLACK}">and Information Systems</text>
</g>"""


def date_time(x, y, date_s, time_s, size, gid="editable-datetime"):
    # returns (svg, total_height)
    bw = size * 0.62
    date_w = len(date_s) * bw * 0.62 + 36
    svg = f"""<g id="{gid}">
<!-- EDIT: date and time -->
<rect x="{x}" y="{y}" width="{date_w:.0f}" height="{size+22}" fill="{BLACK}"/>
<text x="{x+18}" y="{y+size+4}" font-family="{FAM}" font-size="{size}" font-weight="800" fill="{WHITE}" letter-spacing="1">{esc(date_s)}</text>
</g>"""
    y2 = y + size + 34
    svg += f"""
<g id="{gid}-time">
<rect x="{x}" y="{y2}" width="{date_w:.0f}" height="{size+18}" fill="none" stroke="{BLACK}" stroke-width="3"/>
<text x="{x+18}" y="{y2+size+2}" font-family="{FAM}" font-size="{size}" font-weight="800" fill="{BLACK}">{esc(time_s)}</text>
</g>"""
    return svg, (y2 + size + 18) - y


# ---------------------------------------------------------------- letter ---
def letter():
    w, h = 816, 1056
    b = [frame(w, h)]
    b.append(lockup(70, 128, 60, 18))
    b.append(qr_box(596, 66, 150))
    # FIXED: series headline
    b.append('<g id="fixed-series-title">\n<!-- FIXED: series branding -->')
    y = 300
    for line in ["Guest", "Speaker", "Series"]:
        b.append(t(70, y, line, 100, ls=-2)); y += 94
    b.append("</g>")
    # photo band + Teams label
    b.append(photo_box("editable-photo", 70, 545, 500, 250))
    b.append(f'<rect x="570" y="545" width="74" height="250" fill="{RED}"/>')
    b.append(vtext(607, 670, "LIVE ON MICROSOFT TEAMS", 16))
    b.append("<!-- FIXED: Teams label -->")
    # EDIT: event title
    y = 872
    b.append('<g id="editable-event-title">\n<!-- EDIT: event title -->')
    b.append(t(70, y, EVENT_TITLE_1LINE, 54, ls=-1))
    b.append("</g>")
    b.append(f'<g id="editable-event-desc">\n<!-- EDIT: one-line description -->\n{t(70, y+32, EVENT_DESC, 18, weight=400)}' + "</g>")
    d, dh = date_time(70, y+52, EVENT_DATE, EVENT_TIME, 20)
    b.append(d)
    y2 = y + 52 + dh + 26
    b.append(f'<g id="editable-speaker">\n<!-- EDIT: speaker name -->\n{t(70, y2, SPEAKER, 34)}')
    b.append(t(70, y2+26, SPEAKER_ROLE_1LINE, 18, weight=400) + "\n</g>\n<!-- EDIT: speaker role / credentials -->")
    b.append(f'<line x1="70" y1="1000" x2="746" y2="1000" stroke="{BLACK}" stroke-width="2"/>')
    b.append(f'<g id="editable-course">\n<!-- EDIT: course / host line for this event -->\n{t(70, 1022, COURSE, 16, weight=800)}')
    b.append(t(70, 1040, HOSTS, 15, weight=400) + "\n</g>")
    return doc(w, h, "\n".join(b), "LETTER 8.5x11")


# ------------------------------------------------------------------ 16:9 ---
def w16():
    w, h = 1920, 1080
    b = [frame(w, h)]
    b.append(photo_box("editable-photo", 30, 30, 800, 1020))
    x = 900
    b.append(lockup(x, 150, 68, 20))
    b.append(qr_box(1720, 70, 130))
    b.append('<g id="fixed-series-title">\n<!-- FIXED: series branding -->')
    b.append(t(x, 300, "Guest Speaker Series", 92, ls=-2) + "\n</g>")
    b.append(t(x, 340, "LIVE ON MICROSOFT TEAMS", 20, weight=700, fill=RED, ls=4))
    b.append("<!-- FIXED: Teams label -->")
    b.append('<g id="editable-event-title">\n<!-- EDIT: event title -->')
    b.append(t(x, 470, EVENT_TITLE_1LINE, 104, ls=-2) + "\n</g>")
    b.append(f'<g id="editable-event-desc">\n<!-- EDIT: one-line description -->\n{t(x, 530, EVENT_DESC, 30, weight=400)}' + "</g>")
    d, dh = date_time(x, 570, EVENT_DATE, EVENT_TIME, 30)
    b.append(d)
    y2 = 570 + dh + 34
    b.append(f'<g id="editable-speaker">\n<!-- EDIT: speaker name -->\n{t(x, y2, SPEAKER, 44)}')
    b.append(t(x, y2+40, SPEAKER_ROLE_1LINE, 28, weight=400) + "\n</g>")
    b.append(f'<line x1="{x}" y1="980" x2="1850" y2="980" stroke="{BLACK}" stroke-width="3"/>')
    b.append(f'<g id="editable-course">\n<!-- EDIT: course / host line -->\n{t(x, 1010, COURSE, 24, weight=800)}' + "</g>")
    return doc(w, h, "\n".join(b), "16:9 1920x1080")


# ------------------------------------------------------------------ 9:16 ---
def v16():
    w, h = 1080, 1920
    b = [frame(w, h)]
    b.append(lockup(70, 150, 72, 22))
    b.append(qr_box(870, 70, 140))
    b.append('<g id="fixed-series-title">\n<!-- FIXED: series branding -->')
    y = 330
    for line in ["Guest", "Speaker", "Series"]:
        b.append(t(70, y, line, 100, ls=-2)); y += 94
    b.append("</g>")
    b.append(t(70, y + 10, "LIVE ON MICROSOFT TEAMS", 21, weight=700, fill=RED, ls=4))
    b.append("<!-- FIXED: Teams label -->")
    b.append(photo_box("editable-photo", 30, 660, 1020, 560))
    y = 1330
    b.append('<g id="editable-event-title">\n<!-- EDIT: event title -->')
    for line in EVENT_TITLE:
        b.append(t(70, y, line, 112, ls=-2)); y += 104
    b.append("</g>")
    b.append(f'<g id="editable-event-desc">\n<!-- EDIT: one-line description -->\n{t(70, y+10, EVENT_DESC, 30, weight=400)}' + "</g>")
    d, dh = date_time(70, y + 50, EVENT_DATE, EVENT_TIME, 31)
    b.append(d)
    y2 = y + 50 + dh + 36
    b.append(f'<g id="editable-speaker">\n<!-- EDIT: speaker name -->\n{t(70, y2, SPEAKER, 50)}')
    b.append(t(70, y2+40, SPEAKER_ROLE_1LINE, 29, weight=400) + "\n</g>")
    b.append(f'<line x1="70" y1="1820" x2="1010" y2="1820" stroke="{BLACK}" stroke-width="3"/>')
    b.append(f'<g id="editable-course">\n<!-- EDIT: course / host line -->\n{t(70, 1852, COURSE, 27, weight=800)}' + "</g>")
    b.append(t(70, 1880, "Open to the SEIS community", 24, weight=400))
    b.append("<!-- FIXED: SEIS line -->")
    return doc(w, h, "\n".join(b), "9:16 1080x1920")


# ------------------------------------------------------------------ 4:5 ----
def p45():
    w, h = 1080, 1350
    b = [frame(w, h)]
    b.append(lockup(70, 130, 64, 20))
    b.append('<g id="fixed-series-title">\n<!-- FIXED: series branding -->')
    b.append(t(70, 290, "Guest Speaker Series", 84, ls=-2) + "\n</g>")
    b.append(t(70, 328, "LIVE ON MICROSOFT TEAMS", 19, weight=700, fill=RED, ls=4))
    b.append("<!-- FIXED: Teams label -->")
    b.append(photo_box("editable-photo", 30, 370, 1020, 420))
    y = 900
    b.append('<g id="editable-event-title">\n<!-- EDIT: event title -->')
    b.append(t(70, y, EVENT_TITLE_1LINE, 98, ls=-2) + "\n</g>")
    b.append(f'<g id="editable-event-desc">\n<!-- EDIT: one-line description -->\n{t(70, y+44, EVENT_DESC, 27, weight=400)}' + "</g>")
    d, dh = date_time(70, y + 80, EVENT_DATE_SHORT, EVENT_TIME, 27)
    b.append(d)
    y2 = y + 80 + dh + 30
    b.append(f'<g id="editable-speaker">\n<!-- EDIT: speaker name -->\n{t(70, y2, SPEAKER, 42)}')
    b.append(t(70, y2+36, SPEAKER_ROLE_1LINE, 25, weight=400) + "\n</g>")
    b.append(f'<line x1="70" y1="1268" x2="1010" y2="1268" stroke="{BLACK}" stroke-width="3"/>')
    b.append(f'<g id="editable-course">\n<!-- EDIT: course / host line -->\n{t(70, 1298, COURSE, 23, weight=800)}' + "</g>")
    b.append(t(70, 1322, "Open to the SEIS community", 21, weight=400))
    b.append("<!-- FIXED: SEIS line -->")
    return doc(w, h, "\n".join(b), "4:5 1080x1350")


# ------------------------------------------------------------------ 1:1 ----
def sq():
    w, h = 1080, 1080
    b = [frame(w, h)]
    b.append(photo_box("editable-photo", 26, 26, 470, 1028))
    x = 556
    b.append(lockup(x, 120, 52, 16))
    b.append('<g id="fixed-series-title">\n<!-- FIXED: series branding -->')
    y = 300
    for line in ["Guest", "Speaker", "Series"]:
        b.append(t(x, y, line, 60, ls=-1)); y += 58
    b.append("</g>")
    b.append(t(x, y + 6, "LIVE ON MICROSOFT TEAMS", 15, weight=700, fill=RED, ls=3))
    b.append("<!-- FIXED: Teams label -->")
    b.append('<g id="editable-event-title">\n<!-- EDIT: event title -->')
    y += 100
    for line in EVENT_TITLE:
        b.append(t(x, y, line, 80, ls=-1)); y += 76
    b.append("</g>")
    b.append(f'<g id="editable-event-desc">\n<!-- EDIT: one-line description -->\n{t(x, y+8, "A conversation on Silicon Valley,", 22, weight=400)}')
    b.append(t(x, y+36, "creativity, and technological change.", 22, weight=400) + "\n</g>")
    d, dh = date_time(x, y + 60, EVENT_DATE_SHORT, EVENT_TIME, 22)
    b.append(d)
    y2 = y + 60 + dh + 28
    b.append(f'<g id="editable-speaker">\n<!-- EDIT: speaker name -->\n{t(x, y2, SPEAKER, 35)}')
    b.append(t(x, y2+32, SPEAKER_ROLE_1LINE, 20, weight=400) + "\n</g>")
    b.append(f'<line x1="{x}" y1="986" x2="1024" y2="986" stroke="{BLACK}" stroke-width="3"/>')
    b.append(f'<g id="editable-course">\n<!-- EDIT: course / host line -->\n{t(x, 1012, COURSE, 19, weight=800)}' + "</g>")
    return doc(w, h, "\n".join(b), "1:1 1080x1080")


if __name__ == "__main__":
    jobs = [("poster-letter.svg", letter), ("poster-16x9.svg", w16),
            ("poster-9x16.svg", v16), ("poster-4x5.svg", p45),
            ("poster-1x1.svg", sq)]
    for fname, fn in jobs:
        path = os.path.join(OUT, fname)
        with open(path, "w") as f:
            f.write(fn())
        print("wrote", path)
