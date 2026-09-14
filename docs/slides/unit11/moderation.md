# Unit 11 – Moderation

Titelfolie, 32 Hauptfolien für 90 Minuten, zwei Reserve-/Quellenfolien und eine Abschlussfolie. Zeitangaben stehen nur in diesen Notizen.

## 01 · Punktdaten, GBIF und Datenqualität

Titelfolie vor dem Einstieg zeigen.

Titelfolie beim Ankommen zeigen. Die Sitzung ist für 90 Minuten mit 100–150 Bachelor- und Lehramtsstudierenden ausgelegt. Vorbereitendes Lesen wird nicht vorausgesetzt. QGIS 3.40 und das vollständig entpackte Marburger Übungspaket müssen vor Sitzungsbeginn verfügbar sein. Alle Studierenden bearbeiten denselben Kernpfad. Die Folien unterscheiden bewusst Nachweis, Punktgeometrie und Verbreitung.

Quellen / Anschluss an die HTML-Lernumgebung:
/home/dirk/GeoMOER/moer-bsc-geodaten/docs/slides/Vorlagen/präs_ms02_powerpoint_de.pptx

## 02 · JiTT · Rückblick auf Unit 10

Zeitfenster: Minute 0–10 (10 Minuten).

VOR DEM TERMIN: Den gesamten Platzhalter durch die aktuelle JiTT-Auswertung zu Unit 10 ersetzen. Bei Bedarf die Folie duplizieren. Nur tatsächliche, zusammengefasste und anonymisierte Rückmeldungen einsetzen. Die gesamte Phase dauert zehn Minuten. Verständnisfragen zu Datenmodellen, Layern, Datenquellen oder CRS klären.

## 03 · Vom Nachweis zum geprüften Punktlayer

Zeitfenster: Minute 10–11 (1 Minuten).

Den roten Faden ankündigen: Bedeutung von Punktdaten klären, den dokumentierten GBIF-Snapshot als CSV importieren, eine begründete Qualitätsregel anwenden und das Ergebnis reproduzierbar exportieren.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit11/unit11-00_overview.html

## 04 · Ein Punkt ist eine Repräsentation

Zeitfenster: Minute 11–14 (3 Minuten).

Die vier Ebenen nacheinander benennen. Der sichtbare Kreis auf der Karte ist nicht die räumliche Ausdehnung des Tiers. Die Unsicherheit beschreibt die Lageangabe, nicht das Streifgebiet. Diese Trennung später beim Import wieder aufnehmen.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit11/unit11-01_punktdaten.html
Bild: assets/images/unit11/punkt-beobachtung-unsicherheit.svg

## 05 · Ein Record ist nicht automatisch ein Tier

Zeitfenster: Minute 14–17 (3 Minuten).

Kurze Nachbarschaftsfrage: Was könnte eine Tabellenzeile repräsentieren? Danach die Ebenen aufdecken. Ein Occurrence Record dokumentiert einen Nachweis. Mehrere Records können dasselbe Individuum, denselben Ort oder verschiedene Ereignisse betreffen.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit11/unit11-01_punktdaten.html

## 06 · Drei Records können wie zwei Punkte aussehen

Zeitfenster: Minute 17–20 (3 Minuten).

Zuerst nur die Grafik lesen lassen. A und B besitzen dieselben Koordinaten, aber verschiedene Daten. Sie überlagern sich in der Karte, bleiben jedoch zwei Records. Daraus folgt: gleiche Koordinaten sind kein ausreichender Grund zum Löschen.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit11/unit11-01_punktdaten.html
Bild: assets/images/unit11/beobachtungen-gleicher-ort.svg

## 07 · Was dokumentiert ein GBIF Occurrence Record?

Zeitfenster: Minute 20–22 (2 Minuten).

GBIF als internationale Dateninfrastruktur und Aggregator erklären. Der Record kann auf Beobachtung, Beleg, Probe oder anderer Grundlage beruhen. Das Feld basisOfRecord muss gelesen werden. GBIF bleibt nicht automatisch die ursprüngliche Quelle.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit11/unit11-02_gbif.html
https://www.gbif.org/

## 08 · Welche Felder brauchen wir heute?

Zeitfenster: Minute 22–23 (1 Minuten).

Die sechs Gruppen kurz anreißen. Nicht alle GBIF-Spalten im Plenum erklären. Für den Praxisweg sind Kennung, Taxon, Zeitpunkt, Koordinaten, Unsicherheit, Herkunft und Prüfhinweise zentral.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit11/unit11-02_gbif.html

