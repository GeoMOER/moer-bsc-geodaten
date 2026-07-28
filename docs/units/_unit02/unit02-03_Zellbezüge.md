---
title: Zellbezüge
published: false
toc: true
header:
  image: /assets/images/unit02/31031723265_0890cd9547_o.jpg
  image_description: "Cloudscape Over the Philippine Sea"
  caption: "Image: [NASA's Marshall Space Flight Center](https://www.nasa.gov/centers/marshall/home/index.html) [CC BY-NC 2.0] via [flickr.com](https://www.flickr.com/photos/nasamarshall/31031723265/)"
---

- **Relativer Bezug** (`B6`): passt sich beim Kopieren an die neue Zeile/Spalte an – Standardverhalten in Excel
- **Absoluter Bezug** (`$B$3`): bleibt beim Kopieren immer gleich, unabhängig davon, wohin die Formel kopiert wird – erkennbar am `$`-Zeichen vor Spalte und/oder Zeile
- **Gemischter Bezug** (`$B3` oder `B$3`): nur Spalte *oder* nur Zeile wird fixiert
- Praxisbeispiel: Abweichung jeder Messstation vom Gesamt-Mittelwert – der Bezug auf die eigene Temperatur soll sich pro Zeile anpassen (relativ), der Bezug auf den Mittelwert soll immer derselbe bleiben (absolut): `=B6-$B$3`
- `F4` beim Bearbeiten einer Zellreferenz wechselt automatisch zwischen den vier Varianten (`A1` → `$A$1` → `A$1` → `$A1` → `A1`)



- relativ und absoltue Zellbezüge

- Anwendung/Shortcuts


## Additional resources
