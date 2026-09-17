---
title: Textbearbeitung
published: true
toc: true
header:
  image: /assets/images/unit02/31031723265_0890cd9547_o.jpg
  image_description: "Cloudscape Over the Philippine Sea"
  caption: "Image: [NASA's Marshall Space Flight Center](https://www.nasa.gov/centers/marshall/home/index.html) [CC BY-NC 2.0] via [flickr.com](https://www.flickr.com/photos/nasamarshall/31031723265/)"
---


Ihre Sensordaten enthalten eine Spalte `Koordinaten_roh` bzw. `Koordinaten`, in der mehrere Informationen in einem einzigen Text zusammengefasst sind, z. B. `50°48'51.43"N, 8°46'19.85"E`. Das ist ein Muster, das Ihnen bei importierten oder von Geräten exportierten Daten häufig begegnen wird: verschiedene Informationen stecken in einer einzigen Zelle und müssen zunächst technisch getrennt werden, bevor man mit ihnen weiterarbeiten kann.

**Was diese Zahlen genau bedeuten und wie man daraus eine Position auf der Erde bestimmt, behandeln wir ausführlich in einem späteren Lernabschnitt zu Geodaten.** Hier lernen Sie zunächst nur das Handwerkszeug: die Textfunktionen, mit denen sich ein solcher zusammengesetzter Text in Excel in seine Bestandteile zerlegen lässt. Diese Funktionen werden Ihnen auch bei ganz anderen Textspalten wieder begegnen (siehe Kapitel zur Datenbereinigung).

<!-- Hinweis zur Excel-Version: Die Textfunktionen TEIL, FINDEN, WERT und GLÄTTEN sind in allen aktuellen Excel-Versionen identisch verfügbar. -->

## Grundlegende Textfunktionen

| Funktion | Zweck | Beispiel |
|---|---|---|
| `TEIL(Text; Start; Länge)` | Extrahiert einen Ausschnitt aus der Mitte eines Texts, ab einer bestimmten Position, mit einer bestimmten Länge | `TEIL("50°48'51.43\"N";1;2)` → `"50"` |
| `FINDEN(Suchtext; Text)` | Findet die *Position* eines bestimmten Zeichens innerhalb eines Texts | `FINDEN("°";"50°48'51.43\"N")` → `3` |
| `WERT(Text)` | Wandelt einen Text, der wie eine Zahl aussieht, in eine echte, rechenfähige Zahl um | `WERT("50")` → `50` |
| `GLÄTTEN(Text)` | Entfernt überflüssige Leer- und Zwischenraumzeichen | `GLÄTTEN("  50 ")` → `"50"` |

**Warum `FINDEN` und `TEIL` meist gemeinsam auftreten:** `TEIL` braucht eine feste Startposition und Länge – die kennen Sie bei unterschiedlich langen Texten aber oft nicht im Voraus. `FINDEN` liefert genau diese Position, indem es nach einem bestimmten Trennzeichen sucht (hier z. B. `°`, `'` oder `"`). Die Kombination beider Funktionen ist deshalb ein Standardmuster: **erst die Position finden, dann an dieser Position den Text herausschneiden.**

## Textfunktionen anwenden – Schritt für Schritt

Nehmen wir den Wert `50°48'51.43"N` (aus Ihrer Spalte `Koordinaten_roh`, Zelle `B2`) als Übungsbeispiel für das Zerlegen eines zusammengesetzten Texts:

**Schritt 1 – Ersten Teil extrahieren (vor dem `°`):**
```
=TEIL(B2;1;FINDEN("°";B2)-1)
```
`FINDEN("°";B2)` liefert die Position des `°`-Zeichens (hier: `3`). `TEIL` schneidet davon alles **vor** dieser Position heraus, also die ersten beiden Zeichen: `"50"`.

