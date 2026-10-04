#!/usr/bin/env python3
"""build.py — Render all Guest Speaker Series templates from layouts.py.

Outputs per size (letter, 16x9, 9x16, 4x5, 1x1):
  template-<name>.html   editable web/print template
  poster-<name>.svg      XML vector template (opens in Illustrator)
  poster-<name>.idml      InDesign package, zipped XML (opens in InDesign)

Usage: python3 build.py
Edit layouts.py (EDIT: values + element coordinates) then re-run.
"""
import os
import zipfile
import xml.dom.minidom

import layouts
from layouts import RED, BLACK, WHITE, GREY, PHOTO

OUT = os.path.dirname(os.path.abspath(__file__))
IDPKG = "http://ns.adobe.com/AdobeInDesign/idml/1.0/packaging"
PT = 0.75  # px -> pt for IDML


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def lines_of(lines):
    return [lines] if isinstance(lines, str) else list(lines)


# ------------------------------------------------------------------ SVG ----
def svg_text(x, y, s, size, weight, fill, ls):
    return (f'<text x="{x}" y="{y}" font-family="\'Helvetica Neue\',Helvetica,Arial,sans-serif" '
            f'font-size="{size}" font-weight="{weight}" fill="{fill}" '
            f'letter-spacing="{ls}">{esc(s)}</text>')


