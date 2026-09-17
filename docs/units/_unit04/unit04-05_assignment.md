--- 
title: ÜA | Übungsaufgabe Abschnitt 04
published: true
toc: true
header:
  image: /assets/images/01-splash.jpg
  image_description: "Dr. John Snow's map"
  caption: "Map: [**Dr. John Snow**](https://en.wikipedia.org/wiki/John_Snow) [Wellcome Library via wikimedia](https://w.wiki/QtV)"
---
<!-- Übungsaufgabe 04: Kennzahlen, Verteilungen, Fehlwerte, Relationen -->
## Übungsaufgabe 04

In dieser Übungsaufgabe wenden Sie das Gelernte aus Lernabschnitt 04 selbstständig an. Grundlage ist erneut `Abschlusstest_Datensatz.xlsx` (Tabellenblatt „Testdaten").

---

**1.** Berechnen Sie mit `=MITTELWERT(...)` den Mittelwert der **unbereinigten** Temperaturspalte (Rohdaten, ohne vorherige Korrektur von Platzhaltern). Wie lautet das Ergebnis (auf 2 Nachkommastellen)?

**2.** Berechnen Sie mit `=MEDIAN(...)` den Median derselben unbereinigten Spalte. Wie lautet das Ergebnis?

**3.** Wie viele Zellen der Spalte `Temperatur` werden von `MITTELWERT`/`MEDIAN` überhaupt als Zahl berücksichtigt (Rohdaten, vor jeder Bereinigung)?

**4.** Wie viele **echte leere Zellen** enthält die Spalte `Temperatur`?

**5.** Wie viele Zellen enthalten den Text `"NA"`?

**6.** Wie viele Zellen enthalten den Platzhalterwert `-999`?

**7.** Wie viele Zellen enthalten eine verdächtige `0`?

**8.** Ersetzen Sie `-999` und die verdächtige `0` durch echte Lücken. Wie lautet der Mittelwert der Temperaturspalte jetzt (auf 2 Nachkommastellen)?

**9.** Wie lautet der Median der bereinigten Temperaturspalte (nach Schritt 8)?

**10.** Berechnen Sie für die bereinigte Temperaturspalte das 1. und 3. Quartil (`QUARTILE.INKL`). Welche beiden Werte erhalten Sie?

**11.** Erstellen Sie einen Boxplot der bereinigten Temperaturwerte, gruppiert nach Standort. Bei welchem Standort zeigt sich ein deutlicher, aber **echter** (kein Platzhalter-)Ausreißer?

**12.** Erstellen Sie ein Histogramm der bereinigten Temperaturwerte. Was bewirkt eine zu große Bin-Breite im Vergleich zu einer zu kleinen?

**13.** Warum ist ein Mittelwert für die Variable `Temperatur` sinnvoll berechenbar, für die Variable `Standort` aber nicht?

**14.** Erstellen Sie ein Streudiagramm mit `Datum` auf der x-Achse und `Temperatur` auf der y-Achse für die Station `Wilhelm-Roser-Str.`. Was fällt beim eingebauten Ausreißer im zeitlichen Kontext auf (Jahreszeit)?

**15.** Warum sollten Sie einen im Boxplot sichtbaren Ausreißer nicht vorschnell aus Ihrer Auswertung löschen, sondern die Entscheidung dokumentieren?
