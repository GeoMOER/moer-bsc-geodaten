---
title: Geodatenmodelle
published: true
toc: true
header:
  image: /assets/images/unit10/hero-unit10.jpg
  image_description: "Luftbildlandschaft mit überlagerten Punkten, Linien, Polygonflächen und Rasterzellen"
  caption: "KI-generierte Illustration, bearbeitet für diesen Kurs"
---

<!-- Introtext: Von der räumlichen Wirklichkeit zu einer für Computer verarbeitbaren Darstellung. -->

## Von der Wirklichkeit zu Daten

Die räumliche Wirklichkeit ist komplex: Es gibt einzelne Bäume, verzweigte Straßennetze, unscharfe Waldgrenzen und kontinuierliche Übergänge von Höhe oder Temperatur. Ein Computer kann diese Wirklichkeit nicht vollständig speichern. Wir müssen auswählen, welche Eigenschaften für unsere Fragestellung wichtig sind und wie wir sie in Daten übersetzen.

Ein **Geodatenmodell** legt fest, wie räumliche Objekte und Phänomene digital dargestellt werden. Dabei werden Details bewusst ausgewählt, vereinfacht oder weggelassen.

> **Merksatz:** Geodaten sind Modelle der Realität. Das geeignete Modell hängt von Fragestellung, Maßstab und benötigtem Detailgrad ab.

![Vektorfeatures und Rasterzellen modellieren unterschiedliche Aspekte räumlicher Wirklichkeit.]({{ '/assets/images/unit10/datenmodelle.svg' | relative_url }})

## Objekte und kontinuierliche Phänomene

Für eine erste Orientierung können wir zwischen **diskreten Objekten** und **kontinuierlichen Phänomenen** unterscheiden.

### Diskrete Objekte

Diskrete Objekte lassen sich als einzelne Einheiten auffassen. Sie besitzen eine Identität und können häufig voneinander abgegrenzt werden.

Beispiele sind:

* ein einzelner Baum,
* eine Messstation,
* eine Straße,
* ein Gebäude oder
* ein Landkreis.

Solche Objekte werden häufig mit dem **Vektormodell** dargestellt.

### Kontinuierliche Phänomene

Kontinuierliche Phänomene besitzen grundsätzlich an jedem Ort innerhalb eines Gebietes einen Wert. Zwischen benachbarten Orten verändern sich diese Werte oft allmählich.

Beispiele sind:

* Höhe,
* Temperatur,
* Niederschlag,
* Bodenfeuchte oder
* die von einem Satellitensensor gemessene Reflexion.

Solche Phänomene werden häufig mit dem **Rastermodell** dargestellt.

Diese Unterscheidung ist eine hilfreiche Orientierung, aber keine unveränderliche Regel. Auch ein kontinuierliches Phänomen kann beispielsweise durch einzelne Messpunkte erfasst werden. Umgekehrt kann ein abgegrenztes Objekt in einem Raster gespeichert sein.

## Das Vektormodell

Im **Vektormodell** wird die Lage und Form räumlicher Objekte durch Koordinaten beschrieben. Die grundlegenden Geometrietypen sind **Punkt**, **Linie** und **Polygon**.

### Punkte

Ein Punkt beschreibt eine einzelne Position. Er besitzt keine dargestellte Länge oder Fläche.

Typische Beispiele:

* Fundort einer Art,
* Wetterstation,
* Bushaltestelle,
* einzelner Baum oder
* Stadt auf einer kleinmaßstäbigen Übersichtskarte.

### Linien

Eine Linie verbindet mehrere Punkte zu einem Verlauf. Sie besitzt eine dargestellte Länge, aber keine dargestellte Fläche.

Typische Beispiele:

* Straße,
* Flusslauf,
* Wanderweg,
* Bahnstrecke oder
* Grenze als Verlauf.

### Polygone

Ein Polygon ist eine geschlossene Fläche. Es beschreibt die Lage, Form und räumliche Ausdehnung eines Gebietes.

Typische Beispiele:

* Gebäudegrundriss,
* See,
* Schutzgebiet,
* Landkreis oder
* Waldfläche.

| Geometrietyp | beschreibt vor allem | Beispiel |
|---|---|---|
| Punkt | Position | Messstation |
| Linie | Verlauf und Länge | Straße |
| Polygon | Form und Fläche | Gemeindegebiet |

<!-- Optional: Dasselbe Landschaftsbild mit darübergelegten Punkten, Linien und Polygonen zeigen. -->

## Features und Attribute

Ein einzelnes räumliches Objekt in einem Vektorlayer wird häufig als **Feature** bezeichnet. Ein Feature besteht aus:

* einer **Geometrie**, welche Lage und Form beschreibt, und
* **Attributen**, welche die Eigenschaften des Objektes beschreiben.

Ein Baumkataster könnte beispielsweise jeden Baum als Punkt speichern. Die zugehörige Tabellenzeile enthält weitere Eigenschaften:

| baum_id | art | pflanzjahr | höhe_m | Geometrie |
|---:|---|---:|---:|---|
| 101 | Stieleiche | 1998 | 14.2 | Punkt |
| 102 | Winterlinde | 2012 | 7.6 | Punkt |

Jede Tabellenzeile gehört genau zu einem Feature. Wird ein Baum auf der Karte ausgewählt, kann die GIS-Software deshalb die passende Zeile in der Attributtabelle anzeigen.

> **Verbindung zur Tabellenarbeit:** Vektordaten ergänzen tabellarische Sachdaten um eine räumliche Geometrie.

## Das Rastermodell

Im **Rastermodell** wird der Raum in ein regelmäßiges Gitter aus Zeilen und Spalten aufgeteilt. Jede **Rasterzelle** beziehungsweise jedes **Pixel** repräsentiert einen kleinen räumlichen Ausschnitt und speichert einen Wert.

Ein digitales Höhenmodell könnte beispielsweise für jede Rasterzelle die Höhe in Metern enthalten. Ein Landbedeckungsraster könnte stattdessen eine Klasse wie Wald, Acker oder Siedlung speichern.

Wichtige Eigenschaften eines Rasters sind:

* die Größe der Rasterzellen,
* die räumliche Ausdehnung,
* die Bedeutung und Einheit der Zellwerte und
* die Kennzeichnung fehlender Werte als **NoData**.

Die Zellgröße beeinflusst den räumlichen Detailgrad. Kleine Zellen können feinere Strukturen abbilden, führen aber meist zu größeren Datenmengen. Eine kleine Zellgröße beweist jedoch nicht automatisch eine hohe räumliche oder inhaltliche Genauigkeit.

<!-- Die Eigenschaften von Rasterdaten werden in Unit 13 ausführlich behandelt. -->

## Kontinuierliche und kategoriale Raster

Rasterzellen können unterschiedliche Arten von Werten enthalten:

* **kontinuierliche Raster** enthalten Mess- oder Schätzwerte wie Höhe, Temperatur oder Niederschlag,
* **kategoriale Raster** enthalten Klassen wie Wald, Wasser, Acker oder Siedlung.

Raster ist daher nicht gleichbedeutend mit „kontinuierlich“. Das Datenmodell beschreibt zunächst die regelmäßige Anordnung der Zellen. Die Bedeutung der Zellwerte muss zusätzlich aus den Metadaten hervorgehen.

## Vektor und Raster im Vergleich

| Merkmal | Vektor | Raster |
|---|---|---|
| Grundelement | Punkt, Linie oder Polygon | Rasterzelle |
| besonders anschaulich für | einzelne Objekte | flächenhafte Phänomene |
| räumliche Repräsentation | Koordinaten der Geometrie | Lage, Ausrichtung und Größe der Zellen |
| Eigenschaften | Attribute je Feature | Wert je Zelle, gegebenenfalls mehrere Bänder |
| typische Beispiele | Straßen, Gebäude, Schutzgebiete | Höhe, Temperatur, Satellitenbilder |

Keines der beiden Modelle ist grundsätzlich besser. Entscheidend ist, welches Modell die jeweilige Fragestellung sinnvoll unterstützt.

## Dieselbe Realität, verschiedene Modelle

Dasselbe Objekt oder Phänomen kann abhängig vom Maßstab und von der Fragestellung unterschiedlich modelliert werden.

### Beispiel Stadt

Marburg kann dargestellt werden als:

* **Punkt**, wenn auf einer Deutschlandkarte nur die Lage von Städten wichtig ist,
* **Polygon**, wenn das Stadtgebiet untersucht wird, oder
* Ansammlung vieler **Rasterzellen**, wenn ein Satellitenbild ausgewertet wird.

### Beispiel Fluss

Ein Fluss kann dargestellt werden als:

* **Linie**, wenn sein Verlauf im Mittelpunkt steht,
* **Polygon**, wenn Breite und Wasserfläche wichtig sind, oder
* **Raster**, wenn eine Satellitenaufnahme oder ein Überflutungsmodell verwendet wird.

### Beispiel Temperatur

Temperatur kann dargestellt werden als:

* **Punkte**, wenn nur die Messwerte einzelner Wetterstationen vorliegen, oder
* **Raster**, wenn aus diesen Beobachtungen eine flächendeckende Temperaturkarte erstellt wurde.