def render_svg(layout):
    w, h = layout["w"], layout["h"]
    b = [f'<rect x="0" y="0" width="{w}" height="{h}" fill="{WHITE}"/>']
    b.append(f'<rect x="15" y="15" width="{w-30}" height="{h-30}" fill="none" '
             f'stroke="{RED}" stroke-width="30"/>')  # placeholder, replaced below
    b.pop()  # (frame handled per-element for exact sw)
    pid = [0]
    tid = [0]

    for el in layout["elements"]:
        k = el[0]
        if k == "frame":
            sw = el[1]
            o = sw / 2
            b.append(f'<rect x="{o}" y="{o}" width="{w-sw}" height="{h-sw}" '
                     f'fill="none" stroke="{RED}" stroke-width="{sw}"/>')
        elif k == "lockup":
            _, x, y, n_size, name_size = el
            b.append(f'<g id="fixed-nu-lockup"><!-- FIXED: Northeastern lockup -->')
            b.append(svg_text(x, y, "N", n_size, 900, RED, 0))
            lx = x + n_size * 1.15
            ly = y - n_size * 0.62
            for i, s in enumerate(["Northeastern University", "Software Engineering",
                                   "and Information Systems"]):
                b.append(svg_text(lx, ly + i * name_size * 1.3, s, name_size, 700, BLACK, 0))
            b.append("</g>")
        elif k == "qr":
            _, x, y, s = el
            b.append(f'<g id="editable-qr"><!-- EDIT: replace with the event QR code -->')
            b.append(f'<rect x="{x}" y="{y}" width="{s}" height="{s}" fill="none" '
                     f'stroke="{BLACK}" stroke-width="3" stroke-dasharray="10,7"/>')
            b.append(f'<text x="{x + s / 2}" y="{y + s / 2 + 5}" text-anchor="middle" '
                     f'font-family="\'Helvetica Neue\',Helvetica,Arial,sans-serif" '
                     f'font-size="14" font-weight="700" fill="{BLACK}">QR CODE</text>')
            b.append("</g>")
        elif k == "text":
            _, x, y, ls_, size, weight, fill, ls = el[:8]
            fixed = el[8] if len(el) > 8 else False
            gid = f"fixed-t{tid[0]}" if fixed else f"editable-t{tid[0]}"
            tid[0] += 1
            tag = "FIXED: series branding — do not change" if fixed else "EDIT"
            b.append(f'<g id="{gid}"><!-- {tag} -->')
            dy = 0
            for s in lines_of(ls_):
                b.append(svg_text(x, y + dy, s, size, weight, fill, ls))
                dy += size * 1.25
            b.append("</g>")
        elif k == "vtext":
            _, cx, cy, s, size, fill, ls = el
            b.append(f'<!-- FIXED: Teams label -->')
            b.append(f'<text transform="translate({cx},{cy}) rotate(-90)" '
                     f'font-family="\'Helvetica Neue\',Helvetica,Arial,sans-serif" '
                     f'font-size="{size}" font-weight="700" fill="{fill}" '
                     f'text-anchor="middle" letter-spacing="{ls}">{esc(s)}</text>')
        elif k == "photo":
            _, x, y, w_, h_ = el
            pid[0] += 1
            p = f"ph{pid[0]}"
            b.append(f'<g id="editable-photo-{p}"><!-- EDIT: speaker/event photo -->')
            b.append(f'<clipPath id="{p}c"><rect x="{x}" y="{y}" width="{w_}" height="{h_}"/></clipPath>')
            b.append(f'<rect x="{x}" y="{y}" width="{w_}" height="{h_}" fill="{GREY}"/>')
            b.append(f'<g clip-path="url(#{p}c)"><image xlink:href="{PHOTO}" href="{PHOTO}" '
                     f'x="{x}" y="{y}" width="{w_}" height="{h_}" '
                     f'preserveAspectRatio="xMidYMid slice"/></g></g>')
        elif k == "rect":
            _, x, y, w_, h_, fill, stroke, sw = el
            so = f' stroke="{stroke}" stroke-width="{sw}"' if stroke != "none" else ""
            b.append(f'<rect x="{x}" y="{y}" width="{w_}" height="{h_}" fill="{fill}"{so}/>')
        elif k == "line":
            _, x1, y1, x2, y2, sw, color = el
            b.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
                     f'stroke="{color}" stroke-width="{sw}"/>')
        elif k == "dateblock":
            _, x, y, date, time, size = el
            bw = max(len(date), len(time)) * size * 0.62 + 36
            b.append(f'<g id="editable-datetime"><!-- EDIT: date and time -->')
            b.append(f'<rect x="{x}" y="{y}" width="{bw:.0f}" height="{size+22}" fill="{BLACK}"/>')
            b.append(svg_text(x + 18, y + size + 4, date, size, 800, WHITE, 1))
            y2 = y + size + 34
            b.append(f'<rect x="{x}" y="{y2}" width="{bw:.0f}" height="{size+18}" '
                     f'fill="none" stroke="{BLACK}" stroke-width="3"/>')
            b.append(svg_text(x + 18, y2 + size + 2, time, size, 800, BLACK, 0))
            b.append("</g>")
    return (f'<svg xmlns="http://www.w3.org/2000/svg" '
            f'xmlns:xlink="http://www.w3.org/1999/xlink" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}">\n<!-- {layout["label"]}: LOCKED series branding, '
            f'EDITABLE event slots (see comments) -->\n' + "\n".join(b) + "\n</svg>\n")


