# WP12: zusätzliche Lehrabbildungen für Units 09–14

## Sichtung und Auswahl

Stand: 09.09.2026. Ausgangspunkt: `bce45a4`. Die 31 Unit-Seiten wurden anhand der Kernziele, Erklärungen, Praxiswege und bereits eingebundenen Lehrbilder gesichtet. Header zählen nicht als Lehrbilder. Vorhanden sind in Unit 09/10/11/12/13/14 jeweils 4/4/3/2/3/6 unterschiedliche Lehrbilder; das Raster-Abtastschema wird zweimal verwendet.

Die wichtigsten zusätzlichen Lücken betreffen Operationen und ihre sichtbaren Folgen. Die neuen Bilder stehen unmittelbar beim erklärten Begriff. Sie ergänzen die vorhandenen Texte, ohne weitere verpflichtende Übungen einzuführen. Schemawerte sind ausdrücklich keine Marburger Messdaten.

## To-do-Liste und Bildbriefings

Alle Seiten liegen unter `docs/units/_unitXX/`, die SVGs unter `docs/assets/images/unitXX/`. P1 bezeichnet den größten zusätzlichen Lernnutzen innerhalb dieses Bildauftrags; P2 unterstützt die Vertiefung.

| Status | ID / Priorität | Einbauort: Datei → Abschnitt | Abbildung | Didaktische Funktion und konkreter Inhalt |
|---|---|---|---|---|
| [x] | B09a · P1 | `unit09-02_koordinaten.md` → Welche Koordinate steht zuerst? | [achsenreihenfolge.svg](../../docs/assets/images/unit09/achsenreihenfolge.svg) | Gleiche Zahlen an zwei verschiedenen Orten: korrektes und vertauschtes Marburger lon/lat-Paar auf demselben beschrifteten Gradgitter; Zuordnung x/Länge und y/Breite. Formale Wertebereiche allein erkennen den Fehler nicht. |
| [x] | B09b · P1 | `unit09-03_projektionen.md` → CRS zuweisen oder Daten transformieren? | [zuweisen-transformieren.svg](../../docs/assets/images/unit09/zuweisen-transformieren.svg) | Zahlen und CRS-Angabe getrennt verfolgen: fehlendes, aber aus Metadaten bekanntes WGS-84-CRS zuweisen; anschließend nach EPSG:25832 umrechnen. Falsches Umetikettieren von Grad als Meter als Fehler zeigen. |
| [x] | B10a · P1 | `unit10-02_qgigs.md` → Layer organisieren | [layerreihenfolge.svg](../../docs/assets/images/unit10/layerreihenfolge.svg) | Dieselben Punkte und dieselbe deckende Fläche bei vertauschter Reihenfolge. Sichtbarkeit ändert sich, Daten bleiben vorhanden. Layerliste direkt mit Kartenansicht verbinden. |
| [x] | B10b · P1 | `unit10-03_datenquellen.md` → WFS: Vektorobjekte als Dienst | [wms-wfs.svg](../../docs/assets/images/unit10/wms-wfs.svg) | Gleiches Gebiet als gerendertes WMS-Bild und als WFS-Features mit Geometrie/Attributzeile. Sichtbares Objekt versus analysierbares Objekt; mögliche WMS-Objektinformation nicht ausschließen. Verweis aus Unit 12. |
| [x] | B11a · P1 | `unit11-01_punktdaten.md` → Eine Zeile – ein Feature | [beobachtungen-gleicher-ort.svg](../../docs/assets/images/unit11/beobachtungen-gleicher-ort.svg) | Drei eindeutig benannte Records an zwei Koordinaten; zwei unterschiedliche Termine am gleichen Ort. Tabelle und Punktkarte verbinden: Symbolüberdeckung ist weder eine Zählung von Individuen noch ein Dublettennachweis. |
| [x] | B11b · P1 | `unit11-02_gbif.md` → Beobachtungsbias | [beobachtungsbias.svg](../../docs/assets/images/unit11/beobachtungsbias.svg) | Kontrolliertes Gedankenexperiment: dieselben zwölf möglichen Vorkommensorte, aber Suche entlang eines Wegs versus Suche im ganzen Ausschnitt. Unterschiedliche Nachweiskarten trotz unveränderter Ausgangslage; Suchaufwand und ideale Entdeckung ausdrücklich benennen. Verweis aus der Punktdaten-Seite. |
| [x] | B12a · P2 | `unit12-01_vektordaten.md` → Maßstab und Generalisierung | [stuetzpunkte-generalisierung.svg](../../docs/assets/images/unit12/stuetzpunkte-generalisierung.svg) | Derselbe Linienverlauf einmal mit neun, einmal mit fünf übernommenen Stützpunkten. Segmente, ausgelassene Windungen und unveränderte Endpunkte; Generalisierung ist eine Modellentscheidung. |
| [x] | B12b · P2 | `unit12-01_vektordaten.md` → Multipart-Geometrien | [polygon-loch-multipart.svg](../../docs/assets/images/unit12/polygon-loch-multipart.svg) | Polygon mit Loch versus zwei getrennte Teile eines Multipart-Features; jeweils eine Tabellenzeile. Loch gehört nicht zur Fläche; Teilflächenzahl und Featurezahl unterscheiden. |
| [x] | B12c · P1 | `unit12-03_vektoren_qgis.md` → Auswahl und Ergebnis unterscheiden | [auswahl-zuschneiden.svg](../../docs/assets/images/unit12/auswahl-zuschneiden.svg) | Identische Linie und identisches Polygon: Auswahl mit intersects erhält die ganze Linie, Clip erzeugt nur den innerhalb liegenden Abschnitt. Auswahlexport schneidet nicht zu. Verweis von der Theorie-Seite. |
| [x] | B13a · P1 | `unit13-02_rastereigenschaften.md` → Räumliche Auflösung | [raster-vergroebern.svg](../../docs/assets/images/unit13/raster-vergroebern.svg) | Derselbe 40 × 40 m große Ausschnitt: 4 × 4 Zellen à 10 m, daraus 2 × 2 Zellen à 20 m durch berechnete Blockmittelwerte. Ein lokaler Extremwert verschwindet; bloßes Verfeinern stellt ihn nicht wieder her. |
| [x] | B13b · P2 | `unit13-02_rastereigenschaften.md` → Rasterursprung und Ausrichtung | [rasterausrichtung.svg](../../docs/assets/images/unit13/rasterausrichtung.svg) | Zwei 10-m-Gitter in demselben lokalen Meterkoordinatensystem, davon eines um 5 m nach Osten verschoben. Identische Zeilen-/Spaltennummer steht für andere Bodenfläche. |
| [x] | B13c · P1 | `unit13-02_rastereigenschaften.md` → Farbe ist nicht der Zellwert | [rasterwerte-farben.svg](../../docs/assets/images/unit13/rasterwerte-farben.svg) | Identische 3 × 3 Höhenmatrix mit zwei geordneten Farbskalen bei gleichen Grenzen. Alle Werte bleiben sichtbar; hervorgehobene Zelle hat in beiden Darstellungen 220 m. |
| [x] | B14a · P1 | `unit14-01_symbolisierung.md` → Visuelle Variablen | [symbol-und-datenart.svg](../../docs/assets/images/unit14/symbol-und-datenart.svg) | Dieselben drei Punktpositionen einmal nach Kategorie mit Formen, einmal nach numerischer Höhe mit geordneter Helligkeit. Identische Eingabetabelle; verständliche Legenden; Symbolwahl beantwortet unterschiedliche Fragen. |
| [x] | B14b · P1 | `unit14-02_klassifizierung.md` → Quantile | [klassengrenzen-zahlen.svg](../../docs/assets/images/unit14/klassengrenzen-zahlen.svg) | Zehn sichtbare Beispielhöhen, fünf Klassen, gleiche Achse und Palette: gleiche Intervalle mit Besetzung 8/1/0/0/1 versus Quantile mit 2/2/2/2/2. Numerische Breiten der Klassen korrekt zeichnen; Grenzen und Häufigkeiten vollständig nennen. Ergänzt die vorhandenen realen Vergleichskarten um das Rechenprinzip. |

