#!/usr/bin/python3
"""Build the Unit 14 classroom deck with LibreOffice UNO (no downloads).

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
PUBLISHED_PDF = ROOT/'assets/pdfs/Geodaten_Slides_Unit14.pdf'
COURSE = 'https://geomoer.github.io/moer-bsc-geodaten/unit14/'
QDOC = 'https://docs.qgis.org/3.40/en/docs/user_manual/'
GBIF = 'https://www.gbif.org/dataset/6ac3f774-d9fb-4796-b3e9-92bf6c81c084'
DGM_SOURCE = 'https://hvbg.hessen.de/landesvermessung/geotopographie/3d-daten/digitale-gelaendemodelle'
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
             'Universität Marburg | Fachbereich 19 · Geographie | Geodaten · Unit 14', 10, MUTED)
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
    overview = COURSE+'unit14-00_overview.html'
    symbols = COURSE+'unit14-01_symbolisierung.html'
    classes = COURSE+'unit14-02_klassifizierung.html'
    layout = COURSE+'unit14-03_kartenlayout.html'
    assignment = COURSE+'unit14-04_assignment.html'
    workflow = COURSE+'unit14-05_workflow.html'
    material = 'https://geomoer.github.io/moer-bsc-geodaten/material/marburg.html'
    core = 'https://geomoer.github.io/moer-bsc-geodaten/material/qgis-kernpfade.html#unit14'

    p = slide('Kartengestaltung und Abschlusskarte', 'Unit 14', 0, 0,
        'Titelfolie beim Ankommen zeigen. Die Sitzung ist für 90 Minuten mit 100–150 Bachelor- und Lehramtsstudierenden ausgelegt. '
        'Vorbereitendes Lesen wird nicht vorausgesetzt. QGIS 3.40 und das vollständig entpackte Marburger Übungspaket müssen verfügbar sein. '
        'Alle beginnen mit unit14_start.qgz; eigene Ergebnisse aus Unit 13 sind nur Vertiefung.', str(TEMPLATE), kind='title')
    picture(p, FB19_IMAGE, 44, 350, 539, 539*135/394)
    text(p, 625, 275, 860, 315, 'Kartengestaltung und\nAbschlusskarte', 43, WHITE)
    text(p, 625, 614, 840, 70, 'Unit 14', 28, WHITE)
    text(p, 625, 744, 840, 100, 'Fachbereich 19 · Geographie\nPhilipps-Universität Marburg', 19, WHITE)

    p = slide('JiTT · Rückblick auf Unit 13', 'Platzhalter · vollständig austauschbar', 0, 10,
        'VOR DEM TERMIN: Den gesamten Platzhalter durch die aktuelle JiTT-Auswertung zu Unit 13 ersetzen. '
        'Bei Bedarf die Folie duplizieren. Nur tatsächliche, zusammengefasste und anonymisierte Rückmeldungen einsetzen. '
        'Die gesamte Phase dauert zehn Minuten. Verständnisfragen zu Rasterzellen, NoData, DGM oder hoehe_m klären.')
    shape = box(p, 100, 237, 1400, 545, PALE, GRID)
    shape.Name = 'JiTT – vollständigen Block ersetzen'
    text(p, 180, 430, 1240, 130, '[Hier den vollständigen\nJiTT-Block einfügen]', 38, TEAL, False, 'CENTER')

    p = slide('Von geprüften Höhenpunkten zur lesbaren Karte', 'Unit 14 · Orientierung', 10, 11,
        'Den Ablauf ankündigen: Ausgangsprojekt prüfen, zwei Klassifizierungen vergleichen, eine Variante begründet gestalten, das vorbereitete Layout überarbeiten, beide Formate exportieren und eine Aussagegrenze dokumentieren.', overview)
    picture(p, ROOT/'assets/images/unit14/hero-unit14.jpg', 85, 225, 1430, 1430/6)
    for x, label, body in [(85, 'Vergleichen', 'gleiche Intervalle\nund Quantile'),
                           (570, 'Gestalten', 'Hauptinformation, Titel\nund Legende'),
                           (1055, 'Prüfen', 'PDF + PNG öffnen\nGrenzen dokumentieren')]:
        card(p, x, 495, 460, 205, label, body, size=22)
    band(p, 'Leitfrage: Wo liegen die dokumentierten Nachweise – und welchen Höhenklassen sind sie zugeordnet?', size=20)

    p = slide('Startprojekt sofort als Arbeitskopie speichern', 'Einstieg · Verbindlicher Start', 11, 14,
        'Alle öffnen unit14_start.qgz im vollständig entpackten Paket und speichern sofort als unit14_abschluss.qgz. '
        'Nicht mit einem leeren Projekt beginnen und keine Analysen aus Units 11 bis 13 wiederholen. Bei technischen Problemen unit14_beispiel.qgz verwenden.', overview+'\n'+core)
    steps(p, [('Start öffnen', 'unit14_start.qgz im Paket-Hauptordner.'),
              ('Arbeitskopie', 'Speichern unter: unit14_abschluss.qgz.'),
              ('Fallback', 'Bei Ausfall mit unit14_beispiel.qgz weiterarbeiten.')], y=245, gap=170)
    band(p, 'Spätestens jetzt speichern – das Startprojekt bleibt unverändert.', size=23)

    p = slide('Kartenfrage und Zielgruppe zuerst festlegen', 'Einstieg · Aussage', 14, 16,
        'Die Beispielkarte richtet sich an fachlich interessierte Personen ohne Detailkenntnis des Datensatzes. '
        'Titel, Legende und Symbolisierung müssen genau diese vorsichtige Frage beantworten. Zwei Minuten kurze Nachbarschaftsabsprache.', overview+'\n'+layout)
    box(p, 115, 245, 1370, 245, PALE, GRID)
    text(p, 170, 300, 1260, 120,
         'Wo liegen die dokumentierten Feuersalamander-Nachweise\nund welchen Höhenklassen sind sie zugeordnet?', 34, INK, True, 'CENTER')
    card(p, 180, 545, 560, 155, 'Zielgruppe', 'fachlich interessiert\nohne Datensatzkenntnis', size=22)
    card(p, 860, 545, 560, 155, 'Nicht behaupten', 'vollständige Verbreitung\noder Höhenpräferenz', color=ORANGE, size=22)

    p = slide('Der Karteneingang umfasst 35 gültige Höhenwerte', 'Einstieg · Datenprüfung', 16, 18,
        'Den vorbereiteten Punktlayer prüfen: 35 Features, numerisches Feld hoehe_m, EPSG:25832. '
        'Die 21 weiteren qualitätsgeprüften Nachweise ohne DGM-Höhe sind nicht in dieser Höhenklassenkarte dargestellt. Diese Einschränkung muss sichtbar dokumentiert werden.', overview+'\n'+core)
    card(p, 120, 270, 590, 300, '35', 'Nachweise mit gültigem\nhoehe_m', size=29)
    card(p, 890, 270, 590, 300, '21', 'weitere geprüfte Nachweise\nohne DGM-Höhe', color=ORANGE, size=27)
    band(p, 'Kartenaussage: 35 Höhenpunkte – nicht alle 56 geprüften Nachweise.', size=24)

    p = slide('Klassengrenzen verändern die sichtbare Aussage', 'Klassifizieren · Grundidee', 18, 20,
        'Klassifizierung fasst einzelne Zahlenwerte zu wenigen Gruppen zusammen. Dadurch wird die Karte übersichtlicher, aber Information geht verloren. '
        'Ein Punktwert bleibt gleich; nur seine Zuordnung zu einer visuellen Klasse kann sich ändern.', classes)
    card(p, 120, 275, 590, 310, 'Eingabe', '35 einzelne Höhenwerte\n178,55 bis 323,90 m', size=25)
    card(p, 890, 275, 590, 310, 'Darstellung', 'fünf Klassen\nmit geordneten Farben', color=ORANGE, size=25)
    band(p, 'Klassengrenzen sind eine begründungspflichtige Entscheidung.', size=25)

    p = slide('Gleiche Intervalle: gleiche Breite', 'Klassifizieren · Methode 1', 20, 22,
        'Bei gleichen Intervallen ist der gesamte Wertebereich in fünf gleich breite Abschnitte geteilt. '
        'Die Methode ist leicht erklärbar; bei ungleich verteilen Werten können die Klassen aber sehr unterschiedlich besetzt sein.', classes)
    card(p, 120, 265, 610, 330, 'Prinzip', 'gleich breite Wertebereiche\nleichte Vergleichbarkeit', size=26)
    card(p, 870, 265, 610, 330, 'Risiko', 'ungleich viele Punkte\nleere Klassen möglich', color=ORANGE, size=26)
    band(p, 'Hier: fünf Klassen von 178,5 bis 323,9 m.', size=25)

    p = slide('Quantile: ungefähr gleich viele Punkte', 'Klassifizieren · Methode 2', 22, 24,
        'Quantile teilen die sortierten Werte so, dass jede Klasse ungefähr gleich viele Features enthält. '
        'Dadurch erscheinen meist alle Farben, aber die Wertebereiche sind unterschiedlich breit und ähnliche Werte können getrennt werden.', classes)
    card(p, 120, 265, 610, 330, 'Prinzip', 'ähnliche Zahl von Punkten\nje Klasse', size=26)
    card(p, 870, 265, 610, 330, 'Risiko', 'unterschiedliche Klassenbreiten\nrelative statt absolute Lage', color=ORANGE, size=24)
    band(p, 'Hier: fünf Klassen mit ungefähr sieben Punkten.', size=25)

    p = slide('Dieselben 35 Punkte – zwei sichtbare Muster', 'Klassifizieren · Kartenvergleich', 24, 27,
        'Beide Karten zeigen dieselben 35 Punkte, denselben Ausschnitt, dieselbe Symbolgröße und dieselbe Farbpalette. '
        'Links gleiche Intervalle, rechts Quantile. Erst still vergleichen, dann Unterschiede zu zweit benennen. Die 21 Punkte ohne Höhe fehlen in beiden Darstellungen.', classes)
    picture(p, ROOT/'assets/data/marburg/klassifizierung_intervalle.png', 90, 220, 650, 650*1240/1753)
    picture(p, ROOT/'assets/data/marburg/klassifizierung_quantile.png', 860, 220, 650, 650*1240/1753)
    text(p, 90, 692, 650, 44, 'Gleiche Intervalle · fünf Klassen', 20, TEAL, True, 'CENTER')
    text(p, 860, 692, 650, 44, 'Quantile · fünf Klassen', 20, TEAL, True, 'CENTER')
    band(p, 'Was ändert sich sichtbar – obwohl kein Höhenwert verändert wurde?', y=750, size=22)

    p = slide('Rechenprinzip und Klassenbesetzung', 'Klassifizieren · Schematisches Beispiel', 27, 29,
        'Die Grafik erklärt das Rechenprinzip mit zehn erfundenen Höhenwerten, nicht mit den 35 Marburger Nachweisen. '
        'Links entstehen bei gleichen Intervallen die Besetzungen 8/1/0/0/1; rechts enthalten die interpolierten Quantile je zwei Werte. Softwarekonventionen können bei kleinen Datensätzen abweichen.', classes)
    picture(p, ROOT/'assets/images/unit14/klassengrenzen-zahlen.svg', 145, 215, 280, 280*1134/640)
    card(p, 560, 280, 410, 250, 'Intervalle', 'gleiche Breite\n8 · 1 · 0 · 0 · 1', size=23)
    card(p, 1050, 280, 410, 250, 'Quantile', 'gleiche Anzahl\n2 · 2 · 2 · 2 · 2', color=ORANGE, size=23)
    band(p, 'Schematische Werte erklären die Methode – die realen Karten werden separat geprüft.', size=20)

    p = slide('Die realen Klassengrenzen vergleichen', 'Klassifizieren · Prüfwerte', 29, 30,
        'Grenzen aus den beiden vorbereiteten Legenden ablesen. Die Quantilgrenzen liegen bei etwa 214,3, 230,0, 245,0 und 267,7 m. '
        'Bei gleichen Intervallen liegen die inneren Grenzen ungefähr bei 207,6, 236,7, 265,8 und 294,8 m. Werte bleiben unverändert; nur Klassen ändern sich.', classes)
    table(p, ['Methode', 'Klassen in Metern'], [
        ['gleiche Intervalle', '178,5 · 207,6 · 236,7 · 265,8 · 294,8 · 323,9'],
        ['Quantile', '178,5 · 214,3 · 230,0 · 245,0 · 267,7 · 323,9']],
        [430, 1000], y=285, row_h=135, size=23)
    band(p, 'Entscheidung: Welche Methode unterstützt die Kartenfrage verständlicher?', size=23)

    p = slide('Abgestufte Darstellung in QGIS einstellen', 'Umsetzen · Symbolisierung', 30, 33,
        'Layereigenschaften → Symbolisierung öffnen. Abgestuft wählen, hoehe_m als Wert, eine sequentielle Palette und genau fünf Klassen einstellen. '
        'Erst danach die gewählte Methode anwenden. Keine neue Datenquelle und keine zusätzliche Analyse starten.', symbols+'\n'+classes+'\n'+QDOC)
    table(p, ['Parameter', 'Verbindliche Einstellung'], [
        ['Darstellung', 'Abgestuft / Graduated'],
        ['Wert', 'hoehe_m · Meter'],
        ['Klassen', '5'],
        ['Palette', 'sequentiell'],
        ['Methode', 'begründet: gleiche Intervalle oder Quantile']],
        [430, 1000], y=225, row_h=80, size=22)
    band(p, 'Kontrolle vor Anwenden: 35 gültige Features, keine NULL-Werte im Startlayer.', size=21)

    p = slide('Eine Methode auswählen und begründen', 'Umsetzen · Entscheidung', 33, 36,
        'Zwei Minuten zu zweit entscheiden, danach die gewählte Methode anwenden. Die Begründung muss sich auf Frage, Zielgruppe und sichtbare Wirkung beziehen. '
        '„Sieht schöner aus“ reicht nicht. Es gibt nicht für jeden Datensatz genau eine einzig richtige Methode.', classes)
    box(p, 125, 245, 1350, 230, PALE, GRID)
    text(p, 185, 300, 1230, 120,
         'Wir wählen ____________, weil diese Methode\nfür unsere Kartenfrage ________________________________.', 32, INK, True, 'CENTER')
    card(p, 225, 535, 1150, 160, 'Prüfen', 'Klassengrenzen · Besetzung · Legendentext · sichtbare Wirkung', size=24)

    p = slide('Klassen eindeutig und lesbar beschriften', 'Umsetzen · Legende vorbereiten', 36, 38,
        'Die QGIS-Grenzen nicht unbesehen übernehmen. Legendenwerte sinnvoll runden, Einheit ergänzen und Überschneidungen vermeiden. '
        'Die tatsächlichen Grenzen bleiben korrekt, auch wenn die sichtbaren Beschriftungen lesefreundlich formuliert werden.', classes)
    table(p, ['Technischer Ausgang', 'Redaktionell verständlich'], [
        ['178.5 - 207.6', '178,5 bis 207,6 m'],
        ['hoehe_m', 'Geländehöhe am Nachweisort [m]'],
        ['gbif_mit_hoehe_final', 'Dokumentierte Nachweise']],
        [680, 750], y=275, row_h=100, size=23)
    band(p, 'Einheit und Grenzlogik müssen aus der Legende hervorgehen.', size=24)

    p = slide('Für Höhenwerte eine sequentielle Palette wählen', 'Umsetzen · Farbe', 38, 40,
        'Die Palette muss zur fachlichen Bedeutung passen. Qualitative Farben zeigen gleichrangige Kategorien, sequentielle Farben eine geordnete Zahl und divergierende Farben Abweichungen um einen Bezugspunkt. '
        'Für Geländehöhe verwenden wir heute eine sequentielle Palette.', symbols)
    picture(p, ROOT/'assets/images/unit14/farbpaletten.svg', 120, 230, 1360, 1360*370/1000)
    band(p, 'Höhenklassen: niedrig → hoch als erkennbare Helligkeitsfolge.', y=755, size=23)

    p = slide('Symbolwahl folgt der Datenart', 'Umsetzen · Visuelle Variablen', 40, 42,
        'Die Grafik zeigt dieselben drei Positionen. Formen beantworten die kategoriale Typfrage; geordnete Helligkeit beantwortet die numerische Höhenfrage. '
        'Die Beispieldaten sind erfunden. Heute ist hoehe_m die Hauptinformation.', symbols)
    picture(p, ROOT/'assets/images/unit14/symbol-und-datenart.svg', 165, 220, 425, 425*799/640)
    card(p, 720, 285, 690, 175, 'Kategorie', 'Farbton oder Form\nohne Rangfolge', size=24)
    card(p, 720, 520, 690, 175, 'Höhe', 'geordnete Helligkeit\nniedrig → hoch', color=ORANGE, size=24)

    p = slide('Die Hauptinformation muss zuerst auffallen', 'Umsetzen · Visuelle Hierarchie', 42, 44,
        'Beide schematischen Karten zeigen identische Positionen, Fluss und Höhenlinien. Links dominiert der Hintergrund, rechts die Punktinformation. '
        'Im Startprojekt höchstens den vorbereiteten Hintergrund verwenden; zusätzliche Layer sind Vertiefung. Spätestens nach dieser Folie zum Layout wechseln.', symbols)
    picture(p, ROOT/'assets/images/unit14/visuelle-hierarchie.svg', 260, 220, 1080, 1080*480/1000)
    band(p, 'Punkte zuerst · Kontext zurückhaltend · unnötige Layer ausblenden', y=755, size=23)

    p = slide('Vor dem Layout die Kartenansicht prüfen', 'Umsetzen · Zwischenkontrolle', 44, 45,
        'Gemeinsam kurz prüfen: gewählte Methode, fünf Klassen, hoehe_m, sequentielle Palette, lesbare Klassenbezeichnungen und zurückhaltender Hintergrund. '
        'Auch wenn einzelne Personen noch optimieren möchten, jetzt zum vorbereiteten Layout wechseln.', core)
    table(p, ['Prüffrage', 'Sollzustand'], [
        ['Punktlayer', '35 Nachweise · hoehe_m'],
        ['Klassifizierung', 'begründete Methode · 5 Klassen'],
        ['Farbe', 'sequentiell · Reihenfolge sichtbar'],
        ['Hierarchie', 'Punkte dominieren den Kontext']], [520, 910], y=250, row_h=90, size=23)
    band(p, 'Zeitmarke Minute 45: Layout ab jetzt verbindlich.', size=24)

    p = slide('Das vorbereitete Layout gezielt ausarbeiten', 'Layout · Einstieg', 45, 46,
        'Im Projekt das vorhandene A4-Querformatlayout abschlusskarte_unit14 öffnen. Kein neues Layout anlegen. '
        'Aktiv geändert werden Titel und Legende; Kartenausschnitt, Maßstab und Quellen werden kontrolliert und nur bei einem konkreten Fehler korrigiert.', layout+'\n'+core)
    steps(p, [('Layout öffnen', 'abschlusskarte_unit14 · A4 quer.'),
              ('Aktiv ändern', 'Titel und Legende fachlich überarbeiten.'),
              ('Kontrollieren', 'Ausschnitt, Maßstab und Quellen prüfen.')], y=245, gap=170)
    band(p, 'Keine zusätzlichen Layerelemente – Zeit für Export und Partnercheck sichern.', size=22)

    p = slide('Die Beispielkarte ist eine Prüfreferenz', 'Layout · Gesamtansicht', 46, 49,
        'Die Beispielkarte gemeinsam lesen: Was fällt zuerst auf, welche Information liefert die Legende, wo stehen Datenumfang und Quellen? '
        'Sie ist bei technischen Problemen eine Arbeitsgrundlage, aber kein Grund, Entscheidungen ungeprüft zu kopieren.', layout)
    picture(p, ROOT/'assets/data/marburg/abschlusskarte_beispiel.png', 65, 210, 820, 820*1240/1753)
    card(p, 950, 285, 550, 150, 'Hauptthema', '35 dokumentierte Nachweise\nnach Geländehöhe', size=21)
    card(p, 950, 500, 550, 150, 'Pflichtangaben', 'Titel · Legende · Maßstab\nQuellen · Einschränkung', color=ORANGE, size=21)

    p = slide('Der Titel benennt den tatsächlichen Inhalt', 'Layout · Titel', 49, 51,
        'Titel in der Vorlage aktiv überarbeiten. Die Formulierung muss dokumentierte Nachweise statt vollständiger Verbreitung benennen und den Raumbezug verständlich machen.', layout)
    card(p, 120, 275, 610, 300, 'Zu allgemein', 'Karte Unit 14\nVerbreitung der Art', color=ORANGE, size=25)
    card(p, 870, 275, 610, 300, 'Passend', 'Feuersalamander-Nachweise\nbei Marburg', size=25)
    band(p, 'Der Titel darf nicht mehr versprechen, als die Daten zeigen.', size=24)

    p = slide('Die Legende erklärt Klassen statt Dateinamen', 'Layout · Legende', 51, 54,
        'Legendentitel und Klassentexte fachlich überarbeiten. Technische Layernamen und nicht sichtbare oder nicht benötigte Einträge entfernen. '
        'Höhenbezug verständlich als Geländehöhe am Nachweisort in Metern benennen.', layout)
    table(p, ['Prüfen', 'Erwartung'], [
        ['Legendentitel', 'Geländehöhe am Nachweisort [m]'],
        ['Klassen', 'fünf eindeutige, gerundete Bereiche'],
        ['Layernamen', 'fachlich verständlich'],
        ['Inhalt', 'nur tatsächlich benötigte Einträge']], [470, 960], y=255, row_h=90, size=23)
    band(p, 'Automatisch erzeugte Legenden sind ein Ausgangspunkt, kein fertiger Text.', size=22)

    p = slide('Kartenausschnitt und Maßstab funktional prüfen', 'Layout · Raumbezug', 54, 56,
        'Alle relevanten Punkte müssen sichtbar sein, leere Flächen sollen die Karte nicht unnötig verkleinern. Maßstabseinheit und Teilung müssen zur Ausdehnung passen. '
        'Nur bei einem erkennbaren Fehler verändern; heute wird kein neuer Ausschnitt gestaltet.', layout)
    card(p, 120, 275, 610, 300, 'Kartenausschnitt', 'alle 35 Punkte sichtbar\nausreichend räumlicher Kontext', size=24)
    card(p, 870, 275, 610, 300, 'Maßstab', 'geeignete Einheit\nlesbare Teilung', color=ORANGE, size=24)
    band(p, 'Nordpfeil, Gitter und Übersichtskarte sind keine automatischen Pflichtelemente.', size=21)

    p = slide('Quellen und Bearbeitung gehören in die Karte', 'Layout · Dokumentation', 56, 59,
        'Die vorbereiteten Quellenangaben kontrollieren: NABU|naturgucker via GBIF, DGM1 des Hessen Geodatenmanagements, Bearbeitung und Datenabruf. '
        'Keinen neuen DOI erfinden. Zusätzlich 35 gültige Höhenpunkte und die 21 nicht dargestellten Nachweise transparent benennen.', layout+'\n'+GBIF+'\n'+DGM_SOURCE)
    table(p, ['Angabe', 'Kontrollpunkt'], [
        ['Beobachtungen', 'NABU|naturgucker via GBIF · CC BY 4.0'],
        ['Geländehöhe', 'Hessen Geodatenmanagement · DGM1'],
        ['Bearbeitung', '10-m-Mittelwerte · DHHN2016_NH'],
        ['Umfang', '35 dargestellt · 21 ohne gültige DGM-Höhe']], [430, 1000], y=255, row_h=90, size=21)
    band(p, 'Quelle, Datenstand und Bearbeitung sind Teil der fachlichen Aussage.', size=22)

    p = slide('Layout in tatsächlicher Ausgabegröße prüfen', 'Layout · Schlusskontrolle', 59, 62,
        'Vor dem Export die Seite als Ganzes prüfen. Titel, fünf Klassen, Einheiten und Quellen müssen ohne starkes Zoomen lesbar sein. '
        'Hintergrund und Nebenelemente dürfen nicht mit den Punkten konkurrieren. Spätestens jetzt zum Export wechseln.', layout)
    table(p, ['Kontrollfrage', 'Ja / Korrektur'], [
        ['Ist die Kernaussage ohne Erklärung erkennbar?', ''],
        ['Sind alle fünf Klassen unterscheidbar?', ''],
        ['Sind Titel, Legende, Einheit und Quellen lesbar?', ''],
        ['Bleiben Hintergrund und Rahmen zurückhaltend?', '']], [1150, 280], y=245, row_h=90, size=22)
    band(p, 'Zeitmarke Minute 62: jetzt exportieren.', size=25)

    p = slide('Zwei Formate mit verbindlichen Dateinamen exportieren', 'Export · Produkte', 62, 65,
        'Im Layout zuerst PDF exportieren, danach als Bild PNG wählen und 150 dpi einstellen. Beide Dateien gehören in figures. '
        'Vorhandene Beispielausgaben nicht versehentlich überschreiben; die eigenen Ausgaben tragen die verbindlichen Namen.', layout+'\n'+core)
    card(p, 115, 275, 650, 310, 'PDF', 'figures/\nabschlusskarte_unit14.pdf', size=25)
    card(p, 835, 275, 650, 310, 'PNG · 150 dpi', 'figures/\nabschlusskarte_unit14.png', color=ORANGE, size=25)
    band(p, 'Ein erfolgreicher Export ist noch keine bestandene Sichtprüfung.', size=24)

    p = slide('PDF und PNG außerhalb von QGIS öffnen', 'Export · Sichtprüfung', 65, 68,
        'Beide Dateien mit einem unabhängigen Anzeigeprogramm öffnen und in der vorgesehenen Größe prüfen. '
        'Auf abgeschnittene Elemente, Ersatzschriften, unlesbare Klassen, unerwartete Rasterflächen und unvollständige Quellen achten.', layout)
    steps(p, [('PDF öffnen', 'Seite vollständig · Texte und Linien scharf.'),
              ('PNG öffnen', '150 dpi · keine abgeschnittenen Elemente.'),
              ('Vergleichen', 'Titel, Legende, Farben und Quellen stimmen überein.')], y=245, gap=170)
    band(p, 'Nur sichtbare und lesbare Ausgaben gelten als Ergebnis.', size=24)

    p = slide('Vier Produkte vor dem Partnercheck sichern', 'Export · Ergebnissicherung', 68, 70,
        'Arbeitsprojekt speichern und prüfen, ob beide Exporte und das vorbereitete Protokoll am erwarteten Ort vorhanden sind. '
        'Die Dokumentation wird erst nach dem Partnercheck vervollständigt.', overview)
    table(p, ['Produkt', 'Status'], [
        ['unit14_abschluss.qgz', 'gespeichert'],
        ['figures/abschlusskarte_unit14.pdf', 'geöffnet und geprüft'],
        ['figures/abschlusskarte_unit14.png', '150 dpi · geöffnet und geprüft'],
        ['documentation/processing_notes.md', 'vorhanden · Ergänzung folgt']], [1050, 380], y=245, row_h=90, size=22)
    band(p, 'Fehlt ein Produkt, zuerst den Pfad prüfen – keine neue Analyse beginnen.', size=22)

    p = slide('Partnercheck: Karte ohne Zusatzwissen lesen', 'Partnerarbeit · Durchführung', 70, 73,
        'Zu zweit die exportierten Karten tauschen. Drei Minuten: Die betrachtende Person beschreibt zuerst ohne Erklärung die sichtbare Kernaussage. '
        'Bei technischen Problemen die bereitgestellte Beispielkarte verwenden.', overview)
    box(p, 130, 245, 1340, 245, PALE, GRID)
    text(p, 190, 300, 1220, 125,
         'Welche Aussage lesen Sie aus Titel, Karte und Legende –\nohne dass die erstellende Person etwas erklärt?', 32, INK, True, 'CENTER')
    band(p, 'Erst lesen und beschreiben – danach Rückmeldung geben.', y=585, size=25)

    p = slide('Eine konkrete Verbesserung priorisieren', 'Partnerarbeit · Kriterien', 73, 76,
        'Zwei Minuten Rückmeldung: Nur die wichtigste fachliche oder gestalterische Verbesserung auswählen. '
        'Priorität haben missverständliche Aussagen, unklare Klassen oder fehlende Quellen, nicht persönliche Geschmacksfragen.', overview)
    table(p, ['Prüfbereich', 'Leitfrage'], [
        ['Aussage', 'Beschreibt die Karte Nachweise statt Verbreitung?'],
        ['Klassen', 'Sind Methode, Reihenfolge und Einheit verständlich?'],
        ['Layout', 'Sind Titel, Legende, Maßstab und Quellen lesbar?'],
        ['Hierarchie', 'Fällt die Hauptinformation zuerst auf?']], [430, 1000], y=245, row_h=90, size=21)
    band(p, 'Rückmeldung: konkret, begründet und innerhalb von vier Minuten umsetzbar.', size=21)

    p = slide('Korrektur übernehmen und betroffenen Export erneuern', 'Partnerarbeit · Revision', 76, 80,
        'Die wichtigste Korrektur direkt in Projekt oder Layout übernehmen. Betrifft sie Karteninhalt, Klassen oder gemeinsame Texte, beide Formate erneut exportieren und öffnen. '
        'Betrifft sie ausschließlich ein formatbezogenes Exportproblem, nur den betroffenen Export erneuern. Projekt danach speichern.', overview+'\n'+core)
    steps(p, [('Korrektur', 'eine begründete Verbesserung umsetzen.'),
              ('Neu exportieren', 'betroffene Ausgabe – bei Karteninhalt beide.'),
              ('Nochmals öffnen', 'Änderung und Lesbarkeit sichtbar kontrollieren.')], y=245, gap=170)
    band(p, 'Die letzte geprüfte Fassung ist die verbindliche Abgabeversion.', size=22)

    p = slide('Entscheidungen im vorhandenen Protokoll festhalten', 'Dokumentation · processing_notes.md', 80, 83,
        'Nur den vorhandenen Abschnitt Unit 14: Abschlusskarte ergänzen. '
        'Gewählte Methode, fünf Klassengrenzen, Palette, Datenquellen, 35/21-Einschränkung, Partnerkorrektur und Exportpfade dokumentieren. Keine vollständige Workflowdokumentation neu schreiben.', workflow)
    table(p, ['Dokumentieren', 'Heute festhalten'], [
        ['Klassifizierung', 'Methode · 5 Grenzen · Begründung'],
        ['Daten und Quellen', '35 Höhenpunkte · 21 ohne Höhe · Herkunft'],
        ['Gestaltung', 'Palette · Titel/Legende · Korrektur'],
        ['Ausgabe', 'Projekt · PDF · PNG mit 150 dpi']], [450, 980], y=250, row_h=90, size=21)
    band(p, 'Dokumentation macht die sichtbaren Entscheidungen nachvollziehbar.', size=23)

    p = slide('Beobachtungen beschreiben – keine Verbreitung behaupten', 'Dokumentation · Aussagegrenze', 83, 85,
        'Gemeinsam eine belastbare und eine unzulässige Formulierung unterscheiden. '
        'Die Karte zeigt räumlich und zeitlich ungleich erhobene Nachweise; sie belegt weder vollständige Verbreitung noch eine ursächliche Höhenpräferenz. Außerdem fehlen 21 Nachweise ohne gültige DGM-Höhe.', workflow)
    card(p, 115, 265, 660, 330, 'Tragfähig', '„Die dargestellten dokumentierten\nNachweise liegen in … Höhenklassen.“', size=22)
    card(p, 825, 265, 660, 330, 'Nicht gedeckt', '„Die Art verbreitet sich bevorzugt\nin diesen Höhenlagen.“', color=ORANGE, size=22)
    band(p, 'Grenzen: Beobachtungsintensität · Koordinaten · DGM · Klassifizierung · fehlende Höhen', size=20)

    p = slide('Exit Ticket · eine Frage auswählen', 'Sicherung · Einzelarbeit', 85, 88,
        'Eine der drei Fragen passend zum tatsächlichen Sitzungsverlauf auswählen. Zwei Minuten einzeln notieren, danach per Handzeichen oder mit zwei bis drei kurzen Antworten auflösen. '
        'Nicht alle drei Fragen bearbeiten lassen.', overview)
    table(p, ['Option', 'Frage'], [
        ['A', 'Wie beeinflusst die Klassifizierung die sichtbare Aussage?'],
        ['B', 'Welche drei Kartenelemente benötigen fast immer redaktionelle Überarbeitung?'],
        ['C', 'Welche Aussage darf aus den dokumentierten Nachweisen nicht abgeleitet werden?']],
        [180, 1250], y=235, row_h=110, size=22)
    band(p, 'Heute ausgewählt: [ A / B / C ]', size=24)

    p = slide('Nachbereitung · JiTT zu Unit 14', 'Ausblick', 88, 90,
        'Die einzige Übungsaufgabe ankündigen: JiTT-Fragen zu Unit 14 im ILIAS-Kurs. Fragen und Frist ausschließlich aus ILIAS nennen; der Link auf der Kursseite ist noch ein sichtbarer Platzhalter. '
        'Nicht abgeschlossene Layoutvarianten werden nicht als zusätzliche Übungsaufgabe aufgegeben. Unit 15 beginnt mit der JiTT-Auswertung und schließt den Kurs ab.', assignment)
    card(p, 130, 260, 620, 300, 'Einzige Übungsaufgabe', 'JiTT-Fragen zu Unit 14\nim ILIAS-Kurs beantworten', size=25)
    card(p, 850, 260, 620, 300, 'Nächste Unit', 'Rückblick · offene Fragen\nFeedback · Abschluss', color=ORANGE, size=25)
    band(p, 'Fragen, Frist und Link: ausschließlich die aktuellen Angaben in ILIAS verwenden.', size=21)

    p = slide('Vertiefung: den vollständigen Workflow rekonstruieren', 'Reserve · Nachschlagen', 0, 0,
        'Nur bei Bedarf zeigen. Der verbindliche Präsenzweg beginnt mit dem vorbereiteten Projekt. '
        'Die Rekonstruktion von Datenprüfung, Auswahl, Rasterabtastung und neuem Layout ist freiwillige Vertiefung und darf nicht den Export- und Partnercheck verdrängen.', workflow, reserve=True)
    picture(p, ROOT/'assets/images/unit14/karten-workflow.svg', 250, 220, 1100, 1100*470/1000)
    band(p, 'Präsenzkern: vorbereitete Daten gestalten, exportieren, prüfen und dokumentieren.', y=755, size=21)

    p = slide('Quellen und Arbeitsstand', 'Reserve · Nachschlagen', 0, 0,
        'Nur bei Bedarf zeigen. Die Folie dokumentiert Kursseiten, QGIS-Dokumentation und Datenquellen. '
        'Die Live-Erreichbarkeit externer Seiten ist für den Präsenzkern nicht erforderlich.', overview, reserve=True)
    links = [('Unit 14 · Kursübersicht', overview),
             ('Daten sinnvoll symbolisieren', symbols),
             ('Werte klassifizieren', classes),
             ('Eine Karte erstellen', layout),
             ('Vom Datensatz zur räumlichen Aussage', workflow),
             ('QGIS 3.40 · Benutzerhandbuch', QDOC),
             ('Marburger Übungspaket', material),
             ('NABU|naturgucker bei GBIF', GBIF),
             ('Hessen Geodatenmanagement · DGM', DGM_SOURCE)]
    for i, (label, url) in enumerate(links):
        shape = text(p, 110, 215+i*50, 1380, 44, label, 20, TEAL, True)
        hyperlink(shape, url)
    text(p, 110, 690, 1390, 116,
         'Paketstand: 08.09.2026 · Abgleich der Folien: 10.09.2026\n'
         'Layout: Universität-Marburg-Vorlage · Titel-/Abschlussbild: FB19-Vorlage\n'
         'Lehrabbildungen: fünf SVGs und drei vorhandene Kartenexporte der Unit 14', 16, MUTED)

    p = slide('Vielen Dank für Ihre Aufmerksamkeit', 'Abschluss', 90, 90,
        'Die Sitzung mit dieser Folie beenden. Die Abschlussgestaltung nutzt den Kontakt-Master der universitären Vorlage sowie das originale Foto-/Kartenmotiv aus der FB19-Titelseite.', str(TEMPLATE), kind='closing')
    box(p, 44, 44, 809, 807, 0xF7DEED)
    picture(p, FB19_IMAGE, 915, 350, 640, 640*135/394)
    text(p, 100, 380, 700, 250, 'Vielen Dank für Ihre Aufmerksamkeit', 41, INK)
    text(p, 165, 710, 620, 110, 'Geodaten · Unit 14\nFachbereich 19 · Geographie', 18, INK)


def main():
    global DOC, MASTERS
    with tempfile.TemporaryDirectory(prefix='geomoer-unit14-') as profile:
        pipe = 'geomoer_unit14_' + uuid.uuid4().hex
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
            DOC.DocumentProperties.Title = 'Unit 14 – Kartengestaltung und Abschlusskarte'
            DOC.DocumentProperties.Subject = 'Geodaten · Unit 14 · Präsenzlehre'
            DOC.DocumentProperties.Author = 'GeoMOER'
            build()
            pptx = OUT/'unit14_praesenz.pptx'
            DOC.storeAsURL(pptx.as_uri(), (prop('FilterName', 'Impress MS PowerPoint 2007 XML'), prop('Overwrite', True)))
            DOC.close(True)
            DOC = desktop.loadComponentFromURL(pptx.as_uri(), '_blank', 0, (prop('Hidden', True),))
            base.DOC = DOC
            assert DOC.getDrawPages().Count == len(RECORDS)
            pdf = OUT/'unit14_praesenz.pdf'
            DOC.storeToURL(pdf.as_uri(), (prop('FilterName', 'impress_pdf_Export'), prop('Overwrite', True),
                prop('FilterData', (prop('ExportNotesPages', False), prop('ExportHiddenSlides', True), prop('UseTaggedPDF', True)))))
            DOC.close(True)
            PUBLISHED_PDF.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(pdf, PUBLISHED_PDF)
            with (OUT/'moderation.md').open('w') as fp:
                fp.write('# Unit 14 – Moderation\n\nTitelfolie, 35 Hauptfolien für 90 Minuten, zwei Reserve-/Quellenfolien und eine Abschlussfolie. Zeitangaben stehen nur in diesen Notizen.\n\n')
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
