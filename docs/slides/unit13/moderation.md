# Unit 13 – Moderation

Titelfolie, 32 Hauptfolien für 90 Minuten, zwei Reserve-/Quellenfolien und eine Abschlussfolie. Zeitangaben stehen nur in diesen Notizen.

## 01 · Rasterdaten und Höhenwerte

Titelfolie vor dem Einstieg zeigen.

Titelfolie beim Ankommen zeigen. Die Sitzung ist für 90 Minuten mit 100–150 Bachelor- und Lehramtsstudierenden ausgelegt. Vorbereitendes Lesen wird nicht vorausgesetzt. QGIS 3.40 und das vollständig entpackte Marburger Übungspaket müssen verfügbar sein. Erwarteter Punkteeingang ist gbif_checked mit 56 Features aus Unit 11 oder der schemaidentische Ersatzlayer.

Quellen / Anschluss an die HTML-Lernumgebung:
/home/dirk/GeoMOER/moer-bsc-geodaten/docs/slides/Vorlagen/präs_ms02_powerpoint_de.pptx

## 02 · JiTT · Rückblick auf Unit 12

Zeitfenster: Minute 0–10 (10 Minuten).

VOR DEM TERMIN: Den gesamten Platzhalter durch die aktuelle JiTT-Auswertung zu Unit 12 ersetzen. Bei Bedarf die Folie duplizieren. Nur tatsächliche, zusammengefasste und anonymisierte Rückmeldungen einsetzen. Die gesamte Phase dauert zehn Minuten. Verständnisfragen zu Linien, Polygonen, Metadaten oder räumlicher Auswahl klären.

## 03 · Vom Höhenraster zum Punktattribut

Zeitfenster: Minute 10–11 (1 Minuten).

Den Ablauf ankündigen: Rastermodell verstehen, DGM-Eigenschaften prüfen, Werte darstellen und abfragen, Rasterwerte an 56 Punkten abtasten und das Ergebnis mit 35 Zahlen und 21 NULL-Werten dokumentieren.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit13/unit13-00_overview.html

## 04 · Objekte oder flächendeckendes Wertefeld?

Zeitfenster: Minute 11–13 (2 Minuten).

Vektor modelliert einzelne Features mit Geometrie und Attributzeile. Raster teilt den Raum regelmäßig in Zellen mit Werten. Beide Modelle lassen sich kombinieren: Punktposition plus Höhenraster ergibt den Zellwert am Beobachtungsort.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit13/unit13-01_rasterdaten.html

## 05 · Ein Raster ordnet jeder Zelle einen Wert zu

Zeitfenster: Minute 13–15 (2 Minuten).

Zeilen, Spalten und Zellen benennen. Die Position einer Zelle folgt aus Rasterursprung, Zellgröße und CRS. Der Wert 228 ist ein schematischer Höhenwert in Metern, nicht bereits ein Attribut des danebenliegenden Punkts.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit13/unit13-01_rasterdaten.html

## 06 · Kontinuierlich oder kategorial?

Zeitfenster: Minute 15–18 (3 Minuten).

Kurze Zuordnung im Plenum: Geländehöhe ist kontinuierlich, Landbedeckung kategorial. Bei Kategorien sind Zahlen Codes ohne metrische Abstände; sie benötigen Einzelfarben. Höhenwerte können mit einem sequentiellen Verlauf dargestellt werden.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit13/unit13-01_rasterdaten.html

## 07 · DGM und DOM beschreiben verschiedene Oberflächen

Zeitfenster: Minute 18–21 (3 Minuten).

Dasselbe Landschaftsprofil vergleichen. Das DGM folgt dem Gelände unter Vegetation und Gebäuden; das DOM folgt der erfassten Oberfläche über Baumkrone und Dach. Für die Frage nach Geländehöhe der Beobachtungen verwenden wir das DGM.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit13/unit13-01_rasterdaten.html
Bild: assets/images/unit13/dgm-dom-profil.svg

## 08 · Rasterzelle und Bildschirmpixel sind nicht dasselbe

Zeitfenster: Minute 21–22 (1 Minuten).

Beim starken Hineinzoomen wird eine Datenzelle als großes Quadrat sichtbar. Dieses Quadrat besteht am Monitor aus vielen Bildschirmpixeln. Für die fachliche Beschreibung der gespeicherten räumlichen Einheit den Begriff Rasterzelle verwenden.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit13/unit13-01_rasterdaten.html

## 09 · Vergröbern fasst Werte zusammen

Zeitfenster: Minute 22–25 (3 Minuten).