# ------------------------------------------------------------------ HTML ---
def render_html(layout):
    w, h = layout["w"], layout["h"]
    css = ("*{margin:0;padding:0;box-sizing:border-box}"
           "body{background:#888;display:flex;justify-content:center}"
           f".page{{position:relative;width:{w}px;height:{h}px;background:{WHITE};overflow:hidden;"
           "font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;color:#111}")
    b = []
    for el in layout["elements"]:
        k = el[0]
        if k == "frame":
            sw = el[1]
            b.append(f'<div style="position:absolute;inset:0;border:{sw}px solid {RED}"></div>')
        elif k == "lockup":
            _, x, y, n_size, name_size = el
            lx = x + n_size * 1.15
            ly = y - n_size * 0.62
            names = "<br>".join(["Northeastern University", "Software Engineering",
                                 "and Information Systems"])
            b.append(
                f'<!-- FIXED: Northeastern lockup -->'
                f'<div style="position:absolute;left:{x}px;top:{y-n_size}px;color:{RED};'
                f'font-weight:900;font-size:{n_size}px;line-height:1">N</div>'
                f'<div style="position:absolute;left:{lx}px;top:{ly-name_size*0.8}px;'
                f'font-weight:700;font-size:{name_size}px;line-height:1.3">{names}</div>')
        elif k == "qr":
            _, x, y, s = el
            b.append(
                f'<!-- EDIT: replace with the event QR code -->'
                f'<div style="position:absolute;left:{x}px;top:{y}px;width:{s}px;height:{s}px;'
                f'border:3px dashed {BLACK};display:flex;align-items:center;'
                f'justify-content:center;font-weight:700;font-size:14px;text-align:center">QR<br>CODE</div>')
        elif k == "text":
            _, x, y, ls_, size, weight, fill, ls = el[:8]
            fixed = el[8] if len(el) > 8 else False
            tag = "FIXED" if fixed else "EDIT"
            txt = "<br>".join(esc(s) for s in lines_of(ls_))
            b.append(
                f'<!-- {tag} --><div style="position:absolute;left:{x}px;top:{y-size*0.8:.0f}px;'
                f'font-size:{size}px;font-weight:{weight};color:{fill};'
                f'letter-spacing:{ls}px;white-space:nowrap;line-height:1.25">{txt}</div>')
        elif k == "vtext":
            _, cx, cy, s, size, fill, ls = el
            b.append(
                f'<!-- FIXED: Teams label -->'
                f'<div style="position:absolute;left:{cx}px;top:{cy}px;transform:translate(-50%,-50%) rotate(180deg);'
                f'writing-mode:vertical-rl;font-size:{size}px;font-weight:700;color:{fill};'
                f'letter-spacing:{ls}px;white-space:nowrap">{esc(s)}</div>')
        elif k == "photo":
            _, x, y, w_, h_ = el
            b.append(
                f'<!-- EDIT: speaker/event photo -->'
                f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w_}px;height:{h_}px;'
                f'overflow:hidden;background:{GREY}">'
                f'<img src="{PHOTO}" alt="Speaker photo" '
                f'style="width:100%;height:100%;object-fit:cover;display:block"></div>')
        elif k == "rect":
            _, x, y, w_, h_, fill, stroke, sw = el
            bd = f'border:{sw}px solid {stroke};' if stroke != "none" else ""
            bg = f'background:{fill};' if fill != "none" else ""
            b.append(f'<div style="position:absolute;left:{x}px;top:{y}px;'
                     f'width:{w_}px;height:{h_}px;{bg}{bd}"></div>')
        elif k == "line":
            _, x1, y1, x2, y2, sw, color = el
            b.append(f'<div style="position:absolute;left:{min(x1,x2)}px;top:{min(y1,y2)-sw/2}px;'
                     f'width:{abs(x2-x1)}px;height:{sw}px;background:{color}"></div>')
        elif k == "dateblock":
            _, x, y, date, time, size = el
            bw = max(len(date), len(time)) * size * 0.62 + 36
            y2 = y + size + 34
            b.append(
                f'<!-- EDIT: date and time -->'
                f'<div style="position:absolute;left:{x}px;top:{y}px;width:{bw:.0f}px;'
                f'height:{size+22}px;background:{BLACK};color:{WHITE};font-weight:800;'
                f'font-size:{size}px;display:flex;align-items:center;padding:0 18px;'
                f'letter-spacing:1px;white-space:nowrap">{esc(date)}</div>'
                f'<div style="position:absolute;left:{x}px;top:{y2}px;width:{bw:.0f}px;'
                f'height:{size+18}px;border:3px solid {BLACK};font-weight:800;'
                f'font-size:{size}px;display:flex;align-items:center;padding:0 18px;'
                f'white-space:nowrap">{esc(time)}</div>')
    return (f'<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">\n'
            f'<!-- NORTHEASTERN GUEST SPEAKER SERIES — {layout["label"]} -->\n'
            f'<!-- LOCKED: NU colors/branding. EDITABLE items marked EDIT. -->\n'
            f'<style>{css}</style></head><body>\n'
            f'<div class="page">\n' + "\n".join(b) + '\n</div></body></html>\n')


