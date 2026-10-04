#!/usr/bin/env python3
"""build_idml.py — Generate an InDesign IDML package (zipped XML) for the
Northeastern Guest Speaker Series letter-size template.

IDML is Adobe's documented XML interchange format: InDesign CS4+ opens it
natively with fully editable text, styles, colors, and placed images.

Caveat: no InDesign on this machine, so this was validated for XML
well-formedness and package structure only. If InDesign complains about a
specific element (e.g. the image link or the rotated Teams label), report
the message and the package will be fixed.
"""
import os
import shutil
import zipfile
import xml.dom.minidom

OUT = os.path.dirname(os.path.abspath(__file__))
PKG = "poster-letter.idml"
IDPKG = "http://ns.adobe.com/AdobeInDesign/idml/1.0/packaging"

RED = (193, 41, 37)

# EDIT: change these for each event.
EVENT_TITLE = "Fearless Genius"
EVENT_DESC = "A conversation on Silicon Valley, creativity, and technological change."
EVENT_DATE = "SATURDAY, OCT. 10, 2026"
EVENT_TIME = "12:00\u20131:30 PM ET"
SPEAKER = "Doug Menuez"
SPEAKER_ROLE_1 = "Documentary Photographer"
SPEAKER_ROLE_2 = "Author of Fearless Genius"
COURSE = "INFO 7375: Branding & AI"
HOSTS = "Prof. Nina Harris and Prof. Nik Bear Brown"
PHOTO_FILE = "doug-menuez.png"


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;")
             .replace(">", "&gt;").replace('"', "&quot;"))


_uid = [0]


def uid(prefix):
    _uid[0] += 1
    return f"{prefix}{_uid[0]}"


# ---------------------------------------------------------------- geometry --
def rect_points(x, y, w, h):
    pts = [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]
    inner = "\n".join(
        f'<PathPointType Anchor="{a} {b}" LeftDirection="{a} {b}" RightDirection="{a} {b}"/>' for a, b in pts)
    return ("<Properties><PathGeometry><GeometryPathType PathOpen=\"false\">"
            f"<PathPointArray>{inner}</PathPointArray>"
            "</GeometryPathType></PathGeometry></Properties>")


def rectangle(self_id, x, y, w, h, fill="Swatch/None", stroke="Swatch/None",
              stroke_w=0, layer="Layer/layer1", extra=""):
    sw = f' StrokeWeight="{stroke_w}"' if stroke_w else ""
    return (f'<Rectangle Self="{self_id}" FillColor="{fill}" StrokeColor="{stroke}"{sw} '
            f'Layer="{layer}" ItemTransform="1 0 0 1 {x} {y}">{rect_points(x, y, w, h)}{extra}</Rectangle>')


STORIES = []  # (story_id, style, [("t", text) | ("br",)])


def text_frame(self_id, x, y, w, h, story_id, style, segments, transform=None):
    STORIES.append((story_id, style, segments))
    tr = transform if transform else f"1 0 0 1 {x} {y}"
    return (f'<TextFrame Self="{self_id}" ParentStory="{story_id}" PreviousTextFrame="n" '
            f'NextTextFrame="n" Layer="Layer/layer1" ItemTransform="{tr}">'
            f"{rect_points(x, y, w, h)}<TextFramePreference/></TextFrame>")


def story_xml(story_id, style, segments):
    body = []
    for seg in segments:
        if seg[0] == "br":
            body.append("<Br/>")
        else:
            body.append(f"<Content>{esc(seg[1])}</Content>")
    return (f'<idPkg:Story xmlns:idPkg="{IDPKG}" DOMVersion="13.0">'
            f'<Story Self="{story_id}" AppliedTOCStyle="n" TrackChanges="false" StoryTitle="$ID/">'
            f'<ParagraphStyleRange AppliedParagraphStyle="ParagraphStyle/{style}">'
            f'<CharacterStyleRange AppliedCharacterStyle="CharacterStyle/$ID/NormalCharacterStyle">'
            f'{"".join(body)}</CharacterStyleRange></ParagraphStyleRange>'
            f"</Story></idPkg:Story>")


