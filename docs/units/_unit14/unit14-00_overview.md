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

Damit verfügen wir nun über Punkt-, Linien-, Polygon- und Rasterdaten sowie erste Ergebnisse räumlicher Auswertungen. Zu Beginn besprechen wir **10 Minuten lang die JiTT-Antworten zu Unit 13**. An ein bis zwei ausgewählten Verständnisfragen klären wir die wichtigsten offenen Punkte und knüpfen an die vorige Sitzung an.

<!-- Introtext: Allgemeine Einleitung zum Thema im neuen Lernabschnitt und Verbindung zum vorangegangenen Thema. Worum geht es, welche Inhalte werden bearbeitet und warum sind diese wichtig? -->

## Einführung in Lernabschnitt 14

Eine Karte zeigt Daten nicht einfach neutral an. Bereits die Auswahl der Layer, Farben, Symbole, Klassengrenzen und des Kartenausschnitts beeinflusst, welche räumlichen Muster sichtbar werden.

In dieser Unit lernen wir deshalb, Geodaten **sachgerecht, verständlich und nachvollziehbar** zu visualisieren. Wir führen die Ergebnisse der vorherigen Units in einem vollständigen kleinen Geo-Workflow zusammen:

> **Wie verteilen sich die dokumentierten Beobachtungen einer Art im Untersuchungsgebiet, und in welchen Höhenlagen liegen sie?**

Aus dieser Frage entwickeln wir eine Karte für eine festgelegte Zielgruppe. Dazu prüfen wir die vorbereiteten Daten, begründen Symbolisierung und Klassifizierung, arbeiten ein vorhandenes Kartenlayout aus und dokumentieren unsere Entscheidungen.

<!-- Aktuelle Lerneinheit: Welcher konkrete Inhalt erwartet die Studierenden? -->

## In dieser Lerneinheit ...

In dieser Lerneinheit beschäftigen wir uns mit vier aufeinander aufbauenden Fragen:

1. **Wie werden Geodaten passend symbolisiert?**  
   Wir wählen Symbole, Farben, Größen, Linienbreiten und Transparenzen passend zu Geometrietyp und Datenart.

2. **Wie werden Zahlenwerte sinnvoll klassifiziert?**  
   Wir vergleichen gleiche Intervalle, Quantile, natürliche Unterbrechungen und fachlich begründete Klassengrenzen.

3. **Wie entsteht aus der Kartenansicht ein vollständiges Kartenlayout?**  
   Wir überarbeiten Titel und Legende einer vorbereiteten Layoutvorlage und kontrollieren Kartenausschnitt, Maßstab und Quellenangabe.

4. **Wie wird der gesamte Workflow nachvollziehbar?**  
   Wir verbinden Fragestellung, Datenprüfung, Analyse, Gestaltung, Export und Interpretation zu einem nachvollziehbaren und wiederholbaren Arbeitsablauf.

Die abschließende Arbeitslogik lautet:

> **Fragestellung → Zielgruppe → Daten auswählen → Daten prüfen → analysieren → symbolisieren → klassifizieren → Layout erstellen → exportieren → interpretieren und dokumentieren**

<!-- Lernziele: Was sollten Studierende am Ende dieser Lerneinheit wissen und anwenden können? -->

## Lernziele

### Verbindliche Kernziele

Am Ende der gemeinsamen Sitzung sind Studierende in der Lage, ...

* die vorgegebene Kartenfrage und Zielgruppe in eine lesbare visuelle Hierarchie sowie eine passende Symbolisierung und Farbpalette zu übersetzen,
* gleiche Intervalle und Quantile bei gleicher Klassenzahl und Farbpalette zu vergleichen, eine Methode begründet auszuwählen und ihre Klassengrenzen zu prüfen,
* eine vorbereitete QGIS-Layoutvorlage mit aussagekräftigem Titel, überarbeiteter Legende, Maßstab und Quellenangabe zu einer verständlichen Karte auszuarbeiten,
* die Karte als PDF und PNG zu exportieren und beide Ausgaben in ihrer vorgesehenen Größe zu kontrollieren und
* Gestaltungs- und Klassifizierungsentscheidungen zu dokumentieren sowie eine durch die Daten gedeckte räumliche Aussage mit ihren Grenzen zu formulieren.

### Vertiefung und Nachschlagen

Die ausführlichen Unterseiten ermöglichen außerdem, ...

