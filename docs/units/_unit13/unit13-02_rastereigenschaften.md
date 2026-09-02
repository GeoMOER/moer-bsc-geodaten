---
title: Eigenschaften von Rasterdaten
published: true
toc: true
header:
  image: /assets/images/unit13/hero-unit13.jpg
  image_description: "Ein Rasterwert wird als neues Attribut an einen Beobachtungspunkt übertragen"
  caption: "Eigene Darstellung"
---

<!-- Introtext: Eigenschaften erklären, die vor Anzeige, Kombination und Interpretation eines Rasters geprüft werden müssen. -->

## Raster sind mehr als Zellwerte

Damit Rasterwerte räumlich richtig zugeordnet und fachlich sinnvoll interpretiert werden können, benötigen wir weitere Informationen. Besonders wichtig sind:

* Zellgröße und räumliche Auflösung,
* Anzahl der Zeilen und Spalten,
* räumliche Ausdehnung,
* Rasterursprung und Ausrichtung,
* Koordinatenreferenzsystem,
* Anzahl und Bedeutung der Bänder,
* Datentyp und Einheit,
* NoData-Wert sowie
* Entstehung, Aktualität und Genauigkeit.

Diese Eigenschaften sollten vor jeder Analyse kontrolliert werden.

## Zellgröße

Die **Zellgröße** beschreibt, welche Breite und Höhe eine Rasterzelle im Koordinatensystem besitzt. In einem projizierten CRS kann eine Zelle beispielsweise `10 m × 10 m` groß sein.

Eine solche Zelle repräsentiert dann eine Fläche von:

$$
10\,\text{m} \times 10\,\text{m} = 100\,\text{m}^2
$$

Bei geographischen Koordinaten kann die Zellgröße dagegen in Grad angegeben sein. Ein Grad besitzt jedoch nicht überall auf der Erde dieselbe Länge. Die Einheit des CRS muss deshalb immer mitgelesen werden.

## Räumliche Auflösung

Die Zellgröße wird häufig als **räumliche Auflösung** bezeichnet. Ein Raster mit `10 m` großen Zellen kann feinere räumliche Unterschiede abbilden als ein Raster mit `1 km` großen Zellen.

| Zellgröße | Zellen pro Quadratkilometer | mögliche Detailstufe |
|---|---:|---|
| 1.000 m × 1.000 m | 1 | sehr grob |
| 100 m × 100 m | 100 | grob |
| 10 m × 10 m | 10.000 | fein |
| 1 m × 1 m | 1.000.000 | sehr fein |

Eine kleinere Zellgröße führt bei gleicher Ausdehnung zu mehr Zellen und meist zu größeren Dateien und längeren Berechnungszeiten.

## Auflösung ist nicht Genauigkeit

Ein Raster mit kleinen Zellen ist nicht automatisch genau.

Ein Datensatz kann beispielsweise auf ungenauen Eingangsmessungen beruhen und trotzdem in Zellen von einem Meter Größe gespeichert werden. Die feine Zellgröße beschreibt dann nur das Rastergitter, nicht die tatsächliche Mess- oder Modellgenauigkeit.

Unterscheiden Sie deshalb:

* **räumliche Auflösung:** Größe beziehungsweise Abstand der Rasterzellen,
* **Lagegenauigkeit:** Wie genau liegt eine Zelle an der vorgesehenen Position?
* **Wertgenauigkeit:** Wie genau entspricht der gespeicherte Wert dem untersuchten Phänomen?

> Viele kleine Zellen können eine sehr detaillierte Darstellung erzeugen, aber keine fehlende Genauigkeit ersetzen.

## Ausdehnung

Die **räumliche Ausdehnung** – häufig als *extent* bezeichnet – beschreibt das vom Raster abgedeckte Rechteck. Sie wird durch minimale und maximale Koordinaten begrenzt:

* kleinster x-Wert,
* größter x-Wert,
* kleinster y-Wert,
* größter y-Wert.

Zwei Raster können dasselbe CRS und dieselbe Zellgröße besitzen, aber unterschiedliche Gebiete abdecken. Vor einer gemeinsamen Analyse muss deshalb geprüft werden, ob sich ihre Ausdehnungen überschneiden.

