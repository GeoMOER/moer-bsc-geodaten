---
title: ReadMe Dokumentation
published: true
toc: true
header:
  image: assets/images/unit07/DataSwamp_Stage07.png
  image_description: "Streuobstwiese"
  caption: "Image: ulrichstill [CC BY-SA 2.0 DE] via [wikimedia.org](https://commons.wikimedia.org/wiki/File:Tuebingen_Streuobstwiese.jpg)"
---

Wenn Sie nicht nur Messdaten unter FAIR Prinzipien zugänglich machen wollen, sondern ggf. Ihren Workflow, Ihre Analyse oder Ihren Code und entsprechend ein **Projektordner** teilen, ist eine README Datei hilfreich - und je nach Plattform auch eine Voraussetzung zur Veröffentlichung!

## Die README-Datei
 
Eine README ist die erste Datei, die eine fremde Person im Ordner öffnen sollte. Sie erklärt, was der Ordner enthält und wie man ihn nutzt. Je nach Plattform und vorhandenen Dateiformaten und natürlich Ziel des Projektes (reine Analyse, Programm etc) können unterschiedliche Ansprüche an diese README vorhanden sein. Einige Punkte bleiben aber gleich:

1. Titel und Kurzbeschreibung  - Was ist das, wofür wurde es erstellt?
2. Verantwortliche - Kontaktangaben
3. Datum & Version - Wann wurde es erstellt, ggf. Version
4. Lizenz/Zitiehinweis

Wenn Sie eigene Funktionen erstellt haben (s. Unit 08) würden Sie noch **Features** beschreiben. 

Wenn **Daten** genutzt werden ist es natürlich essentiell, deren **Quelle (inkl. Abrufdatum)** und/oder **Messmethode** zu beschreiben, welchen **Zeitraum** sie abdecken, an welchen **Orten** sie gemessen wurden. Des Weiteren sollten Informationen zu Datenstruktur (Format, Codierung, Trennzeichen, NA-Codierung etc) genannt werden.
 
 
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
 