## Bewusst keine weiteren Bilder

- Unit 09: Raumbezug, Gradnetz und berechneter Projektionsvergleich sind vorhanden. Ein zweiter Globus oder eine Orangenschale liefert gegenüber dem vorhandenen Vergleich wenig zusätzlichen Nutzen.
- Unit 10: Modellvergleich, Projekt/Layer/Datei, Oberfläche und Download/Webdienst bestehen bereits. Keine vollständige Serie versionsabhängiger QGIS-Screenshots.
- Unit 11: Importdialog, Herkunftsworkflow und Koordinatenunsicherheit bleiben erhalten. Keine zweite allgemeine Unsicherheitsgrafik.
- Unit 12: Die Randpunktgrafik beantwortet `intersects` versus `within` bereits. Geoportal-Metadaten sind als lesbare Tabelle ausreichend; für WMS/WFS genügt ein Verweis auf das neue Bild in Unit 10.
- Unit 13: DGM/DOM, NoData und Abtasten samt paketbelegten Kontrollfällen sind vorhanden. Keine erfundene Karte der tatsächlichen DGM-Abdeckung.
- Unit 14: Die beiden realen Klassifizierungskarten, Paletten, Hierarchie und Abschlusskarte bleiben erhalten. Das vorhandene Layout ist das Anschauungsbeispiel; zusätzliche UI- oder Exportbilder sind derzeit nicht nötig.
- Overviews und JiTT-Seiten erhalten keine dekorativen Wiederholungen. Zeitpläne, Lernziele, Datenpaket und bestehende URLs bleiben erhalten.

