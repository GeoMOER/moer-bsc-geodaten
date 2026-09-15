#!/usr/bin/python3
"""Build the Unit 10 classroom deck with LibreOffice UNO (no downloads).

Run with /usr/bin/python3, which provides the distro's python3-uno package.
Text, tables and diagrams remain editable PowerPoint shapes.
"""
from pathlib import Path
import math
import subprocess
import tempfile
import time
import uuid
from zipfile import ZipFile
import uno
from com.sun.star.awt import Point, Size
from com.sun.star.beans import PropertyValue

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[1]
W, H = 33867, 19050
SCALE = W / 1600
INK, TEAL, ORANGE = 0x000000, 0x004899, 0xA32123
BG, WHITE, PALE, GRID = 0xFFFFFF, 0xFFFFFF, 0xEAF5F7, 0xA6D9E2
MUTED = 0x414141
FONT = 'Noto Sans'
TEMPLATE = ROOT/'slides/Vorlagen/präs_ms02_powerpoint_de.pptx'
FB19 = ROOT/'slides/Vorlagen/fb19-praesentationsvorlage_16-9-format.pot'
FB19_IMAGE = OUT/'assets/fb19-marburg-europa.png'
PACKAGE = ROOT/'assets/data/marburg/marburg_geodaten.zip'
WMS_IMAGE = OUT/'assets/wms_schutzgebiete.png'
PACKAGE = ROOT/'assets/data/marburg/marburg_geodaten.zip'
WMS_IMAGE = OUT/'assets/wms_schutzgebiete.png'
COURSE = 'https://geomoer.github.io/moer-bsc-geodaten/unit10/'
QDOC = 'https://docs.qgis.org/3.40/en/docs/user_manual/'
HLNUG = 'https://www.hlnug.de/themen/geografische-informationssysteme/geodienste/naturschutz'
WMS_URL = 'https://geodienste-umwelt.hessen.de/arcgis/services/inspire/schutzgebiete/MapServer/WmsServer'
RECORDS = []


def prop(name, value):
    return PropertyValue(Name=name, Value=value)


def enum(kind, value):
    return uno.Enum('com.sun.star.' + kind, value)


def box(page, x, y, w, h, fill=WHITE, stroke=None, ellipse=False):
    sh = DOC.createInstance('com.sun.star.drawing.' + ('EllipseShape' if ellipse else 'RectangleShape'))
    page.add(sh)
    sh.Position = Point(round(x * SCALE), round(y * SCALE))
    sh.Size = Size(round(w * SCALE), round(h * SCALE))
    sh.FillStyle = enum('drawing.FillStyle', 'NONE' if fill is None else 'SOLID')
    if fill is not None:
        sh.FillColor = fill
    sh.LineStyle = enum('drawing.LineStyle', 'NONE' if stroke is None else 'SOLID')
    if stroke is not None:
        sh.LineColor = stroke
        sh.LineWidth = 45
    return sh


def text(page, x, y, w, h, value, size=25, color=INK, bold=False, align='LEFT'):
    sh = DOC.createInstance('com.sun.star.drawing.TextShape')
    page.add(sh)
    sh.Position = Point(round(x * SCALE), round(y * SCALE))
    sh.Size = Size(round(w * SCALE), round(h * SCALE))
    sh.TextAutoGrowHeight = False
    sh.TextAutoGrowWidth = False
    sh.TextLeftDistance = sh.TextRightDistance = 0
    sh.TextUpperDistance = sh.TextLowerDistance = 0
    sh.TextVerticalAdjust = enum('drawing.TextVerticalAdjust', 'TOP')
    sh.String = value
    cur = sh.Text.createTextCursor()
    cur.gotoStart(False)
    cur.gotoEnd(True)
    cur.CharFontName = FONT
    cur.CharHeight = float(size) * 0.94
    cur.CharColor = color
    cur.CharWeight = 150.0 if bold else 100.0
    cur.ParaAdjust = enum('style.ParagraphAdjust', align)
    cur.ParaTopMargin = cur.ParaBottomMargin = 0
    return sh


def poly(page, points, color=TEAL, fill=None, width=45, closed=False):
    sh = DOC.createInstance('com.sun.star.drawing.' + ('PolyPolygonShape' if closed else 'PolyLineShape'))
    page.add(sh)
    sh.PolyPolygon = (tuple(Point(round(x * SCALE), round(y * SCALE)) for x, y in points),)
    sh.LineStyle = enum('drawing.LineStyle', 'SOLID')
    sh.LineColor = color
    sh.LineWidth = width
    sh.FillStyle = enum('drawing.FillStyle', 'NONE' if fill is None else 'SOLID')
    if fill is not None:
        sh.FillColor = fill
    return sh


def line(page, x1, y1, x2, y2, color=GRID, width=45):
    return poly(page, [(x1, y1), (x2, y2)], color, width=width)


def hyperlink(shape, url):
    field=DOC.createInstance('com.sun.star.text.TextField.URL')
    field.URL=url
    field.Representation=shape.String
    cur=shape.Text.createTextCursor()
    cur.gotoStart(False);cur.gotoEnd(True)
    shape.Text.insertTextContent(cur,field,True)


def picture(page, path, x, y, w, h):
    sh=DOC.createInstance('com.sun.star.drawing.GraphicObjectShape')
    page.add(sh)
    sh.Position=Point(round(x*SCALE),round(y*SCALE))
    sh.Size=Size(round(w*SCALE),round(h*SCALE))
    sh.GraphicURL=path.as_uri()
    return sh


