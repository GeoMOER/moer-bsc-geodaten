---
title: Koordinaten
published: true
toc: true
header:
  image: /assets/images/unit09/hero-unit09.jpg
  image_description: "Breiter Blick auf Europa auf einer gekrümmten Erde mit feinem Koordinatengitter und markiertem Ort"
  caption: "KI-generierte Illustration, bearbeitet für diesen Kurs"
---

<!-- Introtext: An die vorherige Unterseite zum Raumbezug anknüpfen. -->

## Orte durch Zahlen beschreiben

Auf der vorherigen Seite haben wir gesehen, dass Daten durch einen Bezug zu einem Ort oder einem räumlichen Objekt zu **Geodaten** werden. Eine besonders wichtige Möglichkeit, einen Ort eindeutig anzugeben, sind **Koordinaten**.

Koordinaten bestehen aus Zahlen, welche die Position eines Punktes innerhalb eines festgelegten räumlichen Bezugssystems beschreiben. Ähnlich wie Zeile und Spalte in einer Tabelle werden mindestens zwei Angaben benötigt, um eine Position auf einer Fläche zu bestimmen.

> **Merksatz:** Ein einzelner Koordinatenwert beschreibt noch keinen Ort. Erst ein vollständiges Koordinatenpaar und das zugehörige Bezugssystem ergeben gemeinsam eine räumliche Position.

![Breitenkreise, Meridiane und die ungefähre Position Marburgs im Gradnetz.]({{ '/assets/images/unit09/gradnetz.svg' | relative_url }})

## Koordinaten in einem ebenen Gitter

Das Grundprinzip lässt sich zunächst an einem einfachen Koordinatensystem zeigen. Eine Position wird durch ihren Abstand entlang zweier Achsen beschrieben:

* Die **x-Koordinate** beschreibt die Position in horizontaler Richtung.
* Die **y-Koordinate** beschreibt die Position in vertikaler Richtung.

Ein Punkt mit den Koordinaten `(3, 5)` liegt also bei `x = 3` und `y = 5`. Üblicherweise wird zuerst die x- und anschließend die y-Koordinate angegeben:

> **(x, y)**

Dieses Prinzip begegnet uns später bei projizierten Koordinatensystemen wieder. Dort können x- und y-Werte beispielsweise Entfernungen in Metern angeben.

<!-- Optional: Punkt (3, 5) in einem kartesischen Koordinatensystem darstellen. -->

## Geographische Koordinaten

Für Positionen auf der Erde werden häufig **geographische Koordinaten** verwendet. Sie geben eine Lage anhand von **Breitengrad** und **Längengrad** an.

### Breitengrad

Der **Breitengrad** beschreibt, wie weit ein Ort nördlich oder südlich des Äquators liegt.

* Der Äquator besitzt den Breitengrad `0°`.
* Der Nordpol liegt bei `90° N`.
* Der Südpol liegt bei `90° S`.

Breitengrade werden auch als **Latitude** bezeichnet. In Datentabellen finden sich dafür häufig Spaltennamen wie `latitude`, `lat` oder `breite`.

### Längengrad

Der **Längengrad** beschreibt, wie weit ein Ort östlich oder westlich des Nullmeridians liegt. Der international verwendete Nullmeridian verläuft durch Greenwich bei London.

* Der Nullmeridian besitzt den Längengrad `0°`.
* Nach Osten und Westen reichen die Werte jeweils bis `180°`.

Längengrade werden auch als **Longitude** bezeichnet. Typische Spaltennamen sind `longitude`, `lon`, `long` oder `länge`.

| Begriff | englischer Begriff | Abkürzung | möglicher Wertebereich |
|---|---|---|---:|
| Breitengrad | Latitude | lat | −90° bis +90° |
| Längengrad | Longitude | lon | −180° bis +180° |

## Das Gradnetz der Erde

Breiten- und Längengrade bilden gemeinsam ein gedachtes **Gradnetz** um die Erde:

* **Breitenkreise** verlaufen parallel zum Äquator.
* **Meridiane** verlaufen vom Nordpol zum Südpol.

An jedem Ort kreuzen sich ein Breitenkreis und ein Meridian. Dadurch lässt sich seine Position durch ein Koordinatenpaar beschreiben.

Marburg liegt ungefähr bei:

> **50,81° nördlicher Breite und 8,77° östlicher Länge**

In einer Datentabelle könnte dieselbe Position so gespeichert werden:

| ort | latitude | longitude |
|---|---:|---:|
| Marburg | 50.81 | 8.77 |

<!-- Optional: Weltkarte mit Äquator, Nullmeridian und der Position Marburgs ergänzen. -->

## Dezimalgrad und Grad-Minuten-Sekunden

Geographische Koordinaten können unterschiedlich notiert werden. Zwei häufige Schreibweisen sind:

