---
title: HA | Hausaufgabe Abschnitt 11
published: true
toc: true
header:
  image: /assets/images/unit11/hero-unit11.jpg
  image_description: "Wald- und Kulturlandschaft mit verteilten Beobachtungspunkten und angedeuteten Unsicherheitsbereichen"
  caption: "KI-generierte Illustration, bearbeitet für diesen Kurs"
---

<!-- Hausaufgabe 11: GBIF-Punktdaten importieren, prüfen und interpretieren -->

## Hausaufgabe 11

In dieser Hausaufgabe erstellen Sie aus einer tabellarischen GBIF-Auswahl einen dokumentierten Punktlayer. Sie prüfen die Datenquelle und Tabellenstruktur, importieren die Koordinaten korrekt in QGIS, untersuchen Qualitätsinformationen und speichern eine nachvollziehbar gefilterte Auswahl als GeoPackage.

| Rahmenbedingung | Festlegung |
|---|---|
| Bearbeitungszeit | etwa 90 Minuten |
| Abgabeformat | vollständiger Arbeitsordner als `unit11_nachname_vorname.zip` |
| Abgabeort | `[ILIAS-Ordner beziehungsweise Abgabeort ergänzen]` |
| Abgabetermin | `[Datum und Uhrzeit ergänzen]` |
| Arbeitsform | Einzelarbeit; Projekt, Entscheidungen und Dokumentation müssen selbst erstellt sein. |

## Lernziele

Nach der Bearbeitung können Sie ...

* einen GBIF Occurrence Record fachlich einordnen,
* wichtige Attribute und Qualitätsinformationen eines GBIF-Downloads erklären,
* geographische Koordinaten aus einer Textdatei korrekt als Punkte importieren,
* die räumliche Lage und Attribute einzelner Records prüfen,
* Records anhand dokumentierter Regeln auswählen,
* einen geprüften Punktlayer als GeoPackage speichern und
* eine Punktkarte als Karte dokumentierter Nachweise vorsichtig interpretieren.

## Vorbereitung

Für die Hausaufgabe benötigen Sie:

| Material | Angabe |
|---|---|
| QGIS-Version | `[dieselbe verbindliche QGIS-LTR-Version wie in Unit 10 ergänzen]` |
| GBIF-Teildatensatz | `[Datei und Downloadlink ergänzen]` |
| GBIF-Download-DOI | `[DOI ergänzen]` |
| verwendete GBIF-Filter | `[Filter ergänzen]` |
| Grenzlayer | `[Datei beziehungsweise Layer ergänzen]` |
| Hintergrundkarte / WMS | `[Dienst oder Layer ergänzen]` |
| Projekt-CRS | `[gemeinsamen EPSG-Code ergänzen; für Marburg voraussichtlich EPSG:25832]` |
| Ausgabe-CRS | `[identisch mit dem Projekt-CRS ergänzen]` |
| schemaidentischer Ersatzlayer | `[Downloadlink ergänzen]` |

Legen Sie folgende Ordnerstruktur an:

```text
hausaufgabe11_nachname/
  data_raw/
  data_output/
  documentation/
  hausaufgabe11_nachname.qgz
```

Speichern Sie die bereitgestellten Originaldaten unverändert in `data_raw`.

## Aufgabe 1: Datenquelle dokumentieren

Dokumentieren Sie zunächst den verwendeten GBIF-Download.

| Angabe | Ihre Dokumentation |
|---|---|
| Taxon |  |
| wissenschaftlicher Name |  |
| räumlicher Filter |  |
| zeitlicher Filter |  |
| weitere Filter |  |
| Erstellungs- beziehungsweise Zugriffsdatum |  |
| Download-DOI |  |
| vorgeschlagene Zitation |  |
| enthaltene Lizenz beziehungsweise Lizenzen |  |
| ursprünglicher Dateiname |  |

Erklären Sie anschließend in zwei Sätzen, warum ein Download-DOI für eine wissenschaftliche Nutzung aussagekräftiger ist als ein allgemeiner Link zur GBIF-Startseite.

