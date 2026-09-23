---
title: Rechnen und Zellbezüge
published: true
toc: true
header:
  image: /assets/images/unit02/31031723265_0890cd9547_o.jpg
  image_description: "Cloudscape Over the Philippine Sea"
  caption: "Image: [NASA's Marshall Space Flight Center](https://www.nasa.gov/centers/marshall/home/index.html) [CC BY-NC 2.0] via [flickr.com](https://www.flickr.com/photos/nasamarshall/31031723265/)"
---

Excel ist im Kern ein programmierbarer Taschenrechner: Jede Zelle kann eine feste Zahl enthalten – oder eine **Formel**, die aus anderen Zellen einen Wert berechnet. Bevor wir mit Textfunktionen oder Statistik weiterarbeiten, brauchen Sie dafür zwei Grundlagen: wie Excel rechnet, und wie sich eine Formel auf andere Zellen bezieht.

<!-- Hinweis zur Excel-Version: Rechenoperatoren und Zellbezüge (relativ/absolut) sind in allen aktuellen Excel-Versionen identisch. -->

## Themenüberschrift 01: Mathematische Operatoren

| Operation | Zeichen | Beispiel |
|---|---|---|
| Addition | `+` | `=2+3` |
| Subtraktion | `-` | `=5-2` |
| Multiplikation | `*` | `=4*6` |
| Division | `/` | `=10/4` |
| Potenz | `^` | `=2^3` (= 8) |

Jede Formel beginnt mit einem Gleichheitszeichen `=` – ohne dieses interpretiert Excel die Eingabe als Text oder Zahl, nicht als Formel.

**Rechenreihenfolge:** Excel rechnet nach der bekannten Regel „Punkt vor Strich" und wertet von links nach rechts aus. Für Ausnahmen von dieser Reihenfolge nutzen Sie Klammern:

```
=2+3*4      → 14  (zuerst 3*4, dann +2)
=(2+3)*4    → 20  (Klammer erzwingt die Addition zuerst)
```

## Übung: Taschenrechner-Funktionalität

Probieren Sie die Taschenrechner-Funktionalität von Excel aus. Blenden Sie dazu über **Formeln → Formeln anzeigen** (oder `Strg`+`#`) die Formelansicht ein und wieder aus, um zu sehen, wie sich angezeigtes Ergebnis und tatsächliche Formel unterscheiden.

Beantworten Sie folgende Fragen, indem Sie die passende Formel direkt in eine Zelle eintippen:

1. Wie viel Grad Celsius entsprechen `298,15` Kelvin? (Die Kelvin-Skala beginnt beim absoluten Nullpunkt `-273,15 °C` mit `0 K`.)
2. `25 °C` entsprechen `25 * 9/5 + 32` Fahrenheit: Wie viel Fahrenheit sind das?

