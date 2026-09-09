---
title: Punktdaten in QGIS
published: true
toc: true
header:
  image: /assets/images/unit11/hero-unit11.jpg
  image_description: "Wald- und Kulturlandschaft mit verteilten Beobachtungspunkten und angedeuteten Unsicherheitsbereichen"
  caption: "KI-generierte Illustration, bearbeitet für diesen Kurs"
---

<!-- Introtext: Eine tabellarische GBIF-Auswahl kontrolliert in einen Punktlayer überführen. -->

> **Verbindlicher Praxisweg:** Die [QGIS-Kurzcheckliste für Unit 11]({{ '/material/qgis-kernpfade.html#unit11' | relative_url }}) bündelt Import, Qualitätsauswahl, Export und Kontrolle. Weitere Filter und Symbolisierungen sind freiwillige Vertiefung.

## Von der Tabelle zur Karte

Der vorbereitete GBIF-Datensatz enthält für jeden Nachweis eine Tabellenzeile. Die Spalten `decimalLongitude` und `decimalLatitude` beschreiben die räumliche Position. QGIS kann daraus Punktgeometrien erzeugen.

Für einen korrekten Import müssen wir eindeutig festlegen:

* welches Zeichen die Spalten trennt,
* welche Spalte die x-Koordinate enthält,
* welche Spalte die y-Koordinate enthält und
* in welchem CRS die Koordinaten gespeichert sind.

Für die GBIF-Koordinaten dieser Übung gilt:

| Einstellung | Wert |
|---|---|
| x-Feld | `decimalLongitude` |
| y-Feld | `decimalLatitude` |
| Koordinateneinheit | Dezimalgrad |
| Geometrie-CRS | WGS 84 – `EPSG:4326` |

> **Merksatz:** Beim Import wird das CRS der vorhandenen Koordinaten angegeben – nicht das CRS, das später für die Karte oder Analyse gewünscht ist.

## Arbeitsordner vorbereiten

Verwenden Sie den entpackten Ordner aus dem [Marburger Übungspaket und Anleitung]({{ '/material/marburg.html' | relative_url }}). Speichern Sie das neue Projekt im Hauptordner:

```text
marburg_geodaten/
  data_raw/
  data_output/
  documentation/
  unit11_punktdaten.qgz
```

* `data_raw` enthält den unveränderten GBIF-Download oder die bereitgestellte Teilmenge.
* `data_output` enthält von Ihnen erzeugte Geodaten.
* `documentation` enthält Quelldatensatz-DOI, Zitation, Filterbeschreibung und eigene Bearbeitungsnotizen.

Verändern Sie die Originaldatei in `data_raw` nicht. Korrekturen und Ausschlüsse werden in einer neuen Datei beziehungsweise einem neuen Layer gespeichert.

## Datensatz vor dem Import prüfen

Öffnen Sie die bereitgestellte Textdatei zunächst in einem Texteditor oder einer Tabellenansicht und prüfen Sie:

* Wie heißt die Datei?
* Welches Zeichen trennt die Spalten: Tabulator, Komma oder Semikolon?
* Besitzt die erste Zeile eindeutige Spaltennamen?
* Werden Dezimalzahlen mit einem Punkt geschrieben?
* Sind `decimalLongitude` und `decimalLatitude` vorhanden?
* Sind fehlende Werte leer oder durch einen bestimmten Code gekennzeichnet?
* Welche der auf der GBIF-Seite besprochenen Attribute sind enthalten?

GBIF stellt einfache Occurrence-Downloads häufig als tabulatorgetrennte Textdaten bereit. Die für den Kurs vorbereitete Datei kann jedoch bereits als kleinere CSV-Datei vorliegen. Entscheidend ist deshalb die tatsächliche Struktur der bereitgestellten Datei.

## Neues QGIS-Projekt anlegen

1. Starten Sie QGIS.
2. Erstellen Sie ein neues Projekt.
3. Speichern Sie es als `unit11_punktdaten.qgz` im Arbeitsordner.
4. Stellen Sie das seit Unit 10 verwendete Projekt-CRS ein: `EPSG:25832`.
5. Laden Sie aus `data_raw/marburg_basis.gpkg` den Layer `untersuchungsgebiet`. Er zeigt das didaktische Untersuchungsrechteck, keine Verwaltungsgrenze.

Der Grenzlayer hilft, die Lage der importierten Punkte unmittelbar auf Plausibilität zu prüfen.

## Textdatei als Punktlayer importieren

### 1. Datenquellenmanager öffnen