Die Grafik von oben nach unten lesen. Aus vier 10-m-Zellen entsteht hier eine 20-m-Zelle mit Mittelwert. Lokale Spitzen gehen verloren. Ein später wieder feineres Gitter kann diese Information nicht zurückholen. Die Zahlen sind ein schematisches Rechenbeispiel.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit13/unit13-02_rastereigenschaften.html
Bild: assets/images/unit13/raster-vergroebern.svg

## 10 · Projekt, DGM und Punkte vorbereiten

Zeitfenster: Minute 25–28 (3 Minuten).

Projekt als unit13_raster.qgz speichern und EPSG:25832 setzen. Das DGM und gbif_checked laden. Nicht die vier Punkte aus Unit 12 verwenden: Unit 13 beginnt erneut mit allen 56 qualitätsgeprüften Punkten aus Unit 11.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit13/unit13-03_raster_qgis.html
https://geomoer.github.io/moer-bsc-geodaten/material/qgis-kernpfade.html#unit13

## 11 · Das DGM ist ein abgeleitetes Lehrprodukt

Zeitfenster: Minute 28–31 (3 Minuten).

Quelle und Bearbeitung trennen. Grundlage sind 162 amtliche DGM1-Kacheln des Hessen Geodatenmanagements. Für den Kurs wurden verfügbare 1-m-Werte zu 10-m-Mittelwerten zusammengefasst. Das Ergebnis ist kein unverändertes amtliches DGM10.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit13/unit13-03_raster_qgis.html
https://hvbg.hessen.de/landesvermessung/geotopographie/3d-daten/digitale-gelaendemodelle

## 12 · Rastereigenschaften gemeinsam kontrollieren

Zeitfenster: Minute 31–34 (3 Minuten).

Layereigenschaften öffnen und Werte gemeinsam finden. Minimum und Maximum sind gerundet. Die Höhenangaben beziehen sich auf DHHN2016_NH; das horizontale CRS ist EPSG:25832. NoData muss von gültigen Werten ausgeschlossen sein.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit13/unit13-03_raster_qgis.html

## 13 · Das Rasterrechteck ist nicht vollständig belegt

Zeitfenster: Minute 34–37 (3 Minuten).

Rasterausdehnung und Datenabdeckung unterscheiden. Die Datei deckt das 20-km-Rechteck technisch ab, aber nur 40,01 Prozent der Zellen enthalten gültige Höhen. Die Lücke stammt aus der DGM-Kachelabdeckung und darf nicht aufgefüllt oder als Höhe null gelesen werden.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit13/unit13-03_raster_qgis.html

## 14 · Gleiche Zellgröße genügt nicht

Zeitfenster: Minute 37–40 (3 Minuten).

Die Gitter vergleichen: Beide besitzen 10-m-Zellen im selben lokalen Meterkoordinatensystem, aber Gitter B beginnt fünf Meter weiter östlich. Für zellenweise Berechnungen müssen auch Ursprung beziehungsweise Zellgrenzen passen. Heute wird kein Raster neu ausgerichtet.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit13/unit13-02_rastereigenschaften.html
Bild: assets/images/unit13/rasterausrichtung.svg

## 15 · Einzelne Zellwerte zuerst direkt abfragen

Zeitfenster: Minute 40–43 (3 Minuten).

Mit Objekte abfragen an mehreren Stellen in Band 1 klicken. Einen gültigen Wert und eine NoData-Stelle vergleichen. Die Einheit Meter, den Wertebereich und die räumliche Lage plausibilisieren, bevor Punkte abgetastet werden.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit13/unit13-03_raster_qgis.html

## 16 · NoData ist nicht der gültige Wert 0

Zeitfenster: Minute 43–46 (3 Minuten).

Die schematische Grafik lesen. Ein gültiger Nullwert ist eine fachliche Zahl. NoData bedeutet fehlenden oder ungültigen Wert. Im Marburger DGM lautet der technische Kennwert -9999; beim Abtasten wird daraus NULL. Das gezeigte 0-m-Beispiel stammt nicht aus dem Marburger Ausschnitt.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit13/unit13-02_rastereigenschaften.html
Bild: assets/images/unit13/zellgroesse-nodata-genauigkeit.svg

## 17 · Höhenwerte mit Pseudofarbe darstellen

Zeitfenster: Minute 46–49 (3 Minuten).

Layereigenschaften → Symbolisierung: Einkanal-Pseudofarbe, Band 1, Minimum und Maximum für den relevanten Datensatz laden und einen sequentiellen Farbverlauf verwenden. NoData transparent halten. Die systematische Kartengestaltung folgt erst in Unit 14.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit13/unit13-03_raster_qgis.html

## 18 · Andere Farben, gleiche Werte

Zeitfenster: Minute 49–51 (2 Minuten).