**Schritt 2 – Mittleren Teil extrahieren (zwischen `°` und `'`):**
```
=TEIL(B2;FINDEN("°";B2)+1;FINDEN("'";B2)-FINDEN("°";B2)-1)
```
Hier wird die Startposition um eins **hinter** das `°`-Zeichen gelegt, und die Länge ergibt sich aus dem Abstand zwischen den beiden Positionen von `°` und `'`.

**Schritt 3 – In eine echte Zahl umwandeln:**
```
=WERT(TEIL(B2;1;FINDEN("°";B2)-1))
```
Ohne `WERT` bliebe das Ergebnis von `TEIL` immer **Text** – auch wenn es wie eine Zahl aussieht. Erst `WERT` macht daraus eine Zahl, mit der Sie z. B. `MITTELWERT` oder eine weitere Berechnung durchführen könnten.

<!-- Screenshot: Excel-Tabelle mit Spalte Koordinaten_roh und daneben drei Hilfsspalten "Teil 1", "Teil 2", "Teil 3", in denen schrittweise mit TEIL und FINDEN einzelne Textabschnitte extrahiert werden - jede Hilfsspalte mit sichtbarer Formel in der Bearbeitungsleiste. -->

## Achtung – Formatfehler innerhalb der Spalte

Wenn Sie Ihre Formeln auf die **gesamte Spalte** `Koordinaten_roh` anwenden, werden Sie vermutlich bei einer Zeile ein unplausibles Ergebnis erhalten: Eine der Koordinaten enthält einen **Tippfehler im Format** – ein einfaches Hochkomma `'` anstelle des Anführungszeichens `"`. Diese Art Fehler passiert in der Praxis häufig (unterschiedliche Tastaturlayouts, Copy-Paste aus verschiedenen Quellen) und fällt beim bloßen Betrachten der Zelle kaum auf.

**Vorgehen bei so einem Fehler:**
1. Identifizieren Sie die betroffene Zeile (die Formel liefert dort `#WERT!` oder ein offensichtlich falsches Ergebnis)
2. Prüfen Sie den Original-Text in der Zelle genau – zählen Sie die Anführungszeichen/Hochkommas
3. Korrigieren Sie den Tippfehler manuell in der Ursprungsspalte, bevor Sie die Formel erneut anwenden

<!-- Screenshot: Excel-Tabelle mit einer Zeile, in der die Formel #WERT! anzeigt, daneben die Ursprungszelle mit dem fehlerhaften Text 50°50'16.5'N (zwei Hochkommas statt Grad-Minuten-Sekunden-Zeichen). -->

---

## Übung: Textfunktionen an den Sensordaten üben

Arbeiten Sie weiter mit Ihrer Arbeitsmappe aus den letzten Kapiteln (Blatt `Datensatz_1`, Spalte `Koordinaten_roh` bzw. Blatt `Datensatz_2`, Spalte `Koordinaten`).

1. Legen Sie auf **beiden** Blättern je drei Hilfsspalten an und extrahieren Sie mit `TEIL`/`FINDEN` schrittweise die drei Zahlen-Anteile (Grad, Minuten, Sekunden) aus der jeweiligen Koordinatenspalte – zunächst nur für eine einzelne Zeile.
2. Wandeln Sie jeden der drei extrahierten Textwerte mit `WERT` in eine echte Zahl um. Prüfen Sie an der Ausrichtung (rechtsbündig = Zahl), ob die Umwandlung funktioniert hat.
3. Ziehen Sie Ihre Formeln über die gesamte jeweilige Spalte. Identifizieren Sie die Zeile mit dem Formatfehler und korrigieren Sie den Tippfehler in der Ursprungsspalte.
4. Speichern Sie Ihre Datei – Sie arbeiten in den kommenden Kapiteln mit denselben Hilfsspalten weiter.

**Reflexionsfrage:** An welcher Stelle Ihrer Formeln hätte sich der Formatfehler (`'` statt `"`) auf das Ergebnis auswirken müssen – auch ohne dass Sie bereits wissen, was die einzelnen Zahlenanteile inhaltlich bedeuten?



