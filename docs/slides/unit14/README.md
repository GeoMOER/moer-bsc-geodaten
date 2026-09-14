# Unit 14 – Folien für die Präsenzsitzung

Für einen Termin von 90 Minuten mit etwa 100–150 Studierenden aus Bachelor und Lehramt. Die Erklärungen setzen keine Vorbereitung voraus. Format: 16:9, helle Folien und große Schrift für den Beamer.

- [PowerPoint bearbeiten und präsentieren](unit14_praesenz.pptx)
- [PDF der Folien](unit14_praesenz.pdf)
- [Moderationshinweise lesen](moderation.md)

Die Präsentation enthält 39 Folien: eine Titelfolie, 35 Hauptfolien, zwei Reserve-/Quellenfolien und als letzte Folie „Vielen Dank für Ihre Aufmerksamkeit“. Die PowerPoint-Notizen enthalten Zeitfenster, Durchführungshinweise, erwartete Antworten, Kontrollwerte und Quellen. Die PDF zeigt dieselben sichtbaren Folien, aber keine Moderationsnotizen. Aufgaben und Auflösungen benötigen keine Animationen.

Vor dem Termin auf Folie 2 den gesamten JiTT-Platzhalter durch die aktuelle Auswertung zu Unit 13 ersetzen. Der Block kann bei Bedarf dupliziert werden und umfasst insgesamt zehn Minuten. Nur tatsächliche, zusammengefasste und anonymisierte Rückmeldungen einsetzen.

## Ablauf

| Minuten | Schwerpunkt |
|---|---|
| 0–10 | JiTT zu Unit 13 |
| 10–18 | `unit14_start.qgz` als Arbeitskopie speichern sowie Kartenfrage, Zielgruppe, 35 Punkte und `hoehe_m` prüfen |
| 18–30 | Gleiche Intervalle und Quantile mit jeweils fünf Klassen vergleichen und eine Methode begründen |
| 30–45 | Gewählte Klassifizierung umsetzen und visuelle Hierarchie prüfen |
| 45–62 | Vorbereitetes Layout öffnen, Titel und Legende überarbeiten, Ausschnitt, Maßstab und Quellen kontrollieren |
| 62–70 | PDF und PNG mit 150 dpi exportieren, öffnen und prüfen |
| 70–80 | Partnercheck durchführen, eine Korrektur übernehmen und betroffene Ausgabe erneuern |
| 80–85 | Klassifizierung, Quellen und Aussagegrenze dokumentieren |
| 85–90 | Eine Exit-Ticket-Frage beantworten und auf JiTT hinweisen |

Der verbindliche Praxisweg endet mit `unit14_abschluss.qgz`, `figures/abschlusskarte_unit14.pdf`, `figures/abschlusskarte_unit14.png` und dem ergänzten Abschnitt in `documentation/processing_notes.md`. Die Kartenübung verwendet 35 Nachweise mit gültigem `hoehe_m`; die 21 weiteren geprüften Nachweise ohne DGM-Höhe bleiben eine sichtbare Aussagegrenze. Falls das eigene Projekt ausfällt, wird mit `unit14_beispiel.qgz` weitergearbeitet.

## Vor dem Termin bereitstellen

- QGIS 3.40 auf den verwendeten Rechnern startbereit
- vollständig entpacktes Marburger Übungspaket
- `unit14_start.qgz` und `unit14_beispiel.qgz`
- `ersatz/unit14_results.gpkg` mit 35 gültigen Höhenpunkten
- `ersatz/klassifizierung_intervalle.png` und `ersatz/klassifizierung_quantile.png`
- vorhandenes Layout `abschlusskarte_unit14`
- `documentation/processing_notes.md`

Die einzige Übungsaufgabe ist die Beantwortung der JiTT-Fragen zu Unit 14 im ILIAS-Kurs. Fragen und Frist stehen in ILIAS; der konkrete Link ist auf der Kursseite noch ein Platzhalter. Unit 15 beginnt mit der JiTT-Auswertung und schließt den Kurs ab.

## Gestaltung und Abbildungen

Die Präsentation verwendet die nativen Master, Noto Sans und Universitätsfarben aus [präs_ms02_powerpoint_de.pptx](../Vorlagen/präs_ms02_powerpoint_de.pptx). Das originale Foto-/Kartenmotiv der FB19-Vorlage erscheint auf Titel und Abschluss. Universitätslogos stehen nur dort; Foliennummern sind schlicht, Zeitangaben stehen nur in den Notizen.

Alle fünf fachlichen SVG-Abbildungen der aktuellen Unit 14 sind eingebettet: Datenart und Symbol, Farbpaletten, berechnete Klassengrenzen, visuelle Hierarchie und vollständiger Kartenworkflow. Hinzu kommen die zwei vorhandenen Klassifikationskarten und die fertige Beispielkarte aus dem Marburger Paket. Texte, Tabellen und ergänzende Schemata bestehen aus bearbeitbaren PowerPoint-Formen.

## Bearbeitung und Export

Der reproduzierbare Ausgangsstand steht in [build_slides.py](build_slides.py). Das Skript benötigt LibreOffice mit Python-UNO-Anbindung, beide Originalvorlagen und die Zeichenhilfen aus dem benachbarten Unit-10-Builder. Es erzeugt PowerPoint, PDF, Moderationsdatei und die veröffentlichte PDF-Kopie unter `docs/assets/pdfs/Geodaten_Slides_Unit14.pdf` neu.

Aus dem Verzeichnis `docs/` ausführen:

```bash
/usr/bin/python3 slides/unit14/build_slides.py
```

Vorhandene Ausgaben werden überschrieben. Die exportierte PowerPoint wird erneut geöffnet und daraus die PDF erzeugt, damit beide sichtbaren Fassungen übereinstimmen. Direkte Änderungen an der PowerPoint entweder im Skript nachführen oder beide PDF-Fassungen anschließend erneut exportieren beziehungsweise kopieren. Eine Prüfung in Microsoft PowerPoint selbst erfolgte nicht.

## Quellenstand

Grundlage sind die aktuellen sechs Unit-14-Seiten, die QGIS-Kurzcheckliste und das Marburger Übungspaket vom 08.09.2026. Kontrollwerte, Klassengrenzen und Exportvorgaben stammen aus den vorhandenen Kursseiten und geprüften Kartenexporten. Die Folien verlinken das QGIS-3.40-Benutzerhandbuch sowie die Datenquellen. Der Abgleich der Folien erfolgte am 10.09.2026. Die Live-Erreichbarkeit externer Seiten ist keine Voraussetzung für die Sitzung.
