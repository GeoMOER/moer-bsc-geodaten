---
title: Was sind Geodaten?
published: true
toc: true
header:
  image: /assets/images/spotlight01/jekyll_github_pages.png
  image_description: "Cutout from Measured carbon dioxide concentrations in Vancouver"
  caption: "Bild: [jekyll](https://jekyllrb.com/)"
---

<!-- Introtext: Verbindung zu den zuvor behandelten Tabellen und Dateien herstellen. -->

## Daten mit Raumbezug

In den bisherigen Lerneinheiten haben wir Daten vor allem als Einträge in Tabellen kennengelernt. Eine Tabelle kann beispielsweise den Namen einer Messstation, das Datum einer Messung und die gemessene Temperatur enthalten. Für viele geographische Fragestellungen benötigen wir jedoch noch eine weitere Information: **Wo wurde die Temperatur gemessen?**

Enthalten Daten einen Bezug zu einem Ort oder einem räumlichen Objekt, sprechen wir von **Geodaten**. Dieser Raumbezug ermöglicht es uns, die Daten auf einer Karte darzustellen und räumliche Fragen zu beantworten.

> **Merksatz:** Geodaten sind Daten, die Informationen über die Lage, Form oder räumliche Ausdehnung von Objekten und Phänomenen enthalten.

<!-- Optional: Abbildung mit Beispielen für Tabelle ohne und mit Raumbezug ergänzen. -->

## Wodurch erhalten Daten einen Raumbezug?

Der Raumbezug kann auf unterschiedliche Weise beschrieben werden. Häufig geschieht dies durch:

* **Koordinaten**, zum Beispiel Längen- und Breitengrad einer Wetterstation,
* **Adressen**, zum Beispiel die Anschrift eines Gebäudes,
* **Gebietsnamen oder Kennziffern**, zum Beispiel der Name oder Gemeindeschlüssel eines Landkreises,
* **Geometrien**, welche die Lage und Form eines Objektes als Punkt, Linie oder Fläche beschreiben,
* **Rasterzellen**, die jeweils einen bestimmten Ausschnitt der Erdoberfläche repräsentieren.

Nicht jede Ortsangabe ist gleich genau. Die Angabe „Deutschland“ beschreibt zwar einen Raumbezug, aber keine genaue Position innerhalb Deutschlands. Eine Koordinate kann dagegen einen sehr konkreten Ort angeben. Welche räumliche Genauigkeit benötigt wird, hängt immer von der jeweiligen Fragestellung ab.

| Information | möglicher Raumbezug | mögliche Frage |
|---|---|---|
| Temperaturmessung | Koordinaten einer Wetterstation | Wo wurde die Temperatur gemessen? |
| Einwohnerzahl | Gemeinde | In welchen Gemeinden leben besonders viele Menschen? |
| Artenbeobachtung | Fundort als Koordinate | Wo wurde die Art beobachtet? |
| Straßenname | Verlauf als Linie | Wo verläuft die Straße? |
| Höhenwert | Zelle eines Höhenrasters | Wie hoch liegt dieser Ort? |

## Lage und Eigenschaften

Geodaten verbinden in der Regel zwei Arten von Informationen:

1. **räumliche Informationen** beschreiben, wo sich etwas befindet oder welche Form es besitzt,
2. **Sachdaten** beschreiben die Eigenschaften dieses Ortes oder Objektes.

Betrachten wir eine Wetterstation als Beispiel. Ihre Koordinaten beschreiben die Lage. Der Name der Station, die Höhe über dem Meeresspiegel und die gemessene Temperatur sind Sachdaten. In einem Geoinformationssystem können beide Informationsarten miteinander verknüpft werden.

| station_id | name | temperatur | breite | länge |
|---|---|---:|---:|---:|
| 001 | Marburg-Cappel | 18,4 | 50,78 | 8,77 |
| 002 | Marburg-Marbach | 17,9 | 50,82 | 8,73 |

In dieser vereinfachten Tabelle enthalten die Spalten `breite` und `länge` den Raumbezug. Die übrigen Spalten beschreiben Eigenschaften der Messstationen und ihrer Messungen. Aus den Koordinaten können die Tabellenzeilen als Punkte auf einer Karte dargestellt werden.

> **Wichtig:** Eine Karte zeigt nicht nur, **was** gemessen oder beobachtet wurde, sondern auch, **wo** dies geschehen ist.

<!-- Die Beispielwerte sind didaktische Beispieldaten und sollten vor Veröffentlichung bei Bedarf durch reale Daten ersetzt werden. -->

## Geodaten beschreiben nicht die Realität selbst

Geodaten sind vereinfachte **Modelle der Wirklichkeit**. Welche Informationen aufgenommen und wie räumliche Objekte dargestellt werden, hängt von der Fragestellung und vom Maßstab ab.

Eine Stadt kann beispielsweise:

* auf einer Deutschlandkarte als **Punkt**,
* auf einer detaillierten Karte als **Fläche** oder
* in einem Satellitenbild durch viele **Rasterzellen**

dargestellt werden. Keine dieser Darstellungen ist grundsätzlich richtig oder falsch. Sie eignen sich lediglich für unterschiedliche Zwecke.

Auch die Grenze eines Waldes oder eines Stadtgebietes ist nicht immer so eindeutig, wie eine scharfe Linie auf einer Karte vermuten lässt. Geodaten enthalten daher immer Entscheidungen, Vereinfachungen und Unsicherheiten.

