#!/usr/bin/python3
"""Build the Unit 12 classroom deck with LibreOffice UNO (no downloads).

Run with /usr/bin/python3, which provides the distro's python3-uno package.
Text, tables and diagrams remain editable PowerPoint shapes. Shared drawing
helpers are loaded from the Unit 10 builder so the slide series stays aligned.
"""
from pathlib import Path
import importlib.util
import shutil
import subprocess
import tempfile
import time
import uuid
from zipfile import ZipFile

import uno

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[1]
TEMPLATE = ROOT/'slides/Vorlagen/präs_ms02_powerpoint_de.pptx'
FB19 = ROOT/'slides/Vorlagen/fb19-praesentationsvorlage_16-9-format.pot'
FB19_IMAGE = OUT/'assets/fb19-marburg-europa.png'
PUBLISHED_PDF = ROOT/'assets/pdfs/Geodaten_Slides_Unit12.pdf'
COURSE = 'https://geomoer.github.io/moer-bsc-geodaten/unit12/'
QDOC = 'https://docs.qgis.org/3.40/en/docs/user_manual/'
GEOPORTAL = 'https://www.geoportal.hessen.de/'
HLNUG_NATURE = 'https://www.hlnug.de/themen/geografische-informationssysteme/geodienste/naturschutz'
HLNUG_WATER = 'https://www.hlnug.de/themen/geografische-informationssysteme/geodienste/wasser'
RECORDS = []

spec = importlib.util.spec_from_file_location('unit10_slide_helpers', OUT.parent/'unit10/build_slides.py')
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)

W, H, SCALE = base.W, base.H, base.SCALE
INK, TEAL, ORANGE = base.INK, base.TEAL, base.ORANGE
WHITE, PALE, GRID, MUTED = base.WHITE, base.PALE, base.GRID, base.MUTED
prop = base.prop
box, text, poly, line = base.box, base.text, base.poly, base.line
hyperlink, picture = base.hyperlink, base.picture
band, card, steps, table = base.band, base.card, base.steps, base.table


def slide(title, section, start, end, notes, source='', reserve=False, kind='content'):
    n = len(RECORDS) + 1
    pages = DOC.getDrawPages()
    page = pages.getByIndex(0) if n == 1 else pages.insertNewByIndex(n - 1)
    for i in range(page.Count - 1, -1, -1):
        page.remove(page.getByIndex(i))
    page.setMasterPage(MASTERS[{'title': 'Titelfolie', 'closing': 'Kontakt'}.get(kind, 'Titel und Inhalt')])
    page.IsFooterVisible = False
    page.IsPageNumberVisible = False
    page.IsDateTimeVisible = False
    page.Width, page.Height = W, H
    page.Name = f'{n:02d} {title}'
    if kind == 'content':
        text(page, 100, 48, 1400, 114, title, 34, bold=True)
        text(page, 100, 173, 1400, 30, section.upper(), 12, TEAL, True)
        text(page, 100, 852, 1100, 30,
             'Universität Marburg | Fachbereich 19 · Geographie | Geodaten · Unit 12', 10, MUTED)
        text(page, 1512, 850, 42, 25, str(n), 10, INK, False, 'CENTER')
    timing = ('Reserve; nicht zusätzlich in die 90 Minuten einplanen.' if reserve else
              'Titelfolie vor dem Einstieg zeigen.' if kind == 'title' else
              'Abschluss nach der Nachbereitung; kein zusätzlicher Zeitblock.' if kind == 'closing' else
              f'Zeitfenster: Minute {start}–{end} ({end-start} Minuten).')
    note_text = timing + '\n\n' + notes
    if source:
        note_text += '\n\nQuellen / Anschluss an die HTML-Lernumgebung:\n' + source
    notes_page = page.getNotesPage()
    for i in range(notes_page.Count):
        shape = notes_page.getByIndex(i)
        if shape.ShapeType == 'com.sun.star.presentation.NotesShape':
            shape.String = note_text
    RECORDS.append(dict(number=n, title=title, section=section, start=start, end=end,
                        reserve=reserve, kind=kind, notes=note_text))
    return page