Öffnen Sie den **Datenquellenmanager** und wählen Sie **Getrennte Texte** beziehungsweise **Delimited Text**.

### 2. Datei und Zeichencodierung wählen

1. Wählen Sie `data_raw/gbif_feuersalamander_marburg.csv` aus. Lassen Sie die gleichnamige CSVT-Datei daneben liegen.
2. Verwenden Sie, sofern nicht anders angegeben, `UTF-8` als Zeichencodierung.
3. Wählen Sie **Komma** als Trennzeichen und aktivieren Sie die Erkennung der Feldtypen. Koordinaten und `coordinateUncertaintyInMeters` müssen Dezimalzahlen sein; `gbifID` und `occurrenceID` sind Kennungen.
4. Prüfen Sie in der Vorschau, ob jede Variable in einer eigenen Spalte erscheint.

Wenn die gesamte Zeile in einer einzigen Spalte steht, wurde sehr wahrscheinlich das falsche Trennzeichen gewählt.

### 3. Geometrie definieren

Wählen Sie **Punktkoordinaten** und tragen Sie ein:

* x-Feld: `decimalLongitude`
* y-Feld: `decimalLatitude`
* Geometrie-CRS: `EPSG:4326`

Prüfen Sie nochmals, dass Länge und Breite nicht vertauscht sind.

### 4. Layer hinzufügen

Fügen Sie die Datei als Layer zum Projekt hinzu. Geben Sie dem Layer einen eindeutigen Anzeigenamen, beispielsweise:

> `gbif_feuersalamander_raw`

Zoomen Sie anschließend auf die Layerausdehnung.

## Lage der Punkte prüfen

Vergleichen Sie die Punkte mit dem Grenzlayer und beantworten Sie:

* Liegt die Mehrzahl der Punkte im erwarteten Untersuchungsgebiet?
* Gibt es Punkte bei `(0, 0)` oder weit außerhalb des Gebietes?
* Liegen auffällig viele Punkte exakt auf demselben Ort?
* Passt die räumliche Ausdehnung zum verwendeten GBIF-Filter?
* Werden Punkte durch den Grenzlayer oder einen anderen Layer verdeckt?

Ein einzelner weit entfernter Punkt kann die Layerausdehnung stark vergrößern. Untersuchen Sie solche Features über Karte und Attributtabelle, bevor Sie eine Entscheidung treffen.

> **Wichtig:** Entfernen Sie auffällige Records nicht direkt aus dem Rohdatensatz. Identifizieren Sie sie über `gbifID` und dokumentieren Sie Ihre Beurteilung.

## Attribute untersuchen

Öffnen Sie die Attributtabelle und prüfen Sie mindestens:

* Anzahl der Records,
* `gbifID` und `occurrenceID`,
* `scientificName` und `species`,
* `basisOfRecord`,
* `eventDate` beziehungsweise `year`,
* `decimalLongitude` und `decimalLatitude`,
* `coordinateUncertaintyInMeters`,
* `datasetKey`,
* `license` und
* `issue`.

Wählen Sie einige Punkte in der Karte aus und vergleichen Sie die zugehörigen Zeilen. Öffnen Sie insbesondere:

* einen räumlich plausiblen Punkt,
* einen Punkt mit hoher oder fehlender Koordinatenunsicherheit und
* einen Record mit einem Eintrag im Feld `issue`.

## Datensätze mit Ausdrücken auswählen

QGIS kann Features anhand ihrer Attribute auswählen oder den angezeigten Layer filtern. Ein **Ausdruck** beschreibt die gewünschte Bedingung.

### Fehlende Koordinaten finden

```text
"decimalLongitude" IS NULL OR "decimalLatitude" IS NULL
```

### Records ab dem Jahr 2000 auswählen

```text
"year" >= 2000
```

### Records mit Qualitätsflags finden

```text
"issue" IS NOT NULL AND "issue" != ''
```

### Records mit angegebener Koordinatenunsicherheit auswählen

```text
"coordinateUncertaintyInMeters" IS NOT NULL
```

Die genaue Feldbezeichnung und der erkannte Datentyp müssen zum bereitgestellten Datensatz passen. Wird `year` fälschlich als Text eingelesen, kann ein numerischer Vergleich zu unerwarteten Ergebnissen führen.

> **Auswahl ist nicht Löschung:** Eine Auswahl markiert Features. Ein Filter beeinflusst die Anzeige. Erst ein Export kann daraus einen neuen dauerhaft gespeicherten Teildatensatz erzeugen.

## Eine Qualitätsentscheidung dokumentieren

Für den gemeinsamen räumlichen Vergleich verwenden wir die Regel:

```text
"coordinateUncertaintyInMeters" > 0 AND "coordinateUncertaintyInMeters" <= 100
```

Damit wählen wir 56 der 79 Records aus; 23 Records mit 250 m angegebener Unsicherheit bleiben im Original erhalten. Die Schwelle ist eine begründbare Übungsentscheidung, kein allgemeingültiger Qualitätsstandard. Die vorhandenen Qualitätsflags werden besprochen und nicht pauschal als Ausschlussgrund verwendet. Weitere Regeln in der folgenden Tabelle sind freiwillige Vertiefung.

Definieren Sie vor einem Ausschluss nachvollziehbare Regeln. Ein einfaches Prüfprotokoll kann so aussehen:

| Regel | betroffene Records | Entscheidung | Begründung |
|---|---:|---|---|
| Koordinaten fehlen |  |  |  |
| Position außerhalb des Untersuchungsgebietes |  |  |  |
| Koordinatenunsicherheit fehlt |  |  |  |
| Koordinatenunsicherheit überschreitet Grenzwert |  |  |  |
| GBIF-Issue vorhanden |  |  |  |
| möglicher doppelter Record |  |  |  |

Ein fehlender Unsicherheitswert ist nicht gleichbedeutend mit geringer Unsicherheit. Ebenso bedeutet ein vorhandenes Issue nicht automatisch, dass der Record ausgeschlossen werden muss.

## Punkte symbolisieren

Für eine erste Karte genügt eine einfache, gut sichtbare Punktsymbolisierung.

1. Öffnen Sie die Layerdarstellung.
2. Wählen Sie eine kontrastreiche Farbe.
3. Stellen Sie eine angemessene Symbolgröße ein.
4. Verwenden Sie gegebenenfalls eine leichte Transparenz, damit überlagerte Punkte erkennbar bleiben.

Anschließend können Sie testweise nach einem Attribut kategorisieren, beispielsweise:

* `basisOfRecord` oder
* gruppiertem Zeitraum.

Verwenden Sie nicht zu viele Kategorien. Die Symbolisierung soll eine konkrete Frage unterstützen und darf nicht den Eindruck erwecken, die Symbolfläche entspreche der tatsächlichen Ausdehnung eines Vorkommens.

## Gefilterte Records als GeoPackage speichern

Der importierte Textlayer verweist weiterhin auf die Ausgangsdatei. Speichern Sie den für die weitere Arbeit vorgesehenen Punktlayer deshalb als GeoPackage.

1. Wählen beziehungsweise filtern Sie die Records nach den für die Übung festgelegten Kriterien.
2. Öffnen Sie im Kontextmenü des Layers **Exportieren → Objekte speichern als**.
3. Wählen Sie das Format **GeoPackage**.
4. Speichern Sie die Datei als `data_output/unit11_results.gpkg`.
5. Verwenden Sie den verbindlichen Layernamen `gbif_checked`.
6. Verwenden Sie das gemeinsame Ausgabe-CRS: `EPSG:25832`.
7. Prüfen Sie, ob nur ausgewählte Features oder alle aktuell gefilterten Features exportiert werden sollen.
8. Fügen Sie den gespeicherten Layer dem Projekt hinzu.

Deaktivieren Sie anschließend testweise den Rohdatenlayer. Der neue GeoPackage-Layer sollte weiterhin sichtbar und vollständig nutzbar sein.

Das Import-CRS `EPSG:4326` beschreibt die vorhandenen Tabellenkoordinaten. Das Ausgabe-CRS beschreibt dagegen die exportierte Geometrie. Eine Transformation muss bewusst gewählt und dokumentiert werden; ein CRS darf nicht nur neu zugewiesen werden.

## Quelle und Verarbeitung dokumentieren

Speichern Sie im Ordner `documentation` eine kurze Textdatei mit:

* Quelldatensatz-DOI `10.15468/uc1apo`, Quellenangabe und Hinweis auf den API-Snapshot ohne eigenen Download-DOI,
* Datum des Zugriffs,
* ursprünglichem Dateinamen,
* verwendeten GBIF-Filtern,
* CRS der Ausgangskoordinaten,
* Anzahl der importierten Records,
* angewendeten Qualitätsregeln,
* Anzahl ausgeschlossener Records,
* Ausgabeformat und Ausgabe-CRS sowie
* Namen des erzeugten GeoPackage-Layers.

Damit bleibt nachvollziehbar, wie aus dem GBIF-Download der verwendete Punktlayer entstanden ist.

## Kleine Forschungsfrage