1. **Grad, Minuten und Sekunden**, zum Beispiel `50° 48′ 36″ N`
2. **Dezimalgrad**, zum Beispiel `50.8100°`

Dabei gilt:

* `1 Grad = 60 Minuten`
* `1 Minute = 60 Sekunden`

Digitale Geodatensätze verwenden meist **Dezimalgrad**, weil sich diese Schreibweise einfacher in Tabellen speichern und mit Software verarbeiten lässt.

Für die Umrechnung gilt:

> Dezimalgrad = Grad + Minuten / 60 + Sekunden / 3600

Beispiel:

> `50° 48′ 36″ = 50 + 48/60 + 36/3600 = 50,81°`

Vor der Verarbeitung sollte geprüft werden, in welcher Schreibweise die Koordinaten vorliegen. Die Zeichen `°`, `′`, `″`, `N`, `S`, `E` und `W` in einer Tabellenspalte können dazu führen, dass ein Programm die Einträge als Text statt als Zahlen interpretiert.

## Himmelsrichtungen und Vorzeichen

In Dezimalgrad werden die Himmelsrichtungen meist durch positive und negative Vorzeichen ausgedrückt:

| Himmelsrichtung | Vorzeichen | Beispiel |
|---|---:|---:|
| nördlich des Äquators | positiv | `50.81` |
| südlich des Äquators | negativ | `−23.55` |
| östlich des Nullmeridians | positiv | `8.77` |
| westlich des Nullmeridians | negativ | `−74.01` |

Die Angabe `−23.55° S` wäre daher doppeldeutig beziehungsweise unnötig doppelt gekennzeichnet, weil sowohl das Minuszeichen als auch das `S` bereits die südliche Richtung ausdrücken. Für tabellarische Daten sollte eine einheitliche Schreibweise verwendet werden.

## Welche Koordinate steht zuerst?

Bei geographischen Koordinaten begegnen uns zwei verbreitete Reihenfolgen:

* in Texten häufig **Breitengrad, Längengrad** beziehungsweise `(lat, lon)`,
* in vielen GIS-Anwendungen **x, y** beziehungsweise `(Längengrad, Breitengrad)`.

Für Marburg wären dies:

| Schreibweise | Koordinatenpaar |
|---|---|
| `(lat, lon)` | `(50.81, 8.77)` |
| `(x, y)` beziehungsweise `(lon, lat)` | `(8.77, 50.81)` |

Vertauschte Koordinaten sind eine häufige Fehlerquelle. Ein Datensatz mit Marburger Punktdaten kann dadurch an einer vollkommen anderen Stelle erscheinen.

> **Kurskonvention:** In Datentabellen und beim späteren GIS-Import schreiben wir geographische Koordinaten als `(longitude, latitude)`, entsprechend `(x, y)`. Diese Reihenfolge ist nicht in allen Standards, Diensten und Programmdialogen identisch. Prüfen Sie daher immer Spaltennamen, Metadaten und die erwartete Achsenreihenfolge der jeweiligen Schnittstelle. Verlassen Sie sich nicht allein auf die Position der Werte.

> **Prüffrage:** Stehen die Werte für Deutschland ungefähr bei einem Breitengrad zwischen 47 und 55 sowie einem Längengrad zwischen 5 und 16?

Diese grobe Plausibilitätsprüfung ersetzt keine genaue Kontrolle, hilft aber dabei, vertauschte oder fehlerhafte Werte schnell zu erkennen.

[![Im selben WGS-84-Gradgitter liegt A bei Länge 8,77 und Breite 50,81 Grad nahe Marburg; das vertauschte Paar B liegt bei Länge 50,81 und Breite 8,77 Grad weit entfernt.]({{ '/assets/images/unit09/achsenreihenfolge.svg' | relative_url }})]({{ '/assets/images/unit09/achsenreihenfolge.svg' | relative_url }})

*Beide Paare liegen in den erlaubten Wertebereichen. Erst die Zuordnung zu den Achsen und die erwartete Lage zeigen den Fehler. Die Abbildung verwendet die Kursreihenfolge Länge, Breite; die Abstände im Gradgitter sind keine Entfernungen in Metern.*

## Koordinaten benötigen ein Bezugssystem

Das Zahlenpaar `(8.77, 50.81)` reicht allein noch nicht vollständig aus. Wir müssen zusätzlich wissen:

* welche Achse durch welchen Wert beschrieben wird,
* welche Einheit verwendet wird und
* auf welches **Koordinatenreferenzsystem** sich die Werte beziehen.

Zahlenwerte um `8` und `50` könnten geographische Koordinaten in Grad sein. Werte wie `483000` und `5629000` können dagegen Koordinaten eines projizierten Systems in Metern darstellen. Ohne diese Information kann eine GIS-Software die Daten nicht zuverlässig an der richtigen Stelle positionieren.