## 09 · Kurz prüfen: Was zeigt eine Punktkarte?

Zeitfenster: Minute 22–23 (1 Minuten).

30 Sekunden zu zweit: Die Aussage bewerten. Danach Handzeichen für „belegt“, „nicht belegt“ oder „unsicher“. Noch nicht ausführlich auflösen; die Aussage am Ende mit dem Qualitätslayer erneut aufgreifen.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit11/unit11-01_punktdaten.html

## 10 · Die Karte zeigt dokumentierte Nachweise

Zeitfenster: Minute 22–23 (1 Minuten).

Knapp auflösen: Die Punkte belegen Records in der gewählten Auswahl. Fehlende Punkte können fehlende Beobachtung oder fehlende Meldung bedeuten. Die genauere Formulierung folgt in Minute 83. Diese Folie höchstens 30 Sekunden zeigen.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit11/unit11-01_punktdaten.html

## 11 · QGIS-Wiedereinstieg nach der Pause

Zeitfenster: Minute 23–26 (3 Minuten).

QGIS öffnen lassen und vier Elemente per Handzeichen oder Zuruf wiederholen: Browser, Layerfenster, Kartenfenster und Projekt-CRS. Die Abbildung stammt aus Unit 10. Keine vollständige Wiederholung der Oberfläche.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/material/qgis-kernpfade.html#unit11
Bild: assets/images/unit10/qgis-oberflaeche.svg

## 12 · Projekt anlegen und Basis laden

Zeitfenster: Minute 26–28 (2 Minuten).

Alle führen die drei Schritte gleichzeitig aus. Wenn ein Pfad scheitert, Paketordner prüfen und nicht frei im Dateisystem suchen lassen. Das Untersuchungsgebiet ist ein didaktisches Rechteck und keine Verwaltungsgrenze.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit11/unit11-03_punkte_qgis.html
https://geomoer.github.io/moer-bsc-geodaten/material/qgis-kernpfade.html#unit11

## 13 · Woher kommen die heutigen 79 Records?

Zeitfenster: Minute 28–30 (2 Minuten).

Den Ablauf von links nach rechts lesen. Der Kurs nutzt einen dokumentierten API-Snapshot ohne eigenen Download-DOI. Der DOI 10.15468/uc1apo gehört zum Quelldatensatz NABU|naturgucker. Eine eigene GBIF-Occurrence-Auswahl würde einen separaten DOI erhalten.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit11/unit11-02_gbif.html
Bild: assets/images/unit11/gbif-workflow.svg
https://doi.org/10.15468/uc1apo

## 14 · CSV zuerst als Tabelle lesen

Zeitfenster: Minute 30–33 (3 Minuten).

Die Datei nicht in einer Tabellenkalkulation speichern oder verändern. Gemeinsam Kopfzeile und erste Zeile lesen. Die leere occurrenceID ist zulässig; gbifID dient als Kennung. Koordinaten liegen in Dezimalgrad vor. CSV und CSVT bleiben nebeneinander.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit11/unit11-03_punkte_qgis.html

## 15 · Textdatei als Punktlayer importieren

Zeitfenster: Minute 33–37 (4 Minuten).

Den Dialog am Beamer schrittweise zeigen und genug Zeit zum Nachvollziehen lassen. Die Abbildung entspricht dem Kursweg. Wichtig: x und y nicht vertauschen; das Geometrie-CRS beschreibt die Koordinaten in der Datei.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit11/unit11-03_punkte_qgis.html
Bild: assets/images/unit11/qgis-csv-import.svg

## 16 · Vier Importangaben müssen zusammenpassen

Zeitfenster: Minute 37–40 (3 Minuten).

Die vier Angaben per Zuruf kontrollieren. EPSG:4326 ist das CRS der Eingangskoordinaten; das Projekt bleibt EPSG:25832. QGIS transformiert die Anzeige zunächst dynamisch. Den temporären Layer gbif_feuersalamander_raw nennen.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit11/unit11-03_punkte_qgis.html

## 17 · Erstkontrolle nach dem Import

Zeitfenster: Minute 40–43 (3 Minuten).

Nicht sofort weiterarbeiten. Zuerst Anzahl, Lage und Attribute kontrollieren. Erwartet werden 79 Records innerhalb beziehungsweise nahe dem Untersuchungsrechteck. Bei Punkten im Meer oder außerhalb Europas zuerst x/y und EPSG:4326 prüfen.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit11/unit11-03_punkte_qgis.html

