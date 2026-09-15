#!/usr/bin/python3
"""Build the Unit 09 classroom deck with LibreOffice UNO (no downloads).

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
COURSE = 'https://geomoer.github.io/moer-bsc-geodaten/unit09/'
PROJ = 'https://proj.org/en/stable/'
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
        text(page, 100, 852, 1100, 30, 'Universität Marburg | Fachbereich 19 · Geographie | Geodaten · Unit 09', 10, MUTED)
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


def table(page, headers, rows, widths, y=235, row_h=86, size=24, colors=None):
    x0 = 85
    for r, values in enumerate([headers] + rows):
        x = x0
        for j, (value, width) in enumerate(zip(values, widths)):
            fill = INK if r == 0 else (WHITE if r % 2 else PALE)
            box(page, x, y + r * row_h, width - 3, row_h - 3, fill)
            color = WHITE if r == 0 else (colors.get(r - 1, INK) if colors else INK)
            text(page, x + 18, y + r * row_h + 17, width - 36, row_h - 20,
                 value, size, color, r == 0)
            x += width


def globe(page, cx, cy, radius):
    box(page, cx-radius, cy-radius, 2*radius, 2*radius, PALE, INK, ellipse=True)
    for lat in [-60, -30, 0, 30, 60]:
        phi = math.radians(lat)
        xx = radius * math.cos(phi)
        yy = cy - radius * math.sin(phi)
        line(page, cx-xx, yy, cx+xx, yy, TEAL if lat == 0 else GRID, 60 if lat == 0 else 25)
    for lon in [-60, -30, 0, 30, 60]:
        pts = [(cx + radius*math.cos(math.radians(a))*math.sin(math.radians(lon)),
                cy-radius*math.sin(math.radians(a))) for a in range(-90,91,3)]
        poly(page, pts, ORANGE if lon == 0 else GRID, width=60 if lon == 0 else 25)


def projection(page, x, label, kind):
    text(page, x, 216, 665, 55, label, 26, TEAL, True)
    cx, cy, scale = x + 345, 476, 94
    f = lambda a: math.asinh(math.tan(a)) if kind == 'merc' else math.sin(a)
    extent = f(math.radians(70))
    box(page, cx-math.pi*scale, cy-extent*scale, 2*math.pi*scale, 2*extent*scale, PALE, GRID)
    for lat in [-60,-30,0,30,60]:
        yy = cy-f(math.radians(lat))*scale
        line(page, cx-math.pi*scale, yy, cx+math.pi*scale, yy, GRID, 18)
    for lon in range(-120,121,60):
        xx = cx+math.radians(lon)*scale
        line(page, xx, cy-extent*scale, xx, cy+extent*scale, GRID, 18)
    # Equal spherical caps of radius 5 degrees, sampled along great-circle bearings.
    # Forward projection uses equal x/y scale within each drawing; no stretching.
    for lat in [0,30,60]:
        for lon in [-95,0,95]:
            p0, l0, r = math.radians(lat), math.radians(lon), math.radians(5)
            pts=[]
            for b in range(0,361,5):
                bearing=math.radians(b)
                p=math.asin(math.sin(p0)*math.cos(r)+math.cos(p0)*math.sin(r)*math.cos(bearing))
                l=l0+math.atan2(math.sin(bearing)*math.sin(r)*math.cos(p0),math.cos(r)-math.sin(p0)*math.sin(p))
                pts.append((cx+l*scale, cy-f(p)*scale))
            poly(page, pts, ORANGE, 0xD96738, 18, True)
    for lat in [0,60]:
        text(page, x, cy-f(math.radians(lat))*scale-18, 58, 40, f'{lat}°', 15, MUTED)


def build():
    p=slide('Geodaten, Koordinaten und Projektionen','Unit 09',0,0,
        'Titelfolie beim Ankommen zeigen. Danach beginnt die Sitzung mit dem JiTT-Block zur vorherigen Sitzung. '
        'Die Gestaltung stammt aus der bereitgestellten universitären PowerPoint-Vorlage. '
        'Das Foto-/Kartenmotiv links wurde unverändert aus der Titelseite der FB19-Vorlage übernommen. '
        'Namen oder Termine werden nicht erfunden.',str(TEMPLATE),kind='title')
    picture(p,FB19_IMAGE,44,350,539,539*135/394)
    text(p,625,285,850,300,'Geodaten,\nKoordinaten und\nProjektionen',44,WHITE)
    text(p,625,614,840,70,'Unit 09',28,WHITE)
    text(p,625,744,840,100,'Fachbereich 19 · Geographie\nPhilipps-Universität Marburg',19,WHITE)

    p=slide('JiTT · Rückblick auf die letzte Sitzung', 'Platzhalter · vollständig austauschbar', 0,10,
        'VOR DEM TERMIN: Diese gesamte Platzhalterfläche durch die aktuelle JiTT-Auswertung zur vorherigen Sitzung ersetzen. '
        'Bei Bedarf die Folie duplizieren und den gesamten Block mit den tatsächlichen Fragen, Antwortverteilungen, Abbildungen und gemeinsamer Klärung befüllen. '
        'Es sind bewusst keine Fragen, Ergebnisse, Aufgaben oder feste Untergliederung vorgegeben. '
        'Der komplette Block hat im Ablauf etwa zehn Minuten. Nur tatsächliche und zusammengefasste/anonymisierte Rückmeldungen einsetzen. '
        'Bei längerer Auswertung die anschließenden kurzen Austauschphasen entsprechend kürzen. Die Zeitplanung steht ausschließlich in den Notizen.')
    placeholder=box(p,100,237,1400,545,PALE,GRID)
    placeholder.Name='JiTT – vollständigen Block ersetzen'
    text(p,180,430,1240,130,'[Hier den vollständigen\nJiTT-Block einfügen]',38,TEAL,False,'CENTER')

    p=slide('Geodaten, Koordinaten und Projektionen', 'Unit 09 · Orientierung',10,11,
        'Die drei Ziele ankündigen: Raumbezug erkennen, Koordinaten prüfen und CRS passend zum Zweck auswählen. '
        'Die Sitzung funktioniert ohne vorheriges Lesen. Alle arbeiten zunächst an denselben Grundlagen. '
        'Bei Partnerphasen kurz mit der Sitznachbarin oder dem Sitznachbarn sprechen; keine Gruppenumbildung im Hörsaal. '
        'Ein GIS wird heute noch nicht benötigt.',
        COURSE+'unit09-00_overview.html\nBild: assets/images/unit09/hero-unit09.jpg, vorhandene KI-generierte Kursillustration.')
    graphic=DOC.createInstance('com.sun.star.drawing.GraphicObjectShape')
    p.add(graphic)
    graphic.Position=Point(round(85*SCALE),round(215*SCALE))
    graphic.Size=Size(round(1430*SCALE),round(238.333*SCALE))
    graphic.GraphicURL=(ROOT/'assets/images/unit09/hero-unit09.jpg').as_uri()
    text(p,85,466,1430,25,'Vorhandene KI-generierte Kursillustration',10,MUTED)
    for x,num,title in [(85,'01','Raumbezug erkennen'),(575,'02','Koordinaten prüfen'),(1065,'03','CRS auswählen')]:
        text(p,x,530,430,65,num,33,TEAL,True)
        text(p,x,607,435,95,title,26,bold=True)
    band(p,'Heute: verstehen, gemeinsam prüfen und begründen.')

    p=slide('Wo ist das?', 'Einstiegsfrage',11,14,
        'Zunächst nur das Zahlenpaar zeigen. 30 Sekunden still überlegen lassen, dann zwei Vermutungen sammeln. '
        'Nachfragen: Sind das Breite und Länge, x und y, Grad oder Meter? Ist eine Reihenfolge vereinbart? '
        'Auflösung mündlich: Als 50,81° N / 8,77° E ist ungefähr Marburg gemeint. Aus dem unbeschrifteten Zahlenpaar allein folgt das nicht eindeutig. '
        'Das CRS muss zusätzlich bekannt sein. Die Leitfrage am Ende der Sitzung erneut aufgreifen.',COURSE+'unit09-02_koordinaten.html')
    text(p,140,300,1320,180,'50,81 / 8,77',80,TEAL,True,'CENTER')
    text(p,160,545,1280,100,'Welche Angaben fehlen für eine eindeutige Position?',32,bold=True,align='CENTER')
    band(p,'30 Sekunden nachdenken → zwei Vermutungen sammeln')

    p=slide('Was macht Daten zu Geodaten?', '01 · Raumbezug',14,16,
        'Die beiden Tabellen aus der aktuellen Kursseite vergleichen. ID, Datum und Messwert bleiben gleich; erst Koordinaten und CRS ergänzen einen direkt nutzbaren Raumbezug. '
        'Messort und Messwert unterscheiden: Raumbezug plus Sachdaten. Auch eine Adresse oder ein eindeutig identifizierbares Gebiet kann einen Raumbezug liefern; Koordinaten sind keine Voraussetzung. '
        'Die Werte sind erfundene, didaktische Beispieldaten.',
        COURSE+'unit09-01_geodaten.html\nBild: assets/images/unit09/raumbezug.svg')
    picture(p,ROOT/'assets/images/unit09/raumbezug.svg',250,215,1100,473)
    band(p,'Geodaten verbinden Informationen mit einem Ort oder Gebiet.')

    p=slide('Wie bilden wir die Wirklichkeit ab?', '01 · Raumbezug',16,18,
        'Punkt, Linie und Fläche als Modelle vorstellen. Dieselbe Stadt kann auf einer Deutschlandkarte ein Punkt und auf einer regionalen Karte eine Fläche sein. '
        'Maßstab und Fragestellung bestimmen die Darstellung. Raster nur kurz ergänzen: Auch räumlich verortete Bild- oder Rasterzellen sind Geodaten. '
        'Hier noch keine vollständige Vektor-/Raster-Systematik vorwegnehmen.',COURSE+'unit09-01_geodaten.html')
    for x,label,caption in [(85,'Punkt','Messstation'),(575,'Linie','Straßenverlauf'),(1065,'Fläche','Stadtgebiet')]:
        box(p,x,235,450,395,WHITE)
        text(p,x+25,260,400,55,label,28,TEAL,True)
        text(p,x+25,545,400,70,caption,25)
    box(p,280,395,48,48,ORANGE,ellipse=True)
    poly(p,[(625,467),(693,390),(775,432),(850,356),(970,400)],TEAL,width=150)
    poly(p,[(1140,373),(1300,338),(1430,433),(1330,500),(1154,478)],TEAL,PALE,60,True)
    band(p,'Die Fragestellung und der Maßstab bestimmen das Modell.')

    p=slide('Welche Beispiele haben einen Raumbezug?', 'Mitdenken · Nachbarschaftsgespräch',18,19,
        '20 Sekunden einzeln prüfen, 30 Sekunden zu zweit austauschen, anschließend per Handzeichen A bis C abfragen. '
        'Nicht nur Ja/Nein sammeln: Ein Paar begründet die Genauigkeit der Lageangabe. Bei Zeitdruck Austausch verkürzen. '
        'Die Lösung kommt erst auf der nächsten Folie.',COURSE+'unit09-01_geodaten.html')
    steps(p,[('A · Einwohnerzahl mit Gemeindenamen','Können Sie die Information räumlich zuordnen?'),
             ('B · Temperatur mit Datum, ohne Messort','Welche Information fehlt?'),
             ('C · Pflanzenfund „in der Nähe von Marburg“','Wie genau ist dieser Raumbezug?')],gap=155)
    band(p,'Erst allein überlegen, dann zu zweit eine Begründung finden.')

    p=slide('Raumbezug ist nicht immer punktgenau', 'Auflösung · Raumbezug',19,20,
        'A: Raumbezug vorhanden, sofern die Gemeinde eindeutig identifiziert ist. Für die Kartendarstellung muss mit einer passenden Geometrie verknüpft werden. '
        'B: Aus diesen Angaben allein ist kein nutzbarer Raumbezug gegeben. C: Raumbezug vorhanden, aber ungenau. '
        'Damit die Fehlvorstellung korrigieren, dass nur Daten mit Koordinaten Geodaten seien.',COURSE+'unit09-01_geodaten.html')
    steps(p,[('A · Ja: Bezug zu einer Gemeinde','Für eine Karte benötigen wir die passende Gemeindegeometrie.'),
             ('B · Nein: Der Messort fehlt','Ein Datum beschreibt die Zeit, nicht die räumliche Lage.'),
             ('C · Ja: aber nur ungefähr','Für eine genaue Fundortkarte reicht die Angabe nicht aus.')],gap=155)
    band(p,'Raumbezug vorhanden? Und: genau genug für die Frage?')

    p=slide('Breite und Länge beschreiben Winkel', '02 · Koordinaten',20,25,
        'Die Abbildung aus der aktuellen Kursseite gemeinsam lesen. Breitenkreise verlaufen parallel zum Äquator; Meridiane verbinden die Pole. '
        'Latitude beschreibt den Winkel nördlich/südlich des Äquators, Longitude östlich/westlich des Nullmeridians. Am Ellipsoid bezieht sich die geodätische Breite auf die Ellipsoidnormale; diese Vertiefung ist heute nicht nötig. '
        'N und E positiv, S und W negativ. Wertebereiche gemeinsam lesen. Die zentralen Referenzlinien sind zusätzlich beschriftet, nicht nur farbig markiert.',COURSE+'unit09-02_koordinaten.html')
    picture(p,ROOT/'assets/images/unit09/gradnetz.svg',85,225,930,484)
    card(p,1055,235,460,205,'Breite · latitude','−90° bis +90°\nSüd bis Nord',size=23)
    card(p,1055,475,460,205,'Länge · longitude','−180° bis +180°\nWest bis Ost',ORANGE,size=23)
    band(p,'Nord und Ost: positiv   /   Süd und West: negativ')

    p=slide('Marburg: Welche Zahl steht zuerst?', '02 · Koordinaten',25,30,
        'Die Position ist ungefähr und dient als Ortsbeispiel. Beide Zeilen sind bei eindeutiger Beschriftung korrekt. '
        'Kurskonvention für Tabellen und spätere GIS-Importe: longitude, latitude beziehungsweise x, y. '
        'Nicht als universelle EPSG-Achsenreihenfolge darstellen: Die EPSG-Definition von 4326 nennt Breite vor Länge; Schnittstellen können andere Erwartungen haben. '
        'Deshalb Spaltennamen UND Metadaten UND erwartete Reihenfolge prüfen. EPSG-Codes werden später erklärt.',
        COURSE+'unit09-02_koordinaten.html\n'+PROJ+'faq.html')
    table(p,['Beschriftung','Werte für Marburg'],[
        ['Breite / Länge','50,81° N / 8,77° E'],
        ['Länge / Breite','8,77° E / 50,81° N']], [640,790],row_h=115,size=29)
    text(p,110,627,1380,64,'Kurskonvention für Tabellen: (longitude, latitude) = (x, y)',27,TEAL,True)
    band(p,'Andere Dienste können eine andere Reihenfolge erwarten.')

    p=slide('Vertauscht – und trotzdem formal gültig', '02 · Koordinaten',30,35,
        'Die aktuelle Kursabbildung zeigt beide Paare im selben WGS-84-Gradgitter. A liegt bei Marburg, B weit entfernt. Beide Wertepaare liegen innerhalb der global erlaubten Bereiche. '
        'Deshalb reicht eine reine Wertebereichsprüfung nicht: Spaltennamen, Achsenreihenfolge, erwartete Region und Metadaten gemeinsam prüfen. '
        'Die Kurskonvention lautet longitude, latitude beziehungsweise x, y. Sie ist keine universelle Achsenregel für alle Standards und Schnittstellen.',
        COURSE+'unit09-02_koordinaten.html\nBild: assets/images/unit09/achsenreihenfolge.svg')
    picture(p,ROOT/'assets/images/unit09/achsenreihenfolge.svg',100,210,500,508)
    card(p,650,235,865,220,'Kurskonvention','(longitude, latitude) = (x, y)',size=29)
    card(p,650,490,865,220,'Plausibilitätsprüfung','Wertebereich + Achsen + erwartete Lage + Metadaten',ORANGE,size=25)
    band(p,'Formal gültig bedeutet noch nicht räumlich plausibel.')

    p=slide('Welche Koordinatenpaare müssen wir prüfen?', 'Übung · Koordinatendaten',35,41,
        'Rahmen laut nennen: Dezimalgrad, Reihenfolge longitude, latitude, erwartete Orte in Deutschland. Alle Beispiele sind didaktisch vereinfacht und entsprechen der aktuellen Kursseite. '
        '1 Minute allein, 2 Minuten Nachbarschaftsgespräch, danach Begründungen sammeln. '
        'Es reicht nicht, nur globale Wertebereiche zu prüfen. Fragen: Was ist sicher falsch? Was ist nur eine Vermutung? Welche Quelle brauchen wir zur Korrektur? '
        'Die Beispiele werden gemeinsam in der Sitzung bearbeitet und besprochen.',COURSE+'unit09-02_koordinaten.html')
    table(p,['Nr.','longitude · x','latitude · y'],[
        ['1','8.77','50.81'],['2','50.81','8.77'],['3','188.40','50.81'],
        ['4','8.77','−50.81'],['5','0','0']],
        [180,625,625],y=210,row_h=74,size=25)
    text(p,100,674,1400,45,'Geplant: Orte in Deutschland · Einheit: Dezimalgrad',23,MUTED)
    band(p,'Markieren Sie Auffälligkeiten. Begründen Sie Ihren Verdacht.')

    p=slide('Plausibel ist noch nicht geprüft', 'Auflösung · Koordinatendaten',41,45,
        '1: Für Deutschland plausibel, aber keine Bestätigung der konkreten Position. '
        '2: Beide Werte global zulässig, unter der Kursreihenfolge aber nicht in Deutschland; möglicherweise vertauscht. Korrektur nur nach Quellenprüfung. '
        '3: longitude 188.40 liegt außerhalb des erlaubten Bereichs. 4: latitude −50.81 liegt auf der Südhalbkugel. '
        '5: (0, 0) ist eine gültige Position im Golf von Guinea, aber unplausibel für Deutschland und möglicherweise ein fehlender Wert. Nicht ungeprüft löschen. '
        'Jede Änderung mit Befund, Quelle und Entscheidung dokumentieren.',COURSE+'unit09-02_koordinaten.html')
    table(p,['Nr.','Befund'],[
        ['1','Für Deutschland plausibel'],['2','Nicht in Deutschland; möglicherweise vertauscht'],
        ['3','Länge über 180°: ungültig'],['4','Breite negativ: Südhalbkugel'],
        ['5','Formal gültig, aber nicht in Deutschland']],
        [180,1250],y=210,row_h=74,size=23)
    band(p,'Auffälligkeit dokumentieren → Quelle prüfen → begründet korrigieren',size=23)

    p=slide('Koordinaten brauchen ein Bezugssystem', '03 · CRS und Projektionen',45,48,
        'CRS steht für Coordinate Reference System beziehungsweise Koordinatenreferenzsystem. Es verknüpft Zahlen mit Positionen auf der Erde. '
        'Das CRS umfasst ein Erdmodell und Bezug dazu, Achsen und Einheiten sowie bei projizierten Systemen eine Kartenprojektion. '
        'Erst Metadaten erlauben die richtige Interpretation. Die UTM-Werte wurden mit PROJ für 50.81 N, 8.77 E nach EPSG:25832 berechnet und hier auf 100 m gerundet. '
        'Es handelt sich um einen ungefähr gewählten Beispielpunkt, nicht um die Vermessung eines bestimmten Gebäudes. Die beiden Angaben repräsentieren innerhalb ihrer Rundung denselben Ort.',
        COURSE+'unit09-03_projektionen.html\n'+PROJ+'usage/quickstart.html\nBild: assets/images/unit09/crs-vergleich.svg\nLokale Prüfung: cs2cs EPSG:4326 EPSG:25832 → 483795, 5628722 m.')
    picture(p,ROOT/'assets/images/unit09/crs-vergleich.svg',250,220,1100,473)
    band(p,'Derselbe ungefähre Ort bei Marburg – unterschiedliche Zahlen.')

    p=slide('Winkel oder Meter?', '03 · CRS und Projektionen',48,50,
        'Geographische Koordinaten sind Winkel. Ein Grad Länge entspricht je nach Breite einer anderen Entfernung. '
        'Projizierte Koordinaten liegen in einer Ebene, häufig mit der Einheit Meter. Sie sind nicht allein wegen der Einheit für jede Messung geeignet. '
        'Das Gebiet und der Messzweck bleiben entscheidend. Präzise geodätische Berechnungen sind auch aus geographischen Koordinaten möglich; heute geht es um die grundlegende Unterscheidung.',
        COURSE+'unit09-03_projektionen.html')
    card(p,85,235,695,415,'Geographisches CRS','Position auf dem Erdmodell\n\nLänge und Breite\nEinheit: Grad',size=28)
    card(p,820,235,695,415,'Projiziertes CRS','Position in einer Ebene\n\nx und y\nEinheit: hier Meter',size=28)
    band(p,'Die Einheit „Meter“ allein garantiert keine genaue Messung.')

    p=slide('Von der gekrümmten Erde auf die Ebene', '03 · Kartenprojektionen',50,53,
        'Frage: Wie lässt sich eine Orangenschale flach auslegen? Antworten wie einschneiden, dehnen oder stauchen aufnehmen. '
        'Die Analogie erklärt, dass die Abbildung einer gekrümmten Oberfläche auf eine Ebene Kompromisse verlangt. '
        'Nicht suggerieren, jede Kartenprojektion sei eine perspektivische Lichtprojektion. Eine Projektion ist hier eine mathematische Abbildung. '
        'Fläche, lokale Winkel/Form, Entfernung und Richtung können nicht gleichzeitig überall unverzerrt bleiben.',COURSE+'unit09-03_projektionen.html')
    globe(p,325,423,145)
    text(p,180,610,290,65,'gekrümmt',28,TEAL,True,'CENTER')
    text(p,570,370,470,80,'Kartenprojektion',29,bold=True,align='CENTER')
    line(p,630,480,940,480,TEAL,100)
    poly(p,[(917,459),(943,480),(917,501)],TEAL,width=100)
    box(p,1110,305,335,235,PALE,TEAL)
    for i in range(1,4):
        line(p,1110+i*335/4,305,1110+i*335/4,540,GRID)
        line(p,1110,305+i*235/4,1445,305+i*235/4,GRID)
    text(p,1110,610,335,65,'eben',28,TEAL,True,'CENTER')
    band(p,'Jede ebene Weltkarte verzerrt bestimmte Eigenschaften.')

    p=slide('Gleich große Gebiete – anders dargestellt', 'Vergleich · Kartenprojektionen',53,56,
        'Die aktuelle Kursabbildung zeigt dieselben geodätischen Referenzflächen mit 1000 Kilometern Radius am Äquator und bei 70° Nord. '
        'Links World Mercator (EPSG:3395), rechts Equal Earth (EPSG:8857). World Mercator vergrößert die polnahe Fläche stark; Equal Earth erhält die Flächenverhältnisse und verändert die Formen. '
        'Zuerst beobachten lassen: Was passiert mit Fläche und Form? Keine Längen aus der Abbildung ablesen und keine Projektionsformeln einführen. '
        'Die Umrisse wurden auf WGS 84 berechnet und anschließend in beide CRS transformiert.',
        COURSE+'unit09-03_projektionen.html\n'+PROJ+'operations/projections/merc.html\nBild: assets/images/unit09/projektionsvergleich.svg')
    picture(p,ROOT/'assets/images/unit09/projektionsvergleich.svg',160,210,1280,602)

    p=slide('Welche Karte passt zum Flächenvergleich?', 'Abstimmung · Kartenprojektionen',56,58,
        '30 Sekunden Entscheidung, 60 Sekunden Austausch mit Nachbarperson, anschließend A/B/C per Handzeichen abfragen. '
        'Optionen nacheinander abfragen; es wird keine Abstimmungssoftware benötigt. Eine Begründung für B und bei Bedarf für C hören. '
        'Bei längerer JiTT-Phase den Austausch verkürzen. Die Auflösung folgt auf der nächsten Folie.',
        COURSE+'unit09-03_projektionen.html')
    text(p,100,218,1400,100,'Wir möchten die Flächen verschiedener Länder vergleichen.',29,bold=True)
    steps(p,[('A · Mercator','Die Formen wirken vertraut.'),('B · Eine flächentreue Projektion','Die Flächenverhältnisse sollen erhalten bleiben.'),
             ('C · Jede Projektion ist gleich geeignet','Alle stellen doch dieselbe Erde dar.')],y=345,gap=112)
    band(p,'A, B oder C? Entscheiden Sie und begründen Sie Ihre Wahl.')

    p=slide('Der Zweck entscheidet über die Projektion', 'Auflösung · Kartenprojektionen',58,60,
        'B ist für diesen Zweck richtig. Flächentreue erhält die Flächenverhältnisse; das bedeutet nicht, dass Entfernungen und Formen ebenfalls erhalten bleiben. '
        'Auf den Diagrammvergleich zurückverweisen. Bei Bedarf einen Schritt zurückgehen. '
        'Die Idee auf andere Fragen übertragen: Lokale Winkel können wichtig sein; für regionale Entfernungsmessungen muss die Projektion zum Gebiet passen. '
        'Die vier Eigenschaften nicht als gleichzeitig erfüllbare Wunschliste darstellen.',COURSE+'unit09-03_projektionen.html')
    card(p,85,235,1430,260,'B · Flächentreu für den Flächenvergleich','Gleich große Gebiete auf der Erde erscheinen gleich groß auf der Karte.',size=30)
    text(p,110,545,1390,115,'Dafür können Formen und Winkel verändert sein.\nEine vertraute Darstellung ist kein Beleg für Flächentreue.',28)
    band(p,'Erst die Frage klären, dann die Projektion auswählen.')

    p=slide('Drei CRS, die uns im Kurs begegnen', '03 · EPSG-Codes',60,65,
        'EPSG-Codes als eindeutige Kennungen erklären, nicht auswendig abfragen. In den drei vereinfachten Szenarien unterscheiden wir Speicherung weltweiter Winkelkoordinaten, regionale Analyse und Webkartendarstellung. '
        '4326 ist geographisch, 25832 und 3857 sind projiziert. Auch bei 3857 steht Meter als Einheit, dennoch ist es nicht für präzise regionale Flächen-/Streckenmessung auszuwählen. '
        'Die sichtbare Webkarte kann in 3857 vorliegen, während Positionsangaben in WGS 84 ausgegeben werden. EPSG-Code und Achsenreihenfolge deshalb getrennt prüfen.',
        COURSE+'unit09-03_projektionen.html\n'+PROJ+'usage/quickstart.html\n'+PROJ+'operations/projections/webmerc.html\nLokale Definitionen geprüft mit projinfo EPSG:4326, EPSG:25832 und EPSG:3857.')
    card(p,85,235,450,470,'EPSG:4326','WGS 84\n\nGrad\n\nWeltweite Positionen',size=26)
    card(p,575,235,450,470,'EPSG:25832','ETRS89 /\nUTM Zone 32N\n\nMeter\nRegional um Marburg',size=26)
    card(p,1065,235,450,470,'EPSG:3857','WGS 84 /\nPseudo-Mercator\n\nMeter\nViele Webkarten',size=26)
    band(p,'Ein EPSG-Code identifiziert ein CRS. Er bewertet nicht seine Eignung.',size=23)

    p=slide('UTM: Die Zone muss zum Gebiet passen', '03 · Regionale Koordinaten',65,68,
        'UTM nutzt im Regelfall 6° breite Zonen; für Marburg gilt Zone 32 auf der Nordhalbkugel. Die schematische Grafik zeigt nur Längengradintervalle, keine Landkarte. '
        'Zone 32 reicht hier von 6° bis 12° Ost, mit Mittelmeridian 9°. Marburg liegt bei ungefähr 8,77° Ost. '
        'Das N in 32N meint in dieser CRS-Bezeichnung Nordhalbkugel, nicht das MGRS-Breitenband. '
        'UTM allein reicht nicht aus: Zone, Halbkugel und geodätisches Referenzsystem gehören dazu. Im Kurs nutzen wir dafür ETRS89 / UTM Zone 32N. '
        'Auch UTM ist nicht überall exakt; für regionale Kursanalysen ist die Verzerrung im passenden Gebiet gering.',COURSE+'unit09-03_projektionen.html\nLokale CRS-Definition: projinfo EPSG:25832.')
    for x,label,tint in [(160,'Zone 31',WHITE),(590,'Zone 32',PALE),(1020,'Zone 33',WHITE)]:
        box(p,x,295,430,270,tint,GRID)
        text(p,x+20,320,390,65,label,31,TEAL,True,'CENTER')
    for x,label in [(160,'0° E'),(590,'6° E'),(1020,'12° E'),(1450,'18° E')]:
        text(p,x-70,585,140,55,label,24,MUTED,align='CENTER')
    mx=590+(8.77-6)/6*430
    box(p,mx-13,450,26,26,ORANGE,ellipse=True)
    text(p,610,488,390,50,'Marburg · 8,77° E',23,ORANGE,True)
    text(p,110,670,1380,40,'Längengradintervalle · schematisch · Nordhalbkugel',20,MUTED)
    band(p,'Vollständig: ETRS89 / UTM Zone 32N · EPSG:25832')

    p=slide('Welches CRS würden Sie auswählen?', 'Übung · Entscheiden und begründen',68,72,
        'Die drei Codes der vorherigen Folien dürfen nachgeschlagen werden. 45 Sekunden allein, 90 Sekunden zu zweit, anschließend drei kurze Begründungen sammeln. '
        'Auf Einheit, Gebiet und Zweck achten. Keine detailgenauen Vermessungsfragen oder Sonderfälle voraussetzen. '
        'Erwartete Antworten auf nächster Folie: 4326, 25832, 3857. Die Aufgaben festigen die CRS-Auswahl in der Sitzung.',COURSE+'unit09-03_projektionen.html')
    steps(p,[('A · Artenbeobachtungen weltweit speichern','Die Positionen liegen als Länge und Breite vor.'),
             ('B · Entfernungen rund um Marburg berechnen','Sie benötigen eine geeignete Ebene mit Meterkoordinaten.'),
             ('C · Daten mit üblichen Webkartenkacheln anzeigen','Es geht um die Darstellung im Browser.')],gap=150)
    band(p,'Zur Wahl: EPSG:4326   /   EPSG:25832   /   EPSG:3857')

    p=slide('Gebiet, Einheit und Zweck zusammen prüfen', 'Auflösung · CRS auswählen',72,75,
        'Jede Auswahl begründen lassen, nicht nur den Code nennen. A: weltweite Winkelkoordinaten, 4326. B: regionale Analyse bei Marburg in Metern, 25832. '
        'C: gemeinsame Darstellung mit den in der Aufgabe gemeinten Webkartenkacheln, 3857. '
        'Das CRS der ursprünglichen Fachdaten muss dafür nicht ebenfalls 3857 sein; die Darstellung kann sie transformieren. '
        'Bei realen Datensätzen das Ausgangs-CRS aus verlässlichen Metadaten übernehmen. Nicht anhand der Wunschaufgabe ein Ausgangs-CRS erfinden.',COURSE+'unit09-03_projektionen.html')
    table(p,['Zweck','CRS','Begründung'],[
        ['A · Speichern','EPSG:4326','Weltweite Winkelkoordinaten'],
        ['B · Messen','EPSG:25832','Passende Zone, Meter'],
        ['C · Webkarte','EPSG:3857','Passend zu den Kartenkacheln']],
        [360,390,680],row_h=108,size=24)
    text(p,110,690,1390,95,'Webkarte und ausgegebene Positionskoordinaten\nkönnen unterschiedliche CRS verwenden.',25,TEAL,True)

    p=slide('Zuweisen und Transformieren unterscheiden', '03 · Typische Fehler vermeiden',75,79,
        'Zuweisen teilt der Software mit, wie die bereits vorhandenen Zahlen interpretiert werden sollen. Das ist zum Ergänzen oder Korrigieren einer bekannten CRS-Angabe da. Die Zahlen bleiben gleich, die Interpretation ändert sich. '
        'Transformieren rechnet zwischen bekanntem Ausgangs- und Ziel-CRS um. Der reale Ort bleibt innerhalb der Transformationsgenauigkeit derselbe. '
        'Die Position muss nicht neu vermessen werden. Fehlerhaft zugewiesene Ausgangssysteme führen auch bei anschließender Transformation zu falschen Ergebnissen. '
        'Die Beispiele mündlich auf Grad versus Meter beziehen, ohne einen QGIS-Dialog einzuführen. Die Abbildung aus der Kursseite zeigt zusätzlich den Fehler, Gradwerte nur als Meter zu etikettieren.',
        COURSE+'unit09-03_projektionen.html\nBild: assets/images/unit09/zuweisen-transformieren.svg')
    card(p,85,235,830,205,'CRS zuweisen','Koordinaten bleiben gleich.\nDie bekannte Interpretation wird ergänzt.',size=25)
    card(p,85,475,830,205,'Daten transformieren','Koordinaten werden umgerechnet.\nDer reale Ort bleibt derselbe.',size=25)
    picture(p,ROOT/'assets/images/unit09/zuweisen-transformieren.svg',1040,210,450,591)

    p=slide('Was wäre hier der richtige nächste Schritt?', 'Abstimmung · CRS-Fehler',79,82,
        'Das Beispiel vollständig vorlesen. 30 Sekunden einzeln entscheiden, danach A/B/C per Handzeichen. '
        'Wenn die Gruppe uneinig ist: 45 Sekunden Nachbarschaftsgespräch und erneut abstimmen. '
        'Eine Begründung hören, dann auflösen. Hier sind die Quellmetadaten ausdrücklich bekannt; es geht nicht um Raten.',COURSE+'unit09-03_projektionen.html')
    text(p,100,215,1400,142,'Die Quelle nennt WGS 84 und (longitude, latitude).\nWerte: (8.77, 50.81). In der Datei fehlt die CRS-Angabe.\nZiel: später Entfernungen rund um Marburg berechnen.',26,bold=True)
    steps(p,[('A · Direkt UTM zuweisen','Die Werte sollen schließlich Meter sein.'),
             ('B · WGS 84 zuweisen, dann nach UTM transformieren','Zuerst die vorhandenen Werte korrekt interpretieren.'),
             ('C · Verschiedene CRS ausprobieren','Bis der Punkt ungefähr richtig aussieht.')],y=400,gap=104)
    band(p,'A, B oder C? Welche Begründung überzeugt Sie?')

    p=slide('Erst richtig zuweisen, dann umrechnen', 'Auflösung · CRS-Fehler',82,85,
        'B ist richtig. Das Ausgangs-CRS ist durch die Quelle bekannt. 4326 zuweisen ändert die Werte nicht; danach können die Daten nach 25832 transformiert werden. '
        'Direktes Zuweisen von 25832 würde die Gradwerte als Meter interpretieren. Das ist keine Umrechnung. '
        'Ohne verlässliche Quelle wäre der nächste Schritt Recherche nach dem Ausgangs-CRS, nicht eine Vermutung als Tatsache einzutragen.',COURSE+'unit09-03_projektionen.html')
    steps(p,[('Quelle prüfen','WGS 84 und Reihenfolge sind dokumentiert.'),
             ('EPSG:4326 zuweisen','Die vorhandenen Gradwerte bleiben unverändert.'),
             ('Nach EPSG:25832 transformieren','Neue Meterwerte, derselbe Ort bei Marburg.')],gap=150)
    band(p,'B ist richtig: Zuweisen ersetzt keine Transformation.')

    p=slide('Exit-Ticket: Was nehmen Sie mit?', 'Abschluss · Ohne Nachschlagen',85,88,
        'Eine der drei Fragen passend zum Sitzungsverlauf auswählen. Eine Minute zu zweit formulieren lassen und anschließend eine gemeinsame Antwort sichern; nicht alle drei Fragen als zusätzliche Pflichtaufgabe behandeln. '
        'Erwartet je nach Auswahl: 1. Achsen/Reihenfolge, Einheit und CRS. 2. Beispielsweise EPSG:25832, passende regionale Zone und Meter; keine exakte Verzerrungsfreiheit behaupten. '
        '3. Die Koordinatenwerte werden umgerechnet, der reale Ort bleibt derselbe. '
        'Bei einer größeren Unsicherheit diese als Frage für die nächste Sitzung notieren. Keine Abgabeplattform voraussetzen.',COURSE+'unit09-00_overview.html')
    steps(p,[('A · Was fehlt bei (8.77, 50.81)?','Nennen Sie die nötigen Zusatzangaben.'),
             ('B · Welches CRS würden Sie für Marburg prüfen?','Begründen Sie Ihre Wahl für Entfernungsmessungen.'),
             ('C · Was passiert beim Transformieren?','Was ändert sich – und was bleibt gleich?')],gap=150)
    band(p,'Eine Frage auswählen → zu zweit formulieren → gemeinsam sichern')

    p=slide('Nachbereitung und nächster Schritt', 'Abschluss · Unit 09',88,90,
        'Als einzige Übungsaufgabe die JiTT-Fragen zu Unit 09 im ILIAS-Kurs beantworten lassen. '
        'Die Fragen und die Bearbeitungsfrist stehen in ILIAS; der konkrete Link ist auf der Kursseite noch zu ergänzen. '
        'Die Antworten dienen der Nachbereitung und zeigen Verständnisfragen für den Einstieg in die nächste Sitzung. '
        'Studierende können das Onlinematerial zur Vorbereitung auf den nächsten Termin nutzen; dies ist nach Absprache keine Voraussetzung für die Teilnahme. '
        'Unit 10 führt in QGIS ein. Danach zur letzten Folie mit dem Dank wechseln. Die beiden dazwischenliegenden Folien sind Reserve und Quellen.',COURSE+'unit09-04_assignment.html')
    card(p,85,235,695,420,'Übungsaufgabe: JiTT-Fragen','Beantworten Sie die JiTT-Fragen\nzu Unit 09 im ILIAS-Kurs.\n\nDie Fragen und die Frist\nfinden Sie in ILIAS.',size=25)
    card(p,820,235,695,420,'Ausblick: Unit 10','Die Grundlagen in QGIS nutzen.\n\nDas Onlinematerial steht zur freiwilligen Vorbereitung bereit.',size=27)
    link=text(p,110,665,1380,48,'Hinweis zu den JiTT-Fragen: HTML-Lernumgebung → Unit 09',23,TEAL,True)
    hyperlink(link,COURSE+'unit09-04_assignment.html')
    band(p,'Die JiTT-Fragen sind Ihre einzige Übungsaufgabe zu Unit 09.',size=23)

    p=slide('Dezimalgrad selbst berechnen', 'Reserve · Koordinatenformate',0,0,
        'Nur bei Bedarf anstelle einer anderen kurzen Übung einsetzen oder als Nachschlagefolie anbieten. '
        'Für positive Gradangaben: Grad + Minuten/60 + Sekunden/3600. Für Süd oder West den gesamten Betrag negativ setzen. '
        'Beispielaufgabe: 8° 46′ 12″ E = 8 + 46/60 + 12/3600 = 8,77° E. '
        'Für 8° 46′ 12″ W wäre das Ergebnis −8,77°. Keine Rechenpflicht als zusätzliche Übungsaufgabe einführen.',COURSE+'unit09-02_koordinaten.html',reserve=True)
    text(p,110,230,1380,100,'Dezimalgrad = Grad + Minuten / 60 + Sekunden / 3600',30,TEAL,True)
    card(p,85,365,1430,240,'Beispiel: 50° 48′ 36″ N','50 + 48/60 + 36/3600 = 50,81°',size=37)
    band(p,'Probieren Sie: 8° 46′ 12″ E. Passt das ungefähr zu Marburg?')

    p=slide('Materialien und fachliche Quellen', 'Reserve · Zum Nachschlagen',0,0,
        'Fachliche Grundlage sind die fünf aktuellen Markdown-Seiten von Unit 09. Diagramme wurden als bearbeitbare Vektorformen eigens für diese Präsentation erstellt. '
        'Der Projektionsvergleich verwendet mathematisch projizierte gleich große Kugelkalotten, keine realen Länderflächen. '
        'Die Kursillustration auf der Orientierungsfolie stammt aus dem vorhandenen KI-generierten Kursasset. '
        'Layout und Master: präs_ms02_powerpoint_de.pptx; Foto-/Kartenmotiv auf Titel und Abschluss: fb19-praesentationsvorlage_16-9-format.pot. '
        'Externe PROJ-Dokumentation zur Prüfung von Achsenreihenfolge und Projektionen abgerufen am 07.09.2026. '
        'CRS-Definitionen zusätzlich mit lokalem projinfo geprüft. Die Folien enthalten weder externe Live-Demos noch verpflichtende Softwareinstallationen.',
        '\n'.join([COURSE+'unit09-00_overview.html',PROJ+'faq.html',PROJ+'usage/quickstart.html',
                    PROJ+'operations/projections/merc.html',PROJ+'operations/projections/cea.html',
                    PROJ+'operations/projections/webmerc.html']),reserve=True)
    links=[('GeoMOER · Kursmaterial und JiTT-Hinweis',COURSE+'unit09-00_overview.html'),
           ('PROJ · Achsenreihenfolge / FAQ',PROJ+'faq.html'),
           ('PROJ · WGS 84 und UTM / Quick start',PROJ+'usage/quickstart.html'),
           ('PROJ · Mercator',PROJ+'operations/projections/merc.html'),
           ('PROJ · Flächentreue Zylinderprojektion',PROJ+'operations/projections/cea.html'),
           ('PROJ · Web Mercator',PROJ+'operations/projections/webmerc.html')]
    for i,(label,url) in enumerate(links):
        sh=text(p,110,222+i*71,1380,60,label,25,TEAL,True)
        hyperlink(sh,url)
    text(p,110,676,1390,124,'Layout: Uni-Marburg-Vorlage · Titel-/Abschlussbild: FB19-Vorlage\nDiagramme: eigene Vektordarstellungen · Kursillustration: KI-generiert\nFachliche Prüfung: 07.09.2026',17,MUTED)

    p=slide('Vielen Dank für Ihre Aufmerksamkeit','Abschluss',90,90,
        'Die Sitzung mit dieser Folie beenden. Der Wortlaut entspricht der gewünschten Abschlussformulierung. '
        'Die Abschlussgestaltung nutzt den Kontakt-Master der universitären Vorlage sowie das originale Foto-/Kartenmotiv aus der FB19-Titelseite.',str(TEMPLATE),kind='closing')
    box(p,44,44,809,807,0xF7DEED)
    picture(p,FB19_IMAGE,915,350,640,640*135/394)
    text(p,100,380,700,250,'Vielen Dank für Ihre Aufmerksamkeit',41,INK)
    text(p,165,710,620,110,'Geodaten · Unit 09\nFachbereich 19 · Geographie',18,INK)


def main():
    global DOC, MASTERS
    with tempfile.TemporaryDirectory(prefix='geomoer-unit09-') as profile:
        pipe='geomoer_unit09_' + uuid.uuid4().hex
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
            # Start from the supplied template and retain its native slide masters.
            legacy=desktop.loadComponentFromURL(FB19.as_uri(),'_blank',0,(prop('Hidden',True),))
            legacy_export=Path(profile)/'fb19.pptx'
            legacy.storeToURL(legacy_export.as_uri(),(prop('FilterName','Impress MS PowerPoint 2007 XML'),))
            legacy.close(True)
            FB19_IMAGE.parent.mkdir(exist_ok=True)
            with ZipFile(legacy_export) as archive:
                FB19_IMAGE.write_bytes(archive.read('ppt/media/image2.png'))
            DOC=desktop.loadComponentFromURL(TEMPLATE.as_uri(),'_blank',0,(prop('Hidden',True),))
            masters=DOC.getMasterPages()
            MASTERS={masters.getByIndex(i).Name:masters.getByIndex(i) for i in range(masters.Count)}
            pages=DOC.getDrawPages()
            for i in range(pages.Count-1,-1,-1):
                if i != 2:pages.remove(pages.getByIndex(i))
            DOC.DocumentProperties.Title='Unit 09 – Geodaten, Koordinaten und Projektionen'
            DOC.DocumentProperties.Subject='Geodaten · Unit 09 · Präsenzlehre'
            DOC.DocumentProperties.Author='GeoMOER'
            build()
            pptx=OUT / 'unit09_praesenz.pptx'
            DOC.storeAsURL(pptx.as_uri(),(prop('FilterName','Impress MS PowerPoint 2007 XML'),prop('Overwrite',True)))
            DOC.close(True)
            # Render the actual delivered PPTX, not a separate approximation.
            DOC=desktop.loadComponentFromURL(pptx.as_uri(),'_blank',0,(prop('Hidden',True),))
            assert DOC.getDrawPages().Count == len(RECORDS)
            DOC.storeToURL((OUT/'unit09_praesenz.pdf').as_uri(),(prop('FilterName','impress_pdf_Export'),prop('Overwrite',True),
                prop('FilterData',(prop('ExportNotesPages',False),prop('ExportHiddenSlides',True),prop('UseTaggedPDF',True)))))
            DOC.close(True)
            with (OUT/'moderation.md').open('w') as fp:
                fp.write('# Unit 09 – Moderation\n\nTitelfolie, 27 Hauptfolien für 90 Minuten, zwei Reserve-/Quellenfolien und eine Abschlussfolie. Zeitangaben stehen nur in diesen Notizen.\n\n')
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


if __name__ == '__main__':
    main()
