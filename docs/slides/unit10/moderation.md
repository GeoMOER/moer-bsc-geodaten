# Unit 10 – Moderation

Titelfolie, 29 Hauptfolien für 90 Minuten, zwei Reserve-/Quellenfolien und eine Abschlussfolie. Zeitangaben stehen nur in diesen Notizen.

## 01 · Geodatenmodelle, QGIS und Datenquellen

Titelfolie vor dem Einstieg zeigen.

Titelfolie beim Ankommen zeigen. Die Sitzung ist für 90 Minuten mit 100–150 Bachelor- und Lehramtsstudierenden ausgelegt. Vorbereitendes Lesen wird nicht vorausgesetzt. QGIS und das vollständig entpackte Marburger Übungspaket müssen vor Sitzungsbeginn verfügbar sein. Keine Installation oder freie Datensuche während des verbindlichen Präsenzwegs einplanen.

Quellen / Anschluss an die HTML-Lernumgebung:
/home/dirk/GeoMOER/moer-bsc-geodaten/docs/slides/Vorlagen/präs_ms02_powerpoint_de.pptx

## 02 · JiTT · Rückblick auf Unit 09

Zeitfenster: Minute 0–10 (10 Minuten).

VOR DEM TERMIN: Den gesamten Platzhalter durch die aktuelle JiTT-Auswertung zu Unit 09 ersetzen. Bei Bedarf die Folie duplizieren. Nur tatsächliche, zusammengefasste und anonymisierte Rückmeldungen einsetzen. Die gesamte Phase dauert zehn Minuten. Verständnisfragen zu Koordinaten, CRS oder Projektionen klären; keinen neuen Test daraus machen.

## 03 · Von Datenmodellen zum ersten QGIS-Projekt

Zeitfenster: Minute 10–11 (1 Minuten).

Den roten Faden ankündigen: ein Modell passend zur Frage wählen, lokale Daten in QGIS prüfen und das Projekt so sichern, dass es wieder geöffnet werden kann. Der WMS folgt erst nach dem abgeschlossenen lokalen Kernpfad. Alle Studierenden bearbeiten dieselben Aufgaben.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit10/unit10-00_overview.html

## 04 · Zwei Modelle räumlicher Wirklichkeit

Zeitfenster: Minute 11–14 (3 Minuten).

Die Abbildung aus der Kursseite gemeinsam lesen. Vektorfeatures modellieren einzelne Objekte mit Geometrien und Attributen. Raster teilen den Raum in Zellen mit Werten. Die Zuordnung ist keine starre Naturregel; Fragestellung, Maßstab und vorhandene Daten entscheiden.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit10/unit10-01_datenmodelle.html
Bild: assets/images/unit10/datenmodelle.svg

## 05 · Vektor: Punkt, Linie und Polygon

Zeitfenster: Minute 14–16 (2 Minuten).

Punkt als Position, Linie als Verlauf und Polygon als Fläche erklären. Ein Punktsymbol besitzt auf dem Bildschirm eine sichtbare Größe; die Punktgeometrie selbst keine Fläche. Ein Fluss kann je nach Frage als Linie oder Polygon modelliert werden. Damit die Modellwahl an die benötigte Information binden.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit10/unit10-01_datenmodelle.html

## 06 · Raster: Zellen speichern Werte

Zeitfenster: Minute 16–18 (2 Minuten).

Links ein kontinuierliches Höhenraster, rechts ein kategoriales Landbedeckungsraster. Raster bedeutet regelmäßige Zellanordnung, nicht automatisch kontinuierliche Werte. Zellgröße, Ausdehnung, Einheit und NoData gehören zur Interpretation. Die Vertiefung folgt in Unit 13.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit10/unit10-01_datenmodelle.html

## 07 · Welches Modell passt zur Frage?

Zeitfenster: Minute 18–20 (2 Minuten).