def build():
    overview = COURSE+'unit12-00_overview.html'
    vectors = COURSE+'unit12-01_vektordaten.html'
    portals = COURSE+'unit12-02_geoportale.html'
    qgis = COURSE+'unit12-03_vektoren_qgis.html'
    assignment = COURSE+'unit12-04_assignment.html'
    core = 'https://geomoer.github.io/moer-bsc-geodaten/material/qgis-kernpfade.html#unit12'

    p = slide('Linien, Polygone und räumliche Auswahl', 'Unit 12', 0, 0,
        'Titelfolie beim Ankommen zeigen. Die Sitzung ist für 90 Minuten mit 100–150 Bachelor- und Lehramtsstudierenden ausgelegt. '
        'Vorbereitendes Lesen wird nicht vorausgesetzt. QGIS 3.40 und das vollständig entpackte Marburger Übungspaket müssen verfügbar sein. '
        'Erwarteter Punkteeingang ist gbif_checked aus Unit 11 oder der schemaidentische Ersatzlayer.', str(TEMPLATE), kind='title')
    picture(p, FB19_IMAGE, 44, 350, 539, 539*135/394)
    text(p, 625, 285, 850, 300, 'Linien, Polygone und\nräumliche Auswahl', 44, WHITE)
    text(p, 625, 614, 840, 70, 'Unit 12', 28, WHITE)
    text(p, 625, 744, 840, 100, 'Fachbereich 19 · Geographie\nPhilipps-Universität Marburg', 19, WHITE)

    p = slide('JiTT · Rückblick auf Unit 11', 'Platzhalter · vollständig austauschbar', 0, 10,
        'VOR DEM TERMIN: Den gesamten Platzhalter durch die aktuelle JiTT-Auswertung zu Unit 11 ersetzen. '
        'Bei Bedarf die Folie duplizieren. Nur tatsächliche, zusammengefasste und anonymisierte Rückmeldungen einsetzen. '
        'Die gesamte Phase dauert zehn Minuten. Verständnisfragen zu Punktdaten, GBIF, Koordinatenunsicherheit oder Export klären.')
    shape = box(p, 100, 237, 1400, 545, PALE, GRID)
    shape.Name = 'JiTT – vollständigen Block ersetzen'
    text(p, 180, 430, 1240, 130, '[Hier den vollständigen\nJiTT-Block einfügen]', 38, TEAL, False, 'CENTER')

    p = slide('Drei Geometrien gemeinsam auswerten', 'Unit 12 · Orientierung', 10, 11,
        'Den Ablauf ankündigen: Linien und Polygone verstehen, Datenquellen über Metadaten beurteilen, drei Layer prüfen, erst nach Attributen und dann räumlich auswählen und drei Ergebnislayer sichern.', overview)
    picture(p, ROOT/'assets/images/unit12/hero-unit12.jpg', 85, 225, 1430, 1430/6)
    for x, label, body in [(85, 'Geometrie lesen', 'Punkt, Linie und\nPolygon unterscheiden'),
                           (570, 'Auswahl planen', 'Attribut und\nLagebeziehung einsetzen'),
                           (1055, 'Ergebnis sichern', '10 · 4 · 106 prüfen\nund dokumentieren')]:
        card(p, x, 495, 460, 205, label, body, size=22)
    band(p, 'Leitfrage: Welche Nachweise und Gewässer schneiden ausgewählte Schutzgebiete?', size=21)

    p = slide('Punkt, Linie und Polygon', 'Vektormodell · Grundtypen', 11, 13,
        'An Unit 10 und 11 anknüpfen. Die Geometrie ist ein Modell für eine Fragestellung; das sichtbare Symbol besitzt zusätzliche Darstellungsbreite oder -größe. '
        'Jedes Feature bleibt mit genau einer Zeile seiner Attributtabelle verbunden.', vectors)
    for x, label, body in [(85, 'Punkt', 'Position\nkeine Fläche'),
                           (570, 'Linie', 'geordnete Stützpunkte\nräumlicher Verlauf'),
                           (1055, 'Polygon', 'geschlossener Ring\nGrenze und Inneres')]:
        card(p, x, 270, 460, 300, label, body, color=ORANGE if label == 'Polygon' else TEAL, size=25)
    band(p, 'Geometrie: wo und in welcher Form · Attribute: welche Eigenschaften', size=23)

    p = slide('Welche Geometrie passt zur Frage?', 'Vektormodell · Nachbarschaftsgespräch', 13, 15,
        '60 Sekunden zu zweit: Für jede Frage genau einen primären Geometrietyp wählen und kurz begründen. Danach Handzeichen für Punkt, Linie oder Polygon. '
        'Die Auflösung folgt auf der nächsten Folie.', vectors)
    table(p, ['Frage', 'Geometrietyp'], [
        ['Wo mündet ein Nebenfluss?', '[Punkt / Linie / Polygon]'],
        ['Wie verläuft ein Gewässer?', '[Punkt / Linie / Polygon]'],
        ['Welche Fläche besitzt ein Schutzgebiet?', '[Punkt / Linie / Polygon]']], [1030, 400], y=245, row_h=105, size=23)
    band(p, 'Entscheiden Sie nach der benötigten Information, nicht nach dem Objektnamen.', size=21)

    p = slide('Lösung: Ort, Verlauf und Fläche', 'Vektormodell · Auflösung', 15, 17,
        'Die Lösungen knapp sichern. Bei der Mündung beschreibt ein Punkt den gesuchten Ort. Für den Verlauf wird eine Linie benötigt; für die Flächenausdehnung ein Polygon. '
        'Andere Modellierungen können für andere Fragen sinnvoll sein.', vectors)
    table(p, ['Frage', 'Modell', 'Begründung'], [
        ['Mündung', 'Punkt', 'gesuchte Position'],
        ['Gewässerverlauf', 'Linie', 'Reihenfolge und Verlauf'],
        ['Schutzgebietsfläche', 'Polygon', 'Grenze und Inneres']], [620, 300, 510], y=250, row_h=105, size=23)
    band(p, 'Dasselbe reale Objekt kann je nach Maßstab und Frage anders modelliert werden.', size=22)

    p = slide('Stützpunkte steuern den Linienverlauf', 'Vektormodell · Generalisierung', 17, 20,
        'Die Grafik von oben nach unten lesen. Zwischen benachbarten Stützpunkten liegen gerade Segmente. Weniger Stützpunkte ergeben hier eine vereinfachte Linie. '
        'Mehr Stützpunkte erlauben mehr Detail, belegen allein aber weder höhere Lagegenauigkeit noch bessere Datenqualität.', vectors+'\nBild: assets/images/unit12/stuetzpunkte-generalisierung.svg')
    picture(p, ROOT/'assets/images/unit12/stuetzpunkte-generalisierung.svg', 330, 215, 500, 500*715/640)
    card(p, 920, 285, 520, 180, 'Strichbreite', 'Darstellung – nicht reale Gewässerbreite', size=21)
    card(p, 920, 520, 520, 180, 'Generalisierung', 'Details passend zu Maßstab und Zweck reduzieren', color=ORANGE, size=20)

    p = slide('Ein Feature kann Loch oder mehrere Teile besitzen', 'Vektormodell · Polygone', 20, 22,
        'Links: Die Lochfläche gehört geometrisch nicht zum Polygon. Rechts: Zwei getrennte Flächen bilden gemeinsam ein Multipart-Feature und besitzen eine Tabellenzeile. '
        'Sichtbare Flächenteile daher nicht mit Featurezahl gleichsetzen.', vectors+'\nBild: assets/images/unit12/polygon-loch-multipart.svg')
    picture(p, ROOT/'assets/images/unit12/polygon-loch-multipart.svg', 350, 215, 455, 455*805/640)
    card(p, 900, 300, 520, 170, 'Loch', 'ausgesparte Innenfläche', size=23)
    card(p, 900, 525, 520, 170, 'Multipart', 'getrennte Teile · eine Tabellenzeile', color=ORANGE, size=22)

    p = slide('Räumliche Beziehungen unterscheiden', 'Vektormodell · Lagebezug', 22, 24,
        'Begriffe nicht als Synonyme verwenden. Die Richtung der Frage ist relevant: Der Punkt liegt innerhalb des Polygons; das Polygon enthält den Punkt. '
        'Heute wird für Punkte und Linien einheitlich schneidet/intersects verwendet.', vectors)
    table(p, ['Beziehung', 'Beispiel'], [
        ['innerhalb', 'Punkt liegt im Inneren eines Polygons'],
        ['enthält', 'Polygon enthält einen Punkt'],
        ['schneidet', 'Geometrien besitzen mindestens einen gemeinsamen Ort'],
        ['berührt', 'Grenzen treffen sich ohne Überlappung der Inneren']], [430, 1000], y=230, row_h=90, size=22)
    band(p, 'Die verwendete Beziehung gehört in die Ergebnisdokumentation.', size=22)

    p = slide('Zählt ein Punkt auf der Grenze mit?', 'Vektormodell · Grenzfall vormerken', 24, 25,
        'Nur die Frage stellen und A, B, C sprachlich verorten. Noch nicht vollständig auflösen; der Grenzfall wird in Minute 80 mit der tatsächlichen Auswahlregel und der Koordinatenunsicherheit erneut betrachtet.', vectors)
    box(p, 200, 270, 1200, 300, PALE, GRID)
    text(p, 250, 330, 1100, 100, 'A innen · B genau auf der Grenze · C außen', 34, INK, True, 'CENTER')
    text(p, 250, 465, 1100, 70, 'Welche Punkte wählt „schneidet“ – und welche „innerhalb“?', 28, TEAL, True, 'CENTER')
    band(p, 'Hypothese notieren · Auflösung in Minute 82', size=23)

    p = slide('Ein Geoportal ist noch kein Datensatz', 'Geoportale · Orientierung', 25, 27,
        'Geoportale bündeln Suche, Metadaten, Kartenansichten, Dienste und Downloads. Ein gefundener Eintrag ist noch kein analysierbarer Datensatz. '
        'Für die Leitfrage werden Feature-Geometrien und Attribute benötigt.', portals+'\n'+GEOPORTAL)
    for x, label, body in [(100, 'Suchen', 'Thema und Gebiet'), (475, 'Prüfen', 'Metadaten und Zugang'),
                           (850, 'Beziehen', 'Download oder WFS'), (1225, 'Nutzen', 'lokal dokumentieren')]:
        card(p, x, 285, 330, 275, label, body, size=22)
    band(p, 'Kartenansicht entdecken · Metadaten entscheiden · Features analysieren', size=22)

    p = slide('Kartenbild oder analysierbare Features?', 'Geoportale · WMS, WFS, Download', 27, 30,
        'Die drei Angebote vergleichen. WMS liefert ein gerendertes Kartenbild; daraus lassen sich nicht die benötigten Schutzgebietsfeatures auswählen. '
        'WFS und Download liefern Vektorfeatures. Für den stabilen Präsenzweg verwenden wir den vorbereiteten lokalen Snapshot.', portals)
    table(p, ['Angebot', 'Ergebnis', 'Heute analysierbar?'], [
        ['WMS', 'Kartenbild vom Server', 'nein · nur Darstellung'],
        ['WFS', 'Features mit Geometrie und Attributen', 'ja · wenn Dienst stabil'],
        ['Download', 'lokale Datendatei', 'ja · reproduzierbarer Snapshot']], [300, 750, 380], y=245, row_h=105, size=21)
    band(p, 'Für die Sitzung: lokale Vektordaten statt abhängiger Live-Suche.', size=23)

    p = slide('Metadaten beantworten die Eignungsfrage', 'Geoportale · Prüfraster', 30, 32,
        'In der großen Gruppe sechs Leitfragen sammeln. Fehlende Angaben bleiben als Einschränkung sichtbar. '
        'Ein bekanntes Dateiformat ersetzt keine Prüfung von Inhalt, Gebiet, Aktualität, Genauigkeit und Lizenz.', portals)
    table(p, ['Metadatum', 'Leitfrage'], [
        ['Inhalt / Geometrie', 'Welche Objekte und Attribute sind enthalten?'],
        ['Abdeckung / Stand', 'Für welches Gebiet und welchen Zeitpunkt?'],
        ['CRS / Genauigkeit', 'Passt der Raumbezug zur Analyse?'],
        ['Zugang / Lizenz', 'Download, WFS oder WMS – und welche Nutzung?']], [500, 930], y=230, row_h=90, size=22)
    band(p, 'Fehlt eine Angabe, ist die Eignung nur eingeschränkt beurteilbar.', size=22)

    p = slide('Unsere vorbereiteten Vektordaten', 'Geoportale · Quellenstand', 32, 34,
        'Die Tabelle als kompakten Metadatennachweis lesen. Abrufdatum ist nicht automatisch fachlicher Datenstand. '
        'Die Features schneiden das 20-km-Unterrichtsrechteck, bleiben aber vollständig und sind nicht an dessen Grenze abgeschnitten.', portals+'\n'+HLNUG_NATURE+'\n'+HLNUG_WATER)
    table(p, ['Datensatz', 'Herausgeber', 'Geometrie', 'Umfang'], [
        ['Schutzgebiete NSG/FFH', 'HMLU · HLNUG', 'MultiPolygon', '22'],
        ['Gewässernetz 1:25.000', 'HLNUG', 'MultiLineString', '412'],
        ['GBIF-Prüfergebnis', 'NABU|naturgucker via GBIF', 'Punkt', '56']], [520, 420, 320, 170], y=250, row_h=105, size=20)
    band(p, 'Gemeinsames Projekt- und Ausgabe-CRS: EPSG:25832', size=24)

    p = slide('Vom Layer zur dokumentierten Auswahl', 'Geoportale · Übergang zur Praxis', 34, 35,
        'Die Abbildung von links nach rechts lesen: drei Geometrietypen werden über Attribute und Lagebeziehungen verbunden. '
        'Die Auswahl wird nicht nur angezeigt, sondern mit Regel und Featurezahl als neuer Layer gespeichert.', vectors+'\nBild: assets/images/unit12/vektor-workflow.svg')
    picture(p, ROOT/'assets/images/unit12/vektor-workflow.svg', 200, 220, 1200, 540)
    band(p, 'Fragestellung → Datenquelle → Geometrie → Beziehung → Ergebnis', size=22)

    p = slide('Projekt und drei Eingangslayer vorbereiten', 'QGIS · Startzustand', 35, 38,
        'Projekt als unit12_vectors.qgz speichern und EPSG:25832 setzen. Zuerst das eigene Unit-11-Ergebnis laden; falls es fehlt, ersatz/unit11_results.gpkg verwenden. '
        'Gewässer und Schutzgebiete stammen aus data_raw/marburg_basis.gpkg.', qgis+'\n'+core)
    steps(p, [('Punkte laden', 'unit11_results.gpkg · gbif_checked oder schemaidentischer Ersatz.'),
              ('Linien laden', 'data_raw/marburg_basis.gpkg · gewaesser.'),
              ('Polygone laden', 'data_raw/marburg_basis.gpkg · schutzgebiete.')], y=245, gap=170)
    band(p, 'Projekt: unit12_vectors.qgz · Projekt-CRS: EPSG:25832', size=23)

    p = slide('Kontrollpunkt vor jeder Auswahl', 'QGIS · Eingang prüfen', 38, 41,
        'Alle drei Layer auf Geometrietyp, CRS, Lage und Featurezahl prüfen. Bei Abweichung nicht mit der Auswahl fortfahren. '
        'Die Begriffe MultiLineString und MultiPolygon sind mit den Multipart-Geometrien aus dem Konzeptteil zu verbinden.', qgis)
    table(p, ['Layer', 'Geometrie', 'Features', 'CRS'], [
        ['gbif_checked', 'Punkt', '56', 'EPSG:25832'],
        ['gewaesser', 'MultiLineString', '412', 'EPSG:25832'],
        ['schutzgebiete', 'MultiPolygon', '22', 'EPSG:25832']], [520, 420, 250, 240], y=245, row_h=105, size=22)
    band(p, 'Kontrollfolge: Name · Geometrie · CRS · Anzahl · Lage · Attribute', size=22)

    p = slide('Layerreihenfolge macht Beziehungen sichtbar', 'QGIS · Darstellung', 41, 43,
        'Punkte oben, Gewässer darunter, Schutzgebiete unten anordnen. Polygonfüllung transparent oder sehr hell setzen. '
        'Diese Darstellung dient der visuellen Kontrolle; die räumliche Auswahl rechnet mit Geometrien und hängt nicht von Symbolfarbe oder Reihenfolge ab.', qgis)
    for i, (label, body, color) in enumerate([('1 · Punkte', 'kontrastierendes Symbol', ORANGE),
                                               ('2 · Gewässer', 'erkennbare Linie', TEAL),
                                               ('3 · Schutzgebiete', 'transparente Fläche', 0x2E7D32)]):
        y = 245+i*145
        box(p, 250, y, 1100, 105, WHITE, GRID)
        box(p, 250, y, 12, 105, color)
        text(p, 295, y+20, 420, 60, label, 27, color, True)
        text(p, 720, y+22, 580, 60, body, 24, INK)
    band(p, 'Darstellung prüfen – aber Auswahlregel nicht aus Farben ableiten.', size=22)

    p = slide('Zuerst nach dem Attribut kategorie auswählen', 'QGIS · Attributauswahl', 43, 47,
        'Attributtabelle der Schutzgebiete öffnen, Werte von kategorie prüfen und dann „Objekte über Ausdruck wählen“ verwenden. '
        'Der Feldname und der Textwert müssen exakt geschrieben werden. Die Auswahl in Tabelle und Karte kontrollieren.', qgis)
    box(p, 210, 285, 1180, 180, 0xF4F4F4, GRID)
    text(p, 260, 330, 1080, 90, '"kategorie" = \'FFH\'', 34, INK, True, 'CENTER')
    band(p, 'Attributauswahl: Tabellenwert entscheidet · räumliche Auswahl folgt danach.', y=570, size=22)

    p = slide('Zehn FFH-Flächen als Vergleichslayer sichern', 'QGIS · Attributergebnis', 47, 50,
        'Erwartet sind 10 ausgewählte von 22 Schutzgebietsfeatures. Nur die Auswahl nach data_output/unit12_results.gpkg exportieren und den Layer schutzgebiete_auswahl nennen. '
        'Diesen neu geladenen Layer für beide folgenden räumlichen Auswahlen verwenden.', qgis+'\n'+core)
    card(p, 140, 280, 520, 290, '22', 'Schutzgebiete gesamt\n12 NSG · 10 FFH', size=27)
    card(p, 800, 280, 660, 290, '10', 'ausgewählte FFH-Features\n→ schutzgebiete_auswahl', color=ORANGE, size=27)
    band(p, 'Ausgabe: data_output/unit12_results.gpkg · EPSG:25832', size=23)

    p = slide('„Nach Position selektieren“ braucht klare Rollen', 'Räumliche Auswahl · Werkzeuglogik', 50, 53,
        'Eingabelayer und Vergleichslayer ausdrücklich unterscheiden. Ausgewählt werden Features des Eingabelayers. '
        'Der Vergleichslayer liefert nur die Geometrien, zu denen die Beziehung geprüft wird.', qgis)
    card(p, 120, 275, 520, 300, 'Eingabelayer', 'Welche Features sollen\nausgewählt werden?', size=27)
    text(p, 675, 365, 250, 100, 'intersects\n→', 27, TEAL, True, 'CENTER')
    card(p, 960, 275, 520, 300, 'Vergleichslayer', 'schutzgebiete_auswahl\n10 FFH-Features', color=ORANGE, size=25)
    band(p, 'Beziehung und Richtung der Frage vor dem Start laut benennen.', size=22)

    p = slide('GBIF-Punkte gegen FFH-Flächen auswählen', 'Räumliche Auswahl · Punkte', 53, 58,
        'Werkzeug gemeinsam einstellen: Eingabelayer gbif_checked, Beziehung schneidet/intersects, Vergleichslayer schutzgebiete_auswahl. '
        'Auswahl im vorhandenen Punktlayer erzeugen und anschließend Attributtabelle auf nur ausgewählte Features stellen.', qgis)
    table(p, ['Parameter', 'Wert'], [
        ['Features auswählen aus', 'gbif_checked'],
        ['räumliche Beziehung', 'schneidet · intersects'],
        ['durch Vergleich mit', 'schutzgebiete_auswahl'],
        ['Auswahlmethode', 'neue Auswahl erstellen']], [610, 820], y=235, row_h=90, size=22)
    band(p, 'Frage: Welche der 56 Punkte besitzen einen gemeinsamen Ort mit einer FFH-Fläche?', size=21)

    p = slide('Prüfwert: 4 von 56 Punkten', 'Räumliche Auswahl · Punktergebnis', 58, 60,
        'Ergebnis erst abfragen, dann zeigen. Ein Punkt, der mehrere FFH-Flächen schneidet, wird in der Auswahl nur einmal gezählt. '
        'Bei Abweichung Eingabe-/Vergleichslayer, Beziehung und die zehn FFH-Features prüfen.', qgis)
    card(p, 170, 285, 550, 300, '56', 'geprüfte GBIF-Records\nim Eingabelayer', size=27)
    card(p, 880, 285, 550, 300, '4', 'schneiden mindestens\neine ausgewählte FFH-Fläche', color=ORANGE, size=27)
    band(p, 'Noch temporär ausgewählt – dauerhafte Speicherung folgt ab Minute 70.', size=22)

    p = slide('Gewässer gegen dieselben FFH-Flächen auswählen', 'Räumliche Auswahl · Linien', 60, 65,
        'Die zweite Auswahl mit denselben Vergleichsgeometrien durchführen. Nur der Eingabelayer wechselt zu gewaesser. '
        'Darauf hinweisen, dass Features des Datensatzes gezählt werden, nicht notwendigerweise eigenständige Flüsse.', qgis)
    table(p, ['Parameter', 'Wert'], [
        ['Features auswählen aus', 'gewaesser'],
        ['räumliche Beziehung', 'schneidet · intersects'],
        ['durch Vergleich mit', 'schutzgebiete_auswahl'],
        ['Auswahlmethode', 'neue Auswahl erstellen']], [610, 820], y=235, row_h=90, size=22)
    band(p, 'Frage: Welche der 412 Linienfeatures besitzen einen gemeinsamen Ort mit einer FFH-Fläche?', size=21)

    p = slide('Prüfwert: 106 von 412 Linienfeatures', 'Räumliche Auswahl · Linienergebnis', 65, 67,
        'Ergebnis abfragen und zeigen. Ein Treffer sagt zunächst nur, dass mindestens ein gemeinsamer Ort existiert. '
        'Ein Linienfeature kann ein Gebiet kurz berühren, darin verlaufen oder es vollständig durchqueren.', qgis)
    card(p, 170, 285, 550, 300, '412', 'Gewässer-Features\nim Eingabelayer', size=27)
    card(p, 880, 285, 550, 300, '106', 'schneiden mindestens\neine ausgewählte FFH-Fläche', color=ORANGE, size=27)
    band(p, 'Gezählt werden Features – nicht Flüsse und nicht Teilstrecken im Schutzgebiet.', size=22)

    p = slide('Auswahl ist nicht Zuschneiden', 'Räumliche Auswahl · Geometrie bleibt', 67, 69,
        'Die Grafik vergleichen: Intersects markiert und exportiert die vollständige Linie einschließlich außen liegender Abschnitte. Clip würde eine neue, gekürzte Geometrie erzeugen. '
        'Zuschneiden ist heute kein Pflichtschritt.', qgis+'\nBild: assets/images/unit12/auswahl-zuschneiden.svg')
    picture(p, ROOT/'assets/images/unit12/auswahl-zuschneiden.svg', 320, 215, 430, 430*852/640)
    card(p, 850, 300, 560, 175, 'Auswahl + Export', 'vollständiges Linienfeature bleibt erhalten', size=22)
    card(p, 850, 530, 560, 175, 'Clip', 'neue Geometrie endet an der Polygonkante', color=ORANGE, size=22)

    p = slide('Was dürfen wir aus 106 Treffern folgern?', 'Räumliche Auswahl · Interpretation', 69, 70,
        'Die zu starke Aussage gemeinsam zurückweisen. Die Auswahl berechnet weder die Gewässerlänge innerhalb der FFH-Flächen noch die Anzahl eigenständiger Flüsse. '
        'Dafür wäre eine andere Operation und eine fachliche Definition erforderlich.', qgis)
    text(p, 170, 275, 1260, 110, '„106 Gewässer liegen vollständig in FFH-Gebieten.“', 34, INK, True, 'CENTER')
    line(p, 330, 430, 1270, 430, GRID, 70)
    text(p, 170, 485, 1260, 150, 'Belegt ist: 106 Features schneiden mindestens eine\nausgewählte FFH-Geometrie.', 30, TEAL, True, 'CENTER')
    band(p, 'Intersects beantwortet „ob“ – nicht automatisch „wie viel“.', size=24)

    p = slide('Beide räumlichen Auswahlen exportieren', 'Export · Dauerhafte Ergebnisse', 70, 74,
        'Jeweils Rechtsklick auf den Eingabelayer und nur ausgewählte Objekte speichern. Beide Ergebnisse in das bereits angelegte unit12_results.gpkg schreiben. '
        'Die Namen exakt übernehmen und EPSG:25832 kontrollieren.', qgis+'\n'+core)
    table(p, ['Auswahl aus', 'Layername', 'Features'], [
        ['gbif_checked', 'gbif_in_schutzgebieten', '4'],
        ['gewaesser', 'gewaesser_an_schutzgebieten', '106']], [480, 720, 230], y=285, row_h=130, size=25)
    band(p, 'Datei: data_output/unit12_results.gpkg · nur ausgewählte Objekte', size=23)

    p = slide('Das GeoPackage enthält drei Ergebnislayer', 'Export · Sollzustand', 74, 77,
        'Den Sollzustand vor der Endkontrolle zeigen. schutzgebiete_auswahl entstand aus der Attributauswahl; die beiden anderen Layer aus räumlichen Auswahlen. '
        'Alle drei Layer haben EPSG:25832.', qgis)
    table(p, ['Layer', 'Geometrie', 'Features'], [
        ['schutzgebiete_auswahl', 'MultiPolygon', '10'],
        ['gbif_in_schutzgebieten', 'Punkt', '4'],
        ['gewaesser_an_schutzgebieten', 'MultiLineString', '106']], [790, 420, 220], y=250, row_h=105, size=23)
    band(p, 'Ein GeoPackage · drei eindeutig benannte und getrennt prüfbare Layer', size=22)

    p = slide('Neu laden, Auswahl lösen, Ergebnis prüfen', 'Export · Kontrolle', 77, 80,
        'Alle drei Ergebnislayer aus dem Browser neu laden. Temporäre Auswahlen in den Rohlayern aufheben oder Rohlayer deaktivieren. '
        'Featurezahlen, Geometrietyp, EPSG:25832 und plausible Lage kontrollieren. Bei technischem Scheitern ersatz/unit12_results.gpkg verwenden.', qgis+'\n'+core)
    steps(p, [('Neu laden', 'Alle drei Layer aus data_output/unit12_results.gpkg.'),
              ('Prüfen', '10 Polygone · 4 Punkte · 106 Linien · EPSG:25832.'),
              ('Sichern', 'Projekt speichern; Ersatznutzung gegebenenfalls notieren.')], y=245, gap=170)
    band(p, 'Fallback: ersatz/unit12_results.gpkg mit gleichnamigen Layern', size=22)

    p = slide('Ein Ergebnis braucht Regel, Zahl und Grenze', 'Dokumentation · Reproduzierbarkeit', 77, 80,
        'Die Mindestdokumentation gemeinsam festhalten. Quellen stehen vollständig in documentation/quellen.md. '
        'Eine technisch eindeutige Auswahl beseitigt weder Koordinatenunsicherheit noch Modell- und Aktualitätsunterschiede der Grenzen.', qgis)
    table(p, ['Dokumentieren', 'Heute'], [
        ['Eingänge', '56 Punkte · 412 Linien · 22 Polygone'],
        ['Attributregel', 'kategorie = FFH · 10 Polygone'],
        ['räumliche Regel', 'intersects · 4 Punkte · 106 Linien'],
        ['Ausgabe', 'unit12_results.gpkg · drei Layer · EPSG:25832'],
        ['Aussagegrenze', 'Koordinate, Grenze und Datenstand bleiben unsicher']], [520, 910], y=220, row_h=94, size=21)

    p = slide('Grenzfall · erst zu zweit erklären', 'Interpretation · Nachbarschaftsgespräch', 80, 82,
        'Zwei Minuten zu zweit: Für A, B und C intersects und within vorhersagen. Danach erklären, was bei B mit einer unsicheren Beobachtungskoordinate fachlich offen bleibt. '
        'Die Auflösung folgt auf der nächsten Folie.', overview)
    text(p, 130, 260, 1340, 120, 'A liegt innen · B liegt auf der Grenze · C liegt außen', 31, INK, True, 'CENTER')
    table(p, ['Punkt', 'intersects?', 'within?'], [
        ['A', '[ja / nein]', '[ja / nein]'],
        ['B', '[ja / nein]', '[ja / nein]'],
        ['C', '[ja / nein]', '[ja / nein]']], [400, 500, 500], y=420, row_h=82, size=23, x0=100)

    p = slide('Intersects zählt den Rand – Unsicherheit bleibt', 'Interpretation · Auflösung', 82, 85,
        'Die Tabelle in der Grafik auswerten: A wird von beiden Beziehungen gewählt, B nur von intersects, C von keiner. '
        'Das gilt für die gespeicherten Geometrien. Bei unsicherer Koordinate kann der tatsächliche Nachweisort dennoch auf der anderen Seite der modellierten Grenze liegen.', vectors+'\nBild: assets/images/unit12/punkt-auf-polygongrenze.svg')
    picture(p, ROOT/'assets/images/unit12/punkt-auf-polygongrenze.svg', 300, 215, 500, 500*736/640)
    card(p, 900, 285, 520, 180, 'Rechnerisch', 'intersects: A + B\nwithin: A', size=24)
    card(p, 900, 525, 520, 180, 'Fachlich', 'Koordinaten- und Grenzunsicherheit bleiben', color=ORANGE, size=21)

    p = slide('Exit Ticket · eine Frage auswählen', 'Sicherung · Einzelarbeit', 85, 88,
        'Genau eine der drei Fragen auswählen und sichtbar markieren. Zwei Minuten einzeln schreiben lassen, anschließend höchstens eine knappe Antwort einsammeln. '
        'Nicht alle drei Fragen bearbeiten lassen.', overview)
    table(p, ['Option', 'Frage'], [
        ['A', 'Wodurch unterscheiden sich Auswahl und neu gespeicherter Ergebnislayer?'],
        ['B', 'Welche räumliche Beziehung wurde für Punkte und Gewässer verwendet?'],
        ['C', 'Warum benötigen Messungen ein geeignetes projiziertes CRS?']], [180, 1250], y=235, row_h=130, size=22)
    band(p, 'Heute ausgewählt: [A / B / C]', size=24)

    p = slide('Nachbereitung · JiTT zu Unit 12', 'Ausblick', 88, 90,
        'Nur die JiTT-Aufgabe als verbindliche Nachbereitung nennen. Fragen, Frist und endgültiger Link stehen in ILIAS. '
        'Der Link auf der Kursseite ist noch ein sichtbarer Platzhalter; keinen Wert erfinden. Unit 13 verwendet wieder gbif_checked aus Unit 11, nicht die vier ausgewählten Punkte aus Unit 12.', assignment)
    card(p, 130, 260, 620, 300, 'Einzige Übungsaufgabe', 'JiTT-Fragen zu Unit 12\nim ILIAS-Kurs beantworten', size=27)
    card(p, 850, 260, 620, 300, 'Nächste Unit', 'Rasterwerte an alle 56 Punkte\naus gbif_checked übertragen', color=ORANGE, size=24)
    band(p, 'Fragen, Frist und Link: ausschließlich die aktuellen Angaben in ILIAS verwenden.', size=21)

    p = slide('Quellen und Arbeitsstand', 'Reserve · Nachweise', 0, 0,
        'Nur bei Bedarf zeigen. Die Folie dokumentiert Kursseiten, QGIS-Dokumentation und Datenquellen. '
        'Die Live-Erreichbarkeit externer Portale ist für den Präsenzkern nicht erforderlich.', overview, reserve=True)
    links = [('Unit 12 · Kursübersicht', overview),
             ('Linien und Polygone', vectors),
             ('Vektordaten aus Geoportalen', portals),
             ('Linien und Polygone in QGIS', qgis),
             ('QGIS 3.40 · Benutzerhandbuch', QDOC),
             ('HLNUG · Naturschutz', HLNUG_NATURE),
             ('HLNUG · Wasser', HLNUG_WATER)]
    for i, (label, url) in enumerate(links):
        shape = text(p, 110, 215+i*61, 1380, 52, label, 23, TEAL, True)
        hyperlink(shape, url)
    text(p, 110, 675, 1390, 126,
         'Paketstand: 08.09.2026 · Abgleich der Folien: 09.09.2026\n'
         'Layout: Universität-Marburg-Vorlage · Titel-/Abschlussbild: FB19-Vorlage\n'
         'Lehrabbildungen: fünf vorhandene SVGs der Unit 12', 17, MUTED)

    p = slide('Vielen Dank für Ihre Aufmerksamkeit', 'Abschluss', 90, 90,
        'Die Sitzung mit dieser Folie beenden. Die Abschlussgestaltung nutzt den Kontakt-Master der universitären Vorlage sowie das originale Foto-/Kartenmotiv aus der FB19-Titelseite.', str(TEMPLATE), kind='closing')
    box(p, 44, 44, 809, 807, 0xF7DEED)
    picture(p, FB19_IMAGE, 915, 350, 640, 640*135/394)
    text(p, 100, 380, 700, 250, 'Vielen Dank für Ihre Aufmerksamkeit', 41, INK)
    text(p, 165, 710, 620, 110, 'Geodaten · Unit 12\nFachbereich 19 · Geographie', 18, INK)