<!--
Ihre Klimadaten enthalten Koordinaten (Latitude, Longitude) – vermutlich bereits im Dezimalgrad-Format, wie Sie es bei der Eingabe erfasst haben. Sobald Sie jedoch Daten aus anderen Quellen einbinden (GPS-Geräte, andere Messstationen, händisch abgelesene Karten, Kommiliton:innen mit anderer Erfassungsmethode), werden Sie feststellen: **Koordinaten kommen selten einheitlich formatiert an.** Das ist kein Nischenproblem – es ist einer der häufigsten Gründe, warum sich Geodaten aus unterschiedlichen Quellen nicht ohne Weiteres kombinieren, in einer Karte darstellen oder in Analyse-Software importieren lassen.

## Themenüberschrift 01: Warum das Koordinatenformat für die Weiterverarbeitung entscheidend ist

Ihre Excel-Tabelle ist in diesem Kurs nur die **erste Station** Ihrer Daten. Realistischerweise werden Geodaten im weiteren Studienverlauf (oder danach) an anderer Stelle weiterverarbeitet:

- **QGIS** (und andere GIS-Software) erwartet für den Import von Punktdaten aus einer Tabelle in der Regel **Dezimalgrad** in zwei getrennten Spalten (z. B. `Longitude`/`X` und `Latitude`/`Y`) – ein Format wie `50°48'12"N` in einer einzigen Zelle kann QGIS beim direkten CSV-Import nicht automatisch interpretieren
- In **R**  müssen Koordinaten als numerische Werte vorliegen, damit sie überhaupt für räumliche Berechnungen (Distanzen, Pufferzonen, Projektionen) oder Kartendarstellungen nutzbar sind – ein Text wie `"50,80"` (mit Komma als Dezimaltrennzeichen und als Text formatiert) führt beim Einlesen in R zu Fehlern oder zumindest zu einer falschen Interpretation
- Auch der **Datenaustausch mit anderen Personen oder Institutionen** setzt meist ein standardisiertes Format voraus – international übliche Geodatenformate (z. B. WGS84, das Referenzsystem, das auch GPS und die meisten Online-Karten verwenden) nutzen durchgehend Dezimalgrad mit Punkt als Dezimaltrennzeichen.

Weitere Hintergünde werden Sie dazu im Verlauf des Kurses lernen, ebenso, wie Sie innerhalb in Excel ihr Format anpassen können.

Entscheident für dieses Kapitel ostFFolgendes:

> Für die Spalten `Latitude`/`Longitude`, die Sie später in QGIS oder R weiterverwenden wollen, sollten Sie **kein** benutzerdefiniertes Format mit angehängtem Symbol verwenden (also nicht `0,0000" °"` o. ä.). Der Grund: Diese Spalten sollen als **reine Zahl ohne jede zusätzliche Anzeige** vorliegen, damit ein späterer Export (z. B. als CSV für den Import in QGIS) garantiert nur den nackten Zahlenwert enthält. Ein angehängtes Gradzeichen wird zwar nur *angezeigt*, aber manche Exportwege oder Programme lesen die *sichtbare* Zeichenkette statt des internen Werts aus – dann scheitert der Import.

> Formatieren Sie die Koordinatenspalten stattdessen als einfaches **Zahlenformat mit ausreichend Nachkommastellen** (`Zellen formatieren → Zahl → 6 Dezimalstellen`, z. B. `50,803330`). Sechs Nachkommastellen entsprechen einer Genauigkeit von unter einem Meter – deutlich mehr Stellen bringen keinen praktischen Mehrwert, deutlich weniger (z. B. nur 2 Nachkommastellen) können bei kleinräumigen Distanzen bereits spürbare Ungenauigkeiten verursachen.


<!-->


