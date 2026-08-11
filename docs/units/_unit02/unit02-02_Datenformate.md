---
title: Datentypen und -strukturen
published: false
toc: true
header:
  image: /assets/images/unit02/31031723265_0890cd9547_o.jpg
  image_description: "Cloudscape Over the Philippine Sea"
  caption: "Image: [NASA's Marshall Space Flight Center](https://www.nasa.gov/centers/marshall/home/index.html) [CC BY-NC 2.0] via [flickr.com](https://www.flickr.com/photos/nasamarshall/31031723265/)"
---

<!-- Themenblock 02-02: Datentypen, Encoding-Probleme, Tidy Data, Koordinatenformate (Basic) -->
Hier sollte ein Einführungstext zum Thema "Datentypen, Encoding-Probleme, Tidy Data, Koordinatenformate" stehen.

## Themenüberschrift 01

- Zeilenbasiert
- Zahlen, Datum, Text, Koordinaten 


**Die vier Grunddatentypen:**

| Typ | Bedeutung | Beispiel aus unserem Datensatz |
|---|---|---|
| Numerisch | Messwert, mit dem gerechnet werden kann | Temperatur (8,4 °C) |
| Kategorial (nominal) | Kategorie ohne Rangfolge | Beobachter-Name, Standort |
| Ordinal | Kategorie *mit* sinnvoller Rangfolge | Ort_Typ (Stadtzentrum > Vorort > Dorf) |
| Datum/Zeit | Zeitpunkt, rechenbar (z. B. Differenz in Tagen) | Messdatum, Uhrzeit |

- Nur wenn Excel eine Zelle als *echte* Zahl bzw. echtes *Datum* erkennt, kann damit gerechnet werden (Summe, Mittelwert, Datumsdifferenz). Text, der wie eine Zahl aussieht (z. B. `"8,4"` als Text importiert), muss erst umgewandelt werden.

**Encoding-Probleme:**
- Entstehen typischerweise, wenn eine Datei mit einer anderen Zeichencodierung geöffnet wird, als sie gespeichert wurde (z. B. UTF-8-Datei wird als Windows-1252/Latin-1 gelesen)
- Typisches Erkennungsmerkmal: Umlaute und ß werden durch merkwürdige Zeichenfolgen ersetzt, z. B. `Cölbe` → `CÃ¶lbe`, `Roßberg` → `RoÃŸberg`
- Wichtig: Das ist **kein Tippfehler**, sondern ein systematisches Problem der Dateicodierung – betrifft daher meist mehrere/alle Zellen mit Sonderzeichen gleichermaßen
- Vorbeugen: Beim Importieren einer CSV-Datei in Excel die Kodierung explizit auf **UTF-8** stellen (Daten → Aus Text/CSV)

**"Tidy Data"-Prinzip:**
- Grundregel: **eine Beobachtung pro Zeile, eine Variable pro Spalte**
- Verstoß in unserem Rohdatensatz: `Koordinaten_roh` enthält Breiten- *und* Längengrad in einer einzigen Zelle → zwei Variablen in einer Spalte vermischt
- Folge unsauberer Daten: Filtern, Sortieren und Berechnen wird unnötig kompliziert oder unmöglich, ohne die Spalte vorher aufzutrennen

**Koordinatenformate:**
- **Dezimalgrad** (z. B. `50,80`): eine einzelne Zahl, direkt rechenfähig – Standard für die meisten digitalen Karten/Tools
- **Grad/Minute/Sekunde (DMS)** (z. B. `50°48'N`): traditionelles Format, für Menschen oft intuitiver lesbar, aber nicht direkt rechenfähig
- Umrechnung: `Dezimalgrad = Grad + Minute/60 + Sekunde/3600`



# Encoding


## Additional resources


<!-- Notizen: Ab hier folgen Vermerke, welche als Gedankenstütze oder Erinnerung dienen aber noch nicht in der vorhandenen Form veröffentlicht werden sollen. -->
<!-- Bitte Gedanken innerhalb der Kommentarfunktion einfügen. -->