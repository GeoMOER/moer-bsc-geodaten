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

Zu Beginn besprechen wir **10 Minuten lang die JiTT-Antworten zu Unit 08**. An ein bis zwei ausgewählten Verständnisfragen klären wir die wichtigsten offenen Punkte und knüpfen an die vorige Sitzung an.

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

### Verbindliche Kernziele

Am Ende der gemeinsamen Sitzung sind Studierende in der Lage, ...

* den Raumbezug einfacher Datensätze zu erkennen und Geodaten von Daten ohne nutzbaren Raumbezug zu unterscheiden,
* geographische Koordinaten zu lesen und ihre Achsenreihenfolge, Einheit und Wertebereiche auf Plausibilität zu prüfen,
* zu erklären, weshalb Koordinaten nur mit einem bekannten Koordinatenreferenzsystem und einer eindeutigen CRS-Angabe, beispielsweise einem EPSG-Code, zuverlässig nutzbar sind,
* geographische und projizierte Koordinatensysteme grundlegend zu unterscheiden und die unvermeidlichen Verzerrungen von Kartenprojektionen zu erläutern und
* das Zuweisen eines CRS vom Transformieren von Daten zu unterscheiden und typische CRS-Fehler zu erkennen.

### Vertiefung und Nachschlagen

Die ausführlichen Unterseiten ermöglichen außerdem, ...

* verschiedene Formen des Raumbezugs, räumliche Ausdehnung, Maßstab und Lagegenauigkeit genauer zu vergleichen,
* Koordinaten zwischen Dezimalgrad und Grad-Minuten-Sekunden umzurechnen sowie weitere CRS über EPSG-Codes zu recherchieren und
* Projektionen für unterschiedliche räumliche Gebiete und Verwendungszwecke differenzierter zu beurteilen.

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

Die Sitzung dauert **90 Minuten**: 10 Minuten JiTT-Besprechung, 75 Minuten für neue Inhalte und angeleitete Übungen sowie 5 Minuten Abschluss. Erklärungen und Beispiele setzen keine vorherige Lektüre der Kursseiten voraus. Kurze Austauschrunden finden mit den Sitznachbarinnen und Sitznachbarn statt.

| Zeit | Aktivität |
|---:|---|
| 0–10 Minuten | JiTT-Antworten zu Unit 08 besprechen und Verständnisfragen klären |
| 10–20 Minuten | Raumbezug am Zahlenpaar `50,81 / 8,77` gemeinsam erschließen |
| 20–35 Minuten | Breite, Länge, Einheiten und Reihenfolge erklären; Koordinaten zu zweit lesen |
| 35–45 Minuten | Fünf Koordinatenpaare auf Plausibilität prüfen und gemeinsam auflösen |
| 45–60 Minuten | Zwei Projektionsdarstellungen vergleichen und Verzerrungen besprechen |
| 60–75 Minuten | WGS 84, UTM und Web Mercator drei Verwendungszwecken zuordnen |
| 75–85 Minuten | CRS zuweisen oder transformieren: zwei Fehlerfälle gemeinsam begründen |
| 85–90 Minuten | Zentrale Ergebnisse sichern, eine Exit-Ticket-Frage gemeinsam beantworten und auf JiTT hinweisen |

### Schwerpunkt und Umfang

* **Kernübung:** In „Koordinaten“ bearbeiten wir „Koordinaten lesen“ und „Daten prüfen“. Entscheidend sind Reihenfolge, Einheit, Wertebereich und Raumbezug.
* **Gemeinsame Besprechung:** Projektionsvergleich und CRS-Auswahl erfolgen an vorgegebenen Beispielen. Jede Entscheidung wird kurz zu zweit begründet und anschließend im Plenum geklärt.
* **Freiwillige Vertiefung:** Eigenständige Ortsrecherche, weitere EPSG-Recherchen und das Umrechnen von Grad-Minuten-Sekunden gehören nicht zum Pflichtumfang der Sitzung.
* **Ergebnissicherung:** Am Ende halten wir fest, welche Angaben Koordinaten eindeutig machen und wann Zuweisen beziehungsweise Transformieren erforderlich ist.

Die ausführlichen Unterseiten dienen auch als Nachschlagewerk. Für die Sitzung gilt die oben beschriebene Auswahl; weitere Übungen sind freiwillige Vertiefung. Nicht abgeschlossene Arbeit wird nicht als Hausaufgabe nachgeholt. Zwischen den Terminen beantworten Sie ausschließlich die **JiTT-Fragen zu Unit 09 in ILIAS**.

<!-- Hinweise für Lehrende zur 90-Minuten-Sitzung:
Zahlenpaare, zwei Projektionsdarstellungen und zwei CRS-Fehlerfälle vorab für den Beamer bereithalten. Keine Softwareinstallation oder individuelle Portalsuche in dieser Sitzung einplanen.
Bei mehr Klärungsbedarf im JiTT-Block einen zusätzlichen Vergleich oder eine Übungsvariante kürzen. Ergebnissicherung und Abschluss beibehalten. Aus den folgenden Exit-Ticket-Fragen eine passend zur Sitzung auswählen und kurz gemeinsam auflösen.
-->

## Exit-Ticket

Wir wählen zum Abschluss eine der folgenden Fragen aus und beantworten sie gemeinsam ohne Nachschlagen:

1. Welche Angaben fehlen, wenn nur das Zahlenpaar `(8.77, 50.81)` vorliegt?
2. Welches der behandelten CRS würden Sie für Entfernungsmessungen rund um Marburg zuerst prüfen – und warum?
3. Was ändert sich beim Transformieren eines Datensatzes, und was bleibt gleich?

<a id="transfer-für-lehramtsstudierende"></a>

## Gemeinsam Projektionen beurteilen

Diese Aktivität bearbeiten alle Studierenden im Zeitblock **45–60 Minuten**. Vergleichen Sie die beiden gezeigten Projektionsdarstellungen zunächst **2 Minuten zu zweit**:

1. Benennen Sie eine sichtbare Veränderung der Form oder der relativen Größe einer Landfläche.
2. Erklären Sie, warum die Fläche auf der Erde dadurch nicht größer oder kleiner geworden ist.
3. Formulieren Sie einen Satz, der eine mögliche Fehlinterpretation der Karte verhindert.

Anschließend vergleichen wir **3 Minuten im Plenum** ausgewählte Begründungen und ordnen sie den besprochenen Verzerrungen zu.

<!-- Erwartung: Die Projektion beeinflusst die Kartendarstellung. Sichtbare Größenverhältnisse dürfen ohne Kenntnis der Projektion nicht als tatsächliche Flächenverhältnisse gelesen werden. -->

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

## Folien zu dieser Unit

{% include pdf pdf="Geodaten_Slides_Unit09.pdf" %}