## 18 · Was bedeutet Koordinatenunsicherheit?

Zeitfenster: Minute 43–47 (4 Minuten).

Die Grafik erneut fachlich lesen: Der gespeicherte Punkt ist eine Lageangabe. Der Unsicherheitsbereich beschreibt, wo der tatsächliche Ort im Rahmen der Angabe liegen kann. Er ist weder Symbolgröße noch Lebensraum. 0 m wird für die Kursauswahl nicht als belastbare Angabe akzeptiert.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit11/unit11-02_gbif.html
Bild: assets/images/unit11/punkt-beobachtung-unsicherheit.svg

## 19 · Eine Qualitätsregel braucht eine Begründung

Zeitfenster: Minute 47–51 (4 Minuten).

Grenzwerte sind keine universellen Naturgesetze. Für die kleinräumige Kursaufgabe wird eine dokumentierte, positive Unsicherheit bis 100 m verlangt. Andere Fragestellungen können eine andere Schwelle erfordern. Die Originaldaten werden nicht gelöscht.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit11/unit11-03_punkte_qgis.html

## 20 · Auswahl mit einem Ausdruck

Zeitfenster: Minute 51–55 (4 Minuten).

Attributtabelle öffnen und „Objekte über Ausdruck wählen“ verwenden. Den Ausdruck genau übernehmen. NULL-Werte erfüllen beide Bedingungen nicht. Die Auswahl bleibt sichtbar und kontrollierbar; noch nichts exportieren.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit11/unit11-03_punkte_qgis.html

## 21 · Prüfwert: 56 ausgewählt, 23 ausgeschlossen

Zeitfenster: Minute 55–58 (3 Minuten).

Ergebnis per Handzeichen abfragen, dann zeigen. Bei Abweichung nicht improvisiert weiterexportieren: Feldtyp, Ausdruck und Gesamtzahl prüfen. Im Snapshot besitzen die 23 ausgeschlossenen Records jeweils 250 m Unsicherheit.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit11/unit11-03_punkte_qgis.html

## 22 · Flags und fehlende Werte nicht pauschal behandeln

Zeitfenster: Minute 58–60 (2 Minuten).

Drei Fehlannahmen vermeiden. GBIF-Issues sind Prüfhinweise und müssen fachlich gelesen werden. Ein fehlender Unsicherheitswert ist nicht 0 m. Ein leerer Issue-Eintrag beweist nicht Fehlerfreiheit.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit11/unit11-02_gbif.html

## 23 · Partnercheck vor dem Export

Zeitfenster: Minute 60–62 (2 Minuten).

Je zwei Nachbarinnen oder Nachbarn vergleichen ihren Zustand. In der großen Gruppe nur die drei Kontrollpunkte prüfen. Wer fertig ist, hilft beim Lesen der Werte; keine zusätzliche Analyse beginnen.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit11/unit11-03_punkte_qgis.html

## 24 · Auswahl exportieren – Rohdaten erhalten

Zeitfenster: Minute 62–64 (2 Minuten).

Klarstellen: Es werden nur ausgewählte Features in einen neuen Layer geschrieben. Der Rohdatenlayer bleibt unverändert und kann die Entscheidung später nachvollziehbar machen.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit11/unit11-03_punkte_qgis.html

## 25 · GeoPackage und Layer eindeutig benennen

Zeitfenster: Minute 64–68 (4 Minuten).

Rechtsklick auf den Rohdatenlayer: Exportieren → Ausgewählte Objekte speichern als. Den Haken für nur ausgewählte Objekte kontrollieren. Die Datei im Ordner data_output erzeugen; Layername exakt gbif_checked.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit11/unit11-03_punkte_qgis.html
https://geomoer.github.io/moer-bsc-geodaten/material/qgis-kernpfade.html#unit11

## 26 · Beim Export wird wirklich transformiert

Zeitfenster: Minute 68–71 (3 Minuten).

An Unit 09 anknüpfen: Die Eingangszahlen werden als EPSG:4326 interpretiert. Beim Export nach EPSG:25832 berechnet QGIS neue Koordinaten. Nur ein anderes CRS zuzuweisen wäre falsch. Das Projekt-CRS allein ändert die gespeicherten Quelldaten nicht.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit11/unit11-03_punkte_qgis.html

## 27 · Neu laden und Ergebnis kontrollieren

Zeitfenster: Minute 71–75 (4 Minuten).

