# Unit 12 – Moderation

Titelfolie, 34 Hauptfolien für 90 Minuten, eine Reserve-/Quellenfolie und eine Abschlussfolie. Zeitangaben stehen nur in diesen Notizen.

## 01 · Linien, Polygone und räumliche Auswahl

Titelfolie vor dem Einstieg zeigen.

Titelfolie beim Ankommen zeigen. Die Sitzung ist für 90 Minuten mit 100–150 Bachelor- und Lehramtsstudierenden ausgelegt. Vorbereitendes Lesen wird nicht vorausgesetzt. QGIS 3.40 und das vollständig entpackte Marburger Übungspaket müssen verfügbar sein. Erwarteter Punkteeingang ist gbif_checked aus Unit 11 oder der schemaidentische Ersatzlayer.

Quellen / Anschluss an die HTML-Lernumgebung:
/home/dirk/GeoMOER/moer-bsc-geodaten/docs/slides/Vorlagen/präs_ms02_powerpoint_de.pptx

## 02 · JiTT · Rückblick auf Unit 11

Zeitfenster: Minute 0–10 (10 Minuten).

VOR DEM TERMIN: Den gesamten Platzhalter durch die aktuelle JiTT-Auswertung zu Unit 11 ersetzen. Bei Bedarf die Folie duplizieren. Nur tatsächliche, zusammengefasste und anonymisierte Rückmeldungen einsetzen. Die gesamte Phase dauert zehn Minuten. Verständnisfragen zu Punktdaten, GBIF, Koordinatenunsicherheit oder Export klären.

## 03 · Drei Geometrien gemeinsam auswerten

Zeitfenster: Minute 10–11 (1 Minuten).

Den Ablauf ankündigen: Linien und Polygone verstehen, Datenquellen über Metadaten beurteilen, drei Layer prüfen, erst nach Attributen und dann räumlich auswählen und drei Ergebnislayer sichern.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit12/unit12-00_overview.html

## 04 · Punkt, Linie und Polygon

Zeitfenster: Minute 11–13 (2 Minuten).

An Unit 10 und 11 anknüpfen. Die Geometrie ist ein Modell für eine Fragestellung; das sichtbare Symbol besitzt zusätzliche Darstellungsbreite oder -größe. Jedes Feature bleibt mit genau einer Zeile seiner Attributtabelle verbunden.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit12/unit12-01_vektordaten.html

## 05 · Welche Geometrie passt zur Frage?

Zeitfenster: Minute 13–15 (2 Minuten).

60 Sekunden zu zweit: Für jede Frage genau einen primären Geometrietyp wählen und kurz begründen. Danach Handzeichen für Punkt, Linie oder Polygon. Die Auflösung folgt auf der nächsten Folie.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit12/unit12-01_vektordaten.html

## 06 · Lösung: Ort, Verlauf und Fläche

Zeitfenster: Minute 15–17 (2 Minuten).

Die Lösungen knapp sichern. Bei der Mündung beschreibt ein Punkt den gesuchten Ort. Für den Verlauf wird eine Linie benötigt; für die Flächenausdehnung ein Polygon. Andere Modellierungen können für andere Fragen sinnvoll sein.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit12/unit12-01_vektordaten.html

## 07 · Stützpunkte steuern den Linienverlauf

Zeitfenster: Minute 17–20 (3 Minuten).

Die Grafik von oben nach unten lesen. Zwischen benachbarten Stützpunkten liegen gerade Segmente. Weniger Stützpunkte ergeben hier eine vereinfachte Linie. Mehr Stützpunkte erlauben mehr Detail, belegen allein aber weder höhere Lagegenauigkeit noch bessere Datenqualität.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit12/unit12-01_vektordaten.html
Bild: assets/images/unit12/stuetzpunkte-generalisierung.svg

## 08 · Ein Feature kann Loch oder mehrere Teile besitzen

Zeitfenster: Minute 20–22 (2 Minuten).

Links: Die Lochfläche gehört geometrisch nicht zum Polygon. Rechts: Zwei getrennte Flächen bilden gemeinsam ein Multipart-Feature und besitzen eine Tabellenzeile. Sichtbare Flächenteile daher nicht mit Featurezahl gleichsetzen.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit12/unit12-01_vektordaten.html
Bild: assets/images/unit12/polygon-loch-multipart.svg

## 09 · Räumliche Beziehungen unterscheiden

Zeitfenster: Minute 22–24 (2 Minuten).

