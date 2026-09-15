# Unit 10 – Folien für die Präsenzsitzung

Für einen Termin von 90 Minuten mit etwa 100–150 Studierenden aus Bachelor und Lehramt. Die Erklärungen setzen keine Vorbereitung voraus. Format: 16:9, helle Folien und große Schrift für den Beamer.

- [PowerPoint bearbeiten und präsentieren](unit10_praesenz.pptx)
- [PDF der Folien](unit10_praesenz.pdf)
- [Moderationshinweise lesen](moderation.md)

Die Präsentation enthält 33 Folien: eine Titelfolie, 29 Hauptfolien, zwei Reserve-/Quellenfolien und als letzte Folie „Vielen Dank für Ihre Aufmerksamkeit“. Die PowerPoint-Notizen enthalten Zeitfenster, Durchführungshinweise, erwartete Antworten, Kontrollwerte und Quellen. Die PDF zeigt dieselben sichtbaren Folien, aber keine Moderationsnotizen. Aufgaben und Auflösungen stehen auf getrennten Folien; Animationen sind nicht erforderlich.

Vor dem Termin auf Folie 2 den gesamten JiTT-Platzhalter durch die aktuelle Auswertung zu Unit 09 ersetzen. Der Block kann bei Bedarf dupliziert werden und umfasst insgesamt zehn Minuten. Nur tatsächliche, zusammengefasste und anonymisierte Rückmeldungen einsetzen.

## Ablauf

| Minuten | Schwerpunkt |
|---|---|
| 0–10 | JiTT zu Unit 09 |
| 10–22 | Vektor und Raster vergleichen und gemeinsam zuordnen |
| 22–30 | Projekt, Layer und Datenquelle unterscheiden |
| 30–55 | Projekt anlegen sowie Gewässerlayer und DGM laden |
| 55–68 | Feature, Attribute, Datenquellen und CRS prüfen und dokumentieren |
| 68–78 | Projekt speichern, schließen, erneut öffnen und kontrollieren |
| 78–85 | WMS demonstrieren oder sofort zum Offline-Ersatz wechseln |
| 85–90 | Eine Exit-Ticket-Frage beantworten und auf JiTT hinweisen |

Der verbindliche Praxisweg endet mit `unit10_einstieg.qgz`, das `gewaesser` und `dgm_marburg_10m` nach dem erneuten Öffnen ohne Pfadreparatur erreicht. Die WMS-Einrichtung auf studentischen Geräten ist keine Voraussetzung. Die Lehrperson beendet die Demonstration spätestens in Minute 85 und verwendet bei einem Dienstausfall ohne weitere Fehlersuche das vorbereitete Ersatzmaterial.

## Vor dem Termin bereitstellen

- QGIS 3.40 auf den verwendeten Rechnern startbereit
- vollständig entpacktes Marburger Übungspaket
- `data_raw/marburg_basis.gpkg`, Layer `gewaesser`
- `data_raw/dgm_marburg_10m.tif`
- `documentation/processing_notes.md`
- für die WMS-Demo die auf der Kursseite angegebene Dienstadresse und den Layer `Naturschutzgebiete`
- als Offline-Ersatz `ersatz/wms_schutzgebiete.png`, `ersatz/wms_capabilities.xml` und `documentation/quellen.md`

Die einzige Übungsaufgabe ist die Beantwortung der JiTT-Fragen zu Unit 10 im ILIAS-Kurs. Fragen und Frist stehen in ILIAS. Der konkrete Link ist auf der Kursseite noch ein Platzhalter.

## Gestaltung und Abbildungen

Die Präsentation verwendet die nativen Master, Noto Sans und Universitätsfarben aus [präs_ms02_powerpoint_de.pptx](../Vorlagen/präs_ms02_powerpoint_de.pptx). Das originale Foto-/Kartenmotiv der FB19-Vorlage erscheint auf Titel und Abschluss. Universitätslogos stehen nur dort; Foliennummern sind schlicht, Zeitangaben stehen nur in den Notizen.

Passende Abbildungen der aktuellen Unit-10-Seiten sind als Vektorgrafiken eingebettet: Datenmodelle, Projekt/Layer/Datenquelle, QGIS-Oberfläche, Layerreihenfolge, Download/Webdienst und WMS/WFS. Der vorbereitete WMS-Ersatz stammt unverändert aus dem Marburger Übungspaket. Texte, Tabellen und ergänzende Schemata bestehen aus bearbeitbaren PowerPoint-Formen.

## Bearbeitung und Export

Der reproduzierbare Ausgangsstand steht in [build_slides.py](build_slides.py). Das Skript benötigt LibreOffice mit Python-UNO-Anbindung und beide Originalvorlagen. Es übernimmt außerdem das WMS-Ersatzbild aus `assets/data/marburg/marburg_geodaten.zip` und erzeugt PowerPoint, PDF und Moderationsdatei neu.

Aus dem Verzeichnis `docs/` ausführen:

```bash
/usr/bin/python3 slides/unit10/build_slides.py
```

Vorhandene Ausgaben werden überschrieben. Die exportierte PowerPoint wird erneut geöffnet und daraus die PDF erzeugt, damit beide sichtbaren Fassungen übereinstimmen. Direkte Änderungen an der PowerPoint entweder im Skript nachführen oder die PDF anschließend erneut exportieren. Eine Prüfung in Microsoft PowerPoint selbst erfolgte nicht.

## Quellenstand

Grundlage sind die aktuellen fünf Unit-10-Seiten, die QGIS-Kurzcheckliste und das Marburger Übungspaket vom 08.09.2026. Die Folien verlinken außerdem das QGIS-3.40-Benutzerhandbuch und die HLNUG-Metadatenseite. Der Abgleich der Folien erfolgte am 09.09.2026. Die Live-Erreichbarkeit des WMS ist keine Voraussetzung für die Sitzung.