<!-- Screenshot 6: Excel-Zelle mit der Formel =25*9/5+32 in der Bearbeitungsleiste, das berechnete Ergebnis 77 in der Zelle sichtbar; daneben zum Vergleich dieselbe Tabelle mit eingeblendeter Formelansicht (Strg+#), in der statt Ergebnissen die Formeln selbst in den Zellen sichtbar sind.
Markdownlösung: ![Screenshot einer Excel-Zelle mit der Formel =25*9/5+32 in der Bearbeitungsleiste und zum Vergleich dieselbe Tabelle mit eingeblendeter Formelansicht.]({{ '/assets/images/unit02/Screenshot06_Excel.png' | relative_url }})
Oder als HTML (lightbox) mit Vergrößerungsoption, Beschreibungstext beim Hovern und Galerie zum durchklicken:-->

<a href="{{ '/assets/images/unit02/Screenshot06_Excel.png' | relative_url }}" 
   data-lightbox="Screenshot06_Excel" 
   title="Screenshot einer Excel-Zelle mit der Formel =25*9/5+32 in der Bearbeitungsleiste und zum Vergleich dieselbe Tabelle mit eingeblendeter Formelansicht.">
  <img src="{{ '/assets/images/unit02/Screenshot06_Excel.png' | relative_url }}" alt="Screenshot einer Excel-Zelle mit der Formel =25*9/5+32 in der Bearbeitungsleiste und zum Vergleich dieselbe Tabelle mit eingeblendeter Formelansicht.">
</a>

<!--Anmerkung von Lisa S.: Ich habe "Strg+#" ausprobiert aber die Ansicht hat nicht gewechselt. -->

## Themenüberschrift 02: Variable Werte über Zellbezüge

Eine Formel kann sich auch auf den Inhalt anderer Zellen beziehen, statt feste Zahlen zu enthalten. Das wird als **Zellbezug** bezeichnet – und ist der eigentliche Grund, warum Tabellenkalkulation so mächtig ist: Ändert sich der Wert einer Zelle, aktualisiert sich automatisch jede Formel, die sich darauf bezieht.

- **Bezug auf eine einzelne Zelle:** die Zellbezeichnung selbst, z. B. `C1`
- **Bezug auf einen zusammenhängenden Zellbereich:** getrennt durch Doppelpunkt, z. B. `C2:E2`

Statt `=25*9/5+32` können Sie also schreiben: `=A2*9/5+32`, wobei `A2` die Temperatur in Celsius enthält. Der Vorteil: Dieselbe Formel funktioniert für jede beliebige Temperatur, ohne dass Sie sie neu eintippen müssen.

## Übung: Relativer Zellbezug

Nutzen Sie Ihre Arbeitsmappe mit `Datensatz_1` aus dem letzten Kapitel.

Berechnen Sie die Temperatur zusätzlich in **Fahrenheit** – dieselbe Umrechnung, die Sie bereits aus der Taschenrechner-Übung kennen (`°C * 9/5 + 32`), jetzt aber mit einem Zellbezug statt einer festen Zahl.

1. Legen Sie eine neue Spalte mit einer sinnvollen Überschrift an (z. B. `Temperatur (°F)`).
2. Tragen Sie für die **erste** Zeile Ihrer Tabelle eine passende Formel ein, die sich auf die Temperaturzelle derselben Zeile bezieht (z. B. `=E2*9/5+32`, falls die Temperatur in Spalte `E` steht).
3. Markieren Sie die Zelle mit Ihrer Formel und ziehen Sie sie am kleinen Quadrat unten rechts (dem „Ausfüllkästchen") über alle folgenden Zeilen der Tabelle – das ist **relatives Kopieren**.
4. Prüfen Sie in der Bearbeitungsleiste, wie sich der Zellbezug in den kopierten Formeln automatisch angepasst hat (aus `E2` wird z. B. `E3`, `E4`, …).

**Warum das „relativ" heißt:** Excel merkt sich beim Kopieren nicht die absolute Zelladresse, sondern die **Position relativ** zur Formelzelle ("die Zelle eine Spalte links, in derselben Zeile"). Genau deshalb passt sich der Bezug beim Kopieren automatisch an.

## Übung: Absoluter Zellbezug

Um Ihre Formel flexibler zu machen – z. B. um die Umrechnungskonstanten jederzeit an einer einzigen Stelle ändern zu können, ohne jede Formel einzeln anzupassen – verwenden Sie jetzt den **absoluten Zellbezug**.

1. Tragen Sie die Werte `9/5` (als Dezimalzahl `1,8`) und `32` in zwei einzelne Zellen oben rechts neben dem Tabellenkopf ein (z. B. `G1` für den Faktor, `G2` für den Offset), mit kurzer Beschriftung daneben.
2. Erstellen Sie in einer weiteren Spalte erneut eine Fahrenheit-Formel, die sich diesmal aber **nicht** auf die festen Zahlen `1,8`/`32`, sondern auf Ihre beiden neuen Zellen bezieht.
3. Setzen Sie vor Spalte **und** Zeile dieser beiden Zellbezüge ein Dollarzeichen, z. B. `$G$1` und `$G$2` (Tastenkürzel: Zelle in der Formel markieren, dann `F4` drücken).
4. Kopieren Sie die Formel wie zuvor über alle Zeilen. Prüfen Sie: Bleibt der Bezug auf `$G$1`/`$G$2` beim Kopieren unverändert, während sich der Bezug auf die Temperaturspalte weiterhin anpasst?

**Warum das „absolut" heißt:** Das Dollarzeichen „fixiert" Spalte bzw. Zeile eines Bezugs – dieser Teil ändert sich beim Kopieren **nicht**, egal wohin die Formel kopiert wird. Ohne das Dollarzeichen würde sich `G1` beim Kopieren nach unten ebenso verschieben wie `E2` – und würde in Zeile 3 plötzlich auf eine leere Zelle `G2` statt auf Ihre Konstante zeigen.

5. Kopieren Sie nun **nur** die Spalte mit Ihrer Fahrenheit-Formel auf ein zweites Tabellenblatt (z. B. `Datensatz_2`). Was passiert mit dem Ergebnis? Woran liegt das, und wie lösen Sie die Situation?

<!-- Screenshot 7: Excel-Tabelle mit den Konstanten (Faktor, Offset) in den Zellen G1/G2 oben rechts, daneben eine Formel in der Bearbeitungsleiste mit den absoluten Bezügen $G$1 und $G$2 sowie dem relativen Bezug auf die Temperaturspalte; zum Vergleich dasselbe nach dem Kopieren auf ein zweites Tabellenblatt, auf dem die Formel einen Fehler oder ein falsches Ergebnis zeigt, da die Konstanten dort fehlen.
Markdownlösung: ![Screenshot zweier Excel-Tabellen mit und ohne Zellbezug.]({{ '/assets/images/unit02/Screenshot07_Excel.png' | relative_url }})
Oder als HTML (lightbox) mit Vergrößerungsoption, Beschreibungstext beim Hovern und Galerie zum durchklicken:-->

<a href="{{ '/assets/images/unit02/Screenshot07_Excel.png' | relative_url }}" 
   data-lightbox="Screenshot07_Excel" 
   title="Screenshot zweier Excel-Tabellen mit und ohne Zellbezug.">
  <img src="{{ '/assets/images/unit02/Screenshot07_Excel.png' | relative_url }}" alt="Screenshot zweier Excel-Tabellen mit und ohne Zellbezug.">
</a>

**Lösungshinweis (nicht vorab verraten, ggf. als Tipp nutzen):** Wird nur die Formel-Spalte kopiert, ohne die Zellen `G1`/`G2` mit auf das neue Blatt zu übernehmen, verweist `$G$1`/`$G$2` dort ins Leere oder auf andere, dort zufällig vorhandene Werte. Lösung: entweder die Konstanten auf dem Zielblatt ebenfalls bereitstellen, oder die Formel vor dem Kopieren mit **„Einfügen als Werte"** von der Formel in einen festen Zahlenwert umwandeln.

## Additional resources