30 Sekunden allein entscheiden, eine Minute zu zweit begründen, anschließend drei kurze Antworten sammeln. Gefragt sind Datenmodell und gegebenenfalls Geometrietyp. Die Lösung folgt auf der nächsten Folie.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit10/unit10-01_datenmodelle.html

## 08 · Die benötigte Information entscheidet

Zeitfenster: Minute 20–22 (2 Minuten).

A: Polygonvektor beschreibt Fläche und Grenze. B: kontinuierliches Raster beschreibt ein flächendeckendes Höhenfeld. C: Punktvektor beschreibt einzelne Fundorte. Andere Modellierungen sind möglich, wenn eine andere Frage oder Datengrundlage genannt wird.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit10/unit10-01_datenmodelle.html

## 09 · Projekt, Layer und Datenquelle

Zeitfenster: Minute 22–26 (4 Minuten).

Die Abbildung aus der Kursseite erläutern. Das QGIS-Projekt speichert Arbeitsstand und Verweise. Layer sind die im Projekt verwendeten Informationsebenen. Die eigentlichen Daten kommen aus lokalen Dateien oder Webdiensten. Eine qgz-Datei enthält diese Daten normalerweise nicht vollständig.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit10/unit10-02_qgigs.html
Bild: assets/images/unit10/projekt-layer-datei.svg
https://docs.qgis.org/3.40/en/docs/user_manual/introduction/project_files.html

## 10 · Warum fehlen die Layer?

Zeitfenster: Minute 26–28 (2 Minuten).

30 Sekunden allein entscheiden, dann A, B oder C per Handzeichen. Nur die Projektdatei wurde kopiert; auf dem ursprünglichen Rechner waren alle Layer sichtbar. Die Dateien wurden nicht durch QGIS gelöscht. Die Lösung folgt auf der nächsten Folie.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit10/unit10-02_qgigs.html

## 11 · Projekt und Daten gemeinsam erhalten

Zeitfenster: Minute 28–30 (2 Minuten).

B ist richtig. Die Projektdatei verweist auf Datendateien. Deshalb den vollständig entpackten Arbeitsordner mit stabiler Struktur verwenden. Relative Pfade erleichtern eine Übertragung, ersetzen die Dateien aber nicht. Das erneute Öffnen ist die entscheidende Kontrolle.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit10/unit10-02_qgigs.html

## 12 · Die wichtigsten Bereiche in QGIS

Zeitfenster: Minute 30–33 (3 Minuten).

Die schematische QGIS-3.40-Ansicht aus der Kursseite zeigen. Browser, Layer-Bereich, Kartenansicht und Statusleiste finden lassen. Die genaue Position von Symbolen kann je nach Betriebssystem und persönlicher Konfiguration abweichen. Nur die heute benötigten Bereiche erklären.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit10/unit10-02_qgigs.html
Bild: assets/images/unit10/qgis-oberflaeche.svg
https://docs.qgis.org/3.40/en/docs/user_manual/introduction/qgis_gui.html

## 13 · Unser verbindlicher Praxisweg

Zeitfenster: Minute 33–35 (2 Minuten).

Vor Beginn den Endzustand und die Reihenfolge klären. Alle Pfade beziehen sich auf den vollständig entpackten Ordner marburg_geodaten. Die WMS-Einrichtung beginnt erst nach dem geprüften lokalen Projekt und ist auf dem eigenen Gerät freiwillig.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/material/qgis-kernpfade.html#unit10

## 14 · Arbeitsordner und Projekt vorbereiten

Zeitfenster: Minute 35–38 (3 Minuten).

Den entpackten Paketordner öffnen. Kein zusätzlicher Unterordner unit10_qgis anlegen. Neues QGIS-Projekt erstellen, Projekt-CRS EPSG:25832 prüfen und sofort im Hauptordner speichern. Die gezeigte Struktur entspricht dem aktuellen Paket. Ausgangsdaten in data_raw nicht überschreiben.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit10/unit10-02_qgigs.html
https://geomoer.github.io/moer-bsc-geodaten/material/qgis-kernpfade.html#unit10

