#!/usr/bin/env python3
"""Rebuild the additional WP12 teaching SVGs; no course data are modified."""
import argparse
from html import escape
from pathlib import Path
from statistics import quantiles

ROOT = Path(__file__).resolve().parents[2]
INK = '#263238'
BLUE = '#1565a7'
TEAL = '#227564'
ORANGE = '#b45309'
PALETTE = ['#e4eff7', '#bdd7e7', '#7eb3d1', '#367fab', '#164568']
HEIGHTS = [100, 110, 120, 130, 140, 150, 160, 170, 190, 500]
FINE = [[100, 100, 200, 200], [100, 180, 200, 200],
        [140, 140, 240, 240], [140, 140, 240, 320]]


class Figure:
    def __init__(self, unit, name, height, title, desc):
        self.path = ROOT / f'docs/assets/images/unit{unit:02}/{name}.svg'
        self.height = height
        self.parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="640" height="{height}" '
                      f'viewBox="0 0 640 {height}" role="img" aria-labelledby="title description">',
                      f'<title id="title">{escape(title)}</title>',
                      f'<desc id="description">{escape(desc)}</desc>',
                      '<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" '
                      'markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
                      f'<path d="M0 0L10 5L0 10Z" fill="{INK}"/></marker></defs>',
                      '<rect width="640" height="100%" fill="#f7f8fa"/>',
                      f'<g font-family="sans-serif" fill="{INK}">']
        self.text(24, 42, title, 28, True)

    def raw(self, s):
        self.parts.append(s)

    def text(self, x, y, value, size=24, bold=False, fill=INK, anchor='start'):
        self.raw(f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{700 if bold else 400}" '
                 f'fill="{fill}" text-anchor="{anchor}">{escape(str(value))}</text>')

    def lines(self, x, y, lines, size=24, step=32, **kw):
        for i, value in enumerate(lines):
            self.text(x, y + i * step, value, size, **kw)

    def rect(self, x, y, w, h, fill='white', stroke='#b7c4cc', sw=1.5, rx=0):
        self.raw(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" '
                 f'stroke="{stroke}" stroke-width="{sw}" rx="{rx}"/>')

    def line(self, x1, y1, x2, y2, color=INK, width=2, dash=False, arrow=False):
        self.raw(f'<path d="M{x1} {y1}L{x2} {y2}" fill="none" stroke="{color}" stroke-width="{width}"'
                 + (' stroke-dasharray="8 6"' if dash else '')
                 + (' marker-end="url(#arrow)"' if arrow else '') + '/>')

    def circle(self, x, y, r=8, fill=BLUE, stroke='white', sw=2):
        self.raw(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')

    def pathline(self, points, color=BLUE, width=4, dash=False):
        self.raw('<polyline points="'+' '.join(f'{x},{y}' for x,y in points)+'" '
                 f'fill="none" stroke="{color}" stroke-width="{width}" stroke-linejoin="round"'
                 + (' stroke-dasharray="8 6"' if dash else '') + '/>')

    def panel(self, y, h, title):
        self.rect(24, y, 592, h, rx=10)
        self.text(44, y+36, title, 25, True)

    def save(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text('\n'.join(self.parts+['</g>', '</svg>', '']), encoding='utf-8')
        print(self.path.relative_to(ROOT))


def unit09():
    f=Figure(9,'achsenreihenfolge',650,'Gleiche Zahlen, anderer Ort',
             'Im gleichen lon/lat-Gitter liegt A bei 8,77 Grad Ost und 50,81 Grad Nord. '
             'Nach Vertauschen liegt B bei 50,81 Grad Ost und 8,77 Grad Nord. Beide Paare sind formal gültig.')
    f.text(24,80,'WGS 84 · x = Länge, y = Breite',24)
    for value in range(0,61,10):
        x=80+value*8; y=450-value*5
        f.line(x,150,x,450,'#d1dce3',1)
        f.line(80,y,560,y,'#d1dce3',1)
        f.text(x,480,f'{value}°',22,anchor='middle')
        f.text(68,y+8,f'{value}°',22,anchor='end')
    f.text(80,125,'Breite (Nord)',24,True)
    f.text(370,520,'Länge (Ost)',24,True)
    for lon,lat,label,col in [(8.77,50.81,'A',BLUE),(50.81,8.77,'B',ORANGE)]:
        x=80+lon*8; y=450-lat*5
        f.line(x,450,x,y,col,2,True); f.line(80,y,x,y,col,2,True)
        f.circle(x,y,9,col); f.text(x+16,y-12,label,27,True,fill=col)
    f.lines(24,561,['A: (8,77; 50,81) → bei Marburg',
                     'B: (50,81; 8,77) → weit entfernt',
                     'Achsen prüfen, nicht nur Wertebereiche.'])
    f.save()

    from pyproj import Transformer
    east,north=Transformer.from_crs(4326,25832,always_xy=True).transform(8.77,50.81)
    assert (round(east),round(north)) == (483795,5628722)
    utm=f'{east:,.0f}; {north:,.0f}'.replace(',',' ')
    f=Figure(9,'zuweisen-transformieren',840,'Zuweisen oder umrechnen?',
             'Bekannte WGS-84-Koordinaten ohne CRS-Angabe erhalten EPSG:4326, ohne Zahlenänderung. '
             'Transformation nach EPSG:25832 ändert die Zahlen zu 483795 und 5628722 Metern. '
             'Bloßes Zuweisen von EPSG:25832 zu Gradwerten ist falsch.')
    f.panel(68,158,'1 · Vorhandenes CRS korrekt zuweisen')
    f.lines(44,143,['Zahlen: (8,77; 50,81) bleiben gleich.',
                    'Metadaten bestätigen: WGS 84 in Grad.',
                    'Fehlende CRS-Angabe → EPSG:4326'])
    f.line(320,235,320,266,arrow=True)
    f.panel(282,213,'2 · In ein anderes CRS transformieren')
    f.lines(44,356,['EPSG:4326 → EPSG:25832',
                    '(8,77; 50,81) Grad',
                    f'→ ({utm}) Meter',
                    'Andere Zahlen, derselbe Ort.'])
    f.panel(520,163,'Fehler · Gradwerte als Meter etikettieren')
    f.lines(44,596,['(8,77; 50,81) + EPSG:25832',
                    'Die Zahlen wurden nicht umgerechnet.',
                    'Die Lage wird falsch interpretiert.'])
    f.lines(24,727,['Zuweisen setzt die passende Beschreibung.',
                    'Transformieren berechnet neue Koordinaten.',
                    'UTM-Werte gerundet; Reihenfolge hier x, y.'])
    f.save()


def unit10():
    f=Figure(10,'layerreihenfolge',752,'Verdeckt heißt nicht gelöscht',
             'Dieselben zwei Punkte liegen innerhalb einer deckend gefüllten Fläche. '
             'Liegt die Fläche über den Punkten, sind diese verdeckt; liegen die Punkte oben, sind sie sichtbar.')
    for y,hidden,title in [(72,True,'A · Fläche über den Punkten'),(374,False,'B · Punkte über der Fläche')]:
        f.panel(y,280,title)
        f.text(44,y+79,'Oben liegt vorne',22)
        labels=['Fläche','Punkte'] if hidden else ['Punkte','Fläche']
        for i,label in enumerate(labels):
            f.rect(44,y+100+i*65,190,50,'#eef3f6')
            f.text(60,y+133+i*65,label)
        f.rect(285,y+75,303,170,'#eef3f6')
        def dots():
            f.circle(371,y+140,10,ORANGE); f.circle(495,y+185,10,ORANGE)
        if hidden:dots()
        f.rect(311,y+100,248,125,'#d0e5d9',TEAL,2)
        if not hidden:dots()
        f.text(301,y+269,'gleicher Kartenausschnitt',22)
    f.lines(24,698,['Nur die Reihenfolge ändert sich.', 'Beide Punktfeatures bleiben gespeichert.'])
    f.save()

    f=Figure(10,'wms-wfs',844,'Kartenbild oder Vektorobjekte?',
             'Dasselbe schematische Gebiet mit Fluss und Fläche: WMS liefert ein gerendertes Bild, '
             'WFS liefert Geometrien mit Attributen. Begrenzte WMS-Objektabfragen sind möglich.')
    for y,title in [(74,'WMS · gerendertes Kartenbild'),(376,'WFS · Features mit Attributen')]:
        f.panel(y,277,title)
        f.rect(44,y+65,220,140,'#edf3ed')
        f.rect(83,y+91,112,84,'#cfdfbe',TEAL,2)
        f.pathline([(54,y+77),(114,y+130),(154,y+141),(250,y+190)],BLUE,5)
        f.line(277,y+132,315,y+132,arrow=True)
        if y==74:
            f.lines(334,y+106,['Bild für den', 'angefragten', 'Ausschnitt'])
            f.text(44,y+249,'Gut für Orientierung und Hintergrund.',23)
        else:
            for yy,t in [(y+86,'ID 17 · Polygon'),(y+128,'Typ: Schutzgebiet')]:
                f.text(334,yy,t,22)
            f.lines(334,y+166,['Geometrie +', 'Attributwerte'],22)
            f.text(44,y+249,'Objekte auswählen und analysieren.',23)
    f.lines(24,698,['Gleicher sichtbarer Inhalt, andere Lieferung.',
                    'WMS kann einzelne Sachinfos abfragen;',
                    'das ersetzt keinen vollständigen Featurelayer.',
                    'Schematisches Beispiel, keine Dienstaufnahme.'],23)
    f.save()


def unit11():
    f=Figure(11,'beobachtungen-gleicher-ort',750,'Drei Records, zwei Positionen',
             'Beispielrecords A und B besitzen dieselbe Position, aber unterschiedliche Termine. '
             'C liegt an einer zweiten Position. Drei Features können daher als zwei sichtbare Symbole erscheinen.')
    f.panel(72,210,'Tabelle · drei Beispielbeobachtungen')
    for x,label in [(44,'ID'),(130,'Datum'),(370,'Position (x; y)')]:f.text(x,151,label,23,True)
    for i,(id,date,pos) in enumerate([('A','18.04.2026','(20; 30)'),('B','02.05.2026','(20; 30)'),('C','02.05.2026','(70; 50)')]):
        for x,t in [(44,id),(130,date),(370,pos)]:f.text(x,193+i*34,t,24)
    f.panel(310,264,'Karte · gleich große Punktsymbole')
    f.rect(44,373,552,171,'#edf3ed')
    # Linear transformation of the two synthetic local coordinates.
    for x,y,label in [(20,30,'A + B'),(70,50,'C')]:
        sx=70+x*6; sy=553-y*2.5
        f.circle(sx,sy,12,BLUE)
        f.text(sx+22,sy-10,label,25,True)
    f.lines(24,620,['A und B liegen exakt übereinander.',
                    'Anderer Termin: nicht sicher eine Dublette.',
                    'Recordzahl ist nicht gleich Individuenzahl.',
                    'Erfundene Daten in lokalen Koordinaten.'],23)
    f.save()

    f=Figure(11,'beobachtungsbias',858,'Mehr Suche, mehr Nachweise?',
             'Gedankenexperiment mit denselben zwölf Vorkommensorten. '
             'Eine Suche entlang des Wegs findet vier, eine flächige Suche alle zwölf. '
             'Nur für dieses Schema wird jedes Vorkommen im Suchbereich entdeckt.')
    f.lines(24,82,['Gedankenexperiment: Vorkommen unverändert.',
                   'Im Suchbereich wird hier jeder Ort entdeckt.'],23)
    points=[(x,y) for y in (35,80,125) for x in (45,165,285,405)]
    for y,all_area,title in [(142,False,'A · Suche nur am Weg: 4 Nachweise'),(442,True,'B · Suche im ganzen Gebiet: 12 Nachweise')]:
        f.panel(y,275,title)
        f.rect(44,y+60,552,163,'#edf3ed')
        f.rect(60,y+66 if all_area else y+117,520,150 if all_area else 48,'#d0dfe9','none')
        f.line(60,y+142,580,y+142,'#52616b',3,True)
        for px,py in points:
            sx=86+px; sy=y+62+py
            if all_area or py==80:f.circle(sx,sy,8,BLUE)
            else:f.circle(sx,sy,8,'white','#68777e',2)
        f.text(44,y+253,'Suchbereich blau hinterlegt · Weg gestrichelt',22)
    f.circle(36,754,8,BLUE); f.text(56,762,'dokumentiert',23)
    f.circle(298,754,8,'white','#68777e'); f.text(318,762,'im Schema vorhanden',23)
    f.lines(24,804,['In echten Nachweisdaten sind unentdeckte',
                    'Vorkommen und Suchaufwand oft unbekannt.'],23)
    f.save()


def unit12():
    f=Figure(12,'stuetzpunkte-generalisierung',715,'Stützpunkte bestimmen den Verlauf',
             'Ein Linienzug aus neun Stützpunkten wird auf fünf dieser Punkte reduziert. '
             'Anfang und Ende bleiben erhalten, dazwischen entfallen Details.')
    points=[(55,125),(112,68),(173,100),(225,57),(294,90),(367,138),(433,79),(501,111),(583,66)]
    reduced=points[::2]
    for y,title,p in [(75,'Detailliert · 9 Stützpunkte',points),(358,'Vereinfacht · 5 Stützpunkte',reduced)]:
        f.panel(y,256,title)
        if y==358:f.pathline([(x,yy+y) for x,yy in points],'#94a3ad',2,True)
        f.pathline([(x,yy+y) for x,yy in p],BLUE,4)
        for i,(x,yy) in enumerate(p):f.circle(x,yy+y,7,BLUE)
        f.text(44,y+207,'Punkte werden durch gerade Segmente verbunden.',22)
        f.text(44,y+238,'Endpunkte gleich; Details dazwischen verändern sich.',22)
    f.lines(24,658,['Gestrichelt: ursprünglicher Linienzug zum Vergleich.',
                    'Schematisch; mehr Punkte belegen keine Genauigkeit.'],22)
    f.save()

    f=Figure(12,'polygon-loch-multipart',805,'Loch oder getrennter Teil?',
             'Ein Polygon mit innerem Ring besitzt eine ausgesparte Fläche. '
             'Ein Multipart-Feature besteht aus zwei getrennten gefüllten Polygonen. Beide Beispiele haben je eine Tabellenzeile.')
    f.panel(76,277,'A · Polygon mit Loch')
    f.raw(f'<path d="M55 145H305V280H55Z M132 181H230V248H132Z" '
          f'fill="#d0e5d9" fill-rule="evenodd" stroke="{TEAL}" stroke-width="3"/>')
    f.text(148,223,'Loch',24)
    f.lines(332,185,['Äußerer Ring', 'Innerer Ring', 'Loch ausgespart'],23)
    f.rect(44,296,550,40,'#eef3f6'); f.text(56,324,'ID A · 1 Feature · 1 Tabellenzeile',23)
    f.panel(379,283,'B · Multipart-Feature')
    f.rect(56,452,111,134,'#d0e5d9',TEAL,3)
    f.rect(214,479,96,92,'#d0e5d9',TEAL,3)
    f.text(84,530,'B',26,True); f.text(248,530,'B',26,True)
    f.lines(332,485,['Zwei getrennte', 'Teile, aber', 'ein Feature'],23)
    f.rect(44,605,550,40,'#eef3f6'); f.text(56,633,'ID B · 1 Feature · 1 Tabellenzeile',23)
    f.lines(24,709,['Grün: Fläche, die zur Geometrie gehört.',
                    'Weiß: Loch oder Raum zwischen den Teilen.',
                    'Schematische Geometrien, keine realen Gebiete.'],23)
    f.save()

    f=Figure(12,'auswahl-zuschneiden',852,'Auswählen oder zuschneiden?',
             'Dieselbe waagerechte Linie L schneidet dasselbe rechteckige Polygon. '
             'Intersects wählt die vollständige Linie aus. Clip gibt nur den innerhalb des Polygons liegenden Abschnitt aus.')
    for y,title,mode in [(75,'Eingang · Linie L und Polygon','input'),(295,'Auswahl mit intersects · ganze Linie','select'),(515,'Clip · nur Abschnitt im Polygon','clip')]:
        f.panel(y,199,title)
        f.rect(198,y+65,246,80,'#d0e5d9',TEAL,2)
        if mode=='clip':
            f.line(64,y+106,575,y+106,'#aab4bb',2,True)
            f.line(198,y+106,444,y+106,BLUE,6)
        else:
            if mode=='select':f.line(64,y+106,575,y+106,'#f1bd4f',13)
            f.line(64,y+106,575,y+106,BLUE,5)
        f.text(70,y+83,'L',24,True)
        label={'input':'Die Linie reicht über beide Grenzen hinaus.',
               'select':'Auch der Auswahlexport behält die ganze Linie.',
               'clip':'Nur die Ausgabe erhält eine neue Geometrie.'}[mode]
        f.text(44,y+178,label,22)
    f.lines(24,758,['Unit 12 verwendet Auswahl und Auswahlexport.',
                    'Zuschneiden ist hier nur der begriffliche Vergleich.',
                    'Die Eingabedaten bleiben jeweils erhalten.'],22)
    f.save()


def grid(f, x, y, values, cell, colors, lo, hi, mark=None):
    for row,line in enumerate(values):
        for col,value in enumerate(line):
            index=min(len(colors)-1, int((value-lo)/(hi-lo)*len(colors)))
            color=colors[index]
            f.rect(x+col*cell,y+row*cell,cell,cell,color,'#52616b',1)
            f.text(x+(col+.5)*cell,y+(row+.5)*cell+8,value,24,True,
                   'white' if index>=len(colors)-2 else INK,'middle')
            if (row,col)==mark:f.rect(x+col*cell+4,y+row*cell+4,cell-8,cell-8,'none',ORANGE,4)


def unit13():
    coarse=[[sum(FINE[y+dy][x+dx] for dy in range(2) for dx in range(2))/4
             for x in (0,2)] for y in (0,2)]
    assert coarse==[[120,200],[140,260]]
    coarse=[[int(v) for v in row] for row in coarse]
    f=Figure(13,'raster-vergroebern',945,'Gleicher Ausschnitt, gröbere Zellen',
             'Ein 40 mal 40 Meter großer Ausschnitt mit sechzehn 10-Meter-Zellen wird durch Blockmittelwerte '
             'zu vier 20-Meter-Zellen. Aus 100,100,100,180 wird 120; der Höchstwert 320 verschwindet im Mittelwert 260.')
    f.panel(76,334,'10-m-Zellen · 4 × 4 Werte')
    grid(f,48,140,FINE,60,PALETTE,100,320)
    f.lines(328,187,['Ausschnitt:', '40 m × 40 m', '', 'Höhenwerte in m', 'Maximum: 320 m'],23)
    f.panel(438,334,'20-m-Zellen · 2 × 2 Blockmittelwerte')
    grid(f,48,503,coarse,120,PALETTE,100,320)
    f.lines(328,552,['Gleicher Ausschnitt,', 'gleiche Farbskala.', '', 'Maximum jetzt: 260 m'],23)
    f.lines(24,818,['Beispiel links oben: (100 + 100 + 100 + 180)',
                    '/ 4 = 120 m. Kleine Details gehen verloren.',
                    'Feineres Speichern holt die Details nicht zurück.',
                    'Erfundene Höhen; keine Marburger Messwerte.'],23)
    f.save()

    f=Figure(13,'rasterausrichtung',710,'Gleiche Zellgröße, anderes Gitter',
             'Zwei 10-Meter-Gitter im gleichen lokalen Meterkoordinatensystem. '
             'Gitter B beginnt fünf Meter weiter östlich. Die erste Zelle beider Gitter deckt verschiedene Flächen ab.')
    f.lines(24,83,['Gitter A: durchgezogen · Gitter B: gestrichelt',
                   'B ist um 5 m nach Osten verschoben.'],23)
    ox,oy,s=85,410,12
    for x in (0,10,20,30):
        f.line(ox+x*s,oy-20*s,ox+x*s,oy,BLUE,3)
        f.line(ox+(x+5)*s,oy-20*s,ox+(x+5)*s,oy,ORANGE,3,True)
    for y in (0,10,20):
        f.line(ox,oy-y*s,ox+30*s,oy-y*s,BLUE,3)
        f.line(ox+5*s,oy-y*s,ox+35*s,oy-y*s,ORANGE,3,True)
        f.text(65,oy-y*s+8,str(y),23,anchor='end')
    for x in (0,10,20,30):f.text(ox+x*s,445,str(x),23,anchor='middle')
    f.text(ox+35*s,484,'x (m)',23,anchor='end')
    f.text(32,150,'y (m)',23)
    f.line(ox,oy+63,ox+5*s,oy+63,arrow=True)
    f.text(ox+72,oy+72,'5 m Versatz',23)
    f.lines(24,542,['Erste Zelle A: x = 0 bis 10 m',
                    'Erste Zelle B: x = 5 bis 15 m',
                    'Dieselbe Spaltennummer ≠ dieselbe Bodenfläche.',
                    'Vor Zellberechnungen auch Ausrichtung prüfen.',
                    'Lokales Meterkoordinatensystem; schematisch.'],23)
    f.save()

    values=[[200,210,220],[210,220,230],[220,230,240]]
    second=['#f0e7f1','#d8bedc','#b389ba','#80538a','#4c2859']
    f=Figure(13,'rasterwerte-farben',735,'Andere Farben, dieselben Werte',
             'Dieselbe 3-mal-3-Höhenmatrix von 200 bis 240 Metern wird blau und violett dargestellt. '
             'Die mittlere markierte Zelle bleibt bei 220 Metern; weder Werte noch Zellpositionen ändern sich.')
    for y,title,colors in [(76,'A · blaue Farbskala',PALETTE),(351,'B · violette Farbskala',second)]:
        f.panel(y,255,title)
        grid(f,48,y+64,values,54,colors,200,240,mark=(1,1))
        for i,c in enumerate(colors):f.rect(278+i*57,y+83,57,27,c,'none')
        f.text(278,y+140,'200 m',23); f.text(564,y+140,'240 m',23,anchor='end')
        f.lines(278,y+183,['Markierte Zelle:', '220 m in beiden Bildern'],23)
    f.lines(24,651,['Die Farbskala gehört zur Darstellung.',
                    'Position und gespeicherte Höhe bleiben gleich.',
                    'Erfundene Höhen; keine Marburger Messwerte.'],23)
    f.save()


def unit14():
    f=Figure(14,'symbol-und-datenart',799,'Welche Eigenschaft wird sichtbar?',
             'Dieselben drei Punkte A, B, C mit Typ Wald, Offenland, Wald und Höhen 200, 250, 300 Meter. '
             'Kategorien werden als Kreis beziehungsweise Dreieck dargestellt; numerische Höhen durch geordnete Helligkeit.')
    for y, cells in [(84, ['Punkt', 'A', 'B', 'C']),
                     (116, ['Typ', 'Wald', 'Offenland', 'Wald']),
                     (148, ['Höhe', '200 m', '250 m', '300 m'])]:
        for x, value in zip([24, 196, 356, 528], cells):
            f.text(x, y, value, 23)
    for y,title in [(183,'Typ zeigen · Formen unterscheiden'),(456,'Höhe zeigen · Helligkeit ordnen')]:
        f.panel(y,251,title)
        for x,label,h in [(115,'A',200),(320,'B',250),(526,'C',300)]:
            f.text(x,y+80,label,24,True,anchor='middle')
            if y==183 and label=='B':
                f.raw(f'<path d="M{x} {y+100}L{x+18} {y+133}H{x-18}Z" fill="{BLUE}"/>')
            else:
                f.circle(x,y+119,17, BLUE if y==183 else PALETTE[(h-200)//25],INK,1.5)
        if y==183:
            f.lines(44,y+186,['Kreis = Wald · Dreieck = Offenland', 'Gleichrangige Kategorien, keine Zahlenfolge.'],23)
        else:
            for x,v in [(115,200),(320,250),(526,300)]:f.text(x,y+164,f'{v} m',23,anchor='middle')
            f.text(44,y+220,'Hell → dunkel: niedrige → hohe Geländehöhe',23)
    f.lines(24,749,['Positionen unverändert; nur das gezeigte Attribut',
                    'wechselt. Erfundene Beispieldaten.'],23)
    f.save()

    equal=[100,180,260,340,420,500]
    quantile=[100]+quantiles(HEIGHTS,n=5,method='inclusive')+[500]
    assert quantile==[100,118,136,154,174,500]
    f=Figure(14,'klassengrenzen-zahlen',1134,'Gleiche Werte, andere Klassen',
             'Zehn Höhen von 100,110,120,130,140,150,160,170,190,500 Metern in fünf Klassen. '
             'Gleiche Intervalle haben 8,1,0,0,1 Werte je Klasse, Quantile je zwei. '
             'Die Bandbreiten auf der Zahlenachse entsprechen den numerischen Klassenbreiten.')
    f.lines(24,83,['Beispielhöhen in m: 100, 110, 120, 130, 140,',
                   '150, 160, 170, 190, 500 · immer fünf Klassen'],23)
    for y,title,bounds,expected in [(142,'A · gleiche Intervalle',equal,[8,1,0,0,1]),
                                   (575,'B · Quantile',quantile,[2,2,2,2,2])]:
        f.panel(y,410,title)
        scale=lambda v: 55+(v-100)*1.30
        for i in range(5):f.rect(scale(bounds[i]),y+63,(bounds[i+1]-bounds[i])*1.30,34,PALETTE[i],INK,1)
        for i,value in enumerate(HEIGHTS):f.circle(scale(value),y+111+(i%2)*13,4,INK,'white',1)
        for value in (100,200,300,400,500):
            f.text(scale(value),y+154,value,22,anchor='middle')
        f.text(55,y+191,'Klasse / Grenzen (m)',23,True)
        f.text(576,y+191,'Anzahl',23,True,anchor='end')
        counts=[]
        for i in range(5):
            lo,hi=bounds[i:i+2]
            count=sum(lo<=v and (v<hi or i==4 and v<=hi) for v in HEIGHTS)
            counts.append(count)
            yy=y+229+i*34
            f.rect(45,yy-19,23,23,PALETTE[i],INK,1)
            interval=f'{lo:g} ≤ h '+('≤' if i==4 else '<')+f' {hi:g}'
            f.text(81,yy,f'{i+1}: {interval}',23)
            f.text(558,yy,count,23,True,anchor='middle')
        assert counts==expected
    f.lines(24,1028,['Punkte: identische Werte auf identischer Achse.',
                     'Quantile hier mit linearer Interpolation berechnet.',
                     'Leere Klassen sind bei gleichen Intervallen möglich.',
                     'Beispieldaten, nicht die 35 Marburger Nachweise.'],23)
    f.save()


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--unit',type=int,choices=range(9,15))
    args=parser.parse_args()
    for unit in range(9,15):
        if args.unit is None or unit==args.unit:
            globals()[f'unit{unit:02}']()
