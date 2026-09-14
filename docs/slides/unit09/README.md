# Unit 09 – Folien für die Präsenzsitzung

Für einen Termin von 90 Minuten mit etwa 100–150 Studierenden aus Bachelor und Lehramt. Die Erklärungen setzen keine Vorbereitung voraus. Format: 16:9, helle Folien und große Schrift für den Beamer.

- [PowerPoint bearbeiten und präsentieren](unit09_praesenz.pptx)
- [PDF der Folien](unit09_praesenz.pdf)
- [Moderationshinweise lesen](moderation.md)

Die Präsentation enthält 31 Folien: eine Titelfolie, 27 Hauptfolien, zwei Reserve-/Quellenfolien und als letzte Folie „Vielen Dank für eure Aufmerksamkeit“. Die PowerPoint-Notizen enthalten Zeitfenster, Durchführungshinweise, erwartete Antworten und Quellen. Auf den Folien stehen keine Zeitangaben in der Fußzeile. Die PDF enthält dieselben sichtbaren Folien einschließlich der Auflösungen und Reservefolien, aber keine Moderationsnotizen. Aufgaben und Auflösungen stehen auf getrennten Folien; Animationen sind nicht erforderlich.

Vor dem Termin auf Folie 2 den gesamten JiTT-Platzhalter durch die aktuelle Auswertung zur vorherigen Sitzung ersetzen. Der Block enthält bewusst keine vorgegebenen Fragen oder Ergebnisse und kann durch Duplizieren erweitert werden. Die ersten zehn Minuten sind für JiTT vorgesehen. Weitere organisatorische Angaben kommen aus der aktuellen Kursorganisation; die Folien legen keine neuen Leistungs- oder Abgaberegeln fest.

| Minuten | Schwerpunkt |
|---|---|
| 0–10 | JiTT zur vorherigen Sitzung |
| 10–20 | Einstieg und Raumbezug |
| 20–35 | Breite, Länge, Einheit und Reihenfolge erklären |
| 35–45 | Fünf Koordinatenpaare gemeinsam prüfen |
| 45–60 | CRS-Grundidee und Projektionsvergleich |
| 60–75 | EPSG-Codes und CRS-Auswahl |
| 75–85 | Zuweisen und Transformieren |
| 85–90 | Ein Exit-Ticket gemeinsam beantworten und auf JiTT hinweisen |

Kurze Einzeldenkphasen, Nachbarschaftsgespräche und Handzeichen ermöglichen die Beteiligung im großen Hörsaal. Alle Studierenden erhalten dieselben Aufgaben und dieselbe Ansprache. Die beiden Reserve-/Quellenfolien 29–30 sind nicht zusätzlich in die 90 Minuten eingeplant; nach der Nachbereitung auf Folie 28 bei Bedarf direkt zur Abschlussfolie 31 wechseln.

Die einzige Übungsaufgabe zu Unit 09 ist die Beantwortung der JiTT-Fragen im ILIAS-Kurs. Folie 28 verweist darauf; die Fragen und die Bearbeitungsfrist stehen in ILIAS. Der konkrete ILIAS-Link muss auf der verlinkten Kursseite noch ergänzt werden.

## Bearbeitung und Export

Die Gestaltung und die nativen Folienmaster stammen aus [präs_ms02_powerpoint_de.pptx](../Vorlagen/präs_ms02_powerpoint_de.pptx): Noto Sans, Marburger Farben sowie Titel-, Inhalts- und Abschlusslayout. Das Foto-/Kartenmotiv auf der Titel- und Abschlussfolie wurde unverändert und mit seinem ursprünglichen Seitenverhältnis aus der Titelseite von [fb19-praesentationsvorlage_16-9-format.pot](../Vorlagen/fb19-praesentationsvorlage_16-9-format.pot) übernommen. Das Universitätslogo erscheint nur auf Titel und Abschluss. Foliennummern stehen ohne Umrandung in der Fußzeile. Die Originalvorlagen bleiben unverändert.

Texte und Tabellen bestehen aus bearbeitbaren PowerPoint-Formen. Passende Abbildungen der aktuellen Unit-9-Seiten sind als Vektorgrafiken eingebettet: Raumbezug, Gradnetz, Achsenreihenfolge, CRS-Vergleich, Projektionsvergleich sowie Zuweisen/Transformieren. Die vorhandene Kursillustration auf Folie 3 und das Foto-/Kartenmotiv auf Titel und Abschluss sind Rasterbilder. Der Projektionsvergleich zeigt berechnete Abbildungen gleich großer geodätischer Referenzflächen, keine realen Länderflächen.

Die Dateien wurden mit LibreOffice erstellt. Für die PDF wurde die exportierte PowerPoint erneut geöffnet und gerendert. Nach manuellen Änderungen in PowerPoint oder LibreOffice die PDF erneut exportieren, damit beide Fassungen zusammenpassen. Eine Prüfung in Microsoft PowerPoint selbst erfolgte nicht.

Der reproduzierbare Ausgangsstand steht in [build_slides.py](build_slides.py). Voraussetzungen: LibreOffice und dessen Python-UNO-Anbindung, hier über `/usr/bin/python3` verfügbar.

```bash
/usr/bin/python3 slides/unit09/build_slides.py
```

Das Skript benötigt beide Originalvorlagen, übernimmt das Foto-/Kartenmotiv unter `assets/fb19-marburg-europa.png` und erzeugt PowerPoint, PDF und Moderationsdatei neu. Vorhandene Ausgaben werden überschrieben. Direkte Änderungen an der PowerPoint werden dabei nicht übernommen; solche Änderungen entweder dort behalten oder in das Skript übertragen.

## Quellen

Grundlage sind die aktuellen fünf Kursseiten unter `units/_unit09/`. Die externen Quellen sind auf Folie 30 sowie in den Notizen verlinkt:

- [PROJ: Achsenreihenfolge](https://proj.org/en/stable/faq.html)
- [PROJ: WGS 84 und UTM](https://proj.org/en/stable/usage/quickstart.html)
- [PROJ: Mercator](https://proj.org/en/stable/operations/projections/merc.html)
- [PROJ: flächentreue Zylinderprojektion](https://proj.org/en/stable/operations/projections/cea.html)
- [PROJ: Web Mercator](https://proj.org/en/stable/operations/projections/webmerc.html)

Die externen Quellen wurden am 07.09.2026 geprüft; der Abgleich mit den aktuellen Unit-9-Seiten und Abbildungen erfolgte am 09.09.2026. Die Kursillustration auf der Orientierungsfolie ist die vorhandene KI-generierte Illustration `assets/images/unit09/hero-unit09.jpg`.