## 15 · Gewässerlayer laden

Zeitfenster: Minute 38–42 (4 Minuten).

Im Browser den Hauptordner und data_raw öffnen. Im GeoPackage marburg_basis.gpkg den Layer gewaesser wählen. Nach dem Laden auf die Layerausdehnung zoomen. Erwartet sind 412 Multi-Linienfeatures in EPSG:25832; die Zahl dient als Kontrollwert, nicht als auswendig zu lernender Inhalt.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit10/unit10-02_qgigs.html
https://geomoer.github.io/moer-bsc-geodaten/material/qgis-kernpfade.html#unit10

## 16 · Höhenraster laden

Zeitfenster: Minute 42–46 (4 Minuten).

Das GeoTIFF aus data_raw laden. Es besitzt 2000 × 2000 Zellen à 10 Meter und EPSG:25832. NoData ist −9999. Diese Werte dienen heute nur zur Identifikation und Kontrolle; die inhaltliche Rasteranalyse folgt in Unit 13. Wenn das Raster die Gewässer verdeckt, die Layerreihenfolge ändern.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit10/unit10-02_qgigs.html
https://geomoer.github.io/moer-bsc-geodaten/material/qgis-kernpfade.html#unit10

## 17 · Verdeckt heißt nicht gelöscht

Zeitfenster: Minute 46–49 (3 Minuten).

Die Abbildung der Kursseite erläutern. Oben stehende Layer werden zuletzt gezeichnet und können darunterliegende Inhalte verdecken. Sichtbarkeit und Reihenfolge verändern nur die Darstellung im Projekt, nicht die gespeicherten Features. Im eigenen Projekt Gewässer über dem DGM anzeigen.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit10/unit10-02_qgigs.html
Bild: assets/images/unit10/layerreihenfolge.svg

## 18 · Beide Layer kurz bedienen

Zeitfenster: Minute 49–55 (6 Minuten).

Zeit zum angeleiteten Mitmachen. Sichtbarkeit beider Layer einzeln schalten, auf den Gewässerlayer zoomen und den Kartenausschnitt verschieben. Dann im Layer-Bereich benennen: Welcher Layer ist Vektor, welcher Raster? Nicht weitere Daten oder alternative Ladewege ergänzen.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit10/unit10-02_qgigs.html
https://geomoer.github.io/moer-bsc-geodaten/material/qgis-kernpfade.html#unit10

## 19 · Feature und Tabellenzeile verbinden

Zeitfenster: Minute 55–59 (4 Minuten).

Attributtabelle des Layers gewaesser öffnen. Ein Feature in der Karte auswählen beziehungsweise abfragen und die zugehörige Tabellenzeile zeigen. Raster besitzt keine gewöhnliche Featuretabelle. Die konkrete Attributausprägung wird nicht vorgegeben; Studierende wählen ein sichtbares Gewässerfeature.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit10/unit10-02_qgigs.html

## 20 · Datenquelle, Modell und CRS prüfen

Zeitfenster: Minute 59–64 (5 Minuten).

Für beide Layer die Eigenschaften öffnen und Datenquelle, Datenmodell, CRS und Ausdehnung finden. Die Studierenden tragen die tatsächliche Ausdehnung selbst ein. Beide Layer nutzen EPSG:25832. Unterschiedliche bekannte Layer-CRS wären nicht automatisch ein Fehler; QGIS kann für die Anzeige dynamisch transformieren.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit10/unit10-02_qgigs.html
https://geomoer.github.io/moer-bsc-geodaten/material/qgis-kernpfade.html#unit10

## 21 · Kontrollen dokumentieren

Zeitfenster: Minute 64–68 (4 Minuten).

Die vorbereitete Tabelle unter documentation/processing_notes.md verwenden. Keine neue Vorlage anlegen. Datenquelle, Modell, Layer-CRS und Ausdehnung beider Layer festhalten. Das Ergebnis des späteren Öffnungstests wird anschließend ergänzt.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit10/unit10-02_qgigs.html
https://geomoer.github.io/moer-bsc-geodaten/material/qgis-kernpfade.html#unit10

