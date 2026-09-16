---
title: Wichtige Werte
published: true
toc: true
header:
  image: /assets/images/unit04/streuobst.jpg
  image_description: "Streuobstwiese"
  caption: "Image: ulrichstill [CC BY-SA 2.0 DE] via [wikimedia.org](https://commons.wikimedia.org/wiki/File:Tuebingen_Streuobstwiese.jpg)"
---

<!-- Themenblock 02-08: Lage- und Streuungsmaße -->

Um Datenqualität sicher zu stellen benötigt man auch einen zahlenbasierten Überblick. Bei **quantitativen** Daten macht es Sinn, sich mehrere Kennzahlen anzuschauen.

## Lagemaße – wo liegt die „Mitte" der Daten?

| Kennzahl | Excel-Funktion | Bedeutung | Wann sinnvoll |
|---|---|---|---|
| Mittelwert (arithmetisches Mittel) | `=MITTELWERT(Bereich)` | Summe aller Werte geteilt durch Anzahl | Bei einigermaßen gleichmäßig verteilten Daten ohne extreme Ausreißer |
| Median | `=MEDIAN(Bereich)` | Der Wert, der die sortierten Daten genau in der Mitte teilt | Robuster gegenüber Ausreißern als der Mittelwert |
| Modus (Modalwert) | `=MODUS.EINF(Bereich)` | Der am häufigsten vorkommende Wert | Sinnvoll bei kategorialen oder gehäuft wiederkehrenden Werten, bei stetigen Messwerten (wie Temperatur) selten aussagekräftig |

**Warum der Unterschied zwischen Mittelwert und Median wichtig ist:** Angenommen, Sie haben an fünf Tagen Temperaturen von `5, 6, 7, 8, 45` °C gemessen (der letzte Wert ein Messfehler oder eine Ausnahme-Hitzewelle). Der Mittelwert läge bei `14,2 °C` – ein Wert, der keinen der tatsächlichen „normalen" Tage widerspiegelt. Der Median läge bei `7 °C` und beschreibt die typische Temperatur deutlich realistischer. **Faustregel:** Bei Vermutung auf Ausreißer immer beide Kennzahlen berechnen und vergleichen – eine große Abweichung zwischen Mittelwert und Median ist selbst schon ein Hinweis auf Ausreißer in den Daten.

## Streuungsmaße – wie weit streuen die Daten?

| Kennzahl | Excel-Funktion | Bedeutung |
|---|---|---|
| Minimum | `=MIN(Bereich)` | Kleinster Wert |
| Maximum | `=MAX(Bereich)` | Größter Wert |
| Spannweite | `=MAX(Bereich)-MIN(Bereich)` | Abstand zwischen größtem und kleinstem Wert |
| Quartile | `=QUARTILE.INKL(Bereich;1)` bzw. `...;3)` | Teilen die sortierten Daten in vier gleich große Viertel; das 1. Quartil (Q1) markiert die Grenze der unteren 25 %, das 3. Quartil (Q3) die Grenze der oberen 25 % |
| Standardabweichung | `=STABW.S(Bereich)` | Durchschnittliche Abweichung der Werte vom Mittelwert |

Der **Interquartilsabstand (IQR)** — die Differenz zwischen Q3 und Q1 — beschreibt die Streuung der „mittleren" 50 % der Daten, ohne von einzelnen Extremwerten beeinflusst zu werden. Er ist die Grundlage für die Definition von Ausreißern, die Ihnen im nächsten Unterkapitel beim Boxplot wiederbegegnet.

**Kurzcheck:** Berechnen Sie für Ihre Temperaturspalte Mittelwert, Median, Minimum und Maximum. Liegen Mittelwert und Median nah beieinander, oder deutet die Abweichung bereits auf Ausreißer hin?

