---
title: Überblick
published: true
toc: true
header:
  image: /assets/images/unit13/hero-unit13.jpg
  image_description: "Ein Höhenwert aus einer Rasterzelle wird als neues Attribut an einen Beobachtungspunkt übertragen"
  caption: "Eigene Darstellung"
---

<!-- Rückblick: Welche Themeninhalte wurden in der letzten Kurssitzung bearbeitet? Sind Fragen zur letzten Kurssitzung offen geblieben? -->

## Rückblick & Fragen

In der letzten Kurssitzung haben wir das Vektormodell vervollständigt. Wir haben Punkte, Linien und Polygone gemeinsam in QGIS untersucht, reale Datensätze aus Geoportalen eingebunden und Features anhand ihrer Attribute und räumlichen Lage ausgewählt.

Bevor wir mit dem neuen Lernabschnitt beginnen, klären wir offene Fragen zu Vektorgeometrien, Geoportalen, räumlichen Beziehungen und der Auswahl nach Position.

<!-- Introtext: Allgemeine Einleitung zum Thema im neuen Lernabschnitt und Verbindung zum vorangegangenen Thema. Worum geht es, welche Inhalte werden bearbeitet und warum sind diese wichtig? -->

## Einführung in Lernabschnitt 13

Das Vektormodell eignet sich besonders für einzelne räumliche Objekte: eine Beobachtung, einen Fluss oder ein Schutzgebiet. Manche Phänomene lassen sich jedoch nicht sinnvoll in klar voneinander getrennte Objekte zerlegen. Höhe, Temperatur oder Niederschlag verändern sich kontinuierlich im Raum.

Für solche Daten wird häufig ein **Rastermodell** verwendet. Ein Raster teilt den Raum in ein regelmäßiges Gitter aus Zellen. Jede Zelle speichert einen Wert – beispielsweise die mittlere Geländehöhe in diesem Bereich.

In dieser Unit untersuchen wir ein digitales Geländemodell und verbinden es mit den GBIF-Punkten aus Unit 11. Damit beantworten wir die Leitfrage:

> **Auf welcher Geländehöhe liegen die dokumentierten Artenbeobachtungen?**

So lernen wir nicht nur einen neuen Geodatentyp kennen, sondern führen erstmals Vektor- und Rasterdaten in einer gemeinsamen Auswertung zusammen.

<!-- Aktuelle Lerneinheit: Welcher konkrete Inhalt erwartet die Studierenden? -->

## In dieser Lerneinheit ...

In dieser Lerneinheit beschäftigen wir uns mit drei aufeinander aufbauenden Fragen:

1. **Wie funktioniert das Rastermodell?**  
   Wir betrachten Rasterzellen, Zeilen, Spalten und Zellwerte und unterscheiden kontinuierliche von kategorialen Rasterdaten.

2. **Welche Eigenschaften bestimmen die Aussagekraft eines Rasters?**  
   Wir untersuchen Zellgröße, räumliche Auflösung, Ausdehnung, Ausrichtung, Datentyp, Bänder und NoData-Werte.

3. **Wie untersuchen und kombinieren wir Rasterdaten in QGIS?**  
   Wir laden ein digitales Geländemodell, prüfen seine Eigenschaften, gestalten eine Farbskala, fragen Zellwerte ab und übertragen Höhenwerte auf Beobachtungspunkte.

Die wiederkehrende Arbeitslogik lautet:

> **Fragestellung → Rasterquelle → Rastereigenschaften → Darstellung → Werte abfragen → Ergebnis prüfen und interpretieren**

<!-- Lernziele: Was sollten Studierende am Ende dieser Lerneinheit wissen und anwenden können? -->

## Lernziele

Am Ende dieser Unit sind Studierende in der Lage, ...

* Vektor- und Rasterdaten anhand ihres Datenmodells zu unterscheiden,
* den Aufbau eines Rasters aus Zeilen, Spalten, Zellen und Zellwerten zu erklären,
* kontinuierliche und kategoriale Rasterdaten zu unterscheiden,
* ein digitales Geländemodell von einem digitalen Oberflächenmodell abzugrenzen,
* Zellgröße, Auflösung, Ausdehnung und Rasterausrichtung zu beschreiben,
* zu erklären, weshalb räumliche Auflösung und räumliche Genauigkeit nicht dasselbe sind,
* NoData-Werte von fachlich gültigen Werten wie null zu unterscheiden,
* Rasterlayer in QGIS zu laden und ihre Metadaten und Eigenschaften zu prüfen,
* ein kontinuierliches Raster mit einer geeigneten Farbskala darzustellen,
* einzelne Rasterwerte in QGIS abzufragen,
* Rasterwerte an Punktpositionen zu ermitteln und als neue Attribute zu speichern und
* die Aussagekraft und Unsicherheit der ermittelten Werte angemessen zu beurteilen.