> **Wichtig:** Das Datenmodell ergibt sich nicht allein aus dem Namen des dargestellten Phänomens. Es ergibt sich aus der Kombination von Datenquelle, Maßstab und Fragestellung.

<!-- Optional: Marburg und einen Fluss jeweils als Punkt/Linie/Polygon/Raster gegenüberstellen. -->

## Das geeignete Datenmodell auswählen

Vor der Auswahl oder Erstellung eines Geodatensatzes helfen folgende Fragen:

1. **Was soll dargestellt werden?**  
   Handelt es sich eher um einzelne Objekte oder um ein flächenhaftes Phänomen?

2. **Welche Frage soll beantwortet werden?**  
   Geht es beispielsweise um Positionen, Verläufe, Flächen, Entfernungen oder Werte an jedem Ort?

3. **Welcher Maßstab und Detailgrad sind erforderlich?**  
   Muss ein Gebäude exakt abgegrenzt werden oder reicht seine ungefähre Position?

4. **Welche Daten liegen tatsächlich vor?**  
   Messstationen liefern zunächst Punktdaten, auch wenn Temperatur als Phänomen kontinuierlich ist.

5. **Welche Verarbeitung ist geplant?**  
   Die spätere Analyse kann bestimmte Geometrien, Zellgrößen oder Datenformate erfordern.

## Kurze Übung

### 1. Datenmodelle zuordnen

Schlagen Sie für jede Fragestellung ein geeignetes Datenmodell und gegebenenfalls einen Geometrietyp vor:

1. Wo wurden Feuersalamander beobachtet?
2. Wie verlaufen die Radwege in Marburg?
3. Welche Flächen gehören zu einem Naturschutzgebiet?
4. Wie hoch liegt jeder Ort in Hessen?
5. Welche Landbedeckung besitzt jeder Ausschnitt eines Satellitenbildes?

Begründen Sie Ihre Entscheidung jeweils in einem Satz.

### 2. Anders modellieren

Wählen Sie eines der folgenden Beispiele und beschreiben Sie zwei unterschiedliche Möglichkeiten der räumlichen Modellierung:

* Stadt,
* Wald,
* Fluss,
* Niederschlag oder
* Straße.

Erklären Sie, für welche Fragestellung die jeweilige Darstellung geeignet wäre.

<!-- Lösungshinweise für Lehrende:
Übung 1, mögliche Lösungen:
1. Punktvektor für einzelne Beobachtungen.
2. Linienvektor für den Verlauf der Radwege.
3. Polygonvektor für die räumliche Ausdehnung der Schutzgebiete.
4. kontinuierliches Raster mit Höhenwert je Zelle.
5. kategoriales Raster mit Landbedeckungsklasse je Zelle.

Übung 2:
- Es sind verschiedene fachlich begründete Antworten möglich.
- Entscheidend ist, dass Datenmodell, Maßstab und Fragestellung zusammenpassen.
-->

## Zusammenfassung

* Geodatenmodelle übersetzen ausgewählte Aspekte der räumlichen Wirklichkeit in digitale Daten.
* Das Vektormodell beschreibt Features durch Punkte, Linien oder Polygone und verknüpft ihre Geometrien mit Attributen.
* Das Rastermodell teilt den Raum in regelmäßige Zellen, die jeweils einen Wert enthalten.
* Diskrete Objekte werden häufig als Vektoren und kontinuierliche Phänomene häufig als Raster dargestellt.
* Diese Zuordnung ist keine feste Regel: Dasselbe Phänomen kann abhängig von Datenquelle, Maßstab und Fragestellung unterschiedlich modelliert werden.
* Ein geeignetes Datenmodell wird anhand der Forschungsfrage und der benötigten räumlichen Information ausgewählt.

<!-- Notizen: Ab hier folgen Vermerke, welche als Gedankenstütze oder Erinnerung dienen, aber noch nicht in der vorhandenen Form veröffentlicht werden sollen. -->

<!--
Möglicher Einstieg im Seminar:
- Foto oder Luftbild eines Landschaftsausschnitts zeigen.
- Studierende markieren lassen, was sie als Punkt, Linie, Polygon oder Raster darstellen würden.
- Anschließend unterschiedliche Lösungen anhand verschiedener Fragestellungen vergleichen.

Didaktisch wichtig:
- Punktdaten von Beginn an als Teil des Vektormodells benennen.
- Nicht den Eindruck vermitteln, dass jedes Phänomen genau ein „richtiges“ Datenmodell besitzt.
- Raster hier nur konzeptionell einführen; Auflösung, Zellwerte und NoData folgen ausführlich in Unit 13.

Anschluss an unit10-02_qgis.html:
- Wie organisiert und zeigt eine GIS-Software Vektor- und Rasterdaten als Layer?
-->
