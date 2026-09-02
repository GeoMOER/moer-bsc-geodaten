---
title: Überblick
published: true
toc: true
header:
  image: /assets/images/unit11/hero-unit11.jpg
  image_description: "Wald- und Kulturlandschaft mit verteilten Beobachtungspunkten und angedeuteten Unsicherheitsbereichen"
  caption: "KI-generierte Illustration, bearbeitet für diesen Kurs"
---

<!-- Rückblick: Welche Themeninhalte wurden in der letzten Kurssitzung bearbeitet? Sind Fragen zur letzten Kurssitzung offen geblieben? -->

## Rückblick & Fragen

In der letzten Kurssitzung haben wir Vektor und Raster als grundlegende Modelle räumlicher Daten kennengelernt. Wir haben erste lokale Layer in QGIS geladen, ein Projekt organisiert und einen WMS aus einem Geoportal eingebunden. Dabei wurde deutlich, dass Datenmodell, Datenquelle und Darstellungsform voneinander unterschieden werden müssen.

Bevor wir mit dem neuen Lernabschnitt beginnen, klären wir offene Fragen zu QGIS, Layern, Attributtabellen, CRS und webbasierten Geodatendiensten.

<!-- Introtext: Allgemeine Einleitung zum Thema im neuen Lernabschnitt und Verbindung zum vorangegangenen Thema. Worum geht es, welche Inhalte werden bearbeitet und warum sind diese wichtig? -->

## Einführung in Lernabschnitt 11

In dieser Unit betrachten wir den ersten Vektordatentyp genauer: **Punktdaten**. Punkte eignen sich, wenn für eine Fragestellung vor allem die Position eines räumlichen Objektes oder Ereignisses wichtig ist. Typische Beispiele sind Messstationen, GPS-Positionen, Probeflächen oder Fundorte von Arten.

Als reales Forschungsbeispiel verwenden wir Beobachtungsdaten aus der **Global Biodiversity Information Facility (GBIF)**. GBIF führt Biodiversitätsdaten vieler Einrichtungen und Projekte zusammen und macht sie über ein gemeinsames Portal zugänglich. Ein einzelner Datensatz kann beispielsweise dokumentieren, dass eine bestimmte Art zu einem bestimmten Zeitpunkt an einem bestimmten Ort beobachtet oder gesammelt wurde.

Am Beispiel des Feuersalamanders untersuchen wir, wie aus einer Tabelle mit Längen- und Breitengraden ein Punktlayer entsteht. Gleichzeitig beschäftigen wir uns mit Datenqualität und Interpretation: Ein Punkt auf der Karte ist ein Nachweis – nicht automatisch eine vollständige Aussage über die tatsächliche Verbreitung einer Art.

<!-- Aktuelle Lerneinheit: Welcher konkrete Inhalt erwartet die Studierenden? -->

## In dieser Lerneinheit ...

In dieser Lerneinheit beschäftigen wir uns mit drei aufeinander aufbauenden Fragen:

1. **Wie sind Punktdaten aufgebaut?**  
   Wir betrachten Punkte als Vektorfeatures, verbinden Geometrien mit Attributen und unterscheiden Position, Beobachtung und dargestelltes Objekt.

2. **Was enthalten Biodiversitätsdaten von GBIF?**  
   Wir lernen Occurrence Records, wichtige Datenfelder, Filter, Lizenzen, Zitation und typische Qualitätsprobleme kennen.

3. **Wie werden tabellarische Beobachtungen in QGIS zu Punkten?**  
   Wir importieren Längen- und Breitengrade aus einer Textdatei, prüfen CRS und Lage, untersuchen Attribute, filtern Datensätze und speichern einen dauerhaften Punktlayer.

Die wiederkehrende Arbeitslogik lautet:

> **Fragestellung → Datenquelle → Tabellenstruktur → Qualitätsprüfung → Punktlayer → Interpretation**

<!-- Lernziele: Was sollten Studierende am Ende dieser Lerneinheit wissen und anwenden können? -->

## Lernziele

Am Ende dieser Unit sind Studierende in der Lage, ...