<!-- Organisatorisches: Gibt es Formalitäten, welche noch geklärt werden sollten? -->

## Organisatorisches

Für die praktische Arbeit benötigen Sie QGIS, den geprüften GBIF-Punktlayer aus Unit 11 und das bereitgestellte digitale Geländemodell. Falls Ihr eigener Punktlayer nicht verfügbar ist, wird ein einheitlicher Ersatzlayer bereitgestellt.

Rasterdateien können deutlich größer als Vektordateien sein. Kopieren Sie die benötigten Daten deshalb vor Beginn der Übung in Ihren Arbeitsordner und verwenden Sie erneut getrennte Ordner für unveränderte Eingangsdaten, Ergebnisse und Dokumentation.

Verwenden Sie dasselbe Projekt-CRS wie in Units 10–12: **`[EPSG-Code ergänzen; für Marburg voraussichtlich EPSG:25832]`**. Erwarteter Punkteingang ist `unit11_results.gpkg/gbif_checked`; ein Ersatzlayer muss identische Feldnamen und Datentypen besitzen.

Das verbindliche Übergabeprodukt ist:

```text
data_output/unit13_results.gpkg
└── gbif_mit_hoehe
```

Das neue Höhenfeld heißt im gesamten weiteren Kurs **`hoehe_m`**. Falls das QGIS-Werkzeug zunächst einen anderen Feldnamen erzeugt, benennen oder berechnen Sie das finale Feld kontrolliert und dokumentiert.

## Ablauf der Sitzung

Die Unit ist für ungefähr **120 Minuten** ausgelegt.

| Zeit | Aktivität |
|---:|---|
| 0–20 Minuten | Rastermodell, Zellwert, DGM und DOM |
| 20–45 Minuten | Zellgröße, Auflösung, Ausdehnung, NoData und Genauigkeit |
| 45–70 Minuten | DGM laden, Metadaten und Werte prüfen |
| 70–90 Minuten | Raster darstellen und Histogramm untersuchen |
| 90–110 Minuten | Werte an `gbif_checked` abtasten und kontrollieren |
| 110–120 Minuten | Unsicherheiten, Export und Exit-Ticket |

## Exit-Ticket

1. Warum ist eine kleine Rasterzelle kein Beweis für hohe Genauigkeit?
2. Warum darf NoData nicht als Höhenwert null interpretiert werden?
3. Welche Unsicherheiten treffen beim Feld `hoehe_m` zusammen?

## Transfer für Lehramtsstudierende

Entwerfen Sie eine kurze Aufgabe, mit der Schülerinnen und Schüler den Unterschied zwischen Auflösung und Genauigkeit erklären. Verwenden Sie ein Höhenraster, formulieren Sie eine typische Fehlvorstellung und beschreiben Sie eine anschauliche Hilfestellung.

<!-- Notizen: Ab hier folgen Vermerke, welche als Gedankenstütze oder Erinnerung dienen aber noch nicht in der vorhandenen Form veröffentlicht werden sollen. -->

<!--
Möglicher Einstieg:
- Nur die GBIF-Punkte zeigen und fragen: „Welche Geländehöhe gehört zu jedem Punkt?“
- Danach ein DGM einblenden und zunächst die sichtbaren Zellen beziehungsweise Zellwerte untersuchen.

Didaktische Schwerpunkte:
- Raster nicht als „Bild“, sondern als georeferenziertes Wertefeld einführen.
- Zellgröße nicht mit Genauigkeit gleichsetzen.
- NoData ausdrücklich von 0 unterscheiden.
- Farbe ist Darstellung; der Zellwert ist die gespeicherte Information.
- Beim Übertragen der Höhe auf GBIF-Punkte auch die Koordinatenunsicherheit der Beobachtungen diskutieren.

Vor Durchführung ergänzen:
- konkreter DGM-Datensatz und Download
- Datenstand, Lizenz und Quellenangabe
- Zellgröße, Höhenbezug und Einheit
- Projekt- und Ausgabe-CRS
- bereitgestellter GBIF-Punktlayer
- erwartete Ergebniswerte für die Übungen

Geplante Unterseiten:
- unit13-01_rasterdaten.md
- unit13-02_rastereigenschaften.md
- unit13-03_raster_qgis.md
- unit13-04_assignment.md
-->
