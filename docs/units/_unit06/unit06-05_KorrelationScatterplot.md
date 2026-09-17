---
title: Korrelation
published: true
toc: true
header:
  image: /assets/images/unit04/streuobst.jpg
  image_description: "Streuobstwiese"
  caption: "Image: ulrichstill [CC BY-SA 2.0 DE] via [wikimedia.org](https://commons.wikimedia.org/wiki/File:Tuebingen_Streuobstwiese.jpg)"
---

Im Kapitel „Relationen" haben Sie bereits ein Streudiagramm erstellt und optisch beurteilt, ob zwei Variablen zusammenhängen. Diesen optischen Eindruck können Sie jetzt mit einer einzelnen Kennzahl untermauern: der **Pearson-Korrelation**.

<!-- Hinweis zur Excel-Version: KORREL ist in allen aktuellen Excel-Versionen identisch verfügbar. Die ältere, gleichwertige Funktion PEARSON() existiert aus Kompatibilitätsgründen noch, liefert aber dasselbe Ergebnis wie KORREL. -->

## Die Pearson-Korrelation

Die Pearson-Korrelation (auch Korrelationskoeffizient `r` genannt) misst, wie stark ein **linearer** Zusammenhang zwischen zwei numerischen Variablen ist. Der Wert liegt immer zwischen `-1` und `1`:

| Wert von `r` | Bedeutung |
|---|---|
| `+1` | perfekter positiver Zusammenhang (steigt die eine Variable, steigt auch die andere – exakt proportional) |
| `0` | kein linearer Zusammenhang erkennbar |
| `-1` | perfekter negativer Zusammenhang (steigt die eine Variable, sinkt die andere – exakt proportional) |

**Grobe Faustregel zur Einordnung der Stärke** (unabhängig vom Vorzeichen):

| Betrag von `r` | Einordnung |
|---|---|
| unter 0,3 | kein bis sehr schwacher Zusammenhang |
| 0,3 – 0,5 | schwacher Zusammenhang |
| 0,5 – 0,7 | mittlerer Zusammenhang |
| über 0,7 | starker Zusammenhang |

Diese Grenzen sind eine grobe Orientierung, keine feste Regel – in unterschiedlichen Fachbereichen werden sie leicht unterschiedlich gezogen.

## Berechnung in Excel

```
=KORREL(Bereich1; Bereich2)
```

Beide Bereiche müssen numerisch sein und dieselbe Anzahl an Werten enthalten – bei fehlenden Werten (siehe Kapitel „Fehlwerte") ignoriert `KORREL` Zeilen, in denen mindestens einer der beiden Werte fehlt.

**Beispiel:** Um zu prüfen, ob die Temperatur im Tagesverlauf mit der Uhrzeit zusammenhängt:

```
=KORREL(Uhrzeit_Bereich; Temperatur_Bereich)
```

## Wichtig: Korrelation ist nicht dasselbe wie Kausalität

Ein hoher Korrelationswert zeigt nur, dass sich zwei Variablen **gemeinsam verändern** – er sagt nichts darüber aus, ob die eine Variable die andere **verursacht**. Zwischen Uhrzeit und Temperatur gibt es einen plausiblen inhaltlichen Zusammenhang (Sonneneinstrahlung im Tagesverlauf) – bei anderen Variablenpaaren kann eine hohe Korrelation aber auch rein zufällig oder durch eine dritte, nicht betrachtete Variable verursacht sein.

**Streudiagramm und Korrelation gemeinsam nutzen:** Verlassen Sie sich nicht allein auf den `r`-Wert – ein Streudiagramm zeigt Ihnen zusätzlich, **ob** der Zusammenhang tatsächlich linear ist. Ein `r` nahe `0` bedeutet nicht zwangsläufig "kein Zusammenhang", sondern kann auch einen **nicht-linearen** Zusammenhang verschleiern (z. B. eine U-förmige Kurve), den `KORREL` nicht erfassen kann, ein Streudiagramm aber sehr wohl sichtbar macht.

---

## Übung: Korrelation berechnen und mit dem Streudiagramm vergleichen

Nutzen Sie Ihre zusammengeführte Arbeitsmappe.

1. Wandeln Sie, falls noch nicht geschehen, Ihre Uhrzeit-Spalte in eine reine Dezimalzahl um (z. B. `12:00` → `0,5`), da `KORREL` mit numerischen Werten arbeitet.
2. Berechnen Sie mit `=KORREL(...)` den Korrelationskoeffizienten zwischen `Uhrzeit` und `Temperatur` für eine einzelne Station.
3. Ordnen Sie den erhaltenen Wert anhand der Faustregel oben ein: schwach, mittel oder stark? Positiv oder negativ?
4. Erstellen Sie zusätzlich ein Streudiagramm derselben beiden Variablen. Passt das visuelle Bild zu Ihrer Einordnung aus Schritt 3?
5. Wiederholen Sie die Berechnung für eine zweite Station. Unterscheidet sich der Korrelationswert deutlich?

**Reflexionsfrage:** Könnten zwei Variablen einen `KORREL`-Wert nahe `0` haben, obwohl im Streudiagramm ein klar erkennbares Muster sichtbar ist? Woran könnte das liegen?
