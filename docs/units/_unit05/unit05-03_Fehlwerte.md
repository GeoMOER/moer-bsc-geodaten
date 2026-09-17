---
title: Fehlwerte
published: true
toc: true
header:
  image: /assets/images/unit04/streuobst.jpg
  image_description: "Streuobstwiese"
  caption: "Image: ulrichstill [CC BY-SA 2.0 DE] via [wikimedia.org](https://commons.wikimedia.org/wiki/File:Tuebingen_Streuobstwiese.jpg)"
---


<!-- Kapitel 05-03: Fehlende Werte (NA) erkennen und behandeln -->

In einem über mehrere Personen und mehrere Tage erhobenen Datensatz wie Ihrem sind fehlende Werte der **Normalfall, nicht die Ausnahme**: Eine Messung wurde vergessen, ein Gerät war defekt, oder eine Angabe wurde schlicht nicht notiert. Entscheidend ist, wie Sie mit diesen Lücken umgehen – unbemerkte Fehlwerte können Kennzahlen und Diagramme erheblich verfälschen.

## Wie sieht ein Fehlwert in Excel überhaupt aus?

Das ist tückischer, als es zunächst scheint – **drei verschiedene Zustände** werden oft verwechselt:

| Zustand | Aussehen | Von Excel-Funktionen wie behandelt |
|---|---|---|
| Echte leere Zelle | Zelle wurde nie befüllt | wird von `MITTELWERT`, `SUMME` etc. automatisch ignoriert |
| Text `"NA"` oder `"k.A."` eingetragen | Zelle enthält sichtbaren Text | führt bei numerischen Funktionen zu **Fehlern** oder wird ignoriert, je nach Funktion – uneinheitlich! |
| Zahl `0` eingetragen, obwohl eigentlich kein Wert gemessen wurde | Zelle sieht aus wie ein gültiger Messwert | wird **mitgerechnet** wie ein echter Wert – verfälscht Mittelwert und Streuung erheblich, ohne dass ein Fehler angezeigt wird |

**Die gefährlichste Variante ist die dritte:** Eine `0` anstelle eines fehlenden Temperaturwerts sieht für Excel wie eine gültige Messung von `0 °C` aus und wird ganz normal in den Mittelwert eingerechnet – ein stiller, aber erheblicher Fehler, der beim bloßen Betrachten der Tabelle nicht auffällt.

<!--**Screenshot 33:** Tabellenausschnitt mit einer Temperaturspalte, in der eine Zelle eine `0` enthält (rot markiert als Warnhinweis), daneben zum Vergleich eine tatsächlich leere Zelle – mit einer Anmerkung/Sprechblase „Sieht aus wie ein Messwert, ist aber vermutlich ein fehlender Wert!" -->

**Empfehlung:** Legen Sie sich bereits **vor** der Dateneingabe eine einheitliche Konvention fest – fehlende Werte am besten als leere Zelle lassen (nicht als `0`, nicht als Text `"NA"`), da dies von den meisten Excel-Funktionen automatisch korrekt ignoriert wird. Falls Sie kennzeichnen möchten, *warum* ein Wert fehlt, nutzen Sie dafür eine **separate Spalte** (z. B. `Anmerkung`), statt die Information in die Wertespalte selbst zu schreiben.

<!-- Ergänzung zu Kapitel 05-03: Fehlende Werte -->

## Fehlwerte, die absichtlich anders codiert wurden

Neben leeren Zellen, Text (`"NA"`) und versehentlichen Nullen gibt es eine vierte, besonders tückische Variante: **Platzhalterwerte**, die bewusst als Zahl codiert wurden, um einen fehlenden Wert zu kennzeichnen – etwa `-999`, `9999` oder `-1`. Solche Codes stammen häufig aus Messgeräten, Sensoren oder älteren Datenerfassungssystemen, bei denen aus technischen Gründen kein Text, sondern nur ein numerischer Wert gespeichert werden konnte.

**Warum das besonders gefährlich ist:** Ein Wert wie `-999` sieht für Excel wie ein ganz normaler, gültiger Zahlenwert aus und wird anstandslos in Mittelwert, Summe oder Boxplot miteingerechnet – mit drastischen Auswirkungen. Eine einzelne `-999` in einer Temperaturspalte reißt den Mittelwert massiv nach unten und lässt im Boxplot einen dramatischen, aber inhaltlich bedeutungslosen Ausreißer entstehen.

<!-- **Screenshot 38:** Boxplot einer Temperaturspalte mit einem extremen Ausreißer weit unterhalb aller anderen Werte (z. B. bei `-999`, während alle übrigen Werte zwischen 0 und 20 °C liegen), mit einer Anmerkung „Kein echter Messwert – Platzhalter für fehlende Messung!".
-->

**Woher weiß man, dass ein Wert ein Platzhalter ist und kein echter Messwert?**
- **Physikalisch unmögliche oder unrealistische Werte:** Eine Lufttemperatur von `-999 °C` ist physikalisch unmöglich (absoluter Nullpunkt liegt bei etwa −273 °C) – ein klares Signal für einen Platzhalter
- **Auffällig runde oder wiederkehrende Zahlen:** Werte wie `9999`, `-1` oder `0` (in einem Kontext, in dem `0` keinen realistischen Messwert darstellt) tauchen oft **mehrfach identisch** auf, während echte Messwerte natürlich variieren
- **Dokumentation der Datenquelle prüfen:** Wenn Sie Daten von einem Gerät, einer Website oder einer anderen Person erhalten, fragen Sie nach oder prüfen Sie eine Dokumentation, ob und welcher Platzhaltercode für fehlende Werte verwendet wurde – verlassen Sie sich nicht allein auf das Erkennen „von Auge"

