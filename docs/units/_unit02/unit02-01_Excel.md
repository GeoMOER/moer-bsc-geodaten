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
 Bevor wir mit konkreten Datentypen und -formaten arbeiten, verschaffen wir uns zunächst einen Überblick über das Werkzeug, mit dem wir diese in diesem Kurs anwenden: Microsoft Excel. Wir lernen die Oberfläche und die grundlegenden Möglichkeiten des Programms kennen – als Grundlage für alle folgenden Übungen.

> Hinweis: je nach späterem Verlauf Ihres Studiums werden Sie mit anderen Programmen für die Bearbeitung von Daten arbeiten, beispielsweise R. Excel eignet sich jedoch hervorragend, um sich als Einsteiger:in mit grundlegenden Konzepten der Datenverarbeitung vertraut zu machen, da die Ergebnisse jeder Eingabe sofort sichtbar sind und man ohne Programmierkenntnisse direkt loslegen kann. 

## Die Excel-Oberfläche
 
| Element | Beschreibung |
|---|---|
| **Menüband (Ribbon)** | Oben angeordnete Registerkarten (Start, Einfügen, Formeln, Daten, Überprüfen, Ansicht …), jede mit thematisch gruppierten Befehlen. |
| **Namensfeld** | Zeigt links oben die Adresse der aktuell markierten Zelle (z. B. `B3`) – kann auch genutzt werden, um direkt zu einer Zelle zu springen. |
| **Bearbeitungsleiste (Formelleiste)** | Zeigt den tatsächlichen Inhalt der aktiven Zelle (Formel statt Ergebnis) – wichtig, um zu prüfen, ob eine Zelle eine Formel oder einen festen Wert enthält. |
| **Tabellenblatt-Reiter** | Unten am Bildschirmrand, zum Wechseln zwischen mehreren Sheets einer Arbeitsmappe (wie in unserer Übungsdatei: Anleitung, Rohdaten, Bearbeitung …). |
| **Statusleiste** | Unten, zeigt bei markierten Zellbereichen automatisch Summe, Mittelwert und Anzahl an – praktisch für einen schnellen Check ohne extra Formel. |
| **Schnellzugriffsleiste** | Oben links, frei anpassbar mit häufig genutzten Befehlen (z. B. Speichern, Rückgängig). |



## Grundlegende Bearbeitung in Excel


> Aufgabe (7 min)
* Öffnen Sie MS Excel
* Geben Sie die Daten, die Sie als Hausaufgabe messen sollten, in die Tabelle ein. Erwartete Werte: Standortname, Latuitude, Longitude, Datum, Uhrzeit, Temperatur (°C), Messmethode (Bsp. Thermometer, Wetter App)

Nachdem Sie sich einen ersten Überblick über die Excel-Oberfläche verschafft haben, lernen wir nun die grundlegenden Techniken kennen, mit denen Sie in Excel Daten bearbeiten, verschieben und organisieren.

### Zellen markieren

Bevor Sie eine Zelle bearbeiten, formatieren oder kopieren können, müssen Sie sie **markieren** (auswählen). Das geht auf mehrere Arten:

* **Einzelne Zelle:** einmal anklicken
* **Zellbereich:** Klicken und bei gedrückter Maustaste über die gewünschten Zellen ziehen
* **Ganze Zeile/Spalte:** auf die Zeilennummer bzw. den Spaltenbuchstaben klicken
* **Mehrere, nicht zusammenhängende Zellen:** erste Auswahl treffen, dann weitere Zellen bei gedrückter `Strg`-Taste anklicken

<!-- **Screenshot 1:** Excel-Tabellenblatt mit markiertem Zellbereich (z. B. B2:D5), die Markierung ist farblich hervorgehoben, Zeilennummern und Spaltenbuchstaben der markierten Bereiche sind ebenfalls hervorgehoben zu sehen.-->

### Bewegung auf dem Tabellenblatt

