---
title: Überblick
published: true
toc: true
header:
  image: /assets/images/unit12/hero-unit12.jpg
  image_description: "Flusslandschaft mit Schutzgebietsfläche und Beobachtungspunkten innerhalb und außerhalb des Gebietes"
  caption: "KI-generierte Illustration, bearbeitet für diesen Kurs"
---

<!-- Rückblick: Welche Themeninhalte wurden in der letzten Kurssitzung bearbeitet? Sind Fragen zur letzten Kurssitzung offen geblieben? -->

## Rückblick & Fragen

In der letzten Kurssitzung haben wir Punktdaten als Teil des Vektormodells untersucht. Aus tabellarischen GBIF-Nachweisen haben wir in QGIS einen Punktlayer erzeugt, Attribute und Qualitätsinformationen geprüft und eine dokumentierte Auswahl als GeoPackage gespeichert.

Bevor wir mit dem neuen Lernabschnitt beginnen, klären wir offene Fragen zu Punktgeometrien, GBIF-Daten, Koordinatenimport, Attributfiltern und der vorsichtigen Interpretation von Beobachtungskarten.

<!-- Introtext: Allgemeine Einleitung zum Thema im neuen Lernabschnitt und Verbindung zum vorangegangenen Thema. Worum geht es, welche Inhalte werden bearbeitet und warum sind diese wichtig? -->

## Einführung in Lernabschnitt 12

Punkte beschreiben einzelne Positionen. Viele geographische Objekte besitzen jedoch einen Verlauf oder eine räumliche Ausdehnung. Gewässer und Verkehrswege werden häufig als **Linien**, Schutzgebiete, Seen oder Verwaltungsgebiete als **Polygone** dargestellt.

In dieser Unit vervollständigen wir damit das grundlegende Vektormodell aus Punkt, Linie und Polygon. Wir untersuchen, wie diese Geometrien aufgebaut sind, welche Attribute sie besitzen und weshalb Maßstab und Fragestellung die gewählte Darstellung beeinflussen.

Anschließend beschaffen wir reale Vektordaten über Geoportale und kombinieren sie in QGIS mit den GBIF-Punkten aus Unit 11. Dadurch können wir erstmals räumliche Fragen beantworten, die mit einer gewöhnlichen Tabelle nur schwer zu bearbeiten wären:

> **Welche dokumentierten Artennachweise liegen innerhalb von Schutzgebieten, und welche Gewässer schneiden diese Flächen?**

<!-- Aktuelle Lerneinheit: Welcher konkrete Inhalt erwartet die Studierenden? -->

## In dieser Lerneinheit ...

In dieser Lerneinheit beschäftigen wir uns mit drei aufeinander aufbauenden Fragen:

1. **Wie funktionieren Linien- und Polygongeometrien?**  
   Wir betrachten Stützpunkte, Linienverläufe, geschlossene Flächen, Multipart-Geometrien sowie die Verbindung von Geometrie und Attributen.

2. **Wie finden und beurteilen wir Vektordaten in Geoportalen?**  
   Wir suchen nach Gewässer- und Schutzgebietsdaten, lesen Metadaten, unterscheiden Vorschau, Download und WFS und prüfen Format, CRS, Aktualität und Lizenz.

3. **Wie untersuchen und kombinieren wir Vektorlayer in QGIS?**  
   Wir laden Linien und Polygone, symbolisieren und filtern sie und verwenden eine räumliche Auswahl, um Punkt-, Linien- und Polygonlayer miteinander in Beziehung zu setzen.

Die wiederkehrende Arbeitslogik lautet:

> **Fragestellung → Datenquelle → Geometrietyp → Attribute → räumliche Beziehung → dokumentiertes Ergebnis**

<!-- Lernziele: Was sollten Studierende am Ende dieser Lerneinheit wissen und anwenden können? -->

## Lernziele

Am Ende dieser Unit sind Studierende in der Lage, ...

* Punkt, Linie und Polygon als Geometrietypen des Vektormodells zu unterscheiden,
* zu erklären, wie Linien und Polygone aus Koordinaten beziehungsweise Stützpunkten aufgebaut sind,
* Geometrie, Feature und Attribut voneinander zu unterscheiden,
* für eine Fragestellung einen geeigneten Vektorgeometrietyp auszuwählen,
* den Einfluss von Maßstab, Generalisierung und Grenzdefinition auf Vektordaten zu beschreiben,
* Geoportale nach geeigneten Vektordaten zu durchsuchen,
* Metadaten, Downloadoptionen, WMS und WFS fachlich zu unterscheiden,
* GeoPackage, GeoJSON und Shapefile grundlegend einzuordnen,
* Linien- und Polygonlayer in QGIS zu laden, zu untersuchen und sinnvoll darzustellen,
* Features über Attribute auszuwählen,
* Punkte und Linien anhand ihrer räumlichen Beziehung zu Polygonen auszuwählen und
* Datenquellen, Auswahlregeln, CRS und Ergebnisse nachvollziehbar zu dokumentieren.