Begriffe nicht als Synonyme verwenden. Die Richtung der Frage ist relevant: Der Punkt liegt innerhalb des Polygons; das Polygon enthält den Punkt. Heute wird für Punkte und Linien einheitlich schneidet/intersects verwendet.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit12/unit12-01_vektordaten.html

## 10 · Zählt ein Punkt auf der Grenze mit?

Zeitfenster: Minute 24–25 (1 Minuten).

Nur die Frage stellen und A, B, C sprachlich verorten. Noch nicht vollständig auflösen; der Grenzfall wird in Minute 80 mit der tatsächlichen Auswahlregel und der Koordinatenunsicherheit erneut betrachtet.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit12/unit12-01_vektordaten.html

## 11 · Ein Geoportal ist noch kein Datensatz

Zeitfenster: Minute 25–27 (2 Minuten).

Geoportale bündeln Suche, Metadaten, Kartenansichten, Dienste und Downloads. Ein gefundener Eintrag ist noch kein analysierbarer Datensatz. Für die Leitfrage werden Feature-Geometrien und Attribute benötigt.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit12/unit12-02_geoportale.html
https://www.geoportal.hessen.de/

## 12 · Kartenbild oder analysierbare Features?

Zeitfenster: Minute 27–30 (3 Minuten).

Die drei Angebote vergleichen. WMS liefert ein gerendertes Kartenbild; daraus lassen sich nicht die benötigten Schutzgebietsfeatures auswählen. WFS und Download liefern Vektorfeatures. Für den stabilen Präsenzweg verwenden wir den vorbereiteten lokalen Snapshot.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit12/unit12-02_geoportale.html

## 13 · Metadaten beantworten die Eignungsfrage

Zeitfenster: Minute 30–32 (2 Minuten).

In der großen Gruppe sechs Leitfragen sammeln. Fehlende Angaben bleiben als Einschränkung sichtbar. Ein bekanntes Dateiformat ersetzt keine Prüfung von Inhalt, Gebiet, Aktualität, Genauigkeit und Lizenz.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit12/unit12-02_geoportale.html

## 14 · Unsere vorbereiteten Vektordaten

Zeitfenster: Minute 32–34 (2 Minuten).

Die Tabelle als kompakten Metadatennachweis lesen. Abrufdatum ist nicht automatisch fachlicher Datenstand. Die Features schneiden das 20-km-Unterrichtsrechteck, bleiben aber vollständig und sind nicht an dessen Grenze abgeschnitten.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit12/unit12-02_geoportale.html
https://www.hlnug.de/themen/geografische-informationssysteme/geodienste/naturschutz
https://www.hlnug.de/themen/geografische-informationssysteme/geodienste/wasser

## 15 · Vom Layer zur dokumentierten Auswahl

Zeitfenster: Minute 34–35 (1 Minuten).

Die Abbildung von links nach rechts lesen: drei Geometrietypen werden über Attribute und Lagebeziehungen verbunden. Die Auswahl wird nicht nur angezeigt, sondern mit Regel und Featurezahl als neuer Layer gespeichert.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit12/unit12-01_vektordaten.html
Bild: assets/images/unit12/vektor-workflow.svg

## 16 · Projekt und drei Eingangslayer vorbereiten

Zeitfenster: Minute 35–38 (3 Minuten).

Projekt als unit12_vectors.qgz speichern und EPSG:25832 setzen. Zuerst das eigene Unit-11-Ergebnis laden; falls es fehlt, ersatz/unit11_results.gpkg verwenden. Gewässer und Schutzgebiete stammen aus data_raw/marburg_basis.gpkg.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit12/unit12-03_vektoren_qgis.html
https://geomoer.github.io/moer-bsc-geodaten/material/qgis-kernpfade.html#unit12

## 17 · Kontrollpunkt vor jeder Auswahl

Zeitfenster: Minute 38–41 (3 Minuten).

Alle drei Layer auf Geometrietyp, CRS, Lage und Featurezahl prüfen. Bei Abweichung nicht mit der Auswahl fortfahren. Die Begriffe MultiLineString und MultiPolygon sind mit den Multipart-Geometrien aus dem Konzeptteil zu verbinden.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit12/unit12-03_vektoren_qgis.html

## 18 · Layerreihenfolge macht Beziehungen sichtbar

Zeitfenster: Minute 41–43 (2 Minuten).

Punkte oben, Gewässer darunter, Schutzgebiete unten anordnen. Polygonfüllung transparent oder sehr hell setzen. Diese Darstellung dient der visuellen Kontrolle; die räumliche Auswahl rechnet mit Geometrien und hängt nicht von Symbolfarbe oder Reihenfolge ab.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit12/unit12-03_vektoren_qgis.html