# ------------------------------------------------------------------ IDML ---
def _pt(v):
    s = f"{v * PT:.2f}"
    return s.rstrip("0").rstrip(".")


def _font_for(weight):
    if weight >= 900:
        return ("Arial Black", "Regular")
    if weight >= 700:
        return ("Arial", "Bold")
    return ("Arial", "Regular")


def _swatch(hexcolor):
    return {"#C12925": "Swatch/nuRed", "#111111": "Swatch/nuBlack",
            "#ffffff": "Swatch/Paper"}.get(hexcolor, "Swatch/nuBlack")


class IDMLDoc:
    def __init__(self, layout):
        self.layout = layout
        self.pw, self.ph = _pt(layout["w"]), _pt(layout["h"])
        self.styles = {}   # key -> name
        self.style_defs = []
        self.stories = []  # (id, style_name, [(kind, text)])
        self.items = []
        self.n = 0

    def uid(self, p):
        self.n += 1
        return f"{p}{self.n}"

    def style(self, weight, size_px, fill, align="Left", ls=0):
        font, fstyle = _font_for(weight)
        size = round(size_px * PT, 1)
        tracking = int(round(ls / size_px * 1000)) if ls else 0
        key = (font, fstyle, size, fill, align, tracking)
        if key not in self.styles:
            name = f"s{len(self.styles)}"
            self.styles[key] = name
            tr = f'<Tracking type="integer">{tracking}</Tracking>' if tracking else ""
            self.style_defs.append(
                f'<ParagraphStyle Self="ParagraphStyle/{name}" Name="{name}"><Properties>'
                f'<AppliedFont type="string">{font}</AppliedFont>'
                f'<FontStyle type="string">{fstyle}</FontStyle>'
                f'<PointSize type="unit">{size}</PointSize>'
                f'<Leading type="unit">{round(size*1.2,1)}</Leading>'
                f'<FillColor type="string">{_swatch(fill)}</FillColor>'
                f'<Justification type="enumeration">{align}</Justification>{tr}'
                f'</Properties></ParagraphStyle>')
        return self.styles[key]

    def add_text(self, x, y, lines, size, weight, fill, ls=0, w_factor=None,
                 transform=None, fixed=False):
        lines = lines_of(lines)
        st = self.style(weight, size, fill, ls=ls)
        sid = self.uid("Story")
        tf = self.uid("tf")
        wf = w_factor or {900: 0.66, 800: 0.64, 700: 0.62, 400: 0.56}[weight]
        wpx = max(len(s) * size * wf + len(s) * ls for s in lines) * 1.08 + 8
        fbox = (_pt(x), _pt(y - size * 1.02), _pt(wpx), _pt(len(lines) * size * 1.3))
        segs = []
        for i, s in enumerate(lines):
            if i:
                segs.append(("br", ""))
            segs.append(("t", s))
        self.stories.append((sid, st, segs))
        tr = transform or f"1 0 0 1 {_pt(x)} {_pt(y - size * 1.02)}"
        tag = "FIXED: series branding" if fixed else "EDIT"
        self.items.append(
            f'<!-- {tag} -->'
            f'<TextFrame Self="{tf}" ParentStory="{sid}" PreviousTextFrame="n" '
            f'NextTextFrame="n" Layer="Layer/layer1" ItemTransform="{tr}">'
            f'{_rect_geom(*fbox)}<TextFramePreference/></TextFrame>')

    def add_rect(self, x, y, w, h, fill="none", stroke="none", sw=0):
        rid = self.uid("r")
        f = _swatch(fill) if fill != "none" else "Swatch/None"
        s = _swatch(stroke) if stroke != "none" else "Swatch/None"
        swa = f' StrokeWeight="{_pt(sw)}"' if sw else ""
        self.items.append(
            f'<Rectangle Self="{rid}" FillColor="{f}" StrokeColor="{s}"{swa} '
            f'Layer="Layer/layer1" ItemTransform="1 0 0 1 {_pt(x)} {_pt(y)}">'
            f'{_rect_geom(_pt(x), _pt(y), _pt(w), _pt(h))}</Rectangle>')

    def add_photo(self, x, y, w, h):
        rid = self.uid("photo")
        iid = rid + "_img"
        lid = rid + "_link"
        self.items.append(
            f'<Rectangle Self="{rid}" FillColor="Swatch/None" StrokeColor="Swatch/None" '
            f'Layer="Layer/layer1" ItemTransform="1 0 0 1 {_pt(x)} {_pt(y)}">'
            f'{_rect_geom(_pt(x), _pt(y), _pt(w), _pt(h))}'
            f'<Image Self="{iid}" Layer="Layer/layer1"><Properties>'
            f'<Profile type="string">$ID/</Profile>'
            f'<GraphicBounds Left="0" Top="0" Right="{_pt(w)}" Bottom="{_pt(h)}"/>'
            f'</Properties><Link Self="{lid}" Name="{PHOTO}" '
            f'LinkResourceURI="Links/{PHOTO}" LinkClassID="104907"/>'
            f'</Image></Rectangle>')


