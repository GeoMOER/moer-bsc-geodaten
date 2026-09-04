---
title: Daten sinnvoll symbolisieren
published: true
toc: true
header:
  image: /assets/images/unit14/hero-unit14.jpg
  image_description: "Fertig gestaltete thematische Karte mit Höhenrelief, Flusslauf und kartographischen Nebenelementen"
  caption: "KI-generierte Illustration, bearbeitet für diesen Kurs"
---

<!-- Introtext: Symbolisierung als fachliche Entscheidung und nicht als dekorativen Arbeitsschritt einführen. -->

## Eine Karte ist eine Auswahl

Eine Karte kann nicht alle Eigenschaften eines Datensatzes gleichzeitig zeigen. Wir wählen aus:

* welche Layer sichtbar sind,
* welches Attribut dargestellt wird,
* welche Objekte hervorgehoben werden,
* welche Farben und Symbole verwendet werden und
* welche Informationen in den Hintergrund treten.

Symbolisierung ist deshalb ein Teil der fachlichen Aussage.

> **Merksatz:** Erst Fragestellung und Datenart bestimmen – danach Symbol und Farbe wählen.

## Datenart vor Darstellung

Für die Symbolisierung ist nicht nur der technische Datentyp eines Feldes wichtig. Entscheidend ist die fachliche Bedeutung der Werte.

| Datenart | Beispiel | geeignete visuelle Logik |
|---|---|---|
| nominal/kategorial | Schutzgebietstyp, Artname | unterscheidbare Farben oder Formen |
| ordinal | gering, mittel, hoch | geordnete Helligkeit oder Größe |
| numerisch | Höhe, Fläche, Länge | geordneter Farbverlauf oder Größe |
| Abweichung um Bezugspunkt | Temperaturabweichung von 0 | divergierende Farbpalette |

Eine Zahl kann auch nur ein Code sein. Die Klassen `1 = Wald`, `2 = Grünland` und `3 = Siedlung` dürfen nicht wie aufeinanderfolgende Messwerte interpretiert werden.

## Visuelle Variablen

Kartensymbole können sich durch verschiedene sichtbare Eigenschaften unterscheiden:

| visuelle Variable | besonders geeignet für |
|---|---|
| Farbton | verschiedene Kategorien |
| Helligkeit | geordnete oder numerische Werte |
| Sättigung | Hervorhebung und Gewichtung |
| Größe | quantitative Unterschiede |
| Form | wenige Punktkategorien |
| Linienbreite | Bedeutung oder Größenordnung von Linien |
| Strichmuster | verschiedene Linienkategorien |
| Transparenz | Überlagerung und visuelle Hierarchie |

Nicht jede Variable ist gleich gut lesbar. Sehr kleine Unterschiede in Form oder Sättigung lassen sich beispielsweise schwer vergleichen.

## Einzelne Symbole

Die Darstellung **Einzelsymbol** verwendet für alle Features eines Layers dasselbe Symbol. Sie eignet sich, wenn:

* nur die Lage der Features wichtig ist,
* alle Features derselben fachlichen Gruppe angehören oder
* der Layer lediglich räumlichen Kontext liefert.

Beispiel: Alle GBIF-Beobachtungen werden zunächst als gleich große dunkle Punkte dargestellt.

## Kategorisierte Symbolisierung

Eine **kategorisierte** Darstellung weist jedem eindeutigen Attributwert ein eigenes Symbol zu.

Geeignete Beispiele:

* verschiedene Arten,
* Schutzgebietskategorien,
* Gewässertypen oder
* Qualitätsklassen als benannte Gruppen.

Verwenden Sie:

* unterscheidbare Farbtöne,
* gegebenenfalls unterschiedliche Punktformen,
* eine begrenzte Zahl gleichzeitig sichtbarer Kategorien und
* verständliche Klassenbezeichnungen in der Legende.

Bei sehr vielen Kategorien wird eine Karte schnell unlesbar. Dann sollte die Fragestellung enger gefasst oder eine Auswahl gebildet werden.

## Abgestufte Symbolisierung

Eine **abgestufte** Darstellung ordnet numerische Werte Klassen zu und stellt diese mit geordneten Farben oder Größen dar.

Beispiele:

* Höhenwerte an Beobachtungspunkten,
* Fläche von Schutzgebieten,
* Länge von Gewässerabschnitten oder
* Anzahl von Beobachtungen pro Gebiet.

Die Wahl der Klassengrenzen beeinflusst das Kartenbild. Sie wird deshalb auf der nächsten Seite ausführlich behandelt.

## Punktdaten darstellen

Punkte besitzen auf der Karte keine tatsächliche Fläche. Ihre Symbolgröße dient der Sichtbarkeit oder codiert einen Wert.

### Lage zeigen

Verwenden Sie ein einheitliches, ausreichend großes Symbol mit gutem Kontrast zum Hintergrund.

### Kategorien unterscheiden

Verwenden Sie unterschiedliche Farbtöne oder wenige gut unterscheidbare Formen.

### Zahlenwerte darstellen

Verwenden Sie:

* einen geordneten Farbverlauf,
* abgestufte Symbolgrößen oder
* eine begründete Kombination beider Mittel.

Wenn Größen quantitative Werte zeigen, müssen größere Werte sichtbar größere Symbole erhalten. Zu große Symbole können sich jedoch stark überdecken und eine hohe Beobachtungsdichte vortäuschen.

## Liniendaten darstellen

Bei Linien können insbesondere Farbe, Breite und Strichmuster variiert werden.

Beispiele:

* Gewässer in einem zurückhaltenden Blauton,
* Hauptgewässer breiter als Nebengewässer,
* Wanderwege gestrichelt,
* Verwaltungsgrenzen dünn und neutral.

Die Linienbreite in QGIS ist eine Darstellungsgröße. Sie entspricht nicht automatisch der realen Breite des Flusses oder der Straße.

Vermeiden Sie sehr breite oder kontrastreiche Linien, wenn der Layer nur Orientierung bieten soll.

## Polygondaten darstellen

Polygone können durch Füllfarbe, Umriss und Transparenz gestaltet werden.

### Fläche ist die Hauptinformation

Verwenden Sie eine Füllfarbe, wenn die flächenhafte Verteilung oder ein Attribut der Polygone wichtig ist.

### Grenze ist die Hauptinformation

Verwenden Sie eine transparente Füllung und einen gut sichtbaren Umriss, wenn andere Layer innerhalb der Polygone sichtbar bleiben sollen.

Für Schutzgebiete über einem Höhenraster eignet sich häufig:

* keine oder nur schwache Füllung,
* ein klarer, aber nicht dominanter Umriss,
* eine Position unterhalb der Beobachtungspunkte.

## Rasterdaten darstellen

Für Raster richtet sich die Symbolisierung nach der Bedeutung der Zellwerte.

### Kontinuierliches Raster

Ein digitales Geländemodell wird meist mit einem kontinuierlichen, sequentiellen Farbverlauf dargestellt. Niedrige und hohe Werte sollen eindeutig geordnet sein.

### Kategoriales Raster

Eine Landbedeckung erhält für jede Klasse eine eigene Farbe. Zwischenwerte werden nicht durch einen kontinuierlichen Verlauf suggeriert.

### Mehrbändiges Raster

Bei Luft- und Satellitenbildern können mehrere Bänder beispielsweise als Rot, Grün und Blau kombiniert werden. Die sichtbaren Farben entstehen dann aus der Bandkombination.

NoData-Bereiche sollten transparent oder eindeutig von gültigen Werten unterscheidbar sein.

## Farbpaletten

### Qualitative Paletten

Qualitative Paletten verwenden verschiedene Farbtöne ohne erkennbare Rangfolge. Sie eignen sich für Kategorien wie Landbedeckung oder Schutzgebietstypen.

### Sequentielle Paletten

Sequentielle Paletten verlaufen geordnet von hell nach dunkel oder von geringer zu stärkerer Farbwirkung. Sie eignen sich für Werte von niedrig nach hoch.

Beispiele:

* Geländehöhe,
* Niederschlag,
* Flächengröße.

### Divergierende Paletten

Divergierende Paletten besitzen zwei Farbrichtungen und einen neutralen Mittelpunkt. Sie eignen sich, wenn ein fachlich wichtiger Bezugswert existiert.

Beispiele:

* Abweichung von einer Referenz,
* Veränderung von negativ über null zu positiv,
* Temperatur unter und über einem Schwellenwert.

Für ausschließlich positive Höhenwerte ohne besonderen Mittelpunkt ist meist eine sequentielle Palette geeigneter.

## Farben zugänglich wählen

Eine Karte sollte auch bei eingeschränktem Farbsehen und auf unterschiedlichen Bildschirmen möglichst verständlich bleiben.

Hilfreiche Regeln:

* Rot und Grün nicht als einzige Unterscheidung verwenden.
* Zusätzlich Helligkeit, Form oder Beschriftung nutzen.
* Sehr helle Farben auf weißem Hintergrund vermeiden.
* Ausreichenden Kontrast zwischen wichtigen Symbolen und Hintergrund herstellen.
* Karte auch verkleinert und gegebenenfalls in Graustufen prüfen.
* Farbpaletten mit gleichmäßiger wahrgenommener Abstufung bevorzugen.

Mehr Farbe führt nicht automatisch zu mehr Information.

## Visuelle Hierarchie

Die wichtigsten Inhalte der Karte sollen zuerst auffallen. Kontextinformationen dürfen sichtbar sein, aber nicht mit der Hauptaussage konkurrieren.

Für unsere Abschlusskarte könnte die Hierarchie lauten:

1. **Beobachtungspunkte mit Höhenklassen** – Hauptinformation,
2. **Untersuchungsgebiet oder Schutzgebietsgrenzen** – räumlicher Kontext,
3. **Geländehöhe** – zurückhaltender Hintergrund,
4. **Gewässer** – optionaler Orientierungslayer.

Diese Hierarchie wird durch Kontrast, Größe, Farbe, Transparenz und Layerreihenfolge erzeugt.

## Hintergrundkarten

Eine Hintergrundkarte kann Orientierung bieten, enthält aber häufig viele eigene Farben, Beschriftungen und Symbole. Dadurch kann sie die eigentliche Aussage überdecken.

Prüfen Sie:

* Wird die Hintergrundkarte wirklich benötigt?
* Ist sie ausreichend zurückhaltend?
* Ist ihre Quelle angegeben?
* Darf sie in der exportierten Karte verwendet werden?
* Passt ihr Informationsstand zur Fragestellung?

Für eine thematische Karte kann ein heller, einfacher Hintergrund oder gar keine zusätzliche Hintergrundkarte besser sein.

## Beschriftungen

Beschriftungen sollten nur Informationen zeigen, die für das Verständnis notwendig sind.

* Verwenden Sie kurze, verständliche Texte.
* Beschriften Sie nicht jedes Feature automatisch.
* Vermeiden Sie Überlagerungen mit wichtigen Kartensymbolen.
* Nutzen Sie gegebenenfalls einen dezenten Texthintergrund oder Puffer.
* Prüfen Sie die Lesbarkeit bei der endgültigen Kartengröße.

Statt alle Beobachtungspunkte zu beschriften, kann es sinnvoller sein, nur wichtige Orte oder das Untersuchungsgebiet zu benennen.

## Symbolisierung in QGIS

Die Symbolisierung eines Layers öffnen Sie über:

1. Doppelklick auf den Layer oder Rechtsklick → **Eigenschaften**,
2. Bereich **Symbolisierung**,
3. Auswahl der Darstellungsart, zum Beispiel:
   * Einzelsymbol,
   * kategorisiert,
   * abgestuft oder
   * Einkanal-Pseudofarbe für ein Raster.

Alternativ ermöglicht das Bedienfeld **Layergestaltung** unmittelbare Änderungen in der Kartenansicht.

Speichern Sie wichtige Gestaltungsentscheidungen im QGIS-Projekt. Eine exportierte Bilddatei allein enthält nicht mehr alle zugrunde liegenden Einstellungen.

## Häufige Probleme