## Herstellung und Kontrolle

Die editierbaren SVGs werden mit `python3 scripts/figures/build_figures.py` erzeugt (optional `--unit 09` usw.). Python benötigt für das überprüfte CRS-Zahlenpaar `pyproj`; die übrigen Figuren verwenden die Standardbibliothek. Geometrie, Beispielwerte und Berechnung bleiben damit nachvollziehbar. Figuren enthalten deutsche Titel/Beschreibungen; Einbettungen zusätzlich Alt-Text, Bildunterschrift und einen Link zur Vollansicht.

- [x] Alle 14 Bilder erzeugt und an den genannten Stellen eingebunden.
- [x] Zahlenbeispiele, Transformation und Geometrievergleiche kontrolliert.
- [x] SVG/XML und Bildziele geprüft; frischer Jekyll-Build.
- [x] Alle neuen Bilder gerendert und visuell geprüft.
- [x] Betroffene Kursseiten bei Desktop- und Mobilbreite auf Lesbarkeit und Überlauf geprüft.
- [x] Context und Progress nach Sichtung/Planung, je Unit und Abschluss gesichert.

Fachliche Referenzen für die technischen Unterschiede: [QGIS 3.40: Projektion zuweisen und Layer reprojizieren](https://docs.qgis.org/3.40/en/docs/user_manual/processing_algs/qgis/vectorgeneral.html), [QGIS 3.40: Clip](https://docs.qgis.org/3.40/en/docs/user_manual/processing_algs/qgis/vectoroverlay.html#clip), [QGIS 3.40: Raster ausrichten](https://docs.qgis.org/3.40/en/docs/user_manual/processing_algs/qgis/rastertools.html#align-rasters). Die didaktischen Beispiele sind eigene, schematische Konstruktionen.

## Abschlussprüfung am 09.09.2026

14 neue SVGs auf elf Bildseiten; drei Querverweise zur Wiederverwendung, insgesamt zwölf geänderte Kursseiten. Die Units 09/10/11/12/13/14 enthalten damit 6/6/5/5/6/8 unterschiedliche Lehrbilder. Jede Bildaufgabe oben ist umgesetzt.

- Die Transformation wurde mit `pyproj` berechnet. Eine unabhängige NumPy-Kontrolle bestätigt Blockmittelwerte, Quantilgrenzen und beide Klassenbesetzungen.
- Alle 14 SVGs sind gültiges XML und wurden gerendert sowie visuell geprüft. Sichtbare Texte liegen im Bild und überlappen einander nicht.
- Frischer Build mit `bundle exec jekyll build --destination /tmp/wp12-site` aus `docs/` erfolgreich. Bestehender Hinweis auf fehlende optionale GitHub-Metadaten-Authentifizierung, kein Buildfehler.
- 178 lokale Verweise einschließlich Sprungmarken auf den betroffenen Seiten geprüft. Frontmatter, ausführbare Codeblöcke und bisherige externe URL-Ziele bleiben erhalten.
- 22 tatsächliche Seitenansichten bei 1366 und 390 Pixeln geprüft, 28 Bild-Screenshots gesichtet. Alle Bilder laden; keine Seitenüberläufe. Neue Bilder sind mobil 343 Pixel breit und verlinken auf die Vollansicht.
- Context und Progress nach Planung, Erstellung/Integration je Unit, Prüfung und Abschluss aktualisiert.

Keine neuen QGIS-Analysen oder Datenexporte waren nötig. Die Darstellungsprüfung erfolgte am Bildschirm; eine Erprobung mit Studierenden oder am Hörsaalbeamer ist damit nicht ersetzt.
