---
title: Funktionen
published: true
toc: true
header:
  image: /assets/images/unit02/DataSwamp_Stage02_2.png
  image_description: "Datensumpf Level 02"
  caption: "Level 2: Die Schwebeteilchen."
---

Im letzten Kapitel haben Sie eigene Formeln mit Grundrechenarten und Zellbezügen gebaut. Für viele wiederkehrende Berechnungen – Datum, Mittelwert, Runden – müssen Sie diese Formeln aber nicht jedes Mal neu erfinden: Excel bringt dafür **Funktionen** mit, vordefinierte Formeln mit festgelegtem Namen und festgelegten Argumenten.

<!-- Hinweis zur Excel-Version: Funktionssyntax und alle in diesem Kapitel gezeigten Funktionen sind in allen aktuellen Excel-Versionen identisch verfügbar. -->

## Struktur von Funktionen

Jede Funktion folgt demselben Grundaufbau:

```
=FUNKTIONSNAME(ARGUMENT1; ARGUMENT2; ...; ARGUMENTx)
```

- **Argumente** sind Zellbezüge oder feste Werte, die die Funktion genauer spezifizieren.
- Manche Argumente sind **optional** – in der Funktionsbeschreibung erkennen Sie das an eckigen Klammern, z. B. `RUNDEN(Zahl; [Anzahl_Stellen])`.
- Es gibt auch Funktionen **ganz ohne** Argumente, z. B. `=PI()` — die Klammern bleiben trotzdem stehen, nur leer.

**Wichtig – Trennzeichen ist sprachabhängig:** Ob Argumente durch Semikolon `;` oder Komma `,` getrennt werden, hängt von der **Spracheinstellung** Ihres Excel ab. Mit deutscher/europäischer Einstellung gilt `;` (da `,` bereits als Dezimaltrennzeichen verwendet wird), mit angloamerikanischer Einstellung gilt `,`. Öffnen Sie eine Datei mit anderer Spracheinstellung als Ihrer eigenen, kann es deshalb zunächst zu Fehlermeldungen kommen, bis Excel die Trennzeichen automatisch anpasst.

## Datumsfunktionen

| Funktion | Bedeutung |
|---|---|
| `HEUTE()` | Aktuelles Datum (aktualisiert sich automatisch bei jedem Öffnen der Datei) |
| `DATUM(Jahr; Monat; Tag)` | Erzeugt aus drei Zahlen ein echtes Datum |
| `JAHR(Datum)` | Extrahiert das Jahr aus einem Datum |
| `MONAT(Datum)` | Extrahiert den Monat aus einem Datum |
| `TAG(Datum)` | Extrahiert den Tag aus einem Datum |
| `DATWERT(Text)` | Wandelt einen als Text vorliegenden Datumswert in ein echtes, rechenfähiges Datum um |

Da Excel ein Datum intern als fortlaufende Zahl speichert (siehe Kapitel zu Zellformaten), lassen sich zwei Daten einfach **voneinander subtrahieren**, um die Anzahl der Tage dazwischen zu erhalten.

## Übung: Datumsfunktionen

Arbeiten Sie auf einem neuen Tabellenblatt und beschriften Sie es mit Ihrem Namen.

Berechnen Sie mit einem Zellbezug, wie alt Sie (oder eine andere Person) **in Tagen** sind:

1. Tragen Sie in eine Zelle Ihr Geburtsdatum ein (z. B. mit `=DATUM(Jahr;Monat;Tag)` oder durch direkte Eingabe im Datumsformat).
2. Berechnen Sie in einer zweiten Zelle mit `=HEUTE()` das aktuelle Datum.
3. Subtrahieren Sie beide Zellen voneinander. Formatieren Sie das Ergebnis als **Zahl** (nicht als Datum!), sonst zeigt Excel Ihnen ein unsinniges Datum statt einer Tagesanzahl an.

*(Zeitbedarf: ca. 10 Minuten)*

## Mathematische Funktionen