## Zeilen und Spalten

Die Anzahl der Zeilen und Spalten ergibt zusammen die Zahl der Rasterzellen:

$$
N_{Zellen} = N_{Zeilen} \times N_{Spalten}
$$

Ein Raster mit 10.000 Zeilen und 10.000 Spalten enthält bereits 100 Millionen Zellen – bei nur einem Band. Das erklärt, weshalb Rasterdateien schnell groß werden können.

## Rasterursprung und Ausrichtung

Zwei Raster können dieselbe Zellgröße besitzen und trotzdem gegeneinander verschoben sein. Ihre Zellgrenzen beginnen dann an unterschiedlichen Koordinaten. Diese Eigenschaft wird als **Rasterausrichtung** oder *grid alignment* bezeichnet.

Für eine zellenweise Berechnung sollten Raster normalerweise übereinstimmen in:

* CRS,
* Zellgröße,
* Rasterausrichtung und
* relevantem räumlichen Ausschnitt.

QGIS kann Raster neu projizieren und neu abtasten. Dabei werden jedoch neue Zellwerte berechnet. Solche Verarbeitungsschritte müssen deshalb bewusst gewählt und dokumentiert werden.

## Koordinatenreferenzsystem

Auch Rasterdaten benötigen ein CRS. Es legt fest, wie die Rasterausdehnung und Zellpositionen auf der Erde verortet werden.

Wenn ein Raster an einer unerwarteten Stelle erscheint oder nicht mit Vektorlayern übereinstimmt, prüfen Sie zuerst:

1. Ist ein CRS angegeben?
2. Ist dieses CRS tatsächlich das CRS der Daten?
3. Liegt das Projekt in einem geeigneten CRS?
4. Wurde ein CRS nur zugewiesen oder wurden die Daten wirklich reprojiziert?

Das bloße Zuweisen eines anderen CRS verändert die Zellwerte und Koordinaten nicht. Eine echte Reprojektion erzeugt dagegen ein neues Rastergitter.

## Datentyp

Der **Datentyp** bestimmt, welche Werte in einem Raster gespeichert werden können.

| Datentyp | mögliche Werte | Beispiel |
|---|---|---|
| Ganzzahl | ganze Zahlen | Klassen einer Landbedeckung |
| Fließkommazahl | Zahlen mit Nachkommastellen | modellierte Temperatur |

Zusätzlich begrenzt der verwendete Speicherbereich den möglichen Werteumfang. Ein geeigneter Datentyp spart Speicherplatz; ein ungeeigneter Datentyp kann Werte runden oder nicht vollständig abbilden.

Für die Interpretation benötigen wir außerdem die **Einheit**. Der Wert `250` könnte beispielsweise 250 Meter Höhe, 250 Millimeter Niederschlag oder lediglich den Code einer Kategorie bedeuten.

## Bänder

Ein Raster kann mehrere Bänder besitzen. Prüfen Sie deshalb:

* Wie viele Bänder sind vorhanden?
* Was beschreibt jedes Band?
* Welche Einheit und welcher Datentyp gelten?
* Beziehen sich alle Bänder auf denselben Zeitpunkt?

Bei einem digitalen Geländemodell erwarten wir gewöhnlich ein Band mit Höhenwerten. Bei Satellitendaten können dagegen viele spektrale Bänder enthalten sein.

## NoData ist nicht null

Ein **NoData-Wert** kennzeichnet Zellen, für die kein gültiger fachlicher Wert vorliegt.

Mögliche Gründe sind:

* außerhalb des Untersuchungsgebiets,
* fehlende Messung,
* Wolken oder Sensorausfall,
* bei der Verarbeitung maskierter Bereich oder
* nicht sinnvoll berechenbarer Wert.

Der Zahlenwert `0` kann dagegen ein gültiger Wert sein:

* 0 Meter Geländehöhe,
* 0 Millimeter Niederschlag,
* 0 Grad Celsius oder
* eine gültige Kategorie mit dem Code 0.

> **NoData bedeutet „kein gültiger Wert“. Null bedeutet „der gültige Wert ist 0“.**