Den neu erzeugten Layer aus dem Browser laden, den temporären Rohdatenlayer deaktivieren und das Projekt speichern. Erwartet werden 56 Punkte. Wenn Export scheitert, den Ersatzlayer ersatz/unit11_results.gpkg · gbif_checked laden und den Fehler dokumentieren.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit11/unit11-03_punkte_qgis.html
https://geomoer.github.io/moer-bsc-geodaten/material/qgis-kernpfade.html#unit11

## 28 · Die Qualitätsentscheidung dokumentieren

Zeitfenster: Minute 75–78 (3 Minuten).

Die Gruppe nennt die Angaben, die eine andere Person zum Nachvollziehen braucht. Anschließend die Liste zeigen. Der Datensatz-DOI ist nicht als eigener GBIF-Download-DOI auszugeben.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit11/unit11-03_punkte_qgis.html
https://doi.org/10.15468/uc1apo

## 29 · Viele Punkte können viel Suchaufwand bedeuten

Zeitfenster: Minute 78–81 (3 Minuten).

Die beiden Suchsituationen vergleichen lassen. Das Gedankenexperiment isoliert den Einfluss des Suchaufwands; in realen Daten sind unentdeckte Vorkommen unbekannt. Eine hohe Punktdichte kann häufiges Vorkommen, gute Zugänglichkeit oder aktive Meldung widerspiegeln.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit11/unit11-02_gbif.html
Bild: assets/images/unit11/beobachtungsbias.svg

## 30 · Die Ausgangsaussage erneut bewerten

Zeitfenster: Minute 81–83 (2 Minuten).

Noch einmal 45 Sekunden zu zweit formulieren lassen: Was ist an der Aussage zu stark? Danach zwei bis drei Vorschläge hören. Die Qualitätsauswahl verbessert die dokumentierte Lagegenauigkeit, erzeugt aber keine systematische Verbreitungserhebung.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit11/unit11-02_gbif.html

## 31 · Eine vorsichtige Kartenaussage

Zeitfenster: Minute 83–85 (2 Minuten).

Die Formulierung laut lesen. Auf die drei Einschränkungen hinweisen: dokumentierte Records, konkreter Datenausschnitt und angewandte Qualitätsregel. Fehlende Punkte dürfen ohne dokumentierte Suche und Erfassungswahrscheinlichkeit nicht als Abwesenheit interpretiert werden.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit11/unit11-02_gbif.html

## 32 · Exit Ticket · eine Frage auswählen

Zeitfenster: Minute 85–88 (3 Minuten).

Genau eine der drei Fragen auswählen und sichtbar markieren. Zwei Minuten einzeln schreiben lassen, anschließend höchstens eine knappe Antwort einsammeln. Nicht alle drei Fragen bearbeiten lassen.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit11/unit11-00_overview.html

## 33 · Nachbereitung · JiTT zu Unit 11

Zeitfenster: Minute 88–90 (2 Minuten).

Nur die JiTT-Aufgabe als verbindliche Nachbereitung nennen. Fragen, Frist und endgültiger Link stehen in ILIAS. Der Link auf der Kursseite ist noch ein sichtbarer Platzhalter; keinen Wert erfinden. Kurz ankündigen, dass gbif_checked in Unit 12 weiterverwendet wird.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit11/unit11-04_assignment.html

## 34 · GBIF-Felder als Lesehilfe

Reserve; nicht zusätzlich in die 90 Minuten einplanen.

Nur bei Rückfragen verwenden. Die Tabelle ist keine zusätzliche Pflichtphase. Zeigen, dass technische Felder jeweils eine fachliche Prüffrage unterstützen.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit11/unit11-02_gbif.html

## 35 · Quellen und Arbeitsstand

Reserve; nicht zusätzlich in die 90 Minuten einplanen.

Nur bei Bedarf zeigen. Die Folie dokumentiert Kursseiten, Softwaredokumentation und Datenquelle. Die Live-Erreichbarkeit externer Seiten ist für den Präsenzkern nicht erforderlich.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit11/unit11-00_overview.html

## 36 · Vielen Dank für Ihre Aufmerksamkeit

Abschluss nach der Nachbereitung; kein zusätzlicher Zeitblock.

Die Sitzung mit dieser Folie beenden. Die Abschlussgestaltung nutzt den Kontakt-Master der universitären Vorlage sowie das originale Foto-/Kartenmotiv aus der FB19-Titelseite.

Quellen / Anschluss an die HTML-Lernumgebung:
/home/dirk/GeoMOER/moer-bsc-geodaten/docs/slides/Vorlagen/präs_ms02_powerpoint_de.pptx

