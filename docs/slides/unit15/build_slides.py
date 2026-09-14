#!/usr/bin/python3
"""Build the Unit 15 classroom deck with LibreOffice UNO.

Run from docs/ with /usr/bin/python3 slides/unit15/build_slides.py.
The Unit 10 builder supplies the established editable drawing helpers.
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
TEMPLATE = ROOT / 'slides/Vorlagen/präs_ms02_powerpoint_de.pptx'
FB19 = ROOT / 'slides/Vorlagen/fb19-praesentationsvorlage_16-9-format.pot'
FB19_IMAGE = OUT / 'assets/fb19-marburg-europa.png'
PUBLISHED_PDF = ROOT / 'assets/pdfs/Geodaten_Slides_Unit15.pdf'
SITE = 'https://geomoer.github.io/moer-bsc-geodaten/'
RECORDS = []

spec = importlib.util.spec_from_file_location('unit10_slide_helpers', OUT.parent / 'unit10/build_slides.py')
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)

W, H = base.W, base.H
INK, TEAL, ORANGE = base.INK, base.TEAL, base.ORANGE
WHITE, PALE, GRID, MUTED = base.WHITE, base.PALE, base.GRID, base.MUTED
prop = base.prop
box, text, picture = base.box, base.text, base.picture
card, band, hyperlink = base.card, base.band, base.hyperlink


def slide(title, section, start, end, notes, sources='', reserve=False, kind='content'):
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
             'Universität Marburg | Fachbereich 19 · Geographie | Geodaten · Unit 15', 10, MUTED)
        text(page, 1512, 850, 42, 25, str(n), 10, INK, False, 'CENTER')
    timing = ('Reserve; außerhalb der 90 Minuten.' if reserve else
              'Titelfolie vor Beginn zeigen.' if kind == 'title' else
              'Nach Minute 90 zeigen; kein zusätzlicher Zeitblock.' if kind == 'closing' else
              f'Zeitfenster: Minute {start}–{end} ({end-start} Minuten).')
    note_text = timing + '\n\n' + notes
    if sources:
        note_text += '\n\nQuellen / Kursseiten:\n' + sources
    note_page = page.getNotesPage()
    for i in range(note_page.Count):
        shape = note_page.getByIndex(i)
        if shape.ShapeType == 'com.sun.star.presentation.NotesShape':
            shape.String = note_text
    RECORDS.append(dict(number=n, title=title, start=start, end=end,
                        reserve=reserve, kind=kind, notes=note_text))
    return page


def early(unit, title, start, concept, message, teacher_note):
    unit_url = f'{SITE}unit{unit:02d}/unit{unit:02d}-00_overview.html'
    p = slide(title, 'Kursrückblick · Grundlagen im Aufbau', start, start + 2,
              teacher_note + ' Die Fachseiten dieser frühen Unit sind noch in Arbeit. '
              'Vor dem Unterricht ein tatsächlich behandeltes Beispiel auswählen; den sichtbaren Platzhalter dann ersetzen. '
              'Keinen unbekannten Arbeitsstand als abgeschlossen darstellen. Diskussionen für Minute 40–60 sammeln.',
              unit_url)
    text(p, 120, 238, 170, 160, f'{unit:02d}', 78, TEAL, True)
    card(p, 320, 240, 1130, 210, 'Bekannter Gedanke', concept, size=29)
    card(p, 320, 485, 1130, 155, 'Zum Mitnehmen', message, color=ORANGE, size=26)
    band(p, f'[Beispiel aus der tatsächlich behandelten Unit {unit:02d} ergänzen]', y=735, size=21)


def geo(unit, title, start, image, metric, body, take, teacher_note, image_size=(1000, 450)):
    unit_url = f'{SITE}unit{unit:02d}/unit{unit:02d}-00_overview.html'
    p = slide(title, 'Kursrückblick · Geodaten', start, start + 2,
              teacher_note + ' Nur einen kurzen Rückblick; längere Nachfragen für Minute 40–60 sammeln.',
              unit_url)
    width = 1050
    height = width * image_size[1] / image_size[0]
    picture(p, ROOT / image, 85, 225, width, height)
    card(p, 1170, 250, 345, 425, metric, body, color=ORANGE, size=20)
    band(p, take, y=735, size=21)


def build():
    overview = SITE + 'unit15/unit15-00_overview.html'
    recap = SITE + 'unit15/unit15-01_rueckblick.html'
    feedback = SITE + 'unit15/unit15-05_assignment.html'

    p = slide('Rückblick, offene Fragen und Kursabschluss', 'Unit 15', 0, 0,
              'Beim Ankommen zeigen. Für Bachelor- und Lehramtsstudierende gilt derselbe gemeinsame Abschluss. '
              'Kein neuer fachlicher Inhalt und keine neue Übungsaufgabe.', overview, kind='title')
    picture(p, FB19_IMAGE, 44, 350, 539, 539*135/394)
    text(p, 625, 275, 860, 315, 'Rückblick, offene Fragen\nund Kursabschluss', 43, WHITE)
    text(p, 625, 614, 840, 70, 'Unit 15', 28, WHITE)
    text(p, 625, 744, 840, 100, 'Fachbereich 19 · Geographie\nPhilipps-Universität Marburg', 19, WHITE)

    p = slide('JiTT: Rückblick auf Unit 14', 'Platzhalter · vollständig austauschbar', 0, 10,
              'Vor dem Termin die aggregierten JiTT-Ergebnisse zu Unit 14 sichten. Den ganzen Platzhalter durch '
              'zwei bis drei tatsächliche Fragen und anonymisierte Antwortverteilungen ersetzen. '
              'Begründung und typisches Missverständnis zu Klassierung, Symbolisierung, Layout oder Aussagegrenze klären. '
              'Keine Namen, Noten, neue Abstimmung oder weiteren Test zeigen. Die ganze Phase dauert zehn Minuten. '
              'Überleitung: „Die Abschlusskarte verbindet viele Schritte unseres Kurses. Wir gehen nun den Weg von den ersten Daten bis zu dieser Karte noch einmal durch.“',
              overview)
    shape = box(p, 100, 237, 1400, 545, PALE, GRID)
    shape.Name = 'JiTT – vollständigen Block ersetzen'
    text(p, 180, 390, 1240, 185,
         '[Hier 2–3 tatsächliche JiTT-Fragen\nund aggregierte Antworten zu Unit 14 einfügen]',
         32, TEAL, False, 'CENTER')

    early(1, 'Unit 01: Digitale Daten und Computer', 10,
          'Dateien speichern und wiederfinden',
          'Kodierung, Format und Speicherort gehören zusammen.',
          'An einem tatsächlich benutzten Datei- oder Pfadfall erinnern: dauerhafte Speicherung ist etwas anderes als Arbeitsspeicher.')
    early(2, 'Unit 02: Daten in Tabellen erfassen', 12,
          'Eine Beobachtung pro Zeile · ein Merkmal pro Spalte',
          'Anzeige, Datentyp und Bedeutung gemeinsam prüfen.',
          'Nur eine bekannte Tabelle aufgreifen; Textzahlen und Datumswerte als mögliche Fehler kurz benennen.')
    early(3, 'Unit 03: Daten organisieren und bereinigen', 14,
          'Rohdaten und Bearbeitungsschritte erhalten',
          'Fehlend, gefiltert und gelöscht sind verschiedene Zustände.',
          'Nur bei vorhandenem Kursbeispiel Original und bereinigte Tabelle gegenüberstellen; Protokoll als Beleg nennen.')
    early(4, 'Unit 04: Daten mit Kennwerten beschreiben', 16,
          'Lage und Streuung einer Verteilung betrachten',
          'Ein Mittelwert allein zeigt weder Ausreißer noch Streuung.',
          'Nur eine tatsächlich behandelte Verteilung zeigen; Median und Mittelwert ohne neue Rechnung erinnern.')
    early(5, 'Unit 05: Zusammenfassen und Zusammenhänge betrachten', 18,
          'Kennzahl und Grafik gemeinsam lesen',
          'Korrelation beweist keine Ursache.',
          'Nur ein tatsächlich besprochenes Streudiagramm oder Pivot-Beispiel verwenden; Muster und Ausreißer nennen.')
    early(6, 'Unit 06: Wiederkehrende Schritte in Excel', 20,
          'Formeln kopieren und Zellbezüge kontrollieren',
          'Ein kopierter Bezug muss noch auf die gemeinte Zelle zeigen.',
          'Nur eine im Kurs eingesetzte Formel verwenden; relativen und festen Bezug kurz erinnern.')
    early(7, 'Unit 07: FAIR, README und Versionierung', 22,
          'Herkunft, Struktur, Bearbeitung und Version beschreiben',
          'Andere müssen einen Datenstand finden und verstehen können.',
          'Nur einen tatsächlich besprochenen Datenordner oder eine README zeigen.')
    early(8, 'Unit 08: Wiederkehrende Schritte automatisieren', 24,
          'Eingabe → Regel → Ausgabe → Kontrolle',
          'Wiederholung ersetzt die fachliche Ergebniskontrolle nicht.',
          'Nur einen im Kurs tatsächlich bearbeiteten Ablauf verwenden; keine neue Software-Demonstration.')

    geo(9, 'Unit 09: Koordinaten und CRS', 26,
        'assets/images/unit09/raumbezug.svg', 'Achsen · Einheit · CRS',
        'Koordinaten in Grad oder Metern sind nur mit bekanntem Bezug lesbar.',
        'Zuweisen benennt ein CRS; Transformieren berechnet neue Koordinaten.',
        'Erste von höchstens drei kurzen Rückfragen: Welche Angaben machen ein Koordinatenpaar eindeutig? Erwartet: Achsen, Einheit und CRS.',
        (1000, 430))
    geo(10, 'Unit 10: Datenmodelle und QGIS-Projekt', 28,
        'assets/images/unit10/projekt-layer-datei.svg', 'Projekt · Layer · Datei',
        'Die .qgz-Datei organisiert Darstellung und verweist auf Datenquellen.',
        'Beim erneuten Öffnen müssen die Datenquellen erreichbar bleiben.',
        'Punkt, Linie, Polygon und Raster am ersten QGIS-Projekt kurz wiedererkennen lassen.',
        (1000, 430))
    geo(11, 'Unit 11: GBIF-Punkte prüfen', 30,
        'assets/images/unit11/gbif-workflow.svg', '79 → 56',
        '79 Rohrecords; 56 mit dokumentierter positiver Koordinatenunsicherheit bis 100 m.',
        'Ein Nachweisrecord zeigt keine vollständige Artenverbreitung.',
        'Regel 0 < coordinateUncertaintyInMeters ≤ 100 nennen. Keine neue Qualitätsregel erfinden.',
        (1000, 470))
    geo(12, 'Unit 12: Räumliche Auswahl', 32,
        'assets/images/unit12/vektor-workflow.svg', '10 · 4 · 106',
        '10 FFH-Flächen; schneidet trifft 4 von 56 Punkten und 106 von 412 Gewässerfeatures.',
        'Auswahl markiert ganze Features; Zuschneiden verändert Geometrien.',
        'Zweite kurze Rückfrage: Welche räumliche Beziehung bestimmte die Treffer? Erwartet: schneidet mit ausgewählten FFH-Polygonen.',
        (1000, 450))
    geo(13, 'Unit 13: Rasterwerte abtasten', 34,
        'assets/images/unit13/raster-workflow.svg', '56 = 35 + 21',
        'Feld hoehe_m: 35 gültige DGM-Höhen und 21 NULL-Werte.',
        'NoData ist nicht 0; der Wert gehört zur getroffenen Rasterzelle.',
        'Die räumliche Lücke des DGM als Grund für NULL erinnern. Nicht alle 56 Punkte auf 35 reduzieren.',
        (1000, 450))

    p = slide('Unit 14: Abschlusskarte gestalten', 'Kursrückblick · Geodaten', 36, 38,
              'Die bekannte Karte mit 35 Höhenpunkten zeigen. Dritte kurze Rückfrage: Welche sichtbaren Entscheidungen beeinflussen die Aussage? '
              'Erwartet: Klassengrenzen, sequentielle Farben, Titel, Legende und Quellen. '
              'Die 21 geprüften Nachweise ohne DGM-Höhe und die Grenze „keine vollständige Verbreitungskarte“ benennen.',
              SITE + 'unit14/unit14-00_overview.html')
    picture(p, ROOT / 'assets/data/marburg/abschlusskarte_beispiel.png', 100, 222, 760, 760*1240/1753)
    card(p, 930, 250, 550, 425, '35 Höhenpunkte',
         'Fünf Klassen, Titel, Legende und Quellen machen die Aussage lesbar.\n\n21 weitere Punkte ohne DGM-Höhe.',
         color=ORANGE, size=23)
    band(p, 'Dokumentierte Nachweise – keine vollständige Verbreitungskarte.', y=755, size=21)

    p = slide('Was verbindet die Units?', 'Rückblick · Verbindung', 38, 40,
              'Die Kurskette von Daten zu begründeter Darstellung schließen. Dokumentation und Ergebniskontrolle '
              'begleiten alle Schritte. Über den ganzen Rückblick nur zwei bis drei kurze Rückfragen zulassen. '
              'Überleitung: „Welche dieser Schritte können Sie inzwischen selbst erklären, und wo ist noch etwas offen?“', recap)
    for x, label in [(85, 'Verstehen'), (380, 'Prüfen'), (675, 'Auswerten'), (970, 'Einordnen'), (1265, 'Darstellen')]:
        box(p, x, 300, 260, 175, PALE)
        text(p, x + 8, 365, 244, 65, label, 21, TEAL, True, 'CENTER')
    text(p, 145, 535, 1320, 105, 'Dokumentieren und Ergebnisse kontrollieren – bei jedem Schritt',
         27, TEAL, True, 'CENTER')
    band(p, 'Von der Tabelle bis zur Karte: Was tragen die Daten wirklich?', y=735, size=23)

    p = slide('Für sich nachdenken', 'Persönliche Rückschau', 40, 43,
              'Drei Minuten Einzelarbeit. Jede Person notiert einen jetzt erklärbaren Arbeitsschritt und eine '
              'verbliebene Unsicherheit; Unit oder bekanntes Beispiel ergänzen. Notizen bleiben privat und werden nicht bewertet.', overview)
    card(p, 125, 290, 620, 310, 'Das kann ich erklären', 'Ein Arbeitsschritt aus dem Kurs', size=29)
    card(p, 855, 290, 620, 310, 'Das ist noch offen', 'Eine möglichst konkrete Unsicherheit', color=ORANGE, size=28)
    band(p, 'Ihre Notizen bleiben bei Ihnen.', size=24)

    p = slide('Zu zweit eine Frage formulieren', 'Persönliche Rückschau', 43, 47,
              'Vier Minuten Partneraustausch. Höchstens eine gemeinsame, konkrete Frage formulieren lassen. '
              'Bei 100–150 Personen keine Einzelrunde beginnen; nur die gemeinsame Frage ins Plenum nehmen.', overview)
    card(p, 200, 265, 1200, 345, 'Eine Frage pro Paar',
         '„Bei Unit ___ / dem Beispiel ___ verstehen wir noch nicht, warum …?“', size=34)
    band(p, 'Fragen zur Karte, zu den Daten oder zum Arbeitsweg sind willkommen.', size=23)

    p = slide('Häufige Fragen gemeinsam klären', 'Offene Fragen', 47, 60,
              'Fragen sammeln, ähnliche Fragen bündeln und die häufigsten anhand bereits behandelter Beispiele klären. '
              'Offenbleibende Fragen samt Materialhinweis festhalten. Keine neue Analyse, QGIS-Demo oder Prüfungsbesprechung beginnen. '
              'Überleitung: „Neben Ihren Fragen interessiert uns, welche Teile des Kurses beim Lernen geholfen haben und was wir verbessern sollten.“',
              recap)
    card(p, 120, 255, 615, 365, 'Im Plenum', 'Fragen bündeln\nBekannte Beispiele heranziehen\nMaterialhinweis notieren', size=27)
    card(p, 865, 255, 615, 365, 'Zum Nachschlagen',
         'Unit-15-Rückblick\nUnit-Seiten 09–14\nEigene Projektnotizen', color=ORANGE, size=27)
    band(p, 'Eine unbeantwortete Frage bleibt mit einem passenden Materialhinweis sichtbar.', size=19)

    p = slide('Anonymen Papierfragebogen ausfüllen', 'Freiwilliges Kursfeedback', 60, 68,
              'Fragebogen ohne Namensfeld und Sammelbox austeilen. Acht Minuten für sieben Einschätzungen und '
              'zwei offene Rückmeldungen geben. „Kann ich nicht beurteilen“ ist zulässig. Um keine Namen oder '
              'personenbezogenen Angaben bitten. Gefaltete Bögen in die Box geben lassen; erst nach der Sitzung auswerten.',
              feedback)
    card(p, 130, 260, 610, 365, '7 Einschätzungen', 'Was hat Ihnen beim Lernen geholfen?', size=27)
    card(p, 860, 260, 610, 365, '2 offene Antworten', 'Was beibehalten?\nWas verändern?', color=ORANGE, size=27)
    band(p, 'Freiwillig · ohne Namen · gefaltet in die Sammelbox', size=24)

    p = slide('Freiwillige Ergänzungen im Plenum', 'Freiwilliges Kursfeedback', 68, 75,
              'Sieben Minuten für konkrete Ergänzungen anbieten. Beiträge bündeln: Was sollte bleiben, was '
              'sollte sich ändern? Mündliche Beiträge sind nicht anonym. Keine individuellen Leistungen oder '
              'handschriftlichen Freitexte live zeigen. '
              'Überleitung: „Zum Kursende halten wir drei Gedanken fest, die Sie bei späteren Datenprojekten wiederverwenden können.“',
              feedback)
    card(p, 130, 280, 610, 300, 'Beibehalten', 'Welcher Teil half beim Lernen?', size=27)
    card(p, 860, 280, 610, 300, 'Verändern', 'Was würde das Lernen erleichtern?', color=ORANGE, size=27)
    band(p, 'Mündliche Beiträge im Plenum sind nicht anonym.', size=23)

    p = slide('Gute Ergebnisse beginnen mit verstandenen Daten', 'Drei Kernbotschaften · 1', 75, 80,
              'Datentypen, Einheiten, Herkunft und Raumbezug nennen lassen. Als bekannten Fehlerfall '
              'das falsche CRS oder als Text gelesene Zahlen verwenden, nur wenn tatsächlich behandelt. '
              'Eine plausible Darstellung kann fachlich irreführen.', feedback)
    card(p, 150, 290, 1300, 295, 'Erst die Daten verstehen',
         'Datentyp · Einheit · Herkunft · Koordinatenreferenzsystem', size=34)
    band(p, 'Ein falsches CRS kann eine plausible Karte in die Irre führen.', size=23)

    p = slide('Der nachvollziehbare Arbeitsweg gehört zum Ergebnis', 'Drei Kernbotschaften · 2', 80, 85,
              'An Units 11–14 den Weg von Rohrecords über Prüfregel und Zwischenergebnis zur Karte '
              'wiedererkennen lassen. Andere müssen später verstehen können, wie eine Zahl, ein Layer '
              'oder eine Karte entstanden ist.', feedback)
    card(p, 140, 275, 1320, 330, 'Von der Quelle zum Ergebnis',
         '79 Rohrecords → 56 geprüfte Punkte → 35 Höhenpunkte → begründete Karte', size=31)
    band(p, 'Prüfregel und Dokumentation sind Teil des Ergebnisses.', size=24)

    p = slide('Aussagen aus Tabellen, Diagrammen und Karten begründen', 'Drei Kernbotschaften · 3', 85, 90,
              'Darstellung und Datengrundlage bestimmen, was eine Aussage trägt und wo ihre Grenze liegt. '
              'Auf Rückblick und Unit-Materialien verweisen. Keine neue Übungsaufgabe, Abgabe oder Pflicht-JiTT '
              'zu Unit 15 ankündigen. Bestehende Fristen früherer Units bleiben bestehen. '
              'Organisatorisches nur mit bestätigten Angaben beantworten, sonst auf reguläre Kurskanäle verweisen.',
              feedback + '\n' + recap)
    card(p, 150, 275, 1300, 330, 'Aussage + Grenze',
         'Was zeigen diese Daten?\nWas können sie nicht zeigen?', size=34)
    band(p, 'Die Unit-Seiten bleiben zum Nachschlagen verfügbar.', size=24)

    p = slide('Materialien zum Nachschlagen', 'Reserve · außerhalb des Zeitplans', 0, 0,
              'Nur bei vorhandener Zeit oder späterem Bedarf zeigen. Die Rückblicksseite verlinkt alle Units. '
              'Die GIS-Stationen 09–14 sind hier direkt erreichbar.', recap, reserve=True)
    links = [('Unit 15 · Rückblick und Ablauf', recap)] + [
        (f'Unit {u:02d} · Kursübersicht', f'{SITE}unit{u:02d}/unit{u:02d}-00_overview.html')
        for u in range(9, 15)]
    for i, (label, url) in enumerate(links):
        shape = text(p, 160, 235 + i*72, 1250, 55, label, 25, TEAL, True)
        hyperlink(shape, url)

    p = slide('Vielen Dank für Ihre Aufmerksamkeit', 'Abschluss', 90, 90,
              'Die Sitzung mit dieser Folie beenden. Das FB19-Motiv erscheint wie in der Serie nur '
              'auf Titel und Abschluss.', str(TEMPLATE), kind='closing')
    box(p, 44, 44, 809, 807, 0xF7DEED)
    picture(p, FB19_IMAGE, 915, 350, 640, 640*135/394)
    text(p, 100, 380, 700, 250, 'Vielen Dank für Ihre Aufmerksamkeit', 41, INK)
    text(p, 165, 710, 620, 110, 'Geodaten · Unit 15\nFachbereich 19 · Geographie', 18, INK)


def main():
    global DOC, MASTERS
    with tempfile.TemporaryDirectory(prefix='geomoer-unit15-') as profile:
        pipe = 'geomoer_unit15_' + uuid.uuid4().hex
        proc = subprocess.Popen(['libreoffice', '-env:UserInstallation=' + Path(profile).as_uri(),
            '--headless', '--accept=pipe,name=' + pipe + ';urp;StarOffice.ComponentContext',
            '--norestore', '--nodefault', '--nofirststartwizard'], stdout=subprocess.DEVNULL)
        desktop = None
        try:
            local = uno.getComponentContext()
            resolver = local.ServiceManager.createInstanceWithContext('com.sun.star.bridge.UnoUrlResolver', local)
            for _ in range(100):
                try:
                    ctx = resolver.resolve('uno:pipe,name=' + pipe + ';urp;StarOffice.ComponentContext')
                    break
                except Exception:
                    if proc.poll() is not None:
                        raise RuntimeError('LibreOffice could not start')
                    time.sleep(.2)
            else:
                raise RuntimeError('LibreOffice connection timed out')
            desktop = ctx.ServiceManager.createInstanceWithContext('com.sun.star.frame.Desktop', ctx)
            legacy = desktop.loadComponentFromURL(FB19.as_uri(), '_blank', 0, (prop('Hidden', True),))
            legacy_export = Path(profile) / 'fb19.pptx'
            legacy.storeToURL(legacy_export.as_uri(), (prop('FilterName', 'Impress MS PowerPoint 2007 XML'),))
            legacy.close(True)
            (OUT / 'assets').mkdir(exist_ok=True)
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
            DOC.DocumentProperties.Title = 'Unit 15 – Rückblick, offene Fragen und Kursabschluss'
            DOC.DocumentProperties.Subject = 'Geodaten · Unit 15 · Präsenzlehre'
            DOC.DocumentProperties.Author = 'GeoMOER'
            build()
            pptx = OUT / 'unit15_praesenz.pptx'
            DOC.storeAsURL(pptx.as_uri(), (prop('FilterName', 'Impress MS PowerPoint 2007 XML'), prop('Overwrite', True)))
            DOC.close(True)
            DOC = desktop.loadComponentFromURL(pptx.as_uri(), '_blank', 0, (prop('Hidden', True),))
            base.DOC = DOC
            assert DOC.getDrawPages().Count == len(RECORDS)
            pdf = OUT / 'unit15_praesenz.pdf'
            DOC.storeToURL(pdf.as_uri(), (prop('FilterName', 'impress_pdf_Export'), prop('Overwrite', True),
                prop('FilterData', (prop('ExportNotesPages', False), prop('ExportHiddenSlides', True),
                                    prop('UseTaggedPDF', True)))))
            DOC.close(True)
            PUBLISHED_PDF.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(pdf, PUBLISHED_PDF)
            with (OUT / 'moderation.md').open('w') as fp:
                fp.write('# Unit 15 – Moderation\n\n'
                         'Titelfolie, 24 zeitlich geplante Folien für 90 Minuten, eine Reservefolie und eine Abschlussfolie. '
                         'Die acht frühen Unit-Stationen tragen sichtbare Beispiel-Platzhalter. '
                         'Zeitfenster stehen nur in diesen Notizen.\n\n')
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
