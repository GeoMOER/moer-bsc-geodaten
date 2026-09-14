#!/usr/bin/python3
"""Build the Unit 13 classroom deck with LibreOffice UNO (no downloads).

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
PUBLISHED_PDF = ROOT/'assets/pdfs/Geodaten_Slides_Unit13.pdf'
COURSE = 'https://geomoer.github.io/moer-bsc-geodaten/unit13/'
QDOC = 'https://docs.qgis.org/3.40/en/docs/user_manual/'
DGM_SOURCE = 'https://hvbg.hessen.de/landesvermessung/geotopographie/3d-daten/digitale-gelaendemodelle'
OPEN_DATA = 'https://hvbg.hessen.de/geoinformation/open-data'
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
band, card, steps, table, raster = base.band, base.card, base.steps, base.table, base.raster


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
             'Universität Marburg | Fachbereich 19 · Geographie | Geodaten · Unit 13', 10, MUTED)
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
    overview = COURSE+'unit13-00_overview.html'
    model = COURSE+'unit13-01_rasterdaten.html'
    properties = COURSE+'unit13-02_rastereigenschaften.html'
    qgis = COURSE+'unit13-03_raster_qgis.html'
    assignment = COURSE+'unit13-04_assignment.html'
    core = 'https://geomoer.github.io/moer-bsc-geodaten/material/qgis-kernpfade.html#unit13'

    p = slide('Rasterdaten und Höhenwerte', 'Unit 13', 0, 0,
        'Titelfolie beim Ankommen zeigen. Die Sitzung ist für 90 Minuten mit 100–150 Bachelor- und Lehramtsstudierenden ausgelegt. '
        'Vorbereitendes Lesen wird nicht vorausgesetzt. QGIS 3.40 und das vollständig entpackte Marburger Übungspaket müssen verfügbar sein. '
        'Erwarteter Punkteeingang ist gbif_checked mit 56 Features aus Unit 11 oder der schemaidentische Ersatzlayer.', str(TEMPLATE), kind='title')
    picture(p, FB19_IMAGE, 44, 350, 539, 539*135/394)
    text(p, 625, 285, 850, 300, 'Rasterdaten und\nHöhenwerte', 44, WHITE)
    text(p, 625, 614, 840, 70, 'Unit 13', 28, WHITE)
    text(p, 625, 744, 840, 100, 'Fachbereich 19 · Geographie\nPhilipps-Universität Marburg', 19, WHITE)

    p = slide('JiTT · Rückblick auf Unit 12', 'Platzhalter · vollständig austauschbar', 0, 10,
        'VOR DEM TERMIN: Den gesamten Platzhalter durch die aktuelle JiTT-Auswertung zu Unit 12 ersetzen. '
        'Bei Bedarf die Folie duplizieren. Nur tatsächliche, zusammengefasste und anonymisierte Rückmeldungen einsetzen. '
        'Die gesamte Phase dauert zehn Minuten. Verständnisfragen zu Linien, Polygonen, Metadaten oder räumlicher Auswahl klären.')
    shape = box(p, 100, 237, 1400, 545, PALE, GRID)
    shape.Name = 'JiTT – vollständigen Block ersetzen'
    text(p, 180, 430, 1240, 130, '[Hier den vollständigen\nJiTT-Block einfügen]', 38, TEAL, False, 'CENTER')

    p = slide('Vom Höhenraster zum Punktattribut', 'Unit 13 · Orientierung', 10, 11,
        'Den Ablauf ankündigen: Rastermodell verstehen, DGM-Eigenschaften prüfen, Werte darstellen und abfragen, Rasterwerte an 56 Punkten abtasten und das Ergebnis mit 35 Zahlen und 21 NULL-Werten dokumentieren.', overview)
    picture(p, ROOT/'assets/images/unit13/hero-unit13.jpg', 85, 225, 1430, 1430/6)
    for x, label, body in [(85, 'Raster lesen', 'Zellen, Werte und\nMetadaten unterscheiden'),
                           (570, 'Werte prüfen', 'Darstellung und NoData\nkontrollieren'),
                           (1055, 'Punkte ergänzen', '35 Werte · 21 NULL\nals hoehe_m sichern')]:
        card(p, x, 495, 460, 205, label, body, size=22)
    band(p, 'Leitfrage: Auf welcher Geländehöhe liegen die dokumentierten Beobachtungen?', size=21)

    p = slide('Objekte oder flächendeckendes Wertefeld?', 'Rastermodell · Vergleich', 11, 13,
        'Vektor modelliert einzelne Features mit Geometrie und Attributzeile. Raster teilt den Raum regelmäßig in Zellen mit Werten. '
        'Beide Modelle lassen sich kombinieren: Punktposition plus Höhenraster ergibt den Zellwert am Beobachtungsort.', model)
    card(p, 120, 270, 600, 320, 'Vektor', 'einzelne Objekte\nPunkt · Linie · Polygon\nAttribute je Feature', size=25)
    card(p, 880, 270, 600, 320, 'Raster', 'regelmäßiges Gitter\nWert je Zelle und Band\nflächendeckende Felder', color=ORANGE, size=25)
    band(p, 'Heute: Punktvektor + kontinuierliches Raster → neues Punktattribut', size=23)

    p = slide('Ein Raster ordnet jeder Zelle einen Wert zu', 'Rastermodell · Aufbau', 13, 15,
        'Zeilen, Spalten und Zellen benennen. Die Position einer Zelle folgt aus Rasterursprung, Zellgröße und CRS. '
        'Der Wert 228 ist ein schematischer Höhenwert in Metern, nicht bereits ein Attribut des danebenliegenden Punkts.', model)
    text(p, 250, 255, 430, 50, 'Spalten →', 24, TEAL, True, 'CENTER')
    text(p, 120, 410, 110, 80, 'Zeilen\n↓', 24, TEAL, True, 'CENTER')
    raster(p, 260, 325, 95)
    box(p, 260+2*95, 325+2*95, 93, 93, None, ORANGE)
    card(p, 820, 285, 600, 275, 'Rasterzelle', 'räumliche Einheit\nmit einem Wert pro Band', size=26)
    band(p, 'Zellwert ≠ automatisch fehlerfreie Wahrheit für jeden Ort der Zelle', size=22)

    p = slide('Kontinuierlich oder kategorial?', 'Rastermodell · Bedeutung der Werte', 15, 18,
        'Kurze Zuordnung im Plenum: Geländehöhe ist kontinuierlich, Landbedeckung kategorial. '
        'Bei Kategorien sind Zahlen Codes ohne metrische Abstände; sie benötigen Einzelfarben. Höhenwerte können mit einem sequentiellen Verlauf dargestellt werden.', model)
    table(p, ['Rastertyp', 'Beispielwerte', 'Darstellung'], [
        ['kontinuierlich', '241,3 m · 241,8 m · 243,1 m', 'sequentieller Farbverlauf'],
        ['kategorial', '1 = Wald · 2 = Grünland · 3 = Siedlung', 'unterscheidbare Einzelfarben'],
        ['mehrbändig', 'Rot · Grün · Blau', 'Bandkombination, z. B. RGB']], [430, 620, 380], y=275, row_h=120, size=22)
    band(p, 'Die fachliche Bedeutung entsteht aus Daten und Metadaten – nicht aus der Dateiendung.', size=21)

    p = slide('DGM und DOM beschreiben verschiedene Oberflächen', 'Rastermodell · Höhenmodelle', 18, 21,
        'Dasselbe Landschaftsprofil vergleichen. Das DGM folgt dem Gelände unter Vegetation und Gebäuden; das DOM folgt der erfassten Oberfläche über Baumkrone und Dach. '
        'Für die Frage nach Geländehöhe der Beobachtungen verwenden wir das DGM.', model+'\nBild: assets/images/unit13/dgm-dom-profil.svg')
    picture(p, ROOT/'assets/images/unit13/dgm-dom-profil.svg', 190, 225, 1220, 1220*430/1000)
    band(p, 'Unsere Frage verlangt Gelände – deshalb DGM, nicht DOM.', size=24)

    p = slide('Rasterzelle und Bildschirmpixel sind nicht dasselbe', 'Rastermodell · Darstellung', 21, 22,
        'Beim starken Hineinzoomen wird eine Datenzelle als großes Quadrat sichtbar. Dieses Quadrat besteht am Monitor aus vielen Bildschirmpixeln. '
        'Für die fachliche Beschreibung der gespeicherten räumlichen Einheit den Begriff Rasterzelle verwenden.', model)
    card(p, 160, 285, 570, 300, 'Rasterzelle', 'räumliche Einheit im Datensatz\nzum Beispiel 10 m × 10 m', size=25)
    card(p, 870, 285, 570, 300, 'Bildschirmpixel', 'Bildelement der aktuellen Anzeige\nabhängig von Zoom und Bildschirm', color=ORANGE, size=24)
    band(p, 'Zoomen vergrößert die Anzeige – nicht die räumliche Auflösung des Datensatzes.', size=22)

    p = slide('Vergröbern fasst Werte zusammen', 'Rastermodell · Auflösung', 22, 25,
        'Die Grafik von oben nach unten lesen. Aus vier 10-m-Zellen entsteht hier eine 20-m-Zelle mit Mittelwert. Lokale Spitzen gehen verloren. '
        'Ein später wieder feineres Gitter kann diese Information nicht zurückholen. Die Zahlen sind ein schematisches Rechenbeispiel.', properties+'\nBild: assets/images/unit13/raster-vergroebern.svg')
    picture(p, ROOT/'assets/images/unit13/raster-vergroebern.svg', 350, 215, 385, 385*945/640)
    card(p, 840, 285, 600, 190, 'Kleinere Zellen', 'können feinere Unterschiede abbilden', size=23)
    card(p, 840, 525, 600, 190, 'Aber', 'Auflösung ist kein Beweis für Genauigkeit', color=ORANGE, size=23)

    p = slide('Projekt, DGM und Punkte vorbereiten', 'QGIS · Startzustand', 25, 28,
        'Projekt als unit13_raster.qgz speichern und EPSG:25832 setzen. Das DGM und gbif_checked laden. '
        'Nicht die vier Punkte aus Unit 12 verwenden: Unit 13 beginnt erneut mit allen 56 qualitätsgeprüften Punkten aus Unit 11.', qgis+'\n'+core)
    steps(p, [('Projekt speichern', 'unit13_raster.qgz · Projekt-CRS EPSG:25832.'),
              ('Raster laden', 'data_raw/dgm_marburg_10m.tif · DGM – Geländehöhe.'),
              ('Punkte laden', 'unit11_results.gpkg/gbif_checked oder Ersatz · 56 Features.')], y=245, gap=170)
    band(p, 'Kontrolle: DGM unten · 56 Punkte sichtbar darüber', size=23)

    p = slide('Das DGM ist ein abgeleitetes Lehrprodukt', 'QGIS · Quelle und Entstehung', 28, 31,
        'Quelle und Bearbeitung trennen. Grundlage sind 162 amtliche DGM1-Kacheln des Hessen Geodatenmanagements. '
        'Für den Kurs wurden verfügbare 1-m-Werte zu 10-m-Mittelwerten zusammengefasst. Das Ergebnis ist kein unverändertes amtliches DGM10.', qgis+'\n'+DGM_SOURCE)
    table(p, ['Merkmal', 'Angabe'], [
        ['Quelle', 'Hessen DGM1 · Downloadpaket Marburg'],
        ['Kursbearbeitung', '162 Kacheln mosaikiert · 10-m-Mittelwerte'],
        ['Lizenz', 'Datenlizenz Deutschland – Zero 2.0'],
        ['Paketstand', '08.09.2026']], [500, 930], y=250, row_h=105, size=23)
    band(p, 'Mittelung verändert Auflösung – sie verbessert nicht automatisch die Höhengenauigkeit.', size=21)

    p = slide('Rastereigenschaften gemeinsam kontrollieren', 'QGIS · Information und Quelle', 31, 34,
        'Layereigenschaften öffnen und Werte gemeinsam finden. Minimum und Maximum sind gerundet. '
        'Die Höhenangaben beziehen sich auf DHHN2016_NH; das horizontale CRS ist EPSG:25832. NoData muss von gültigen Werten ausgeschlossen sein.', qgis)
    table(p, ['Eigenschaft', 'DGM-Wert'], [
        ['Rastergröße', '2.000 × 2.000 Zellen · ein Band'],
        ['Zellgröße / Datentyp', '10 m × 10 m · Float32'],
        ['CRS / Einheit', 'EPSG:25832 · Höhe in m'],
        ['Höhenbezug', 'DHHN2016_NH'],
        ['gültiger Wertebereich', '161,91 bis 414,12 m'],
        ['NoData', '-9999']], [520, 910], y=220, row_h=82, size=21)

    p = slide('Das Rasterrechteck ist nicht vollständig belegt', 'QGIS · Ausdehnung und NoData', 34, 37,
        'Rasterausdehnung und Datenabdeckung unterscheiden. Die Datei deckt das 20-km-Rechteck technisch ab, aber nur 40,01 Prozent der Zellen enthalten gültige Höhen. '
        'Die Lücke stammt aus der DGM-Kachelabdeckung und darf nicht aufgefüllt oder als Höhe null gelesen werden.', qgis)
    card(p, 120, 285, 590, 300, '1.600.200', 'Zellen mit gültiger Höhe\n161,91–414,12 m', size=26)
    card(p, 890, 285, 590, 300, '2.399.800', 'NoData-Zellen\nKennwert -9999', color=ORANGE, size=26)
    band(p, 'NoData beschreibt fehlende gültige Werte – nicht Gelände unter dem Meeresspiegel.', size=21)

    p = slide('Gleiche Zellgröße genügt nicht', 'QGIS · Rasterausrichtung', 37, 40,
        'Die Gitter vergleichen: Beide besitzen 10-m-Zellen im selben lokalen Meterkoordinatensystem, aber Gitter B beginnt fünf Meter weiter östlich. '
        'Für zellenweise Berechnungen müssen auch Ursprung beziehungsweise Zellgrenzen passen. Heute wird kein Raster neu ausgerichtet.', properties+'\nBild: assets/images/unit13/rasterausrichtung.svg')
    picture(p, ROOT/'assets/images/unit13/rasterausrichtung.svg', 300, 215, 510, 510*710/640)
    card(p, 900, 300, 520, 170, 'Gleich', 'CRS und Zellgröße', size=23)
    card(p, 900, 525, 520, 170, 'Verschieden', 'Ursprung und Zellgrenzen', color=ORANGE, size=23)

    p = slide('Einzelne Zellwerte zuerst direkt abfragen', 'QGIS · Werte prüfen', 40, 43,
        'Mit Objekte abfragen an mehreren Stellen in Band 1 klicken. Einen gültigen Wert und eine NoData-Stelle vergleichen. '
        'Die Einheit Meter, den Wertebereich und die räumliche Lage plausibilisieren, bevor Punkte abgetastet werden.', qgis)
    steps(p, [('Gültige Zelle', 'Zahl zwischen etwa 161,91 und 414,12 m.'),
              ('NoData-Stelle', 'kein gültiger Höhenwert; Kennwert -9999 nicht als Höhe lesen.'),
              ('Darstellung', 'geglättete Anzeige kann Zellgrenzen verbergen, Werte aber nicht ändern.')], y=245, gap=170)
    band(p, 'Direkte Abfrage ist später die unabhängige Stichprobe für hoehe_m.', size=22)

    p = slide('NoData ist nicht der gültige Wert 0', 'QGIS · Fehlende Werte', 43, 46,
        'Die schematische Grafik lesen. Ein gültiger Nullwert ist eine fachliche Zahl. NoData bedeutet fehlenden oder ungültigen Wert. '
        'Im Marburger DGM lautet der technische Kennwert -9999; beim Abtasten wird daraus NULL. Das gezeigte 0-m-Beispiel stammt nicht aus dem Marburger Ausschnitt.', properties+'\nBild: assets/images/unit13/zellgroesse-nodata-genauigkeit.svg')
    picture(p, ROOT/'assets/images/unit13/zellgroesse-nodata-genauigkeit.svg', 300, 215, 485, 485*752/640)
    card(p, 880, 285, 560, 175, '0', 'kann ein gültiger Messwert sein', size=25)
    card(p, 880, 525, 560, 175, 'NoData → NULL', 'kein gültiger Wert verfügbar', color=ORANGE, size=24)

    p = slide('Höhenwerte mit Pseudofarbe darstellen', 'QGIS · Symbolisierung', 46, 49,
        'Layereigenschaften → Symbolisierung: Einkanal-Pseudofarbe, Band 1, Minimum und Maximum für den relevanten Datensatz laden und einen sequentiellen Farbverlauf verwenden. '
        'NoData transparent halten. Die systematische Kartengestaltung folgt erst in Unit 14.', qgis)
    steps(p, [('Darstellungsart', 'Einkanal-Pseudofarbe · Band 1.'),
              ('Wertebereich', 'Minimum und Maximum laden; NoData ausschließen.'),
              ('Farbverlauf', 'niedrig nach hoch eindeutig und sequentiell.')], y=245, gap=170)
    band(p, 'Symbolisierung macht Muster sichtbar – sie verändert keine Zellwerte.', size=22)

    p = slide('Andere Farben, gleiche Werte', 'QGIS · Darstellung und Daten', 49, 51,
        'Die umrahmte Zelle in beiden Darstellungen ablesen. In beiden Fällen bleibt ihr Wert 220 m. '
        'Nur die Zuordnung von Zahlen zu Farben ändert sich. Die Beispielmatrix ist schematisch und keine Marburger Messung.', properties+'\nBild: assets/images/unit13/rasterwerte-farben.svg')
    picture(p, ROOT/'assets/images/unit13/rasterwerte-farben.svg', 315, 215, 495, 495*735/640)
    card(p, 900, 315, 520, 170, 'Datenwert', '220 m bleibt 220 m', size=24)
    card(p, 900, 535, 520, 170, 'Farbe', 'Darstellungsentscheidung', color=ORANGE, size=24)

    p = slide('Eine kleine Zelle beweist keine hohe Genauigkeit', 'Interpretation · Nachbarschaftsgespräch', 51, 53,
        'Zwei Minuten zu zweit: Die Aussage prüfen und mindestens eine zusätzliche Metadatenangabe nennen. '
        'Unterscheiden: Zellgröße beschreibt das Gitter; Lage- und Wertgenauigkeit beschreiben Unsicherheiten. Die Auflösung folgt auf der nächsten Folie.', overview)
    text(p, 140, 255, 1320, 170, '„Das Raster hat 1-m-Zellen.\nDeshalb ist jeder Höhenwert auf 1 m genau.“', 36, INK, True, 'CENTER')
    band(p, 'Welche Information liefert die Zellgröße – und welche fehlt?', y=570, size=24)

    p = slide('Auflösung, Lage und Wert getrennt beurteilen', 'Interpretation · Auflösung', 53, 55,
        'Drei Begriffe sichern. Für die Höhengenauigkeit werden Erfassungsmethode und dokumentierte vertikale Genauigkeit benötigt. '
        'Das heutige Kursraster hat 10-m-Zellen, nicht 1-m-Zellen; die Ausgangsdaten wurden gemittelt.', properties)
    table(p, ['Begriff', 'Frage'], [
        ['räumliche Auflösung', 'Wie groß beziehungsweise weit auseinander sind die Zellen?'],
        ['Lagegenauigkeit', 'Wie genau liegt das Gitter an der vorgesehenen Position?'],
        ['Wertgenauigkeit', 'Wie genau beschreibt der Wert das Gelände?']], [520, 910], y=270, row_h=115, size=23)
    band(p, 'Korrigiert: 10-m-Zellen beschreiben das Gitter – nicht automatisch einen 10-m-Höhenfehler.', size=20)

    p = slide('Punkteeingang: alle 56 aus Unit 11', 'Abtasten · Eingang prüfen', 55, 58,
        'gbif_checked laden und auf 56 Features, EPSG:25832 und das vollständige Feldschema prüfen. '
        'Einige Punkte liegen außerhalb gültiger DGM-Zellen. Sie bleiben im Ergebnis und erhalten später NULL.', qgis+'\n'+core)
    card(p, 140, 285, 560, 300, 'Raster', 'dgm_marburg_10m.tif\n10 m · EPSG:25832', size=25)
    card(p, 900, 285, 560, 300, 'Punkte', 'gbif_checked\n56 · EPSG:25832', color=ORANGE, size=25)
    band(p, 'Nicht verwenden: gbif_in_schutzgebieten mit nur vier Punkten aus Unit 12.', size=22)

    p = slide('Werkzeug „Rasterwerte abtasten“ einstellen', 'Abtasten · Parameter', 58, 62,
        'Verarbeitungswerkzeuge öffnen und Sample raster values beziehungsweise Rasterwerte abtasten wählen. '
        'Eingabelayer, Raster und Präfix exakt kontrollieren. Der Ausgabepfad und Layername werden bereits im Werkzeug festgelegt.', qgis)
    table(p, ['Parameter', 'Wert'], [
        ['Eingabepunkte', 'gbif_checked · 56 Features'],
        ['Rasterlayer', 'dgm_marburg_10m.tif · Band 1'],
        ['Spaltenpräfix', 'hoehe_'],
        ['Ausgabe', 'data_output/unit13_results.gpkg'],
        ['Layername', 'gbif_mit_hoehe']], [520, 910], y=230, row_h=88, size=22)
    band(p, 'Das Werkzeug verschiebt keine Punkte – es ergänzt einen Zellwert als Attribut.', size=21)

    p = slide('Der getroffene Zellwert wird zum Attribut', 'Abtasten · Arbeitslogik', 62, 65,
        'Die Grafik von links nach rechts lesen. Der Punkt liegt in der Zelle mit dem sichtbaren Wert 228 und erhält diesen Wert im neuen Attribut. '
        'Das Beispiel erklärt die Operation; 228 ist kein geforderter Kontrollwert für einen bestimmten GBIF-Record.', qgis+'\nBild: assets/images/unit13/raster-workflow.svg')
    picture(p, ROOT/'assets/images/unit13/raster-workflow.svg', 200, 220, 1200, 540)
    band(p, 'Punktposition + Rasterzelle → Zellwert in neuer Tabellenspalte', size=23)

    p = slide('QGIS erzeugt zunächst hoehe_1', 'Abtasten · Ergebnisfeld', 65, 68,
        'Werkzeug ausführen und Ergebnisattributtabelle öffnen. Mit QGIS 3.40 und dem Präfix hoehe_ heißt das Band-1-Feld hoehe_1. '
        'Den tatsächlichen Namen prüfen. Noch nicht einfach ein zweites Feld ergänzen, ohne das Übergabeschema zu planen.', qgis)
    card(p, 140, 285, 560, 300, 'Werkzeugausgabe', 'hoehe_1\nDezimalzahl', size=28)
    text(p, 715, 375, 170, 100, '→', 48, TEAL, True, 'CENTER')
    card(p, 900, 285, 560, 300, 'Kursübergabe', 'hoehe_m\nDezimalzahl', color=ORANGE, size=28)
    band(p, 'Erst Feldname und Typ prüfen, dann kontrolliert umbenennen.', size=22)

    p = slide('Nur das Höhenfeld kontrolliert umbenennen', 'Abtasten · Schema sichern', 68, 72,
        'Mit Felder überarbeiten hoehe_1 in hoehe_m umbenennen und alle übrigen GBIF-Felder unverändert erhalten. '
        'Alternativ kann ein neues Dezimalfeld berechnet werden; dann das überflüssige hoehe_1 entfernen. Jeden Schritt dokumentieren.', qgis)
    steps(p, [('Felder überarbeiten', 'gbif_mit_hoehe als Eingabelayer wählen.'),
              ('Name und Typ', 'hoehe_1 → hoehe_m · Dezimalzahl beibehalten.'),
              ('Schema prüfen', '56 Features und alle ursprünglichen GBIF-Felder erhalten.')], y=245, gap=170)
    band(p, 'Verbindlicher Übergabename für Unit 14: hoehe_m', size=24)

    p = slide('Prüfwert: 35 Höhen und 21 NULL', 'Abtasten · Gesamtergebnis', 72, 75,
        'Ergebnis zuerst abfragen, dann zeigen. Alle 56 Punkte müssen erhalten bleiben. 35 treffen eine gültige DGM-Zelle; 21 liegen außerhalb der gültigen Abdeckung und erhalten NULL. '
        'NULL-Werte nicht durch 0 ersetzen und die Punkte nicht löschen.', qgis)
    card(p, 130, 285, 590, 300, '35', 'gültige Höhenwerte\nin hoehe_m', size=28)
    card(p, 880, 285, 590, 300, '21', 'NULL\nkein gültiger Rasterwert', color=ORANGE, size=28)
    band(p, 'Kontrollsumme: 35 + 21 = 56 Punkte · kein Featureverlust', size=24)

    p = slide('Ergebnis speichern und neu laden', 'Ausgabe · Dauerhafter Layer', 75, 78,
        'Sicherstellen, dass das endgültige Ergebnis wirklich im GeoPackage liegt und hoehe_m enthält. Den Layer aus dem Browser neu laden und die temporäre Werkzeugausgabe deaktivieren. '
        'Bei technischem Scheitern ersatz/unit13_results.gpkg/gbif_mit_hoehe laden und die Ersatznutzung notieren.', qgis+'\n'+core)
    steps(p, [('Datei', 'data_output/unit13_results.gpkg.'),
              ('Layer', 'gbif_mit_hoehe · 56 Features · EPSG:25832.'),
              ('Feld', 'hoehe_m · 35 Zahlen · 21 NULL.')], y=245, gap=170)
    band(p, 'Fallback: ersatz/unit13_results.gpkg · gbif_mit_hoehe', size=22)

    p = slide('Zwei konkrete Punkte als Stichprobe', 'Ausgabe · Ergebnis prüfen', 78, 81,
        'Die beiden GBIF-IDs im Ergebnis suchen. Für den gültigen Fall Raster an derselben Position direkt abfragen und den ungerundeten Wert vergleichen. '
        'Der zweite Punkt belegt einen NULL-Fall. Die Werte sind im Ersatzlayer geprüft.', qgis)
    table(p, ['gbifID', 'hoehe_m', 'Kontrolle'], [
        ['5012616638', '291,8 m', 'gültiger Rasterwert; direkt abfragen'],
        ['5012778768', 'NULL', 'keine gültige DGM-Zelle']], [430, 330, 670], y=285, row_h=130, size=24)
    band(p, 'Stichprobe bestätigt Wertübernahme – nicht die vollständige Genauigkeit des DGM.', size=21)

    p = slide('Gültige Punkthöhen liegen zwischen 178,55 und 323,90 m', 'Ausgabe · Vorsichtige Beschreibung', 81, 82,
        'Die Werte beziehen sich ausschließlich auf die 35 Punkte mit gültigem Rasterwert im bereitgestellten Snapshot. '
        'Keine Aussage über alle Feuersalamander oder ihre vollständige Höhenverbreitung ableiten. Ein Median ist im Kernweg nicht vorgegeben und wird nicht erfunden.', qgis)
    text(p, 160, 275, 1280, 110, '35 dokumentierte Beobachtungspunkte', 34, TEAL, True, 'CENTER')
    text(p, 160, 405, 1280, 100, '178,55 m ≤ hoehe_m ≤ 323,90 m', 38, INK, True, 'CENTER')
    band(p, '21 weitere Punkte bleiben erhalten, besitzen aber keinen gültigen Höhenwert.', y=590, size=23)

    p = slide('Welche Unsicherheiten treffen zusammen?', 'Interpretation · Grenzen', 82, 84,
        'Die drei Unsicherheitsquellen sammeln. Der Rasterwert beschreibt die getroffene 10-m-Zelle, die Punktkoordinate den gemeldeten Ort mit eigener Unsicherheit. '
        'DGM-Entstehung, Mittelung, Datenstand und Gelände-/Oberflächenbezug begrenzen die Aussage zusätzlich.', qgis)
    card(p, 85, 275, 450, 300, 'Punkt', 'Koordinatenunsicherheit\nund Rundung', size=24)
    card(p, 575, 275, 450, 300, 'Raster', '10-m-Zelle, Mittelung\nund Höhengenauigkeit', color=ORANGE, size=23)
    card(p, 1065, 275, 450, 300, 'Beziehung', 'starkes Relief innerhalb\nder möglichen Punktlage', size=23)
    band(p, 'Abtasten ist rechnerisch eindeutig – die fachliche Aussage bleibt begrenzt.', size=22)

    p = slide('Quelle, Verarbeitung und Ergebnis dokumentieren', 'Dokumentation · Übergabe', 84, 85,
        'Die Mindestangaben sichern. DHHN2016_NH ist der Höhenbezug, EPSG:25832 der horizontale Raumbezug. '
        'Die DGM-Lücke und 21 NULL-Werte sind dokumentierte Datenmerkmale, kein Fehler, der verborgen werden soll.', qgis+'\n'+DGM_SOURCE)
    table(p, ['Dokumentieren', 'Heute'], [
        ['Quelle / Produkt', 'Hessen DGM1 → 10-m-Kursraster'],
        ['Raumbezug', 'EPSG:25832 · Höhe in m · DHHN2016_NH'],
        ['NoData / Abtasten', '-9999 → NULL · ohne Interpolation'],
        ['Ergebnis', 'gbif_mit_hoehe · 56 = 35 Werte + 21 NULL'],
        ['Aussagegrenze', 'Raster- und Koordinatenunsicherheit']], [520, 910], y=230, row_h=90, size=21)

    p = slide('Exit Ticket · eine Frage auswählen', 'Sicherung · Einzelarbeit', 85, 88,
        'Genau eine der drei Fragen auswählen und sichtbar markieren. Zwei Minuten einzeln schreiben lassen, anschließend höchstens eine knappe Antwort einsammeln. '
        'Nicht alle drei Fragen bearbeiten lassen.', overview)
    table(p, ['Option', 'Frage'], [
        ['A', 'Warum ist eine kleine Rasterzelle kein Beweis für hohe Genauigkeit?'],
        ['B', 'Warum darf NoData nicht als Höhenwert 0 interpretiert werden?'],
        ['C', 'Welche Unsicherheiten treffen beim Feld hoehe_m zusammen?']], [180, 1250], y=235, row_h=130, size=22)
    band(p, 'Heute ausgewählt: [A / B / C]', size=24)

    p = slide('Nachbereitung · JiTT zu Unit 13', 'Ausblick', 88, 90,
        'Nur die JiTT-Aufgabe als verbindliche Nachbereitung nennen. Fragen, Frist und endgültiger Link stehen in ILIAS. '
        'Der Link auf der Kursseite ist noch ein sichtbarer Platzhalter; keinen Wert erfinden. Unit 14 kartiert nur die 35 Punkte mit gültigem hoehe_m und dokumentiert diese Einschränkung.', assignment)
    card(p, 130, 260, 620, 300, 'Einzige Übungsaufgabe', 'JiTT-Fragen zu Unit 13\nim ILIAS-Kurs beantworten', size=27)
    card(p, 850, 260, 620, 300, 'Nächste Unit', '35 gültige Höhenwerte\nklassifizieren und kartieren', color=ORANGE, size=25)
    band(p, 'Fragen, Frist und Link: ausschließlich die aktuellen Angaben in ILIAS verwenden.', size=21)

    p = slide('Vertiefung: Neuabtastung bewusst wählen', 'Reserve · Resampling', 0, 0,
        'Nur bei Rückfragen verwenden. Bei geändertem Gitter entstehen neue Rasterwerte. Für Kategorien ist meist nächster Nachbar geeignet; bilineare oder kubische Verfahren berechnen Zwischenwerte und passen eher zu kontinuierlichen Daten. '
        'In der Kernübung wird das DGM nicht eigenständig reprojiziert oder neu abgetastet.', properties, reserve=True)
    table(p, ['Rastertyp', 'häufiges Verfahren', 'Begründung'], [
        ['kategorial', 'nächster Nachbar', 'erhält vorhandene Klassencodes'],
        ['kontinuierlich', 'bilinear / kubisch', 'bildet Übergänge aus Nachbarwerten']], [420, 460, 550], y=290, row_h=135, size=24)
    band(p, 'Resampling erzeugt keine neue gemessene Information.', size=24)

    p = slide('Quellen und Arbeitsstand', 'Reserve · Nachweise', 0, 0,
        'Nur bei Bedarf zeigen. Die Folie dokumentiert Kursseiten, QGIS-Dokumentation und Datenquelle. '
        'Die Live-Erreichbarkeit externer Seiten ist für den Präsenzkern nicht erforderlich.', overview, reserve=True)
    links = [('Unit 13 · Kursübersicht', overview),
             ('Das Rastermodell', model),
             ('Eigenschaften von Rasterdaten', properties),
             ('Rasterdaten in QGIS', qgis),
             ('QGIS 3.40 · Benutzerhandbuch', QDOC),
             ('Hessen Geodatenmanagement · DGM', DGM_SOURCE),
             ('Hessen Geodatenmanagement · Open Data', OPEN_DATA)]
    for i, (label, url) in enumerate(links):
        shape = text(p, 110, 215+i*61, 1380, 52, label, 23, TEAL, True)
        hyperlink(shape, url)
    text(p, 110, 675, 1390, 126,
         'Paketstand: 08.09.2026 · Abgleich der Folien: 09.09.2026\n'
         'Layout: Universität-Marburg-Vorlage · Titel-/Abschlussbild: FB19-Vorlage\n'
         'Lehrabbildungen: sechs vorhandene SVGs der Unit 13', 17, MUTED)

    p = slide('Vielen Dank für Ihre Aufmerksamkeit', 'Abschluss', 90, 90,
        'Die Sitzung mit dieser Folie beenden. Die Abschlussgestaltung nutzt den Kontakt-Master der universitären Vorlage sowie das originale Foto-/Kartenmotiv aus der FB19-Titelseite.', str(TEMPLATE), kind='closing')
    box(p, 44, 44, 809, 807, 0xF7DEED)
    picture(p, FB19_IMAGE, 915, 350, 640, 640*135/394)
    text(p, 100, 380, 700, 250, 'Vielen Dank für Ihre Aufmerksamkeit', 41, INK)
    text(p, 165, 710, 620, 110, 'Geodaten · Unit 13\nFachbereich 19 · Geographie', 18, INK)


def main():
    global DOC, MASTERS
    with tempfile.TemporaryDirectory(prefix='geomoer-unit13-') as profile:
        pipe = 'geomoer_unit13_' + uuid.uuid4().hex
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
            DOC.DocumentProperties.Title = 'Unit 13 – Rasterdaten und Höhenwerte'
            DOC.DocumentProperties.Subject = 'Geodaten · Unit 13 · Präsenzlehre'
            DOC.DocumentProperties.Author = 'GeoMOER'
            build()
            pptx = OUT/'unit13_praesenz.pptx'
            DOC.storeAsURL(pptx.as_uri(), (prop('FilterName', 'Impress MS PowerPoint 2007 XML'), prop('Overwrite', True)))
            DOC.close(True)
            DOC = desktop.loadComponentFromURL(pptx.as_uri(), '_blank', 0, (prop('Hidden', True),))
            base.DOC = DOC
            assert DOC.getDrawPages().Count == len(RECORDS)
            pdf = OUT/'unit13_praesenz.pdf'
            DOC.storeToURL(pdf.as_uri(), (prop('FilterName', 'impress_pdf_Export'), prop('Overwrite', True),
                prop('FilterData', (prop('ExportNotesPages', False), prop('ExportHiddenSlides', True), prop('UseTaggedPDF', True)))))
            DOC.close(True)
            PUBLISHED_PDF.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(pdf, PUBLISHED_PDF)
            with (OUT/'moderation.md').open('w') as fp:
                fp.write('# Unit 13 – Moderation\n\nTitelfolie, 32 Hauptfolien für 90 Minuten, zwei Reserve-/Quellenfolien und eine Abschlussfolie. Zeitangaben stehen nur in diesen Notizen.\n\n')
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
