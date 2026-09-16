---
title: Daten bereinigen
published: true
header:
  image: /assets/images/unit05/notebook.jpg
  caption: "Image: [Neil Conway](https://www.flickr.com/photos/neilconway/) [(Public Domain Mark 1.0)](https://creativecommons.org/publicdomain/mark/1.0/deed.en) via [flickr.com](https://www.flickr.com/photos/neilconway/5625707813/in/photostream/)"
---

<!-- Themenblock 02-07: Datenbereinigung -->

Sie haben in den letzten Kapiteln gelernt, wie Sie Daten korrekt formatieren, filtern und sortieren. Doch bevor eine Tabelle überhaupt zuverlässig ausgewertet werden kann, muss sie **bereinigt** sein – gerade wenn Daten aus mehreren Quellen zusammengeführt wurden (wie Ihre eigenen Klimadaten mit denen Ihrer Kommiliton:innen), schleichen sich fast zwangsläufig Inkonsistenzen ein: doppelte Einträge, uneinheitliche Schreibweisen, überflüssige Leerzeichen. Diese Fehler sind besonders tückisch, weil sie auf den ersten Blick oft **nicht auffallen** – die Tabelle sieht vollständig und plausibel aus, liefert aber bei Auswertungen falsche Ergebnisse.

## Themenüberschrift 01: Doppelte Einträge

Wenn Sie Daten mehrerer Personen zusammenführen, kann derselbe Datensatz versehentlich mehrfach in der Tabelle landen – z. B. weil eine Messung sowohl in Ihrer eigenen Tabelle als auch in der eines Kommilitonen erfasst wurde, oder weil beim Kopieren ein Bereich doppelt eingefügt wurde.

**Duplikate über die eingebaute Funktion entfernen:**
1. Klicken Sie in eine Zelle innerhalb Ihrer Datentabelle
2. Menüband: **Daten → Duplikate entfernen**
3. Im folgenden Dialog wählen Sie aus, **welche Spalten** zur Prüfung auf Duplikate herangezogen werden sollen

<!-- **Screenshot 21:** Dialogfenster „Duplikate entfernen" mit Liste aller Spaltenüberschriften (Standortname, Latitude, Longitude, Datum, Uhrzeit, Temperatur, Messmethode), jede mit Checkbox, alle standardmäßig angehakt. -->

**Wichtige Überlegung vor dem Löschen:** Was genau als „Duplikat" gilt, hängt davon ab, welche Spalten Sie zum Vergleich auswählen. Vergleichen Sie **alle** Spalten, gelten nur exakt identische Zeilen als Duplikat. Vergleichen Sie dagegen nur `Standortname` und `Datum`, würde Excel bereits zwei Zeilen als Duplikat behandeln, die sich nur in der Temperatur unterscheiden – das wäre in Ihrem Fall vermutlich falsch, da unterschiedliche Uhrzeiten am selben Tag durchaus unterschiedliche, beide gültige Messungen sein können.

**Vor dem Löschen: immer eine Kopie behalten.** `Daten → Duplikate entfernen` löscht unwiderruflich (abgesehen von `Strg`+`Z`, solange die Datei noch nicht erneut gespeichert wurde). Erstellen Sie sich vor diesem Schritt eine Sicherheitskopie der Datei, oder führen Sie die Bereinigung auf einer Kopie des Tabellenblatts durch.

**Duplikate zunächst nur sichtbar machen, statt sofort zu löschen:** Über **Start → Bedingte Formatierung → Regeln zum Hervorheben von Zellen → Doppelte Werte** lassen sich doppelte Einträge farblich markieren, ohne sie zu entfernen. So können Sie zunächst prüfen, ob es sich tatsächlich um echte Duplikate handelt, bevor Sie sie löschen.

<!-- **Screenshot 22:** Tabellenausschnitt mit einer Spalte „Standortname", in der zwei identische Einträge (z. B. „Marburg") rot hinterlegt sind durch die bedingte Formatierung „Doppelte Werte". -->

## Groß-/Kleinschreibung und uneinheitliche Schreibweisen

Ein Standortname wie `Marburg`, `marburg` und `MARBURG` sieht für Excel beim reinen Betrachten unterschiedlich aus – bei Filtern und Sortieren werden diese Varianten zwar meist noch zusammen einsortiert, bei **Duplikat-Erkennung, Zählen oder Gruppierungen** (z. B. mit `ZÄHLENWENN` oder einer Pivot-Tabelle) behandelt Excel sie aber teils inkonsistent, was zu verzerrten Auswertungen führt: Eine Auszählung „wie oft wurde in Marburg gemessen?" kann dann fälschlich mehrere getrennte Kategorien statt einer einzigen ausweisen.

**Funktionen zur Vereinheitlichung der Groß-/Kleinschreibung:**

| Funktion | Wirkung | Beispiel |
|---|---|---|
| `GROSS(Text)` | wandelt alle Buchstaben in Großbuchstaben um | `GROSS("marburg")` → `"MARBURG"` |
| `KLEIN(Text)` | wandelt alle Buchstaben in Kleinbuchstaben um | `KLEIN("MARBURG")` → `"marburg"` |
| `GROSS2(Text)` | schreibt den ersten Buchstaben jedes Worts groß, den Rest klein | `GROSS2("marburg an der lahn")` → `"Marburg An Der Lahn"` |

**Praktisches Vorgehen:** Legen Sie sich eine Hilfsspalte an, in der Sie z. B. `=GROSS2(A2)` auf die Spalte `Standortname` anwenden, prüfen Sie das Ergebnis, und ersetzen Sie anschließend die ursprüngliche Spalte durch die bereinigten Werte (Kopieren → Einfügen als Werte, damit die Formel nicht erhalten bleibt, sondern nur das berechnete Ergebnis).

