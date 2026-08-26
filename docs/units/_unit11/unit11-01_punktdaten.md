---
title: Punktdaten
published: true
toc: true
header:
  image: /assets/images/spotlight01/jekyll_github_pages.png
  image_description: "Cutout from Measured carbon dioxide concentrations in Vancouver"
  caption: "Bild: [jekyll](https://jekyllrb.com/)"
---

<!-- Introtext: Punktdaten als ersten konkreten Geometrietyp des Vektormodells einführen. -->

## Ein Ort als Punkt

Ein **Punkt** ist die einfachste Geometrie des Vektormodells. Er beschreibt eine einzelne Position durch Koordinaten. In einer Karte kann ein Punkt beispielsweise eine Messstation, einen Fundort oder eine Haltestelle repräsentieren.

Ein Punkt besitzt in seinem Datenmodell keine dargestellte Länge oder Fläche. Das Kartensymbol, mit dem er sichtbar gemacht wird, besitzt zwar eine Größe, diese Symbolgröße ist aber nicht automatisch die tatsächliche Größe des dargestellten Objektes.

> **Merksatz:** Ein Punkt zeigt, **wo** sich etwas befindet. Was der Punkt bedeutet, steht in seinen Attributen und Metadaten.

## Wann ist das Punktmodell geeignet?

Das Punktmodell ist besonders geeignet, wenn:

* die Position wichtiger ist als Form und Ausdehnung,
* das dargestellte Objekt im gewählten Maßstab sehr klein ist,
* eine Messung oder Beobachtung an einem bestimmten Ort dokumentiert wird oder
* einzelne Ereignisse räumlich verglichen werden sollen.

Typische Punktdaten sind:

| Punkt repräsentiert | mögliche Attribute |
|---|---|
| Wetterstation | Stationsname, Höhe, Betreiber |
| Temperaturmessung | Zeitpunkt, Messwert, Einheit |
| Artenbeobachtung | Art, Datum, Beobachtungsmethode |
| Bodenprobe | Probennummer, Tiefe, Laborwerte |
| GPS-Position | Zeitstempel, Geschwindigkeit, Genauigkeit |
| Bushaltestelle | Name, Linien, Barrierefreiheit |

Das Punktmodell ist weniger geeignet, wenn die tatsächliche Form oder Fläche eines Objektes für die Fragestellung wichtig ist. Ein See kann auf einer Übersichtskarte als Punkt erscheinen, für die Berechnung seiner Fläche wird jedoch eine Polygongeometrie benötigt.

## Punktfeature, Objekt und Beobachtung

Bei Punktdaten müssen mehrere Ebenen unterschieden werden:

* Das **reale Objekt oder Ereignis** befindet sich in der Wirklichkeit.
* Der **Datensatz** enthält ausgewählte Informationen darüber.
* Das **Punktfeature** ist die räumliche Repräsentation im GIS.
* Das **Kartensymbol** macht das Feature sichtbar.

Diese Ebenen sind nicht identisch. Ein Beobachtungspunkt für einen Feuersalamander bedeutet beispielsweise nicht, dass genau ein Tier dauerhaft an dieser punktgenauen Position lebt. Er dokumentiert zunächst einen gemeldeten Nachweis mit einer bestimmten räumlichen und zeitlichen Genauigkeit.

> **Wichtig:** Eine Beobachtung, ein Individuum und ein Punktfeature können zusammenhängen, sind aber nicht automatisch dasselbe.

## Geometrie und Attribute

Ein Punktfeature verbindet eine Geometrie mit Sachdaten:

* Die **Geometrie** enthält die räumliche Position.
* Die **Attribute** beschreiben das Feature oder die zugrunde liegende Beobachtung.

Eine vereinfachte Tabelle mit Artenbeobachtungen könnte so aussehen:

| observation_id | species | event_date | longitude | latitude | observer |
|---|---|---|---:|---:|---|
| obs_001 | Salamandra salamandra | 2026-04-18 | 8.77 | 50.81 | Person A |
| obs_002 | Salamandra salamandra | 2026-05-02 | 9.49 | 51.31 | Person B |

Aus `longitude` und `latitude` kann eine GIS-Software die Punktgeometrie erzeugen. Die übrigen Spalten werden als Attribute übernommen.

<!-- Beispieldaten sind didaktisch und vor Veröffentlichung gegebenenfalls durch reale, lizenzkonforme Daten ersetzen. -->

## Eine Zeile – ein Feature

In einer üblichen Attributtabelle entspricht jede Zeile einem Feature. Das bedeutet jedoch nicht zwangsläufig, dass jede Zeile einen einzigartigen realen Ort oder ein einzigartiges Individuum beschreibt.

Mehrere Zeilen können:

* dieselben Koordinaten besitzen,
* verschiedene Beobachtungen am selben Ort dokumentieren,
* dasselbe Individuum zu verschiedenen Zeitpunkten betreffen oder
* durch mehrfache Übermittlung desselben Nachweises als Dubletten entstanden sein.

