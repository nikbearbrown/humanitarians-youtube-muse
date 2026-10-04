#!/usr/bin/env python3
"""layouts.py — Single source of truth for the Northeastern Guest Speaker
Series templates. Each layout is defined once in px; build.py renders it to
HTML, SVG, and IDML.

LOCKED (do not change): Northeastern colors, series branding, SEIS/Teams
labels, red frame.
EDITABLE: the EVENT dict below — photo, title, description, date/time,
speaker, QR, course/host line.

Element kinds (all coords in px, text y = baseline):
  ("frame", sw)
  ("lockup", x, y, n_size, name_size)
  ("qr", x, y, s)
  ("text", x, y, lines, size, weight, fill, ls)   lines: str or [str]
  ("vtext", cx, cy, s, size, fill, ls)            vertical, reads bottom-to-top
  ("photo", x, y, w, h)
  ("rect", x, y, w, h, fill, stroke, sw)
  ("line", x1, y1, x2, y2, sw, color)
  ("dateblock", x, y, date, time, size)
"""
import math

RED = "#C12925"
BLACK = "#111111"
WHITE = "#ffffff"
GREY = "#dddddd"
PHOTO = "doug-menuez.png"

# ------------------------------------------------------------------ content
# EDIT: change these for each event.
TITLE_LINES = ["Fearless", "Genius"]
TITLE_1LINE = "Fearless Genius"
DESC_1LINE = "A conversation on Silicon Valley, creativity, and technological change."
DESC_2A = ["A conversation on Silicon Valley, creativity,",
           "and technological change."]
DESC_2B = ["A conversation on Silicon Valley,",
           "creativity, and technological change."]
DATE = "SATURDAY, OCT. 10, 2026"
DATE_SHORT = "SAT, OCT. 10, 2026"
TIME = "12:00\u20131:30 PM ET"
SPEAKER = "Doug Menuez"
ROLE_1LINE = "Documentary Photographer \u00b7 Author of Fearless Genius"
ROLE_LINES = ["Documentary Photographer", "Author of Fearless Genius"]
COURSE = "INFO 7375: Branding & AI"
HOSTS = "Prof. Nina Harris and Prof. Nik Bear Brown"
SEIS = "Open to the SEIS community"
TEAMS = "LIVE ON MICROSOFT TEAMS"
SERIES_1LINE = "Guest Speaker Series"
SERIES_LINES = ["Guest", "Speaker", "Series"]
SERIES_2LINES = ["Guest Speaker", "Series"]

# ------------------------------------------------------------------ layouts
def layout_letter():
    return {"name": "letter", "label": "LETTER 8.5x11", "w": 816, "h": 1056,
            "elements": [
        ("frame", 30),
        ("lockup", 70, 112, 54, 16),
        ("qr", 610, 60, 120),
        ("text", 70, 252, SERIES_LINES[0], 84, 900, BLACK, -2, True),
        ("text", 70, 336, SERIES_LINES[1], 84, 900, BLACK, -2, True),
        ("text", 70, 420, SERIES_LINES[2], 84, 900, BLACK, -2, True),
        ("photo", 70, 452, 490, 210),
        ("rect", 560, 452, 70, 210, RED, "none", 0),
        ("vtext", 595, 557, TEAMS, 12, WHITE, 2),
        ("text", 70, 724, TITLE_1LINE, 50, 900, BLACK, -1),
        ("text", 70, 752, DESC_1LINE, 16, 400, BLACK, 0),
        ("dateblock", 70, 768, DATE, TIME, 17),
        ("text", 70, 884, SPEAKER, 30, 900, BLACK, 0),
        ("text", 70, 908, ROLE_1LINE, 16, 400, BLACK, 0),
        ("line", 70, 936, 746, 936, 2, BLACK),
        ("text", 70, 958, COURSE, 15, 800, BLACK, 0),
        ("text", 70, 978, HOSTS, 14, 400, BLACK, 0),
        ("text", 70, 996, SEIS, 13, 400, BLACK, 0, True),
    ]}


