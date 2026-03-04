---
title: Geodaten
layout: splash
date: '2026-10-12 09:15:00 +0100'
header:
  overlay_color: "#000"
  overlay_filter: 0.6
  overlay_image: "/assets/images/title.png"
  caption: 'Image: [solar.empire via flickr.com](https://www.flickr.com/photos/solar-empire/23815961328/) [CC BY-NC 2.0 DEED](https://creativecommons.org/licenses/by-nc/2.0/)'
  cta_label: go to course units
  cta_url: "/units.html"
excerpt: Einführung in die Arbeit mit Geodaten.
feature_row_intro:
- excerpt: Bachelor level course at the Department of Geography at the University of Marburg.
feature_row_ilos:
- image_path: "/assets/images/envobs_ilos.jpg"
  alt: PC monitor laying in the garden of the institute.
  title: Intended learning outcomes
  excerpt: "Template..."
---

{% include feature_row id="feature_row_intro" type="center" %}

## Motivation

Daten mit Raumbezug liefern wichtige Daten für alle Bereiche des Lebens; sie helfen Enscheidungsträgern, können in der Prognose zukünftiger Bedingungen eingestetzt werden 
Mit fortschreitenden technologischen Möglichkeiten - sowohl in der Datenaufnahme, als auch in Analysemöglichkeiten, ist die Menge an Daten allerdings exponentiell gestiegen. Das Potential, dass mit diesem  sog. Datalake / Datensee, also Datendepot, in dem all diese Daten herinfließen, kann sich aber nur entfalten, wenn die Daten nutzbar gemacht werden - und auch so bleiben.
In der Realität sieht das aber häufig anders - wichtige Informationen gehen verloren, so dass zB keine informationen zu Daenherkunft mehr vorhanden sind, sie sind nicht gut strukturiert oder auffindbar. Damit "versumpft" der datalake schnell - und wird zu einem dataswamp, durch den es kein Durchkommen gibt. Deswegen ist vernünftiges Datenmanagement entscheident - sowohl im wissenschaftlichen, wirtschaftlichen als auch im Kontext eines möglichst effizienten Studiums, immerhin wollen Sie Daten, die sie in späteren Übungen und ihrer Abschlussarbeit bearbeiten, nicht erst lange suchen müssen / allzeit für ihre reports wissen, was sie wann mit den Daten gemacht haben, relevante Informatuionen auffinden.,   

<!-- “Everything is related to everything else, but near things are more related than distant things” [(Tobler, 1970)](https://www.tandfonline.com/doi/abs/10.2307/143141). <br>
With this sentence, Waldo R. Tobler ... <br> made geographic history, although his main concern was to reduce the complexity of his population simulation model so that it could be calculated at all on the IT infrastructure of the 1970s.
Fifty years later, society is facing other major challenges. Environmental and climate change is leading to species loss rates comparable only to the great mass extinctions. Ecosystem functionality will change, with consequences for ecosystem services such as food production, climate regulation, or recreation.
Understanding environmental change and assessing consequences requires spatial information from landscapes. The crucial question is not whether a landscape contains forest, meadow, field, and river, but how they relate to each other spatially. Simply put, if a strip of forest separates the river from the cropland, the forest acts as an important barrier to the input of nutrients from the cropland into the river. If a clearing is present in the forest, habitat complexity increases, increasing the likelihood of biodiversity and resilience to environmental change. 
When collecting spatial information in the field, a tradeoff must be made between level of detail, scale, and temporal repetition. Selected processes can either be studied in detail at a very limited number of observation sites or estimated at a generalized scale for a landscape. The constraints loosen when linking local surveys with area-wide remote sensing observations and predicting the locally collected information in space with artificial intelligence methods. -->


## Learning objectives

Nach Abschluss können Studierende:

* Daten strukturiert organisieren, Methoden zur Datenbereinigung anwenden
* Einfache deskriptive Statistik anwenden
* Punkt-, Raster- und Vektordaten unterscheiden  
* Datensätze nach FAIR-Prinzipien dokumentieren

<!--
# Setting

This course will take place in a hybrid synchronous setting in presence in room F 14 | 00A19 and online. 
In addition, there will be regular meetings with a tutor. 
Details on the additional tutor sessions will be provided in the first regular session, which will take place on **Dayday ??.10.2026 at 9:15 am** (German time) in room F 14 | 00A19. 
The virtual room for online participants must be accessed via [ILIAS](please insert ILIAS link). 
Note that the tutor sessions are voluntary.
{: .notice--info}


# Syllabus
The course covers 9 units:

<!-- Datalake flowchart einfügen -->

Der Kurs umfasst 9 Units:

1) Von bits zu Informationen - Wie Daten und Computer funktionieren
   Am Ende der Unit sind Sie in der Lage
   * Binärsystem, Bits & Bytes erklären
   * Unterschied zwischen Speicher, RAM und Prozessor verstehen
   * Kodierung (Text, Zahlen, Bilder) grundlegend erklären
   * Dateiformate als Strukturierungsprinzip verstehen

2) Daten basics - Datentypen und -Formate (in Excel)
   Am Ende der Unit sind Sie in der Lage
   * Unterschiede zwischen verschiedenen Datentypen zu erklären
   * Encoding-Probleme (z.B. Umlaute) erkennen
   * „Tidy Data“-Prinzip verstehen (eine Beobachtung pro Zeile)
   * Koordinatenformate (dezimal vs. Grad/Minute/Sekunde) unterscheiden
   * Metadaten anzulegen
   * grundlegende Excel-Funktionalitäten zu beherrschen (zB. absolute vs. relative Zellbezüge)

