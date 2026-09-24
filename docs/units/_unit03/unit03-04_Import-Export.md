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

Nutzen Sie einen kleinen Ausschnitt (10–15 Zeilen) aus Ihrem Blatt `Datensatz_1`.

1. Speichern Sie die Tabelle über **Datei → Speichern unter** als **Textdatei (Tabstopp-getrennt)** (`.txt`) mit dem Dateinamen `IhrName_export_Datum_Version.txt` (z. B. `Mueller_export_20250316_v1.txt`).
2. Speichern Sie dieselbe Tabelle zusätzlich als **CSV (Comma Separated Values)** (`.csv`) mit dem Dateinamen `IhrName_export_Datum_Version.csv`.
3. Öffnen Sie Ihren Datei-Explorer (Windows) bzw. Finder (Mac) und vergleichen Sie die **Dateigröße** beider Dateien sowie der ursprünglichen `.xlsx`-Datei. Notieren Sie sich die Größenunterschiede.
4. Öffnen Sie **beide** Dateien (`.txt` und `.csv`) mit einem einfachen **Texteditor** (z. B. Editor/Notepad unter Windows, TextEdit im „Nur-Text"-Modus unter Mac) – **nicht** mit Excel. Vergleichen Sie, wie die Spalten jeweils getrennt sind, und woran Sie das im reinen Text erkennen (Tabstopp ist im Texteditor meist als größere Lücke sichtbar, Komma/Semikolon als sichtbares Zeichen).

<!-- **Screenshot 12:** Nebeneinander geöffnetes Fenster des Datei-Explorers mit den drei Dateien (`.xlsx`, `.txt`, `.csv`) und sichtbarer Größenangabe in einer Spalte, sowie ein Texteditor-Fenster, das den Inhalt der `.csv`-Datei mit sichtbaren Kommas/Semikolons zwischen den Werten zeigt.
Markdownlösung: ![Screenshot einer CSV-Tabelle mit Semikolon als Trennzeichen und Dateigrößen zum Vergleich.]({{ '/assets/images/unit03/Screenshot12_Excel.png' | relative_url }})
Oder als HTML (lightbox) mit Vergrößerungsoption, Beschreibungstext beim Hovern und Galerie zum durchklicken:-->

<a href="{{ '/assets/images/unit03/Screenshot12_Excel.png' | relative_url }}" 
   data-lightbox="Screenshot12_Excel" 
   title="Screenshot einer CSV-Tabelle mit Semikolon als Trennzeichen und Dateigrößen zum Vergleich.">
  <img src="{{ '/assets/images/unit03/Screenshot12_Excel.png' | relative_url }}" alt="Screenshot einer CSV-Tabelle mit Semikolon als Trennzeichen und Dateigrößen zum Vergleich.">
</a>

**Reflexionsfrage:** Warum ist die `.xlsx`-Datei vermutlich die größte der drei Dateien, obwohl sie dieselben Daten enthält?

## Themenüberschrift 02: Import einer Textdatei in Excel

Wenn Sie umgekehrt eine `.txt`- oder `.csv`-Datei erhalten und in Excel öffnen möchten, sollten Sie **nicht** per Doppelklick öffnen, sondern über **Daten → Aus Text/CSV** –  so erhalten Sie Zugriff auf den Import-Assistenten, der Ihnen die Kontrolle über Kodierung, Trennzeichen und Datentyp gibt. Der Assistent führt Sie durch drei Schritte:

### Schritt 1: Dateiursprung (Zeichenkodierung) und Struktur

Excel zeigt zunächst eine Vorschau der Datei und schlägt eine Zeichenkodierung vor (meist „Windows" oder „UTF-8"). Genau hier setzt das Encoding-Problem aus einem früheren Kapitel an: Wird die falsche Kodierung gewählt, erscheinen Umlaute bereits in dieser Vorschau verstümmelt (`Cölbe` → `CÃ¶lbe`). **Prüfen Sie die Vorschau sorgfältig, bevor Sie fortfahren** – ein falsch gewähltes Encoding lässt sich zwar später korrigieren, aber deutlich umständlicher, als es hier gleich richtig einzustellen.

<!-- Screetshot 13: Erster Schritt des Text-Import-Assistenten mit Dropdown-Menü „Dateiursprung", in dem „UTF-8" ausgewählt ist, und einer Datenvorschau darunter, in der ein Standort mit Umlaut korrekt angezeigt wird (Vergleich: falsch gewählte Kodierung mit verstümmelter Vorschau daneben).
Markdownlösung: ![Screenshot des Text-Import-Assistenten mit unterschiedlichen Dateiursprüngen und Darstellungen der Daten.]({{ '/assets/images/unit03/Screenshot13_Excel.png' | relative_url }})
Oder als HTML (lightbox) mit Vergrößerungsoption, Beschreibungstext beim Hovern und Galerie zum durchklicken:-->

<a href="{{ '/assets/images/unit03/Screenshot13_Excel.png' | relative_url }}" 
   data-lightbox="Screenshot13_Excel" 
   title="Screenshot des Text-Import-Assistenten mit unterschiedlichen Dateiursprüngen und Darstellungen der Daten.">
  <img src="{{ '/assets/images/unit03/Screenshot13_Excel.png' | relative_url }}" alt="Screenshot des Text-Import-Assistenten mit unterschiedlichen Dateiursprüngen und Darstellungen der Daten.">
</a>

### Schritt 2: Trennzeichen festlegen

Hier geben Sie an, welches Zeichen die Spalten in der Datei voneinander trennt – üblicherweise Tabstopp, Komma oder Semikolon. Excel zeigt bereits eine Vorschau, wie die Datei mit dem gewählten Trennzeichen in Spalten zerlegt würde. Ist das falsche Trennzeichen gewählt, landen mehrere eigentlich getrennte Werte in einer einzigen Spalte – ein direkter Verstoß gegen das Tidy-Data-Prinzip aus dem vorherigen Kapitel.

<!-- **Screenshot 14:** Zweiter Schritt des Assistenten mit Checkbox-Auswahl der Trennzeichen (Tab, Semikolon, Komma, Leerzeichen, Andere), darunter eine Vorschau mit bereits sichtbaren Spaltentrennlinien. 
Markdownlösung: ![Screenshot des Text-Import-Assistenten mit Checkbox-Auswahl der Trennzeichen.]({{ '/assets/images/unit03/Screenshot14_Excel.png' | relative_url }}) 
Oder als HTML (lightbox) mit Vergrößerungsoption, Beschreibungstext beim Hovern und Galerie zum durchklicken:-->

<a href="{{ '/assets/images/unit03/Screenshot14_Excel.png' | relative_url }}" 
   data-lightbox="Screenshot14_Excel" 
   title="Screenshot des Text-Import-Assistenten mit Checkbox-Auswahl der Trennzeichen.">
  <img src="{{ '/assets/images/unit03/Screenshot14_Excel.png' | relative_url }}" alt="Screenshot des Text-Import-Assistenten mit Checkbox-Auswahl der Trennzeichen.">
</a>

### Schritt 3: Datentyp je Spalte festlegen

Im letzten Schritt können Sie für **jede Spalte einzeln** festlegen, welchen Datentyp Excel beim Import verwenden soll: Standard, Text, Datum (mit wählbarem Datumsformat, z. B. `TMJ` oder `MTJ` – wichtig bei importierten Dateien aus dem englischsprachigen Raum!), oder die Spalte komplett überspringen.

**Das ist der entscheidende Schritt, um spätere Probleme zu vermeiden:** Legen Sie hier z. B. Ihre Spalte `Standort` explizit als **Text** fest (auch wenn sie nur Zahlen wie Postleitzahlen enthielte, die keine führenden Nullen verlieren sollen), und Ihre Spalte `Datum` mit dem passenden Format, falls die Quelldatei ein anderes Datumsformat verwendet als in Deutschland üblich (z. B. `MM/TT/JJJJ` bei einer aus den USA stammenden Datei). Ein nachträgliches Ändern des Datentyps nach dem Import ist – wie Sie bereits aus dem Kapitel zu Zellformaten wissen – deutlich fehleranfälliger, als ihn gleich beim Import korrekt festzulegen.

<!-- **Screenshot 15:** Dritter Schritt des Assistenten, eine Spalte ist markiert und im Dropdown „Spaltendatenformat" ist „Datum: MTJ" ausgewählt, sichtbar als Kopfzeile über der jeweiligen Spalte in der Vorschau.
Markdownlösung: ![Screenshot des Text-Import-Assistenten mit „Datum: MTJ" als Spaltendatenformat.]({{ '/assets/images/unit03/Screenshot15_Excel.png' | relative_url }}) 
Oder als HTML (lightbox) mit Vergrößerungsoption, Beschreibungstext beim Hovern und Galerie zum durchklicken:

<a href="{{ '/assets/images/unit03/Screenshot15_Excel.png' | relative_url }}" 
   data-lightbox="Screenshot15_Excel" 
   title="Screenshot des Text-Import-Assistenten mit *Datum: MTJ* als Spaltendatenformat.">
  <img src="{{ '/assets/images/unit03/Screenshot15_Excel.png' | relative_url }}" alt="Screenshot des Text-Import-Assistenten mit *Datum: MTJ* als Spaltendatenformat.">
</a>

-->
<!-- Notiz von Lisa S.: Ich habe kein Dropdownmenü mit "Spaltendatenformat" im Assistenten gefunden. Das letzte Dropdownmenü heißt bei mir "Datentyperkennung" und enthält die Auswahl "Basierend auf den ersten 200 Zeilen", "Basierend auf dem gesamten Datensatz", "Datentypen nicht ermitteln". -->

**Zusammenfassung des Imports in vier Punkten:**
1. Nicht per Doppelklick öffnen, sondern über „Daten → Aus Text/CSV"
2. Zeichenkodierung prüfen (Encoding-Probleme direkt hier vermeiden)
3. Richtiges Trennzeichen wählen (sonst Tidy-Data-Verstoß)
4. Datentyp pro Spalte gezielt festlegen, statt „Standard" für alles zu belassen

### Zusatz zu Schritt 3: Dezimaltrennzeichen explizit festlegen

Neben dem Datentyp je Spalte lohnt sich bei importierten Zahlenwerten ein zweiter Blick auf das **Dezimaltrennzeichen**. Deutsche Excel-Installationen erwarten standardmäßig das **Komma** (`8,4`), viele internationale Quellen – GPS-Geräte, R-Exporte, viele Web-APIs – liefern Zahlen dagegen mit **Punkt** (`8.4`). Wird das nicht korrigiert, liest Excel `23.65` im schlimmsten Fall als „2365" statt „23,65" – ohne Fehlermeldung.

**Weg 1 – Aktuelle Excel-Version (Microsoft 365, Power-Query-Import):**
1. Im Vorschaufenster **„Daten transformieren"** klicken (öffnet den Power-Query-Editor), nicht direkt „Laden"
2. Betroffene Spalte anklicken
3. Falls Power Query die Spalte bereits automatisch (und falsch) umgewandelt hat: Im Bereich „Angewendete Schritte" rechts den Schritt „Geänderter Typ" per X **löschen**, sodass die Spalte wieder als Text vorliegt
4. Rechtsklick auf die Spalte → **„Datentyp ändern" → „Unter Verwendung von Gebietsschema…"**
5. Gebietsschema **„Englisch (USA)"** wählen, Zieldatentyp „Dezimalzahl"

<!-- Screenshot 16: Power-Query-Editor, rechter Bereich "Angewendete Schritte" mit dem Schritt "Geänderter Typ" zum Löschen markiert, darunter das Dialogfenster "Datentyp ändern mit Gebietsschema" mit Auswahl "Englisch (USA)".
Markdownlösung: ![Screenshot des Power-Query-Editor mit Typ-Vorauswahl durch Excel, Dropdownmenü zur Typänderung und Dialogfenster zum einstellen des Gebietsschemas.]({{ '/assets/images/unit03/Screenshot16_Excel.png' | relative_url }}) 
Oder als HTML (lightbox) mit Vergrößerungsoption, Beschreibungstext beim Hovern und Galerie zum durchklicken: -->

<a href="{{ '/assets/images/unit03/Screenshot16_Excel.png' | relative_url }}" 
   data-lightbox="Screenshot16_Excel" 
   title="Screenshot des Power-Query-Editor mit Typ-Vorauswahl durch Excel, Dropdownmenü zur Typänderung und Dialogfenster zum einstellen des Gebietsschemas.">
  <img src="{{ '/assets/images/unit03/Screenshot16_Excel.png' | relative_url }}" alt="Screenshot des Power-Query-Editor mit Typ-Vorauswahl durch Excel, Dropdownmenü zur Typänderung und Dialogfenster zum einstellen des Gebietsschemas.">
</a>

**Weg 2 – Ältere Excel-Version (klassischer Text-Import-Assistent):**
Im letzten Schritt des Assistenten die Schaltfläche **„Erweitert…"** anklicken, dort **Dezimaltrennzeichen** (Punkt) und **1000er-Trennzeichen** direkt festlegen.

<!-- Screenshot 17: Dritter Schritt des klassischen Text-Import-Assistenten mit Schaltfläche "Erweitert…" und dem sich öffnenden Dialog "Erweiterte Texterkennungseinstellungen".
Markdownlösung: ![Screenshot des klassischen Text-Import-Assistenten mit der Schaltfläche "Erweitert" un dem zugehörigen Dialogfeld.]({{ '/assets/images/unit03/Screenshot17_Excel.png' | relative_url }}) 
Oder als HTML (lightbox) mit Vergrößerungsoption, Beschreibungstext beim Hovern und Galerie zum durchklicken:

<a href="{{ '/assets/images/unit03/Screenshot17_Excel.png' | relative_url }}" 
   data-lightbox="Screenshot17_Excel" 
   title="Screenshot des klassischen Text-Import-Assistenten mit der Schaltfläche *Erweitert* un dem zugehörigen Dialogfeld.">
  <img src="{{ '/assets/images/unit03/Screenshot17_Excel.png' | relative_url }}" alt="Screenshot des klassischen Text-Import-Assistenten mit der Schaltfläche *Erweitert* un dem zugehörigen Dialogfeld.">
</a>
 -->

 <!-- Notiz von Lisa S.: Dazu muss ich erst eine ältere Exelversion finden. -->

> Welchen der beiden Wege Sie sehen, hängt von Ihrer Excel-Version und Konfiguration ab – prüfen Sie zuerst, welcher Dialog bei Ihnen erscheint (unter „Datei → Optionen → Daten" lässt sich der „Legacy-Datenimport-Assistent" bei Bedarf reaktivieren).

**Kontrolle nach dem Import:** Prüfen Sie mit `=MIN(...)`/`=MAX(...)`, ob die Werte plausibel sind (z. B. Temperaturwerte im einstelligen bis niedrigen zweistelligen Bereich, nicht im Tausenderbereich).

---

## Übung: Import einer fehlerhaften Sensordaten-Datei

Sie erhalten die Datei `Import_roh.csv` – einen Export aus dem Sensor-System, der **absichtlich mehrere typische Fehlerquellen** enthält: falsches Encoding, ein untypisches Trennzeichen und US-Datumsformat. Ihre Aufgabe: die Datei so importieren, dass am Ende Standortname, Zeitpunkt und Temperatur korrekt und rechenfähig in Excel vorliegen.

1. Importieren Sie die Datei über **Daten → Aus Text/CSV** (nicht per Doppelklick).
2. Prüfen Sie die Zeichenkodierung anhand der Stationsnamen mit Umlaut/ß (z. B. `Schloßpark`, `Neuhöfe`) – erscheinen diese verstümmelt, wechseln Sie die Kodierung.
3. Prüfen und korrigieren Sie das Trennzeichen.
4. Legen Sie die Datumsspalte mit dem passenden Format fest (US-Format `MM/DD/YYYY`).
5. Prüfen und korrigieren Sie ggf. das Dezimaltrennzeichen der Temperaturspalte (siehe oben).
6. Kontrollieren Sie Ihr Ergebnis mit `=MIN(...)`/`=MAX(...)` auf Plausibilität.
7. Speichern Sie das importierte Ergebnis als eigene `.xlsx`-Datei.