def _rect_geom(x, y, w, h):
    pts = [(x, y), (f"{float(x)+float(w):.2f}".rstrip("0").rstrip("."), y),
           (f"{float(x)+float(w):.2f}".rstrip("0").rstrip("."), f"{float(y)+float(h):.2f}".rstrip("0").rstrip(".")),
           (x, f"{float(y)+float(h):.2f}".rstrip("0").rstrip("."))]
    inner = "".join(
        f'<PathPointType Anchor="{a} {b}" LeftDirection="{a} {b}" RightDirection="{a} {b}"/>'
        for a, b in pts)
    return ("<Properties><PathGeometry><GeometryPathType PathOpen=\"false\">"
            f"<PathPointArray>{inner}</PathPointArray>"
            "</GeometryPathType></PathGeometry></Properties>")


def render_idml(layout):
    d = IDMLDoc(layout)
    for el in layout["elements"]:
        k = el[0]
        if k == "frame":
            d.add_rect(0, 0, layout["w"], layout["h"], fill="none",
                       stroke=RED, sw=el[1])
        elif k == "lockup":
            _, x, y, n_size, name_size = el
            d.add_text(x, y, "N", n_size, 900, RED, fixed=True)
            d.add_text(x + n_size * 1.15, y - n_size * 0.62 + name_size * 0.8,
                       ["Northeastern University", "Software Engineering",
                        "and Information Systems"], name_size, 700, BLACK, fixed=True)
        elif k == "qr":
            _, x, y, s = el
            d.add_rect(x, y, s, s, fill="none", stroke=BLACK, sw=3)
            d.add_text(x, y + s / 2 + 5, "QR CODE", 14, 700, BLACK)
        elif k == "text":
            _, x, y, ls_, size, weight, fill, ls = el[:8]
            fixed = el[8] if len(el) > 8 else False
            d.add_text(x, y, ls_, size, weight, fill, ls=ls, fixed=fixed)
        elif k == "vtext":
            _, cx, cy, s, size, fill, ls = el
            st = d.style(700, size, fill, align="Center", ls=ls)
            sid = d.uid("Story")
            tf = d.uid("tf")
            d.stories.append((sid, st, [("t", s)]))
            # local box (0,0,textlen,bandw); matrix maps (x,y)->(y+tx,-x+ty)
            textlen = len(s) * (size * 0.60 + ls)
            tx = cx - size * 0.9
            ty = cy + textlen / 2
            d.items.append(
                f'<!-- FIXED: Teams label -->'
                f'<TextFrame Self="{tf}" ParentStory="{sid}" PreviousTextFrame="n" '
                f'NextTextFrame="n" Layer="Layer/layer1" '
                f'ItemTransform="0 -1 1 0 {_pt(tx)} {_pt(ty)}">'
                f'{_rect_geom("0", "0", _pt(textlen), _pt(size*1.8))}'
                f'<TextFramePreference/></TextFrame>')
        elif k == "photo":
            _, x, y, w_, h_ = el
            d.add_photo(x, y, w_, h_)
        elif k == "rect":
            _, x, y, w_, h_, fill, stroke, sw = el
            d.add_rect(x, y, w_, h_, fill=fill, stroke=stroke, sw=sw)
        elif k == "line":
            _, x1, y1, x2, y2, sw, color = el
            d.add_rect(min(x1, x2), min(y1, y2) - sw / 2, abs(x2 - x1), sw, fill=color)
        elif k == "dateblock":
            _, x, y, date, time, size = el
            bw = max(len(date), len(time)) * size * 0.62 + 36
            d.add_rect(x, y, bw, size + 22, fill=BLACK)
            d.add_text(x + 18, y + size + 4, date, size, 800, WHITE, ls=1)
            y2 = y + size + 34
            d.add_rect(x, y2, bw, size + 18, fill="none", stroke=BLACK, sw=3)
            d.add_text(x + 18, y2 + size + 2, time, size, 800, BLACK)

    name = layout["name"]
    files = {}
    files["META-INF/container.xml"] = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">'
        '<rootfiles><rootfile full-path="designmap.xml" '
        'media-type="application/vnd.adobe.indesign-idml-package"/>'
        '</rootfiles></container>')
    story_refs = "\n".join(
        f'<idPkg:Story src="Stories/{s}.xml"/>' for s, _, _ in d.stories)
    files["designmap.xml"] = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        f'<Document xmlns:idPkg="{IDPKG}" DOMVersion="16.0" Self="d" '
        f'Name="poster-{name}" ZeroPoint="0 0" ActiveLayer="Layer/layer1">'
        '<Color Self="Color/nuRed" Model="Process" Space="RGB" '
        'ColorValue="193 41 37" ColorOverride="Normal"/>'
        '<Color Self="Color/nuBlack" Model="Process" Space="CMYK" '
        'ColorValue="0 0 0 100" ColorOverride="Normal"/>'
        '<Color Self="Color/Paper" Model="Process" Space="CMYK" '
        'ColorValue="0 0 0 0" ColorOverride="Normal"/>'
        '<Swatch Self="Swatch/None" Name="None"/>'
        '<Swatch Self="Swatch/nuRed" Name="NU Red" Color="Color/nuRed"/>'
        '<Swatch Self="Swatch/nuBlack" Name="NU Black" Color="Color/nuBlack"/>'
        '<Swatch Self="Swatch/Paper" Name="Paper" Color="Color/Paper"/>'
        '<Layer Self="Layer/layer1" Name="Layer 1" Visible="true" Locked="false"/>'
        '<Section Self="Section/1" Name="" Length="1" PageStart="n"/>'
        f'<DocumentPreference PageWidth="{d.pw}" PageHeight="{d.ph}" '
        'FacingPages="false" PageBinding="LeftToRight"/>'
        '<idPkg:Spread src="Spreads/Spread_1.xml"/>\n'
        f'{story_refs}\n'
        '<idPkg:BackingStory src="BackingStory.xml"/>'
        '<idPkg:Preferences src="Resources/Preferences.xml"/>'
        '<idPkg:Fonts src="Resources/Fonts.xml"/>'
        '<idPkg:Styles src="Resources/Styles.xml"/>'
        '<idPkg:Graphic src="Resources/Graphic.xml"/>'
        '</Document>')
    files["Resources/Styles.xml"] = (
        f'<idPkg:Styles xmlns:idPkg="{IDPKG}" DOMVersion="13.0">'
        + "\n".join(d.style_defs) + '</idPkg:Styles>')
    files["Resources/Fonts.xml"] = (
        f'<idPkg:Fonts xmlns:idPkg="{IDPKG}" DOMVersion="13.0">'
        '<FontFamily Self="FontFamily/Arial" Name="Arial">'
        '<Font Self="Font/ArialRegular" Name="Arial" FontFamily="Arial" '
        'FontStyleName="Regular" FontType="OpenTypeCFF"/>'
        '<Font Self="Font/ArialBold" Name="Arial Bold" FontFamily="Arial" '
        'FontStyleName="Bold" FontType="OpenTypeCFF"/></FontFamily>'
        '<FontFamily Self="FontFamily/ArialBlack" Name="Arial Black">'
        '<Font Self="Font/ArialBlack" Name="Arial Black" FontFamily="Arial Black" '
        'FontStyleName="Regular" FontType="OpenTypeCFF"/></FontFamily>'
        '</idPkg:Fonts>')
    files["Resources/Graphic.xml"] = f'<idPkg:Graphic xmlns:idPkg="{IDPKG}" DOMVersion="8.0"/>'
    files["Resources/Preferences.xml"] = f'<idPkg:Preferences xmlns:idPkg="{IDPKG}" DOMVersion="13.0"/>'
    page = (f'<Page Self="Page/1" Name="1" GeometricBounds="0 0 {d.ph} {d.pw}" '
            f'ItemTransform="1 0 0 1 0 0"><MarginPreference ColumnCount="1" '
            f'ColumnGutter="12" Top="36" Bottom="36" Inside="36" Outside="36"/></Page>')
    files["Spreads/Spread_1.xml"] = (
        f'<idPkg:Spread xmlns:idPkg="{IDPKG}" DOMVersion="13.0">'
        f'<Spread Self="Spread/1" FlattenerOverride="Default">{page}'
        + "".join(d.items) + '</Spread></idPkg:Spread>')
    for sid, st, segs in d.stories:
        inner = []
        for kind, val in segs:
            inner.append("<Br/>" if kind == "br" else f"<Content>{esc(val)}</Content>")
        files[f"Stories/{sid}.xml"] = (
            f'<idPkg:Story xmlns:idPkg="{IDPKG}" DOMVersion="13.0">'
            f'<Story Self="{sid}" AppliedTOCStyle="n" TrackChanges="false" StoryTitle="$ID/">'
            f'<ParagraphStyleRange AppliedParagraphStyle="ParagraphStyle/{st}">'
            f'<CharacterStyleRange AppliedCharacterStyle="CharacterStyle/$ID/NormalCharacterStyle">'
            + "".join(inner) + '</CharacterStyleRange></ParagraphStyleRange>'
            '</Story></idPkg:Story>')
    files["BackingStory.xml"] = (
        f'<idPkg:BackingStory xmlns:idPkg="{IDPKG}" DOMVersion="13.0">'
        '<BackingStory Self="$ID/BackingStory" AppliedTOCStyle="n" '
        'TrackChanges="false" StoryTitle="$ID/"/></idPkg:BackingStory>')

    for path, content in files.items():
        try:
            xml.dom.minidom.parseString(content.encode("utf-8"))
        except Exception as e:
            raise SystemExit(f"XML error in {name}/{path}: {e}")

    idml_path = os.path.join(OUT, f"poster-{name}.idml")
    with zipfile.ZipFile(idml_path, "w") as z:
        z.writestr("mimetype", "application/vnd.adobe.indesign-idml-package",
                   compress_type=zipfile.ZIP_STORED)
        for path, content in files.items():
            z.writestr(path, content.encode("utf-8"), compress_type=zipfile.ZIP_DEFLATED)
        photo_src = os.path.join(OUT, PHOTO)
        if os.path.exists(photo_src):
            z.write(photo_src, f"Links/{PHOTO}", compress_type=zipfile.ZIP_DEFLATED)
    return idml_path, len(d.stories)


# ------------------------------------------------------------------ main ----
if __name__ == "__main__":
    for fn in layouts.ALL:
        layout = fn()
        layouts.verify_layout(layout)
        name = layout["name"]
        html = render_html(layout)
        with open(os.path.join(OUT, f"template-{name}.html"), "w") as f:
            f.write(html)
        svg = render_svg(layout)
        xml.dom.minidom.parseString(svg.encode("utf-8"))  # validate
        with open(os.path.join(OUT, f"poster-{name}.svg"), "w") as f:
            f.write(svg)
        idml_path, nstories = render_idml(layout)
        print(f"{name}: html + svg + idml ({nstories} stories) OK")
    print("done.")
