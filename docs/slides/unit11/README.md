# Unit 11 – Folien für die Präsenzsitzung

Für einen Termin von 90 Minuten mit etwa 100–150 Studierenden aus Bachelor und Lehramt. Die Erklärungen setzen keine Vorbereitung voraus. Format: 16:9, helle Folien und große Schrift für den Beamer.

- [PowerPoint bearbeiten und präsentieren](unit11_praesenz.pptx)
- [PDF der Folien](unit11_praesenz.pdf)
- [Moderationshinweise lesen](moderation.md)

Die Präsentation enthält 36 Folien: eine Titelfolie, 32 Hauptfolien, zwei Reserve-/Quellenfolien und als letzte Folie „Vielen Dank für Ihre Aufmerksamkeit“. Die PowerPoint-Notizen enthalten Zeitfenster, Durchführungshinweise, erwartete Antworten, Kontrollwerte und Quellen. Die PDF zeigt dieselben sichtbaren Folien, aber keine Moderationsnotizen. Aufgaben und Auflösungen stehen auf getrennten Folien; Animationen sind nicht erforderlich.

Vor dem Termin auf Folie 2 den gesamten JiTT-Platzhalter durch die aktuelle Auswertung zu Unit 10 ersetzen. Der Block kann bei Bedarf dupliziert werden und umfasst insgesamt zehn Minuten. Nur tatsächliche, zusammengefasste und anonymisierte Rückmeldungen einsetzen.

## Ablauf

| Minuten | Schwerpunkt |
|---|---|
| 0–10 | JiTT zu Unit 10 |
| 10–23 | Punktfeature, Occurrence Record und Kartenaussage unterscheiden |
| 23–28 | Kurzer QGIS-Wiedereinstieg und Projektstart |
| 28–43 | CSV prüfen und mit EPSG:4326 als Punktlayer importieren |
| 43–62 | Lage prüfen und Qualitätsregel zur Koordinatenunsicherheit anwenden |
| 62–75 | Auswahl als `gbif_checked` in EPSG:25832 exportieren und neu laden |
| 75–85 | Qualitätsentscheidung dokumentieren und Punktkarte vorsichtig interpretieren |
| 85–90 | Eine Exit-Ticket-Frage beantworten und auf JiTT hinweisen |

Der verbindliche Praxisweg endet mit `data_output/unit11_results.gpkg`, Layer `gbif_checked`. Der Layer enthält 56 der 79 Records. Die Regel lautet `0 < coordinateUncertaintyInMeters <= 100`; 23 Records mit 250 m Unsicherheit werden ausgeschlossen. Wenn Import oder Export scheitert, steht `ersatz/unit11_results.gpkg`, Layer `gbif_checked`, als transparenter Fallback bereit.

## Vor dem Termin bereitstellen

- QGIS 3.40 auf den verwendeten Rechnern startbereit
- vollständig entpacktes Marburger Übungspaket
- `data_raw/gbif_feuersalamander_marburg.csv` und zugehörige `.csvt`
- `data_raw/marburg_basis.gpkg`, Layer `untersuchungsgebiet`
- `documentation/quellen.md`, `processing_notes.md` und `pruefwerte.md`
- als Fallback `ersatz/unit11_results.gpkg`, Layer `gbif_checked`

Die einzige Übungsaufgabe ist die Beantwortung der JiTT-Fragen zu Unit 11 im ILIAS-Kurs. Fragen und Frist stehen in ILIAS. Der konkrete Link ist auf der Kursseite noch ein Platzhalter.

## Gestaltung und Abbildungen

Die Präsentation verwendet die nativen Master, Noto Sans und Universitätsfarben aus [präs_ms02_powerpoint_de.pptx](../Vorlagen/präs_ms02_powerpoint_de.pptx). Das originale Foto-/Kartenmotiv der FB19-Vorlage erscheint auf Titel und Abschluss. Universitätslogos stehen nur dort; Foliennummern sind schlicht, Zeitangaben stehen nur in den Notizen.

Alle fünf fachlichen SVG-Abbildungen der aktuellen Unit 11 sind eingebettet: Überlagerung mehrerer Records, Punkt/Beobachtung/Unsicherheit, GBIF-Workflow, CSV-Import und Beobachtungsbias. Für den fünfminütigen Wiedereinstieg wird zusätzlich die QGIS-Oberflächenabbildung aus Unit 10 verwendet. Texte, Tabellen und ergänzende Schemata bestehen aus bearbeitbaren PowerPoint-Formen.

## Bearbeitung und Export

Der reproduzierbare Ausgangsstand steht in [build_slides.py](build_slides.py). Das Skript benötigt LibreOffice mit Python-UNO-Anbindung, beide Originalvorlagen und die Zeichenhilfen aus dem benachbarten Unit-10-Builder. Es erzeugt PowerPoint, PDF und Moderationsdatei neu.

Aus dem Verzeichnis `docs/` ausführen:

```bash
/usr/bin/python3 slides/unit11/build_slides.py
```

Vorhandene Ausgaben werden überschrieben. Die exportierte PowerPoint wird erneut geöffnet und daraus die PDF erzeugt, damit beide sichtbaren Fassungen übereinstimmen. Direkte Änderungen an der PowerPoint entweder im Skript nachführen oder die PDF anschließend erneut exportieren. Eine Prüfung in Microsoft PowerPoint selbst erfolgte nicht.

## Quellenstand

Grundlage sind die aktuellen fünf Unit-11-Seiten, die QGIS-Kurzcheckliste und das Marburger Übungspaket vom 08.09.2026. Die Folien verlinken außerdem das QGIS-3.40-Benutzerhandbuch und den Datensatz-DOI `10.15468/uc1apo`. Der Abgleich der Folien erfolgte am 09.09.2026. Die Live-Erreichbarkeit externer Seiten ist keine Voraussetzung für die Sitzung.