Mit Koordinatenreferenzsystemen und Kartenprojektionen beschäftigen wir uns auf der nächsten Unterseite ausführlicher.

## Typische Fehler in Koordinatendaten

Bei der Arbeit mit Koordinaten sollten insbesondere folgende Fehler geprüft werden:

* Breiten- und Längengrad wurden vertauscht.
* Dezimaltrennzeichen werden uneinheitlich verwendet.
* Zahlen wurden als Text gespeichert.
* Vorzeichen für südliche oder westliche Koordinaten fehlen.
* Grad-Minuten-Sekunden und Dezimalgrad wurden verwechselt.
* Werte liegen außerhalb der möglichen Bereiche.
* Einzelne Koordinaten fehlen oder wurden mit `0` ersetzt.
* Das Koordinatenreferenzsystem ist unbekannt oder falsch angegeben.

Gerade der Punkt `(0, 0)` sollte kritisch betrachtet werden: Er liegt tatsächlich im Golf von Guinea und ist nicht automatisch ein gültiger Platzhalter für fehlende Daten.

## Kurze Übung

### 1. Koordinaten lesen

Ordnen Sie den Angaben jeweils Breiten- und Längengrad zu:

1. `50.81, 8.77`
2. `8.77, 50.81`
3. `latitude = 50.81, longitude = 8.77`
4. `x = 8.77, y = 50.81`

Welche zusätzlichen Angaben benötigen Sie bei den ersten beiden Beispielen, um die Reihenfolge eindeutig zu bestimmen?

### 2. Daten prüfen

Welche der folgenden Koordinatenpaare sind für einen Ort in Deutschland plausibel?

1. `(8.77, 50.81)`
2. `(50.81, 8.77)`
3. `(188.40, 50.81)`
4. `(8.77, −50.81)`
5. `(0, 0)`

Beachten Sie dabei die angegebene Reihenfolge `(Längengrad, Breitengrad)`.

### 3. Schreibweisen umrechnen – freiwillige Vertiefung

Rechnen Sie `8° 46′ 12″ E` in Dezimalgrad um. Prüfen Sie anschließend, ob das Ergebnis ungefähr zum Längengrad von Marburg passt.

<!-- Lösungshinweise für Lehrende:
Übung 1:
- Ohne Beschriftung oder Konvention ist die Reihenfolge der ersten beiden Paare nicht eindeutig.
- Bei latitude/longitude ist 50.81 die Breite und 8.77 die Länge.
- Bei x/y ist 8.77 die x-Koordinate beziehungsweise Länge und 50.81 die y-Koordinate beziehungsweise Breite.

Übung 2:
- Unter der Konvention (lon, lat) ist nur (8.77, 50.81) für Deutschland plausibel.
- (50.81, 8.77) liegt nach dieser Konvention nicht in Deutschland und deutet auf vertauschte Werte hin.
- 188.40 ist kein gültiger Längengrad.
- −50.81 liegt auf der Südhalbkugel.
- (0, 0) ist formal gültig, liegt aber nicht in Deutschland.

Übung 3:
- 8 + 46/60 + 12/3600 = 8.77° E.
-->

## Zusammenfassung

* Koordinaten beschreiben die Position eines Ortes innerhalb eines festgelegten Bezugssystems.
* Geographische Koordinaten bestehen aus Breiten- und Längengrad.
* Breitenwerte reichen von −90° bis +90°, Längenwerte von −180° bis +180°.
* Dezimalgrad ist für digitale Datensätze meist geeigneter als Grad-Minuten-Sekunden.
* Reihenfolge, Einheit, Vorzeichen und Koordinatenreferenzsystem müssen bekannt sein.
* Plausibilitätsprüfungen helfen, vertauschte oder fehlerhafte Koordinaten zu erkennen.

<!-- Notizen: Ab hier folgen Vermerke, welche als Gedankenstütze oder Erinnerung dienen, aber noch nicht in der vorhandenen Form veröffentlicht werden sollen. -->

<!--
Möglicher Einstieg im Seminar:
- Die Zahlen 50.81 und 8.77 ohne weitere Angaben zeigen.
- Studierende vermuten lassen, was sie bedeuten und welche Information noch fehlt.
- Anschließend die Position zunächst korrekt und danach mit vertauschten Achsen auf einer Karte zeigen.

Mögliche Demonstrationen:
- Koordinaten eines bekannten Ortes in einem Kartendienst ablesen
- eine kleine Tabelle mit latitude/longitude prüfen
- denselben Ort in Dezimalgrad und Grad-Minuten-Sekunden vergleichen
- den Punkt (0, 0) auf einer Weltkarte anzeigen

Anschluss an unit09-03_projektionen.html:
- Warum können Koordinaten desselben Ortes in einem anderen Bezugssystem völlig andere Zahlenwerte besitzen?
-->