## 22 · Speichern, schließen, erneut öffnen

Zeitfenster: Minute 68–72 (4 Minuten).

Jetzt den verbindlichen Öffnungstest durchführen. Erst speichern, dann QGIS schließen. Die qgz-Datei aus dem Hauptordner erneut öffnen. Nicht über die Liste zuletzt geöffneter Projekte ausweichen, damit der Speicherort sichtbar bleibt.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit10/unit10-02_qgigs.html
https://geomoer.github.io/moer-bsc-geodaten/material/qgis-kernpfade.html#unit10

## 23 · Was prüfen Sie bei einem roten Ausrufezeichen?

Zeitfenster: Minute 72–75 (3 Minuten).

Das Symbol steht hier für eine nicht erreichbare Datenquelle. 30 Sekunden zu zweit den ersten sinnvollen Prüfschritt formulieren lassen. Nicht verschiedene CRS ausprobieren: Ein nicht erreichbarer Dateipfad ist zunächst ein Ablageproblem.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit10/unit10-02_qgigs.html

## 24 · Ablage prüfen – dann Ergebnis sichern

Zeitfenster: Minute 75–78 (3 Minuten).

A ist richtig. Prüfen, ob Projekt und vollständig entpackter Datenordner noch zusammenliegen und ob Dateien umbenannt oder verschoben wurden. Nach einer nötigen Pfadreparatur erneut speichern, schließen und öffnen. Im Protokoll vollständig ja oder nein eintragen und ein Problem knapp notieren.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit10/unit10-02_qgigs.html
https://geomoer.github.io/moer-bsc-geodaten/material/qgis-kernpfade.html#unit10

## 25 · Download oder Webdienst?

Zeitfenster: Minute 78–79 (1 Minuten).

Die Abbildung kurz als Übergang lesen. Ein Download erzeugt eine lokale, dokumentierbare Kopie. Ein Webdienst antwortet bei jeder Anfrage über das Netz. In beiden Fällen Metadaten, Datenstand, Lizenz und Quelle dokumentieren.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit10/unit10-03_datenquellen.html
Bild: assets/images/unit10/download-webdienst.svg

## 26 · Ein WMS liefert ein Kartenbild

Zeitfenster: Minute 79–81 (2 Minuten).

WMS als Web Map Service auflösen. QGIS sendet Ausschnitt, Bildgröße und CRS; der Server liefert ein gerendertes Kartenbild. Ein WMS eignet sich für Orientierung und Hintergrund, aber normalerweise nicht für eine freie Vektoranalyse. Begrenzte Objektabfragen können möglich sein.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit10/unit10-03_datenquellen.html

## 27 · HLNUG-WMS gemeinsam einbinden

Zeitfenster: Minute 81–84 (3 Minuten).

Die lokale Kernübung ist beendet. Die Lehrperson demonstriert die vorgegebene Verbindung. Studierende mit fertigem Projekt können optional mitmachen. Dienstadresse von der Kursseite kopieren, nicht aus einer Portalseiten-URL erraten. Bei der ersten Nichterreichbarkeit direkt zur nächsten Folie wechseln.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit10/unit10-03_datenquellen.html

## 28 · Offline-Ersatz: derselbe Vergleich bleibt möglich

Zeitfenster: Minute 84–85 (1 Minuten).

Wenn der Dienst nicht unmittelbar reagiert, ohne weiteren Versuch diese vorbereiteten Paketdateien verwenden: wms_schutzgebiete.png, wms_capabilities.xml und documentation/quellen.md. Der Screenshot zeigt nur die gerenderte Schutzgebietsdarstellung. Capabilities und Quellenblatt liefern Dienst- und Metadaten. Der Ausfall ist kein studentischer Fehler.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit10/unit10-03_datenquellen.html
Ersatzbild aus assets/data/marburg/marburg_geodaten.zip