def slide(title, section, start, end, notes, source='', reserve=False, kind='content'):
    n = len(RECORDS) + 1
    pages = DOC.getDrawPages()
    page = pages.getByIndex(0) if n == 1 else pages.insertNewByIndex(n - 1)
    for i in range(page.Count-1,-1,-1):
        sh=page.getByIndex(i)
        page.remove(sh)
    page.setMasterPage(MASTERS[{'title':'Titelfolie','closing':'Kontakt'}.get(kind,'Titel und Inhalt')])
    page.IsFooterVisible=False
    page.IsPageNumberVisible=False
    page.IsDateTimeVisible=False
    page.Width, page.Height = W, H
    page.Name = f'{n:02d} {title}'
    if kind == 'content':
        text(page, 100, 48, 1400, 114, title, 34, bold=True)
        text(page, 100, 173, 1400, 30, section.upper(), 12, TEAL, True)
        text(page, 100, 852, 1100, 30, 'Universität Marburg | Fachbereich 19 · Geographie | Geodaten · Unit 10', 10, MUTED)
        text(page,1512,850,42,25,str(n),10,INK,False,'CENTER')
    timing = ('Reserve; nicht zusätzlich in die 90 Minuten einplanen.' if reserve else
              'Titelfolie vor dem Einstieg zeigen.' if kind == 'title' else
              'Abschluss nach der Nachbereitung; kein zusätzlicher Zeitblock.' if kind == 'closing' else
              f'Zeitfenster: Minute {start}–{end} ({end-start} Minuten).')
    note_text = timing + '\n\n' + notes
    if source:
        note_text += '\n\nQuellen / Anschluss an die HTML-Lernumgebung:\n' + source
    np = page.getNotesPage()
    for i in range(np.Count):
        sh = np.getByIndex(i)
        if sh.ShapeType == 'com.sun.star.presentation.NotesShape':
            sh.String = note_text
    RECORDS.append(dict(number=n, title=title, section=section, start=start, end=end,
                        reserve=reserve, kind=kind, notes=note_text))
    return page


def band(page, value, y=724, fill=PALE, size=25):
    box(page, 85, y, 1430, 78, fill)
    text(page, 110, y + 14, 1380, 58, value, size, TEAL, True)


def card(page, x, y, w, h, label, body, color=TEAL, size=25):
    box(page, x, y, w, h, WHITE)
    box(page, x, y, 7, h, color)
    text(page, x + 27, y + 24, w - 54, 85, label, 27, color, True)
    body_top = 100 if h <= 230 else 124
    text(page, x + 27, y + body_top, w - 54, h - body_top - 18, body, size)


def steps(page, items, y=230, gap=150):
    for i, (label, body) in enumerate(items):
        yy = y + i * gap
        badge = str(i + 1)
        if label[:4] in ('A · ', 'B · ', 'C · '):
            badge, label = label[0], label[4:]
        box(page, 85, yy, 62, 62, TEAL, ellipse=True)
        text(page, 85, yy + 8, 62, 48, badge, 26, WHITE, True, 'CENTER')
        text(page, 180, yy, 1290, 55, label, 29, bold=True)
        if body:
            text(page, 180, yy + 62, 1280, 80, body, 24, MUTED)


def table(page, headers, rows, widths, y=235, row_h=86, size=24, colors=None, x0=85):
    for r, values in enumerate([headers] + rows):
        x = x0
        for j, (value, width) in enumerate(zip(values, widths)):
            fill = INK if r == 0 else (WHITE if r % 2 else PALE)
            box(page, x, y + r * row_h, width - 3, row_h - 3, fill)
            color = WHITE if r == 0 else (colors.get(r - 1, INK) if colors else INK)
            text(page, x + 18, y + r * row_h + 17, width - 36, row_h - 20,
                 value, size, color, r == 0)
            x += width


def landscape(page, x, y, w, h, mode='all'):
    """Schematic invented landscape, made from editable slide shapes."""
    box(page,x,y,w,h,PALE,GRID)
    if mode in ('all','polygon'):
        poly(page,[(x+w*.13,y+h*.14),(x+w*.72,y+h*.12),(x+w*.83,y+h*.66),
                   (x+w*.40,y+h*.87),(x+w*.10,y+h*.57)],TEAL,0xBFE0CC,35,True)
    if mode in ('all','line'):
        poly(page,[(x+w*.05,y+h*.72),(x+w*.29,y+h*.56),(x+w*.47,y+h*.60),
                   (x+w*.69,y+h*.30),(x+w*.95,y+h*.20)],TEAL,width=125)
    if mode in ('all','point'):
        for a,b in [(.20,.28),(.47,.37),(.72,.74)]:
            box(page,x+w*a-10,y+h*b-10,20,20,ORANGE,ellipse=True)


def raster(page,x,y,cell=64,classes=False):
    vals=[[210,214,219,224],[205,211,217,221],[201,207,213,218],[198,203,209,215]]
    colors=[0xEAF5F7,0xC8E8E3,0xA0D1C0,0x70B29C]
    for r,row in enumerate(vals):
        for c,v in enumerate(row):
            label=['W','W','A','S'][c] if classes else str(v)
            box(page,x+c*cell,y+r*cell,cell-2,cell-2,colors[c],GRID)
            text(page,x+c*cell,y+r*cell+cell*.25,cell-2,cell*.65,label,17,INK,False,'CENTER')