def layout_16x9():
    return {"name": "16x9", "label": "16:9 1920x1080", "w": 1920, "h": 1080,
            "elements": [
        ("frame", 30),
        ("photo", 30, 30, 800, 1020),
        ("lockup", 900, 150, 68, 20),
        ("qr", 1720, 70, 130),
        ("text", 900, 292, SERIES_2LINES[0], 88, 900, BLACK, -2, True),
        ("text", 900, 380, SERIES_2LINES[1], 88, 900, BLACK, -2, True),
        ("text", 900, 420, TEAMS, 20, 700, RED, 4, True),
        ("text", 900, 544, TITLE_1LINE, 96, 900, BLACK, -2),
        ("text", 900, 612, DESC_2A[0], 28, 400, BLACK, 0),
        ("text", 900, 648, DESC_2A[1], 28, 400, BLACK, 0),
        ("dateblock", 900, 676, DATE, TIME, 30),
        ("text", 900, 880, SPEAKER, 44, 900, BLACK, 0),
        ("text", 900, 920, ROLE_1LINE, 28, 400, BLACK, 0),
        ("line", 900, 980, 1850, 980, 3, BLACK),
        ("text", 900, 1012, COURSE, 24, 800, BLACK, 0),
    ]}


def layout_9x16():
    return {"name": "9x16", "label": "9:16 1080x1920", "w": 1080, "h": 1920,
            "elements": [
        ("frame", 30),
        ("lockup", 70, 150, 72, 22),
        ("qr", 870, 70, 140),
        ("text", 70, 330, SERIES_LINES[0], 100, 900, BLACK, -2, True),
        ("text", 70, 424, SERIES_LINES[1], 100, 900, BLACK, -2, True),
        ("text", 70, 518, SERIES_LINES[2], 100, 900, BLACK, -2, True),
        ("text", 70, 566, TEAMS, 21, 700, RED, 4, True),
        ("photo", 30, 610, 1020, 540),
        ("text", 70, 1262, TITLE_LINES[0], 104, 900, BLACK, -2),
        ("text", 70, 1366, TITLE_LINES[1], 104, 900, BLACK, -2),
        ("text", 70, 1410, DESC_2A[0], 27, 400, BLACK, 0),
        ("text", 70, 1444, DESC_2A[1], 27, 400, BLACK, 0),
        ("dateblock", 70, 1472, DATE, TIME, 30),
        ("text", 70, 1674, SPEAKER, 48, 900, BLACK, 0),
        ("text", 70, 1716, ROLE_1LINE, 28, 400, BLACK, 0),
        ("line", 70, 1760, 1010, 1760, 3, BLACK),
        ("text", 70, 1792, COURSE, 26, 800, BLACK, 0),
        ("text", 70, 1820, HOSTS, 24, 400, BLACK, 0),
        ("text", 70, 1846, SEIS, 22, 400, BLACK, 0, True),
    ]}


def layout_4x5():
    return {"name": "4x5", "label": "4:5 1080x1350", "w": 1080, "h": 1350,
            "elements": [
        ("frame", 28),
        ("lockup", 70, 128, 62, 19),
        ("text", 70, 280, SERIES_2LINES[0], 78, 900, BLACK, -2, True),
        ("text", 70, 358, SERIES_2LINES[1], 78, 900, BLACK, -2, True),
        ("text", 70, 396, TEAMS, 18, 700, RED, 4, True),
        ("photo", 30, 430, 1020, 380),
        ("text", 70, 912, TITLE_1LINE, 88, 900, BLACK, -2),
        ("text", 70, 974, DESC_2A[0], 25, 400, BLACK, 0),
        ("text", 70, 1006, DESC_2A[1], 25, 400, BLACK, 0),
        ("dateblock", 70, 1032, DATE_SHORT, TIME, 26),
        ("text", 70, 1206, SPEAKER, 40, 900, BLACK, 0),
        ("text", 70, 1242, ROLE_1LINE, 24, 400, BLACK, 0),
        ("line", 70, 1268, 1010, 1268, 3, BLACK),
        ("text", 70, 1292, COURSE, 22, 800, BLACK, 0),
        ("text", 70, 1312, SEIS, 16, 400, BLACK, 0, True),
    ]}


