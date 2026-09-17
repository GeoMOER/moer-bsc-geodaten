---
title: Recap
published: true
toc: true
header:
  image: /assets/images/unit04/streuobst.jpg
  image_description: "Streuobstwiese"
  caption: "Image: ulrichstill [CC BY-SA 2.0 DE] via [wikimedia.org](https://commons.wikimedia.org/wiki/File:Tuebingen_Streuobstwiese.jpg)"
---


Ihre beiden Sensordatensätze sind inzwischen bereinigt (keine Duplikate mehr, einheitliche Schreibweise, saubere Koordinatenspalten). Trotzdem lassen sie sich noch nicht einfach übereinanderkopieren – ihre Spalten heißen unterschiedlich und stehen in unterschiedlicher Reihenfolge. Genau das lösen wir in diesem Kapitel.

<!-- Hinweis zur Excel-Version: Alle in diesem Kapitel gezeigten Funktionen (SVERWEIS, Pivot-Tabelle, Einfügen als Werte) sind in allen aktuellen Excel-Versionen identisch verfügbar. -->

## Spalten angleichen

Vergleichen Sie die Kopfzeilen Ihrer beiden Blätter:

| `Datensatz_1` | `Datensatz_2` | Bedeutung |
|---|---|---|
| `Standort` | `Ort` | Stationsname |
| `Koordinaten_roh` | `Koordinaten` | Koordinate (vor der Aufsplittung) |
| `Datum` + `Uhrzeit` (getrennt) | `Zeitstempel` (kombiniert) | Zeitpunkt der Messung |
| `Temperatur` | `Temp_Celsius` | Messwert |
| `Messmethode` | `Erfassungsart` | Art der Erfassung |

Bevor Sie beide Tabellen zusammenführen können, müssen Sie sich für **ein** gemeinsames Schema entscheiden und beide Tabellen darauf angleichen. Ein sinnvolles Vorgehen:

1. **Spalten umbenennen:** Benennen Sie auf `Datensatz_2` die Spalten so um, dass sie zu `Datensatz_1` passen (`Ort` → `Standort`, `Temp_Celsius` → `Temperatur`, `Koordinaten` → `Koordinaten_roh`, `Erfassungsart` → `Messmethode`).
2. **Zeitstempel aufteilen:** `Datensatz_2` hat Datum und Uhrzeit in einer Spalte `Zeitstempel` kombiniert. Legen Sie zwei neue Spalten `Datum` und `Uhrzeit` an:
   - `Datum`: `=GANZZAHL(A2)` (schneidet den Uhrzeit-Anteil ab) – anschließend als Datum formatieren
   - `Uhrzeit`: `=A2-GANZZAHL(A2)` (übrig bleibt nur der Nachkomma-Anteil, der die Uhrzeit repräsentiert) – anschließend als Uhrzeit formatieren
3. **Spaltenreihenfolge angleichen:** Ordnen Sie die Spalten auf `Datensatz_2` in derselben Reihenfolge an wie auf `Datensatz_1` (per Drag & Drop der Spaltenköpfe oder Ausschneiden/Einfügen ganzer Spalten).

<!-- Screenshot: Zwei Excel-Tabellenblätter nebeneinander, links Datensatz_1 mit den Spalten Standort/Koordinaten_roh/Datum/Uhrzeit/Temperatur/Messmethode, rechts Datensatz_2 nach der Angleichung mit identischer Spaltenreihenfolge und identischen Überschriften. -->

## Zeilen anhängen

Sobald beide Tabellen dieselben Spalten in derselben Reihenfolge haben, können Sie sie zusammenführen:

1. Markieren Sie auf `Datensatz_2` den gesamten Datenbereich **ohne** die Kopfzeile
2. Kopieren Sie ihn (`Strg`+`C`)
3. Wechseln Sie zu `Datensatz_1`, klicken Sie in die erste leere Zeile **unterhalb** der letzten Datenzeile (am schnellsten mit `Strg`+`Ende`, dann eine Zeile weiter)
4. Fügen Sie ein (`Strg`+`V`)

Sie haben jetzt eine einzige, zusammengeführte Tabelle mit allen Messungen aus beiden Quellen.

**Kontrolle:** Prüfen Sie mit `Strg`+`Ende`, ob die Gesamtzeilenzahl der Summe aus beiden Ausgangstabellen entspricht. Prüfen Sie außerdem stichprobenartig, ob Datum und Uhrzeit nach dem Aufteilen in Schritt 2 des vorigen Abschnitts korrekt aussehen.
