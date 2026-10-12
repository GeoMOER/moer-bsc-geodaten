---
title: Programmierung
published: true
toc: true
header:
  image: assets/images/unit08/DataSwamp_Stage08.png
  image_description: "Streuobstwiese"
  caption: "Image: ulrichstill [CC BY-SA 2.0 DE] via [wikimedia.org](https://commons.wikimedia.org/wiki/File:Tuebingen_Streuobstwiese.jpg)"
---

<!-- Themenblock 08-01: Automatisierung wiederkehrender Arbeitsschritte -->
Automatisierung erfolgt häufig über **Programmierung**.
R und Python sind Programmiersprachen. Ein **Skript** ist eine Textdatei, in der das Rezept steht. Das Programm führt sie Zeile für Zeile von oben nach unten aus.
 
## Ausprobieren im Browser: ein Skript lesen und ändern
 
Die folgenden zwei kurzen Aufgaben laufen direkt in Ihrem Browser, Sie müssen nichts installieren. Sie schreiben im Editor links, klicken auf **Submit Answer** und sehen rechts das Ergebnis. **Hint** gibt Tipps, **Solution** zeigt die Lösung. Das erste Laden kann einen Moment dauern.
 
Zur Orientierung: Eine Zeile wie `celsius <- 25` legt einen Wert unter einem Namen ab. Das entspricht einer Excel-Zelle, in der `25` steht. Der Pfeil `<-` heißt „speichere in“. Alles hinter einem `#` ist ein Kommentar und wird nicht ausgeführt.
 
| Zeile im Skript | Entspricht in Excel |
|---|---|
| `celsius <- 25` | Zelle mit dem Wert 25 |
| `celsius <- c(21.74, 15.01, 13.09)` | Spalte mit mehreren Werten |
| `fahrenheit <- celsius * 9/5 + 32` | Formel `=A2*9/5+32` mit Zellbezug |
| `mean(fahrenheit)` | `MITTELWERT` |
| `round(…, 1)` | `RUNDEN` |
 
<script src="https://cdn.datacamp.com/datacamp-light-latest.min.js"></script>
 
### Aufgabe 1: Neue Eingabe, gleiches Rezept
 
Das Skript rechnet eine Temperatur von Celsius in Fahrenheit um. Ändern Sie nur den Wert von `celsius` auf 30 und führen Sie es erneut aus. Die Formel darunter müssen Sie nicht anfassen.
 
<div data-datacamp-exercise data-lang="r" data-height="auto">
<code data-type="pre-exercise-code"># no pec</code>
<code data-type="sample-code"># Temperatur in Grad Celsius (wie ein Wert in einer Excel-Zelle)
celsius <- 25
# Das Rezept: Celsius in Fahrenheit umrechnen
fahrenheit <- celsius * 9/5 + 32
 
# Ergebnis anzeigen
fahrenheit
 
# AUFGABE: Ändern Sie oben den Wert von celsius auf 30.
</code>
<code data-type="solution"># Temperatur in Grad Celsius (wie ein Wert in einer Excel-Zelle)
celsius <- 30
# Das Rezept: Celsius in Fahrenheit umrechnen
fahrenheit <- celsius * 9/5 + 32
 
# Ergebnis anzeigen
fahrenheit
</code>
<code data-type="sct">test_object("celsius", incorrect_msg = "Setzen Sie celsius auf 30.")
test_object("fahrenheit", incorrect_msg = "Lassen Sie die Formel unverändert, nur der Wert von celsius soll sich ändern.")
success_msg("Richtig. Neue Eingabe, gleiches Rezept: Das Ergebnis ist 86.")
</code>
<div data-type="hint">Ändern Sie in der Zeile celsius &lt;- 25 nur die Zahl.</div>
</div>

 
## Ausblick: Automatisierung bei Geodaten
 
Auch bei Geodaten spielt Automatisierung eine große Rolle. GIS-Programme wie QGIS bieten Werkzeuge zur Verarbeitung, die sich hintereinander zu Modellen verknüpfen lassen. Für R und Python gibt es Bibliotheken für räumliche Daten. Das Prinzip ist dasselbe wie hier: Schritte aufschreiben, die sich auf neue Daten anwenden lassen. 


## Wann lohnt sich Automatisierung?
 
- Ein Schritt wird mehr als dreimal wiederholt.
- Neue Daten mit derselben Struktur treffen regelmäßig ein.
- Andere sollen nachvollziehen können, wie ein Ergebnis zustande kam.
- Die Datenmenge ist so groß, dass Handarbeit nicht mehr praktikabel ist.
