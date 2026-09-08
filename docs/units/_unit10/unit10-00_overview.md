---
title: Überblick
published: true
toc: true
header:
  image: /assets/images/unit10/hero-unit10.jpg
  image_description: "Luftbildlandschaft mit überlagerten Punkten, Linien, Polygonflächen und Rasterzellen"
  caption: "KI-generierte Illustration, bearbeitet für diesen Kurs"
---

<!-- Rückblick: Welche Themeninhalte wurden in der letzten Kurssitzung bearbeitet? Sind Fragen zur letzten Kurssitzung offen geblieben? -->

## Rückblick & Fragen

In der letzten Kurssitzung haben wir die grundlegenden Eigenschaften von Geodaten kennengelernt. Wir haben untersucht, wie Orte durch Koordinaten beschrieben werden, warum Koordinaten nur gemeinsam mit einem Koordinatenreferenzsystem eindeutig sind und weshalb jede Übertragung der gekrümmten Erdoberfläche auf eine ebene Karte zu Verzerrungen führt.

Bevor wir mit dem neuen Lernabschnitt beginnen, klären wir offene Fragen zu Geodaten, Koordinaten, Koordinatenreferenzsystemen und Projektionen.

<!-- Introtext: Allgemeine Einleitung zum Thema im neuen Lernabschnitt und Verbindung zum vorangegangenen Thema. Worum geht es, welche Inhalte werden bearbeitet und warum sind diese wichtig? -->

## Einführung in Lernabschnitt 10

Wir wissen nun, wodurch Daten einen räumlichen Bezug erhalten. Damit ist jedoch noch nicht entschieden, **wie** ein Ausschnitt der Wirklichkeit in einem Geodatensatz dargestellt werden soll. Eine Baumbeobachtung kann als Punkt erfasst werden, eine Straße als Linie und ein Landkreis als Fläche. Höhe oder Temperatur lassen sich dagegen häufig sinnvoll als regelmäßiges Raster beschreiben.

Geodaten sind deshalb keine vollständigen Abbilder der Realität, sondern zweckgebundene **Modelle**. Das gewählte Datenmodell entscheidet, welche Informationen gespeichert werden können und welche räumlichen Fragen sich später beantworten lassen.

In diesem Lernabschnitt lernen wir die beiden grundlegenden Geodatenmodelle **Vektor** und **Raster** kennen. Anschließend beginnen wir praktisch mit **QGIS**, einem freien Geoinformationssystem. Darin können wir Geodaten öffnen, gemeinsam darstellen, untersuchen und später auch bearbeiten und analysieren.

<!-- Aktuelle Lerneinheit: Welcher konkrete Inhalt erwartet die Studierenden? -->

## In dieser Lerneinheit ...

In dieser Lerneinheit beschäftigen wir uns mit drei grundlegenden Fragen:

1. **Wie wird die räumliche Wirklichkeit zu einem Datenmodell?**  
   Wir unterscheiden Vektor- und Rasterdaten und betrachten, wie Punkte, Linien, Polygone und Rasterzellen unterschiedliche räumliche Phänomene repräsentieren.

2. **Wie lassen sich Geodaten in einem GIS untersuchen?**  
   Wir lernen die wichtigsten Bereiche der QGIS-Oberfläche kennen, öffnen ein Projekt, laden Layer und betrachten deren räumliche und tabellarische Informationen.

3. **Woher kommen Geodaten und wie können sie eingebunden werden?**  
   Wir unterscheiden lokale Dateien von webbasierten Geodatendiensten und binden erstmals einen Web Map Service, kurz WMS, in QGIS ein.

Dabei wechseln sich kurze konzeptionelle Abschnitte und praktische Arbeitsschritte ab. Ziel ist noch keine umfassende Beherrschung von QGIS, sondern ein sicheres Grundverständnis von **Datenmodell, Layer, Karte, Attributen, Projekt und Datenquelle**.

<!-- Lernziele: Was sollten Studierende am Ende dieser Lerneinheit wissen und anwenden können? -->

## Lernziele

Am Ende dieser Unit sind Studierende in der Lage, ...

* Geodaten als vereinfachte und zweckgebundene Modelle der Realität zu beschreiben,
* Vektor- und Rasterdaten grundlegend zu unterscheiden,
* Punkte, Linien und Polygone als Geometrietypen des Vektormodells zu benennen,
* für einfache räumliche Objekte und Phänomene ein geeignetes Datenmodell vorzuschlagen,
* zu erklären, warum dieselbe Realität abhängig von Fragestellung und Maßstab unterschiedlich modelliert werden kann,
* den Zweck eines Geoinformationssystems zu beschreiben,
* die zentralen Bereiche der QGIS-Oberfläche zu erkennen,
* den Unterschied zwischen einem QGIS-Projekt und den darin eingebundenen Geodatendateien zu erklären,
* Layer zu laden, ein- und auszublenden sowie deren Attribute und CRS-Informationen aufzurufen,
* lokale Geodatendateien von webbasierten Kartendiensten zu unterscheiden und
* einen vorgegebenen WMS in QGIS einzubinden.