def build():
    model=COURSE+'unit10-01_datenmodelle.html'
    qgis=COURSE+'unit10-02_qgigs.html'
    sources=COURSE+'unit10-03_datenquellen.html'
    assignment=COURSE+'unit10-04_assignment.html'
    overview=COURSE+'unit10-00_overview.html'
    core='https://geomoer.github.io/moer-bsc-geodaten/material/qgis-kernpfade.html#unit10'

    p=slide('Geodatenmodelle, QGIS und Datenquellen','Unit 10',0,0,
        'Titelfolie beim Ankommen zeigen. Die Sitzung ist für 90 Minuten mit 100–150 Bachelor- und Lehramtsstudierenden ausgelegt. '
        'Vorbereitendes Lesen wird nicht vorausgesetzt. QGIS und das vollständig entpackte Marburger Übungspaket müssen vor Sitzungsbeginn verfügbar sein. '
        'Keine Installation oder freie Datensuche während des verbindlichen Präsenzwegs einplanen.',str(TEMPLATE),kind='title')
    picture(p,FB19_IMAGE,44,350,539,539*135/394)
    text(p,625,285,850,300,'Geodatenmodelle,\nQGIS und\nDatenquellen',44,WHITE)
    text(p,625,614,840,70,'Unit 10',28,WHITE)
    text(p,625,744,840,100,'Fachbereich 19 · Geographie\nPhilipps-Universität Marburg',19,WHITE)

    p=slide('JiTT · Rückblick auf Unit 09','Platzhalter · vollständig austauschbar',0,10,
        'VOR DEM TERMIN: Den gesamten Platzhalter durch die aktuelle JiTT-Auswertung zu Unit 09 ersetzen. '
        'Bei Bedarf die Folie duplizieren. Nur tatsächliche, zusammengefasste und anonymisierte Rückmeldungen einsetzen. '
        'Die gesamte Phase dauert zehn Minuten. Verständnisfragen zu Koordinaten, CRS oder Projektionen klären; keinen neuen Test daraus machen.')
    sh=box(p,100,237,1400,545,PALE,GRID)
    sh.Name='JiTT – vollständigen Block ersetzen'
    text(p,180,430,1240,130,'[Hier den vollständigen\nJiTT-Block einfügen]',38,TEAL,False,'CENTER')

    p=slide('Von Datenmodellen zum ersten QGIS-Projekt','Unit 10 · Orientierung',10,11,
        'Den roten Faden ankündigen: ein Modell passend zur Frage wählen, lokale Daten in QGIS prüfen und das Projekt so sichern, dass es wieder geöffnet werden kann. '
        'Der WMS folgt erst nach dem abgeschlossenen lokalen Kernpfad. Alle Studierenden bearbeiten dieselben Aufgaben.',overview)
    picture(p,ROOT/'assets/images/unit10/hero-unit10.jpg',85,225,1430,1430/6)
    for x,label,body in [(85,'Modell wählen','Vektor und Raster\nunterscheiden'),(570,'Projekt aufbauen','Layer und Datenquellen\nprüfen'),(1055,'Ergebnis sichern','Speichern, schließen\nund erneut öffnen')]:
        card(p,x,495,460,205,label,body,size=23)
    band(p,'Verbindliches Ergebnis: unit10_einstieg.qgz öffnet beide lokalen Layer.',size=22)

    p=slide('Zwei Modelle räumlicher Wirklichkeit','Datenmodelle · Vergleichen',11,14,
        'Die Abbildung aus der Kursseite gemeinsam lesen. Vektorfeatures modellieren einzelne Objekte mit Geometrien und Attributen. '
        'Raster teilen den Raum in Zellen mit Werten. Die Zuordnung ist keine starre Naturregel; Fragestellung, Maßstab und vorhandene Daten entscheiden.',
        model+'\nBild: assets/images/unit10/datenmodelle.svg')
    picture(p,ROOT/'assets/images/unit10/datenmodelle.svg',200,215,1200,600)

    p=slide('Vektor: Punkt, Linie und Polygon','Datenmodelle · Geometrien',14,16,
        'Punkt als Position, Linie als Verlauf und Polygon als Fläche erklären. Ein Punktsymbol besitzt auf dem Bildschirm eine sichtbare Größe; die Punktgeometrie selbst keine Fläche. '
        'Ein Fluss kann je nach Frage als Linie oder Polygon modelliert werden. Damit die Modellwahl an die benötigte Information binden.',model)
    for x,mode,label,desc in [(85,'point','Punkt','Position · Beobachtung'),(570,'line','Linie','Verlauf · Gewässer'),(1055,'polygon','Polygon','Fläche · Schutzgebiet')]:
        text(p,x,228,460,55,label,30,TEAL,True)
        landscape(p,x,305,460,280,mode)
        text(p,x,620,460,55,desc,25)
    band(p,'Die Fragestellung bestimmt Geometrietyp und Detailgrad.',size=24)

    p=slide('Raster: Zellen speichern Werte','Datenmodelle · Raster',16,18,
        'Links ein kontinuierliches Höhenraster, rechts ein kategoriales Landbedeckungsraster. Raster bedeutet regelmäßige Zellanordnung, nicht automatisch kontinuierliche Werte. '
        'Zellgröße, Ausdehnung, Einheit und NoData gehören zur Interpretation. Die Vertiefung folgt in Unit 13.',model)
    text(p,110,225,650,55,'Höhe in Metern',28,TEAL,True)
    raster(p,160,315,73)
    text(p,820,225,650,55,'Landbedeckung als Klasse',28,TEAL,True)
    raster(p,850,315,73,True)
    text(p,110,635,640,50,'Jede Zelle speichert einen Wert.',22)
    text(p,820,635,650,50,'W = Wald · A = Acker · S = Siedlung',21)
    band(p,'Kleine Zellen bedeuten mehr Details – nicht automatisch genauere Daten.',size=22)

    p=slide('Welches Modell passt zur Frage?','Gemeinsam auswählen',18,20,
        '30 Sekunden allein entscheiden, eine Minute zu zweit begründen, anschließend drei kurze Antworten sammeln. '
        'Gefragt sind Datenmodell und gegebenenfalls Geometrietyp. Die Lösung folgt auf der nächsten Folie.',model)
    steps(p,[('A · Grenze eines Schutzgebiets','Welche räumliche Information benötigen Sie?'),
             ('B · Geländehöhe im gesamten Ausschnitt','Ein Wert soll an jedem Ort vorliegen.'),
             ('C · Fundorte einzelner Feuersalamander','Jede Beobachtung besitzt eine Position.')])
    band(p,'Modell nennen – und mit der benötigten Information begründen.',size=23)

    p=slide('Die benötigte Information entscheidet','Auflösung · Datenmodelle',20,22,
        'A: Polygonvektor beschreibt Fläche und Grenze. B: kontinuierliches Raster beschreibt ein flächendeckendes Höhenfeld. C: Punktvektor beschreibt einzelne Fundorte. '
        'Andere Modellierungen sind möglich, wenn eine andere Frage oder Datengrundlage genannt wird.',model)
    steps(p,[('A · Polygonvektor','Schutzgebietsfläche und Grenze'),
             ('B · kontinuierliches Raster','Höhenwert je Rasterzelle'),
             ('C · Punktvektor','Position je Beobachtung')])
    band(p,'Nicht der Name des Phänomens, sondern Frage und Datengrundlage entscheiden.',size=21)

    p=slide('Projekt, Layer und Datenquelle','QGIS · Begriffe unterscheiden',22,26,
        'Die Abbildung aus der Kursseite erläutern. Das QGIS-Projekt speichert Arbeitsstand und Verweise. Layer sind die im Projekt verwendeten Informationsebenen. '
        'Die eigentlichen Daten kommen aus lokalen Dateien oder Webdiensten. Eine qgz-Datei enthält diese Daten normalerweise nicht vollständig.',
        qgis+'\nBild: assets/images/unit10/projekt-layer-datei.svg\n'+QDOC+'introduction/project_files.html')
    picture(p,ROOT/'assets/images/unit10/projekt-layer-datei.svg',210,215,1180,507)
    band(p,'Projektdatei und Geodatendateien gehören zusammen – sind aber nicht dasselbe.',size=21)

    p=slide('Warum fehlen die Layer?','Abstimmung · Projekt weitergeben',26,28,
        '30 Sekunden allein entscheiden, dann A, B oder C per Handzeichen. Nur die Projektdatei wurde kopiert; auf dem ursprünglichen Rechner waren alle Layer sichtbar. '
        'Die Dateien wurden nicht durch QGIS gelöscht. Die Lösung folgt auf der nächsten Folie.',qgis)
    text(p,110,220,1380,110,'Sie kopieren nur unit10_einstieg.qgz.\nAuf dem anderen Rechner fehlen die Layer.',29,bold=True)
    steps(p,[('A · Die qgz-Datei enthält automatisch alle Daten.',''),
             ('B · Die gespeicherten Datenpfade sind nicht erreichbar.',''),
             ('C · QGIS hat beim Kopieren die Geometrien gelöscht.','')],y=385,gap=100)
    band(p,'A, B oder C? Begründen Sie Ihre Wahl.',size=24)

    p=slide('Projekt und Daten gemeinsam erhalten','Auflösung · Dateipfade',28,30,
        'B ist richtig. Die Projektdatei verweist auf Datendateien. Deshalb den vollständig entpackten Arbeitsordner mit stabiler Struktur verwenden. '
        'Relative Pfade erleichtern eine Übertragung, ersetzen die Dateien aber nicht. Das erneute Öffnen ist die entscheidende Kontrolle.',qgis)
    steps(p,[('B · Die Quellen sind nicht erreichbar.','Das Projekt speichert Verweise auf Speicherorte.'),
             ('Arbeitsordner zusammenhalten','data_raw, documentation und Projekt nicht getrennt verschieben.'),
             ('Projekt erneut öffnen','Beide Layer müssen ohne Pfadreparatur erreichbar sein.')])
    band(p,'Speichern allein genügt nicht: Wiederöffnen und kontrollieren.',size=24)

    p=slide('Die wichtigsten Bereiche in QGIS','QGIS · Orientierung',30,33,
        'Die schematische QGIS-3.40-Ansicht aus der Kursseite zeigen. Browser, Layer-Bereich, Kartenansicht und Statusleiste finden lassen. '
        'Die genaue Position von Symbolen kann je nach Betriebssystem und persönlicher Konfiguration abweichen. Nur die heute benötigten Bereiche erklären.',
        qgis+'\nBild: assets/images/unit10/qgis-oberflaeche.svg\n'+QDOC+'introduction/qgis_gui.html')
    picture(p,ROOT/'assets/images/unit10/qgis-oberflaeche.svg',275,210,1050,588)

    p=slide('Unser verbindlicher Praxisweg','Praxis · Ziel und Reihenfolge',33,35,
        'Vor Beginn den Endzustand und die Reihenfolge klären. Alle Pfade beziehen sich auf den vollständig entpackten Ordner marburg_geodaten. '
        'Die WMS-Einrichtung beginnt erst nach dem geprüften lokalen Projekt und ist auf dem eigenen Gerät freiwillig.',core)
    steps(p,[('Projekt speichern','unit10_einstieg.qgz im Hauptordner'),
             ('Zwei lokale Layer laden und prüfen','gewaesser + dgm_marburg_10m.tif'),
             ('Speichern, schließen, erneut öffnen','Beide Quellen ohne Reparatur erreichbar')])
    band(p,'Fertig heißt: Das Projekt öffnet Gewässerlayer und DGM erneut.',size=23)

    p=slide('Arbeitsordner und Projekt vorbereiten','Praxis · Schritt 1',35,38,
        'Den entpackten Paketordner öffnen. Kein zusätzlicher Unterordner unit10_qgis anlegen. Neues QGIS-Projekt erstellen, Projekt-CRS EPSG:25832 prüfen und sofort im Hauptordner speichern. '
        'Die gezeigte Struktur entspricht dem aktuellen Paket. Ausgangsdaten in data_raw nicht überschreiben.',qgis+'\n'+core)
    text(p,110,235,720,440,'marburg_geodaten/\n    data_raw/\n    data_output/\n    documentation/\n    ersatz/\n    unit10_einstieg.qgz',29,TEAL,True)
    card(p,880,235,600,310,'Projekt zuerst speichern','Name: unit10_einstieg.qgz\nOrt: Hauptordner\nProjekt-CRS: EPSG:25832',size=25)
    band(p,'Ausgangsdaten bleiben unverändert in data_raw.',size=24)

    p=slide('Gewässerlayer laden','Praxis · Schritt 2',38,42,
        'Im Browser den Hauptordner und data_raw öffnen. Im GeoPackage marburg_basis.gpkg den Layer gewaesser wählen. '
        'Nach dem Laden auf die Layerausdehnung zoomen. Erwartet sind 412 Multi-Linienfeatures in EPSG:25832; die Zahl dient als Kontrollwert, nicht als auswendig zu lernender Inhalt.',qgis+'\n'+core)
    steps(p,[('Browser → data_raw','Den entpackten Paketordner verwenden.'),
             ('marburg_basis.gpkg öffnen','Layer gewaesser hinzufügen.'),
             ('Auf Layer zoomen','Linien sichtbar? CRS: EPSG:25832?')])
    band(p,'Kontrollwert: gewaesser · 412 Linienfeatures · EPSG:25832',size=22)

    p=slide('Höhenraster laden','Praxis · Schritt 3',42,46,
        'Das GeoTIFF aus data_raw laden. Es besitzt 2000 × 2000 Zellen à 10 Meter und EPSG:25832. NoData ist −9999. '
        'Diese Werte dienen heute nur zur Identifikation und Kontrolle; die inhaltliche Rasteranalyse folgt in Unit 13. '
        'Wenn das Raster die Gewässer verdeckt, die Layerreihenfolge ändern.',qgis+'\n'+core)
    steps(p,[('Browser → data_raw','dgm_marburg_10m.tif hinzufügen.'),
             ('Layer sichtbar schalten','Auf gemeinsame räumliche Lage achten.'),
             ('Eigenschaften kurz prüfen','Raster · 2000 × 2000 · 10 m · EPSG:25832')])
    band(p,'Jetzt sind genau ein Vektorlayer und ein Rasterlayer geladen.',size=23)

    p=slide('Verdeckt heißt nicht gelöscht','Praxis · Layerreihenfolge',46,49,
        'Die Abbildung der Kursseite erläutern. Oben stehende Layer werden zuletzt gezeichnet und können darunterliegende Inhalte verdecken. '
        'Sichtbarkeit und Reihenfolge verändern nur die Darstellung im Projekt, nicht die gespeicherten Features. Im eigenen Projekt Gewässer über dem DGM anzeigen.',
        qgis+'\nBild: assets/images/unit10/layerreihenfolge.svg')
    picture(p,ROOT/'assets/images/unit10/layerreihenfolge.svg',115,210,425,499)
    card(p,600,240,915,205,'Im Layer-Bereich','gewaesser nach oben\ndgm_marburg_10m darunter',size=27)
    card(p,600,485,915,205,'Kontrollfrage','Sind beide Layer vorhanden und sinnvoll sichtbar?',ORANGE,size=25)
    band(p,'Die Reihenfolge ändert die Darstellung – nicht die Daten.',size=23)

    p=slide('Beide Layer kurz bedienen','Praxis · Karte und Layer',49,55,
        'Zeit zum angeleiteten Mitmachen. Sichtbarkeit beider Layer einzeln schalten, auf den Gewässerlayer zoomen und den Kartenausschnitt verschieben. '
        'Dann im Layer-Bereich benennen: Welcher Layer ist Vektor, welcher Raster? Nicht weitere Daten oder alternative Ladewege ergänzen.',qgis+'\n'+core)
    steps(p,[('Sichtbarkeit testen','Gewässer und DGM einzeln ein- und ausblenden.'),
             ('Navigieren','Auf gewaesser zoomen und Kartenausschnitt verschieben.'),
             ('Datenmodell benennen','gewaesser = Vektor · DGM = Raster')])
    band(p,'Zwischenstand: beide Layer geladen, sichtbar und als Modell erkannt.',size=22)

    p=slide('Feature und Tabellenzeile verbinden','Praxis · Vektordaten prüfen',55,59,
        'Attributtabelle des Layers gewaesser öffnen. Ein Feature in der Karte auswählen beziehungsweise abfragen und die zugehörige Tabellenzeile zeigen. '
        'Raster besitzt keine gewöhnliche Featuretabelle. Die konkrete Attributausprägung wird nicht vorgegeben; Studierende wählen ein sichtbares Gewässerfeature.',qgis)
    box(p,105,300,420,280,PALE,GRID)
    poly(p,[(150,510),(245,430),(330,465),(460,350)],TEAL,width=130)
    box(p,300,423,34,34,ORANGE,ellipse=True)
    text(p,120,610,430,55,'ausgewähltes Linienfeature',22,TEAL,True,'CENTER')
    line(p,550,440,635,440,TEAL,85)
    poly(p,[(610,419),(638,440),(610,461)],TEAL,width=85)
    table(p,['fid','name','gewaesserzahl'],[['[Zeile]','[Wert]','[Wert]']],[160,330,375],y=350,row_h=105,size=20,x0=650)
    band(p,'Ein Vektorfeature in der Karte gehört zu einer Tabellenzeile.',size=22)

    p=slide('Datenquelle, Modell und CRS prüfen','Praxis · Layereigenschaften',59,64,
        'Für beide Layer die Eigenschaften öffnen und Datenquelle, Datenmodell, CRS und Ausdehnung finden. Die Studierenden tragen die tatsächliche Ausdehnung selbst ein. '
        'Beide Layer nutzen EPSG:25832. Unterschiedliche bekannte Layer-CRS wären nicht automatisch ein Fehler; QGIS kann für die Anzeige dynamisch transformieren.',qgis+'\n'+core)
    table(p,['Layer','Datenquelle','Modell','CRS'],[
        ['gewaesser','marburg_basis.gpkg','Vektor · Linie','EPSG:25832'],
        ['dgm_marburg_10m','dgm_marburg_10m.tif','Raster · 10-m-Zellen','EPSG:25832']],
        [350,470,340,270],y=260,row_h=112,size=21)
    text(p,110,645,1380,60,'Zusätzlich im Protokoll: räumliche Ausdehnung beider Layer.',25,TEAL,True)
    band(p,'Projekt-CRS und Layer-CRS prüfen – nicht miteinander verwechseln.',size=22)

    p=slide('Kontrollen dokumentieren','Praxis · processing_notes.md',64,68,
        'Die vorbereitete Tabelle unter documentation/processing_notes.md verwenden. Keine neue Vorlage anlegen. '
        'Datenquelle, Modell, Layer-CRS und Ausdehnung beider Layer festhalten. Das Ergebnis des späteren Öffnungstests wird anschließend ergänzt.',qgis+'\n'+core)
    table(p,['Prüfung','Eintrag'],[
        ['Projektdatei','unit10_einstieg.qgz'],
        ['Vektor','marburg_basis.gpkg / gewaesser'],
        ['Raster','dgm_marburg_10m.tif'],
        ['Modelle, CRS, Ausdehnung','[eintragen]'],
        ['Projekt erneut vollständig geöffnet','[später eintragen]']],
        [650,780],y=215,row_h=79,size=22)
    band(p,'Dokumentieren heißt: Eine andere Person kann den Stand nachvollziehen.',size=21)

    p=slide('Speichern, schließen, erneut öffnen','Praxis · Funktionstest',68,72,
        'Jetzt den verbindlichen Öffnungstest durchführen. Erst speichern, dann QGIS schließen. Die qgz-Datei aus dem Hauptordner erneut öffnen. '
        'Nicht über die Liste zuletzt geöffneter Projekte ausweichen, damit der Speicherort sichtbar bleibt.',qgis+'\n'+core)
    steps(p,[('Projekt speichern','unit10_einstieg.qgz im Hauptordner.'),
             ('QGIS schließen','Der gespeicherte Arbeitsstand wird beendet.'),
             ('qgz erneut öffnen','Sind Gewässerlayer und DGM ohne Reparatur erreichbar?')])
    band(p,'Der Öffnungstest ist Teil des Ergebnisses – kein optionaler Zusatz.',size=22)

    p=slide('Was prüfen Sie bei einem roten Ausrufezeichen?','Praxis · Fehlerdiagnose',72,75,
        'Das Symbol steht hier für eine nicht erreichbare Datenquelle. 30 Sekunden zu zweit den ersten sinnvollen Prüfschritt formulieren lassen. '
        'Nicht verschiedene CRS ausprobieren: Ein nicht erreichbarer Dateipfad ist zunächst ein Ablageproblem.',qgis)
    text(p,115,255,250,250,'!',110,ORANGE,True,'CENTER')
    text(p,430,245,1050,185,'Ein Layer ist nach dem Öffnen\nnicht erreichbar.',35,bold=True)
    steps(p,[('A · Datenpfad und Dateiname prüfen',''),('B · Ein zufälliges CRS zuweisen',''),('C · Den Layer sofort neu erzeugen','')],y=475,gap=85)
    band(p,'Welcher erste Prüfschritt passt zur beobachteten Ursache?',size=23)

    p=slide('Ablage prüfen – dann Ergebnis sichern','Auflösung · Öffnungstest',75,78,
        'A ist richtig. Prüfen, ob Projekt und vollständig entpackter Datenordner noch zusammenliegen und ob Dateien umbenannt oder verschoben wurden. '
        'Nach einer nötigen Pfadreparatur erneut speichern, schließen und öffnen. Im Protokoll vollständig ja oder nein eintragen und ein Problem knapp notieren.',qgis+'\n'+core)
    steps(p,[('A · Datenpfad prüfen','Sind data_raw und Dateien am erwarteten Ort?'),
             ('Falls nötig: Pfad reparieren','Ursache verstehen, nicht Daten neu erfinden.'),
             ('Erneut öffnen und protokollieren','Beide Layer erreichbar: ja / nein')])
    band(p,'Kernpfad fertig: Gewässerlayer und DGM öffnen ohne Pfadreparatur.',size=21)

    p=slide('Download oder Webdienst?','Datenquellen · Übergang',78,79,
        'Die Abbildung kurz als Übergang lesen. Ein Download erzeugt eine lokale, dokumentierbare Kopie. Ein Webdienst antwortet bei jeder Anfrage über das Netz. '
        'In beiden Fällen Metadaten, Datenstand, Lizenz und Quelle dokumentieren.',
        sources+'\nBild: assets/images/unit10/download-webdienst.svg')
    picture(p,ROOT/'assets/images/unit10/download-webdienst.svg',200,215,1200,540)
    band(p,'Das lokale Projekt funktioniert bereits – jetzt folgt die WMS-Demo.',size=22)

    p=slide('Ein WMS liefert ein Kartenbild','Datenquellen · WMS',79,81,
        'WMS als Web Map Service auflösen. QGIS sendet Ausschnitt, Bildgröße und CRS; der Server liefert ein gerendertes Kartenbild. '
        'Ein WMS eignet sich für Orientierung und Hintergrund, aber normalerweise nicht für eine freie Vektoranalyse. Begrenzte Objektabfragen können möglich sein.',sources)
    card(p,85,235,430,390,'QGIS fragt an','Ausschnitt\nBildgröße\nCRS',size=27)
    line(p,545,420,735,420,TEAL,95)
    poly(p,[(708,398),(738,420),(708,442)],TEAL,width=95)
    card(p,770,235,745,390,'WMS antwortet','Gerendertes Kartenbild\nfür den angefragten Ausschnitt\n\nKeine vollständigen Vektorfeatures',ORANGE,size=27)
    band(p,'WMS: Kartenansicht statt vollständigem ursprünglichem Datensatz.',size=22)

    p=slide('HLNUG-WMS gemeinsam einbinden','Beamer-Demo · maximal 3 Minuten',81,84,
        'Die lokale Kernübung ist beendet. Die Lehrperson demonstriert die vorgegebene Verbindung. Studierende mit fertigem Projekt können optional mitmachen. '
        'Dienstadresse von der Kursseite kopieren, nicht aus einer Portalseiten-URL erraten. Bei der ersten Nichterreichbarkeit direkt zur nächsten Folie wechseln.',sources)
    steps(p,[('Datenquellenmanager → WMS/WMTS','Neue Verbindung: HLNUG Schutzgebiete Hessen'),
             ('Dienstadresse von der Kursseite','Verbinden und Naturschutzgebiete wählen.'),
             ('Layer hinzufügen','Unter den lokalen Gewässerlayer legen und Ausschnitt prüfen.')])
    band(p,'Keine Fehlersuche im Plenum: Bei Ausfall sofort Offline-Ersatz.',size=22)

    p=slide('Offline-Ersatz: derselbe Vergleich bleibt möglich','WMS-Demo · Minute 84–85',84,85,
        'Wenn der Dienst nicht unmittelbar reagiert, ohne weiteren Versuch diese vorbereiteten Paketdateien verwenden: wms_schutzgebiete.png, wms_capabilities.xml und documentation/quellen.md. '
        'Der Screenshot zeigt nur die gerenderte Schutzgebietsdarstellung. Capabilities und Quellenblatt liefern Dienst- und Metadaten. Der Ausfall ist kein studentischer Fehler.',
        sources+'\nErsatzbild aus assets/data/marburg/marburg_geodaten.zip')
    box(p,85,220,500,500,PALE,GRID)
    picture(p,WMS_IMAGE,100,235,470,470)
    card(p,650,235,865,205,'Online erreichbar','WMS-Layer Naturschutzgebiete laden und unter gewaesser anordnen.',size=23)
    card(p,650,485,865,205,'Dienst nicht erreichbar','Screenshot + Capabilities + quellen.md verwenden; Ausfall notieren.',ORANGE,size=23)
    band(p,'Online oder Ersatz: lokale Datei und Kartenbilddienst unterscheiden.',size=21)

    p=slide('Exit-Ticket: Was nehmen Sie mit?','Abschluss · ohne Nachschlagen',85,88,
        'Eine der drei Fragen passend zum Sitzungsverlauf auswählen. Eine Minute zu zweit formulieren lassen und anschließend eine gemeinsame Antwort sichern. '
        'Nicht alle drei Fragen als Pflichtaufgabe behandeln. Erwartet: 1. qgz speichert Arbeitsstand und Verweise, nicht normalerweise alle Daten. '
        '2. Layerart über Symbol, Eigenschaften und Attributtabelle prüfen. 3. WMS liefert primär ein Kartenbild und keine frei analysierbaren Vektorfeatures.',overview)
    steps(p,[('A · Was enthält eine qgz-Datei – und was nicht?',''),
             ('B · Woran erkennen Sie Vektor oder Raster?',''),
             ('C · Warum ist ein WMS meist kein Vektor-Analyselayer?','')])
    band(p,'Eine Frage auswählen → zu zweit formulieren → gemeinsam sichern',size=21)

    p=slide('Nachbereitung und nächster Schritt','Abschluss · Unit 10',88,90,
        'Als einzige Übungsaufgabe die JiTT-Fragen zu Unit 10 im ILIAS-Kurs nennen. Fragen und Frist stehen in ILIAS; der konkrete Link ist auf der Kursseite noch Platzhalter. '
        'Keine Fertigstellung der WMS-Einrichtung oder des Praxiswegs als Übungsaufgabe verlangen. Unit 11 beginnt nach der Winterpause mit dem kurzen QGIS-Wiedereinstieg und importiert Punktdaten.',assignment)
    card(p,85,235,695,420,'Übungsaufgabe: JiTT-Fragen','Beantworten Sie die JiTT-Fragen\nzu Unit 10 im ILIAS-Kurs.\n\nFragen und Frist stehen in ILIAS.',size=25)
    card(p,820,235,695,420,'Ausblick: Unit 11','QGIS kurz wiederfinden.\n\nEine CSV als Punktlayer importieren\nund Beobachtungen prüfen.',size=25)
    link=text(p,110,665,1380,48,'Hinweis zu den JiTT-Fragen: HTML-Lernumgebung → Unit 10',23,TEAL,True)
    hyperlink(link,assignment)
    band(p,'Die JiTT-Fragen sind Ihre einzige Übungsaufgabe zu Unit 10.',size=22)

    p=slide('WMS oder WFS?','Reserve · Datenquellen unterscheiden',0,0,
        'Nur bei Bedarf zur begrifflichen Abgrenzung zeigen. Ein WMS liefert primär ein gerendertes Kartenbild. Ein WFS liefert Vektorfeatures mit Geometrien und Attributen. '
        'WFS wird in Unit 10 nicht praktisch eingerichtet. Die Abbildung ist schematisch und ersetzt keine Dienstprüfung.',
        sources+'\nBild: assets/images/unit10/wms-wfs.svg',reserve=True)
    picture(p,ROOT/'assets/images/unit10/wms-wfs.svg',120,210,380,501)
    card(p,550,245,965,200,'WMS','Kartenbild für Orientierung und Hintergrund',size=27)
    card(p,550,485,965,200,'WFS','Vektorfeatures mit Geometrien und Attributen',ORANGE,size=27)
    band(p,'Ähnlicher sichtbarer Inhalt – technisch unterschiedliche Lieferung.',size=21)

    p=slide('Materialien und Quellen','Reserve · zum Nachschlagen',0,0,
        'Fachliche Grundlage sind die aktuellen fünf Unit-10-Seiten, der QGIS-Kernpfad und das Marburger Übungspaket vom 08.09.2026. '
        'Die Folien verwenden die vorhandenen Unit-10-Abbildungen sowie den vorbereiteten WMS-Ersatz aus dem Paket. '
        'QGIS-Dokumentation passend zur Kursversion 3.40 verlinken. Der HLNUG-Dienst wird nach Angabe der Kursseite verwendet; seine Live-Erreichbarkeit ist nicht Voraussetzung der Sitzung.',
        '\n'.join([overview,model,qgis,sources,assignment,core,QDOC,HLNUG,WMS_URL]),reserve=True)
    links=[('GeoMOER · Überblick Unit 10',overview),
           ('GeoMOER · QGIS-Kernpfad Unit 10',core),
           ('GeoMOER · Einführung in QGIS',qgis),
           ('GeoMOER · Datenquellen und WMS',sources),
           ('QGIS 3.40 · Benutzerhandbuch',QDOC),
           ('HLNUG · Geodienste Naturschutz',HLNUG)]
    for i,(label,url) in enumerate(links):
        sh=text(p,110,222+i*71,1380,60,label,25,TEAL,True)
        hyperlink(sh,url)
    text(p,110,676,1390,124,'Paketstand: 08.09.2026 · Abgleich der Folien: 09.09.2026\nLayout: Universität-Marburg-Vorlage · Titel-/Abschlussbild: FB19-Vorlage\nLehrabbildungen: vorhandene SVGs der Unit 10',17,MUTED)

    p=slide('Vielen Dank für Ihre Aufmerksamkeit','Abschluss',90,90,
        'Die Sitzung mit dieser Folie beenden. Die Abschlussgestaltung nutzt den Kontakt-Master der universitären Vorlage sowie das originale Foto-/Kartenmotiv aus der FB19-Titelseite.',str(TEMPLATE),kind='closing')
    box(p,44,44,809,807,0xF7DEED)
    picture(p,FB19_IMAGE,915,350,640,640*135/394)
    text(p,100,380,700,250,'Vielen Dank für Ihre Aufmerksamkeit',41,INK)
    text(p,165,710,620,110,'Geodaten · Unit 10\nFachbereich 19 · Geographie',18,INK)