## 29 · Exit-Ticket: Was nehmen Sie mit?

Zeitfenster: Minute 85–88 (3 Minuten).

Eine der drei Fragen passend zum Sitzungsverlauf auswählen. Eine Minute zu zweit formulieren lassen und anschließend eine gemeinsame Antwort sichern. Nicht alle drei Fragen als Pflichtaufgabe behandeln. Erwartet: 1. qgz speichert Arbeitsstand und Verweise, nicht normalerweise alle Daten. 2. Layerart über Symbol, Eigenschaften und Attributtabelle prüfen. 3. WMS liefert primär ein Kartenbild und keine frei analysierbaren Vektorfeatures.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit10/unit10-00_overview.html

## 30 · Nachbereitung und nächster Schritt

Zeitfenster: Minute 88–90 (2 Minuten).

Als einzige Übungsaufgabe die JiTT-Fragen zu Unit 10 im ILIAS-Kurs nennen. Fragen und Frist stehen in ILIAS; der konkrete Link ist auf der Kursseite noch Platzhalter. Keine Fertigstellung der WMS-Einrichtung oder des Praxiswegs als Übungsaufgabe verlangen. Unit 11 beginnt nach der Winterpause mit dem kurzen QGIS-Wiedereinstieg und importiert Punktdaten.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit10/unit10-04_assignment.html

## 31 · WMS oder WFS?

Reserve; nicht zusätzlich in die 90 Minuten einplanen.

Nur bei Bedarf zur begrifflichen Abgrenzung zeigen. Ein WMS liefert primär ein gerendertes Kartenbild. Ein WFS liefert Vektorfeatures mit Geometrien und Attributen. WFS wird in Unit 10 nicht praktisch eingerichtet. Die Abbildung ist schematisch und ersetzt keine Dienstprüfung.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit10/unit10-03_datenquellen.html
Bild: assets/images/unit10/wms-wfs.svg

## 32 · Materialien und Quellen

Reserve; nicht zusätzlich in die 90 Minuten einplanen.

Fachliche Grundlage sind die aktuellen fünf Unit-10-Seiten, der QGIS-Kernpfad und das Marburger Übungspaket vom 08.09.2026. Die Folien verwenden die vorhandenen Unit-10-Abbildungen sowie den vorbereiteten WMS-Ersatz aus dem Paket. QGIS-Dokumentation passend zur Kursversion 3.40 verlinken. Der HLNUG-Dienst wird nach Angabe der Kursseite verwendet; seine Live-Erreichbarkeit ist nicht Voraussetzung der Sitzung.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit10/unit10-00_overview.html
https://geomoer.github.io/moer-bsc-geodaten/unit10/unit10-01_datenmodelle.html
https://geomoer.github.io/moer-bsc-geodaten/unit10/unit10-02_qgigs.html
https://geomoer.github.io/moer-bsc-geodaten/unit10/unit10-03_datenquellen.html
https://geomoer.github.io/moer-bsc-geodaten/unit10/unit10-04_assignment.html
https://geomoer.github.io/moer-bsc-geodaten/material/qgis-kernpfade.html#unit10
https://docs.qgis.org/3.40/en/docs/user_manual/
https://www.hlnug.de/themen/geografische-informationssysteme/geodienste/naturschutz
https://geodienste-umwelt.hessen.de/arcgis/services/inspire/schutzgebiete/MapServer/WmsServer

## 33 · Vielen Dank für Ihre Aufmerksamkeit

Abschluss nach der Nachbereitung; kein zusätzlicher Zeitblock.

Die Sitzung mit dieser Folie beenden. Die Abschlussgestaltung nutzt den Kontakt-Master der universitären Vorlage sowie das originale Foto-/Kartenmotiv aus der FB19-Titelseite.

Quellen / Anschluss an die HTML-Lernumgebung:
/home/dirk/GeoMOER/moer-bsc-geodaten/docs/slides/Vorlagen/präs_ms02_powerpoint_de.pptx

