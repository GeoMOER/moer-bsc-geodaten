---
title: Pivot
published: true
toc: true
header:
  image: /assets/images/unit04/streuobst.jpg
  image_description: "Streuobstwiese"
  caption: "Image: ulrichstill [CC BY-SA 2.0 DE] via [wikimedia.org](https://commons.wikimedia.org/wiki/File:Tuebingen_Streuobstwiese.jpg)"
---
Eine einfache Pivot-Tabelle erstellen

Eine Pivot-Tabelle fasst große Datenmengen per Drag-and-Drop zusammen, ganz ohne eigene Formel – ideal, um schnell zu sehen, wie viele Messungen pro Station vorliegen oder wie hoch die durchschnittliche Temperatur je Station ist.

**Pivot-Tabelle erstellen:**
1. Klicken Sie in Ihre zusammengeführte Datentabelle
2. Menüband: **Einfügen → PivotTable**
3. Bestätigen Sie den vorgeschlagenen Datenbereich und wählen Sie „Neues Arbeitsblatt"
4. Im Bereich „PivotTable-Felder" rechts: Ziehen Sie `Standort` in den Bereich **„Zeilen"**
5. Ziehen Sie `Temperatur` in den Bereich **„Werte"** – Excel summiert standardmäßig; klicken Sie auf das Werte-Feld → „Wertfeldeinstellungen" → **„Mittelwert"** wählen

<!-- Screenshot: Excel mit geöffnetem Bereich "PivotTable-Felder" rechts, "Standort" im Feld "Zeilen", "Temperatur" im Feld "Werte" mit der Aggregation "Mittelwert", links die daraus resultierende Pivot-Tabelle mit einer Zeile pro Station und der jeweiligen Durchschnittstemperatur. -->

**Zweites Wertefeld ergänzen:** Ziehen Sie zusätzlich `Temperatur` ein zweites Mal in den Bereich „Werte" und stellen Sie dort auf **„Anzahl"** – so sehen Sie in einer Tabelle sowohl die Durchschnittstemperatur als auch die Anzahl der Messungen je Station.

**Warum das für die Fehlwert-Kontrolle nützlich ist:** Eine Pivot-Tabelle mit „Anzahl" pro Station zeigt Ihnen sofort, ob eine Station auffällig wenige Messwerte hat (Hinweis auf viele Fehlwerte) – deutlich schneller, als die `ZÄHLENWENN`-Formeln aus dem Fehlwerte-Kapitel manuell für jede Station einzeln zu bauen.

**Pivot-Tabelle aktualisieren:** Ändern sich die Ausgangsdaten nachträglich, übernimmt die Pivot-Tabelle das **nicht automatisch** – Rechtsklick in die Pivot-Tabelle → **„Aktualisieren"**.