def main():
    global DOC, MASTERS
    with tempfile.TemporaryDirectory(prefix='geomoer-unit10-') as profile:
        pipe='geomoer_unit10_' + uuid.uuid4().hex
        proc=subprocess.Popen(['libreoffice', '-env:UserInstallation='+Path(profile).as_uri(),
            '--headless', '--accept=pipe,name='+pipe+';urp;StarOffice.ComponentContext',
            '--norestore', '--nodefault', '--nofirststartwizard'], stdout=subprocess.DEVNULL)
        desktop = None
        try:
            local=uno.getComponentContext()
            resolver=local.ServiceManager.createInstanceWithContext('com.sun.star.bridge.UnoUrlResolver',local)
            for _ in range(100):
                try:
                    ctx=resolver.resolve('uno:pipe,name='+pipe+';urp;StarOffice.ComponentContext')
                    break
                except Exception:
                    if proc.poll() is not None:
                        raise RuntimeError('LibreOffice could not start')
                    time.sleep(.2)
            else:
                raise RuntimeError('LibreOffice connection timed out')
            desktop=ctx.ServiceManager.createInstanceWithContext('com.sun.star.frame.Desktop',ctx)
            legacy=desktop.loadComponentFromURL(FB19.as_uri(),'_blank',0,(prop('Hidden',True),))
            legacy_export=Path(profile)/'fb19.pptx'
            legacy.storeToURL(legacy_export.as_uri(),(prop('FilterName','Impress MS PowerPoint 2007 XML'),))
            legacy.close(True)
            (OUT/'assets').mkdir(exist_ok=True)
            with ZipFile(legacy_export) as archive:
                FB19_IMAGE.write_bytes(archive.read('ppt/media/image2.png'))
            with ZipFile(PACKAGE) as archive:
                WMS_IMAGE.write_bytes(archive.read('marburg_geodaten/ersatz/wms_schutzgebiete.png'))
            DOC=desktop.loadComponentFromURL(TEMPLATE.as_uri(),'_blank',0,(prop('Hidden',True),))
            masters=DOC.getMasterPages()
            MASTERS={masters.getByIndex(i).Name:masters.getByIndex(i) for i in range(masters.Count)}
            pages=DOC.getDrawPages()
            for i in range(pages.Count-1,-1,-1):
                if i != 2:pages.remove(pages.getByIndex(i))
            DOC.DocumentProperties.Title='Unit 10 – Geodatenmodelle, QGIS und Datenquellen'
            DOC.DocumentProperties.Subject='Geodaten · Unit 10 · Präsenzlehre'
            DOC.DocumentProperties.Author='GeoMOER'
            build()
            pptx=OUT/'unit10_praesenz.pptx'
            DOC.storeAsURL(pptx.as_uri(),(prop('FilterName','Impress MS PowerPoint 2007 XML'),prop('Overwrite',True)))
            DOC.close(True)
            DOC=desktop.loadComponentFromURL(pptx.as_uri(),'_blank',0,(prop('Hidden',True),))
            assert DOC.getDrawPages().Count == len(RECORDS)
            DOC.storeToURL((OUT/'unit10_praesenz.pdf').as_uri(),(prop('FilterName','impress_pdf_Export'),prop('Overwrite',True),
                prop('FilterData',(prop('ExportNotesPages',False),prop('ExportHiddenSlides',True),prop('UseTaggedPDF',True)))))
            DOC.close(True)
            with (OUT/'moderation.md').open('w') as fp:
                fp.write('# Unit 10 – Moderation\n\nTitelfolie, 29 Hauptfolien für 90 Minuten, zwei Reserve-/Quellenfolien und eine Abschlussfolie. Zeitangaben stehen nur in diesen Notizen.\n\n')
                for r in RECORDS:
                    fp.write(f"## {r['number']:02d} · {r['title']}\n\n{r['notes']}\n\n")
            print(f'Created {len(RECORDS)} slides: {pptx} and matching PDF',flush=True)
        finally:
            if desktop:
                desktop.terminate()
            try:
                proc.wait(timeout=10)
            except subprocess.TimeoutExpired:
                proc.terminate()


if __name__=='__main__':
    main()