def main():
    global DOC, MASTERS
    with tempfile.TemporaryDirectory(prefix='geomoer-unit12-') as profile:
        pipe = 'geomoer_unit12_' + uuid.uuid4().hex
        proc = subprocess.Popen(['libreoffice', '-env:UserInstallation='+Path(profile).as_uri(),
            '--headless', '--accept=pipe,name='+pipe+';urp;StarOffice.ComponentContext',
            '--norestore', '--nodefault', '--nofirststartwizard'], stdout=subprocess.DEVNULL)
        desktop = None
        try:
            local = uno.getComponentContext()
            resolver = local.ServiceManager.createInstanceWithContext('com.sun.star.bridge.UnoUrlResolver', local)
            for _ in range(100):
                try:
                    ctx = resolver.resolve('uno:pipe,name='+pipe+';urp;StarOffice.ComponentContext')
                    break
                except Exception:
                    if proc.poll() is not None:
                        raise RuntimeError('LibreOffice could not start')
                    time.sleep(.2)
            else:
                raise RuntimeError('LibreOffice connection timed out')
            desktop = ctx.ServiceManager.createInstanceWithContext('com.sun.star.frame.Desktop', ctx)
            legacy = desktop.loadComponentFromURL(FB19.as_uri(), '_blank', 0, (prop('Hidden', True),))
            legacy_export = Path(profile)/'fb19.pptx'
            legacy.storeToURL(legacy_export.as_uri(), (prop('FilterName', 'Impress MS PowerPoint 2007 XML'),))
            legacy.close(True)
            (OUT/'assets').mkdir(exist_ok=True)
            with ZipFile(legacy_export) as archive:
                FB19_IMAGE.write_bytes(archive.read('ppt/media/image2.png'))
            DOC = desktop.loadComponentFromURL(TEMPLATE.as_uri(), '_blank', 0, (prop('Hidden', True),))
            base.DOC = DOC
            masters = DOC.getMasterPages()
            MASTERS = {masters.getByIndex(i).Name: masters.getByIndex(i) for i in range(masters.Count)}
            base.MASTERS = MASTERS
            pages = DOC.getDrawPages()
            for i in range(pages.Count - 1, -1, -1):
                if i != 2:
                    pages.remove(pages.getByIndex(i))
            DOC.DocumentProperties.Title = 'Unit 12 – Linien, Polygone und räumliche Auswahl'
            DOC.DocumentProperties.Subject = 'Geodaten · Unit 12 · Präsenzlehre'
            DOC.DocumentProperties.Author = 'GeoMOER'
            build()
            pptx = OUT/'unit12_praesenz.pptx'
            DOC.storeAsURL(pptx.as_uri(), (prop('FilterName', 'Impress MS PowerPoint 2007 XML'), prop('Overwrite', True)))
            DOC.close(True)
            DOC = desktop.loadComponentFromURL(pptx.as_uri(), '_blank', 0, (prop('Hidden', True),))
            base.DOC = DOC
            assert DOC.getDrawPages().Count == len(RECORDS)
            pdf = OUT/'unit12_praesenz.pdf'
            DOC.storeToURL(pdf.as_uri(), (prop('FilterName', 'impress_pdf_Export'), prop('Overwrite', True),
                prop('FilterData', (prop('ExportNotesPages', False), prop('ExportHiddenSlides', True), prop('UseTaggedPDF', True)))))
            DOC.close(True)
            PUBLISHED_PDF.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(pdf, PUBLISHED_PDF)
            with (OUT/'moderation.md').open('w') as fp:
                fp.write('# Unit 12 – Moderation\n\nTitelfolie, 34 Hauptfolien für 90 Minuten, eine Reserve-/Quellenfolie und eine Abschlussfolie. Zeitangaben stehen nur in diesen Notizen.\n\n')
                for record in RECORDS:
                    fp.write(f"## {record['number']:02d} · {record['title']}\n\n{record['notes']}\n\n")
            print(f'Created {len(RECORDS)} slides: {pptx}, matching PDF and published PDF copy', flush=True)
        finally:
            if desktop:
                desktop.terminate()
            try:
                proc.wait(timeout=10)
            except subprocess.TimeoutExpired:
                proc.terminate()


if __name__ == '__main__':
    main()
