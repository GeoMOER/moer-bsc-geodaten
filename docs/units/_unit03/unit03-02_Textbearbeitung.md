---
title: Textbearbeitung
published: true
toc: true
header:
  image: /assets/images/unit02/31031723265_0890cd9547_o.jpg
  image_description: "Cloudscape Over the Philippine Sea"
  caption: "Image: [NASA's Marshall Space Flight Center](https://www.nasa.gov/centers/marshall/home/index.html) [CC BY-NC 2.0] via [flickr.com](https://www.flickr.com/photos/nasamarshall/31031723265/)"
---


Ihre Sensordaten enthalten eine Spalte `Koordinaten_roh` bzw. `Koordinaten`, in der mehrere Informationen in einem einzigen Text zusammengefasst sind, z. B. `50°48'51.43"N, 8°46'19.85"E`. Das ist ein Muster, das Ihnen bei importierten oder von Geräten exportierten Daten häufig begegnen wird: verschiedene Informationen stecken in einer einzigen Zelle und müssen zunächst technisch getrennt werden, bevor man mit ihnen weiterarbeiten kann.

**Was diese Zahlen genau bedeuten und wie man daraus eine Position auf der Erde bestimmt, behandeln wir ausführlich in einem späteren Lernabschnitt zu Geodaten.** Hier lernen Sie zunächst nur das Handwerkszeug: die Textfunktionen, mit denen sich ein solcher zusammengesetzter Text in Excel in seine Bestandteile zerlegen lässt. Diese Funktionen werden Ihnen auch bei ganz anderen Textspalten wieder begegnen (siehe Kapitel zur Datenbereinigung).

<!-- Hinweis zur Excel-Version: Die Textfunktionen TEIL, FINDEN, WERT und GLÄTTEN sind in allen aktuellen Excel-Versionen identisch verfügbar. -->

## Grundlegende Textfunktionen

| Funktion | Zweck | Beispiel |
|---|---|---|
| `TEIL(Text; Start; Länge)` | Extrahiert einen Ausschnitt aus der Mitte eines Texts, ab einer bestimmten Position, mit einer bestimmten Länge | `TEIL("50°48'51.43\"N";1;2)` → `"50"` |
| `FINDEN(Suchtext; Text)` | Findet die *Position* eines bestimmten Zeichens innerhalb eines Texts | `FINDEN("°";"50°48'51.43\"N")` → `3` |
| `WERT(Text)` | Wandelt einen Text, der wie eine Zahl aussieht, in eine echte, rechenfähige Zahl um | `WERT("50")` → `50` |
| `GLÄTTEN(Text)` | Entfernt überflüssige Leer- und Zwischenraumzeichen | `GLÄTTEN("  50 ")` → `"50"` |

**Warum `FINDEN` und `TEIL` meist gemeinsam auftreten:** `TEIL` braucht eine feste Startposition und Länge – die kennen Sie bei unterschiedlich langen Texten aber oft nicht im Voraus. `FINDEN` liefert genau diese Position, indem es nach einem bestimmten Trennzeichen sucht (hier z. B. `°`, `'` oder `"`). Die Kombination beider Funktionen ist deshalb ein Standardmuster: **erst die Position finden, dann an dieser Position den Text herausschneiden.**

## Textfunktionen anwenden – Schritt für Schritt

Nehmen wir den Wert `50°48'51.43"N` (aus Ihrer Spalte `Koordinaten_roh`, Zelle `B2`) als Übungsbeispiel für das Zerlegen eines zusammengesetzten Texts:

**Schritt 1 – Ersten Teil extrahieren (vor dem `°`):**
```
=TEIL(B2;1;FINDEN("°";B2)-1)
```
`FINDEN("°";B2)` liefert die Position des `°`-Zeichens (hier: `3`). `TEIL` schneidet davon alles **vor** dieser Position heraus, also die ersten beiden Zeichen: `"50"`.

