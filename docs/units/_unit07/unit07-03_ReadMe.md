---
title: ReadMe Dokumentation
published: true
toc: true
header:
  image: assets/images/unit07/DataSwamp_Stage07.png
  image_description: "Streuobstwiese"
  caption: "Image: ulrichstill [CC BY-SA 2.0 DE] via [wikimedia.org](https://commons.wikimedia.org/wiki/File:Tuebingen_Streuobstwiese.jpg)"
---

## Die README-Datei
 
Eine README ist die erste Datei, die eine fremde Person im Ordner öffnen sollte. Sie erklärt, was der Ordner enthält und wie man ihn nutzt.
 
| Abschnitt | Inhalt |
|---|---|
| 1. Titel und Kurzbeschreibung | Was ist das, wofür wurde es erstellt? |
| 2. Verantwortliche | Name, Kontakt, Datum, Version |
| 3. Inhalt des Ordners | Liste der Dateien und ihr Zweck |
| 4. Herkunft der Daten | Quelle, Zeitraum, Ort, Messmethode, Abrufdatum |
| 5. Datenstruktur | Format, Kodierung, Trennzeichen, Datenwörterbuch |
| 6. Bearbeitung | Schritte in der Reihenfolge, Software, Ort der Rohdaten |
| 7. Qualität und Besonderheiten | Fehlende Werte, Auffälligkeiten |
| 8. Nutzung | Lizenz, Zitierhinweis |
| 9. Verweise | Quellen, verwandte Datensätze |
 
**Hinweise zur Form:**
- Dateiname immer gleich: `README.txt`.
- Format: reine Textdatei in UTF-8, keine Word-Datei. Das ist dasselbe Prinzip wie bei CSV: Ein Format, das jedes Programm liest, bleibt auch in zehn Jahren lesbar.
- Kurz halten und aktuell halten. Eine falsche README ist schlechter als keine.
- Die unveränderten Rohdaten gehören nicht in die README, aber ihr Speicherort.
**Bearbeitungsschritte als Protokoll:** Der Abschnitt 6 hält fest, was Sie in den letzten Kapiteln getan haben. Beispiel:
 
```
1. Rohdateien über "Daten → Aus Text/CSV" importiert (Kodierung, Trennzeichen, Datumsformat geprüft).
2. Spaltennamen und Spaltenreihenfolge der beiden Dateien angeglichen.
3. Doppelte Zeilen entfernt.
4. Schreibweise der Standortnamen vereinheitlicht, überflüssige Leerzeichen entfernt.
5. Platzhalter -999 und Text "NA" durch leere Zellen ersetzt.
6. Beide Tabellen untereinander zu einer Tabelle zusammengeführt.
```
 
<!-- Screenshot [Nr]: Ordnerfenster mit den Ordnern 01_Rohdaten, 02_Bearbeitete_Daten und der Datei README.txt, daneben die geöffnete README.txt im Texteditor mit den ersten Abschnitten.
Markdownlösung: ![Screenshot eines Ordners mit README.txt und der geöffneten README im Texteditor.]({{ '/assets/images/unit07/Screenshot[Nr]_ReadMe.png' | relative_url }})
Oder als HTML (lightbox) mit Vergrößerungsoption, Beschreibungstext beim Hovern und Galerie zum durchklicken:-->
 