Deshalb benötigt jeder Datensatz möglichst eine **stabile eindeutige ID**. Eine ID hilft, Datensätze zu unterscheiden und Verarbeitungsschritte nachvollziehbar zu dokumentieren. Sie beweist allein jedoch noch nicht, dass zwei sehr ähnliche Zeilen unterschiedliche Beobachtungen darstellen.

## Aus einer Tabelle wird ein Punktlayer

Eine Text- oder Tabellenstruktur mit Koordinatenspalten ist zunächst noch keine dauerhaft gespeicherte Geodatendatei. Damit eine GIS-Software daraus Punkte erzeugen kann, müssen mindestens bekannt sein:

* die Spalte mit der x-Koordinate,
* die Spalte mit der y-Koordinate,
* das verwendete Koordinatenreferenzsystem,
* das Dezimaltrennzeichen und
* die Kennzeichnung fehlender Werte.

Für geographische Koordinaten gilt in QGIS üblicherweise:

* **x = Longitude = Längengrad**
* **y = Latitude = Breitengrad**

Sind die Werte in WGS 84 als Dezimalgrad gespeichert, wird beim Import `EPSG:4326` angegeben.

> **Achtung:** Das CRS beim Import beschreibt die vorhandenen Koordinaten. Es darf nicht danach ausgewählt werden, welches CRS später für die Analyse gewünscht ist.

## Räumliche Genauigkeit und Präzision

Viele Koordinaten sehen genauer aus, als sie tatsächlich sind. Die Anzahl der Dezimalstellen beschreibt nur die **numerische Präzision**. Sie sagt nicht automatisch, wie genau der Ort erfasst wurde.

Ein GPS-Gerät kann mehrere Dezimalstellen ausgeben, obwohl die reale Positionsunsicherheit einige Meter beträgt. Historische Fundangaben wurden vielleicht nur einer Gemeinde zugeordnet und später durch deren Mittelpunkt repräsentiert. Beide Datensätze können ähnlich aussehende Koordinaten besitzen, aber eine sehr unterschiedliche räumliche Qualität.

Wichtige Fragen sind daher:

* Wie wurde die Position bestimmt?
* Welche räumliche Unsicherheit wird angegeben?
* Wurden Koordinaten gerundet oder nachträglich ergänzt?
* Bezeichnet der Punkt den genauen Fundort oder nur ein größeres Gebiet?
* Passt die Genauigkeit zur geplanten Analyse?

## Zeit gehört zur Beobachtung

Beobachtungsdaten besitzen häufig nicht nur einen Raum-, sondern auch einen **Zeitbezug**. Ein Punkt kann ohne Datum leicht falsch interpretiert werden.

Beispiele:

* Eine Art wurde an einem Ort vor 80 Jahren beobachtet.
* Eine Messstation hat ihren Standort gewechselt.
* Ein Unfallpunkt gehört zu einem bestimmten Jahr.
* Eine GPS-Position ist Teil einer zeitlich geordneten Bewegung.

Für viele Fragestellungen müssen deshalb Datum, Jahr, Uhrzeit oder Erhebungszeitraum gemeinsam mit der Position gefiltert und dokumentiert werden.

## Punktdaten auf Plausibilität prüfen

Vor der Kartierung sollten mindestens folgende Prüfungen erfolgen:

### Koordinaten

* Sind Längen- und Breitengrad vorhanden?
* Liegen die Werte im möglichen Bereich?
* Sind x und y möglicherweise vertauscht?
* Passen die Positionen zum erwarteten Untersuchungsgebiet?
* Wurde `(0, 0)` möglicherweise als Platzhalter verwendet?

### Attribute

* Gibt es eine eindeutige ID?
* Sind Artname, Messgröße oder Ereignistyp verständlich?
* Sind Einheiten und Datentypen dokumentiert?
* Fehlen wichtige Datumsangaben?
* Werden fehlende Werte einheitlich gekennzeichnet?

### Dubletten

* Gibt es identische IDs?
* Wiederholen sich Kombinationen aus Ort, Zeit und Objekt?
* Handelt es sich um echte Wiederholungsbeobachtungen oder Mehrfachmeldungen?

### Herkunft

* Wer hat die Daten erhoben oder veröffentlicht?
* Welche Methode wurde verwendet?
* Welche Lizenz gilt?
* Welche Bearbeitungsschritte wurden bereits durchgeführt?

Auffällige Datensätze sollten nicht stillschweigend gelöscht werden. Dokumentieren Sie Prüfregel, Entscheidung und Anzahl betroffener Datensätze.

## Beobachtung ist nicht gleich Verbreitung

Eine Karte mit Beobachtungspunkten zeigt zunächst, **wo Nachweise dokumentiert wurden**. Sie zeigt nicht automatisch:

* alle Orte, an denen die Art vorkommt,
* alle Orte, an denen gezielt gesucht wurde,
* Orte mit bestätigter Abwesenheit oder
* die Wahrscheinlichkeit eines Vorkommens zwischen den Punkten.

