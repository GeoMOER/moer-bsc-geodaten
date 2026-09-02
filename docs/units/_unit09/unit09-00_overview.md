---
title: Überblick
published: true
toc: true
header:
  image: /assets/images/unit09/hero-unit09.jpg
  image_description: "Breiter Blick auf Europa auf einer gekrümmten Erde mit feinem Koordinatengitter und markiertem Ort"
  caption: "KI-generierte Illustration, bearbeitet für diesen Kurs"
---

<!-- Rückblick: Welche Themeninhalte wurden in der letzten Kurssitzung bearbeitet? Sind Fragen zur letzten Kurssitzung offen geblieben? -->

## Rückblick & Fragen

In der letzten Kurssitzung haben wir uns damit beschäftigt, wie sich wiederkehrende Arbeitsschritte automatisieren und dadurch schneller, zuverlässiger und nachvollziehbarer ausführen lassen. Dabei haben wir gesehen, warum ein gut strukturierter und reproduzierbarer Arbeitsablauf meist besser ist als die wiederholte manuelle Bearbeitung einzelner Daten.

Bevor wir mit dem neuen Lernabschnitt beginnen, klären wir offene Fragen zur letzten Sitzung.

<!-- Introtext: Allgemeine Einleitung zum Thema im neuen Lernabschnitt und Verbindung zum vorangegangenen Thema. Worum geht es, welche Inhalte werden bearbeitet und warum sind diese wichtig? -->

## Einführung in Lernabschnitt 09

Bisher haben wir vor allem Daten betrachtet, die in Tabellen oder Dateien gespeichert sind. Viele Fragestellungen in der Geographie enthalten jedoch zusätzlich eine räumliche Information: **Wo befindet sich etwas? Wie groß ist ein Gebiet? Welche Eigenschaften besitzt ein bestimmter Ort?**

Solche Daten werden als **Geodaten** bezeichnet. Neben den eigentlichen Messwerten oder Eigenschaften enthalten sie einen Bezug zu einem Ort oder einem räumlichen Objekt. Dieser Raumbezug kann beispielsweise durch Koordinaten, Adressen, administrative Gebiete oder ein Koordinatenreferenzsystem beschrieben werden.

In diesem Lernabschnitt schaffen wir die Grundlagen für die weitere Arbeit mit Geodaten. Wir untersuchen, was Geodaten von anderen Daten unterscheidet, wie Positionen durch Koordinaten angegeben werden und warum die gekrümmte Erdoberfläche nicht ohne Verzerrungen auf einer ebenen Karte dargestellt werden kann.

<!-- Aktuelle Lerneinheit: Welcher konkrete Inhalt erwartet die Studierenden? -->

## In dieser Lerneinheit ...

In dieser Lerneinheit beschäftigen wir uns mit drei grundlegenden Fragen:

1. **Was sind Geodaten?**  
   Wir betrachten, wodurch Daten einen räumlichen Bezug erhalten und welche besonderen Eigenschaften sich daraus ergeben.

2. **Wie werden Orte durch Koordinaten beschrieben?**  
   Wir lernen geographische Koordinaten kennen und üben, Längen- und Breitengrade zu lesen und richtig zuzuordnen.

3. **Warum gibt es unterschiedliche Koordinatensysteme und Kartenprojektionen?**  
   Wir untersuchen, weshalb die Erde für Karten in eine Ebene übertragen werden muss, welche Verzerrungen dabei entstehen und warum das Koordinatenreferenzsystem eines Datensatzes wichtig ist.

Dabei arbeiten wir mit anschaulichen Beispielen und typischen Problemen aus der Praxis. Im Mittelpunkt steht nicht die Mathematik von Kartenprojektionen, sondern ein sicherer erster Umgang mit räumlich referenzierten Daten.

<!-- Lernziele: Was sollten Studierende am Ende dieser Lerneinheit wissen und anwenden können? -->

## Lernziele

Am Ende dieser Unit sind Studierende in der Lage, ...