| Problem | Wirkung | Verbesserung |
|---|---|---|
| zu viele kräftige Farben | keine klare Hauptaussage | visuelle Hierarchie festlegen |
| qualitative Farben für Zahlenwerte | Reihenfolge bleibt unklar | sequentielle Palette verwenden |
| Farbverlauf für Kategorien | nicht vorhandene Ordnung wird suggeriert | qualitative Palette verwenden |
| deckende Polygone | darunterliegende Layer verschwinden | Transparenz oder nur Umriss nutzen |
| sehr große Punktsymbole | starke Überdeckung | Größe verringern oder Auswahl bilden |
| kontrastreicher Hintergrund | Themendaten gehen unter | Hintergrund vereinfachen |
| Rot-Grün-Unterscheidung | für manche Personen schwer lesbar | andere Palette und zusätzliche Variable verwenden |
| unverständliche Layernamen | Legende bleibt technisch | kurze fachliche Bezeichnungen vergeben |

## Kurze Übung

### 1. Palette auswählen

Welche Palette ist geeignet?

1. Schutzgebietstypen,
2. Höhe von niedrig nach hoch,
3. Temperaturabweichung unter und über null,
4. Landbedeckungsklassen.

### 2. Visuelle Hierarchie herstellen

Laden Sie DGM, Schutzgebiete, Gewässer und GBIF-Punkte. Gestalten Sie die Karte so, dass die Beobachtungspunkte zuerst auffallen und alle anderen Layer nur den notwendigen Kontext liefern.

### 3. Entscheidung begründen

Dokumentieren Sie für jeden sichtbaren Layer:

| Layer | dargestelltes Attribut | Symbolisierung | Begründung |
|---|---|---|---|
| `[eintragen]` | `[eintragen]` | `[eintragen]` | `[eintragen]` |

<!-- Lösungshinweise für Lehrende:
Übung 1:
1. qualitativ.
2. sequentiell.
3. divergierend mit neutralem Mittelpunkt bei 0.
4. qualitativ.

Übung 2/3:
- keine eindeutige Musterlösung; Aussageziel und Lesbarkeit müssen begründet werden.
- DGM zurückhaltend, Punkte kontrastreich, Polygonflächen transparent, Gewässer optional und dezent.
-->

## Zusammenfassung

* Symbolisierung ist Teil der fachlichen Aussage einer Karte.
* Kategorien benötigen unterscheidbare Symbole; geordnete Zahlenwerte benötigen eine sichtbare Ordnung.
* Qualitative, sequentielle und divergierende Paletten erfüllen unterschiedliche Aufgaben.
* Punkt-, Linien-, Polygon- und Rasterlayer benötigen jeweils angepasste Darstellungsentscheidungen.
* Farbe, Größe, Form, Linienbreite und Transparenz erzeugen eine visuelle Hierarchie.
* Der wichtigste Inhalt muss sich vom räumlichen Kontext abheben.
* Lesbarkeit, Farbzugänglichkeit und verständliche Legendenbezeichnungen müssen geprüft werden.

## Weiterführende Informationen

* [QGIS-Dokumentation: Eigenschaften und Symbolisierung von Vektorlayern](https://docs.qgis.org/latest/en/docs/user_manual/working_with_vector/vector_properties.html)
* [QGIS-Übung: Grundlagen der Symbolisierung](https://docs.qgis.org/latest/en/docs/training_manual/basic_map/symbology.html)
* [QGIS-Dokumentation: Rastereigenschaften und Symbolisierung](https://docs.qgis.org/latest/en/docs/user_manual/working_with_raster/raster_properties.html)

<!-- Notizen: Ab hier folgen Vermerke, welche als Gedankenstütze oder Erinnerung dienen, aber noch nicht in der vorhandenen Form veröffentlicht werden sollen. -->

<!--
Mögliche Abbildungen:
- qualitative, sequentielle und divergierende Palette nebeneinander
- Punkt, Linie, Polygon und Raster mit passenden visuellen Variablen
- dieselbe Karte ohne und mit klarer visueller Hierarchie
- problematische Rot-Grün-Karte und zugänglichere Alternative
- deckendes und transparentes Schutzgebietspolygon über einem Raster

Didaktisch wichtig:
- Symbolisierung nicht mit Klassifizierung vermischen: Hier Grundprinzipien, nächste Seite Klassengrenzen.
- Einzelsymbol als legitime und oft beste Lösung darstellen.
- Naturfarbassoziationen nur als mögliche Konvention, nicht als zwingende Regel erklären.
- Keine feste Pflichtliste sichtbarer Layer vorgeben; Relevanz zur Frage entscheidet.
-->
