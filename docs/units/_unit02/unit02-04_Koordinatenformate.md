---
title: Koordinaten
published: false
toc: true
header:
  image: /assets/images/unit02/31031723265_0890cd9547_o.jpg
  image_description: "Cloudscape Over the Philippine Sea"
  caption: "Image: [NASA's Marshall Space Flight Center](https://www.nasa.gov/centers/marshall/home/index.html) [CC BY-NC 2.0] via [flickr.com](https://www.flickr.com/photos/nasamarshall/31031723265/)"
---

<!-- Themenblock 02-03: Koordinatenformate bearbeiten/vereinheitlichen -->
Hier sollte ein Einführungstext zum Thema "Koordinatenformate bearbeiten/vereinheitlichen" stehen.

## Themenüberschrift 01

- Rohdaten liefern Koordinaten selten einheitlich – je nach Quelle (GPS-Gerät, Website, händische Erfassung) unterschiedlich formatiert
- Umrechnung in der Praxis meist in zwei Schritten: (1) Grad-, Minuten- (ggf. Sekunden-)Anteil aus dem Text herauslösen, (2) daraus die Dezimalzahl berechnen
- Dafür sind Textfunktionen nötig, die einzelne Zeichen bzw. Positionen innerhalb eines Textstrings ansprechen können – siehe nächster Abschnitt

## Textfunktionen (TEIL, GLÄTTEN, ERSETZEN)

| Funktion | Zweck | Beispiel |
|---|---|---|
| `TEIL(Text; Start; Länge)` | Extrahiert einen Ausschnitt aus der Mitte eines Texts | `TEIL("50°48'N";4;2)` → `"48"` |
| `GLÄTTEN(Text)` | Entfernt überflüssige Leer- und Zwischenraumzeichen | `GLÄTTEN("  Anna Müller")` → `"Anna Müller"` |
| `ERSETZEN(Text; Start; Länge; neuer_Text)` | Ersetzt Zeichen an einer *bestimmten Position* | `ERSETZEN("8,4";2;1;".")` → `"8.4"` |
| `FINDEN(Suchtext; Text)` | Findet die *Position* eines Zeichens (wird oft mit `TEIL`/`ERSETZEN` kombiniert, da diese eine Positionsangabe brauchen) | `FINDEN(",";"8,4")` → `2` |
| `WERT(Text)` | Wandelt einen Text, der wie eine Zahl aussieht, in eine echte, rechenfähige Zahl um | `WERT("8.4")` → `8.4` |

## Konsistente Formatierung

- **Dezimaltrennzeichen:** Deutschland nutzt standardmäßig das Komma (`8,4`), viele internationale/technische Quellen den Punkt (`8.4`) – für Berechnungen muss ein Datensatz einheitlich sein
- **Datumsformate:** `14.03.2024` (DE), `2024-03-14` (ISO 8601), `3/14/2024` (US) sehen unterschiedlich aus und werden von Excel nicht automatisch vereinheitlicht – vor allem `TT.MM.JJJJ` vs. `MM/TT/JJJJ` ist eine häufige Fehlerquelle, weil beide Formate wie eine gültige Zahlenfolge aussehen, aber unterschiedlich interpretiert werden
- Empfehlung: Datensätze früh in ein einheitliches Format bringen (idealerweise ISO 8601 für Daten, Punkt als Dezimaltrennzeichen für den internationalen Austausch), bevor weiterverarbeitet oder mit anderen Datensätzen kombiniert wird

## Additional resources


<!-- Notizen: Ab hier folgen Vermerke, welche als Gedankenstütze oder Erinnerung dienen aber noch nicht in der vorhandenen Form veröffentlicht werden sollen. -->
<!-- Bitte Gedanken innerhalb der Kommentarfunktion einfügen. -->