<!-- Optional: Abbildung „Marburg als Punkt, Polygon und Rasterausschnitt“ ergänzen. -->

## Absolute und relative Lage

Die Lage eines Ortes kann auf zwei grundlegend verschiedene Arten beschrieben werden:

* Die **absolute Lage** wird durch ein festgelegtes räumliches Bezugssystem angegeben, zum Beispiel durch geographische Koordinaten.
* Die **relative Lage** beschreibt einen Ort im Verhältnis zu anderen Orten, zum Beispiel „nördlich des Hauptbahnhofs“ oder „fünf Kilometer von Marburg entfernt“.

Für die digitale Verarbeitung von Geodaten benötigen wir meist eine eindeutig definierte absolute Lage. Relative Lagebeziehungen bleiben dennoch wichtig, denn viele geographische Fragen betreffen Entfernungen, Nachbarschaften oder räumliche Überschneidungen.

## Räumliche Ausdehnung und Maßstab

Geodaten beziehen sich immer auf einen bestimmten räumlichen Ausschnitt. Dieser kann sehr klein oder sehr groß sein:

* ein einzelnes Gebäude,
* das Stadtgebiet von Marburg,
* das Bundesland Hessen,
* ganz Deutschland oder
* die gesamte Erde.

Die **räumliche Ausdehnung** beschreibt den Bereich, den ein Datensatz abdeckt. Der **Maßstab** beziehungsweise der betrachtete Detailgrad beeinflusst, welche Objekte sinnvoll dargestellt werden können. Auf einer Weltkarte erscheint Marburg höchstens als Punkt. Auf einem Stadtplan können dagegen einzelne Straßen und Gebäude sichtbar sein.

Bei der Auswahl von Geodaten sollten wir deshalb immer prüfen:

* Decken die Daten mein Untersuchungsgebiet ab?
* Sind sie für meine Fragestellung räumlich detailliert genug?
* Passen Lagegenauigkeit und Maßstab zu den übrigen Daten?

## Warum sind Geodaten besonders?

Mit gewöhnlichen Tabellen können wir Werte sortieren, filtern und vergleichen. Durch den Raumbezug kommen zusätzliche Fragen hinzu:

* Wo befinden sich Beobachtungen oder Objekte?
* Wie weit sind zwei Orte voneinander entfernt?
* Welche Objekte grenzen aneinander?
* Welche Punkte liegen innerhalb eines Gebietes?
* Wie verändert sich eine Eigenschaft im Raum?

Damit solche Fragen zuverlässig beantwortet werden können, müssen Lageinformationen eindeutig beschrieben sein. In den nächsten Unterseiten beschäftigen wir uns deshalb mit **Koordinaten**, **Koordinatenreferenzsystemen** und **Kartenprojektionen**.

## Kurze Übung

Entscheiden Sie für jedes Beispiel, ob ein Raumbezug vorhanden ist und wie genau dieser beschrieben wird:

1. Eine Tabelle enthält den Namen und die Einwohnerzahl aller hessischen Gemeinden.
2. Eine Temperaturmessung enthält einen Messwert und ein Datum, aber keinen Messort.
3. Ein Foto wurde mit einem Smartphone aufgenommen und enthält GPS-Koordinaten.
4. Ein Bericht nennt als Fundort einer Pflanze lediglich „in der Nähe von Marburg“.

Überlegen Sie anschließend:

* Welche Beispiele sind Geodaten?
* Welche Angaben wären nötig, um die Daten auf einer Karte darzustellen?
* Für welche Fragestellungen wäre der jeweilige Raumbezug zu ungenau?

<!-- Lösungshinweise für Lehrende:
1. Raumbezug über Gemeindenamen vorhanden, aber für eine Kartendarstellung ist eine Verknüpfung mit Gemeindegeometrien nötig.
2. Kein nutzbarer Raumbezug.
3. Direkter Raumbezug über Koordinaten.
4. Raumbezug vorhanden, aber räumlich ungenau und nicht eindeutig abgegrenzt.
-->

## Zusammenfassung

* Geodaten verbinden Sachdaten mit einem räumlichen Bezug.
* Der Raumbezug kann unter anderem durch Koordinaten, Adressen, Gebiete, Geometrien oder Rasterzellen beschrieben werden.
* Geodaten sind vereinfachte Modelle der Realität und werden passend zu einer Fragestellung erstellt.
* Räumliche Ausdehnung, Maßstab und Lagegenauigkeit bestimmen, wofür ein Datensatz geeignet ist.
* Für die gemeinsame Verarbeitung verschiedener Geodaten muss ihre räumliche Referenz eindeutig bekannt sein.

<!-- Notizen: Ab hier folgen Vermerke, welche als Gedankenstütze oder Erinnerung dienen, aber noch nicht in der vorhandenen Form veröffentlicht werden sollen. -->

<!--
Möglicher Einstieg im Seminar:
- Zwei Tabellen zeigen: eine Temperaturmessung ohne Messort und dieselbe Messung mit Koordinaten.
- Frage an die Gruppe: Welche zusätzliche Information macht aus den Tabellendaten Geodaten?

Mögliche Abbildungen:
- Tabelle und zugehörige Punktkarte
- Marburg als Punkt, Polygon und Rasterausschnitt
- Beispiele verschiedener räumlicher Ausdehnungen

Anschluss an unit09-02_koordinaten.html:
- Wie können wir einen Ort so durch Zahlen beschreiben, dass Computer ihn eindeutig auf einer Karte positionieren können?
-->