## 19 · Zuerst nach dem Attribut kategorie auswählen

Zeitfenster: Minute 43–47 (4 Minuten).

Attributtabelle der Schutzgebiete öffnen, Werte von kategorie prüfen und dann „Objekte über Ausdruck wählen“ verwenden. Der Feldname und der Textwert müssen exakt geschrieben werden. Die Auswahl in Tabelle und Karte kontrollieren.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit12/unit12-03_vektoren_qgis.html

## 20 · Zehn FFH-Flächen als Vergleichslayer sichern

Zeitfenster: Minute 47–50 (3 Minuten).

Erwartet sind 10 ausgewählte von 22 Schutzgebietsfeatures. Nur die Auswahl nach data_output/unit12_results.gpkg exportieren und den Layer schutzgebiete_auswahl nennen. Diesen neu geladenen Layer für beide folgenden räumlichen Auswahlen verwenden.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit12/unit12-03_vektoren_qgis.html
https://geomoer.github.io/moer-bsc-geodaten/material/qgis-kernpfade.html#unit12

## 21 · „Nach Position selektieren“ braucht klare Rollen

Zeitfenster: Minute 50–53 (3 Minuten).

Eingabelayer und Vergleichslayer ausdrücklich unterscheiden. Ausgewählt werden Features des Eingabelayers. Der Vergleichslayer liefert nur die Geometrien, zu denen die Beziehung geprüft wird.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit12/unit12-03_vektoren_qgis.html

## 22 · GBIF-Punkte gegen FFH-Flächen auswählen

Zeitfenster: Minute 53–58 (5 Minuten).

Werkzeug gemeinsam einstellen: Eingabelayer gbif_checked, Beziehung schneidet/intersects, Vergleichslayer schutzgebiete_auswahl. Auswahl im vorhandenen Punktlayer erzeugen und anschließend Attributtabelle auf nur ausgewählte Features stellen.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit12/unit12-03_vektoren_qgis.html

## 23 · Prüfwert: 4 von 56 Punkten

Zeitfenster: Minute 58–60 (2 Minuten).

Ergebnis erst abfragen, dann zeigen. Ein Punkt, der mehrere FFH-Flächen schneidet, wird in der Auswahl nur einmal gezählt. Bei Abweichung Eingabe-/Vergleichslayer, Beziehung und die zehn FFH-Features prüfen.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit12/unit12-03_vektoren_qgis.html

## 24 · Gewässer gegen dieselben FFH-Flächen auswählen

Zeitfenster: Minute 60–65 (5 Minuten).

Die zweite Auswahl mit denselben Vergleichsgeometrien durchführen. Nur der Eingabelayer wechselt zu gewaesser. Darauf hinweisen, dass Features des Datensatzes gezählt werden, nicht notwendigerweise eigenständige Flüsse.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit12/unit12-03_vektoren_qgis.html

## 25 · Prüfwert: 106 von 412 Linienfeatures

Zeitfenster: Minute 65–67 (2 Minuten).

Ergebnis abfragen und zeigen. Ein Treffer sagt zunächst nur, dass mindestens ein gemeinsamer Ort existiert. Ein Linienfeature kann ein Gebiet kurz berühren, darin verlaufen oder es vollständig durchqueren.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit12/unit12-03_vektoren_qgis.html

## 26 · Auswahl ist nicht Zuschneiden

Zeitfenster: Minute 67–69 (2 Minuten).

Die Grafik vergleichen: Intersects markiert und exportiert die vollständige Linie einschließlich außen liegender Abschnitte. Clip würde eine neue, gekürzte Geometrie erzeugen. Zuschneiden ist heute kein Pflichtschritt.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit12/unit12-03_vektoren_qgis.html
Bild: assets/images/unit12/auswahl-zuschneiden.svg

## 27 · Was dürfen wir aus 106 Treffern folgern?

Zeitfenster: Minute 69–70 (1 Minuten).

Die zu starke Aussage gemeinsam zurückweisen. Die Auswahl berechnet weder die Gewässerlänge innerhalb der FFH-Flächen noch die Anzahl eigenständiger Flüsse. Dafür wäre eine andere Operation und eine fachliche Definition erforderlich.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit12/unit12-03_vektoren_qgis.html

## 28 · Beide räumlichen Auswahlen exportieren

Zeitfenster: Minute 70–74 (4 Minuten).