# ------------------------------------------------------------------ styles --
def styles_xml():
    def ps(name, font, fstyle, size, leading=None, fill="Swatch/nuBlack",
           align="Left", space_after=0):
        ld = f'<Leading type="unit">{leading}</Leading>' if leading else ""
        return (f'<ParagraphStyle Self="ParagraphStyle/{name}" Name="{name}">'
                f"<Properties><AppliedFont type=\"string\">{font}</AppliedFont>"
                f"<FontStyle type=\"string\">{fstyle}</FontStyle>"
                f"<PointSize type=\"unit\">{size}</PointSize>{ld}"
                f"<FillColor type=\"string\">{fill}</FillColor>"
                f"<Justification type=\"enumeration\">{align}</Justification>"
                f"<SpaceAfter type=\"unit\">{space_after}</SpaceAfter>"
                "</Properties></ParagraphStyle>")

    styles = "\n".join([
        ps("series", "Arial Black", "Regular", 68, 64),
        ps("eventtitle", "Arial Black", "Regular", 38, 40),
        ps("desc", "Arial", "Regular", 13.5, 17),
        ps("datetext", "Arial", "Bold", 18, 20, fill="Swatch/Paper"),
        ps("timetext", "Arial", "Bold", 18, 20),
        ps("speaker", "Arial Black", "Regular", 22, 24),
        ps("role", "Arial", "Regular", 12.5, 15),
        ps("nlogo", "Arial Black", "Regular", 44, 44, fill="Swatch/nuRed"),
        ps("lockup", "Arial", "Bold", 12.5, 15),
        ps("teamstext", "Arial", "Bold", 12, 14, fill="Swatch/Paper", align="Center"),
        ps("qrtext", "Arial", "Bold", 10, 12, align="Center"),
        ps("course", "Arial", "Bold", 11, 13),
        ps("footer", "Arial", "Regular", 10.5, 13),
    ])
    return (f'<idPkg:Styles xmlns:idPkg="{IDPKG}" DOMVersion="13.0">{styles}'
            "</idPkg:Styles>")


def fonts_xml():
    return (f'<idPkg:Fonts xmlns:idPkg="{IDPKG}" DOMVersion="13.0">'
            '<FontFamily Self="FontFamily/Arial" Name="Arial">'
            '<Font Self="Font/ArialRegular" Name="Arial" FontFamily="Arial" FontStyleName="Regular" FontType="OpenTypeCFF"/>'
            '<Font Self="Font/ArialBold" Name="Arial Bold" FontFamily="Arial" FontStyleName="Bold" FontType="OpenTypeCFF"/>'
            "</FontFamily>"
            '<FontFamily Self="FontFamily/ArialBlack" Name="Arial Black">'
            '<Font Self="Font/ArialBlack" Name="Arial Black" FontFamily="Arial Black" FontStyleName="Regular" FontType="OpenTypeCFF"/>'
            "</FontFamily></idPkg:Fonts>")


def graphic_xml():
    return (f'<idPkg:Graphic xmlns:idPkg="{IDPKG}" DOMVersion="8.0" Self="d"/>'
            .replace(' Self="d"/>', '/>'))


def prefs_xml():
    return (f'<idPkg:Preferences xmlns:idPkg="{IDPKG}" DOMVersion="13.0" Self="d"/>'
            .replace(' Self="d"/>', '/>'))


def backing_story_xml():
    return (f'<idPkg:BackingStory xmlns:idPkg="{IDPKG}" DOMVersion="13.0">'
            '<BackingStory Self="$ID/BackingStory" AppliedTOCStyle="n" '
            'TrackChanges="false" StoryTitle="$ID/"/></idPkg:BackingStory>')


def container_xml():
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
            '<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">'
            "<rootfiles><rootfile full-path=\"designmap.xml\" "
            'media-type="application/vnd.adobe.indesign-idml-package"/>'
            "</rootfiles></container>")


