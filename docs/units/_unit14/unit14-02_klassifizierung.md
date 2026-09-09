---
title: Werte klassifizieren
published: true
toc: true
header:
  image: /assets/images/unit14/hero-unit14.jpg
  image_description: "Fertig gestaltete thematische Karte mit Höhenrelief, Flusslauf und kartographischen Nebenelementen"
  caption: "KI-generierte Illustration, bearbeitet für diesen Kurs"
---

<!-- Introtext: Zeigen, dass Klassengrenzen das sichtbare Muster und damit die Interpretation einer Karte beeinflussen. -->

## Warum Werte klassifizieren?

Numerische Daten können viele unterschiedliche Werte enthalten. In einer **Klassifizierung** werden Wertebereiche zu Klassen zusammengefasst. Jede Klasse erhält anschließend ein Symbol oder eine Farbe.

Beispiel für Höhenwerte an Beobachtungspunkten:

| Höhenklasse | Bedeutung |
|---|---|
| 150 bis unter 250 m | niedrige Lage |
| 250 bis unter 350 m | mittlere Lage |
| 350 bis unter 450 m | höhere Lage |
| ab 450 m | sehr hohe Lage im Untersuchungsgebiet |

Die Klassifizierung erleichtert die visuelle Übersicht, reduziert aber zugleich die ursprüngliche Information: Zwei unterschiedliche Werte können in derselben Klasse gleich aussehen.

> **Merksatz:** Klassengrenzen sind eine Entscheidung. Sie können räumliche Muster hervorheben, abschwächen oder scheinbar neu erzeugen.

## Klassifizieren oder kontinuierlich darstellen?

Nicht alle numerischen Daten müssen in Klassen aufgeteilt werden.

### Kontinuierliche Darstellung

Ein Farbverlauf ordnet jedem Wert entlang einer Skala eine Farbe zu. Dies eignet sich beispielsweise für ein Höhenraster, wenn feine Übergänge sichtbar bleiben sollen.

### Klassifizierte Darstellung

Werte werden zu wenigen Gruppen zusammengefasst. Dies eignet sich, wenn:

* bestimmte Wertebereiche verglichen werden sollen,
* fachlich bedeutsame Schwellen existieren,
* eine Legende mit klaren Gruppen benötigt wird oder
* sehr viele Einzelwerte die Karte unübersichtlich machen.

Für unsere Beobachtungspunkte können die abgetasteten Höhenwerte beispielsweise in vier oder fünf Höhenklassen dargestellt werden.

## Kategorien sind keine Zahlenklassen

Die Werte `1 = Wald`, `2 = Grünland` und `3 = Siedlung` sind Kategorien. Sie werden **kategorisiert**, nicht anhand numerischer Intervalle klassifiziert.

Eine abgestufte Darstellung wäre irreführend, weil sie eine messbare Reihenfolge oder einen Abstand zwischen den Codes suggeriert.

Prüfen Sie daher vor jeder Klassifizierung:

1. Ist das Feld tatsächlich numerisch?
2. Besitzen die Zahlen eine quantitative Bedeutung?
3. In welcher Einheit werden sie angegeben?
4. Gibt es fachlich sinnvolle Grenzwerte?

## Anzahl der Klassen

Zu wenige Klassen können wichtige Unterschiede verdecken. Zu viele Klassen lassen sich in Karte und Legende schwer unterscheiden.

Für eine einfache thematische Karte sind häufig etwa **vier bis sieben Klassen** ein sinnvoller Ausgangspunkt. Die passende Zahl hängt jedoch ab von:

* Verteilung der Werte,
* Zahl der Features,
* Kartengröße,
* Farbpalette,
* Zielgruppe und
* fachlicher Fragestellung.

Für einen kleinen Datensatz mit wenigen verschiedenen Werten können bereits drei oder vier Klassen genügen.

## Gleiche Intervalle

Bei **gleichen Intervallen** besitzt jede Klasse dieselbe Breite.

Wenn Höhenwerte von 100 bis 500 Metern in vier Klassen aufgeteilt werden, könnten die Klassen lauten:

* 100 bis unter 200 m,
* 200 bis unter 300 m,
* 300 bis unter 400 m,
* 400 bis 500 m.

