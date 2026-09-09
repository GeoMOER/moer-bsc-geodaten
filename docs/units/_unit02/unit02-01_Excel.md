---
title: Einführung Excel
published: true
toc: true
header:
  image: /assets/images/unit02/31031723265_0890cd9547_o.jpg
  image_description: "Cloudscape Over the Philippine Sea"
  caption: "Image: [NASA's Marshall Space Flight Center](https://www.nasa.gov/centers/marshall/home/index.html) [CC BY-NC 2.0] via [flickr.com](https://www.flickr.com/photos/nasamarshall/31031723265/)"
---

<!-- Themenblock 02-01: Einführung in Excel, Grundlagen -->
Nachdem wir uns mit Datentypen und -formaten befasst haben, geht es in diesem Kapitel um das Werkzeug, mit dem wir diese in der Praxis anwenden: Microsoft Excel. Bevor wir mit konkreten Formeln und Funktionen arbeiten, verschaffen wir uns zunächst einen Überblick über die Herkunft, die Oberfläche und die grundlegenden Möglichkeiten des Programms – als Grundlage für alle folgenden Übungen.

## Die Excel-Oberfläche
 
| Element | Beschreibung |
|---|---|
| **Menüband (Ribbon)** | Oben angeordnete Registerkarten (Start, Einfügen, Formeln, Daten, Überprüfen, Ansicht …), jede mit thematisch gruppierten Befehlen. |
| **Namensfeld** | Zeigt links oben die Adresse der aktuell markierten Zelle (z. B. `B3`) – kann auch genutzt werden, um direkt zu einer Zelle zu springen. |
| **Bearbeitungsleiste (Formelleiste)** | Zeigt den tatsächlichen Inhalt der aktiven Zelle (Formel statt Ergebnis) – wichtig, um zu prüfen, ob eine Zelle eine Formel oder einen festen Wert enthält. |
| **Tabellenblatt-Reiter** | Unten am Bildschirmrand, zum Wechseln zwischen mehreren Sheets einer Arbeitsmappe (wie in unserer Übungsdatei: Anleitung, Rohdaten, Bearbeitung …). |
| **Statusleiste** | Unten, zeigt bei markierten Zellbereichen automatisch Summe, Mittelwert und Anzahl an – praktisch für einen schnellen Check ohne extra Formel. |
| **Schnellzugriffsleiste** | Oben links, frei anpassbar mit häufig genutzten Befehlen (z. B. Speichern, Rückgängig). |

## Überblick über Excels Möglichkeiten
 
Ein kurzer Ausblick, was Excel neben den Grundfunktionen alles kann – Details dazu folgen in späteren Einheiten:
 
- **Formeln & Funktionen**: mathematisch (`SUMME`, `MITTELWERT`), logisch (`WENN`), Text (`TEIL`, `GLÄTTEN`, `ERSETZEN`), sowie Nachschlage-Funktionen (`SVERWEIS`, `INDEX`+`VERGLEICH`).
- **PivotTables**: fassen große Datensätze interaktiv per Drag-and-Drop zusammen, ganz ohne eigene Formel.
- **Diagramme**: visuelle Darstellung von Zahlenreihen (Balken, Linien, Streudiagramme).
- **Bedingte Formatierung**: färbt Zellen automatisch abhängig vom Wert – nützlich, um Auffälligkeiten auf einen Blick zu erkennen.
- **Datenvalidierung**: schränkt erlaubte Zelleingaben ein und verhindert so Fehler direkt an der Quelle.
- **Power Query**: importiert und bereinigt Daten aus externen Quellen automatisiert – im Grunde eine grafische Oberfläche für Datenbereinigung.
- **Makros/VBA**: automatisiert wiederkehrende Arbeitsschritte per Code.
- **Solver/Zielwertsuche**: sucht automatisch den Eingabewert, der zu einem gewünschten Ergebnis führt.
## Nützliche Shortcuts
 
| Shortcut | Funktion |
|---|---|
| `Strg` + `C` / `V` / `X` | Kopieren / Einfügen / Ausschneiden |
| `Strg` + `Z` / `Y` | Rückgängig / Wiederholen |
| `Strg` + `S` | Speichern |
| `F2` | Aktive Zelle bearbeiten |
| `F4` | Beim Bearbeiten einer Formel: zwischen relativem und absolutem Zellbezug wechseln (`A1` → `$A$1` → `A$1` → `$A1`) |
| `Alt` + `=` | AutoSumme für markierten Bereich einfügen |
| `Strg` + `Pfeiltaste` | Zum Rand des zusammenhängenden Datenbereichs springen |
| `Strg` + `Shift` + `Pfeiltaste` | Bereich bis zum Rand der Daten markieren |
| `Strg` + `Pos1` | Zur Zelle A1 springen |
| `Strg` + `Ende` | Zur letzten benutzten Zelle springen |
| `Strg` + `1` | Dialog „Zellen formatieren" öffnen |
| `Strg` + `Shift` + `L` | Autofilter ein-/ausschalten |
| `Strg` + `;` | Aktuelles Datum einfügen |
| `F9` | Arbeitsmappe neu berechnen |
 
Besonders **F4** lohnt sich früh einzuprägen, da absolute und relative Zellbezüge eines der zentralen Lernziele dieser Einheit sind.