# ---------------------------------------------------------------- designmap -
def designmap_xml(story_ids):
    stories = "\n".join(f'<idPkg:Story src="Stories/{s}.xml"/>' for s in story_ids)
    return (f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
            f'<Document xmlns:idPkg="{IDPKG}" DOMVersion="16.0" Self="d" Name="poster-letter" '
            'ZeroPoint="0 0" ActiveLayer="Layer/layer1">'
            '<Color Self="Color/nuRed" Model="Process" Space="RGB" ColorValue="193 41 37" ColorOverride="Normal"/>'
            '<Color Self="Color/nuBlack" Model="Process" Space="CMYK" ColorValue="0 0 0 100" ColorOverride="Normal"/>'
            '<Color Self="Color/Paper" Model="Process" Space="CMYK" ColorValue="0 0 0 0" ColorOverride="Normal"/>'
            '<Swatch Self="Swatch/None" Name="None"/>'
            '<Swatch Self="Swatch/nuRed" Name="NU Red" Color="Color/nuRed"/>'
            '<Swatch Self="Swatch/nuBlack" Name="NU Black" Color="Color/nuBlack"/>'
            '<Swatch Self="Swatch/Paper" Name="Paper" Color="Color/Paper"/>'
            '<Layer Self="Layer/layer1" Name="Layer 1" Visible="true" Locked="false"/>'
            '<Section Self="Section/1" Name="" Length="1" PageStart="n"/>'
            '<DocumentPreference PageWidth="612" PageHeight="792" FacingPages="false" '
            'PageBinding="LeftToRight" BleedInside="0" BleedOutside="0"/>'
            '<idPkg:Spread src="Spreads/Spread_1.xml"/>'
            f"{stories}"
            '<idPkg:BackingStory src="BackingStory.xml"/>'
            '<idPkg:Preferences src="Resources/Preferences.xml"/>'
            '<idPkg:Fonts src="Resources/Fonts.xml"/>'
            '<idPkg:Styles src="Resources/Styles.xml"/>'
            '<idPkg:Graphic src="Resources/Graphic.xml"/>'
            "</Document>")


# ------------------------------------------------------------------- spread -
def spread_xml(items):
    page = ('<Page Self="Page/1" Name="1" GeometricBounds="0 0 792 612" '
            'ItemTransform="1 0 0 1 0 0">'
            '<MarginPreference ColumnCount="1" ColumnGutter="12" Top="36" Bottom="36" '
            'Inside="36" Outside="36" Pin="0"/>'
            "</Page>")
    return (f'<idPkg:Spread xmlns:idPkg="{IDPKG}" DOMVersion="13.0">'
            f"<Spread Self=\"Spread/1\" FlattenerOverride=\"Default\" "
            f"ShowMasterItems=\"true\">{page}{''.join(items)}</Spread></idPkg:Spread>")


