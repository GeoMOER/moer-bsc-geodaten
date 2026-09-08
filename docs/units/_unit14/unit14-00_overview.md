---
title: Überblick
published: true
toc: true
header:
  image: /assets/images/unit14/hero-unit14.jpg
  image_description: "Fertig gestaltete thematische Karte mit Höhenrelief, Flusslauf und kartographischen Nebenelementen"
  caption: "KI-generierte Illustration, bearbeitet für diesen Kurs"
---

<!-- Rückblick: Welche Themeninhalte wurden in der letzten Kurssitzung bearbeitet? Sind Fragen zur letzten Kurssitzung offen geblieben? -->

## Rückblick & Fragen

In der letzten Kurssitzung haben wir das Rastermodell untersucht. Wir haben ein digitales Geländemodell in QGIS geprüft und dargestellt und die Höhenwerte des Rasters auf die GBIF-Beobachtungspunkte übertragen.

Damit verfügen wir nun über Punkt-, Linien-, Polygon- und Rasterdaten sowie erste Ergebnisse räumlicher Auswertungen. Bevor wir mit dem letzten Lernabschnitt beginnen, klären wir offene Fragen zu Rasterzellen, Auflösung, NoData und dem Abtasten von Rasterwerten.

<!-- Introtext: Allgemeine Einleitung zum Thema im neuen Lernabschnitt und Verbindung zum vorangegangenen Thema. Worum geht es, welche Inhalte werden bearbeitet und warum sind diese wichtig? -->

## Einführung in Lernabschnitt 14

Eine Karte zeigt Daten nicht einfach neutral an. Bereits die Auswahl der Layer, Farben, Symbole, Klassengrenzen und des Kartenausschnitts beeinflusst, welche räumlichen Muster sichtbar werden.

In dieser Unit lernen wir deshalb, Geodaten **sachgerecht, verständlich und nachvollziehbar** zu visualisieren. Wir führen die Ergebnisse der vorherigen Units in einem vollständigen kleinen Geo-Workflow zusammen:

> **Wie verteilen sich die dokumentierten Beobachtungen einer Art im Untersuchungsgebiet, und in welchen Höhenlagen liegen sie?**

Aus dieser Frage entwickeln wir eine Karte für eine festgelegte Zielgruppe. Dazu wählen wir die benötigten Daten, begründen die Symbolisierung und Klassifizierung, erstellen ein Kartenlayout und dokumentieren unsere Entscheidungen.

<!-- Aktuelle Lerneinheit: Welcher konkrete Inhalt erwartet die Studierenden? -->

## In dieser Lerneinheit ...

In dieser Lerneinheit beschäftigen wir uns mit vier aufeinander aufbauenden Fragen:

1. **Wie werden Geodaten passend symbolisiert?**  
   Wir wählen Symbole, Farben, Größen, Linienbreiten und Transparenzen passend zu Geometrietyp und Datenart.

2. **Wie werden Zahlenwerte sinnvoll klassifiziert?**  
   Wir vergleichen gleiche Intervalle, Quantile, natürliche Unterbrechungen und fachlich begründete Klassengrenzen.

3. **Wie entsteht aus der Kartenansicht ein vollständiges Kartenlayout?**  
   Wir gestalten Kartenausschnitt, Titel, Legende, Maßstab, Quellenangabe und weitere notwendige Elemente.

4. **Wie wird der gesamte Workflow nachvollziehbar?**  
   Wir verbinden Fragestellung, Datenprüfung, Analyse, Gestaltung, Export und Interpretation zu einem reproduzierbaren Arbeitsablauf.

Die abschließende Arbeitslogik lautet:

> **Fragestellung → Zielgruppe → Daten auswählen → Daten prüfen → analysieren → symbolisieren → klassifizieren → Layout erstellen → exportieren → interpretieren und dokumentieren**

<!-- Lernziele: Was sollten Studierende am Ende dieser Lerneinheit wissen und anwenden können? -->

## Lernziele

Am Ende dieser Unit sind Studierende in der Lage, ...

* Symbolisierungsentscheidungen aus Geometrietyp, Datenart und Aussageziel abzuleiten,
* qualitative, sequentielle und divergierende Farbpaletten passend einzusetzen,
* Punkt-, Linien-, Polygon- und Rasterlayer zu einer lesbaren visuellen Hierarchie zu verbinden,
* kategoriale und numerische Attribute unterschiedlich darzustellen,
* gleiche Intervalle, Quantile und natürliche Unterbrechungen grundlegend zu unterscheiden,
* Klassenzahl und Klassengrenzen zu prüfen und zu begründen,
* zu erklären, wie verschiedene Klassifizierungen die Wahrnehmung derselben Daten verändern,
* in QGIS ein übersichtliches Kartenlayout anzulegen,
* Titel, Legende, Maßstab und Quellenangabe passend zur Karte zu gestalten,
* zu beurteilen, ob Nordpfeil, Koordinatengitter oder weitere Elemente tatsächlich benötigt werden,
* eine Karte als PDF und Bilddatei zu exportieren,
* den vollständigen Workflow von der Fragestellung bis zur räumlichen Aussage zu dokumentieren und
* Grenzen und Unsicherheiten der Karte transparent zu benennen.

