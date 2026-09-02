---
title: Vektordaten aus Geoportalen
published: true
toc: true
header:
  image: /assets/images/unit12/hero-unit12.jpg
  image_description: "Flusslandschaft mit Schutzgebietsfläche und Beobachtungspunkten innerhalb und außerhalb des Gebietes"
  caption: "KI-generierte Illustration, bearbeitet für diesen Kurs"
---

<!-- Rückblick: Welche Inhalte aus der vorherigen Seite werden benötigt? -->

## Rückblick

Auf der vorherigen Seite haben wir das **Vektormodell** kennengelernt. Darin werden räumliche Objekte als Punkte, Linien oder Polygone dargestellt. Jedes Objekt kann zusätzlich Eigenschaften in einer Attributtabelle besitzen.

Nun benötigen wir geeignete Linien- und Polygondaten für unsere Fragestellung:

> **Welche Artenbeobachtungen und Gewässer liegen in beziehungsweise schneiden ausgewählte Schutzgebiete?**

Solche Daten finden wir häufig in **Geoportalen** von Behörden und anderen öffentlichen Einrichtungen.

## Was ist ein Geoportal?

Ein Geoportal ist ein zentraler Zugang zu räumlichen Daten, Karten und Geodatendiensten. Es kann verschiedene Funktionen miteinander verbinden:

- nach Geodatensätzen suchen,
- Metadaten zu einem Datensatz anzeigen,
- Daten in einer Kartenansicht betrachten,
- Geodatendienste bereitstellen,
- Daten zum Download anbieten.

Ein Eintrag im Geoportal ist jedoch noch nicht automatisch ein für unsere Analyse geeigneter Datensatz. Deshalb prüfen wir immer, **was genau angeboten wird**.

## Kartenansicht, Dienst oder Download?

Geoportale können dieselben Geodaten auf unterschiedliche Weise bereitstellen.

| Angebot | Was erhalten wir? | Wofür ist es geeignet? |
|---|---|---|
| Kartenansicht | eine Darstellung im Browser | Daten entdecken und räumlich einordnen |
| WMS | ein vom Server erzeugtes Kartenbild | Hintergrundkarte und Visualisierung |
| WFS | einzelne Vektorobjekte mit Geometrien und Attributen | Abfragen und Analysen in QGIS |
| Download | eine lokale Datendatei, zum Beispiel GeoPackage, GeoJSON oder Shapefile | reproduzierbares und teilweise auch offline mögliches Arbeiten |

Ein **WMS** sieht in QGIS wie ein Layer aus, besteht für uns aber zunächst nur aus einem Kartenbild. Einzelne Schutzgebiete oder Gewässer lassen sich daraus normalerweise nicht als Vektorobjekte auswählen.

Ein **WFS** überträgt dagegen Features: Wir erhalten Geometrien und Attribute und können diese untersuchen, filtern und räumlich auswählen.

> Für die Übungen dieser Unit benötigen wir **Vektordaten**, also einen Download oder einen geeigneten Feature-Dienst – nicht nur ein Kartenbild.

## Geeignete Daten suchen

Eine gute Suche beginnt nicht beim Dateiformat, sondern bei der benötigten Information. Für unser Beispiel suchen wir:

1. **Schutzgebiete** als Polygone,
2. **Gewässer** als Linien,
3. einen passenden räumlichen Ausschnitt, zum Beispiel Marburg oder Hessen.

Hilfreiche Suchbegriffe sind Kombinationen aus Thema, Gebiet und Datentyp:

- `Naturschutzgebiete Hessen Geodaten`
- `Fließgewässer Hessen WFS`
- `Gewässernetz Marburg Download`

Mögliche Ausgangspunkte sind beispielsweise:

- das [Geoportal Hessen](https://www.geoportal.hessen.de/),
- die Karten und Geodaten des [Bundesamtes für Naturschutz](https://www.bfn.de/thema/karten-und-daten),
- weitere kommunale oder thematische Geoportale.

## Metadaten lesen

Bevor wir einen Datensatz verwenden, lesen wir seine **Metadaten**. Sie beschreiben, woher die Daten stammen, welchen Inhalt sie besitzen und unter welchen Bedingungen wir sie verwenden dürfen.

Mindestens diese Angaben sollten wir festhalten:

| Merkmal | Leitfrage |
|---|---|
| Titel | Wie heißt der Datensatz genau? |
| Herausgeber | Wer hat die Daten erstellt oder veröffentlicht? |
| Inhalt | Welche Objekte und Attribute sind enthalten? |
| Geometrietyp | Handelt es sich um Punkte, Linien oder Polygone? |
| räumliche Abdeckung | Für welches Gebiet liegen Daten vor? |
| Aktualität | Auf welchen Stand beziehen sich die Daten? |
| Maßstab oder Genauigkeit | Für welche räumliche Detailstufe wurden sie erstellt? |
| Koordinatenreferenzsystem | In welchem CRS liegen die Daten vor? |
| Zugang | Gibt es Download, WFS oder nur WMS? |
| Lizenz | Dürfen wir die Daten bearbeiten und weitergeben? |
| Quellenangabe | Wie soll der Datensatz zitiert werden? |

Fehlt eine wichtige Angabe, ist das ebenfalls eine Information: Wir können die Eignung des Datensatzes dann nur eingeschränkt beurteilen.

## Zwei Datensätze für unser Beispiel

Für die folgenden Übungen werden zwei vorbereitete Datensätze verwendet. Ergänzen Sie die Angaben anhand der jeweiligen Metadatenseite.

| Merkmal | Schutzgebiete | Gewässer |
|---|---|---|
| Titel | `[ergänzen]` | `[ergänzen]` |
| Herausgeber | `[ergänzen]` | `[ergänzen]` |
| Geometrietyp | Polygon | Linie |
| räumliche Abdeckung | `[ergänzen]` | `[ergänzen]` |
| Datenstand | `[ergänzen]` | `[ergänzen]` |
| CRS | `[ergänzen]` | `[ergänzen]` |
| Zugang/Format | `[ergänzen]` | `[ergänzen]` |
| Lizenz | `[ergänzen]` | `[ergänzen]` |
| Quelle/URL | `[ergänzen]` | `[ergänzen]` |

<!-- Lehrende: Hier die im Kurs tatsächlich eingesetzten Datensätze und Metadatenlinks ergänzen. Wenn möglich, zusätzlich eine lokale Kopie als Ausweichlösung bereitstellen. -->

## Download oder Webdienst?

Beide Zugangswege können sinnvoll sein.

### Download

Ein Download eignet sich besonders, wenn wir:

- mit einem klar definierten Datenstand arbeiten möchten,
- die Übung ohne dauerhafte Internetverbindung durchführen wollen,
- die Eingabedaten unverändert archivieren möchten,
- einen kleinen oder bereits zugeschnittenen Datensatz benötigen.

### WFS

Ein WFS eignet sich besonders, wenn wir:

- auf einen aktuellen Datenbestand zugreifen möchten,
- nur einen bestimmten räumlichen Ausschnitt benötigen,
- Features und Attribute direkt in QGIS laden möchten.

Webdienste können sich verändern oder zeitweise nicht erreichbar sein. Für eine Lehrveranstaltung ist deshalb eine vorbereitete lokale Kopie hilfreich.

## Dateien richtig ablegen

Legen Sie heruntergeladene Originaldaten getrennt von später erzeugten Ergebnissen ab:

```text
unit12/
  data_raw/
  data_output/
  documentation/
```

- **`data_raw/`** enthält unveränderte Downloads.
- **`data_output/`** enthält bearbeitete oder ausgewählte Daten.
- **`documentation/`** enthält Metadaten, Quellenangaben und Notizen.

Wenn ein Shapefile als ZIP-Archiv bereitgestellt wird, gehören mehrere Dateien zusammen. Benennen oder verschieben Sie deshalb nicht nur die Datei mit der Endung `.shp`. Speichern Sie die zusammengehörenden Bestandteile gemeinsam oder überführen Sie den Datensatz später in ein GeoPackage.

## Daten vor der Analyse prüfen

Nach dem Download oder Einbinden kontrollieren wir in QGIS:

1. Wird der Layer ohne Fehlermeldung geladen?
2. Besitzt er den erwarteten Geometrietyp?
3. Liegt er im erwarteten Gebiet?
4. Sind CRS und räumliche Ausdehnung plausibel?
5. Enthält die Attributtabelle verständliche Felder?
6. Sind Datenstand, Lizenz und Quelle dokumentiert?

Erst danach verwenden wir den Datensatz für eine räumliche Auswertung.

## Übung: Einen Datensatz beurteilen

Suchen Sie in einem Geoportal nach einem Linien- oder Polygondatensatz für Hessen. Vergleichen Sie zwei Suchergebnisse und beantworten Sie für beide:

1. Wer stellt die Daten bereit?
2. Welcher Geometrietyp ist zu erwarten?
3. Welches Gebiet deckt der Datensatz ab?
4. Wie aktuell ist er?
5. Gibt es einen Download, WFS oder nur WMS?
6. Ist die Nutzungslizenz angegeben?
7. Welcher Datensatz wäre für eine Analyse in QGIS besser geeignet – und warum?

Dokumentieren Sie anschließend den ausgewählten Datensatz in der Tabelle oben.

## Zusammenfassung

- Geoportale helfen uns, Geodaten und ihre Metadaten zu finden.
- Eine Kartenansicht oder ein WMS ist nicht dasselbe wie ein analysierbarer Vektordatensatz.
- Für Vektoranalysen benötigen wir Features aus einem Download oder Feature-Dienst.
- Metadaten sind notwendig, um Inhalt, Qualität, Aktualität und Nutzbarkeit zu beurteilen.
- Originaldaten, Ergebnisse und Dokumentation werden getrennt abgelegt.

## Weiterführende Informationen

- [Geoportal Hessen](https://www.geoportal.hessen.de/)
- [Suche im Geoportal Hessen](https://www.geoportal.hessen.de/search/)
- [Karten und Daten des Bundesamtes für Naturschutz](https://www.bfn.de/thema/karten-und-daten)
- [QGIS-Dokumentation: Vektorlayer erstellen und verwalten](https://docs.qgis.org/latest/en/docs/user_manual/managing_data_source/create_layers.html)

<!-- Notizen: Ab hier folgen Vermerke, welche als Gedankenstütze oder Erinnerung dienen, aber noch nicht in der vorhandenen Form veröffentlicht werden sollen. -->

<!--
TODO Lehrende vor Durchführung:
- Konkreten Polygon- und Liniendatensatz auswählen.
- Metadatenlinks, Lizenz und Datenstand prüfen und in die Tabelle eintragen.
- Einen kleinen räumlichen Ausschnitt als lokale Sicherung bereitstellen.
- Screenshots der Portalsuche und Metadatenseiten ergänzen.
- Feldnamen mit den Aufgaben in unit12-03_vektoren_qgis.md abstimmen.
-->