* weitere Farbpaletten und Klassifizierungsverfahren wie natürliche Unterbrechungen differenzierter zu beurteilen,
* ein Kartenlayout neu anzulegen und zusätzliche Elemente wie Nordpfeil, Koordinatengitter oder Übersichtskarte begründet einzusetzen und
* den vollständigen Geo-Workflow ausgehend von den Eingangsdaten selbstständig zu rekonstruieren und ausführlicher zu dokumentieren.

<!-- Organisatorisches: Gibt es Formalitäten, welche noch geklärt werden sollten? -->

## Organisatorisches

Laden Sie das [Marburger Übungspaket mit Anleitung]({{ '/material/marburg.html' | relative_url }}) herunter und entpacken Sie es vollständig in einen lokalen Arbeitsordner. Alle folgenden Dateipfade beziehen sich auf diesen Ordner; Quellen und vorbereitete Dokumentationsvorlagen liegen in `documentation/`.

Für die gemeinsame Sitzung öffnen alle das vorbereitete Projekt **`unit14_start.qgz`** und speichern sofort eine Arbeitskopie als `unit14_abschluss.qgz`. Das Startprojekt enthält das Layout `abschlusskarte_unit14`, die geprüften Ersatzdaten und höchstens einen zurückhaltenden Hintergrundlayer. Dadurch beginnen alle mit demselben kontrollierten Stand.

Die Kartenübung verwendet die 35 Nachweise mit gültigem `hoehe_m`; 21 weitere geprüfte Nachweise haben im DGM-Ausschnitt keinen Höhenwert. Diese Einschränkung gehört in die Kartenaussage. Das Startprojekt verweist auf `ersatz/unit14_results.gpkg`; seine Verwendung wird im Protokoll vermerkt. Projekt-CRS bleibt **`EPSG:25832`**.

Verbindliche Produkte der Sitzung sind:

```text
unit14_abschluss.qgz
figures/abschlusskarte_unit14.pdf
figures/abschlusskarte_unit14.png
documentation/processing_notes.md
```

Die Verwendung eigener Ergebnisse aus Unit 13 und das Erzeugen von `data_output/unit14_results.gpkg/gbif_mit_hoehe_final` sind freiwillige Vertiefung. In der gemeinsamen Sitzung werden keine Analysen aus Units 11–13 wiederholt und keine Datenquellen ausgetauscht.

## Ablauf der Sitzung

Die Sitzung dauert **90 Minuten**: 10 Minuten JiTT-Besprechung, 75 Minuten für neue Inhalte und angeleitete Übungen sowie 5 Minuten Abschluss. Erklärungen und Beispiele setzen keine vorherige Lektüre der Kursseiten voraus. Kurze Austauschrunden finden mit den Sitznachbarinnen und Sitznachbarn statt.

| Zeit | Aktivität |
|---:|---|
| 0–10 Minuten | JiTT-Antworten zu Unit 13 besprechen und Verständnisfragen klären |
| 10–18 Minuten | Startprojekt als Arbeitskopie speichern; Kartenfrage, Zielgruppe, Punktzahl und Höhenfeld klären |
| 18–30 Minuten | Zwei vorbereitete Klassifizierungen mit jeweils fünf Klassen vergleichen und eine Methode begründen |
| 30–45 Minuten | Gewählte Klassifizierung mit fünf Klassen umsetzen und eine einfache Layerhierarchie prüfen |
| 45–62 Minuten | Vorbereitetes Layout gezielt anpassen: Titel und Legende überarbeiten; Kartenausschnitt, Maßstab und Quellen kontrollieren |
| 62–70 Minuten | Karte als PDF und PNG exportieren und beide Dateien öffnen |
| 70–80 Minuten | Partnercheck durchführen, eine wichtige Korrektur übernehmen und betroffenen Export erneuern |
| 80–85 Minuten | Klassifizierung, Quellen und eine fachliche Aussagegrenze im vorbereiteten Protokoll festhalten |
| 85–90 Minuten | Zentrale Ergebnisse sichern, eine Exit-Ticket-Frage gemeinsam beantworten und auf JiTT hinweisen |

### Schwerpunkt und Umfang