Viele Beobachtungsdaten sind räumlich ungleich verteilt. In gut erreichbaren, dicht besiedelten oder besonders intensiv untersuchten Gebieten werden häufig mehr Beobachtungen gemeldet. Eine hohe Punktdichte kann deshalb sowohl ein biologisches Muster als auch hohe Beobachtungsaktivität widerspiegeln.

> **Interpretationsregel:** „Keine Beobachtung“ bedeutet ohne dokumentierte Suche nicht automatisch „kein Vorkommen“.

## Punkte und Maßstab

Ob ein Objekt sinnvoll als Punkt dargestellt wird, hängt vom Maßstab ab. Eine Stadt kann auf einer Deutschlandkarte als Punkt ausreichen, während auf einem Stadtplan ihre Verwaltungsgrenze als Polygon benötigt wird.

Auch die Symbolgröße verändert sich beim Zoomen nicht zwingend wie ein reales Objekt. Ein großes Punktsymbol dient häufig nur der Lesbarkeit. Es darf nicht als räumliche Ausdehnung der Beobachtung interpretiert werden.

## Kurze Übung

### 1. Ist ein Punkt geeignet?

Entscheiden Sie für jede Fragestellung, ob ein Punktmodell geeignet ist:

1. Wo befinden sich Wetterstationen in Hessen?
2. Wie groß sind die hessischen Naturschutzgebiete?
3. Wo wurden Feuersalamander beobachtet?
4. Wie verläuft die Lahn?
5. Wo wurden Bodenproben entnommen?

Begründen Sie Ihre Entscheidung und nennen Sie bei ungeeigneten Beispielen einen besseren Geometrietyp.

### 2. Beobachtungen beurteilen

Zwei Datensätze besitzen dieselben Koordinaten und denselben Artnamen, aber unterschiedliche Beobachtungsdaten. Handelt es sich sicher um Dubletten? Welche zusätzlichen Attribute würden Sie prüfen?

### 3. Aussage einer Punktkarte

Formulieren Sie eine fachlich vorsichtige Bildunterschrift für eine Karte mit GBIF-Nachweisen des Feuersalamanders. Vermeiden Sie die unbelegte Aussage, die Karte zeige die vollständige Verbreitung der Art.

<!-- Lösungshinweise für Lehrende:
Übung 1:
1. Punkt geeignet.
2. Polygon erforderlich, wenn Flächen berechnet werden sollen.
3. Punkt geeignet für einzelne Nachweise.
4. Linie geeignet; bei detaillierter Betrachtung kann auch ein Polygon sinnvoll sein.
5. Punkt geeignet.

Übung 2:
- Unterschiedliche Daten können echte Wiederholungsbeobachtungen sein.
- Zu prüfen sind unter anderem occurrenceID/gbifID, Uhrzeit, Beobachter, Datensatz, Grundlage des Nachweises und Erfassungsmethode.

Übung 3, Beispiel:
- „In GBIF dokumentierte Nachweise von Salamandra salamandra im ausgewählten Zeitraum; Punktdichte beschreibt sowohl Vorkommen als auch Erfassungs- und Meldeaktivität.“
-->

## Zusammenfassung

* Punkte sind Vektorgeometrien für einzelne Positionen ohne dargestellte Länge oder Fläche.
* Ein Punktfeature verbindet eine Koordinate mit Attributen.
* Objekt, Beobachtung, Datensatz, Feature und Kartensymbol müssen unterschieden werden.
* Aus Tabellen werden nur dann korrekt positionierte Punktlayer, wenn Koordinatenspalten, Reihenfolge und CRS bekannt sind.
* Viele Dezimalstellen bedeuten nicht automatisch eine hohe räumliche Genauigkeit.
* Zeit, Erhebungsmethode, Datenquelle und eindeutige IDs sind für die Interpretation von Beobachtungspunkten wichtig.
* Punktkarten mit Nachweisen zeigen nicht automatisch die vollständige Verbreitung oder Abwesenheit einer Art.

<!-- Notizen: Ab hier folgen Vermerke, welche als Gedankenstütze oder Erinnerung dienen, aber noch nicht in der vorhandenen Form veröffentlicht werden sollen. -->

<!--
Mögliche Abbildungen:
- reales Objekt → Datensatz → Punktfeature → Kartensymbol
- Tabelle mit Koordinaten → Punktlayer
- große und kleine Symbolgröße bei identischer Punktgeometrie
- Beobachtungsdichte entlang von Städten und Wegen als Beispiel für Erfassungsbias

Didaktisch wichtig:
- numerische Präzision und tatsächliche Positionsgenauigkeit unterscheiden
- wiederholte Beobachtung und Dublette nicht gleichsetzen
- Punktdichte nicht vorschnell biologisch interpretieren

Anschluss an unit11-02_gbif.md:
- Wie sehen reale Biodiversitätsbeobachtungen aus, welche Felder stellt GBIF bereit und welche Qualitätsinformationen müssen berücksichtigt werden?
-->