Um sich effizient zwischen Zellen zu bewegen, eignen sich folgende Tastenkombinationen:

| Aktion | Shortcut |
|---|---|
| Eine Zelle in Pfeilrichtung | Pfeiltasten |
| Zum Ende eines zusammenhängenden Datenbereichs | `Strg` + Pfeiltaste |
| Zum Anfang des Tabellenblatts (Zelle A1) | `Strg` + `Pos1` |
| Zur letzten benutzten Zelle des Tabellenblatts | `Strg` + `Ende` |
| Eine Zelle nach rechts (nach Eingabe) | `Tab` |
| Eine Zelle nach unten (nach Eingabe) | `Enter` |

Besonders `Strg` + `Ende` ist praktisch, um zu überprüfen, wie weit Ihre Tabelle tatsächlich reicht – auch wenn dort scheinbar keine Daten mehr stehen (z. B. nach dem Löschen von Spalten).

### Spaltenbreite anpassen

Wenn eine Spalte zu schmal ist, um den Inhalt anzuzeigen (Sie sehen dann z. B. `###` oder abgeschnittenen Text), können Sie die Breite ändern:

* Mit der Maus auf die Trennlinie zwischen zwei Spaltenköpfen gehen, bis sich der Cursor in einen Doppelpfeil verwandelt, dann klicken und ziehen
* Doppelklick auf die Trennlinie passt die Breite automatisch an den Inhalt an

<!-- **Screenshot 2:** Nahaufnahme der Spaltenköpfe (z. B. C und D), Mauszeiger als Doppelpfeil auf der Trennlinie positioniert, evtl. Vorher/Nachher-Vergleich einer zu schmalen Spalte mit `###`. -->

### Drag & Drop

Markierte Zellen lassen sich mit der Maus verschieben:

* Zellbereich markieren
* Mit der Maus auf den **Rand** der Markierung gehen (Cursor wird zum Verschiebe-Symbol, meist ein Kreuz mit Pfeilen)
* Klicken, halten und an die gewünschte Stelle ziehen

Achtung: Zellen an der Zielposition werden dabei überschrieben, falls dort bereits Werte stehen.

<!-- **Screenshot 3:** Markierter Zellbereich mit sichtbarem Verschiebe-Cursor am Rand der Markierung, gestrichelter Rahmen zeigt die Zielposition beim Ziehen an.
-->

### Kopieren und Einfügen über das Kontextmenü

Statt der Tastenkombinationen können Sie auch die rechte Maustaste nutzen:

1. Zelle(n) markieren
2. Rechtsklick → **Kopieren** (oder **Ausschneiden**, wenn die Zelle verschoben statt kopiert werden soll)
3. Zielzelle anklicken
4. Rechtsklick → **Einfügen**

<!-- **Screenshot 4:** Geöffnetes Kontextmenü nach Rechtsklick auf eine markierte Zelle, mit sichtbaren Optionen „Ausschneiden“, „Kopieren“ und „Einfügeoptionen“.
-->

### Vorsicht: Einzelne Zellen statt ganzer Zeilen einfügen

Wenn Sie über das Kontextmenü (Rechtsklick → „Zellen einfügen“) eine neue Zelle einfügen, fragt Excel, wie die anderen Zellen verschoben werden sollen – **nach unten** oder **nach rechts**. Das betrifft aber nur die Spalte bzw. Zeile, in der Sie geklickt haben, nicht die gesamte Zeile oder Tabelle!

Das kann dazu führen, dass Ihre Daten **nicht mehr zusammenpassen**: Eine Zelle in Spalte C rutscht z. B. eine Zeile nach unten, während die dazugehörigen Werte in Spalte B, D und E an ihrer ursprünglichen Position bleiben. Ihre Datensätze sind dann nicht mehr korrekt zugeordnet, ohne dass Sie das auf den ersten Blick sehen.