<!--Tabelle mit Spalte A „Standortname" (uneinheitlich: „marburg", „MARBURG", „Marburg") und daneben Spalte B mit der Formel `=GROSS2(A2)`, sichtbar in der Bearbeitungsleiste, Ergebnis in Spalte B einheitlich „Marburg". -->

## Überflüssige Leer- und Sonderzeichen

Häufig enthalten Zellen unsichtbare überflüssige Leerzeichen – etwa am Anfang, Ende oder doppelt zwischen Wörtern (z. B. durch Copy-Paste aus einer Webseite oder einem PDF entstanden). Diese fallen beim bloßen Betrachten der Zelle **nicht auf**, führen aber dazu, dass `"Marburg"` und `"Marburg "` (mit Leerzeichen am Ende) von Excel als zwei unterschiedliche Werte behandelt werden.

**Funktionen zur Bereinigung:**

| Funktion | Wirkung | Beispiel |
|---|---|---|
| `GLÄTTEN(Text)` | entfernt führende/nachfolgende Leerzeichen sowie doppelte Leerzeichen zwischen Wörtern | `GLÄTTEN("  Marburg  Lahn ")` → `"Marburg Lahn"` |
| `SÄUBERN(Text)` | entfernt nicht druckbare Zeichen (z. B. Zeilenumbrüche, die beim Kopieren aus PDFs mit eingefügt wurden) | entfernt unsichtbare Steuerzeichen |

**So finden Sie versteckte Leerzeichen, bevor Sie bereinigen:** Markieren Sie eine verdächtige Zelle und schauen Sie in die Bearbeitungsleiste – ein Leerzeichen am Ende ist dort oft als kleiner Abstand nach dem letzten sichtbaren Zeichen erkennbar. Alternativ hilft die Formel `=LÄNGE(A2)`, um die tatsächliche Zeichenanzahl einer Zelle zu prüfen und mit der erwarteten Länge zu vergleichen.

## Textaufbereitung am Beispiel Koordinaten

Angenommen, eine Kommilitonin hat ihre Messung mit `50°48'12"N` erfasst, statt wie Sie selbst direkt in Dezimalgrad. Um daraus einen für QGIS oder R nutzbaren Wert zu machen, gehen Sie in Teilschritten vor (angenommen, der Text steht in Zelle `A2`):

1. **Grad extrahieren:** `=WERT(TEIL(A2;1;FINDEN("°";A2)-1))` → `50`
2. **Minuten extrahieren:** `=WERT(TEIL(A2;FINDEN("°";A2)+1;FINDEN("'";A2)-FINDEN("°";A2)-1))` → `48`
3. **Sekunden extrahieren:** analog zwischen `'` und `"`
4. **Umrechnung in Dezimalgrad:** `Dezimalgrad = Grad + Minute/60 + Sekunde/3600` → `50 + 48/60 + 12/3600 = 50,80333...`
5. **Vorzeichen beachten:** Ein „S" (Süd) oder „W" (West) am Ende bedeutet einen **negativen** Wert in Dezimalgrad – wichtig, da QGIS und R negative Werte für die südliche bzw. westliche Hemisphäre erwarten, nicht den Buchstaben `S`/`W`

**Warum das wichtig ist:** Genau in diesem letzten Punkt liegt eine häufige Fehlerquelle beim Datenimport in GIS-Software: Ein Punkt mit `Latitude = 50,80` und dem Buchstaben `S` in einer separaten Spalte wird von QGIS beim direkten Import als nördliche Hemisphäre interpretiert, wenn das Vorzeichen nicht vorher korrekt in der Zahl selbst abgebildet wurde.

## Konsistente Formatierung – Voraussetzung für jede Weiterverarbeitung

- **Dezimaltrennzeichen:** Deutschland nutzt standardmäßig das Komma (`8,4`), viele internationale/technische Quellen (darunter GPS-Geräte, R, Python, die meisten GIS-Programme) den Punkt (`8.4`) – für Berechnungen und insbesondere für den Export/Import in andere Software muss ein Datensatz einheitlich sein. Ein Datensatz mit gemischten Trennzeichen wird von R oder QGIS im schlimmsten Fall nicht als Fehler erkannt, sondern **falsch interpretiert** (z. B. `8.400` als „achttausendvierhundert" statt „8,4").
- **Datumsformate:** `14.03.2024` (DE), `2024-03-14` (ISO 8601), `3/14/2024` (US) sehen unterschiedlich aus und werden von Excel nicht automatisch vereinheitlicht – vor allem `TT.MM.JJJJ` vs. `MM/TT/JJJJ` ist eine häufige Fehlerquelle, weil beide Formate wie eine gültige Zahlenfolge aussehen, aber unterschiedlich interpretiert werden (der 3. Januar wird so leicht zum 1. März)
- **Koordinatenreferenzsystem (kurz erwähnt):** Dezimalgrad allein legt noch nicht fest, auf welches Referenzsystem sich die Koordinate bezieht. Für die meisten alltäglichen Anwendungen (GPS, Google Maps, OpenStreetMap) ist das **WGS84** (EPSG-Code 4326) der Standard, auf den sich auch QGIS beim Import ohne weitere Angaben meist bezieht. Für diesen Kurs reicht es zu wissen, dass dieser Standard existiert – bei Bedarf finden Sie in QGIS unter den Layer-Eigenschaften, welches System aktuell verwendet wird.

**Empfehlung für die Praxis:** Bringen Sie Ihre Datensätze möglichst früh in ein einheitliches Format – idealerweise **Dezimalgrad mit Punkt als Trennzeichen** für Koordinaten bevor Sie sie weiterverarbeiten, mit anderen Datensätzen kombinieren oder in eine andere Software importieren.