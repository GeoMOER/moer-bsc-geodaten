# Unit 13 – Folien für die Präsenzsitzung

Für einen Termin von 90 Minuten mit etwa 100–150 Studierenden aus Bachelor und Lehramt. Die Erklärungen setzen keine Vorbereitung voraus. Format: 16:9, helle Folien und große Schrift für den Beamer.

- [PowerPoint bearbeiten und präsentieren](unit13_praesenz.pptx)
- [PDF der Folien](unit13_praesenz.pdf)
- [Moderationshinweise lesen](moderation.md)

Die Präsentation enthält 36 Folien: eine Titelfolie, 32 Hauptfolien, zwei Reserve-/Quellenfolien und als letzte Folie „Vielen Dank für Ihre Aufmerksamkeit“. Die PowerPoint-Notizen enthalten Zeitfenster, Durchführungshinweise, erwartete Antworten, Kontrollwerte und Quellen. Die PDF zeigt dieselben sichtbaren Folien, aber keine Moderationsnotizen. Aufgaben und Auflösungen stehen auf getrennten Folien; Animationen sind nicht erforderlich.

Vor dem Termin auf Folie 2 den gesamten JiTT-Platzhalter durch die aktuelle Auswertung zu Unit 12 ersetzen. Der Block kann bei Bedarf dupliziert werden und umfasst insgesamt zehn Minuten. Nur tatsächliche, zusammengefasste und anonymisierte Rückmeldungen einsetzen.

## Ablauf

| Minuten | Schwerpunkt |
|---|---|
| 0–10 | JiTT zu Unit 12 |
| 10–25 | Rasterzellen, Zellwerte, Rastertypen sowie DGM und DOM unterscheiden |
| 25–40 | DGM laden und Quelle, Zellgröße, Ausdehnung, CRS, Einheit und NoData prüfen |
| 40–55 | Werte abfragen, Pseudofarbe verwenden sowie Auflösung und Genauigkeit trennen |
| 55–75 | Rasterwerte an allen 56 Punkten abtasten und das Feld `hoehe_m` herstellen |
| 75–85 | Ergebnis mit 35 Höhen und 21 `NULL` speichern, kontrollieren und dokumentieren |
| 85–90 | Eine Exit-Ticket-Frage beantworten und auf JiTT hinweisen |

Der verbindliche Praxisweg endet mit `data_output/unit13_results.gpkg`, Layer `gbif_mit_hoehe`. Er enthält weiterhin alle 56 Punkte: 35 mit gültigem `hoehe_m` und 21 mit `NULL`. Das DGM besitzt 2.000 × 2.000 Zellen à 10 m, ein Float32-Band, `EPSG:25832`, Höhen in Metern bezogen auf `DHHN2016_NH` und NoData `-9999`. Falls ein Schritt scheitert, steht `ersatz/unit13_results.gpkg/gbif_mit_hoehe` bereit.

## Vor dem Termin bereitstellen

- QGIS 3.40 auf den verwendeten Rechnern startbereit
- vollständig entpacktes Marburger Übungspaket
- eigenes `unit11_results.gpkg/gbif_checked` oder `ersatz/unit11_results.gpkg/gbif_checked`
- `data_raw/dgm_marburg_10m.tif`
- `documentation/quellen.md`, `dgm_kacheln.json`, `processing_notes.md` und `pruefwerte.md`
- als Fallback `ersatz/unit13_results.gpkg`, Layer `gbif_mit_hoehe`

Die einzige Übungsaufgabe ist die Beantwortung der JiTT-Fragen zu Unit 13 im ILIAS-Kurs. Fragen und Frist stehen in ILIAS. Der konkrete Link ist auf der Kursseite noch ein Platzhalter. Unit 14 verwendet nur die 35 Punkte mit gültigem `hoehe_m`; die räumliche Einschränkung bleibt zu dokumentieren.

## Gestaltung und Abbildungen

Die Präsentation verwendet die nativen Master, Noto Sans und Universitätsfarben aus [präs_ms02_powerpoint_de.pptx](../Vorlagen/präs_ms02_powerpoint_de.pptx). Das originale Foto-/Kartenmotiv der FB19-Vorlage erscheint auf Titel und Abschluss. Universitätslogos stehen nur dort; Foliennummern sind schlicht, Zeitangaben stehen nur in den Notizen.

Alle sechs fachlichen SVG-Abbildungen der aktuellen Unit 13 sind eingebettet: DGM und DOM, Rastervergröberung, Rasterausrichtung, Zellgröße/NoData/Genauigkeit, unveränderte Werte bei anderer Farbskala und das Abtasten eines Rasterwerts. Texte, Tabellen und ergänzende Schemata bestehen aus bearbeitbaren PowerPoint-Formen.

## Bearbeitung und Export

Der reproduzierbare Ausgangsstand steht in [build_slides.py](build_slides.py). Das Skript benötigt LibreOffice mit Python-UNO-Anbindung, beide Originalvorlagen und die Zeichenhilfen aus dem benachbarten Unit-10-Builder. Es erzeugt PowerPoint, PDF, Moderationsdatei und die veröffentlichte PDF-Kopie unter `docs/assets/pdfs/Geodaten_Slides_Unit13.pdf` neu.

Aus dem Verzeichnis `docs/` ausführen:

```bash
/usr/bin/python3 slides/unit13/build_slides.py
```

Vorhandene Ausgaben werden überschrieben. Die exportierte PowerPoint wird erneut geöffnet und daraus die PDF erzeugt, damit beide sichtbaren Fassungen übereinstimmen. Direkte Änderungen an der PowerPoint entweder im Skript nachführen oder beide PDF-Fassungen anschließend erneut exportieren beziehungsweise kopieren. Eine Prüfung in Microsoft PowerPoint selbst erfolgte nicht.

## Quellenstand

Grundlage sind die aktuellen fünf Unit-13-Seiten, die QGIS-Kurzcheckliste und das Marburger Übungspaket vom 08.09.2026. Rastermetadaten und Kontrollfälle wurden zusätzlich direkt mit GDAL/OGR am Paket geprüft. Die Folien verlinken das QGIS-3.40-Benutzerhandbuch und Hessen Geodatenmanagement. Der Abgleich der Folien erfolgte am 09.09.2026. Die Live-Erreichbarkeit externer Seiten ist keine Voraussetzung für die Sitzung.