Manche Dateiformate speichern für NoData einen besonderen Zahlenwert wie `-9999`. QGIS muss wissen, dass dieser Wert nicht in Berechnungen oder Farbskalen einbezogen werden soll.

## Minimum, Maximum und Verteilung

Für kontinuierliche Raster sind Minimum und Maximum hilfreich, aber allein nicht ausreichend. Ein einzelner extremer Wert kann eine Farbskala stark beeinflussen.

Ein Histogramm zeigt, wie häufig Wertebereiche im Raster vorkommen. Damit lässt sich besser beurteilen:

* ob die Werte plausibel verteilt sind,
* ob extreme Werte vorkommen,
* welche Farbskala geeignet ist und
* ob ein möglicher NoData-Code fälschlich als Messwert behandelt wird.

Statistiken können sich auf das gesamte Raster oder nur auf einen aktuellen Ausschnitt beziehungsweise eine Stichprobe beziehen. Prüfen Sie daher, wie sie berechnet wurden.

## Farbe ist nicht der Zellwert

QGIS ordnet Zahlenwerten Farben zu. Ändern wir die Farbskala, verändern wir nicht die gespeicherten Höhenwerte – nur ihre Darstellung.

Für kontinuierliche Werte eignen sich häufig **sequentielle Farbverläufe**, die von hell nach dunkel oder von niedrigen zu hohen Farbwerten verlaufen. Eine kategoriale Landbedeckung benötigt dagegen einzelne, klar unterscheidbare Farben.

Die Symbolisierung kann räumliche Muster sichtbar machen, sie kann aber auch Unterschiede verstärken oder verschleiern. Die Gestaltung wird deshalb in Unit 14 noch einmal systematisch behandelt.

## Raster neu abtasten

Wenn sich Zellgröße, Ausrichtung oder CRS ändern, muss QGIS Werte für ein neues Rastergitter bestimmen. Dieser Vorgang heißt **Resampling** oder Neuabtastung.

Vereinfachte Grundregel:

| Rastertyp | häufig geeignetes Verfahren | Begründung |
|---|---|---|
| kategorial | nächster Nachbar | erhält vorhandene Klassenwerte |
| kontinuierlich | bilinear oder kubisch | bildet glattere Übergänge aus benachbarten Werten |

Beim nächsten Nachbarn wird ein vorhandener Zellwert übernommen. Bilineare oder kubische Verfahren berechnen neue Zwischenwerte. Für Klassen wären solche Zwischenwerte meist sinnlos: Aus den Klassen `Wald = 1` und `Grünland = 2` darf nicht die neue Klasse `1,5` entstehen.

> Resampling kann die technische Rasterstruktur verändern, erzeugt aber keine neue gemessene Information.

## Dateiformate

Ein häufig verwendetes Rasterformat ist **GeoTIFF** mit der Endung `.tif`. Es kann Zellwerte und Informationen zur Georeferenzierung in einer Datei speichern.

Weitere Rasterdaten können beispielsweise als Cloud Optimized GeoTIFF, ASCII Grid, NetCDF oder in einem GeoPackage vorliegen. Für den Einstieg genügt zunächst:

* Dateiformat erkennen,
* CRS und Rastereigenschaften kontrollieren,
* Originaldatei unverändert aufbewahren und
* Ergebnisse mit eindeutigen Namen speichern.

Eine `.tif`-Datei kann sowohl ein georeferenziertes Werte-Raster als auch ein gewöhnliches Bild ohne vollständigen Raumbezug sein. Die Dateiendung allein genügt deshalb nicht zur Beurteilung.

## Metadaten prüfen

Dokumentieren Sie für einen Rasterdatensatz mindestens:

| Merkmal | Frage |
|---|---|
| Titel | Wie heißt der Datensatz? |
| Herausgeber | Wer stellt ihn bereit? |
| Inhalt | Was bedeutet der Zellwert? |
| Einheit | In welcher Einheit wird der Wert angegeben? |
| Zellgröße | Welche räumliche Auflösung besitzt das Raster? |
| CRS | Wie ist das Raster räumlich referenziert? |
| Ausdehnung | Welches Gebiet wird abgedeckt? |
| Bänder | Wie viele Bänder gibt es und was bedeuten sie? |
| NoData | Wie werden fehlende Werte gekennzeichnet? |
| Entstehung | Wurde gemessen, modelliert, interpoliert oder klassifiziert? |
| Aktualität | Auf welchen Stand beziehen sich die Daten? |
| Genauigkeit | Welche Unsicherheiten werden angegeben? |
| Lizenz | Wie dürfen die Daten verwendet werden? |

