---
title: Das Rastermodell
published: true
toc: true
header:
  image: /assets/images/unit13/hero-unit13.jpg
  image_description: "Ein Rasterwert wird als neues Attribut an einen Beobachtungspunkt übertragen"
  caption: "Eigene Darstellung"
---

<!-- Introtext: Das bisher behandelte Vektormodell um das Rastermodell ergänzen. -->

## Vom Objekt zum Wertefeld

Im Vektormodell wird jedes räumliche Objekt durch eine eigene Geometrie beschrieben. Ein Baum kann ein Punkt, ein Fluss eine Linie und ein Schutzgebiet ein Polygon sein.

Bei der Geländehöhe gibt es dagegen nicht nur einzelne, klar voneinander getrennte Höhenobjekte. Grundsätzlich besitzt jeder Ort eine Höhe. Um ein solches räumlich veränderliches Phänomen zu speichern, können wir ein regelmäßiges Gitter über das Untersuchungsgebiet legen.

Dieses Gitter bildet das **Rastermodell**.

> **Merksatz:** Ein Raster teilt den Raum in regelmäßig angeordnete Zellen. Jede Zelle speichert einen Wert.

## Aufbau eines Rasters

Ein Raster besteht aus:

* **Zeilen**,
* **Spalten**,
* **Rasterzellen** und
* einem Wert pro Zelle und Band.

Eine kleine Rastermatrix könnte beispielsweise so aussehen:

|  | Spalte 1 | Spalte 2 | Spalte 3 | Spalte 4 |
|---|---:|---:|---:|---:|
| Zeile 1 | 241 | 245 | 250 | 254 |
| Zeile 2 | 238 | 243 | 248 | 252 |
| Zeile 3 | 235 | 239 | 244 | 249 |

In einem digitalen Geländemodell könnten diese Zahlen Höhen in Metern darstellen. Die Position einer Zelle ergibt sich aus der Position des gesamten Rasters sowie ihrer Zeile und Spalte.

## Rasterzelle und Pixel

Die Begriffe **Rasterzelle** und **Pixel** werden häufig ähnlich verwendet. Eine hilfreiche Unterscheidung ist:

* Die **Rasterzelle** ist die räumliche Einheit des Datensatzes.
* Das **Pixel** ist das dargestellte Bildelement auf einem Bildschirm oder in einer Bilddatei.

Beim starken Hineinzoomen wird eine Rasterzelle in QGIS als großes Quadrat sichtbar. Auf dem Bildschirm besteht dieses Quadrat dann aus vielen Bildschirmpixeln. Für die fachliche Beschreibung der Daten verwenden wir deshalb bevorzugt den Begriff Rasterzelle.

## Wo liegt eine Rasterzelle?

Ein Raster besitzt einen räumlichen Bezug. Dazu gehören:

* ein Koordinatenreferenzsystem,
* die Koordinaten seiner äußeren Begrenzung,
* die Zellgröße,
* die Anzahl der Zeilen und Spalten und
* ein festgelegter Startpunkt beziehungsweise Rasterursprung.

Damit kann QGIS jede Zelle an der richtigen Position anzeigen und mit Vektordaten überlagern.

Ein Zellwert beschreibt jedoch nicht einen mathematisch unendlich kleinen Punkt. Er steht für die betreffende Zelle beziehungsweise für eine aus Messung oder Modellierung abgeleitete Repräsentation dieses räumlichen Bereichs.

## Kontinuierliche Rasterdaten

Ein **kontinuierliches Raster** beschreibt eine Größe, die sich im Raum grundsätzlich stufenlos verändern kann.

Beispiele:

* Geländehöhe,
* Temperatur,
* Niederschlag,
* Bodenfeuchte,
* Entfernung zu einer Straße oder
* Vegetationsindizes aus Satellitendaten.

Benachbarte Zellen können sehr ähnliche, aber unterschiedliche Werte besitzen. Zur Darstellung verwenden wir häufig einen kontinuierlichen Farbverlauf.

> Die sichtbaren Farbstufen entstehen durch die Darstellung. Im Raster können weiterhin einzelne Zahlenwerte gespeichert sein.

## Kategoriale Rasterdaten

Ein **kategoriales Raster** ordnet jede Zelle einer Klasse zu.

Beispiele:

* Landbedeckung,
* Bodentyp,
* geologische Einheit,
* Waldtyp oder
* Ergebnis einer Klassifikation von Satellitendaten.

Die Zellwerte dienen hier häufig als Codes:

| Zellwert | Bedeutung |
|---:|---|
| 1 | Wald |
| 2 | Grünland |
| 3 | Ackerfläche |
| 4 | Siedlungsfläche |
| 5 | Wasser |

