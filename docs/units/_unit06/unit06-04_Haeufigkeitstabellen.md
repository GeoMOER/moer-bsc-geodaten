---
title: Häufigkeitstabellen
published: true
toc: true
header:
  image: /assets/images/unit05/notebook.jpg
  caption: "Image: [Neil Conway](https://www.flickr.com/photos/neilconway/) [(Public Domain Mark 1.0)](https://creativecommons.org/publicdomain/mark/1.0/deed.en) via [flickr.com](https://www.flickr.com/photos/neilconway/5625707813/in/photostream/)"
---

Ihre Pivot-Tabelle aus dem letzten Kapitel zeigt bereits, wie viele Messungen je Station vorliegen. Für qualitative (kategoriale) Spalten wie `Standort` oder `Messmethode` lohnt sich aber auch ohne Pivot-Tabelle ein schneller Blick auf die **Häufigkeitsverteilung** – gerade um Bereinigungsbedarf zu erkennen, den Sie sonst leicht übersehen.

## Überblick über qualitative Daten verschaffen

| Frage | Excel-Funktion | Beispiel |
|---|---|---|
| Wie oft kommt jeder Wert vor? | `=ZÄHLENWENN(Bereich;"Firmaneiplatz")` für einen einzelnen Wert, oder eine kleine Übersichtstabelle mit einer Zeile je Kategorie | „Firmaneiplatz": 12 Messungen |
| Gibt es unbeabsichtigt mehrere Schreibweisen derselben Kategorie? | Häufigkeitstabelle durchsehen: Tauchen inhaltlich identische Werte mehrfach mit leicht unterschiedlicher Schreibweise auf? | „Firmaneiplatz" und „firmaneiplatz" separat gezählt → Hinweis auf Bereinigungsbedarf |

**Praxisbeispiel:** Eine Häufigkeitsübersicht Ihrer Spalte `Messmethode` könnte etwa zeigen: `Sensor (automatisch)`: 38, `sensor (automatisch)`: 3. Der zweite Eintrag gehört inhaltlich zur ersten Kategorie – ohne eine solche Übersicht würde diese Aufteilung unbemerkt bleiben und spätere Auswertungen (z. B. „Wie viele Messungen wurden mit welcher Methode erhoben?") verfälschen.

**Unterschied zur Pivot-Tabelle:** Eine Pivot-Tabelle liefert Ihnen dieselbe Information bequemer per Drag-and-Drop – `ZÄHLENWENN` lohnt sich trotzdem, wenn Sie nur schnell **eine** einzelne Kategorie überprüfen wollen, ohne extra eine Pivot-Tabelle aufzubauen.

**Kurzcheck:** Erstellen Sie eine Häufigkeitsübersicht für Ihre zusammengeführte Spalte `Standort`. Tauchen darin Kategorien auf, die eigentlich zusammengehören, aber durch uneinheitliche Schreibweise getrennt gezählt werden?