Jeweils Rechtsklick auf den Eingabelayer und nur ausgewählte Objekte speichern. Beide Ergebnisse in das bereits angelegte unit12_results.gpkg schreiben. Die Namen exakt übernehmen und EPSG:25832 kontrollieren.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit12/unit12-03_vektoren_qgis.html
https://geomoer.github.io/moer-bsc-geodaten/material/qgis-kernpfade.html#unit12

## 29 · Das GeoPackage enthält drei Ergebnislayer

Zeitfenster: Minute 74–77 (3 Minuten).

Den Sollzustand vor der Endkontrolle zeigen. schutzgebiete_auswahl entstand aus der Attributauswahl; die beiden anderen Layer aus räumlichen Auswahlen. Alle drei Layer haben EPSG:25832.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit12/unit12-03_vektoren_qgis.html

## 30 · Neu laden, Auswahl lösen, Ergebnis prüfen

Zeitfenster: Minute 77–80 (3 Minuten).

Alle drei Ergebnislayer aus dem Browser neu laden. Temporäre Auswahlen in den Rohlayern aufheben oder Rohlayer deaktivieren. Featurezahlen, Geometrietyp, EPSG:25832 und plausible Lage kontrollieren. Bei technischem Scheitern ersatz/unit12_results.gpkg verwenden.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit12/unit12-03_vektoren_qgis.html
https://geomoer.github.io/moer-bsc-geodaten/material/qgis-kernpfade.html#unit12

## 31 · Ein Ergebnis braucht Regel, Zahl und Grenze

Zeitfenster: Minute 77–80 (3 Minuten).

Die Mindestdokumentation gemeinsam festhalten. Quellen stehen vollständig in documentation/quellen.md. Eine technisch eindeutige Auswahl beseitigt weder Koordinatenunsicherheit noch Modell- und Aktualitätsunterschiede der Grenzen.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit12/unit12-03_vektoren_qgis.html

## 32 · Grenzfall · erst zu zweit erklären

Zeitfenster: Minute 80–82 (2 Minuten).

Zwei Minuten zu zweit: Für A, B und C intersects und within vorhersagen. Danach erklären, was bei B mit einer unsicheren Beobachtungskoordinate fachlich offen bleibt. Die Auflösung folgt auf der nächsten Folie.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit12/unit12-00_overview.html

## 33 · Intersects zählt den Rand – Unsicherheit bleibt

Zeitfenster: Minute 82–85 (3 Minuten).

Die Tabelle in der Grafik auswerten: A wird von beiden Beziehungen gewählt, B nur von intersects, C von keiner. Das gilt für die gespeicherten Geometrien. Bei unsicherer Koordinate kann der tatsächliche Nachweisort dennoch auf der anderen Seite der modellierten Grenze liegen.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit12/unit12-01_vektordaten.html
Bild: assets/images/unit12/punkt-auf-polygongrenze.svg

## 34 · Exit Ticket · eine Frage auswählen

Zeitfenster: Minute 85–88 (3 Minuten).

Genau eine der drei Fragen auswählen und sichtbar markieren. Zwei Minuten einzeln schreiben lassen, anschließend höchstens eine knappe Antwort einsammeln. Nicht alle drei Fragen bearbeiten lassen.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit12/unit12-00_overview.html

## 35 · Nachbereitung · JiTT zu Unit 12

Zeitfenster: Minute 88–90 (2 Minuten).

Nur die JiTT-Aufgabe als verbindliche Nachbereitung nennen. Fragen, Frist und endgültiger Link stehen in ILIAS. Der Link auf der Kursseite ist noch ein sichtbarer Platzhalter; keinen Wert erfinden. Unit 13 verwendet wieder gbif_checked aus Unit 11, nicht die vier ausgewählten Punkte aus Unit 12.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit12/unit12-04_assignment.html

## 36 · Quellen und Arbeitsstand

Reserve; nicht zusätzlich in die 90 Minuten einplanen.

Nur bei Bedarf zeigen. Die Folie dokumentiert Kursseiten, QGIS-Dokumentation und Datenquellen. Die Live-Erreichbarkeit externer Portale ist für den Präsenzkern nicht erforderlich.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit12/unit12-00_overview.html

## 37 · Vielen Dank für Ihre Aufmerksamkeit

Abschluss nach der Nachbereitung; kein zusätzlicher Zeitblock.

Die Sitzung mit dieser Folie beenden. Die Abschlussgestaltung nutzt den Kontakt-Master der universitären Vorlage sowie das originale Foto-/Kartenmotiv aus der FB19-Titelseite.

Quellen / Anschluss an die HTML-Lernumgebung:
/home/dirk/GeoMOER/moer-bsc-geodaten/docs/slides/Vorlagen/präs_ms02_powerpoint_de.pptx