| Funktion | Bedeutung |
|---|---|
| `SUMME(Zellbereich)` | Summe aller Werte im Bereich |
| `MITTELWERT(Zellbereich)` | Arithmetisches Mittel |
| `MEDIAN(Zellbereich)` | Median (siehe Kapitel zu Kennzahlen) |
| `MIN(Zellbereich)` / `MAX(Zellbereich)` | Kleinster / größter Wert |
| `RUNDEN(Zahl; Anzahl_Stellen)` | Rundet mathematisch auf die angegebene Anzahl Nachkommastellen |
| `WURZEL(Zahl)` | Quadratwurzel |
| `POTENZ(Basis; Potenz)` | z. B. `POTENZ(x;2)` für `x²` |
| `PI()` | Die Kreiszahl π |
| `ZUFALLSZAHL()` | Zufallszahl zwischen 0 und 1 |
| `GANZZAHL(Zahl)` | Rundet **ab** auf die nächste ganze Zahl (kappt alle Nachkommastellen) |

## Runden — zwei grundverschiedene Wege

Es gibt zwei Möglichkeiten, eine Zahl mit weniger Nachkommastellen anzuzeigen – die aber **nicht dasselbe** bewirken:

| Methode | Effekt |
|---|---|
| **Funktion `RUNDEN(...)`** | Verändert den **tatsächlich gespeicherten Wert** der Zelle. Die überschüssigen Nachkommastellen gehen dabei unwiederbringlich verloren. |
| **Dezimalstellen-Buttons** (Start → Zahl → „Dezimalstelle hinzufügen/entfernen") | Rein **optische** Rundung des Zellformats. Der intern gespeicherte Wert bleibt unverändert – nur die Anzeige ändert sich. |

**Testen Sie den Unterschied konkret:** Wenden Sie beide Methoden auf denselben Ausgangswert an und kopieren Sie das jeweilige Ergebnis anschließend mit „Einfügen als Werte" in eine neue Zelle. Bei der `RUNDEN`-Variante bleibt der gerundete Wert erhalten; bei der Dezimalstellen-Variante erscheint der ursprüngliche, ungerundete Wert wieder – der war die ganze Zeit nur optisch versteckt.

**Warum der Unterschied wichtig ist:** Wenn Sie mit einer optisch gerundeten Zahl weiterrechnen, rechnet Excel weiterhin mit dem **vollen, ungerundeten** Wert – das kann zu Ergebnissen führen, die auf den ersten Blick nicht zur Anzeige zu passen scheinen (z. B. wenn `2,4 + 2,4` als `5` statt `4,8` angezeigt wird, weil beide Ausgangswerte eigentlich `2,45` waren und nur optisch auf eine Nachkommastelle gerundet angezeigt wurden). Möchten Sie dagegen sicherstellen, dass **wirklich** mit dem gerundeten Wert weitergerechnet wird, müssen Sie `RUNDEN(...)` verwenden.

## Verschachteln

Statt für eine Berechnung mehrere Spalten nacheinander zu nutzen, kann man auch Funktionen verschachteln. Dazu setzt man eine Funktion als Argument in eine andere Funktion ein. Excel berechnet dabei immer zuerst die innere Funktion und gibt ihr Ergebnis an die äußere weiter, beispielsweise =RUNDEN(MITTELWERT(A1:A10);2)

## Übung: Mathematische Funktionen 

Nutzen Sie erneut Ihre Arbeitsmappe mit `Datensatz_1`.

Die durchschnittliche Temperatur soll übersichtlich zusammengefasst werden:

1. Berechnen Sie in einer Zelle oben rechts die **durchschnittliche, maximale und minimale Temperatur** aller Messungen.
2. Verschachteln Sie diese Formel mit `RUNDEN`, sodass das Ergebnis auf **zwei Nachkommastellen** mathematisch gerundet direkt in derselben Zelle steht (nicht nur optisch).
<!--
## Additional resources
-->