Untersuchen Sie mit dem erzeugten Layer:

> **Wo wurden Feuersalamander im gewählten Gebiet und Zeitraum dokumentiert?**

Beschreiben Sie:

* erkennbare räumliche Schwerpunkte,
* größere Gebiete ohne Records,
* mögliche Einflüsse von Städten, Wegen oder Beobachtungsaktivität und
* Grenzen der Interpretation.

Formulieren Sie das Ergebnis als Beschreibung der **dokumentierten Nachweise**, nicht als vollständige Verbreitungskarte.

## Typische Probleme

| Problem | mögliche Ursache | erster Prüfschritt |
|---|---|---|
| gesamte Zeile erscheint in einer Spalte | falsches Trennzeichen | Dateivorschau und Separator prüfen |
| keine Punktgeometrie entsteht | falsche Geometrieoption oder Koordinatenfelder | Punktkoordinaten sowie x/y prüfen |
| Punkte liegen an falscher Stelle | x/y vertauscht oder falsches Import-CRS | `decimalLongitude`, `decimalLatitude` und EPSG:4326 prüfen |
| Punkte erscheinen vor Westafrika | fehlende Werte wurden als `(0, 0)` interpretiert | entsprechende Tabellenzeilen prüfen |
| Jahresfilter funktioniert nicht | Feld wurde als Text importiert | erkannten Datentyp kontrollieren |
| sehr großer Kartenausschnitt | einzelner Ausreißer liegt weit entfernt | auf Auswahl zoomen und Record prüfen |
| exportierter Layer enthält zu viele oder zu wenige Punkte | Auswahl- beziehungsweise Filteroption falsch | Exportdialog und Recordzahl prüfen |

## Zusammenfassung

* Koordinatenhaltige Textdateien können in QGIS als Punktlayer geladen werden.
* Für GBIF-Daten gilt `decimalLongitude` als x, `decimalLatitude` als y und WGS 84 (`EPSG:4326`) als CRS der geographischen Koordinaten.
* Trennzeichen, Datentypen, fehlende Werte, Lage und CRS müssen beim Import geprüft werden.
* Karte und Attributtabelle sind miteinander verknüpft und ermöglichen die Untersuchung einzelner Records.
* Auswahlen und Filter müssen von dauerhaften Datenänderungen unterschieden werden.
* Qualitätsentscheidungen werden regelbasiert getroffen und dokumentiert.
* Ein GeoPackage speichert den geprüften Punktlayer dauerhaft für die weitere Arbeit.
* Die Karte beschreibt dokumentierte Nachweise, nicht automatisch die vollständige Artverbreitung.

## Weiterführende Informationen

* [QGIS: Getrennte Textdateien und Koordinatenfelder](https://docs.qgis.org/latest/en/docs/user_manual/managing_data_source/supported_data.html#delimited-text-files)
* [QGIS: Daten öffnen](https://docs.qgis.org/latest/en/docs/user_manual/managing_data_source/opening_data.html)
* [QGIS: Vektorlayer in einem anderen CRS speichern](https://docs.qgis.org/latest/en/docs/training_manual/vector_analysis/reproject_transform.html)

<!-- Notizen: Ab hier folgen Vermerke, welche als Gedankenstütze oder Erinnerung dienen, aber noch nicht in der vorhandenen Form veröffentlicht werden sollen. -->

<!--
Vor Durchführung ergänzen:
- bereitgestellte GBIF-Datei und tatsächliches Trennzeichen
- Grenzlayer
- Projekt- und Ausgabe-CRS
- konkrete Qualitätsregeln und gegebenenfalls Grenzwert für coordinateUncertaintyInMeters
- erwartete Recordzahlen vor und nach dem Filter
- Hintergrundkarte beziehungsweise WMS

Benötigte Screenshots:
- Delimited-Text-Dialog mit x/y und EPSG:4326
- Punktlayer über Deutschlandgrenze
- Attributtabelle mit wichtigen GBIF-Feldern
- Ausdrucksdialog
- Export als GeoPackage

Didaktisch wichtig:
- Rohdaten unverändert lassen.
- Fehlen von coordinateUncertaintyInMeters nicht als Unsicherheit von null interpretieren.
- vorhandenes Issue nicht pauschal mit Ausschluss gleichsetzen.
- Recordzahlen nur in Aufgabenlösung, nicht dauerhaft im allgemeinen Erklärungstext festschreiben.

Anschluss an unit11-04_assignment.md:
- Zur Nachbereitung ausschließlich auf die JiTT-Fragen zu Unit 11 in ILIAS verweisen.
-->