Die Zahlen `1` bis `5` beschreiben keine Rangfolge und keine messbare Entfernung zwischen den Kategorien. Sie sind Bezeichner für verschiedene Klassen. Deshalb werden kategoriale Raster mit unterscheidbaren Einzelfarben und nicht mit einem kontinuierlichen Farbverlauf dargestellt.

## Rasterbilder mit mehreren Kanälen

Ein Raster kann aus einem oder mehreren **Bändern** bestehen. Jedes Band besitzt für jede Zelle einen eigenen Wert.

Beispiele:

* Ein digitales Geländemodell besitzt meist ein Band mit Höhenwerten.
* Ein RGB-Luftbild besitzt Bänder für Rot, Grün und Blau.
* Satellitendaten können zusätzlich Bänder für nahes Infrarot oder andere Wellenlängen enthalten.

Mehrere Bänder beschreiben also unterschiedliche Messgrößen oder Spektralbereiche für dasselbe Rastergitter.

## Digitales Geländemodell und digitales Oberflächenmodell

Ein **digitales Geländemodell (DGM)** beschreibt die Höhe der Geländeoberfläche. Gebäude und Vegetation sollen darin möglichst nicht als Oberflächenhöhe enthalten sein.

Ein **digitales Oberflächenmodell (DOM)** beschreibt dagegen die sichtbare beziehungsweise erfasste Oberfläche einschließlich beständiger Objekte wie Gebäuden und Vegetation.

| Modell | dargestellte Oberfläche | mögliche Fragestellung |
|---|---|---|
| DGM | Gelände ohne Gebäude und Vegetationsoberflächen | Auf welcher Geländehöhe liegt eine Beobachtung? |
| DOM | Gelände einschließlich Gebäude- und Vegetationsoberflächen | Wie hoch liegt die erfasste Oberfläche an diesem Ort? |

Die beiden Datensätze können am selben Ort unterschiedliche Höhenwerte besitzen. Welcher Wert fachlich sinnvoll ist, hängt von der Fragestellung ab.

## Satelliten- und Luftbilder sind ebenfalls Raster

Ein digitales Foto oder Satellitenbild ist regelmäßig in Bildpunkte gegliedert. Ein georeferenziertes Luft- oder Satellitenbild besitzt zusätzlich einen räumlichen Bezug und kann deshalb als Rasterlayer in einem GIS verwendet werden.

Seine Zellwerte können beispielsweise gemessene oder verarbeitete Strahlungsinformationen repräsentieren. Die sichtbare Farbe ist dann das Ergebnis der Kombination und Darstellung verschiedener Bänder.

Ein Raster ist deshalb nicht automatisch:

* ein Foto,
* eine Hintergrundkarte oder
* ein Höhenmodell.

Das Rastermodell beschreibt zunächst nur die regelmäßige räumliche Anordnung von Zellwerten. Die fachliche Bedeutung ergibt sich aus Daten, Bändern und Metadaten.

## Raster und Vektor im Vergleich

| Eigenschaft | Vektor | Raster |
|---|---|---|
| grundlegende Einheit | Feature mit Geometrie | Rasterzelle |
| räumliche Struktur | Koordinaten von Punkt, Linie oder Polygon | regelmäßiges Gitter |
| Eigenschaften | Attribute in Tabellenzeile | Zellwerte und gegebenenfalls Rasterattributtabelle |
| typische Stärke | einzelne Objekte und Grenzen | flächendeckende Wertefelder und Bilddaten |
| Detail | abhängig von Geometrie und Maßstab | begrenzt durch Zellgröße und Datengrundlage |
| Beispiel | Schutzgebietspolygon | digitales Geländemodell |

Beide Modelle sind keine Gegensätze, die nicht zusammenarbeiten können. Häufig beantworten wir eine Frage erst durch ihre Kombination:

> **Punktposition einer Beobachtung + Höhenraster = Geländehöhe am Beobachtungsort**

## Dieselbe Realität in verschiedenen Datenmodellen

Auch beim Rastermodell hängt die Darstellung von der Fragestellung ab.

### Stadtgebiet

* als Polygon für eine Verwaltungsgrenze,
* als Raster für die Landbedeckung innerhalb der Stadt,
* als Bildraster für ein Luftbild.

### Wald

* als Polygon für eine abgegrenzte Waldfläche,
* als kategoriales Raster für Landbedeckung,
* als kontinuierliches Raster für Baumhöhe oder Vegetationsdichte.

### Gewässer

* als Linie für den Verlauf eines Flusses,
* als Polygon für seine Wasserfläche,
* als Rasterzellen in einer Landbedeckungsklassifikation.

Es gibt daher auch hier nicht das eine grundsätzlich richtige Datenmodell. Entscheidend sind Fragestellung, Datengrundlage, Maßstab und benötigte Genauigkeit.

## Was bedeutet ein Zellwert?

![Beim Abtasten erhält ein Beobachtungspunkt den Wert der Rasterzelle an seiner Position als neues Attribut.]({{ '/assets/images/unit13/raster-workflow.svg' | relative_url }})

