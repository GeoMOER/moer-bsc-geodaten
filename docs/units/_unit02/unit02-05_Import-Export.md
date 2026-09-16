---
title: Import und Export
published: true
toc: true
header:
  image: /assets/images/unit02/31031723265_0890cd9547_o.jpg
  image_description: "Cloudscape Over the Philippine Sea"
  caption: "Image: [NASA's Marshall Space Flight Center](https://www.nasa.gov/centers/marshall/home/index.html) [CC BY-NC 2.0] via [flickr.com](https://www.flickr.com/photos/nasamarshall/31031723265/)"
---


Bisher haben Sie ausschließlich innerhalb einer Excel-Datei (.xlsx) gearbeitet. In der Praxis werden Daten jedoch häufig als **Textdatei** ausgetauscht – etwa wenn Sie Messdaten von einem Sensor, einer Website oder einer anderen Software erhalten, die kein Excel-Format unterstützt. Textdateien sind das kleinste gemeinsame Format, das praktisch jede Software lesen kann – dafür müssen Sie beim Import selbst festlegen, wie die Datei strukturiert ist und welche Datentypen die einzelnen Spalten haben sollen. Genau das üben Sie in diesem Kapitel.

## Themenüberschrift 01: Textdatei vs. CSV-Datei

Beide Formate speichern reinen Text, unterscheiden sich aber in der Art, wie Spalten getrennt werden:

| Format | Dateiendung | Trennzeichen zwischen Spalten |
|---|---|---|
| Textdatei | `.txt` | meist Tabulator (Tab) |
| CSV (Comma Separated Values) | `.csv` | meist Komma `,` – in Deutschland oft auch Semikolon `;`, da das Komma bereits als Dezimaltrennzeichen verwendet wird |

Beide Dateien enthalten **keine Formatierung** (keine Schriftart, keine Zellfarben, keine Formeln) – nur die reinen Werte und das Trennzeichen. Das ist auch der Grund, warum solche Dateien in der Regel deutlich kleiner sind als eine vergleichbare `.xlsx`-Datei.

## Übung: Export einer Tabelle

Nutzen Sie eine die Beispieltabelle 

