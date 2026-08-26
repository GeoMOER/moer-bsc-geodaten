---
title: Überblick
published: true
toc: true
header:
  image: /assets/images/spotlight01/jekyll_github_pages.png
  image_description: "Cutout from Measured carbon dioxide concentrations in Vancouver"
  caption: "Bild: [jekyll](https://jekyllrb.com/)"
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

In dieser Lerneinheit arbeiten wir erstmals praktisch mit QGIS. Stellen Sie vor Beginn sicher, dass QGIS auf dem verwendeten Rechner gestartet werden kann. Die benötigten Übungsdaten und Angaben zum verwendeten Webdienst werden in der Lehrveranstaltung bereitgestellt.

Bitte speichern Sie Ihr QGIS-Projekt und alle zugehörigen Dateien in einem gemeinsamen, eindeutig benannten Arbeitsordner. Ein Projekt speichert Verweise auf die verwendeten Daten; es enthält die eingebundenen Datensätze in der Regel nicht selbst.

<!-- Notizen: Ab hier folgen Vermerke, welche als Gedankenstütze oder Erinnerung dienen aber noch nicht in der vorhandenen Form veröffentlicht werden sollen. -->

<!--
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

Vor Veröffentlichung prüfen beziehungsweise ergänzen:
- verwendete QGIS-Installation und Arbeitsumgebung
- Downloadpfad der Übungsdaten
- URL und Name des verwendeten WMS

Geplante Unterseiten:
- unit10-01_datenmodelle.html
- unit10-02_qgis.html
- unit10-03_datenquellen.html
- unit10-04_assignment.html
-->