### Vorteile

* leicht zu erklären,
* gleich große Wertebereiche,
* Karten mit denselben Grenzen können gut verglichen werden.

### Nachteile

* bei stark ungleich verteilten Daten können manche Klassen sehr viele und andere kaum Features enthalten,
* Ausreißer können breite, wenig aussagekräftige Klassen erzeugen.

Gleiche Intervalle sind sinnvoll, wenn der Wertebereich gleichmäßig gegliedert werden soll und die Verteilung nicht zu stark verzerrt ist.

## Quantile

Bei **Quantilen** enthält jede Klasse ungefähr gleich viele Features.

Bei 100 Beobachtungspunkten und vier Klassen würden ungefähr 25 Punkte je Klasse zugeordnet.

### Vorteile

* alle Farben beziehungsweise Klassen erscheinen meist sichtbar auf der Karte,
* Rangunterschiede zwischen Features werden hervorgehoben.

### Nachteile

* Klassen können sehr unterschiedlich breite Wertebereiche besitzen,
* sehr ähnliche Werte können in verschiedene Klassen fallen,
* identische Werte an einer Klassengrenze erschweren eine gleichmäßige Aufteilung,
* Karten verschiedener Datensätze sind schwerer direkt vergleichbar.

Quantile zeigen relative Positionen innerhalb des Datensatzes – nicht automatisch fachlich gleich große Unterschiede.

## Natürliche Unterbrechungen

Die Methode **Natürliche Unterbrechungen** beziehungsweise **Natural Breaks (Jenks)** sucht Klassengrenzen an Stellen, an denen größere Lücken in der Werteverteilung liegen. Innerhalb der Klassen sollen die Werte möglichst ähnlich sein.

### Vorteile

* vorhandene Gruppen in der Werteverteilung können sichtbar werden,
* häufig gut an einen einzelnen Datensatz angepasst.

### Nachteile

* Grenzwerte sind weniger leicht vorherzusagen,
* bei veränderten Daten können völlig andere Klassen entstehen,
* verschiedene Karten lassen sich schlecht vergleichen, wenn jede eigene Grenzen erhält,
* gefundene Gruppen sind nicht automatisch fachlich bedeutsam.

Die Methode beschreibt Strukturen des konkreten Datensatzes. Sie liefert nicht von selbst eine wissenschaftliche Erklärung für diese Strukturen.

## Fachlich definierte Klassen

Bei **manuellen** oder fachlich definierten Klassen werden die Grenzen aus der Fragestellung oder aus etablierten Schwellenwerten abgeleitet.

Beispiele:

* Höhenstufen mit fachlicher Bedeutung,
* gesetzliche Grenzwerte,
* Gefahrenstufen,
* für mehrere Zeitpunkte unverändert verwendete Vergleichsklassen.

### Vorteile

* gut interpretierbar,
* über mehrere Karten hinweg vergleichbar,
* direkter Bezug zur fachlichen Frage.

### Nachteile

* geeignete Schwellenwerte müssen begründet werden,
* einzelne Klassen können leer oder stark unterschiedlich besetzt sein,
* schlecht gewählte Grenzen können ebenfalls irreführen.

Wenn keine fachlichen Schwellen existieren, darf eine rein technische Klassifizierung nicht nachträglich als fachlich zwingend dargestellt werden.

## Weitere Methoden

QGIS bietet zusätzliche Verfahren, beispielsweise eine Einteilung nach **Standardabweichung**. Dabei werden Werte relativ zum Mittelwert und ihrer Streuung gruppiert.

Diese Methode kann sinnvoll sein, wenn Abweichungen vom Mittelwert die zentrale Aussage bilden. Für den Einstieg konzentrieren wir uns jedoch auf:

* gleiche Intervalle,
* Quantile,
* natürliche Unterbrechungen und
* manuelle Grenzen.

## Klassengrenzen eindeutig formulieren

Klassen dürfen sich nicht überlappen und keinen gültigen Wert auslassen.

Eine eindeutige Schreibweise ist beispielsweise:

* 100 bis unter 200 m,
* 200 bis unter 300 m,
* 300 bis einschließlich 400 m.

