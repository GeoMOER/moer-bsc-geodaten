---
title: Verteilungen
published: true
toc: true
header:
  image: /assets/images/unit04/streuobst.jpg
  image_description: "Streuobstwiese"
  caption: "Image: ulrichstill [CC BY-SA 2.0 DE] via [wikimedia.org](https://commons.wikimedia.org/wiki/File:Tuebingen_Streuobstwiese.jpg)"
---

Zahlen allein zeigen nicht, *wie* die Werte verteilt sind – ob sie sich um einen Wert konzentrieren, gleichmäßig gestreut sind, oder sogar zwei getrennte Häufungspunkte haben. Dafür eignet sich das **Histogramm**: die grundlegendste und intuitivste Möglichkeit, eine einzelne Variable zu visualisieren.

## Was zeigt ein Histogramm?

Ein Histogramm teilt den Wertebereich einer Variable in gleich breite Intervalle („Klassen" oder „Bins") ein und zeigt als Balkenhöhe, wie viele Beobachtungen in jedes Intervall fallen. Anders als bei einem gewöhnlichen Balkendiagramm gibt es zwischen den Balken **keine Lücken** – das macht deutlich, dass es sich um eine fortlaufende, keine kategoriale Skala handelt.

<!-- **Screenshot 29:** Histogramm der Temperaturwerte mit x-Achse „Temperatur (°C)" in Intervallen von 2 °C (z. B. 4–6, 6–8, 8–10, …) und y-Achse „Anzahl Messungen", Balken lückenlos aneinandergereiht, eine leichte Rechtsschiefe der Verteilung erkennbar. -->

## Histogramm in Excel erstellen

1. Markieren Sie die Datenspalte (z. B. `Temperatur`)
2. Menüband: **Einfügen → Diagramme → Statistikdiagramm → Histogramm**
3. Excel wählt automatisch eine Klassenbreite („Bin-Breite") – diese lässt sich über Rechtsklick auf die x-Achse → „Achse formatieren" manuell anpassen

<!-- **Screenshot 30:** Rechte Seitenleiste „Achse formatieren" mit Eingabefeldern „Bin-Breite" und „Anzahl der Bins", sichtbar mit Beispielwert `2` bei der Bin-Breite. -->

**Warum die Klassenbreite wichtig ist:** Zu breite Klassen verschleiern Muster in den Daten (alles landet in 2–3 Balken), zu schmale Klassen erzeugen ein „zerklüftetes" Bild mit vielen einzelnen, kaum interpretierbaren Balken. Probieren Sie bei eigenen Daten ruhig 2–3 verschiedene Bin-Breiten aus, bevor Sie sich für eine Darstellung entscheiden.

## Was ein Histogramm zeigt, das ein einzelner Kennwert verbirgt

Zwei Datensätze können denselben Mittelwert und dieselbe Standardabweichung haben und trotzdem völlig unterschiedlich aussehen – etwa wenn ein Datensatz gleichmäßig um einen Wert streut, während ein anderer zwei deutlich getrennte Häufungspunkte hat (z. B. Messungen zu zwei sehr unterschiedlichen Tageszeiten, morgens kühl, mittags warm). Ein Histogramm macht diesen Unterschied sofort sichtbar – eine Tabelle mit Kennzahlen würde ihn komplett verstecken.

**Kurzcheck:** Erstellen Sie ein Histogramm Ihrer Temperaturwerte. Wirkt die Verteilung eher gleichmäßig um einen zentralen Wert, oder erkennen Sie mehrere Häufungspunkte bzw. eine deutliche Schiefe zu einer Seite?

# Boxplot

Der Boxplot fasst dieselbe Information wie ein Histogramm – Lage, Streuung, Ausreißer – kompakter zusammen und eignet sich dadurch besonders gut, um **mehrere Gruppen nebeneinander zu vergleichen** (z. B. Ihre Sensordaten je Standort), was mit mehreren Histogrammen nebeneinander schnell unübersichtlich würde.

## Aufbau eines Boxplots

- Die **Box** reicht vom 1. Quartil (Q1) bis zum 3. Quartil (Q3) – sie enthält also die mittleren 50 % der Daten
- Die Linie **innerhalb der Box** markiert den Median
- Die „**Whisker**" (Antennen) reichen bis zum kleinsten bzw. größten Wert **innerhalb** des 1,5-fachen Interquartilsabstands
- Einzelne Punkte **außerhalb** der Whisker gelten als statistische **Ausreißer**

<!-- **Screenshot 31:** Schematischer Boxplot mit beschrifteten Elementen: unterer Whisker, Q1 (untere Boxkante), Medianlinie in der Box, Q3 (obere Boxkante), oberer Whisker, sowie ein einzelner Punkt oberhalb des oberen Whiskers, beschriftet als „Ausreißer". -->

## Boxplot in Excel erstellen

1. Markieren Sie die Datenspalte (z. B. `Temperatur`), ggf. gruppiert nach einer zweiten Spalte (z. B. `Standort`), wenn Sie mehrere Boxplots nebeneinander vergleichen möchten
2. Menüband: **Einfügen → Diagramme → Statistikdiagramm → Kastengrafik (Box-Whisker)**
3. Excel berechnet Quartile und Ausreißer automatisch und stellt sie grafisch dar

<!-- **Screenshot 32:** Excel mit markiertem Datenbereich (zwei Spalten: „Standort" und „Temperatur"), Menüband-Reiter „Einfügen" mit hervorgehobener Schaltfläche „Statistikdiagramm" und Untermenü, in dem „Kastengrafik" sichtbar ist. -->

**Praxisnutzen für Ihren Datensatz:** Stellen Sie die Temperaturwerte mehrerer Standorte als Boxplots nebeneinander dar, erkennen Sie auf einen Blick, welcher Standort stärker schwankende Werte hat (breitere Box) oder einzelne untypische Ausreißer-Messungen enthält – deutlich schneller als beim Vergleich einzelner Mittelwerte in einer Tabelle.

## Hinweis: Ausreißer nicht vorschnell löschen

Ein im Boxplot sichtbarer Ausreißer ist zunächst nur eine **statistische Auffälligkeit** – kein Beweis für einen Messfehler. Bevor Sie einen solchen Wert aus Ihrer Auswertung entfernen, prüfen Sie, ob es dafür eine inhaltliche Erklärung gibt (z. B. ein tatsächlicher Kälteeinbruch an einem bestimmten Tag) oder ob es sich um einen Erfassungsfehler handelt (z. B. Zahlendreher bei der Eingabe).

> **Wichtig – Protokollierung:** Wenn Sie sich entscheiden, einen Ausreißer aus Ihrer Auswertung auszuschließen, dokumentieren Sie **welchen Wert**, **warum** und **wo** Sie diese Entscheidung getroffen haben. Wie eine solche Dokumentation sauber und nachvollziehbar aufgebaut wird, behandeln wir ausführlich in einem eigenen späteren Kapitel zur Protokollierung – halten Sie sich diese Angaben aber schon jetzt in einer Notiz oder Kommentarspalte fest, statt Ausreißer stillschweigend zu löschen.