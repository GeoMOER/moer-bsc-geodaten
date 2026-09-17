--- 
title: ÜA | Übungsaufgabe Abschnitt 05
published: true
toc: true
header:
  image: /assets/images/01-splash.jpg
  image_description: "Dr. John Snow's map"
  caption: "Map: [**Dr. John Snow**](https://en.wikipedia.org/wiki/John_Snow) [Wellcome Library via wikimedia](https://w.wiki/QtV)"
---
Nutzen Sie Ihre bereinigte Arbeitsmappe mit `Datensatz_1` und `Datensatz_2` sowie die neue Datei `Stationsmetadaten.xlsx`.

1. Benennen Sie die Spalten auf `Datensatz_2` so um, dass sie zu `Datensatz_1` passen.
2. Teilen Sie die Spalte `Zeitstempel` auf `Datensatz_2` in `Datum` und `Uhrzeit` auf (siehe Themenüberschrift 01).
3. Bringen Sie die Spalten auf `Datensatz_2` in dieselbe Reihenfolge wie auf `Datensatz_1`.
4. Fügen Sie die Daten von `Datensatz_2` unterhalb von `Datensatz_1` an, sodass eine gemeinsame Tabelle entsteht.
5. Ergänzen Sie eine neue Spalte `Höhe_ueber_NN` und füllen Sie sie mit `SVERWEIS` aus `Stationsmetadaten.xlsx`.
6. Prüfen Sie, ob für alle Zeilen ein Wert gefunden wurde, oder ob irgendwo `#NV` erscheint. Falls ja: Woran liegt das, und wie beheben Sie es?
7. Erstellen Sie eine Pivot-Tabelle mit `Standort` in den Zeilen und `Temperatur` zweimal in den Werten (einmal als Mittelwert, einmal als Anzahl).
8. Identifizieren Sie anhand der Pivot-Tabelle: Welche Station hat die wenigsten gültigen Messwerte?
9. Speichern Sie Ihre zusammengeführte Datei.