* Geodaten von nicht räumlich referenzierten Daten zu unterscheiden,
* den Raumbezug einfacher Datensätze zu erkennen und zu beschreiben,
* geographische Koordinaten als Längen- und Breitengrad zu lesen,
* die Reihenfolge und Einheit von Koordinatenangaben zu überprüfen,
* den Unterschied zwischen geographischen und projizierten Koordinatensystemen grundlegend zu erklären,
* zu erläutern, warum Kartenprojektionen zu Verzerrungen führen,
* die Bedeutung eines Koordinatenreferenzsystems und eines EPSG-Codes für die Arbeit mit Geodaten zu beschreiben und
* typische Probleme durch fehlende oder falsch zugewiesene Koordinatenreferenzsysteme zu erkennen.

<!-- Organisatorisches: Gibt es Formalitäten, welche noch geklärt werden sollten? -->

## Organisatorisches

Für die kurzen Recherche- und Vergleichsaufgaben benötigen Sie einen Webbrowser. Ein GIS ist in dieser Unit noch nicht erforderlich. Die praktische Arbeit mit QGIS beginnt in Unit 10.

Verbindliche Arbeitsmittel:

* Kursseiten dieser Unit,
* [OpenStreetMap](https://www.openstreetmap.org/){:target="_blank"} zum Auffinden eines öffentlich bekannten Ortes,
* [EPSG.io](https://epsg.io/){:target="_blank"} zum Nachschlagen von CRS-Definitionen und
* die auf den Kursseiten bereitgestellten Abbildungen zum Projektionsvergleich.

Beachten Sie bei externen Diensten, dass die Projektion der sichtbaren Webkarte nicht zwingend mit dem CRS der angezeigten oder ausgegebenen Positionskoordinaten identisch ist.

## Ablauf der Sitzung

Die Unit ist für eine Sitzung von ungefähr **90 Minuten** ausgelegt.

| Zeit | Aktivität |
|---:|---|
| 0–10 Minuten | Einstieg mit dem unbeschrifteten Zahlenpaar `50,81 / 8,77` |
| 10–25 Minuten | Raumbezug und Eigenschaften von Geodaten |
| 25–40 Minuten | Breite, Länge, Wertebereiche und Reihenfolge |
| 40–55 Minuten | Plausibilitätsprüfung einer Koordinatentabelle |
| 55–70 Minuten | Kartenprojektionen und unvermeidbare Verzerrungen |
| 70–82 Minuten | WGS 84, UTM, Web Mercator und EPSG-Codes |
| 82–90 Minuten | Zuweisen und Transformieren; Exit-Ticket |

## Exit-Ticket

Beantworten Sie zum Abschluss ohne Nachschlagen:

1. Welche Angaben fehlen, wenn nur das Zahlenpaar `(8.77, 50.81)` vorliegt?
2. Welches der behandelten CRS würden Sie für Entfernungsmessungen rund um Marburg zuerst prüfen – und warum?
3. Was ändert sich beim Transformieren eines Datensatzes, und was bleibt gleich?

## Transfer für Lehramtsstudierende

Wählen Sie eine der beiden Projektionsdarstellungen aus dieser Unit und entwerfen Sie einen kurzen Arbeitsauftrag für Schülerinnen und Schüler der Sekundarstufe I oder II. Halten Sie fest:

* angestrebtes Lernziel,
* erwartete Fehlvorstellung,
* zwei Beobachtungsfragen und
* eine fachlich angemessene Ergebnissicherung.

Der Arbeitsauftrag soll verdeutlichen, dass eine vertraute Weltkarte keine neutrale oder in allen Eigenschaften korrekte Abbildung der Erde ist.

<!-- Notizen: Ab hier folgen Vermerke, welche als Gedankenstütze oder Erinnerung dienen aber noch nicht in der vorhandenen Form veröffentlicht werden sollen. -->

<!-- Hinweise für Lehrende:
Mögliche Einstiegsfrage: Was bedeuten die beiden Zahlen 50.8 und 8.8 – und reichen sie aus, um einen Ort eindeutig zu beschreiben?

Mögliche Demonstrationen:
- Marburg in geographischen Koordinaten lokalisieren
- dieselbe Position in WGS 84 und UTM vergleichen
- Verzerrungen verschiedener Weltkarten gegenüberstellen
- einen Datensatz mit falsch zugewiesenem CRS zeigen

Unterseiten:
- unit09-01_geodaten.html
- unit09-02_koordinaten.html
- unit09-03_projektionen.html
-->