<!-- Organisatorisches: Gibt es Formalitäten, welche noch geklärt werden sollten? -->

## Organisatorisches

In dieser Lerneinheit arbeiten wir erstmals praktisch mit QGIS. Stellen Sie vor Beginn sicher, dass **QGIS `[verbindliche QGIS-LTR-Version ergänzen]`** auf dem verwendeten Rechner gestartet werden kann. Die Sprache der Oberfläche darf Deutsch oder Englisch sein; die Anleitung nennt zentrale Begriffe bei Bedarf in beiden Sprachen.

Benötigt werden:

* Übungsdaten: `[Downloadlink ergänzen]`,
* lokaler Vektorlayer: `[Dateiname und Layer ergänzen]`,
* lokaler Rasterlayer: `[Dateiname ergänzen]`,
* Projekt-CRS: `[EPSG-Code ergänzen; für Marburg voraussichtlich EPSG:25832]`,
* WMS-Verbindung: `[Name, Dienstadresse und Layer ergänzen]` und
* ein vorbereiteter Ersatz-Screenshot samt Metadatenblatt für den Fall, dass der WMS während der Sitzung ausfällt.

Bitte speichern Sie Ihr QGIS-Projekt und alle zugehörigen Dateien in einem gemeinsamen, eindeutig benannten Arbeitsordner. Ein Projekt speichert Verweise auf die verwendeten Daten; es enthält die eingebundenen Datensätze in der Regel nicht selbst.

## Ablauf der Sitzung

Die Unit ist für eine Sitzung von ungefähr **120 Minuten** ausgelegt. Bei nur 90 Minuten wird die WMS-Dokumentation in der Sitzung gemeinsam an einem Beispiel besprochen. Als Hausaufgabe beantworten Sie ausschließlich die JiTT-Fragen zu Unit 10 in ILIAS.

| Zeit | Aktivität |
|---:|---|
| 0–15 Minuten | Einstieg: dieselbe Realität als Punkt, Linie, Polygon oder Raster |
| 15–35 Minuten | Vektor- und Rastermodell; Features und Attribute |
| 35–50 Minuten | Projekt, Layer und Datendatei unterscheiden |
| 50–70 Minuten | QGIS-Oberfläche und Arbeitsordner kennenlernen |
| 70–90 Minuten | lokale Vektor- und Rasterdaten laden und prüfen |
| 90–110 Minuten | WMS verbinden und mit lokalen Daten vergleichen |
| 110–120 Minuten | Projekt erneut öffnen, Ergebnissicherung und Exit-Ticket |

## Exit-Ticket

1. Was enthält eine `.qgz`-Projektdatei, und was enthält sie normalerweise nicht?
2. Woran erkennen Sie in QGIS, ob ein Layer Vektor- oder Rasterdaten enthält?
3. Weshalb eignet sich ein WMS als Hintergrund, aber meist nicht für eine Vektoranalyse?

## Transfer für Lehramtsstudierende

Entwerfen Sie eine kurze schulische Aufgabe, in der Lernende denselben geographischen Inhalt in zwei Datenmodellen darstellen. Legen Sie fest:

* Jahrgangsstufe und Lernziel,
* verwendetes Beispiel,
* zwei mögliche Modellierungen,
* erwartete Begründung der Lernenden und
* eine Hilfestellung für Lernende mit geringer GIS-Erfahrung.

Die Aufgabe soll deutlich machen, dass das Datenmodell von Fragestellung und Maßstab abhängt.

<!-- Notizen: Ab hier folgen Vermerke, welche als Gedankenstütze oder Erinnerung dienen aber noch nicht in der vorhandenen Form veröffentlicht werden sollen. -->

<!-- Hinweise für Lehrende:
Mögliche Einstiegsfrage:
- Wie könnte dieselbe Stadt auf einer Deutschlandkarte, einer Stadtkarte und in einem Satellitenbild dargestellt werden?

Mögliche Demonstrationen:
- Marburg als Punkt, Polygon und Ausschnitt eines Rasters zeigen
- ein QGIS-Projekt ohne die zugehörigen Datendateien öffnen und fehlende Layerpfade thematisieren
- denselben Datensatz als lokale Datei und einen vergleichbaren Inhalt als WMS gegenüberstellen

Didaktische Schwerpunkte:
- Vektor und Raster zunächst nur konzeptionell unterscheiden; die vertiefte praktische Arbeit folgt in den Units 11 bis 13.
- QGIS-Oberfläche nur so weit einführen, wie sie für die ersten Arbeitsschritte benötigt wird.
- Projektdatei und Datendatei von Beginn an sprachlich sauber trennen.

Vor Durchführung prüfen beziehungsweise ergänzen:
- verwendete QGIS-Installation und Arbeitsumgebung
- Downloadpfad der Übungsdaten
- URL und Name des verwendeten WMS

Unterseiten:
- unit10-01_datenmodelle.html
- unit10-02_qgis.html
- unit10-03_datenquellen.html
- unit10-04_assignment.html
-->