def layout_1x1():
    return {"name": "1x1", "label": "1:1 1080x1080", "w": 1080, "h": 1080,
            "elements": [
        ("frame", 26),
        ("photo", 26, 26, 470, 1028),
        ("lockup", 556, 118, 50, 15),
        ("text", 556, 290, SERIES_LINES[0], 58, 900, BLACK, -1, True),
        ("text", 556, 348, SERIES_LINES[1], 58, 900, BLACK, -1, True),
        ("text", 556, 406, SERIES_LINES[2], 58, 900, BLACK, -1, True),
        ("text", 556, 444, TEAMS, 14, 700, RED, 3, True),
        ("text", 556, 560, TITLE_LINES[0], 76, 900, BLACK, -1),
        ("text", 556, 636, TITLE_LINES[1], 76, 900, BLACK, -1),
        ("text", 556, 678, DESC_2B[0], 21, 400, BLACK, 0),
        ("text", 556, 706, DESC_2B[1], 21, 400, BLACK, 0),
        ("dateblock", 556, 726, DATE_SHORT, TIME, 21),
        ("text", 556, 880, SPEAKER, 34, 900, BLACK, 0),
        ("text", 556, 912, ROLE_LINES[0], 19, 400, BLACK, 0),
        ("text", 556, 936, ROLE_LINES[1], 19, 400, BLACK, 0),
        ("line", 556, 966, 1024, 966, 3, BLACK),
        ("text", 556, 992, COURSE, 18, 800, BLACK, 0),
        ("text", 556, 1018, SEIS, 15, 400, BLACK, 0, True),
    ]}


ALL = [layout_letter, layout_16x9, layout_9x16, layout_4x5, layout_1x1]

# ------------------------------------------------------- bounds verification
_WF = {900: 0.60, 800: 0.58, 700: 0.56, 400: 0.50}


def _text_w(s, size, weight):
    return len(s) * size * _WF[weight] + abs(s.count(" ") * 0) + len(s) * 0  # ls handled below


def element_bbox(el):
    k = el[0]
    if k == "frame":
        return None  # frame is the page edge by design
    if k == "lockup":
        _, x, y, n_size, name_size = el
        w = n_size * 1.15 + max(len(s) for s in
            ["Northeastern University", "Software Engineering",
             "and Information Systems"]) * name_size * 0.55
        return (x, y - n_size, x + w, y + name_size)
    if k == "qr":
        _, x, y, s = el
        return (x, y, x + s, y + s)
    if k == "text":
        _, x, y, lines, size, weight, fill, ls = el[:8]
        lines = [lines] if isinstance(lines, str) else lines
        w = max(len(s) * size * _WF[weight] + len(s) * ls for s in lines)
        return (x, y - size, x + w, y + size * 0.25)
    if k == "vtext":
        _, cx, cy, s, size, fill, ls = el
        h = len(s) * (size * 0.60 + ls)
        return (cx - size, cy - h / 2, cx + size, cy + h / 2)
    if k == "photo":
        _, x, y, w, h = el
        return (x, y, x + w, y + h)
    if k == "rect":
        _, x, y, w, h, *_ = el
        return (x, y, x + w, y + h)
    if k == "line":
        _, x1, y1, x2, y2, sw, _ = el
        return (min(x1, x2), min(y1, y2) - sw, max(x1, x2), max(y1, y2) + sw)
    if k == "dateblock":
        _, x, y, date, time, size = el
        w = max(len(date), len(time)) * size * 0.62 + 36
        h = 2 * size + 54
        return (x, y, x + w, y + h)
    raise ValueError(f"unknown element {k}")


def verify_layout(layout):
    w, h = layout["w"], layout["h"]
    bad = []
    for el in layout["elements"]:
        bb = element_bbox(el)
        if bb is None:
            continue
        x1, y1, x2, y2 = bb
        if x1 < 0 or y1 < 0 or x2 > w or y2 > h:
            bad.append((el[0], str(el[1:4]), f"bbox=({x1:.0f},{y1:.0f},{x2:.0f},{y2:.0f})"))
    if bad:
        raise SystemExit(f"LAYOUT OVERFLOW in {layout['name']}: {bad}")
    print(f"  {layout['name']}: all elements within {w}x{h} OK")