* **Kernübung:** Alle arbeiten mit `unit14_start.qgz`, den darin enthaltenen 35 Nachweisen und höchstens einem vorbereiteten Hintergrundlayer. Eigene Datenquellen werden während der gemeinsamen Übung nicht eingebunden.
* **Gemeinsame Besprechung:** Gleiche Intervalle und Quantile werden anhand zweier vorbereiteter Darstellungen mit jeweils fünf Klassen und derselben Farbpalette verglichen. Danach setzen wir genau eine begründete Variante um.
* **Gezielte Kürzung:** Wir verändern nur Klassifizierung, Titel und Legende. Kartenausschnitt, Maßstab und Quellen werden kontrolliert und nur bei einem erkennbaren Fehler korrigiert. Ein neues Layout, zusätzliche Kontextlayer, natürliche Unterbrechungen, Koordinatengitter und Übersichtskarten bleiben freiwillige Vertiefung.
* **Ergebnissicherung:** Arbeitsprojekt, PDF, PNG mit 150 dpi und der Abschnitt zu Unit 14 im vorbereiteten Protokoll entstehen in der Sitzung. Beim Partnercheck wird eine wichtige Korrektur direkt übernommen und nur der betroffene Export erneuert.

Die ausführlichen Unterseiten dienen auch als Nachschlagewerk. Für die Sitzung gilt die oben beschriebene Auswahl; weitere Übungen sind freiwillige Vertiefung. Nicht abgeschlossene Arbeit wird nicht als Hausaufgabe nachgeholt. Zwischen den Terminen beantworten Sie ausschließlich die **JiTT-Fragen zu Unit 14 in ILIAS**.

<!-- Hinweise für Lehrende zur 90-Minuten-Sitzung:
`unit14_start.qgz` mit geprüftem Punkteingang, genau einem zurückhaltenden Hintergrundlayer und dem Layout `abschlusskarte_unit14` verwenden. Quellen, Maßstab und bisherige Verarbeitungsschritte vorab eintragen; nur Klassifizierung, Titel, Legende und eigene Begründung bearbeiten lassen. Zwei Klassifizierungsbilder und die fertige Beispielkarte bereithalten. Spätestens in Minute 45 zum Layout und in Minute 62 zum Export wechseln. Bei technischen Problemen am Beispielprojekt fortfahren; Export, Partnercheck und fachliche Aussagegrenze beibehalten.
Bei mehr Klärungsbedarf im JiTT-Block einen zusätzlichen Vergleich oder eine Übungsvariante kürzen. Ergebnissicherung und Abschluss beibehalten. Aus den folgenden Exit-Ticket-Fragen eine passend zur Sitzung auswählen und kurz gemeinsam auflösen.
-->

## Exit-Ticket

Wir wählen zum Abschluss eine der folgenden Fragen aus und beantworten sie gemeinsam ohne Nachschlagen:

1. Wie beeinflusst die Klassifizierung die sichtbare Aussage?
2. Welche drei Kartenelemente benötigen fast immer eine bewusste redaktionelle Überarbeitung?
3. Welche Aussage darf aus den dokumentierten Beobachtungen nicht abgeleitet werden?

<a id="transfer-für-lehramtsstudierende"></a>

## Gemeinsam die Abschlusskarte prüfen

Diese Aktivität bearbeiten alle Studierenden im Zeitblock **70–80 Minuten**. Zeigen Sie sich zu zweit die exportierten Karten; bei technischen Problemen verwenden Sie die bereitgestellte Beispielkarte.

1. **3 Minuten:** Prüfen Sie gegenseitig, ob Titel, Legende und Quellen verständlich sind und die Karte dokumentierte Nachweise angemessen beschreibt.
2. **2 Minuten:** Geben Sie einander jeweils eine konkrete Rückmeldung zur wichtigsten Verbesserung.
3. **5 Minuten:** Übernehmen Sie diese Korrektur und exportieren Sie die betroffene Datei erneut. Prüfen Sie bei einer Änderung des Karteninhalts beide Exportformate.

Als Maßstab gilt die gemeinsame Kartenfrage: Wo liegen die dokumentierten Beobachtungen, und welchen Höhenklassen sind sie zugeordnet?

<!-- Erwartung: Priorität haben missverständliche Aussagen, unklare Klassen oder fehlende Quellen. Eine Karte dokumentierter Nachweise darf keine vollständige Verbreitung oder einen ursächlichen Einfluss der Höhe behaupten. -->

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

## Folien zu dieser Unit

{% include pdf pdf="Geodaten_Slides_Unit14.pdf" %}