## Aufgabe 2: Tabelle vor dem Import prüfen

Öffnen Sie die bereitgestellte Datei in einer geeigneten Tabellen- oder Textansicht, ohne die Originaldatei zu verändern.

Ermitteln Sie:

1. verwendetes Trennzeichen,
2. Zeichencodierung, soweit erkennbar,
3. Anzahl der Records,
4. Spalten für Längen- und Breitengrad,
5. Schreibweise der Dezimalzahlen,
6. Kennzeichnung fehlender Werte und
7. Vorhandensein der folgenden Felder:
   * `gbifID`,
   * `scientificName`,
   * `basisOfRecord`,
   * `eventDate` oder `year`,
   * `coordinateUncertaintyInMeters`,
   * `datasetKey`,
   * `license` und
   * `issue`.

Notieren Sie außerdem zwei Attribute, die Sie für die fachliche Interpretation besonders wichtig finden, und begründen Sie Ihre Auswahl.

## Aufgabe 3: Punktlayer in QGIS erzeugen

1. Erstellen und speichern Sie ein neues QGIS-Projekt im Arbeitsordner.
2. Stellen Sie das vorgegebene Projekt-CRS ein.
3. Laden Sie den Grenzlayer und gegebenenfalls die vorgegebene Hintergrundkarte.
4. Öffnen Sie den Datenquellenmanager für getrennte Textdateien.
5. Wählen Sie Datei, Zeichencodierung und korrektes Trennzeichen.
6. Definieren Sie die Geometrie mit:
   * x = `decimalLongitude`,
   * y = `decimalLatitude`,
   * CRS = WGS 84 (`EPSG:4326`).
7. Fügen Sie den Punktlayer hinzu und nennen Sie ihn `gbif_raw`.
8. Zoomen Sie auf die Layerausdehnung.
9. Speichern Sie das Projekt.

Erstellen Sie einen Screenshot, auf dem Punktlayer, Grenzlayer und Layer-Bereich sichtbar sind.

## Aufgabe 4: Qualität prüfen

Untersuchen Sie Karte und Attributtabelle. Füllen Sie das Prüfprotokoll aus.

| Prüfregel | Anzahl betroffener Records | verwendeter Ausdruck / Vorgehen | Bewertung |
|---|---:|---|---|
| Koordinaten fehlen |  |  |  |
| Punkt liegt außerhalb des erwarteten Gebietes |  |  |  |
| `(0, 0)` oder vergleichbarer Platzhalter |  |  |  |
| Koordinatenunsicherheit fehlt |  |  |  |
| Koordinatenunsicherheit über `[Grenzwert ergänzen]` m |  |  |  |
| GBIF-Issue vorhanden |  |  |  |
| Beobachtungsjahr vor `[Jahr ergänzen]` |  |  |  |
| möglicher doppelter Nachweis |  |  |  |

Wählen Sie drei auffällige Records aus und dokumentieren Sie jeweils:

* `gbifID`,
* Art des Problems,
* weitere geprüfte Attribute,
* Entscheidung und
* Begründung.

> **Wichtig:** Ein fehlender Unsicherheitswert bedeutet nicht null Meter Unsicherheit. Ein GBIF-Issue führt nicht automatisch zum Ausschluss. Begründen Sie jede Regel fachlich.

## Aufgabe 5: Geprüften Layer speichern

Erstellen Sie eine Auswahl beziehungsweise einen Filter nach den vorgegebenen Kriterien:

* gültige und vorhandene Koordinaten,
* Position im vorgesehenen Untersuchungsgebiet,
* Beobachtungsjahr ab `[Jahr ergänzen]`,
* Koordinatenunsicherheit nach der festgelegten Regel und
* weitere begründete Entscheidungen aus Aufgabe 4.

Exportieren Sie die resultierenden Features:

* Format: **GeoPackage**
* Datei: `data_output/unit11_results.gpkg`
* Layername: `gbif_checked`
* CRS: `[gemeinsames Ausgabe-CRS ergänzen]`

