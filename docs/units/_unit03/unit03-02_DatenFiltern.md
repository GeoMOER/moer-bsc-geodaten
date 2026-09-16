---
title: Daten filtern und sortieren
published: true
header:
  image: /assets/images/unit05/notebook.jpg
  caption: "Image: [Neil Conway](https://www.flickr.com/photos/neilconway/) [(Public Domain Mark 1.0)](https://creativecommons.org/publicdomain/mark/1.0/deed.en) via [flickr.com](https://www.flickr.com/photos/neilconway/5625707813/in/photostream/)"
---

<!-- Themenblock 02-06: Filtern und Sortieren -->

Ihre Excel-Tabelle wächst mit jeder weiteren Messung. Um darin gezielt einzelne Werte zu finden, Auffälligkeiten zu erkennen oder die Tabelle für eine bestimmte Fragestellung einzugrenzen, benötigen Sie zwei grundlegende Werkzeuge: **Sortieren** (die Reihenfolge der Zeilen verändern) und **Filtern** (nur bestimmte Zeilen anzeigen, ohne die übrigen zu löschen). Beide Funktionen verändern nicht die Daten selbst, sondern nur deren Darstellung.

##  Sortieren

Beim Sortieren wird die Reihenfolge der **gesamten Zeilen** nach dem Inhalt einer oder mehrerer Spalten verändert – nicht nur die einzelne Spalte, in der Sie sortieren.

**Einfache Sortierung:**
1. Klicken Sie in eine beliebige Zelle der Spalte, nach der sortiert werden soll (z. B. `Temperatur`)
2. Menüband: **Daten → Sortieren A–Z** (aufsteigend) oder **Sortieren Z–A** (absteigend) – bei Zahlen entsprechend „kleinster bis größter Wert" bzw. umgekehrt

<!-- **Screenshot 16:** Excel-Menüband, Reiter „Daten", mit hervorgehobenen Schaltflächen „A-Z" und „Z-A" in der Gruppe „Sortieren & Filtern".
-->

**Wichtig – der häufigste Anfängerfehler beim Sortieren:** Wird nur eine einzelne Spalte markiert (statt die ganze Tabelle bzw. mindestens eine Zelle darin) und sortiert, kann Excel nachfragen, ob die „Auswahl erweitert" werden soll. Wählen Sie in diesem Fall immer **„Auswahl erweitern"** – andernfalls wird nur die markierte Spalte umsortiert, während alle anderen Spalten unverändert an ihrer Position bleiben. Die Folge: Ihre Datensätze passen nicht mehr zusammen – eine Temperatur steht dann plötzlich beim falschen Standort und Datum.

<!-- **Screenshot 17:** Excel-Dialogfenster „Sortierwarnung" mit den zwei Optionen „Auswahl erweitern" (markiert/empfohlen) und „Mit der aktuellen Auswahl fortfahren".
-->