def build_items():
    items = []
    A = items.append
    # red frame
    A(rectangle("frame", 0, 0, 612, 792, fill="Swatch/None",
                stroke="Swatch/nuRed", stroke_w=19.5))
    # masthead: N logo + lockup (FIXED)
    A(text_frame("tf_n", 42, 42, 60, 60, "Story_n", "nlogo", [("t", "N")]))
    A(text_frame("tf_lockup", 108, 44, 220, 66, "Story_lockup", "lockup",
                 [("t", "Northeastern University"), ("br",),
                  ("t", "Software Engineering"), ("br",),
                  ("t", "and Information Systems")]))
    # QR placeholder (EDIT)
    A(rectangle("qr_box", 460, 42, 110, 110, fill="Swatch/None",
                stroke="Swatch/nuBlack", stroke_w=1.5))
    A(text_frame("tf_qr", 460, 78, 110, 40, "Story_qr", "qrtext",
                 [("t", "QR CODE")]))
    # series headline (FIXED)
    A(text_frame("tf_series", 40, 118, 530, 205, "Story_series", "series",
                 [("t", "Guest"), ("br",), ("t", "Speaker"), ("br",), ("t", "Series")]))
    # photo band: image + red vertical label (photo EDIT, label FIXED)
    img_id = "photo1"
    A(f'<Rectangle Self="{img_id}" FillColor="Swatch/None" StrokeColor="Swatch/None" '
       f'Layer="Layer/layer1" ItemTransform="1 0 0 1 40 330">'
       f"{rect_points(40, 330, 340, 160)}"
       f'<Image Self="{img_id}_img" Layer="Layer/layer1">'
       "<Properties><Profile type=\"string\">$ID/</Profile>"
       '<GraphicBounds Left="0" Top="0" Right="340" Bottom="160"/>'
       '<VisibleBounds Left="0" Top="0" Right="340" Bottom="160"/>'
       "</Properties>"
       f'<Link Self="{img_id}_link" Name="{PHOTO_FILE}" '
       f'LinkResourceURI="Links/{PHOTO_FILE}" LinkClassID="104907"/>'
       "</Image></Rectangle>")
    A(rectangle("teamsband", 390, 330, 40, 160, fill="Swatch/nuRed"))
    # vertical label, rotated -90deg: local box (0,0,160,40), matrix "0 -1 1 0 tx ty"
    # (x,y) -> (y+tx, -x+ty); want x in [390,430], y in [330,490]
    A(text_frame("tf_teams", 0, 0, 160, 40, "Story_teams", "teamstext",
                 [("t", "LIVE ON MICROSOFT TEAMS")],
                 transform="0 -1 1 0 390 490"))
    # event title / desc (EDIT)
    A(text_frame("tf_title", 40, 500, 530, 50, "Story_title", "eventtitle",
                 [("t", EVENT_TITLE)]))
    A(text_frame("tf_desc", 40, 548, 530, 40, "Story_desc", "desc",
                 [("t", EVENT_DESC)]))
    # date block (EDIT)
    A(rectangle("datebg", 40, 592, 320, 30, fill="Swatch/nuBlack"))
    A(text_frame("tf_date", 50, 594, 310, 28, "Story_date", "datetext",
                 [("t", EVENT_DATE)]))
    A(rectangle("timebg", 40, 628, 220, 28, fill="Swatch/None",
                stroke="Swatch/nuBlack", stroke_w=2))
    A(text_frame("tf_time", 50, 630, 210, 26, "Story_time", "timetext",
                 [("t", EVENT_TIME)]))
    # speaker (EDIT)
    A(text_frame("tf_speaker", 40, 664, 400, 30, "Story_speaker", "speaker",
                 [("t", SPEAKER)]))
    A(text_frame("tf_role", 40, 694, 400, 34, "Story_role", "role",
                 [("t", SPEAKER_ROLE_1), ("br",), ("t", SPEAKER_ROLE_2)]))
    # footer rule + course/host (EDIT) + SEIS (FIXED)
    A(f'<Rectangle Self="footrule" FillColor="Swatch/nuBlack" StrokeColor="Swatch/None" '
       f'Layer="Layer/layer1" ItemTransform="1 0 0 1 40 736">{rect_points(40, 736, 532, 2)}</Rectangle>')
    A(text_frame("tf_course", 40, 742, 360, 18, "Story_course", "course",
                 [("t", COURSE)]))
    A(text_frame("tf_hosts", 40, 758, 360, 16, "Story_hosts", "footer",
                 [("t", HOSTS)]))
    A(text_frame("tf_seis", 410, 742, 162, 18, "Story_seis", "footer",
                 [("t", "Open to the SEIS community")]))
    return items


def main():
    global STORIES
    STORIES = []
    items = build_items()
    story_ids = [s for s, _, _ in STORIES]

    files = {
        "META-INF/container.xml": container_xml(),
        "designmap.xml": designmap_xml(story_ids),
        "Resources/Styles.xml": styles_xml(),
        "Resources/Fonts.xml": fonts_xml(),
        "Resources/Graphic.xml": graphic_xml(),
        "Resources/Preferences.xml": prefs_xml(),
        "Spreads/Spread_1.xml": spread_xml(items),
        "BackingStory.xml": backing_story_xml(),
    }
    for s, style, segs in STORIES:
        files[f"Stories/{s}.xml"] = story_xml(s, style, segs)

    # validate XML before zipping
    for path, content in files.items():
        try:
            xml.dom.minidom.parseString(content.encode("utf-8"))
        except Exception as e:
            raise SystemExit(f"XML error in {path}: {e}")

    idml_path = os.path.join(OUT, PKG)
    if os.path.exists(idml_path):
        os.remove(idml_path)
    with zipfile.ZipFile(idml_path, "w") as z:
        z.writestr("mimetype", "application/vnd.adobe.indesign-idml-package",
                   compress_type=zipfile.ZIP_STORED)
        for path, content in files.items():
            z.writestr(path, content.encode("utf-8"),
                       compress_type=zipfile.ZIP_DEFLATED)
        photo_src = os.path.join(OUT, PHOTO_FILE)
        if os.path.exists(photo_src):
            z.write(photo_src, f"Links/{PHOTO_FILE}",
                    compress_type=zipfile.ZIP_DEFLATED)
    print("wrote", idml_path, f"({len(story_ids)} stories)")

    # verify zip integrity
    with zipfile.ZipFile(idml_path) as z:
        bad = z.testzip()
        names = z.namelist()
    print("zip OK" if bad is None else f"zip BAD: {bad}")
    print(len(names), "entries; has Links:",
          any(n.startswith("Links/") for n in names))


if __name__ == "__main__":
    main()