Die umrahmte Zelle in beiden Darstellungen ablesen. In beiden Fällen bleibt ihr Wert 220 m. Nur die Zuordnung von Zahlen zu Farben ändert sich. Die Beispielmatrix ist schematisch und keine Marburger Messung.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit13/unit13-02_rastereigenschaften.html
Bild: assets/images/unit13/rasterwerte-farben.svg

## 19 · Eine kleine Zelle beweist keine hohe Genauigkeit

Zeitfenster: Minute 51–53 (2 Minuten).

Zwei Minuten zu zweit: Die Aussage prüfen und mindestens eine zusätzliche Metadatenangabe nennen. Unterscheiden: Zellgröße beschreibt das Gitter; Lage- und Wertgenauigkeit beschreiben Unsicherheiten. Die Auflösung folgt auf der nächsten Folie.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit13/unit13-00_overview.html

## 20 · Auflösung, Lage und Wert getrennt beurteilen

Zeitfenster: Minute 53–55 (2 Minuten).

Drei Begriffe sichern. Für die Höhengenauigkeit werden Erfassungsmethode und dokumentierte vertikale Genauigkeit benötigt. Das heutige Kursraster hat 10-m-Zellen, nicht 1-m-Zellen; die Ausgangsdaten wurden gemittelt.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit13/unit13-02_rastereigenschaften.html

## 21 · Punkteeingang: alle 56 aus Unit 11

Zeitfenster: Minute 55–58 (3 Minuten).

gbif_checked laden und auf 56 Features, EPSG:25832 und das vollständige Feldschema prüfen. Einige Punkte liegen außerhalb gültiger DGM-Zellen. Sie bleiben im Ergebnis und erhalten später NULL.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit13/unit13-03_raster_qgis.html
https://geomoer.github.io/moer-bsc-geodaten/material/qgis-kernpfade.html#unit13

## 22 · Werkzeug „Rasterwerte abtasten“ einstellen

Zeitfenster: Minute 58–62 (4 Minuten).

Verarbeitungswerkzeuge öffnen und Sample raster values beziehungsweise Rasterwerte abtasten wählen. Eingabelayer, Raster und Präfix exakt kontrollieren. Der Ausgabepfad und Layername werden bereits im Werkzeug festgelegt.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit13/unit13-03_raster_qgis.html

## 23 · Der getroffene Zellwert wird zum Attribut

Zeitfenster: Minute 62–65 (3 Minuten).

Die Grafik von links nach rechts lesen. Der Punkt liegt in der Zelle mit dem sichtbaren Wert 228 und erhält diesen Wert im neuen Attribut. Das Beispiel erklärt die Operation; 228 ist kein geforderter Kontrollwert für einen bestimmten GBIF-Record.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit13/unit13-03_raster_qgis.html
Bild: assets/images/unit13/raster-workflow.svg

## 24 · QGIS erzeugt zunächst hoehe_1

Zeitfenster: Minute 65–68 (3 Minuten).

Werkzeug ausführen und Ergebnisattributtabelle öffnen. Mit QGIS 3.40 und dem Präfix hoehe_ heißt das Band-1-Feld hoehe_1. Den tatsächlichen Namen prüfen. Noch nicht einfach ein zweites Feld ergänzen, ohne das Übergabeschema zu planen.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit13/unit13-03_raster_qgis.html

## 25 · Nur das Höhenfeld kontrolliert umbenennen

Zeitfenster: Minute 68–72 (4 Minuten).

Mit Felder überarbeiten hoehe_1 in hoehe_m umbenennen und alle übrigen GBIF-Felder unverändert erhalten. Alternativ kann ein neues Dezimalfeld berechnet werden; dann das überflüssige hoehe_1 entfernen. Jeden Schritt dokumentieren.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit13/unit13-03_raster_qgis.html

## 26 · Prüfwert: 35 Höhen und 21 NULL

Zeitfenster: Minute 72–75 (3 Minuten).

Ergebnis zuerst abfragen, dann zeigen. Alle 56 Punkte müssen erhalten bleiben. 35 treffen eine gültige DGM-Zelle; 21 liegen außerhalb der gültigen Abdeckung und erhalten NULL. NULL-Werte nicht durch 0 ersetzen und die Punkte nicht löschen.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit13/unit13-03_raster_qgis.html

## 27 · Ergebnis speichern und neu laden

Zeitfenster: Minute 75–78 (3 Minuten).

Sicherstellen, dass das endgültige Ergebnis wirklich im GeoPackage liegt und hoehe_m enthält. Den Layer aus dem Browser neu laden und die temporäre Werkzeugausgabe deaktivieren. Bei technischem Scheitern ersatz/unit13_results.gpkg/gbif_mit_hoehe laden und die Ersatznutzung notieren.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit13/unit13-03_raster_qgis.html
https://geomoer.github.io/moer-bsc-geodaten/material/qgis-kernpfade.html#unit13

