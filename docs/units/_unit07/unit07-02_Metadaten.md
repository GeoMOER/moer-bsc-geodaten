---
title: Metadaten und README
published: true
toc: true
header:
  image: /assets/images/unit05/notebook.jpg
  caption: "Image: [Neil Conway](https://www.flickr.com/photos/neilconway/) [(Public Domain Mark 1.0)](https://creativecommons.org/publicdomain/mark/1.0/deed.en) via [flickr.com](https://www.flickr.com/photos/neilconway/5625707813/in/photostream/)"
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

**Ebene 1: der ganze Datensatz.** Angaben, die für die gesamte Datei oder den gesamten Ordner gelten.

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

| Spalte | Bedeutung | Einheit | Datentyp / Skalenniveau | Fehlende Werte | Herkunft / Messmethode |
|---|---|---|---|---|---|
| Standort | Name der Messstation | – | Text / nominal | nicht vorgesehen | Zuordnung laut Rohdatei |
| Latitude | geografische Breite | Grad (dezimal) | Zahl / Grenzfall (siehe Kapitel zu Datentypen) | nicht vorgesehen | Stationsdokumentation |
| Longitude | geografische Länge | Grad (dezimal) | Zahl / Grenzfall | nicht vorgesehen | Stationsdokumentation |
| Datum | Datum der Messung | – | Datum / Intervall | nicht vorgesehen | Zeitstempel des Sensors |
| Uhrzeit | Uhrzeit der Messung | hh:mm:ss | Uhrzeit / Intervall | nicht vorgesehen | Zeitstempel des Sensors |
| Temperatur | Lufttemperatur an der Station | °C | Zahl / Intervall | leere Zelle | Sensor, automatische Messung |
| Messmethode | Art der Messung | – | Text / nominal | nicht vorgesehen | Angabe des Netzwerks |
| Versiegelung | mittlerer Versiegelungsgrad im 100-m-Radius um die Station (ergänzt mit `SVERWEIS`) | % | Zahl / Verhältnis | nicht vorgesehen | Copernicus-Raster, Mittel im 100-m-Radius |

Die Spalte „Herkunft / Messmethode“ ist wichtig, weil sich die Erfassung je Spalte unterscheiden kann: Die Temperatur stammt von einem Sensor, die Versiegelung aus einem Raster, `Standort_clean` ist per Formel berechnet. Eine einzige Angabe „Messmethode: Sensor“ für die ganze Datei würde das verdecken. Ähnlich unterscheiden sich Herkunft, Zeitraum und Umfang je Datei, deshalb hat die README dafür eine Tabelle (Abschnitt 3).

> Wer Daten mit einer DOI veröffentlicht, muss mindestens sechs Angaben machen: Identifier, Creator, Title, Publisher, PublicationYear und ResourceType. Das ist der Mindeststandard des Metadatenschemas DataCite. Wo diese Angaben liegen, hängt vom Repositorium ab.

## Wie hängt das zusammen? Dokumentation, Metadaten und README

Die Begriffe werden leicht verwechselt. Ein Überblick:

```
Dokumentation (Oberbegriff: alles, was erklärt, wie Daten entstanden sind und zu verstehen sind)
├─ Metadaten: strukturierte Angaben ÜBER die Daten
│   ├─ Datensatz-Ebene: Titel, Ersteller:in, Zeitraum, Format, Lizenz …
│   └─ Spalten-Ebene (Datenwörterbuch): Bedeutung, Einheit, Typ, Codierung fehlender Werte
├─ README: lesbare Einstiegsdatei im Ordner; enthält Metadaten und verweist auf den Rest
└─ Bearbeitung: welche Schritte wurden mit den Daten gemacht (steht in der README, Abschnitt 6)
```

**Merksatz:** Metadaten sind der **Inhalt**, die README ist ein möglicher **Behälter** dafür. Metadaten können auch an anderen Stellen liegen, etwa in einer Datenbank, in einer XML-Datei oder im Kopf einer Bilddatei. Die README ist die einfachste Form: eine Textdatei, die jede Person mit jedem Programm öffnen kann.