> Ein zweiter Fallstrick: Das Dezimaltrennzeichen (Komma vs. Punkt), das Sie in der Zelle sehen, ist eine reine **Anzeige-Einstellung Ihres Excel bzw. Betriebssystems** – gespeichert ist intern immer derselbe Zahlenwert. Erst beim **Export** (z. B. Speichern als CSV) wird das tatsächlich verwendete Trennzeichen relevant, und das hängt wiederum von den Regionseinstellungen Ihres Rechners ab. Prüfen Sie deshalb nach einem CSV-Export in einem einfachen Texteditor (nicht wieder in Excel!), welches Trennzeichen tatsächlich in der Datei steht – das ist das Zeichen, das QGIS oder R beim Einlesen sehen werden.


**Praktische Konsequenz:** Wenn Ihre Koordinaten uneinheitlich vorliegen – manche im DMS-Format, manche mit Komma statt Punkt, manche als Text statt als Zahl – müssen Sie diese **vor jeder Weiterverarbeitung** in Excel bereinigen und vereinheitlichen. Das ist die Aufgabe, die Sie in diesem Kapitel üben.

- Rohdaten liefern Koordinaten also typischerweise **nicht** einheitlich – je nach Quelle (GPS-Gerät, Website, händische Erfassung) unterschiedlich formatiert
- Die Umrechnung von DMS in Dezimalgrad erfolgt in der Praxis meist in zwei Schritten: (1) Grad-, Minuten- (ggf. Sekunden-)Anteil aus dem Text herauslösen, (2) daraus die Dezimalzahl berechnen
- Dafür werden Textfunktionen benötigt, die einzelne Zeichen bzw. Positionen innerhalb eines Textstrings ansprechen können – siehe nächster Abschnitt

## Textfunktionen (TEIL, GLÄTTEN, ERSETZEN)

| Funktion | Zweck | Beispiel |
|---|---|---|
| `TEIL(Text; Start; Länge)` | Extrahiert einen Ausschnitt aus der Mitte eines Texts | `TEIL("50°48'N";4;2)` → `"48"` |
| `GLÄTTEN(Text)` | Entfernt überflüssige Leer- und Zwischenraumzeichen | `GLÄTTEN("  Anna Müller")` → `"Anna Müller"` |
| `ERSETZEN(Text; Start; Länge; neuer_Text)` | Ersetzt Zeichen an einer *bestimmten Position* | `ERSETZEN("8,4";2;1;".")` → `"8.4"` |
| `FINDEN(Suchtext; Text)` | Findet die *Position* eines Zeichens (wird oft mit `TEIL`/`ERSETZEN` kombiniert, da diese eine Positionsangabe brauchen) | `FINDEN(",";"8,4")` → `2` |
| `WERT(Text)` | Wandelt einen Text, der wie eine Zahl aussieht, in eine echte, rechenfähige Zahl um | `WERT("8.4")` → `8.4` |

> **Screenshot 9:** Excel-Tabelle mit einer Spalte `Koordinaten_roh` (z. B. `50°48'12"N`) und daneben mehreren Hilfsspalten, in denen schrittweise mit `TEIL`, `FINDEN` und `WERT` die Grad-, Minuten- und Sekundenanteile extrahiert werden – jede Hilfsspalte mit sichtbarer Formel in der Bearbeitungsleiste.

### Praxisbeispiel: DMS-Koordinate in Dezimalgrad umrechnen

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

**Empfehlung für die Praxis:** Bringen Sie Ihre Datensätze möglichst früh in ein einheitliches Format – idealerweise **Dezimalgrad mit Punkt als Trennzeichen** für Koordinaten und **ISO 8601** (`JJJJ-MM-TT`) für Datumsangaben –, bevor Sie sie weiterverarbeiten, mit anderen Datensätzen kombinieren oder in eine andere Software importieren. Diese beiden Formate sind die am weitesten verbreiteten Standards im internationalen und technischen Datenaustausch und ersparen Ihnen spätere Fehlersuche.
-->