Die Legende sollte keine unnötig langen Nachkommastellen enthalten. Grenzen wie `249,8736–351,2941` vermitteln meist eine Genauigkeit, die fachlich weder nötig noch vorhanden ist.

Runden Sie Legendenbeschriftungen nachvollziehbar und prüfen Sie, ob die tatsächlichen QGIS-Klassengrenzen weiterhin korrekt sind.

## Ausreißer prüfen

Ein einzelner ungewöhnlich hoher oder niedriger Wert kann die Klassifizierung stark beeinflussen.

Prüfen Sie vor dem Klassifizieren:

* Minimum und Maximum,
* Histogramm oder Werteverteilung,
* fehlende Werte,
* mögliche Fehlercodes wie `-9999`,
* ungewöhnliche Einzelwerte und
* Einheit des Feldes.

Ein Ausreißer darf nicht nur deshalb entfernt werden, weil die Karte danach gleichmäßiger aussieht. Zuerst muss geklärt werden, ob es sich um einen Fehler oder einen gültigen Extremwert handelt.

## Absolute Werte und Bezugsgrößen

Absolute Zahlen können durch unterschiedlich große Bezugsflächen oder Populationen beeinflusst sein.

Beispiel:

* 1.000 Beobachtungen pro Landkreis zeigen häufig auch, wo viele Menschen leben oder intensiv gesucht wird.
* Beobachtungen pro Quadratkilometer beantworten eine andere Frage.

Vor einer Klassifizierung ist deshalb zu prüfen, ob ein absoluter Wert, eine Rate, ein Anteil oder eine Dichte fachlich angemessen ist.

Für einzelne GBIF-Punkte mit bereits abgetasteter Höhe ist keine Normalisierung notwendig: Jeder Punkt besitzt direkt einen Höhenwert.

## Klassifizierung in QGIS

Für den Layer `gbif_mit_hoehe`:

1. Öffnen Sie **Layereigenschaften → Symbolisierung**.
2. Wählen Sie **Abgestuft** beziehungsweise **Graduated**.
3. Wählen Sie das verbindliche Höhenfeld `hoehe_m`.
4. Verwenden Sie eine sequentielle Farbpalette.
5. Stellen Sie zunächst vier oder fünf Klassen ein.
6. Wählen Sie eine Klassifizierungsmethode.
7. Klicken Sie auf **Klassifizieren**.
8. Prüfen Sie Grenzen, Anzahl der Features je Klasse und Legendenbeschriftungen.

Speichern Sie vor dem Vergleich gegebenenfalls Screenshots oder notieren Sie die Klassengrenzen.

<!-- Lehrende: Feldname an den tatsächlichen Ergebnislayer aus Unit 13 anpassen. -->

## Methoden vergleichen

In der Sitzung vergleichen wir `ersatz/klassifizierung_intervalle.png` und `ersatz/klassifizierung_quantile.png` aus dem [Marburger Übungspaket und Anleitung]({{ '/material/marburg.html' | relative_url }}). Beide zeigen dieselben 35 Nachweise mit fünf Klassen und derselben Farbpalette. Dadurch untersuchen wir gezielt den Einfluss der Methode. Anschließend setzen wir eine der beiden Methoden mit ebenfalls fünf Klassen in QGIS um; weitere Varianten gehören nicht zum Pflichtumfang.

<style>
.classification-comparison { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 1rem; margin: 1.5rem 0; }
.classification-comparison figure { display: block; min-width: 0; margin: 0; }
.classification-comparison img { display: block; width: 100%; height: auto; }
.classification-comparison figcaption { margin-top: .5rem; }
@media (max-width: 1100px) { .classification-comparison { grid-template-columns: minmax(0, 1fr); } }
</style>

