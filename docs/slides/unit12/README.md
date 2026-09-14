# Unit 12 – Folien für die Präsenzsitzung

Für einen Termin von 90 Minuten mit etwa 100–150 Studierenden aus Bachelor und Lehramt. Die Erklärungen setzen keine Vorbereitung voraus. Format: 16:9, helle Folien und große Schrift für den Beamer.

- [PowerPoint bearbeiten und präsentieren](unit12_praesenz.pptx)
- [PDF der Folien](unit12_praesenz.pdf)
- [Moderationshinweise lesen](moderation.md)

Die Präsentation enthält 37 Folien: eine Titelfolie, 34 Hauptfolien, eine Reserve-/Quellenfolie und als letzte Folie „Vielen Dank für Ihre Aufmerksamkeit“. Die PowerPoint-Notizen enthalten Zeitfenster, Durchführungshinweise, erwartete Antworten, Kontrollwerte und Quellen. Die PDF zeigt dieselben sichtbaren Folien, aber keine Moderationsnotizen. Aufgaben und Auflösungen stehen auf getrennten Folien; Animationen sind nicht erforderlich.

Vor dem Termin auf Folie 2 den gesamten JiTT-Platzhalter durch die aktuelle Auswertung zu Unit 11 ersetzen. Der Block kann bei Bedarf dupliziert werden und umfasst insgesamt zehn Minuten. Nur tatsächliche, zusammengefasste und anonymisierte Rückmeldungen einsetzen.

## Ablauf

| Minuten | Schwerpunkt |
|---|---|
| 0–10 | JiTT zu Unit 11 |
| 10–25 | Linien, Polygone, Generalisierung und räumliche Beziehungen |
| 25–35 | Geoportalangebote, Metadaten und lokale Quelldaten unterscheiden |
| 35–50 | Drei Layer laden, 22/412/56 prüfen und zehn FFH-Flächen auswählen |
| 50–70 | Vier GBIF-Punkte und 106 Gewässerfeatures mit `intersects` auswählen |
| 70–80 | Beide Auswahlen exportieren, drei Ergebnislayer neu laden und dokumentieren |
| 80–85 | `intersects` und `within` am Grenzfall samt Koordinatenunsicherheit erklären |
| 85–90 | Eine Exit-Ticket-Frage beantworten und auf JiTT hinweisen |

Der verbindliche Praxisweg endet mit `data_output/unit12_results.gpkg`. Es enthält `schutzgebiete_auswahl` mit zehn Polygonfeatures, `gbif_in_schutzgebieten` mit vier Punkten und `gewaesser_an_schutzgebieten` mit 106 Linienfeatures. Das gemeinsame CRS ist `EPSG:25832`. Falls ein Schritt scheitert, steht `ersatz/unit12_results.gpkg` mit denselben Layernamen und Prüfzahlen bereit.

## Vor dem Termin bereitstellen

- QGIS 3.40 auf den verwendeten Rechnern startbereit
- vollständig entpacktes Marburger Übungspaket
- eigenes `unit11_results.gpkg/gbif_checked` oder `ersatz/unit11_results.gpkg/gbif_checked`
- `data_raw/marburg_basis.gpkg`, Layer `gewaesser` und `schutzgebiete`
- `documentation/quellen.md`, `processing_notes.md` und `pruefwerte.md`
- als Fallback `ersatz/unit12_results.gpkg` mit den drei Ergebnislayern

Die einzige Übungsaufgabe ist die Beantwortung der JiTT-Fragen zu Unit 12 im ILIAS-Kurs. Fragen und Frist stehen in ILIAS. Der konkrete Link ist auf der Kursseite noch ein Platzhalter. Unit 13 verwendet wieder alle 56 Punkte aus `gbif_checked`, nicht die vier Punkte des räumlichen Unit-12-Ergebnisses.

## Gestaltung und Abbildungen

Die Präsentation verwendet die nativen Master, Noto Sans und Universitätsfarben aus [präs_ms02_powerpoint_de.pptx](../Vorlagen/präs_ms02_powerpoint_de.pptx). Das originale Foto-/Kartenmotiv der FB19-Vorlage erscheint auf Titel und Abschluss. Universitätslogos stehen nur dort; Foliennummern sind schlicht, Zeitangaben stehen nur in den Notizen.

Alle fünf fachlichen SVG-Abbildungen der aktuellen Unit 12 sind eingebettet: Stützpunkte und Generalisierung, Polygonloch und Multipart, gemeinsamer Vektorworkflow, Auswahl versus Zuschneiden sowie der Punkt auf einer Polygongrenze. Texte, Tabellen und ergänzende Schemata bestehen aus bearbeitbaren PowerPoint-Formen.

## Bearbeitung und Export

Der reproduzierbare Ausgangsstand steht in [build_slides.py](build_slides.py). Das Skript benötigt LibreOffice mit Python-UNO-Anbindung, beide Originalvorlagen und die Zeichenhilfen aus dem benachbarten Unit-10-Builder. Es erzeugt PowerPoint, PDF, Moderationsdatei und die veröffentlichte PDF-Kopie unter `docs/assets/pdfs/Geodaten_Slides_Unit12.pdf` neu.

Aus dem Verzeichnis `docs/` ausführen:

```bash
/usr/bin/python3 slides/unit12/build_slides.py
```

Vorhandene Ausgaben werden überschrieben. Die exportierte PowerPoint wird erneut geöffnet und daraus die PDF erzeugt, damit beide sichtbaren Fassungen übereinstimmen. Direkte Änderungen an der PowerPoint entweder im Skript nachführen oder beide PDF-Fassungen anschließend erneut exportieren beziehungsweise kopieren. Eine Prüfung in Microsoft PowerPoint selbst erfolgte nicht.

## Quellenstand

Grundlage sind die aktuellen fünf Unit-12-Seiten, die QGIS-Kurzcheckliste und das Marburger Übungspaket vom 08.09.2026. Die Folien verlinken außerdem das QGIS-3.40-Benutzerhandbuch sowie die HLNUG-Seiten zu Naturschutz und Wasser. Der Abgleich der Folien erfolgte am 09.09.2026. Die Live-Erreichbarkeit externer Portale ist keine Voraussetzung für die Sitzung.