**Nach mehreren Kriterien sortieren:**
Über **Daten → Sortieren** (nicht A–Z/Z–A, sondern die Schaltfläche „Sortieren" selbst) öffnet sich ein Dialog, in dem Sie mehrere Sortierebenen festlegen können – z. B. zunächst nach `Standortname` (alphabetisch), und innerhalb jedes Standorts zusätzlich nach `Datum` (chronologisch). Über „Ebene hinzufügen" fügen Sie weitere Sortierkriterien hinzu.

<!-- **Screenshot 18:** Dialogfenster „Sortieren" mit zwei definierten Ebenen: „Sortieren nach: Standortname, A bis Z" und „Dann nach: Datum, Älteste zuerst", inklusive der Schaltfläche „Ebene hinzufügen".
-->

##  Filtern

Während Sortieren die Reihenfolge verändert, blendet **Filtern** einzelne Zeilen nur vorübergehend aus, ohne sie zu löschen. Das ist besonders nützlich, wenn Sie z. B. nur die Messungen eines bestimmten Standorts oder eines bestimmten Zeitraums betrachten möchten, ohne die übrigen Daten zu verlieren.

**Filter aktivieren:**
1. Klicken Sie in eine beliebige Zelle innerhalb Ihrer Datentabelle
2. Menüband: **Daten → Filtern** – in der Kopfzeile jeder Spalte erscheint nun ein kleines Dropdown-Symbol (Pfeil)

<!-- **Screenshot 19:** Tabellenkopf mit sichtbaren Filter-Dropdown-Pfeilen neben jeder Spaltenüberschrift (Standortname, Latitude, Longitude, Datum, Uhrzeit, Temperatur, Messmethode).
-->
**Filter anwenden:**
- Klick auf das Dropdown-Symbol einer Spalte öffnet eine Liste aller in dieser Spalte vorkommenden Werte, jeweils mit Checkbox
- Häkchen bei den gewünschten Werten setzen (bzw. „Alles auswählen" entfernen und dann gezielt einzelne Werte auswählen) → nur Zeilen mit diesen Werten bleiben sichtbar
- Bei Zahlen- und Datumsspalten stehen zusätzlich **Zahlenfilter** bzw. **Datumsfilter** zur Verfügung (z. B. „größer als", „zwischen", „letzte 7 Tage")

<!-- Geöffnetes Filter-Dropdown der Spalte „Temperatur" mit sichtbarer Werteliste (Checkboxen) im oberen Bereich und dem Untermenü „Zahlenfilter" mit Optionen wie „Größer als…", „Zwischen…" im unteren Bereich. -->

**Woran erkennt man, dass gefiltert wurde?**
- Das Filter-Symbol der aktiven Spalte ändert sich sichtbar (Trichter-Symbol statt einfachem Pfeil)
- Die Zeilennummern am linken Rand springen (z. B. 1, 2, 5, 9, …) – sichtbares Zeichen dafür, dass Zeilen ausgeblendet sind
- In der Statusleiste unten zeigt Excel z. B. „12 von 45 Datensätzen gefunden" an

**Filter zurücksetzen:**
Über das Dropdown-Symbol der gefilterten Spalte → „Filter löschen aus [Spaltenname]", oder über **Daten → Löschen**, um alle Filter der Tabelle gleichzeitig zu entfernen.

## Typische Fallstricke

**Gefilterte Daten werden oft übersehen.** Wenn eine Tabelle gefiltert ist und Sie neue Zeilen ergänzen, geraten diese leicht außerhalb des sichtbaren (gefilterten) Bereichs – sie sind dann zwar vorhanden, aber nicht automatisch im aktuellen Filter enthalten. Prüfen Sie nach dem Eintragen neuer Daten daher immer, ob der Filter noch die gewünschten Zeilen anzeigt, oder setzen Sie ihn vor dem Ergänzen neuer Werte zurück.

**Berechnungen berücksichtigen gefilterte Zeilen unterschiedlich.** Die Funktion `=SUMME(...)` bezieht ausgeblendete (gefilterte) Zeilen weiterhin mit ein – das Ergebnis ändert sich also **nicht**, wenn Sie filtern. Möchten Sie dagegen nur die aktuell sichtbaren, gefilterten Zeilen summieren, benötigen Sie die Funktion `=TEILERGEBNIS(9;Bereich)`. Das ist ein Detail, das bei Zwischenständen häufig zu scheinbar „falschen" Ergebnissen führt.

**Sortieren einer gefilterten Tabelle ist möglich, aber unübersichtlich.** Wenn Sie eine bereits gefilterte Tabelle zusätzlich sortieren, bezieht sich die Sortierung nur auf die aktuell sichtbaren Zeilen – für die Nachvollziehbarkeit ist es meist sinnvoller, zuerst zu sortieren und danach zu filtern, oder umgekehrt konsequent zu trennen.

**Tidy-Data-Bezug:** Filtern und Sortieren funktionieren nur zuverlässig, wenn Ihre Tabelle dem Tidy-Data-Prinzip aus einem früheren Kapitel folgt (eine Beobachtung pro Zeile, eine Variable pro Spalte, durchgehende Kopfzeile ohne Leerzeilen dazwischen). Eine Leerzeile mitten in der Tabelle etwa führt dazu, dass Excel beim Filtern/Sortieren nur den Bereich bis zur Leerzeile erkennt – die Zeilen danach werden stillschweigend ignoriert.

---

## Übung: Klimadaten filtern und sortieren

Nutzen Sie Ihre zusammengeführte Excel-Tabelle mit den eigenen und den zusätzlichen Klimadaten aus den vorherigen Kapiteln.

1. Aktivieren Sie den Filter für Ihre gesamte Tabelle (**Daten → Filtern**).
2. Filtern Sie die Tabelle so, dass **nur Messungen eines einzigen Standorts** angezeigt werden. Notieren Sie, wie viele Zeilen danach sichtbar sind (Statusleiste).
3. Erweitern Sie den Filter der Spalte „Temperatur" um einen **Zahlenfilter**, der nur Werte über einem von Ihnen gewählten Schwellenwert anzeigt (z. B. „größer als 10").
4. Setzen Sie beide Filter wieder zurück, sodass alle Zeilen sichtbar sind.
5. Sortieren Sie die gesamte Tabelle **zuerst nach Standortname (A–Z), dann nach Datum (älteste zuerst)** über den Dialog „Daten → Sortieren" mit zwei Sortierebenen.
6. Markieren Sie versuchsweise **nur die Spalte „Temperatur"** (nicht die ganze Tabelle) und sortieren Sie diese für sich allein. Bestätigen Sie im erscheinenden Warndialog bewusst **„Mit der aktuellen Auswahl fortfahren"** statt „Auswahl erweitern". Beobachten Sie, was mit den anderen Spalten passiert – prüfen Sie anhand einer Ihnen bekannten Zeile, ob Standort und Temperatur noch zusammenpassen.
7. Machen Sie diesen letzten Schritt mit `Strg` + `Z` rückgängig und wiederholen Sie die Sortierung korrekt, diesmal mit „Auswahl erweitern".
8. Speichern Sie Ihre Datei abschließend.