Ein Zellwert kann auf unterschiedliche Weise entstanden sein:

* direkt durch einen Sensor gemessen,
* aus mehreren Messungen zusammengefasst,
* aus benachbarten Beobachtungen interpoliert,
* durch ein Modell geschätzt,
* aus anderen Datensätzen berechnet oder
* als Kategorie zugewiesen.

Der Zellwert ist deshalb nicht automatisch die fehlerfreie Wahrheit für jeden Punkt innerhalb der Zelle. Um ihn richtig zu interpretieren, benötigen wir Metadaten zur Erhebungs- und Berechnungsmethode.

## Kurze Übung

### 1. Datenmodell auswählen

Entscheiden Sie, welches Datenmodell für die jeweilige Fragestellung besonders geeignet ist:

1. Wo befindet sich eine Wetterstation?
2. Wie hoch ist das Gelände an jedem Ort eines Untersuchungsgebiets?
3. Welche Fläche umfasst ein Naturschutzgebiet?
4. Welche Landbedeckungsklasse besitzt jeder Teil eines Bundeslandes?
5. Wie verläuft ein Wanderweg?

### 2. Rastertyp bestimmen

Ordnen Sie zu: kontinuierliches Raster, kategoriales Raster oder mehrbändiges Bildraster.

1. jährlicher Niederschlag in Millimetern,
2. Landbedeckung mit den Klassen Wald, Grünland und Siedlung,
3. RGB-Luftbild,
4. Geländehöhe in Metern,
5. Bodentypen.

### 3. DGM oder DOM?

Welcher Datensatz ist für diese Fragen geeigneter?

1. Auf welcher Geländehöhe wurde eine Pflanzenart beobachtet?
2. Wie hoch ist die erfasste Oberfläche eines Gebäudedachs?
3. Welche Bereiche eines Tals liegen unterhalb von 250 Metern Geländehöhe?

<!-- Lösungshinweise für Lehrende:
Übung 1:
1. Punktvektor.
2. kontinuierliches Raster.
3. Polygonvektor.
4. kategoriales Raster.
5. Linienvektor.

Übung 2:
1. kontinuierlich.
2. kategorial.
3. mehrbändiges Bildraster.
4. kontinuierlich.
5. kategorial.

Übung 3:
1. DGM.
2. DOM.
3. DGM.
-->

## Zusammenfassung

* Ein Raster besteht aus regelmäßig angeordneten Zellen mit räumlich verorteten Werten.
* Zeilen, Spalten, Zellgröße, Ausdehnung und CRS bestimmen die räumliche Anordnung.
* Kontinuierliche Raster beschreiben messbare oder modellierte Größen; kategoriale Raster speichern Klassen.
* Ein Raster kann ein oder mehrere Bänder besitzen.
* Ein DGM beschreibt die Geländeoberfläche, ein DOM zusätzlich die erfassten Objektoberflächen.
* Farbe und Zellwert sind nicht dasselbe: Die Farbe ist eine Form der Darstellung.
* Ein Zellwert muss im Zusammenhang mit seiner Entstehung und den Metadaten interpretiert werden.
* Vektor- und Rasterdaten lassen sich kombinieren, um neue räumliche Fragen zu beantworten.

## Weiterführende Informationen

* [QGIS: Einführung in Rasterdaten](https://docs.qgis.org/latest/en/docs/gentle_gis_introduction/raster_data.html)
* [Hessen Geodatenmanagement: Digitale Geländemodelle](https://hvbg.hessen.de/landesvermessung/geotopographie/3d-daten/digitale-gelaendemodelle)
* [Hessen Geodatenmanagement: Digitale Oberflächenmodelle](https://hvbg.hessen.de/landesvermessung/geotopographie/3d-daten/digitale-oberflaechenmodelle)

<!-- Notizen: Ab hier folgen Vermerke, welche als Gedankenstütze oder Erinnerung dienen, aber noch nicht in der vorhandenen Form veröffentlicht werden sollen. -->

<!--
Mögliche Abbildungen:
- einfaches Rastergitter mit Zeilen, Spalten und Zellwerten
- kontinuierliches und kategoriales Raster nebeneinander
- DGM und DOM als zwei Profile derselben Landschaft
- Punkt-, Linien- und Polygonvektoren über einem Raster
- ein mehrbändiges RGB-Raster

Didaktisch wichtig:
- Zellwert nicht als stets direkt gemessenen Wert darstellen.
- Rasterzelle und Bildschirm-Pixel begrifflich unterscheiden, ohne die Alltagssprache unnötig zu problematisieren.
- DGM/DOM nur auf der für die Aufgabe nötigen Ebene behandeln.
- Räumliche Auflösung und Unsicherheit folgen ausführlich auf der nächsten Seite.
-->
