# Unit 15 – Folien für die Abschlusssitzung

Die Präsentation begleitet die gemeinsame 90-Minuten-Sitzung für Bachelor- und Lehramtsstudierende. Sie enthält 27 Folien: eine Titelfolie, 24 zeitlich geplante Folien, eine Reservefolie und eine Schlussfolie. Die Zeitfenster stehen in den PowerPoint-Notizen und in [moderation.md](moderation.md), nicht auf den projizierten Folien.

- [PowerPoint bearbeiten und präsentieren](unit15_praesenz.pptx)
- [PDF der Folien](unit15_praesenz.pdf)
- [Moderationshinweise lesen](moderation.md)

## Vor dem Termin

1. Folie 02 vollständig durch zwei bis drei tatsächliche, aggregierte JiTT-Ergebnisse zu Unit 14 ersetzen. Zehn Minuten für den ganzen Block einhalten. Keine Namen oder individuellen Noten zeigen.
2. Auf den Folien 03–10 die sichtbaren Beispiel-Platzhalter nur durch tatsächlich behandelte Beispiele aus Units 01–08 ersetzen. Diese Units sind noch in Ausarbeitung. Falls bis zum Termin kein belastbares Beispiel vorliegt, die betreffende Station knapp als Erinnerung moderieren und den Platzhalter nicht als fertiges Lehrmaterial ausgeben.
3. Den freiwilligen Papierfragebogen ohne Namensfeld gemäß der [Feedbackseite](../../units/_unit15/unit15-05_assignment.md) ausdrucken und eine Sammelbox bereitstellen. Organisatorische Termine nur nach Bestätigung nennen.
4. Präsentation und PDF nach jeder sichtbaren Änderung erneut synchronisieren; Beamer-Lesbarkeit am tatsächlichen Gerät prüfen.

## Ablauf

| Minuten | Folien | Inhalt |
|---|---|---|
| 0–10 | 02 | JiTT-Auswertung zu Unit 14 |
| 10–26 | 03–10 | Knappe Erinnerungsstationen zu Units 01–08; Beispiele noch einzusetzen |
| 26–40 | 11–17 | Schwerpunkt Units 09–14 und Verbindung zur Abschlusskarte |
| 40–60 | 18–20 | Persönliche Rückschau, Partnerfrage, häufige Fragen |
| 60–75 | 21–22 | Freiwilliger anonymer Papierfragebogen und Plenum |
| 75–90 | 23–25 | Drei Kernbotschaften und Kursabschluss |

Folie 26 ist Reserve; Folie 27 schließt die Sitzung ohne zusätzlichen Zeitblock. Im 30-Minuten-Rückblick sind höchstens zwei bis drei kurze Rückfragen vorgesehen. Die sechs GIS-Stationen verwenden vorhandene Kursabbildungen und die geprüften Kontrollwerte 79/56, 10/4/106 und 56/35/21. Unit 15 führt keine neuen Inhalte und keine neue Übungsaufgabe ein.

## Gestaltung und Quellen

Die Folien verwenden die nativen Master, Noto Sans und Universitätsfarben aus [präs_ms02_powerpoint_de.pptx](../Vorlagen/präs_ms02_powerpoint_de.pptx). Das FB19-Foto-/Kartenmotiv erscheint nur auf Titel und Schlussfolie. Die GIS-Grafiken stammen aus den aktuellen Units 09–13; die Abschlusskarte aus dem Marburger Übungspaket. Die verlinkte Reservefolie führt zur Unit-15-Rückblicksseite und zu Units 09–14. Texte und Kartenkommentare sind bearbeitbare PowerPoint-Objekte; eingebettete SVGs und die Beispielkarte bleiben Bildobjekte.

## Erzeugen und bearbeiten

Das Skript [build_slides.py](build_slides.py) benötigt LibreOffice mit Python-UNO-Anbindung, die beiden Originalvorlagen und die Zeichenhilfen aus dem Unit-10-Builder. Im Verzeichnis `docs/` ausführen:

```bash
/usr/bin/python3 slides/unit15/build_slides.py
```

Das Skript erzeugt PowerPoint, PDF, Moderationsdatei und die veröffentlichte PDF-Kopie `docs/assets/pdfs/Geodaten_Slides_Unit15.pdf` neu. Vorhandene Ausgaben werden überschrieben. Die exportierte PowerPoint wird vor dem PDF-Export erneut geöffnet, damit beide Fassungen denselben Stand zeigen. Direkte Änderungen an der PowerPoint im Skript nachführen oder anschließend beide PDF-Fassungen neu exportieren und kopieren. Eine Prüfung in Microsoft PowerPoint selbst ist noch offen.

`docs/slides/` und die veröffentlichte PDF unter `docs/assets/pdfs/` sind im aktuellen Repository versionierbar. Bei einem Gerätewechsel beide Stände gemeinsam übertragen.
