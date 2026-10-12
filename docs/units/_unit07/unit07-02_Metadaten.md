---
title: METADATEN
published: true
toc: true
header:
  image: assets/images/unit07/DataSwamp_Stage07.png
  image_description: "Streuobstwiese"
  caption: "Image: ulrichstill [CC BY-SA 2.0 DE] via [wikimedia.org](https://commons.wikimedia.org/wiki/File:Tuebingen_Streuobstwiese.jpg)"
---


Im letzten Kapitel haben wir gesehen, dass unserem Sensordatensatz für „findbar“ und „wiederverwendbar“ vor allem Beschreibungen fehlen. In diesem Kapitel lernen Sie, wie man diese Beschreibungen aufschreibt: als Metadaten, die in einer README-Datei festgehalten werden.
 
## Fragen, die die Daten nicht beantworten
 
Eine Tabelle mit Spalten wie `Standort;Datum;Temperatur` sieht selbsterklärend aus, solange man sie selbst erzeugt hat. Eine fremde Person hat dagegen viele Fragen:
 
- Was ist das, und wofür wurde es erstellt?
- Woher stammen die Daten, und wer hat sie erzeugt?
- Wann wurden sie erhoben?
- In welcher Einheit steht die Temperatur?
- Was bedeutet `-999` oder eine leere Zelle?
- Darf ich die Daten nutzen?
Diese Fragen beantworten die Daten selbst nicht. Die Antworten heißen **Metadaten**: strukturierte Angaben über die Daten, die man braucht, um sie zu verstehen und nachzunutzen.
 
## Metadaten auf zwei Ebenen
 
**Ebene 1: der ganze Datensatz.** Angaben, die für die gesamte Datei oder den gesamten Ordner gelten. Diese werden auch gerne in einem ReadMe hinterlegt (s. nächstes Kapitel)
 
| Angabe | Beispiel aus unseren Sensordaten |
|---|---|
| Titel | Temperaturmessungen der Marburger Umweltsensoren, bereinigt und zusammengeführt |
| Ersteller:in | Ihr Name |
| Zeitraum | Beginn bis Ende der Messungen |
| Ort | Marburg, Stadtgebiet |
| Format | CSV, UTF-8, Semikolon als Trennzeichen |
| Quelle | Marburger Umweltsensoren-Netzwerk |
| Lizenz | wird vom Datenhalter vorgegeben |
| Version | v1 |
 
**Ebene 2: jede einzelne Spalte.** Diese Beschreibung nennt man **Datenwörterbuch**. Hier wird das nachgeholt, was wir in den Kapiteln zu Zellformaten und Fehlwerten angekündigt haben: die Einheit gehört nicht in die Zelle, sondern in die Beschreibung, und fehlende Werte müssen eindeutig benannt sein.
 
| Spalte | Bedeutung | Einheit | Datentyp / Skalenniveau | Fehlende Werte |
|---|---|---|---|---|
| Standort | Name der Messstation | – | Text / nominal | nicht vorgesehen |
| Latitude | geografische Breite | Grad (dezimal) | Zahl / Grenzfall (siehe Kapitel zu Datentypen) | nicht vorgesehen |
| Longitude | geografische Länge | Grad (dezimal) | Zahl / Grenzfall | nicht vorgesehen |
| Datum | Datum der Messung | – | Datum / Intervall | nicht vorgesehen |
| Uhrzeit | Uhrzeit der Messung | hh:mm:ss | Uhrzeit / Intervall | nicht vorgesehen |
| Temperatur | Lufttemperatur an der Station | °C | Zahl / Intervall | leere Zelle |
| Messmethode | Art der Messung | – | Text / nominal | nicht vorgesehen |
 

## Übung: Metadaten (Ebene 2)
 
Arbeiten Sie mit Ihrer zusammengeführten Tabelle aus dem letzten Lernabschnitt.
 
1. Erstellen Sie ein Datenwörterbuch mit einer Zeile pro Spalte (Bedeutung, Einheit, Datentyp und Skalenniveau, Codierung fehlender Werte). Falls Ihre Tabelle weitere Spalten hat, etwa die Höhe über NN, ergänzen Sie diese.