**Schritt 2 – Mittleren Teil extrahieren (zwischen `°` und `'`):**
```
=TEIL(B2;FINDEN("°";B2)+1;FINDEN("'";B2)-FINDEN("°";B2)-1)
```
Hier wird die Startposition um eins **hinter** das `°`-Zeichen gelegt, und die Länge ergibt sich aus dem Abstand zwischen den beiden Positionen von `°` und `'`.

**Schritt 3 – In eine echte Zahl umwandeln:**
```
=WERT(TEIL(B2;1;FINDEN("°";B2)-1))
```
Ohne `WERT` bliebe das Ergebnis von `TEIL` immer **Text** – auch wenn es wie eine Zahl aussieht. Erst `WERT` macht daraus eine Zahl, mit der Sie z. B. `MITTELWERT` oder eine weitere Berechnung durchführen könnten.

<!-- Screenshot: Excel-Tabelle mit Spalte Koordinaten_roh und daneben drei Hilfsspalten "Teil 1", "Teil 2", "Teil 3", in denen schrittweise mit TEIL und FINDEN einzelne Textabschnitte extrahiert werden - jede Hilfsspalte mit sichtbarer Formel in der Bearbeitungsleiste. -->

## Achtung – Formatfehler innerhalb der Spalte

Wenn Sie Ihre Formeln auf die **gesamte Spalte** `Koordinaten_roh` anwenden, werden Sie vermutlich bei einer Zeile ein unplausibles Ergebnis erhalten: Eine der Koordinaten enthält einen **Tippfehler im Format** – ein einfaches Hochkomma `'` anstelle des Anführungszeichens `"`. Diese Art Fehler passiert in der Praxis häufig (unterschiedliche Tastaturlayouts, Copy-Paste aus verschiedenen Quellen) und fällt beim bloßen Betrachten der Zelle kaum auf.

**Vorgehen bei so einem Fehler:**
1. Identifizieren Sie die betroffene Zeile (die Formel liefert dort `#WERT!` oder ein offensichtlich falsches Ergebnis)
2. Prüfen Sie den Original-Text in der Zelle genau – zählen Sie die Anführungszeichen/Hochkommas
3. Korrigieren Sie den Tippfehler manuell in der Ursprungsspalte, bevor Sie die Formel erneut anwenden

<!-- Screenshot: Excel-Tabelle mit einer Zeile, in der die Formel #WERT! anzeigt, daneben die Ursprungszelle mit dem fehlerhaften Text 50°50'16.5'N (zwei Hochkommas statt Grad-Minuten-Sekunden-Zeichen). -->

---

## Übung: Textfunktionen an den Sensordaten üben

Arbeiten Sie weiter mit Ihrer Arbeitsmappe aus den letzten Kapiteln (Blatt `Datensatz_1`, Spalte `Koordinaten_roh` bzw. Blatt `Datensatz_2`, Spalte `Koordinaten`).

1. Legen Sie auf **beiden** Blättern je drei Hilfsspalten an und extrahieren Sie mit `TEIL`/`FINDEN` schrittweise die drei Zahlen-Anteile (Grad, Minuten, Sekunden) aus der jeweiligen Koordinatenspalte – zunächst nur für eine einzelne Zeile.
2. Wandeln Sie jeden der drei extrahierten Textwerte mit `WERT` in eine echte Zahl um. Prüfen Sie an der Ausrichtung (rechtsbündig = Zahl), ob die Umwandlung funktioniert hat.
3. Ziehen Sie Ihre Formeln über die gesamte jeweilige Spalte. Identifizieren Sie die Zeile mit dem Formatfehler und korrigieren Sie den Tippfehler in der Ursprungsspalte.
4. Speichern Sie Ihre Datei – Sie arbeiten in den kommenden Kapiteln mit denselben Hilfsspalten weiter.

**Reflexionsfrage:** An welcher Stelle Ihrer Formeln hätte sich der Formatfehler (`'` statt `"`) auf das Ergebnis auswirken müssen – auch ohne dass Sie bereits wissen, was die einzelnen Zahlenanteile inhaltlich bedeuten?

> Im nächsten Kapitel lernen Sie weitere Textfunktionen kennen und stellen damit Koordinaten in einer lesbaren Form dar.