<!-- Organisatorisches: Gibt es Formalitäten, welche noch geklärt werden sollten? -->

## Organisatorisches

Für die praktische Arbeit benötigen Sie QGIS sowie die vorbereiteten oder selbst erzeugten Ergebnisse aus den Units 11–13:

* geprüfte GBIF-Beobachtungspunkte,
* Punktlayer mit abgetasteten Höhenwerten,
* digitales Geländemodell,
* optional Schutzgebiete und Gewässer als räumlicher Kontext.

Falls einzelne Ergebnisse fehlen, werden einheitliche Ersatzlayer bereitgestellt. Verwenden Sie für die Abschlusskarte nur Layer, die zur Fragestellung beitragen. Eine größere Zahl sichtbarer Layer macht eine Karte nicht automatisch informativer.

Verwenden Sie dasselbe Projekt-CRS wie in Units 10–13: **`[EPSG-Code ergänzen; für Marburg voraussichtlich EPSG:25832]`**. Verbindlicher Eingang ist `unit13_results.gpkg/gbif_mit_hoehe` mit dem Feld `hoehe_m`.

Die Abschlussprodukte sind:

```text
data_output/unit14_results.gpkg
└── gbif_mit_hoehe_final
figures/abschlusskarte_unit14.pdf
figures/abschlusskarte_unit14.png
documentation/processing_notes.md
```

## Ablauf der Sitzung

Die Unit ist für ungefähr **150 Minuten** oder zwei kürzere Sitzungen ausgelegt.

| Zeit | Aktivität |
|---:|---|
| 0–25 Minuten | Datenart, visuelle Variablen und Farbpaletten |
| 25–50 Minuten | Klassifizierungen vergleichen und begründen |
| 50–75 Minuten | visuelle Hierarchie der Layer herstellen |
| 75–110 Minuten | Kartenlayout für eine Zielgruppe erstellen |
| 110–130 Minuten | PDF und PNG exportieren und kontrollieren |
| 130–145 Minuten | Peer-Check und Überarbeitung |
| 145–150 Minuten | Exit-Ticket |

## Exit-Ticket

1. Wie beeinflusst die Klassifizierung die sichtbare Aussage?
2. Welche drei Kartenelemente benötigen fast immer eine bewusste redaktionelle Überarbeitung?
3. Welche Aussage darf aus den dokumentierten Beobachtungen nicht abgeleitet werden?

## Transfer für Lehramtsstudierende

Überarbeiten Sie die Abschlusskarte für eine konkret benannte schulische Zielgruppe. Formulieren Sie Lernziel, didaktische Reduktion, Arbeitsauftrag, Hilfestellung und Kriterien, anhand derer Lernende eine irreführende Kartengestaltung erkennen können.

<!-- Notizen: Ab hier folgen Vermerke, welche als Gedankenstütze oder Erinnerung dienen aber noch nicht in der vorhandenen Form veröffentlicht werden sollen. -->

<!--
Möglicher Einstieg:
- dieselben Beobachtungsdaten mit zwei sehr unterschiedlichen Farbpaletten und Klassifizierungen zeigen.
- Studierende spontan beschreiben lassen, welche Karte stärkere räumliche Unterschiede suggeriert.

Didaktische Schwerpunkte:
- Visualisierung als Teil wissenschaftlicher Interpretation behandeln.
- erst Aussage und Datenart, dann Farbe oder Symbol wählen.
- Legende und Quellenangabe als fachliche Bestandteile der Karte verstehen.
- Nordpfeil nicht als automatisches Pflichtsymbol darstellen.
- lieber eine klare Aussage mit wenigen Layern als eine überladene „Alles-Karte“.
- Workflow und Unsicherheit gemeinsam mit dem Endprodukt in der Sitzung besprechen.

Vor Durchführung ergänzen:
- verbindliche Leitfrage und Zielgruppe
- finale Eingabedaten und Ersatzlayer
- Feldname des abgetasteten Höhenwertes
- vorgegebenes Projekt-CRS und Untersuchungsgebiet
- gewünschtes Seitenformat und Exportauflösung
- Bearbeitungszeit für die Übungen in der Sitzung

Geplante Unterseiten:
- unit14-01_symbolisierung.md
- unit14-02_klassifizierung.md
- unit14-03_kartenlayout.md
- unit14-04_workflow.md
- unit14-04_assignment.md
-->