Prüfen Sie nach dem Export:

* Anzahl der Features im neuen Layer,
* Vorhandensein von `gbifID`,
* CRS des Layers,
* räumliche Lage und
* Unterschied zur Anzahl der Rohdatenrecords.

Dokumentieren Sie, wie viele Records ausgeschlossen wurden und aufgrund welcher Regeln.

## Aufgabe 6: Punkte darstellen und interpretieren

Symbolisieren Sie den geprüften Layer so, dass die Punkte vor dem Hintergrund gut lesbar sind. Verwenden Sie zusätzlich genau eine sinnvolle Unterscheidung, beispielsweise:

* Kategorien nach `basisOfRecord` oder
* zwei bis vier Zeiträume auf Grundlage von `year`.

Erstellen Sie einen zweiten Screenshot der fertigen Darstellung.

Beantworten Sie anschließend in insgesamt fünf bis acht Sätzen:

1. Wo konzentrieren sich die dokumentierten Nachweise?
2. Welche Gebiete enthalten wenige oder keine Records?
3. Welche Rolle könnten Zugänglichkeit, Siedlungen oder Beobachtungsaktivität spielen?
4. Warum darf die Karte nicht ohne Weiteres als vollständige Verbreitungskarte bezeichnet werden?
5. Welche zusätzlichen Daten wären nötig, um Aussagen über Abwesenheit zu treffen?

Formulieren Sie außerdem eine fachlich angemessene Kartenüberschrift oder Bildunterschrift.

## Aufgabe 7: Verarbeitung dokumentieren

Erstellen Sie im Ordner `documentation` eine Textdatei `processing_notes.md` mit:

* Name der bearbeitenden Person,
* Datum der Bearbeitung,
* GBIF-Download-DOI und Zitation,
* Eingangsdaten und Recordzahl,
* Importparameter einschließlich x, y und CRS,
* angewendeten Qualitäts- und Filterregeln,
* ausgeschlossenen Recordzahlen,
* Ausgabeformat, Layername und CRS sowie
* kurzer Beschreibung der Darstellung.

## Einzureichende Ergebnisse

Reichen Sie den vollständigen Arbeitsordner als `unit11_nachname_vorname.zip` ein. Er enthält mindestens:

1. `hausaufgabe11_nachname.qgz`,
2. `data_output/unit11_results.gpkg` mit dem Layer `gbif_checked`,
3. `processing_notes.md`,
4. ausgefüllte Tabellen und Antworten sowie
5. beide Screenshots.

Öffnen Sie das ZIP-Archiv probeweise und kontrollieren Sie Ordnerstruktur, Dateinamen und Projektpfade. Die bereitgestellte GBIF-Teilmenge soll im Ordner `data_raw` enthalten bleiben.

<!-- Je nach Kursplattform als einzelne Dateien oder gesamter Arbeitsordner als ZIP abgeben lassen. Die unveränderte GBIF-Rohdatei muss bei zentral bereitgestellten Daten nicht erneut eingereicht werden. -->

## Abgabecheck

Prüfen Sie vor der Abgabe, ob ...

* die Originaldaten unverändert erhalten sind,
* GBIF-Download-DOI, Filter, Lizenz und Zitation dokumentiert sind,
* `decimalLongitude` als x und `decimalLatitude` als y verwendet wurden,
* beim Import `EPSG:4326` angegeben wurde,
* räumliche Ausreißer und Qualitätsfelder geprüft wurden,
* Ausschlussregeln und betroffene Recordzahlen nachvollziehbar sind,
* der geprüfte Layer als GeoPackage vorliegt,
* `gbifID` im Ergebnis erhalten ist,
* die Karte von dokumentierten Nachweisen und nicht pauschal von Verbreitung spricht und
* das QGIS-Projekt nach erneutem Öffnen funktioniert.

## Bewertung

Die Hausaufgabe wird anhand von **50 Punkten** bewertet.