**Umgang mit Platzhalterwerten in Excel:**

1. **Auffinden:** Nutzen Sie den Filter oder `Strg`+`F`, um nach dem vermuteten Platzhalterwert (z. B. `-999`) zu suchen, oder prüfen Sie Minimum/Maximum Ihrer Spalte auf unrealistische Extremwerte (`=MIN(Bereich)` – ein Ergebnis von `-999` bei Temperaturdaten ist ein klares Warnsignal)
2. **In echte Fehlwerte umwandeln:** Nutzen Sie `Strg`+`H` (Suchen & Ersetzen), um den Platzhalterwert gezielt durch **nichts** zu ersetzen (Feld „Ersetzen durch" leer lassen) – dadurch wird die Zelle wieder echt leer, statt einen falschen Zahlenwert zu enthalten
3. **Kontrolle:** Prüfen Sie nach dem Ersetzen erneut Minimum und Maximum der Spalte, um sicherzugehen, dass keine weiteren Platzhalterwerte übersehen wurden

**Wichtig – Protokollierung:** Auch das Ersetzen von Platzhalterwerten ist eine inhaltliche Entscheidung, die dokumentiert werden sollte: Welcher Code (`-999`, `9999`, …) wurde durch einen echten Fehlwert ersetzt, in welcher Spalte, und wie viele Zellen waren betroffen? Diese Angaben gehören – wie bereits bei Ausreißern erwähnt – in die Dokumentation, die im späteren Kapitel zur Protokollierung vertieft wird.

**Kurzcheck:** Prüfen Sie mit `=MIN(...)` und `=MAX(...)` Ihre eigene Temperatur- und Luftdruckspalte auf unrealistische Extremwerte, die auf einen versteckten Platzhaltercode hindeuten könnten.


## Fehlwerte zählen und lokalisieren

Bevor Sie überhaupt mit den Daten rechnen, sollten Sie sich einen Überblick verschaffen, **wie viele** Werte fehlen und **wo**:

| Funktion | Zweck |
|---|---|
| `=ANZAHL(Bereich)` | zählt nur Zellen mit **Zahlen** |
| `=ANZAHL2(Bereich)` | zählt alle **nicht-leeren** Zellen (Zahlen und Text) |
| `=ANZAHLLEEREZELLEN(Bereich)` | zählt **leere** Zellen im Bereich |

**Fehlende Werte pro Station zählen:** Mit `ZÄHLENWENNS` lässt sich das direkt lösen:

```
=ZÄHLENWENNS(Standort_Bereich;"Firmaneiplatz";Temperatur_Bereich;"")
```


Diese Formel zählt, wie viele Zeilen mit `Standort = "Firmaneiplatz"` gleichzeitig eine leere Temperaturspalte haben.

**Übersichtlicher: eine kleine Fehlwert-Übersichtstabelle je Station**

| Standort | Anzahl Messungen gesamt | Davon fehlend (Temperatur) | Anteil fehlend |
|---|---|---|---|
| Firmaneiplatz | `=ZÄHLENWENN(Standort_Bereich;"Firmaneiplatz")` | `=ZÄHLENWENNS(Standort_Bereich;"Firmaneiplatz";Temperatur_Bereich;"")` | `=C2/B2` (als Prozent formatiert) |

<!-- **Screenshot 34:** Kleine Excel-Übersichtstabelle mit Spalten „Standort", „Anzahl Messungen gesamt", „Davon fehlend", „Anteil fehlend (%)", für 3–4 Stationen, wobei eine Zeile mit auffällig hohem Anteil fehlender Werte (z. B. 40 %) farblich hervorgehoben ist (bedingte Formatierung). -->

**Ausblick:** Es gibt in Excel ein deutlich schnelleres Werkzeug, um solche Übersichten auf Knopfdruck statt mit einzelnen Formeln zu erstellen – die **Pivot-Tabelle**, die Sie in einem späteren Kapitel kennenlernen. Für den Moment reicht die manuelle Lösung über Formeln völlig aus.

## Wenn Sie fehlende Werte in der Auswertung ausschließen

Sobald Sie z. B. eine Station wegen zu vieler Fehlwerte aus einer Auswertung herausnehmen, oder Zeilen mit fehlenden Werten filtern, ist das eine **inhaltliche Entscheidung**, die das Ergebnis beeinflusst.

> **Wichtig – Protokollierung:** Halten Sie fest, **welche Station oder Zeilen** Sie ausgeschlossen haben und **warum** (z. B. „Station X: nur 3 von 20 erwarteten Messungen vorhanden, daher aus Mittelwertberechnung ausgeschlossen"). Auch dieser Aspekt gehört zur sauberen Dokumentation Ihrer Arbeit, die im späteren Kapitel zur Protokollierung noch vertieft wird – ohne eine solche Notiz ist Ihre Auswertung für andere (und für Sie selbst nach einigen Wochen) nicht mehr nachvollziehbar.