## Die README-Datei

Eine README ist die erste Datei, die eine fremde Person im Ordner öffnen sollte. Sie erklärt, was der Ordner enthält und wie man ihn nutzt.

| Abschnitt | Inhalt |
|---|---|
| 1. Titel und Kurzbeschreibung | Was ist das, wofür wurde es erstellt? |
| 2. Verantwortliche | Name, Kontakt, Datum, Version |
| 3. Inhalt des Ordners | Eine Zeile pro Datei: Zweck, Herkunft, Zeitraum und Ort, Anzahl Einträge |
| 4. Methode (Überblick) | Datengeber, Methode in Kurzform wie im Aufsatz |
| 5. Datenstruktur | Format, Kodierung, Trennzeichen, Datenwörterbuch (oder Verweis auf das Blatt in der Excel-Datei) |
| 6. Bearbeitung | Schritte in der Reihenfolge, Versionen und Zwischenstände (oder Verweis auf das Blatt), Software, Ort der Rohdaten, Ablage und Zugriff |
| 7. Qualität und Besonderheiten | Fehlende Werte, Auffälligkeiten |
| 8. Nutzung | Lizenz, Zitierhinweis |
| 9. Verweise | Quellen, verwandte Datensätze |

![Die neun Abschnitte einer README. Die Abschnitte 3 bis 7 tragen die Methodenbeschreibung.]({{ '/assets/images/unit07/unit07_readme_aufbau.png' | relative_url }})

**Hinweise zur Form:**
- Dateiname immer gleich: `README.txt`.
- Format: reine Textdatei in UTF-8, keine Word-Datei. Das ist dasselbe Prinzip wie bei CSV: Ein Format, das jedes Programm liest, bleibt auch in zehn Jahren lesbar.
- Kurz halten und aktuell halten. Eine falsche README ist schlechter als keine.
- Die unveränderten Rohdaten gehören nicht in die README, aber ihr Speicherort.
- Versionen gehören dazu: Wenn Sie Zwischenstände aufheben (Kopien, Blätter v1, v2, ...), halten Sie in einer kleinen Tabelle fest, welcher Stand woraus entstanden ist, was sich geändert hat und welcher der aktuelle ist (in einer Excel-Arbeitsmappe als Blatt „Versionen“, siehe unten). Sonst weiß eine fremde Person nicht, welche Datei sie verwenden soll.
- Ablage und Zugriff gehören dazu: Wo liegen die Dateien (lokal oder Cloud), gibt es ein Backup, und wer darf darauf zugreifen? Auch das sollte eine fremde Person nicht erraten müssen.

**Bearbeitungsschritte:** Der Abschnitt 6 hält fest, was Sie in den letzten Kapiteln getan haben. Beispiel:

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

## Beschreibung in der Excel-Datei

Eine Arbeitsmappe wandert oft ohne ihren Ordner weiter, zum Beispiel per E-Mail. Außerdem existieren die Blattversionen (v0, v1, …) nur in der Datei. Deshalb gehört die Beschreibung der Tabelle in die Arbeitsmappe selbst, als eigene Blätter am Anfang:

- **Blatt „Versionen“:** welches Blatt aus welchem entstanden ist, was sich geändert hat und welcher Stand der aktuelle ist.
- **Blatt „Datenwörterbuch“:** eine Zeile pro Spalte mit Bedeutung, Einheit, Datentyp, Skalenniveau und Codierung fehlender Werte.

Die README im Ordner bleibt der Einstieg. Sie beschreibt den Ordner (eine Zeile pro Datei mit Zweck, Herkunft, Zeitraum und Anzahl Einträgen), die Methode im Überblick, Ablage und Zugriff, Qualität und Nutzung und verweist für Wörterbuch und Versionen auf die Blätter („siehe Blatt Datenwörterbuch in Datei X“). So steht jede Angabe nur an einer Stelle und kann nicht widersprüchlich werden.