<!-- **Screenshot 5:** Dialogfenster „Zellen einfügen“ mit den Optionen „Zellen nach unten verschieben“ / „Zellen nach rechts verschieben“, idealerweise mit einem Beispiel-Tabellenausschnitt im Hintergrund, in dem eine Zeile durch fehlerhaftes Einfügen bereits verrutscht ist. -->

**Wenn Sie eine ganze Datenzeile einfügen möchten**, markieren Sie stattdessen die komplette Zeile (Klick auf die Zeilennummer) und wählen dann „Zeilen einfügen“ – so bleiben alle Spalten synchron.

**Merksatz:** Einzelne Zelle einfügen → nur diese eine Spalte verschiebt sich → Gefahr von Datenverrutschern. Ganze Zeile einfügen → alle Spalten bleiben synchron.

### Wichtige Shortcuts im Überblick

| Aktion | Shortcut |
|---|---|
| Kopieren | `Strg` + `C` |
| Ausschneiden (zum Verschieben) | `Strg` + `X` |
| Einfügen | `Strg` + `V` |
| Rückgängig machen | `Strg` + `Z` |
| Wiederholen | `Strg` + `Y` |
| Speichern | `Strg` + `S` |

**Tipp:** Wenn Sie unsicher sind, ob eine Aktion die gewünschte war, probieren Sie sie einfach aus – mit `Strg` + `Z` können Sie fast jede Aktion rückgängig machen.

---

> Übung: Klimadaten organisieren (15 min)

Sie haben bereits Ihre eigenen Klimadaten (Standortname, Latitude, Longitude, Datum, Uhrzeit, Temperatur, Messmethode) in eine Excel-Tabelle eingetragen. Um mit einer größeren Datenmenge üben zu können, erhalten Sie zusätzlich ein zweites Tabellenblatt mit Messdaten von Kommiliton:innen.

**Wichtig:** Die Spalten auf dem zweiten Blatt sind nicht unbedingt identisch benannt oder gleich angeordnet wie auf Ihrem eigenen Blatt. Überlegen Sie sich selbst, wie Sie die Daten sinnvoll und einheitlich strukturieren wollen, bevor Sie sie zusammenführen.

1. Öffnen Sie Ihre bestehende Excel-Datei mit den eigenen Messdaten.
2. Fügen Sie ein neues Tabellenblatt hinzu und kopieren Sie die bereitgestellten zusätzlichen Messdaten hinein (Rechtsklick auf ein Tabellenblatt → „Verschieben oder kopieren“, oder Daten direkt kopieren/einfügen).
3. Formatieren Sie auf beiden Blättern die Überschriften der Spalten erkennbar (z. B. fett), sodass klar ist, wo die Tabelle beginnt.
4. Prüfen Sie mit `Strg` + `Ende`, wie weit die Tabelle auf dem zweiten Blatt tatsächlich reicht.
5. Vergleichen Sie die Spaltennamen und -reihenfolge beider Blätter. Passen Sie die Spaltenüberschriften des zweiten Blatts so an, dass sie zu Ihrer eigenen Struktur passen (z. B. „Ort“ → „Standortname“).
6. Duplizieren Sie auf Ihrem eigenen Blatt die Spalte „Messmethode“ (kopieren und einfügen als neue Spalte).
7. Löschen Sie die soeben duplizierte Spalte wieder und speichern Sie die Datei. Prüfen Sie erneut mit `Strg` + `Ende`, ob sich die Größe der Tabelle verändert hat.
8. Fügen Sie ganz links eine neue Spalte ein und benennen Sie sie „ID“. Vergeben Sie fortlaufende Nummern für Ihre Messungen.
9. Verschieben Sie testweise eine einzelne Zeile per Drag & Drop an eine andere Position im Tabellenblatt – und machen Sie diese Änderung anschließend mit `Strg` + `Z` wieder rückgängig.
10. Speichern Sie Ihre Datei abschließend.


<!--


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

-->