* Punktdaten als Teil des Vektormodells einzuordnen,
* Geometrie und Attribute eines Punktfeatures zu unterscheiden,
* geeignete und ungeeignete Anwendungen des Punktmodells zu benennen,
* tabellarische Koordinatenfelder zu erkennen und auf Plausibilität zu prüfen,
* einen GBIF Occurrence Record als dokumentierten Artnachweis zu erklären,
* zentrale GBIF-Felder wie Artname, Datum, Koordinaten, Datengrundlage und Koordinatenunsicherheit zu interpretieren,
* typische Einschränkungen von Beobachtungsdaten wie räumliche Verzerrung, Dubletten und fehlende Nachweise zu beschreiben,
* eine koordinatenhaltige Textdatei korrekt als Punktlayer in QGIS zu importieren,
* Punktfeatures über die Attributtabelle auszuwählen und zu filtern,
* einen importierten Punktlayer als GeoPackage zu speichern und
* GBIF-Datenquelle, Download-DOI, Lizenz und Verarbeitungsschritte nachvollziehbar zu dokumentieren.

<!-- Organisatorisches: Gibt es Formalitäten, welche noch geklärt werden sollten? -->

## Organisatorisches

Für die praktische Arbeit benötigen Sie QGIS sowie die bereitgestellte Auswahl von GBIF-Beobachtungen. Verwenden Sie während der Lehrveranstaltung den vorbereiteten Datensatz, damit alle mit derselben dokumentierten Datenversion arbeiten.

Verwenden Sie **QGIS `[dieselbe verbindliche QGIS-LTR-Version wie in Unit 10 ergänzen]`** und das gemeinsame Projekt-CRS **`[EPSG-Code ergänzen; für Marburg voraussichtlich EPSG:25832]`**.

Das verbindliche Übergabeprodukt dieser Unit ist:

```text
data_output/unit11_results.gpkg
└── gbif_checked
```

Falls das eigene Ergebnis nicht verwendbar ist, steht ein schemaidentischer Ersatzlayer bereit: `[Downloadlink ergänzen]`.

## Ablauf der Sitzung

Die Unit ist für ungefähr **120 Minuten** ausgelegt.

| Zeit | Aktivität |
|---:|---|
| 0–15 Minuten | Einstieg: Beobachtung oder Verbreitung? |
| 15–35 Minuten | Punktfeatures, Attribute und räumliche Unsicherheit |
| 35–55 Minuten | GBIF, Herkunftsebenen, DOI und Lizenz |
| 55–75 Minuten | Tabelle und Importparameter prüfen |
| 75–100 Minuten | Punkte importieren und Qualitätsfelder untersuchen |
| 100–115 Minuten | Auswahl dokumentieren und `gbif_checked` exportieren |
| 115–120 Minuten | Exit-Ticket und Übergabeprüfung |

## Exit-Ticket

1. Weshalb ist ein GBIF-Punkt nicht automatisch eine exakt lokalisierte Lebendbeobachtung?
2. Welche drei Angaben müssen beim Import von `decimalLongitude` und `decimalLatitude` stimmen?
3. Warum beschreibt `gbif_checked` dokumentierte Nachweise und nicht die vollständige Verbreitung einer Art?

## Transfer für Lehramtsstudierende

Entwerfen Sie einen kurzen Unterrichtsimpuls zur kritischen Interpretation einer Punktkarte. Formulieren Sie Lernziel, zwei Leitfragen, eine erwartbare Fehlinterpretation und eine Ergebnissicherung. Die Lernenden sollen zwischen „kein Nachweis vorhanden“ und „Art nachweislich abwesend“ unterscheiden.

<!-- Notizen: Ab hier folgen Vermerke, welche als Gedankenstütze oder Erinnerung dienen aber noch nicht in der vorhandenen Form veröffentlicht werden sollen. -->

<!--
Mögliche Einstiegsfrage:
- Eine Karte mit GBIF-Punkten des Feuersalamanders zeigen und fragen: „Wo kommt die Art vor?“
- Anschließend problematisieren: Zeigt die Karte Vorkommen, Beobachtungen oder Beobachtungsaktivität?

Didaktische Schwerpunkte:
- Punkte ausdrücklich als Vektordaten benennen.
- Beobachtung, Individuum, Fundort und Punktfeature sprachlich unterscheiden.
- Datenqualität nicht als nachträgliches Spezialthema, sondern bei jedem Arbeitsschritt behandeln.
- Keine Verbreitungskarte im strengen Sinn versprechen; zunächst Nachweisdaten kartieren.

Vor Durchführung ergänzen:
- GBIF-Download und DOI
- Datenstand und Filter des Downloads
- verwendeter Artenname beziehungsweise alternatives Beispiel
- Deutschland- oder Hessen-Grenzlayer
- Abgabe- und Datenpfade

Geplante Unterseiten:
- unit11-01_punktdaten.md
- unit11-02_gbif.md
- unit11-03_punkte_qgis.md
- unit11-04_assignment.md
-->