<!-- Organisatorisches: Gibt es Formalitäten, welche noch geklärt werden sollten? -->

## Organisatorisches

Für die praktische Arbeit benötigen Sie QGIS, den geprüften GBIF-Punktlayer aus Unit 11 sowie die bereitgestellten Linien- und Polygondaten. Falls Ihr Ergebnis aus Unit 11 nicht verfügbar ist, wird ein einheitlicher Ersatzlayer bereitgestellt.

Speichern Sie die unveränderten Eingangsdaten, eigene Ausgaben und Metadaten erneut in getrennten Unterordnern. Verwenden Sie für räumliche Messungen und Auswahlen das vorgegebene Projekt- und Ausgabe-CRS.

Verwenden Sie dasselbe Projekt-CRS wie seit Unit 10: **`[EPSG-Code ergänzen; für Marburg voraussichtlich EPSG:25832]`**. Erwarteter Eingang ist `unit11_results.gpkg/gbif_checked`; der Ersatzlayer muss dasselbe Schema besitzen.

Das verbindliche Übergabeprodukt ist `data_output/unit12_results.gpkg` mit:

* `schutzgebiete_auswahl`,
* `gbif_in_schutzgebieten` und
* `gewaesser_an_schutzgebieten`.

## Ablauf der Sitzung

Die Unit ist für ungefähr **120 Minuten** ausgelegt.

| Zeit | Aktivität |
|---:|---|
| 0–20 Minuten | Linien, Polygone, Multipart und Generalisierung |
| 20–40 Minuten | räumliche Beziehungen und Grenzfälle |
| 40–60 Minuten | Geoportal, Metadaten, Download und WFS |
| 60–80 Minuten | Layer laden, prüfen und gestalten |
| 80–105 Minuten | Attribut- und räumliche Auswahl durchführen |
| 105–115 Minuten | Ergebnisse exportieren und kontrollieren |
| 115–120 Minuten | Exit-Ticket |

## Exit-Ticket

1. Wodurch unterscheiden sich Auswahl und neu gespeicherter Ergebnislayer?
2. Welche räumliche Beziehung wurde für Punkte beziehungsweise Gewässer verwendet?
3. Warum benötigen Messungen ein geeignetes projiziertes CRS?

## Transfer für Lehramtsstudierende

Entwerfen Sie ein einfaches Schulbeispiel, in dem Punkte, Linien und Polygone gemeinsam eine räumliche Frage beantworten. Benennen Sie Lernziel, Layer, räumliche Beziehung, einen Grenzfall und eine gestufte Hilfestellung.

<!-- Notizen: Ab hier folgen Vermerke, welche als Gedankenstütze oder Erinnerung dienen aber noch nicht in der vorhandenen Form veröffentlicht werden sollen. -->

<!--
Möglicher Einstieg:
- GBIF-Punkte allein zeigen und fragen: „Welche Beobachtungen liegen in einem Schutzgebiet?“
- Danach Schutzgebietspolygone einblenden und diskutieren, welche neue Information entsteht.

Didaktische Schwerpunkte:
- Punkt bleibt Teil des Vektormodells; Unit 12 ergänzt Linie und Polygon.
- Kartensymbol und tatsächliche Geometrie unterscheiden.
- Räumliche Auswahl als erste echte GIS-Operation einführen.
- „innerhalb“ und „schneidet“ an Grenzfällen anschaulich unterscheiden.
- Messungen nur in einem geeigneten projizierten CRS durchführen.

Vor Durchführung ergänzen:
- Gewässer- und Schutzgebietsdatensatz
- Geoportal- und Metadatenlinks
- Datenstand, Lizenz und Quellenangabe
- Projekt- und Ausgabe-CRS
- bereitgestellter GBIF-Punktlayer

Geplante Unterseiten:
- unit12-01_vektordaten.md
- unit12-02_geoportale.md
- unit12-03_vektoren_qgis.md
- unit12-04_assignment.md
-->