1. Speichern Sie die Tabelle über **Datei → Speichern unter** als **Textdatei (Tabstopp-getrennt)** (`.txt`) mit dem Dateinamen `IhrName_export_Datum_Version.txt` (z. B. `Mueller_export_20250316_v1.txt`).
2. Speichern Sie dieselbe Tabelle zusätzlich als **CSV (Comma Separated Values)** (`.csv`) mit dem Dateinamen `IhrName_export_Datum_Version.csv`.
3. Öffnen Sie Ihren Datei-Explorer (Windows) bzw. Finder (Mac) und vergleichen Sie die **Dateigröße** beider Dateien sowie der ursprünglichen `.xlsx`-Datei. Notieren Sie sich die Größenunterschiede.
4. Öffnen Sie **beide** Dateien (`.txt` und `.csv`) mit einem einfachen **Texteditor** (z. B. Editor/Notepad unter Windows, TextEdit im „Nur-Text"-Modus unter Mac) – **nicht** mit Excel. Vergleichen Sie, wie die Spalten jeweils getrennt sind, und woran Sie das im reinen Text erkennen (Tabstopp ist im Texteditor meist als größere Lücke sichtbar, Komma/Semikolon als sichtbares Zeichen).

<!-- **Screenshot 10:** Nebeneinander geöffnetes Fenster des Datei-Explorers mit den drei Dateien (`.xlsx`, `.txt`, `.csv`) und sichtbarer Größenangabe in einer Spalte, sowie ein Texteditor-Fenster, das den Inhalt der `.csv`-Datei mit sichtbaren Kommas/Semikolons zwischen den Werten zeigt. -->

**Reflexionsfrage:** Warum ist die `.xlsx`-Datei vermutlich die größte der drei Dateien, obwohl sie dieselben Daten enthält?

## Themenüberschrift 02: Import einer Textdatei in Excel

Wenn Sie umgekehrt eine `.txt`- oder `.csv`-Datei erhalten und in Excel öffnen möchten, sollten Sie **nicht** per Doppelklick öffnen, sondern über **Daten → Aus Text/CSV** –  so erhalten Sie Zugriff auf den Import-Assistenten, der Ihnen die Kontrolle über Kodierung, Trennzeichen und Datentyp gibt. Der Assistent führt Sie durch drei Schritte:

### Schritt 1: Dateiursprung (Zeichenkodierung) und Struktur

Excel zeigt zunächst eine Vorschau der Datei und schlägt eine Zeichenkodierung vor (meist „Windows" oder „UTF-8"). Genau hier setzt das Encoding-Problem aus einem früheren Kapitel an: Wird die falsche Kodierung gewählt, erscheinen Umlaute bereits in dieser Vorschau verstümmelt (`Cölbe` → `CÃ¶lbe`). **Prüfen Sie die Vorschau sorgfältig, bevor Sie fortfahren** – ein falsch gewähltes Encoding lässt sich zwar später korrigieren, aber deutlich umständlicher, als es hier gleich richtig einzustellen.

<!-- Screetshot Erster Schritt des Text-Import-Assistenten mit Dropdown-Menü „Dateiursprung", in dem „UTF-8" ausgewählt ist, und einer Datenvorschau darunter, in der ein Standortname mit Umlaut korrekt angezeigt wird (Vergleich: falsch gewählte Kodierung mit verstümmelter Vorschau daneben). -->

### Schritt 2: Trennzeichen festlegen

Hier geben Sie an, welches Zeichen die Spalten in der Datei voneinander trennt – üblicherweise Tabstopp, Komma oder Semikolon. Excel zeigt bereits eine Vorschau, wie die Datei mit dem gewählten Trennzeichen in Spalten zerlegt würde. Ist das falsche Trennzeichen gewählt, landen mehrere eigentlich getrennte Werte in einer einzigen Spalte – ein direkter Verstoß gegen das Tidy-Data-Prinzip aus dem vorherigen Kapitel.

<!-- **Screenshot 12:** Zweiter Schritt des Assistenten mit Checkbox-Auswahl der Trennzeichen (Tab, Semikolon, Komma, Leerzeichen, Andere), darunter eine Vorschau mit bereits sichtbaren Spaltentrennlinien. -->

### Schritt 3: Datentyp je Spalte festlegen

Im letzten Schritt können Sie für **jede Spalte einzeln** festlegen, welchen Datentyp Excel beim Import verwenden soll: Standard, Text, Datum (mit wählbarem Datumsformat, z. B. `TMJ` oder `MTJ` – wichtig bei importierten Dateien aus dem englischsprachigen Raum!), oder die Spalte komplett überspringen.

**Das ist der entscheidende Schritt, um spätere Probleme zu vermeiden:** Legen Sie hier z. B. Ihre Spalte `Standortname` explizit als **Text** fest (auch wenn sie nur Zahlen wie Postleitzahlen enthielte, die keine führenden Nullen verlieren sollen), und Ihre Spalte `Datum` mit dem passenden Format, falls die Quelldatei ein anderes Datumsformat verwendet als in Deutschland üblich (z. B. `MM/TT/JJJJ` bei einer aus den USA stammenden Datei). Ein nachträgliches Ändern des Datentyps nach dem Import ist – wie Sie bereits aus dem Kapitel zu Zellformaten wissen – deutlich fehleranfälliger, als ihn gleich beim Import korrekt festzulegen.

<!-- **Screenshot 13:** Dritter Schritt des Assistenten, eine Spalte ist markiert und im Dropdown „Spaltendatenformat" ist „Datum: MTJ" ausgewählt, sichtbar als Kopfzeile über der jeweiligen Spalte in der Vorschau. -->

**Zusammenfassung des Imports in vier Punkten:**
1. Nicht per Doppelklick öffnen, sondern über „Daten → Aus Text/CSV"
2. Zeichenkodierung prüfen (Encoding-Probleme direkt hier vermeiden)
3. Richtiges Trennzeichen wählen (sonst Tidy-Data-Verstoß)
4. Datentyp pro Spalte gezielt festlegen, statt „Standard" für alles zu belassen