<div class="classification-comparison" aria-label="Vergleich derselben Nachweise mit zwei Klassifizierungsmethoden">
  <figure>
    <a href="{{ '/assets/data/marburg/klassifizierung_intervalle.png' | relative_url }}" aria-label="Karte mit gleichen Intervallen in voller Größe öffnen">
      <img src="{{ '/assets/data/marburg/klassifizierung_intervalle.png' | relative_url }}" alt="35 Feuersalamander-Nachweise bei Marburg, nach Geländehöhe in fünf gleich breite Werteintervalle von etwa 178,5 bis 323,9 Metern eingeteilt. Die Klassen können unterschiedlich viele Nachweise enthalten." loading="lazy">
    </a>
    <figcaption><strong>Gleiche Intervalle:</strong> gleiche Breite der Werteintervalle.</figcaption>
  </figure>
  <figure>
    <a href="{{ '/assets/data/marburg/klassifizierung_quantile.png' | relative_url }}" aria-label="Karte mit Quantilen in voller Größe öffnen">
      <img src="{{ '/assets/data/marburg/klassifizierung_quantile.png' | relative_url }}" alt="Dieselben 35 Nachweise mit gleicher Farbpalette und fünf Quantilklassen: Die Klassengrenzen liegen bei etwa 178,5, 214,3, 230,0, 245,0, 267,7 und 323,9 Metern. Die Werteintervalle sind unterschiedlich breit." loading="lazy">
    </a>
    <figcaption><strong>Quantile:</strong> möglichst gleich viele Nachweise je Klasse.</figcaption>
  </figure>
</div>

*Auf schmalen Bildschirmen stehen die Karten untereinander. Öffnen Sie eine Karte für die vollständige Größe. Beide Exporte stammen unverändert aus dem Übungspaket; Daten, Ausschnitt, Symbolgröße und Farbpalette sind identisch.*

Vergleichen Sie einen Nachweis, dessen Farbe sich verändert: Hat sich seine Höhe geändert oder nur seine Zuordnung zu einer Farbklasse? Prüfen Sie dazu die beiden Legenden. Die 21 geprüften Nachweise ohne gültige Höhe sind in beiden Karten nicht dargestellt.

Als freiwillige Vertiefung können Sie für denselben Punktlayer drei Varianten erstellen:

1. gleiche Intervalle,
2. Quantile,
3. natürliche Unterbrechungen.

Dokumentieren Sie:

| Methode | Klassengrenzen | Features je Klasse | sichtbare Wirkung |
|---|---|---|---|
| gleiche Intervalle | `[eintragen]` | `[eintragen]` | `[eintragen]` |
| Quantile | `[eintragen]` | `[eintragen]` | `[eintragen]` |
| natürliche Unterbrechungen | `[eintragen]` | `[eintragen]` | `[eintragen]` |

Beantworten Sie:

1. Bei welcher Methode sind die Klassen ähnlich stark besetzt?
2. Bei welcher Methode sind die Wertebereiche gleich breit?
3. Welche Methode erzeugt die auffälligsten räumlichen Gruppen?
4. Welche Variante beantwortet die Leitfrage am verständlichsten?
5. Welche Einschränkung besitzt Ihre bevorzugte Variante?

## Vergleichbarkeit sichern

Wenn mehrere Karten verglichen werden sollen, sollten sie nach Möglichkeit dieselben:

* Klassengrenzen,
* Farben,
* Einheiten,
* Kartenausschnitte und
* Legendenbegriffe

verwenden.

Werden für jedes Jahr neue Quantile oder natürliche Unterbrechungen berechnet, kann dieselbe Farbe in verschiedenen Karten unterschiedliche Wertebereiche bedeuten.

## Klassifizierung dokumentieren

Halten Sie mindestens fest:

* klassifiziertes Attribut,
* Einheit,
* Methode,
* Zahl der Klassen,
* genaue Klassengrenzen,
* verwendete Farbpalette,
* Behandlung fehlender Werte und
* fachliche Begründung.

Damit bleibt nachvollziehbar, wie das sichtbare Muster erzeugt wurde.

## Häufige Probleme