## Übung: Zwei Raster vergleichen

Vergleichen Sie zwei gedachte Höhenraster desselben Gebietes:

| Eigenschaft | Raster A | Raster B |
|---|---:|---:|
| Zellgröße | 10 m | 100 m |
| Zeilen | 5.000 | 500 |
| Spalten | 5.000 | 500 |
| Datentyp | Ganzzahl | Fließkommazahl |
| NoData | -9999 | nicht dokumentiert |

Beantworten Sie:

1. Welches Raster besitzt das feinere Gitter?
2. Wie viele Zellen besitzt jedes Raster?
3. Welches Raster ist vermutlich größer? Welche weitere Information wäre für eine genaue Aussage nötig?
4. Können wir allein aus der Zellgröße schließen, welches Raster genauere Höhenwerte besitzt?
5. Welches Problem entsteht bei Raster B durch die fehlende NoData-Dokumentation?

<!-- Lösungshinweise für Lehrende:
1. Raster A.
2. A: 25.000.000; B: 250.000 Zellen.
3. Vermutlich A; zusätzlich sind unter anderem Datentyp, Kompression und Zahl der Bänder nötig.
4. Nein, Wert- und Lagegenauigkeit sowie Entstehungsmethode fehlen.
5. Fehlende Werte könnten als gültige Höhen interpretiert werden; Statistiken und Darstellung können dadurch falsch sein.
-->

## Zusammenfassung

* Zellgröße und räumliche Auflösung beschreiben das Rastergitter, nicht automatisch die Genauigkeit.
* Ausdehnung, CRS, Zellgröße und Rasterausrichtung bestimmen die räumliche Lage der Zellen.
* Datentyp, Bandbedeutung und Einheit sind für die Interpretation der Zellwerte notwendig.
* NoData kennzeichnet einen fehlenden oder ungültigen Wert und ist nicht mit null gleichzusetzen.
* Statistik und Histogramm helfen, Wertverteilung und mögliche Fehler zu erkennen.
* Die Farbe ist eine Darstellung der Werte und nicht der Wert selbst.
* Bei einer Neuabtastung muss das Verfahren zum Rastertyp passen.
* Rastermetadaten sind notwendig, um Eignung, Herkunft und Unsicherheit zu beurteilen.

## Weiterführende Informationen

* [QGIS-Dokumentation: Rastereigenschaften](https://docs.qgis.org/latest/en/docs/user_manual/working_with_raster/raster_properties.html)
* [QGIS-Dokumentation: Rasterdaten](https://docs.qgis.org/latest/en/docs/gentle_gis_introduction/raster_data.html)
* [Hessen Geodatenmanagement: Open Data](https://hvbg.hessen.de/geoinformation/open-data)

<!-- Notizen: Ab hier folgen Vermerke, welche als Gedankenstütze oder Erinnerung dienen, aber noch nicht in der vorhandenen Form veröffentlicht werden sollen. -->

<!--
Mögliche Abbildungen:
- dasselbe Gebiet mit grobem und feinem Rastergitter
- zwei gleich große, aber gegeneinander verschobene Rastergitter
- gültiger Wert 0 neben NoData-Zellen
- kategoriales Resampling mit falschem Zwischenwert
- unveränderte Zellwerte mit zwei verschiedenen Farbskalen

Didaktisch wichtig:
- „hohe Auflösung“ ist mehrdeutig; besser konkrete Zellgröße nennen.
- Auflösung, Genauigkeit und Präzision nicht vermischen.
- Resampling nur konzeptionell behandeln; in der Praxisübung ist keine eigenständige Reprojektion erforderlich.
- Speicherbedarf nicht allein aus Zellzahl ableiten; Datentyp, Bänder und Kompression erwähnen.
-->
