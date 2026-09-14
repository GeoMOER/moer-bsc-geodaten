#!/usr/bin/python3
"""Build the Unit 11 classroom deck with LibreOffice UNO (no downloads).

Run with /usr/bin/python3, which provides the distro's python3-uno package.
Text, tables and diagrams remain editable PowerPoint shapes. Shared drawing
helpers are loaded from the Unit 10 builder so both decks stay consistent.
"""
from pathlib import Path
import importlib.util
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
PACKAGE = ROOT/'assets/data/marburg/marburg_geodaten.zip'
COURSE = 'https://geomoer.github.io/moer-bsc-geodaten/unit11/'
QDOC = 'https://docs.qgis.org/3.40/en/docs/user_manual/'
GBIF = 'https://www.gbif.org/'
DATASET = 'https://doi.org/10.15468/uc1apo'
RECORDS = []

spec = importlib.util.spec_from_file_location('unit10_slide_helpers', OUT.parent/'unit10/build_slides.py')
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)

W, H, SCALE = base.W, base.H, base.SCALE
INK, TEAL, ORANGE = base.INK, base.TEAL, base.ORANGE
BG, WHITE, PALE, GRID, MUTED = base.BG, base.WHITE, base.PALE, base.GRID, base.MUTED
prop, enum = base.prop, base.enum
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
             'Universität Marburg | Fachbereich 19 · Geographie | Geodaten · Unit 11', 10, MUTED)
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
    overview = COURSE+'unit11-00_overview.html'
    points = COURSE+'unit11-01_punktdaten.html'
    gbif = COURSE+'unit11-02_gbif.html'
    qgis = COURSE+'unit11-03_punkte_qgis.html'
    assignment = COURSE+'unit11-04_assignment.html'
    core = 'https://geomoer.github.io/moer-bsc-geodaten/material/qgis-kernpfade.html#unit11'

    p = slide('Punktdaten, GBIF und Datenqualität', 'Unit 11', 0, 0,
        'Titelfolie beim Ankommen zeigen. Die Sitzung ist für 90 Minuten mit 100–150 Bachelor- und Lehramtsstudierenden ausgelegt. '
        'Vorbereitendes Lesen wird nicht vorausgesetzt. QGIS 3.40 und das vollständig entpackte Marburger Übungspaket müssen vor Sitzungsbeginn verfügbar sein. '
        'Alle Studierenden bearbeiten denselben Kernpfad. Die Folien unterscheiden bewusst Nachweis, Punktgeometrie und Verbreitung.', str(TEMPLATE), kind='title')
    picture(p, FB19_IMAGE, 44, 350, 539, 539*135/394)
    text(p, 625, 285, 850, 300, 'Punktdaten, GBIF\nund Datenqualität', 44, WHITE)
    text(p, 625, 614, 840, 70, 'Unit 11', 28, WHITE)
    text(p, 625, 744, 840, 100, 'Fachbereich 19 · Geographie\nPhilipps-Universität Marburg', 19, WHITE)

    p = slide('JiTT · Rückblick auf Unit 10', 'Platzhalter · vollständig austauschbar', 0, 10,
        'VOR DEM TERMIN: Den gesamten Platzhalter durch die aktuelle JiTT-Auswertung zu Unit 10 ersetzen. '
        'Bei Bedarf die Folie duplizieren. Nur tatsächliche, zusammengefasste und anonymisierte Rückmeldungen einsetzen. '
        'Die gesamte Phase dauert zehn Minuten. Verständnisfragen zu Datenmodellen, Layern, Datenquellen oder CRS klären.')
    shape = box(p, 100, 237, 1400, 545, PALE, GRID)
    shape.Name = 'JiTT – vollständigen Block ersetzen'
    text(p, 180, 430, 1240, 130, '[Hier den vollständigen\nJiTT-Block einfügen]', 38, TEAL, False, 'CENTER')

    p = slide('Vom Nachweis zum geprüften Punktlayer', 'Unit 11 · Orientierung', 10, 11,
        'Den roten Faden ankündigen: Bedeutung von Punktdaten klären, den dokumentierten GBIF-Snapshot als CSV importieren, eine begründete Qualitätsregel anwenden und das Ergebnis reproduzierbar exportieren.', overview)
    picture(p, ROOT/'assets/images/unit11/hero-unit11.jpg', 85, 225, 1430, 1430/6)
    for x, label, body in [(85, 'Nachweis lesen', 'Record, Position und\nUnsicherheit trennen'),
                           (570, 'Qualität prüfen', 'Regel anwenden und\nAusnahmen dokumentieren'),
                           (1055, 'Ergebnis sichern', '56 Punkte exportieren\nund dokumentieren')]:
        card(p, x, 495, 460, 205, label, body, size=22)
    band(p, 'Verbindliches Ergebnis: unit11_results.gpkg · Layer gbif_checked', size=22)

    p = slide('Ein Punkt ist eine Repräsentation', 'Punktdaten · Begriffe trennen', 11, 14,
        'Die vier Ebenen nacheinander benennen. Der sichtbare Kreis auf der Karte ist nicht die räumliche Ausdehnung des Tiers. '
        'Die Unsicherheit beschreibt die Lageangabe, nicht das Streifgebiet. Diese Trennung später beim Import wieder aufnehmen.', points+'\nBild: assets/images/unit11/punkt-beobachtung-unsicherheit.svg')
    picture(p, ROOT/'assets/images/unit11/punkt-beobachtung-unsicherheit.svg', 485, 215, 515, 515*714/640)
    text(p, 1115, 280, 350, 240, 'Beobachtung\n≠ Koordinate\n≠ Punktsymbol', 29, TEAL, True, 'CENTER')
    text(p, 1115, 565, 350, 125, 'Unsicherheit\n≠ Lebensraum', 26, ORANGE, True, 'CENTER')

    p = slide('Ein Record ist nicht automatisch ein Tier', 'Punktdaten · Datenmodell', 14, 17,
        'Kurze Nachbarschaftsfrage: Was könnte eine Tabellenzeile repräsentieren? Danach die Ebenen aufdecken. '
        'Ein Occurrence Record dokumentiert einen Nachweis. Mehrere Records können dasselbe Individuum, denselben Ort oder verschiedene Ereignisse betreffen.', points)
    for x, label, body in [(85, 'Ereignis', 'Ein Organismus wird\nerfasst oder belegt.'),
                           (455, 'Record', 'Eine Zeile hält Angaben\nzum Nachweis fest.'),
                           (825, 'Feature', 'Koordinaten werden als\nGeometrie interpretiert.'),
                           (1195, 'Symbol', 'Darstellung mit Farbe\nund sichtbarer Größe.')]:
        card(p, x, 260, 330, 330, label, body, size=21)
    band(p, 'Prüffrage: Was ist hier gezählt – Individuen, Ereignisse oder Records?', size=22)

    p = slide('Drei Records können wie zwei Punkte aussehen', 'Punktdaten · Überlagerung', 17, 20,
        'Zuerst nur die Grafik lesen lassen. A und B besitzen dieselben Koordinaten, aber verschiedene Daten. Sie überlagern sich in der Karte, bleiben jedoch zwei Records. '
        'Daraus folgt: gleiche Koordinaten sind kein ausreichender Grund zum Löschen.', points+'\nBild: assets/images/unit11/beobachtungen-gleicher-ort.svg')
    picture(p, ROOT/'assets/images/unit11/beobachtungen-gleicher-ort.svg', 430, 215, 495, 495*750/640)
    card(p, 990, 280, 470, 175, 'Karte', 'zwei sichtbare Positionen', size=22)
    card(p, 990, 500, 470, 175, 'Tabelle', 'drei unterscheidbare Records', color=ORANGE, size=22)

    p = slide('Was dokumentiert ein GBIF Occurrence Record?', 'GBIF · Bedeutung', 20, 22,
        'GBIF als internationale Dateninfrastruktur und Aggregator erklären. Der Record kann auf Beobachtung, Beleg, Probe oder anderer Grundlage beruhen. '
        'Das Feld basisOfRecord muss gelesen werden. GBIF bleibt nicht automatisch die ursprüngliche Quelle.', gbif+'\n'+GBIF)
    table(p, ['Ebene', 'Frage'], [
        ['Record', 'Welcher Nachweis wird dokumentiert?'],
        ['Datensatz', 'Zu welcher Veröffentlichung gehört er?'],
        ['Herausgeber', 'Wer stellte die Daten bereit?'],
        ['GBIF', 'Wie wurde der Record vereinheitlicht und auffindbar?']], [390, 1040], y=245, row_h=96, size=23)
    band(p, 'Occurrence ist weiter als „direkte Beobachtung eines lebenden Tiers“.', size=22)

    p = slide('Welche Felder brauchen wir heute?', 'GBIF · Record lesen', 22, 23,
        'Die sechs Gruppen kurz anreißen. Nicht alle GBIF-Spalten im Plenum erklären. Für den Praxisweg sind Kennung, Taxon, Zeitpunkt, Koordinaten, Unsicherheit, Herkunft und Prüfhinweise zentral.', gbif)
    items = [('Kennung', 'gbifID'), ('Taxon', 'species'), ('Grundlage', 'basisOfRecord'),
             ('Zeit', 'eventDate'), ('Ort', 'decimalLongitude\ndecimalLatitude'), ('Qualität', 'coordinateUncertaintyInMeters')]
    for i, (label, body) in enumerate(items):
        x = 85 + (i % 3)*490
        y = 245 + (i // 3)*235
        card(p, x, y, 460, 190, label, body, color=ORANGE if label == 'Qualität' else TEAL, size=21)

    p = slide('Kurz prüfen: Was zeigt eine Punktkarte?', 'Punktdaten · Nachbarschaftsgespräch', 22, 23,
        '30 Sekunden zu zweit: Die Aussage bewerten. Danach Handzeichen für „belegt“, „nicht belegt“ oder „unsicher“. Noch nicht ausführlich auflösen; die Aussage am Ende mit dem Qualitätslayer erneut aufgreifen.', points)
    text(p, 160, 260, 1280, 190, '„In Bereichen ohne Punkte kommt der\nFeuersalamander nicht vor.“', 37, INK, True, 'CENTER')
    band(p, 'Belegt · nicht belegt · unsicher? Begründen Sie mit einem Satz.', y=600, size=24)

    p = slide('Die Karte zeigt dokumentierte Nachweise', 'Punktdaten · Zwischenfazit', 22, 23,
        'Knapp auflösen: Die Punkte belegen Records in der gewählten Auswahl. Fehlende Punkte können fehlende Beobachtung oder fehlende Meldung bedeuten. '
        'Die genauere Formulierung folgt in Minute 83. Diese Folie höchstens 30 Sekunden zeigen.', points)
    text(p, 150, 280, 1300, 100, 'Punkte vorhanden', 31, TEAL, True, 'CENTER')
    text(p, 150, 390, 1300, 70, '→ dokumentierte Nachweise im Datenausschnitt', 28, INK, False, 'CENTER')
    line(p, 260, 500, 1340, 500, GRID, 70)
    text(p, 150, 555, 1300, 100, 'Keine Punkte vorhanden', 31, ORANGE, True, 'CENTER')
    text(p, 150, 665, 1300, 70, '↛ automatisch Abwesenheit der Art', 28, INK, False, 'CENTER')

    p = slide('QGIS-Wiedereinstieg nach der Pause', 'QGIS · Oberfläche', 23, 26,
        'QGIS öffnen lassen und vier Elemente per Handzeichen oder Zuruf wiederholen: Browser, Layerfenster, Kartenfenster und Projekt-CRS. '
        'Die Abbildung stammt aus Unit 10. Keine vollständige Wiederholung der Oberfläche.', core+'\nBild: assets/images/unit10/qgis-oberflaeche.svg')
    picture(p, ROOT/'assets/images/unit10/qgis-oberflaeche.svg', 300, 215, 1000, 570)

    p = slide('Projekt anlegen und Basis laden', 'QGIS · Startzustand', 26, 28,
        'Alle führen die drei Schritte gleichzeitig aus. Wenn ein Pfad scheitert, Paketordner prüfen und nicht frei im Dateisystem suchen lassen. '
        'Das Untersuchungsgebiet ist ein didaktisches Rechteck und keine Verwaltungsgrenze.', qgis+'\n'+core)
    steps(p, [('Projekt speichern', 'Als unit11_punktdaten.qgz im eigenen Arbeitsordner.'),
              ('Projekt-CRS setzen', 'EPSG:25832 · ETRS89 / UTM zone 32N.'),
              ('Basis laden', 'data_raw/marburg_basis.gpkg · Layer untersuchungsgebiet.')], y=250, gap=170)
    band(p, 'Kontrolle: Projektname sichtbar · EPSG:25832 · Rechteck im Kartenfenster', size=22)

    p = slide('Woher kommen die heutigen 79 Records?', 'GBIF · Dokumentierter Snapshot', 28, 30,
        'Den Ablauf von links nach rechts lesen. Der Kurs nutzt einen dokumentierten API-Snapshot ohne eigenen Download-DOI. '
        'Der DOI 10.15468/uc1apo gehört zum Quelldatensatz NABU|naturgucker. Eine eigene GBIF-Occurrence-Auswahl würde einen separaten DOI erhalten.', gbif+'\nBild: assets/images/unit11/gbif-workflow.svg\n'+DATASET)
    picture(p, ROOT/'assets/images/unit11/gbif-workflow.svg', 315, 220, 970, 970*470/1000)
    band(p, 'Heute: bereitgestellter Snapshot → Qualitätsregel → dokumentierter Export', size=22)

    p = slide('CSV zuerst als Tabelle lesen', 'Import · Struktur prüfen', 30, 33,
        'Die Datei nicht in einer Tabellenkalkulation speichern oder verändern. Gemeinsam Kopfzeile und erste Zeile lesen. '
        'Die leere occurrenceID ist zulässig; gbifID dient als Kennung. Koordinaten liegen in Dezimalgrad vor. CSV und CSVT bleiben nebeneinander.', qgis)
    table(p, ['Feld', 'Beispiel', 'Bedeutung'], [
        ['gbifID', '5012616638', 'Kennung'],
        ['species', 'Salamandra salamandra', 'Art'],
        ['decimalLongitude', '8.817572', 'x · Länge'],
        ['decimalLatitude', '50.807076', 'y · Breite'],
        ['coordinateUncertainty…', '25.0', 'Unsicherheit in m']], [410, 480, 540], y=220, row_h=80, size=20)
    band(p, 'Datei: data_raw/gbif_feuersalamander_marburg.csv · 79 Zeilen', size=21)

    p = slide('Textdatei als Punktlayer importieren', 'Import · Dialog', 33, 37,
        'Den Dialog am Beamer schrittweise zeigen und genug Zeit zum Nachvollziehen lassen. Die Abbildung entspricht dem Kursweg. '
        'Wichtig: x und y nicht vertauschen; das Geometrie-CRS beschreibt die Koordinaten in der Datei.', qgis+'\nBild: assets/images/unit11/qgis-csv-import.svg')
    picture(p, ROOT/'assets/images/unit11/qgis-csv-import.svg', 300, 215, 1000, 570)

    p = slide('Vier Importangaben müssen zusammenpassen', 'Import · Einstellungen', 37, 40,
        'Die vier Angaben per Zuruf kontrollieren. EPSG:4326 ist das CRS der Eingangskoordinaten; das Projekt bleibt EPSG:25832. '
        'QGIS transformiert die Anzeige zunächst dynamisch. Den temporären Layer gbif_feuersalamander_raw nennen.', qgis)
    table(p, ['Angabe', 'Wert'], [
        ['Kodierung / Trennzeichen', 'UTF-8 / Komma'],
        ['x-Feld', 'decimalLongitude'],
        ['y-Feld', 'decimalLatitude'],
        ['Geometrie-CRS', 'EPSG:4326 · WGS 84']], [570, 860], y=235, row_h=90, size=23)
    band(p, 'Import-CRS = Bedeutung der Zahlen · nicht gewünschtes Ausgabe-CRS', size=23)

    p = slide('Erstkontrolle nach dem Import', 'Import · Plausibilität', 40, 43,
        'Nicht sofort weiterarbeiten. Zuerst Anzahl, Lage und Attribute kontrollieren. Erwartet werden 79 Records innerhalb beziehungsweise nahe dem Untersuchungsrechteck. '
        'Bei Punkten im Meer oder außerhalb Europas zuerst x/y und EPSG:4326 prüfen.', qgis)
    steps(p, [('Anzahl', '79 Records im Layer gbif_feuersalamander_raw.'),
              ('Lage', 'Auf Layer zoomen; Punkte liegen im Marburger Ausschnitt.'),
              ('Attribute', 'gbifID, Art, Koordinaten und Unsicherheit stichprobenartig lesen.')], y=250, gap=170)
    band(p, 'Fehlerbild weit weg? Meist sind x/y vertauscht oder das Import-CRS falsch.', size=21)

    p = slide('Was bedeutet Koordinatenunsicherheit?', 'Qualität · Raumbezug', 43, 47,
        'Die Grafik erneut fachlich lesen: Der gespeicherte Punkt ist eine Lageangabe. Der Unsicherheitsbereich beschreibt, wo der tatsächliche Ort im Rahmen der Angabe liegen kann. '
        'Er ist weder Symbolgröße noch Lebensraum. 0 m wird für die Kursauswahl nicht als belastbare Angabe akzeptiert.', gbif+'\nBild: assets/images/unit11/punkt-beobachtung-unsicherheit.svg')
    picture(p, ROOT/'assets/images/unit11/punkt-beobachtung-unsicherheit.svg', 280, 215, 515, 515*714/640)
    card(p, 900, 285, 560, 180, 'Heute akzeptiert', '> 0 m und ≤ 100 m', color=TEAL, size=25)
    card(p, 900, 515, 560, 180, 'Ausgeschlossen', 'fehlend, 0 m oder > 100 m', color=ORANGE, size=23)

    p = slide('Eine Qualitätsregel braucht eine Begründung', 'Qualität · Entscheidung', 47, 51,
        'Grenzwerte sind keine universellen Naturgesetze. Für die kleinräumige Kursaufgabe wird eine dokumentierte, positive Unsicherheit bis 100 m verlangt. '
        'Andere Fragestellungen können eine andere Schwelle erfordern. Die Originaldaten werden nicht gelöscht.', qgis)
    card(p, 85, 260, 440, 310, 'Fragestellung', 'kleinräumige Darstellung\nim Marburger Ausschnitt', size=23)
    card(p, 580, 260, 440, 310, 'Regel', '0 < Unsicherheit\n≤ 100 m', color=ORANGE, size=28)
    card(p, 1075, 260, 440, 310, 'Dokumentation', 'Schwelle, Anzahl und\nAusschlüsse festhalten', size=23)
    band(p, 'Transparent und reproduzierbar ist wichtiger als „perfekt bereinigt“.', size=22)

    p = slide('Auswahl mit einem Ausdruck', 'Qualität · QGIS-Auswahl', 51, 55,
        'Attributtabelle öffnen und „Objekte über Ausdruck wählen“ verwenden. Den Ausdruck genau übernehmen. '
        'NULL-Werte erfüllen beide Bedingungen nicht. Die Auswahl bleibt sichtbar und kontrollierbar; noch nichts exportieren.', qgis)
    box(p, 135, 280, 1330, 210, 0xF4F4F4, GRID)
    text(p, 175, 330, 1250, 110, '"coordinateUncertaintyInMeters" > 0\nAND "coordinateUncertaintyInMeters" <= 100', 29, INK, True, 'CENTER')
    band(p, 'Logik: positive Angabe UND höchstens 100 Meter', y=595, size=25)

    p = slide('Prüfwert: 56 ausgewählt, 23 ausgeschlossen', 'Qualität · Ergebnis kontrollieren', 55, 58,
        'Ergebnis per Handzeichen abfragen, dann zeigen. Bei Abweichung nicht improvisiert weiterexportieren: Feldtyp, Ausdruck und Gesamtzahl prüfen. '
        'Im Snapshot besitzen die 23 ausgeschlossenen Records jeweils 250 m Unsicherheit.', qgis)
    card(p, 150, 270, 590, 320, '56', 'ausgewählt\n> 0 m und ≤ 100 m', color=TEAL, size=28)
    card(p, 860, 270, 590, 320, '23', 'ausgeschlossen\njeweils 250 m', color=ORANGE, size=28)
    band(p, 'Kontrollsumme: 56 + 23 = 79 Records', size=26)

    p = slide('Flags und fehlende Werte nicht pauschal behandeln', 'Qualität · Grenzen', 58, 60,
        'Drei Fehlannahmen vermeiden. GBIF-Issues sind Prüfhinweise und müssen fachlich gelesen werden. '
        'Ein fehlender Unsicherheitswert ist nicht 0 m. Ein leerer Issue-Eintrag beweist nicht Fehlerfreiheit.', gbif)
    table(p, ['Fehlannahme', 'Bessere Arbeitsregel'], [
        ['issue vorhanden → löschen', 'Hinweis lesen und zur Frage bewerten'],
        ['Unsicherheit fehlt → 0 m', 'fehlend bleibt unbekannt'],
        ['issue leer → fehlerfrei', 'weitere Plausibilitätsprüfungen bleiben nötig']], [630, 800], y=270, row_h=112, size=23)

    p = slide('Partnercheck vor dem Export', 'Qualität · 2 Minuten', 60, 62,
        'Je zwei Nachbarinnen oder Nachbarn vergleichen ihren Zustand. In der großen Gruppe nur die drei Kontrollpunkte prüfen. '
        'Wer fertig ist, hilft beim Lesen der Werte; keine zusätzliche Analyse beginnen.', qgis)
    steps(p, [('Layer', 'gbif_feuersalamander_raw enthält 79 Records.'),
              ('Ausdruck', 'positive Unsicherheit und höchstens 100 m.'),
              ('Auswahl', '56 markiert; 23 nicht ausgewählt.')], y=250, gap=170)
    band(p, 'Erst bei 79 / 56 / 23 gemeinsam zum Export wechseln.', size=23)

    p = slide('Auswahl exportieren – Rohdaten erhalten', 'Export · Prinzip', 62, 64,
        'Klarstellen: Es werden nur ausgewählte Features in einen neuen Layer geschrieben. Der Rohdatenlayer bleibt unverändert und kann die Entscheidung später nachvollziehbar machen.', qgis)
    card(p, 110, 290, 560, 300, 'Rohdaten', 'gbif_feuersalamander_raw\n79 Records · EPSG:4326', size=25)
    text(p, 720, 390, 160, 80, '→', 48, TEAL, True, 'CENTER')
    card(p, 930, 290, 560, 300, 'Prüfergebnis', 'gbif_checked\n56 Records · EPSG:25832', color=ORANGE, size=25)
    band(p, 'Auswahl ist eine dokumentierte Ableitung – kein Ersatz für die Quelle.', size=22)

    p = slide('GeoPackage und Layer eindeutig benennen', 'Export · Einstellungen', 64, 68,
        'Rechtsklick auf den Rohdatenlayer: Exportieren → Ausgewählte Objekte speichern als. Den Haken für nur ausgewählte Objekte kontrollieren. '
        'Die Datei im Ordner data_output erzeugen; Layername exakt gbif_checked.', qgis+'\n'+core)
    table(p, ['Einstellung', 'Wert'], [
        ['Format', 'GeoPackage'],
        ['Datei', 'data_output/unit11_results.gpkg'],
        ['Layername', 'gbif_checked'],
        ['Nur ausgewählte Objekte', 'ja'],
        ['CRS', 'EPSG:25832']], [560, 870], y=235, row_h=96, size=24)

    p = slide('Beim Export wird wirklich transformiert', 'Export · CRS', 68, 71,
        'An Unit 09 anknüpfen: Die Eingangszahlen werden als EPSG:4326 interpretiert. Beim Export nach EPSG:25832 berechnet QGIS neue Koordinaten. '
        'Nur ein anderes CRS zuzuweisen wäre falsch. Das Projekt-CRS allein ändert die gespeicherten Quelldaten nicht.', qgis)
    card(p, 110, 280, 520, 280, 'Import', '8.817572 / 50.807076\nals EPSG:4326 verstehen', size=24)
    text(p, 680, 350, 240, 110, '→', 48, TEAL, True, 'CENTER')
    card(p, 970, 280, 520, 280, 'Export', 'Koordinaten neu berechnen\nund als EPSG:25832 speichern', color=ORANGE, size=24)
    band(p, 'Zuordnen ändert nur das Etikett · Transformieren ändert die Koordinatenwerte.', size=22)

    p = slide('Neu laden und Ergebnis kontrollieren', 'Export · Abschluss', 71, 75,
        'Den neu erzeugten Layer aus dem Browser laden, den temporären Rohdatenlayer deaktivieren und das Projekt speichern. '
        'Erwartet werden 56 Punkte. Wenn Export scheitert, den Ersatzlayer ersatz/unit11_results.gpkg · gbif_checked laden und den Fehler dokumentieren.', qgis+'\n'+core)
    steps(p, [('Neu laden', 'data_output/unit11_results.gpkg · gbif_checked.'),
              ('Kontrollieren', '56 Features · EPSG:25832 · Lage plausibel.'),
              ('Sichern', 'Rohdatenlayer deaktivieren und Projekt speichern.')], y=240, gap=170)
    band(p, 'Fallback: ersatz/unit11_results.gpkg · gbif_checked', size=23)

    p = slide('Die Qualitätsentscheidung dokumentieren', 'Dokumentation · Reproduzierbarkeit', 75, 78,
        'Die Gruppe nennt die Angaben, die eine andere Person zum Nachvollziehen braucht. Anschließend die Liste zeigen. '
        'Der Datensatz-DOI ist nicht als eigener GBIF-Download-DOI auszugeben.', qgis+'\n'+DATASET)
    table(p, ['Dokumentieren', 'Heute'], [
        ['Quelle / DOI', 'NABU|naturgucker · 10.15468/uc1apo'],
        ['Snapshot / Abruf', 'GBIF API · 08.09.2026 · 79 Records'],
        ['Import', 'x/y · EPSG:4326'],
        ['Regel', '0 < uncertainty ≤ 100 m · 23 ausgeschlossen'],
        ['Ergebnis', 'gbif_checked · 56 · EPSG:25832']], [510, 920], y=225, row_h=91, size=21)

    p = slide('Viele Punkte können viel Suchaufwand bedeuten', 'Interpretation · Beobachtungsbias', 78, 81,
        'Die beiden Suchsituationen vergleichen lassen. Das Gedankenexperiment isoliert den Einfluss des Suchaufwands; in realen Daten sind unentdeckte Vorkommen unbekannt. '
        'Eine hohe Punktdichte kann häufiges Vorkommen, gute Zugänglichkeit oder aktive Meldung widerspiegeln.', gbif+'\nBild: assets/images/unit11/beobachtungsbias.svg')
    picture(p, ROOT/'assets/images/unit11/beobachtungsbias.svg', 500, 215, 430, 430*858/640)
    card(p, 1010, 300, 475, 175, 'Punktdichte', 'Vorkommen UND\nBeobachtung/Meldung', size=21)
    card(p, 1010, 525, 475, 175, 'Leere Fläche', 'keine dokumentierten\nRecords im Ausschnitt', color=ORANGE, size=20)

    p = slide('Die Ausgangsaussage erneut bewerten', 'Interpretation · Nachbarschaftsgespräch', 81, 83,
        'Noch einmal 45 Sekunden zu zweit formulieren lassen: Was ist an der Aussage zu stark? Danach zwei bis drei Vorschläge hören. '
        'Die Qualitätsauswahl verbessert die dokumentierte Lagegenauigkeit, erzeugt aber keine systematische Verbreitungserhebung.', gbif)
    text(p, 160, 260, 1280, 190, '„In Bereichen ohne Punkte kommt der\nFeuersalamander nicht vor.“', 37, INK, True, 'CENTER')
    band(p, 'Welche Aussage trägt der Layer gbif_checked tatsächlich?', y=600, size=24)

    p = slide('Eine vorsichtige Kartenaussage', 'Interpretation · Auflösung', 83, 85,
        'Die Formulierung laut lesen. Auf die drei Einschränkungen hinweisen: dokumentierte Records, konkreter Datenausschnitt und angewandte Qualitätsregel. '
        'Fehlende Punkte dürfen ohne dokumentierte Suche und Erfassungswahrscheinlichkeit nicht als Abwesenheit interpretiert werden.', gbif)
    box(p, 125, 250, 1350, 330, PALE, GRID)
    text(p, 180, 315, 1240, 220,
         '„Der Layer zeigt 56 dokumentierte Feuersalamander-Records\naus dem bereitgestellten GBIF-Snapshot, deren angegebene\nKoordinatenunsicherheit größer als 0 und höchstens 100 m ist.“',
         29, INK, True, 'CENTER')
    band(p, 'Er zeigt weder alle Individuen noch die vollständige Verbreitung der Art.', size=23)

    p = slide('Exit Ticket · eine Frage auswählen', 'Sicherung · Einzelarbeit', 85, 88,
        'Genau eine der drei Fragen auswählen und sichtbar markieren. Zwei Minuten einzeln schreiben lassen, anschließend höchstens eine knappe Antwort einsammeln. '
        'Nicht alle drei Fragen bearbeiten lassen.', overview)
    table(p, ['Option', 'Frage'], [
        ['A', 'Warum ist ein GBIF-Punkt nicht automatisch ein exakt verortetes lebendes Tier?'],
        ['B', 'Welche drei Angaben müssen beim Import von longitude/latitude stimmen?'],
        ['C', 'Warum zeigt gbif_checked Nachweise, aber nicht die vollständige Verbreitung?']], [180, 1250], y=235, row_h=130, size=22)
    band(p, 'Heute ausgewählt: [A / B / C]', size=24)

    p = slide('Nachbereitung · JiTT zu Unit 11', 'Ausblick', 88, 90,
        'Nur die JiTT-Aufgabe als verbindliche Nachbereitung nennen. Fragen, Frist und endgültiger Link stehen in ILIAS. '
        'Der Link auf der Kursseite ist noch ein sichtbarer Platzhalter; keinen Wert erfinden. Kurz ankündigen, dass gbif_checked in Unit 12 weiterverwendet wird.', assignment)
    card(p, 130, 260, 620, 300, 'Einzige Übungsaufgabe', 'JiTT-Fragen zu Unit 11\nim ILIAS-Kurs beantworten', size=27)
    card(p, 850, 260, 620, 300, 'Nächste Unit', 'gbif_checked als geprüfte\nPunktgrundlage weiterverwenden', color=ORANGE, size=25)
    band(p, 'Fragen, Frist und Link: ausschließlich die aktuellen Angaben in ILIAS verwenden.', size=21)

    p = slide('GBIF-Felder als Lesehilfe', 'Reserve · Record prüfen', 0, 0,
        'Nur bei Rückfragen verwenden. Die Tabelle ist keine zusätzliche Pflichtphase. Zeigen, dass technische Felder jeweils eine fachliche Prüffrage unterstützen.', gbif, reserve=True)
    table(p, ['Feld', 'Prüffrage'], [
        ['gbifID / occurrenceID', 'Ist der Record eindeutig nachvollziehbar?'],
        ['basisOfRecord', 'Worauf beruht der Nachweis?'],
        ['eventDate', 'Wann wurde erfasst?'],
        ['decimalLongitude / Latitude', 'Wo wird der Record verortet?'],
        ['coordinateUncertaintyInMeters', 'Passt die Lagegenauigkeit zur Frage?'],
        ['datasetKey / license / issue', 'Woher stammt er und was ist zu beachten?']], [570, 860], y=220, row_h=86, size=22)

    p = slide('Quellen und Arbeitsstand', 'Reserve · Nachweise', 0, 0,
        'Nur bei Bedarf zeigen. Die Folie dokumentiert Kursseiten, Softwaredokumentation und Datenquelle. '
        'Die Live-Erreichbarkeit externer Seiten ist für den Präsenzkern nicht erforderlich.', overview, reserve=True)
    links = [('Unit 11 · Kursübersicht', overview),
             ('Punktdaten', points),
             ('GBIF und Datenqualität', gbif),
             ('Punktdaten in QGIS', qgis),
             ('QGIS 3.40 · Benutzerhandbuch', QDOC),
             ('NABU|naturgucker · Datensatz-DOI', DATASET)]
    for i, (label, url) in enumerate(links):
        shape = text(p, 110, 220+i*69, 1380, 58, label, 24, TEAL, True)
        hyperlink(shape, url)
    text(p, 110, 675, 1390, 126,
         'Paketstand: 08.09.2026 · Abgleich der Folien: 09.09.2026\n'
         'Layout: Universität-Marburg-Vorlage · Titel-/Abschlussbild: FB19-Vorlage\n'
         'Lehrabbildungen: vorhandene SVGs der Units 10 und 11', 17, MUTED)

    p = slide('Vielen Dank für Ihre Aufmerksamkeit', 'Abschluss', 90, 90,
        'Die Sitzung mit dieser Folie beenden. Die Abschlussgestaltung nutzt den Kontakt-Master der universitären Vorlage sowie das originale Foto-/Kartenmotiv aus der FB19-Titelseite.', str(TEMPLATE), kind='closing')
    box(p, 44, 44, 809, 807, 0xF7DEED)
    picture(p, FB19_IMAGE, 915, 350, 640, 640*135/394)
    text(p, 100, 380, 700, 250, 'Vielen Dank für Ihre Aufmerksamkeit', 41, INK)
    text(p, 165, 710, 620, 110, 'Geodaten · Unit 11\nFachbereich 19 · Geographie', 18, INK)


def main():
    global DOC, MASTERS
    with tempfile.TemporaryDirectory(prefix='geomoer-unit11-') as profile:
        pipe = 'geomoer_unit11_' + uuid.uuid4().hex
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
            DOC.DocumentProperties.Title = 'Unit 11 – Punktdaten, GBIF und Datenqualität'
            DOC.DocumentProperties.Subject = 'Geodaten · Unit 11 · Präsenzlehre'
            DOC.DocumentProperties.Author = 'GeoMOER'
            build()
            pptx = OUT/'unit11_praesenz.pptx'
            DOC.storeAsURL(pptx.as_uri(), (prop('FilterName', 'Impress MS PowerPoint 2007 XML'), prop('Overwrite', True)))
            DOC.close(True)
            DOC = desktop.loadComponentFromURL(pptx.as_uri(), '_blank', 0, (prop('Hidden', True),))
            base.DOC = DOC
            assert DOC.getDrawPages().Count == len(RECORDS)
            DOC.storeToURL((OUT/'unit11_praesenz.pdf').as_uri(), (prop('FilterName', 'impress_pdf_Export'), prop('Overwrite', True),
                prop('FilterData', (prop('ExportNotesPages', False), prop('ExportHiddenSlides', True), prop('UseTaggedPDF', True)))))
            DOC.close(True)
            with (OUT/'moderation.md').open('w') as fp:
                fp.write('# Unit 11 – Moderation\n\nTitelfolie, 32 Hauptfolien für 90 Minuten, zwei Reserve-/Quellenfolien und eine Abschlussfolie. Zeitangaben stehen nur in diesen Notizen.\n\n')
                for record in RECORDS:
                    fp.write(f"## {record['number']:02d} · {record['title']}\n\n{record['notes']}\n\n")
            print(f'Created {len(RECORDS)} slides: {pptx} and matching PDF', flush=True)
        finally:
            if desktop:
                desktop.terminate()
            try:
                proc.wait(timeout=10)
            except subprocess.TimeoutExpired:
                proc.terminate()


if __name__ == '__main__':
    main()