3) Daten organisieren - Aufbereitung von Daten mit Textfunktionen, Sortieren, Filterfunktion
   Am Ende dieser Unit sind Sie in der Lage:
   * Sinnvolle Ordnerstrukturen anzulegen
   * Daten zu sortieren und filtern
   * Doppelte Einträge zu identifizieren
   * Textfunktionen anwenden (z.B. TEIL, GLÄTTEN, ERSETZEN)
   * Fehlende Werte identifizieren
   * einfache Qualitätskontrollen durchzuführen
   * Bereinigungsschritte zu dokumentieren (ReadMe)

4) Daten verstehen - deskriptive Statistik (Streuung, Mittelwerte, Korrelationen)
   Am Ende dieser Unit sind Sie in der Lage:
   * Mittelwert, Median und Modus zu berechnen und zu interpretieren
   * Varianz und Standardabweichung zu erklären
   * Verteilungen zu interpretieren


5) Zusammenhänge erkennen - Korrelationen und Zusammenhänge
   <!-- Recap: Dateinamen der letzten Übungen, Zeit messen, ohne in das vorherige Chapter zu schauen; was wurde gemacht? / Quiz und wordbubble /  -->
   Am Ende dieser Unit sind Sie in der Lage
   * Pearson-Korrelation zu berechnen
   * Scatterplots zu interpretieren
   * Pivot-Tabellen zu erstellen
   * Häufigkeitstabellen zu erzeugen

6) Exkurs: Fuktionen und Automatisierung
   Am Ende dieser Unit sind Sie in der Lage:
   * Einfache Automatisierung (Formeln, Kopieren, Serien)

7) Daten zugänglich machen
   Am Ende dieser Unit sind Sie in der Lage:
   * FAIR Prinzipien zu erklären
   * Dokumentation / ReadMe zu erstellen
   * Git nachzuvollziehen

8) QGIS & WMS
   eine Einführung

9) Besonderheiten Geodaten: point, raster und vector Daten
   (3 Kurstage)



<!-- vermutlich besser Teil 3 zu 2 vorzuziehen, damit die Studis schon Mal Daten in der Hand hatten (Aufgabe dann in Datenmanagement: Findet die Daten der letzten ~ 6 sessions wieder) -->

<!-- statt Karten (ist schon in QGIS) noch andere open source + coding/scriptsteuerung Möglichkeiten anteasen, bsp. R/python. Hier nur wirklich ganz grob das Prinip solcher programmiersprachen als Möglichkeit der automatisierung darstellen, Level "Hello World", einbinden wie zB im R Kurs, auf die Aufbauenden Kurse (BaseR, python, Grass: Chris? Christiane vllt?) verweisen -->

| Session | Date | Topic | Content |
|---------|------|-------|---------|
||| **Einführung** |
| 01 | ??.??.2026 | Einführung | Orga & Überblick & Computerbasics |
||| **01 Methoden Excel, deskriptive Statistik** |
| 02 | ??.??.2026 | Tabellenverarbeitung I | Excel basics & Koordinaten |
| 03 | ??.??.2026 | Tabellenverarbeitung II | mehr Excel & Datenanalyse |
| 04 | ??.??.2026 | Tabellenverarbeitung III | Funktionen, Protokolle |
||| **02 Umgang mit Daten und Datenmanagement** |
| 05 | ??.??.2026 | Forschungsdatenmanagement I | Ordnerstruktur, Dateinamen, FAIR, Metadaten |
| 06 | ??.??.2026 | Forschungsdatenmanagement II | Ordnerstruktur, Dateinamen, FAIR, Metadaten |
||| **03 Eigenschaften von Geodaten** |
| 07 | ??.??.2026 | Projektionen, Eigenschaften von Geodaten | Projektionen, Eigenschaften von Geodaten |
| 08 | ??.??.2026 | Räumliche Autokorrelation, Datentypen, Beispiele von Datenbanken | Räumliche Autokorrelation, Datentypen, Beispiele von Datenbanken |
||| **04 Open-source tools** |
| 09 | ??.??.2026 | Einführung QGIS | Projektionen verwalten, layer erstellen, WMS Import |
||| **05 Beispiele** |
| 10 | ??.??.2026 | Forschungsdaten I | Point: Applied example, GBIF gobal & Fragestellung |
| 11 | ??.??.2026 | Forschungsdaten II |Raster: Applied example, BGR Deutschland, Geoportal & Fragestellung |
| 12 | ??.??.2026 | Forschungsdaten III |Vector: Applied example, BGR, Geoportal Marburg? & Fragestellung |
||| **06 Visualisierungen** |
| 13 | ??.??.2026 | Karten | Paletten, Klassifizierungen |
||| **Feedback** |
| 14 | ??.??.2026 | Abschlusssession | Time for questions and feedback, goodbye |


<!--
| Unit | Topic | Learning Content |
|-------------|-------|-------------|
|**01**| **Big questions are spatial** |On the invalidity of the first law of geography in heterogeneous spaces.|
|**02**| **Remote sensing 101** |A brief introduction to remote sensing using optical sensors as an example.|
|**03**| **Deep learning** |Deep-learning and spatial patterns.|
|**04**| **Final team project: spatial prediction** |From curiosity to research question and project planning.|
-->


# Preparation and prerequisites

The course assumes basic knowledge and skills in using your brain.

Also check our additional material for teaching basic R skills, 
which can be found [here](https://geomoer.github.io/moer-base-r/){:target="_blank"}.
{: .notice--success}




## Team

{% for author in site.data.authors %}
  {% include author-profile.html %}
 <br />
{% endfor %}