![Ordner-README und Beschreibungsblätter in der Arbeitsmappe: Versionen und Datenwörterbuch als eigene Blätter.]({{ '/assets/images/unit07/unit07_ordner_arbeitsmappe.png' | relative_url }})

Bei **CSV-Dateien** gibt es keine Blätter. Dort stehen Datenwörterbuch und Versionen in der README. Außerdem bleibt die README als Textdatei auch dann lesbar, wenn die Excel-Datei einmal nicht mehr geöffnet werden kann.

## Die Methodenbeschreibung

Bevor Sie eine README schreiben, hilft ein Blick auf eine Methodenbeschreibung, wie sie in einem wissenschaftlichen Aufsatz stehen würde. Sie beantwortet knapp und in Fachsprache, wie die Daten entstanden sind. Hier ein fiktives Beispiel zu einem anderen Thema:

> Niederschlagsdaten wurden an der Station „Wiesenweg“ (50,81° N, 8,77° O; 215 m ü. NN) mit einem Kippwaagen-Regenmesser (Auflösung 0,2 mm, Auffangfläche 200 cm²) erfasst. Der Sensor registrierte jedes Kippereignis; der Datenlogger aggregierte die Ereignisse zu Stundensummen (UTC). Die Messreihe umfasst den Zeitraum vom 1. Mai bis 31. August 2026 (n = 2 952 Stundenwerte). Die Daten wurden vom Stationsbetreiber bereitgestellt. Logger-Ausfälle (Platzhalter −999) wurden von der Auswertung ausgeschlossen, doppelt registrierte Zeitstempel (n = 12) entfernt. Aus den Stundensummen wurden Tagessummen (00:00–23:59 UTC) berechnet. Die Auswertung erfolgte mit Microsoft Excel 365.

Sie enthält: **Was** wurde erfasst, **wo**, **wann**, **womit** und in welchen Abständen, **woher** stammen die Daten, welche **Qualitätsprüfung** und **Aggregation** gab es und mit welcher **Software** wurde ausgewertet.

Nicht in der Methode stehen die praktischen Angaben: Ordnerstruktur und Dateinamen, die einzelnen Arbeitsschritte (zum Beispiel „Pivot-Tabelle“ oder „Suchen und Ersetzen“), Kontrollwerte, Speicherort, Sicherungskopie, Zugriff, Lizenz und Ansprechperson. Diese Angaben gehören in die README. Methode und README ergänzen sich also:

![Gegenüberstellung: Die Methode beschreibt wie im Aufsatz, die README enthält die praktischen Angaben.]({{ '/assets/images/unit07/unit07_methode_readme.png' | relative_url }})

Ein vollständiges Beispiel zu demselben fiktiven Projekt finden Sie in `README_Beispiel_Niederschlag.txt`.

## Übung Runde 2: Lücken-README ausfüllen (Gruppenarbeit)**

Jetzt wenden Sie es auf Daten an, die Sie kennen: die Marburger Kursdaten. Jede Gruppe wählt einen Projektordner aus. Zusammen ergänzen Sie das vorbereitetes README mit Lücken (`Lueckenreadme_Runde2.txt`). Was Sie nicht wissen, schreiben Sie nicht vermutend hin, sondern als „[fehlt: …]“ und notieren, wen Sie fragen müssten. Die Gruppe gibt den Ordner in der ILIAS-Übung ab (Team = Ihre Gruppennummer + FARBE). Nach der Frist ist die Abgabe eingefroren.


Ausgefüllte Beispiele finden Sie in den Dateien `README_Beispiel_Sensordaten.txt` und `README_Beispiel_Niederschlag.txt`. Die Vorlage für die eigene Arbeit ist `README_Vorlage.txt`.


## Additional resources

- DataCite Metadata Working Group: DataCite Metadata Schema. https://datacite-metadata-schema.readthedocs.io
