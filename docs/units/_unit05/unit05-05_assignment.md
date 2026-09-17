--- 
title: ÜA | Übungsaufgabe Abschnitt 05
published: true
toc: true
header:
  image: /assets/images/01-splash.jpg
  image_description: "Dr. John Snow's map"
  caption: "Map: [**Dr. John Snow**](https://en.wikipedia.org/wiki/John_Snow) [Wellcome Library via wikimedia](https://w.wiki/QtV)"
---
<!-- Übungsaufgabe 05: Kennzahlen, Verteilungen, Fehlwerte, Relationen -->
## Übungsaufgabe 05

In dieser Übungsaufgabe wenden Sie das Gelernte aus Lernabschnitt 05 selbstständig an. Grundlage ist erneut `Abschlusstest_Datensatz.xlsx` (Tabellenblatt „Testdaten").

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

<!-- Musterlösung (nicht für Studierende sichtbar):
1. -33,14
2. 24,91
3. 19
4. 1
5. 1
6. 1
7. 1
8. 21,73
9. 25,41
10. Q1 = 20,33; Q3 = 26,04
11. Wilhelm-Roser-Str. (26,04 °C im Februar, deutlich ueber den uebrigen Werten von 8-9 °C dieser Station)
12. Zu grosse Bin-Breite verschleiert Muster (alles in 2-3 Balken), zu kleine erzeugt ein zerklueftetes, kaum interpretierbares Bild
13. Standort ist nominalskaliert (keine Rangfolge, keine rechenbaren Abstaende), Temperatur ist intervallskaliert und damit rechenfaehig
14. Der Ausreisserwert (26,04 °C) tritt im Februar auf, waehrend die uebrigen Werte dieser Station (8-9 °C) fuer die Jahreszeit plausibel sind - ein winterlicher Wert von ueber 26 °C ist unrealistisch und sollte inhaltlich hinterfragt werden
15. Ein Ausreisser ist zunaechst nur eine statistische Auffaelligkeit, kein Beweis fuer einen Messfehler; ohne Dokumentation der Ausschluss-Entscheidung ist die Auswertung fuer andere (und einen selbst später) nicht mehr nachvollziehbar
-->