| Problem | Wirkung | Verbesserung |
|---|---|---|
| Zahlen-Codes werden abgestuft dargestellt | falsche Ordnung wird suggeriert | Kategorien verwenden |
| zu viele Klassen | Unterschiede kaum erkennbar | Klassenzahl reduzieren |
| Ausreißer bestimmt gesamten Wertebereich | viele Features wirken gleich | Ausreißer prüfen und Methode begründen |
| Quantile werden als gleiche Wertebereiche gelesen | Unterschiede falsch interpretiert | Grenzen klar beschriften |
| jede Vergleichskarte besitzt andere Grenzen | Farben sind nicht vergleichbar | feste gemeinsame Klassen verwenden |
| lange Dezimalzahlen in Legende | Scheingenauigkeit und schlechte Lesbarkeit | sinnvoll runden |
| leere oder fast leere Klassen | Legende enthält wenig Information | Grenzen und Methode prüfen |
| NoData wird mitklassifiziert | ungültige Werte erscheinen als Klasse | fehlende Werte korrekt behandeln |

## Kurze Übung

Eine Höhenverteilung enthält viele Beobachtungen zwischen 180 und 260 Metern, wenige zwischen 260 und 400 Metern und einen Punkt bei 620 Metern.

1. Wie könnte der einzelne hohe Wert gleiche Intervalle beeinflussen?
2. Wie würden Quantile mit der ungleichen Verteilung umgehen?
3. Warum könnten natürliche Unterbrechungen eine eigene hohe Klasse erzeugen?
4. Welche Methode würden Sie für eine einmalige Übersicht wählen?
5. Welche Methode wäre sinnvoll, wenn dieselben Höhenklassen für mehrere Arten verglichen werden sollen?

<!-- Lösungshinweise für Lehrende:
- keine einzelne Methode ist immer richtig; Begründung zählt.
- gleicher Intervallbereich kann in oberen Klassen sehr wenige Features enthalten.
- Quantile verteilen Features ungefähr gleich, erzeugen aber ungleiche Wertebereiche.
- Natural Breaks kann die Lücke vor dem Extremwert aufgreifen.
- für mehrere Arten sind gemeinsame manuelle oder gleiche fachliche Grenzen häufig besser vergleichbar.
-->

## Zusammenfassung

* Klassifizierung fasst numerische Werte zu Klassen zusammen und reduziert dabei Information.
* Gleiche Intervalle erzeugen gleich breite Wertebereiche.
* Quantile erzeugen ungefähr gleich stark besetzte Klassen.
* Natürliche Unterbrechungen passen Grenzen an Gruppen im konkreten Datensatz an.
* Fachlich definierte Grenzen können besonders gut interpretierbar und vergleichbar sein.
* Klassenzahl, Ausreißer und Werteverteilung müssen vor der Entscheidung geprüft werden.
* Verschiedene Methoden können aus denselben Daten unterschiedliche sichtbare Muster erzeugen.
* Methode, Grenzen, Einheit und Farbpalette müssen dokumentiert werden.

## Weiterführende Informationen

* [QGIS-Dokumentation: Vektorsymbolisierung](https://docs.qgis.org/latest/en/docs/user_manual/working_with_vector/vector_properties.html)
* [QGIS-Übung: Klassifizierung](https://docs.qgis.org/latest/en/docs/training_manual/vector_classification/classification.html)
* [QGIS-Dokumentation: Rasterklassifizierung und Farbverläufe](https://docs.qgis.org/latest/en/docs/user_manual/working_with_raster/raster_properties.html)

<!-- Notizen: Ab hier folgen Vermerke, welche als Gedankenstütze oder Erinnerung dienen, aber noch nicht in der vorhandenen Form veröffentlicht werden sollen. -->

<!--
Mögliche Abbildungen:
- derselbe Punktdatensatz mit gleichen Intervallen, Quantilen und Natural Breaks
- Histogramm mit eingezeichneten Klassengrenzen
- Beispiel für eindeutige und überlappende Klassenbeschriftungen
- Vergleichskarten mit identischen versus neu berechneten Grenzen

Didaktisch wichtig:
- nicht nach der einen „richtigen“ technischen Methode suchen lassen.
- jede Wahl an Frage, Verteilung und Vergleichsziel binden.
- Natural Breaks nicht als Entdeckung fachlich realer Gruppen darstellen.
- bei Punkt-Höhenwerten Farbe bevorzugen; Größenvariation optional vergleichen.
- für die Abschlussaufgabe mindestens zwei Methoden vergleichen, aber nur eine begründet verwenden.
-->
