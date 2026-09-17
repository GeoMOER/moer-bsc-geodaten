---
title: Textfunktionen – Vertiefung
published: true
toc: true
header:
  image: /assets/images/unit02/31031723265_0890cd9547_o.jpg
  image_description: "Cloudscape Over the Philippine Sea"
  caption: "Image: [NASA's Marshall Space Flight Center](https://www.nasa.gov/centers/marshall/home/index.html) [CC BY-NC 2.0] via [flickr.com](https://www.flickr.com/photos/nasamarshall/31031723265/)"
---

Im letzten Kapitel haben Sie mit `TEIL`, `FINDEN` und `WERT` einen zusammengesetzten Text in seine Zahlen-Bestandteile zerlegt. Jetzt drehen wir die Richtung um: Sie berechnen zunächst mit den mathematischen Funktionen aus dem vorletzten Kapitel neue Werte und stellen diese anschließend mit weiteren Textfunktionen in einer lesbaren Form dar.

<!-- Hinweis zur Excel-Version: Alle in diesem Kapitel gezeigten Textfunktionen sind in allen aktuellen Excel-Versionen identisch verfügbar. -->

## Weitere Textfunktionen im Überblick

| Funktion | Zweck | Beispiel |
|---|---|---|
| `GLÄTTEN(Text)` | Entfernt überflüssige Leer- und Zwischenraumzeichen | `GLÄTTEN("  50  ")` → `"50"` |
| `LÄNGE(Text)` | Gibt die Anzahl der Zeichen eines Texts zurück | `LÄNGE("Firmaneiplatz")` → `13` |
| `GROSS(Text)` | Wandelt Text vollständig in Großbuchstaben um | `GROSS("firmaneiplatz")` → `"FIRMANEIPLATZ"` |
| `SUCHEN(Suchtext; Text)` | Findet die Position eines Zeichens, **Groß-/Kleinschreibung wird ignoriert** | `SUCHEN("f";"Firmaneiplatz")` → `1` |
| `FINDEN(Suchtext; Text)` | Findet die Position eines Zeichens, **Groß-/Kleinschreibung wird beachtet** | `FINDEN("f";"Firmaneiplatz")` → `9` (das kleine „f", nicht das große „F") |
| `IDENTISCH(Wert1; Wert2)` | Prüft, ob zwei Texte **exakt** übereinstimmen (inkl. Groß-/Kleinschreibung) | `IDENTISCH("Text";"text")` → `FALSCH` |
| `LINKS(Text; Anzahl_Zeichen)` | Extrahiert die ersten `n` Zeichen von links | `LINKS("Firmaneiplatz";4)` → `"Firm"` |
| `RECHTS(Text; Anzahl_Zeichen)` | Extrahiert die letzten `n` Zeichen von rechts | `RECHTS("Firmaneiplatz";4)` → `"latz"` |
| `TEIL(Text; Start; Länge)` | Extrahiert einen Ausschnitt aus der Mitte (bereits bekannt) | `TEIL("Firmaneiplatz";2;3)` → `"irm"` |

**Wichtiger Unterschied `SUCHEN` vs. `FINDEN`:** Beide Funktionen liefern eine Zeichenposition, unterscheiden sich aber genau in dem einen Punkt, der in der Tabelle oben auffällt: `SUCHEN` behandelt Groß- und Kleinbuchstaben als gleich, `FINDEN` unterscheidet sie. Wählen Sie je nach Anwendungsfall bewusst die passende Funktion.

**`IDENTISCH` statt `=`:** Der einfache Vergleich `A1=A2` behandelt `"Text"` und `"text"` in Excel meist als gleich. Wenn Sie dagegen wirklich prüfen wollen, ob zwei Texte inklusive Groß-/Kleinschreibung exakt übereinstimmen, brauchen Sie `IDENTISCH`.

## Übung: Koordinaten als Gradminuten darstellen

Sie erhalten die Datei `Stationskoordinaten.xlsx` mit den Dezimalgrad-Koordinaten aller sechs Marburger Sensorstationen. Diese sollen für eine ansehnlichere Ausgabe in **Gradminuten** dargestellt werden. Zur Vereinfachung vernachlässigen wir die Gradsekunden und bearbeiten nur die geografische Breite (`Latitude`).

**Schritt 1 – Gradzahl berechnen:**
Die Gradzahl ist die Ganzzahl der Dezimalzahl (alle Nachkommastellen abgeschnitten, nicht gerundet):
```
=GANZZAHL(B2)
```

**Schritt 2 – Dezimalen Minutenüberhang berechnen:**
Der Überhang ergibt sich aus der Differenz zwischen der ursprünglichen Koordinate und ihrer (abgeschnittenen) Gradzahl:
```
=B2-GANZZAHL(B2)
```

**Schritt 3 – In Gradminuten umrechnen:**
Die Gradminuten `x` errechnen Sie aus dem dezimalen Minutenüberhang `ϑ` per Dreisatz — dazu wird `ϑ` mit 60 multipliziert:
```
=D2*60
```
(wobei `D2` die Zelle mit dem Minutenüberhang aus Schritt 2 ist)

**Schritt 4 – Runden:**
Runden Sie den so berechneten Wert auf **null Nachkommastellen**:
```
=RUNDEN(D2*60;0)
```

Legen Sie für jeden dieser vier Schritte eine eigene Spalte mit sinnvoller Überschrift an (`Grad`, `Minuten_Dezimal`, `Minuten_x60`, `Gradminuten`).

## Übung: Textliche Darstellung

Stellen Sie nun Gradzahl und Gradminuten für jede Station in der üblichen Form (`50° 49'`) in einer **neuen Spalte** dar. Nutzen Sie dafür eine **Textverkettung** Ihrer bereits berechneten Zahlenspalten:

```
=E2&"° "&F2&"'"
```

Dabei ist `E2` Ihre Gradspalte und `F2` Ihre Gradminuten-Spalte aus der vorherigen Übung; das kaufmännische Und-Zeichen `&` verkettet Text und Zahlenwerte zu einem gemeinsamen Textstring.

**Kontrolle:** Prüfen Sie mit `LÄNGE(...)`, ob alle Einträge Ihrer neuen Spalte eine plausible, einheitliche Zeichenlänge haben — ein auffällig abweichender Wert kann auf ein Problem bei einer der vorherigen Berechnungen hindeuten (z. B. eine einstellige statt zweistellige Gradminuten-Zahl).

<!-- Screenshot: Excel-Tabelle mit Spalten Standort, Latitude, Grad, Minuten_Dezimal, Minuten_x60, Gradminuten und einer letzten Spalte "Darstellung" mit Werten wie "50° 49'", jede Formel in der Bearbeitungsleiste sichtbar. -->

*(Zeitbedarf: ca. 10 Minuten für beide Übungen zusammen)*

## Additional resources