| Bereich | Punkte | vollständig erfüllt, wenn ... |
|---|---:|---|
| Quelle und Tabellenprüfung | 10 | DOI, Filter, Zitation, Lizenz, Struktur und zentrale Felder sind nachvollziehbar dokumentiert. |
| Punktimport | 8 | `decimalLongitude` ist x, `decimalLatitude` ist y und das Import-CRS ist `EPSG:4326`; Lage und Anzahl werden geprüft. |
| Qualitätsprüfung | 12 | Regeln, betroffene Records, auffällige Beispiele und Entscheidungen sind fachlich begründet. |
| Export `gbif_checked` | 8 | Ergebnis, Featurezahl, Felder und gemeinsames Ausgabe-CRS sind korrekt und kontrolliert. |
| Darstellung und Interpretation | 7 | Darstellung ist lesbar; Beobachtungsbias und fehlende Absenzdaten werden berücksichtigt. |
| Reproduzierbarkeit und Abgabe | 5 | Projekt, Daten, `processing_notes.md`, Screenshots und ZIP-Struktur sind vollständig und funktionieren. |

Für das Bestehen sind **`[Mindestpunktzahl ergänzen, Vorschlag: 25 von 50 Punkten]`** erforderlich. Fachlich gleichwertige Entscheidungen sind zulässig, wenn sie dokumentiert und begründet sind. Folgefehler werden nicht mehrfach bewertet.

<!-- Lösungshinweise für Lehrende:

Aufgabe 1:
- DOI verweist auf eine persistente, zeitlich festgehaltene Auswahl und ermöglicht die Anerkennung der enthaltenen Datenquellen.
- Allgemeine GBIF- oder Suchlinks können dynamische Inhalte zeigen und ersetzen die konkrete Downloadzitation nicht.

Aufgabe 2:
- erwartete Werte und Felder anhand der tatsächlich bereitgestellten Datei ergänzen.

Aufgabe 3:
- Kernprüfung: x = decimalLongitude, y = decimalLatitude, Import-CRS = EPSG:4326.
- Recordzahl des importierten Layers mit Anzahl der gültig importierbaren Tabellenzeilen vergleichen.

Aufgabe 4:
- Musterlösungen und erwartete Zahlen erst nach Festlegung des Downloads eintragen.
- fehlende uncertainty nicht wie null behandeln.
- Issues differenziert nach Art des Flags bewerten.
- identische Koordinaten allein beweisen keine Dublette.

Aufgabe 5:
- Featurezahl und Ausschlusszahlen müssen rechnerisch zusammenpassen.
- gbifID soll zur Rückverfolgbarkeit erhalten bleiben.
- Ausgabe-CRS und Transformation müssen dokumentiert sein.

Aufgabe 6:
- Formulierung muss dokumentierte GBIF-Nachweise und den verwendeten Zeitraum nennen.
- Interpretation soll Beobachtungsbias und fehlende systematische Absenzdaten ansprechen.

Aufgabe 7:
- processing_notes.md soll eine knappe reproduzierbare Verarbeitungskette bilden.
-->

<!-- Notizen: Ab hier folgen Vermerke, welche als Gedankenstütze oder Erinnerung dienen, aber noch nicht in der vorhandenen Form veröffentlicht werden sollen. -->

<!--
Vor Durchführung ergänzen:
- Eingangsdatei, DOI, Filter und Lizenzangaben
- Grenzlayer und Hintergrunddienst
- Projekt- und Ausgabe-CRS
- Mindestjahr
- Regel und Grenzwert für coordinateUncertaintyInMeters
- erwartete Recordzahlen für jede Prüfregel
- Abgabetermin, Abgabeort und Mindestpunktzahl
- schemaidentischen Ersatzlayer erzeugen und testen

Mögliche Vereinfachung:
- nur drei Qualitätsregeln prüfen lassen und Aufgabe 7 als vorgegebenes Formular bereitstellen.

Mögliche Erweiterung:
- Punktdichte mit Bevölkerungs- oder Wegenähe lediglich explorativ vergleichen, ohne daraus bereits kausale Schlüsse zu ziehen.
-->