## 28 · Zwei konkrete Punkte als Stichprobe

Zeitfenster: Minute 78–81 (3 Minuten).

Die beiden GBIF-IDs im Ergebnis suchen. Für den gültigen Fall Raster an derselben Position direkt abfragen und den ungerundeten Wert vergleichen. Der zweite Punkt belegt einen NULL-Fall. Die Werte sind im Ersatzlayer geprüft.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit13/unit13-03_raster_qgis.html

## 29 · Gültige Punkthöhen liegen zwischen 178,55 und 323,90 m

Zeitfenster: Minute 81–82 (1 Minuten).

Die Werte beziehen sich ausschließlich auf die 35 Punkte mit gültigem Rasterwert im bereitgestellten Snapshot. Keine Aussage über alle Feuersalamander oder ihre vollständige Höhenverbreitung ableiten. Ein Median ist im Kernweg nicht vorgegeben und wird nicht erfunden.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit13/unit13-03_raster_qgis.html

## 30 · Welche Unsicherheiten treffen zusammen?

Zeitfenster: Minute 82–84 (2 Minuten).

Die drei Unsicherheitsquellen sammeln. Der Rasterwert beschreibt die getroffene 10-m-Zelle, die Punktkoordinate den gemeldeten Ort mit eigener Unsicherheit. DGM-Entstehung, Mittelung, Datenstand und Gelände-/Oberflächenbezug begrenzen die Aussage zusätzlich.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit13/unit13-03_raster_qgis.html

## 31 · Quelle, Verarbeitung und Ergebnis dokumentieren

Zeitfenster: Minute 84–85 (1 Minuten).

Die Mindestangaben sichern. DHHN2016_NH ist der Höhenbezug, EPSG:25832 der horizontale Raumbezug. Die DGM-Lücke und 21 NULL-Werte sind dokumentierte Datenmerkmale, kein Fehler, der verborgen werden soll.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit13/unit13-03_raster_qgis.html
https://hvbg.hessen.de/landesvermessung/geotopographie/3d-daten/digitale-gelaendemodelle

## 32 · Exit Ticket · eine Frage auswählen

Zeitfenster: Minute 85–88 (3 Minuten).

Genau eine der drei Fragen auswählen und sichtbar markieren. Zwei Minuten einzeln schreiben lassen, anschließend höchstens eine knappe Antwort einsammeln. Nicht alle drei Fragen bearbeiten lassen.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit13/unit13-00_overview.html

## 33 · Nachbereitung · JiTT zu Unit 13

Zeitfenster: Minute 88–90 (2 Minuten).

Nur die JiTT-Aufgabe als verbindliche Nachbereitung nennen. Fragen, Frist und endgültiger Link stehen in ILIAS. Der Link auf der Kursseite ist noch ein sichtbarer Platzhalter; keinen Wert erfinden. Unit 14 kartiert nur die 35 Punkte mit gültigem hoehe_m und dokumentiert diese Einschränkung.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit13/unit13-04_assignment.html

## 34 · Vertiefung: Neuabtastung bewusst wählen

Reserve; nicht zusätzlich in die 90 Minuten einplanen.

Nur bei Rückfragen verwenden. Bei geändertem Gitter entstehen neue Rasterwerte. Für Kategorien ist meist nächster Nachbar geeignet; bilineare oder kubische Verfahren berechnen Zwischenwerte und passen eher zu kontinuierlichen Daten. In der Kernübung wird das DGM nicht eigenständig reprojiziert oder neu abgetastet.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit13/unit13-02_rastereigenschaften.html

## 35 · Quellen und Arbeitsstand

Reserve; nicht zusätzlich in die 90 Minuten einplanen.

Nur bei Bedarf zeigen. Die Folie dokumentiert Kursseiten, QGIS-Dokumentation und Datenquelle. Die Live-Erreichbarkeit externer Seiten ist für den Präsenzkern nicht erforderlich.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit13/unit13-00_overview.html

## 36 · Vielen Dank für Ihre Aufmerksamkeit

Abschluss nach der Nachbereitung; kein zusätzlicher Zeitblock.

Die Sitzung mit dieser Folie beenden. Die Abschlussgestaltung nutzt den Kontakt-Master der universitären Vorlage sowie das originale Foto-/Kartenmotiv aus der FB19-Titelseite.

Quellen / Anschluss an die HTML-Lernumgebung:
/home/dirk/GeoMOER/moer-bsc-geodaten/docs/slides/Vorlagen/präs_ms02_powerpoint_de.pptx

