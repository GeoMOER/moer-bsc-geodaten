---
title: Linien und Polygone
published: true
toc: true
header:
  image: /assets/images/unit12/hero-unit12.jpg
  image_description: "Flusslandschaft mit Schutzgebietsfläche und Beobachtungspunkten innerhalb und außerhalb des Gebietes"
  caption: "KI-generierte Illustration, bearbeitet für diesen Kurs"
---

<!-- Introtext: Das in Unit 11 behandelte Punktmodell um Linien und Polygone erweitern. -->

## Das vollständige grundlegende Vektormodell

Das Vektormodell beschreibt räumliche Objekte mithilfe von Koordinaten. In Unit 11 haben wir Punkte als einzelne Positionen untersucht. Nun ergänzen wir die beiden weiteren grundlegenden Geometrietypen:

* **Punkt:** einzelne Position,
* **Linie:** räumlicher Verlauf,
* **Polygon:** geschlossene Fläche.

Jedes Vektorfeature verbindet seine Geometrie mit einer Zeile in der Attributtabelle.

> **Merksatz:** Die Geometrie beschreibt, **wo und in welcher Form** ein Feature liegt. Die Attribute beschreiben, **welche Eigenschaften** es besitzt.

## Wie entsteht eine Linie?

Eine Linie besteht aus mindestens zwei geordneten **Stützpunkten** beziehungsweise **Vertices**. Benachbarte Stützpunkte werden durch gerade Segmente verbunden. Gemeinsam bilden sie den Linienverlauf.

Je mehr Stützpunkte verwendet werden, desto detaillierter kann ein gekrümmter Verlauf angenähert werden. Eine digitale Linie ist dennoch ein Modell und nicht der reale Fluss oder die reale Straße selbst.

Typische Linienfeatures sind:

* Flüsse und Bäche,
* Straßen und Wege,
* Bahnstrecken,
* Leitungen,
* Wander- oder Bewegungsrouten und
* Grenzen, wenn nur ihr Verlauf betrachtet wird.

<!-- Optional: Eine vereinfachte und eine detaillierte Linie mit sichtbaren Stützpunkten gegenüberstellen. -->

## Was kann eine Linie beschreiben?

Eine Linie besitzt eine dargestellte Länge, aber keine dargestellte Fläche. Ihre Strichbreite auf der Karte dient der Lesbarkeit und entspricht nicht automatisch der realen Breite des Objektes.

Ein Fluss kann beispielsweise als dünne Linie symbolisiert werden, obwohl er in der Realität mehrere Meter breit ist. Wird die tatsächliche Wasserfläche benötigt, ist ein Polygon geeigneter.

Linien können außerdem eine Richtung besitzen. Bei einem Gewässernetz kann die Reihenfolge der Stützpunkte beispielsweise für die Fließrichtung relevant sein. Ob und wie diese Richtung gespeichert wurde, muss aus Datenmodell und Metadaten hervorgehen.

## Wie entsteht ein Polygon?

Ein Polygon wird durch eine geschlossene Folge von Stützpunkten begrenzt. Der erste und letzte Punkt des äußeren Rings fallen zusammen. Dadurch entstehen:

* eine Grenze,
* ein Inneres und
* eine räumliche Fläche.

Typische Polygonfeatures sind:

* Schutzgebiete,
* Verwaltungsgebiete,
* Gebäudegrundrisse,
* Seen,
* Flurstücke,
* Landbedeckungsflächen und
* Untersuchungsgebiete.

Ein Polygon kann zusätzlich **Löcher** besitzen. Ein Schutzgebiet könnte beispielsweise eine nicht geschützte Fläche vollständig umschließen. Diese Innenfläche gehört dann geometrisch nicht zum Polygon.

<!-- Optional: Polygon mit äußerem Ring und Loch darstellen. -->

## Multipart-Geometrien

Ein einzelnes Feature kann aus mehreren räumlich getrennten Teilen bestehen. Dies wird als **Multipart-Geometrie** bezeichnet.

Beispiele:

* ein Schutzgebiet mit mehreren getrennten Teilflächen,
* ein Verwaltungsgebiet mit Inseln,
* ein Flussfeature mit mehreren getrennten Abschnitten oder
* ein Staat mit räumlich getrennten Gebietsteilen.

Alle Teile gehören dabei zu derselben Zeile in der Attributtabelle. Die Anzahl der Tabellenzeilen entspricht deshalb nicht immer der Anzahl sichtbarer Einzelflächen oder Linienabschnitte.

> **Prüffrage:** Beschreibt eine Zeile genau eine zusammenhängende Geometrie oder ein Feature mit mehreren Teilen?

[![Ein Polygon mit Loch und ein Multipart-Feature mit zwei getrennten Polygonteilen besitzen jeweils eine Tabellenzeile. Die Lochfläche ist ausgespart; die beiden Multipart-Flächen gehören zusammen zu Feature B.]({{ '/assets/images/unit12/polygon-loch-multipart.svg' | relative_url }})]({{ '/assets/images/unit12/polygon-loch-multipart.svg' | relative_url }})

*Beide Beispiele sind schematisch. Zählen Sie Features anhand der Tabellenzeilen und IDs, nicht anhand der sichtbaren Teilflächen. Ein Loch ist eine ausgesparte Innenfläche und kein zusätzlicher Teil des Polygons.*

## Features und Attribute

Ein Gewässerlayer könnte für jeden Gewässerabschnitt eine Liniengeometrie und folgende Attribute enthalten:

| gewaesser_id | name | typ | ordnung | Geometrie |
|---:|---|---|---:|---|
| 101 | Lahn | Fließgewässer | 1 | Linie |
| 102 | Allna | Fließgewässer | 2 | Linie |

Ein Schutzgebietslayer könnte jedes Gebiet als Polygon mit weiteren Eigenschaften speichern:

| gebiet_id | name | kategorie | ausweisung | Geometrie |
|---:|---|---|---:|---|
| 201 | Beispielgebiet A | Naturschutzgebiet | 1990 | Polygon |
| 202 | Beispielgebiet B | Landschaftsschutzgebiet | 2004 | Polygon |

Die Geometrie erlaubt räumliche Fragen. Die Attribute erlauben sachliche Fragen. Häufig werden beide kombiniert, beispielsweise:

> Welche Naturschutzgebiete werden von einem bestimmten Gewässer geschnitten?

## Dasselbe Objekt, verschiedene Geometrien

Der geeignete Geometrietyp hängt von Maßstab und Fragestellung ab.

### Fluss

* als **Linie**, wenn Verlauf, Länge oder Netzwerk wichtig sind,
* als **Polygon**, wenn Wasserfläche und Breite untersucht werden.

### Straße

* als **Linie**, wenn Verbindungen und Strecken betrachtet werden,
* als **Polygon**, wenn versiegelte Fläche oder genaue Fahrbahnbreite relevant sind.

### Schutzgebiet

* als **Polygon**, wenn Ausdehnung und enthaltene Objekte wichtig sind,
* als **Punkt**, wenn auf einer sehr kleinen Übersichtskarte nur die ungefähre Lage gezeigt wird.

### Stadt

* als **Punkt** auf einer Deutschlandkarte,
* als **Polygon** bei einer Analyse des Stadtgebietes,
* als Netz aus **Linien** bei einer Untersuchung des Straßensystems.

Es gibt daher nicht für jedes reale Objekt genau einen immer richtigen Geometrietyp.

## Maßstab und Generalisierung

Vektorgeometrien werden passend zu einem bestimmten Maßstab und Zweck erzeugt. Bei einer **Generalisierung** werden Details vereinfacht, zusammengefasst oder weggelassen.

Eine Flusslinie kann in einem detaillierten Datensatz viele Windungen enthalten und in einer Übersichtskarte stark vereinfacht sein. Beide Darstellungen können für ihren jeweiligen Zweck korrekt sein.

Für die gemeinsame Analyse sollten Daten deshalb einen passenden Detailgrad besitzen. Eine hochpräzise Schutzgebietsgrenze wird durch die Kombination mit einem sehr groben Gewässerdatensatz nicht automatisch zu einer hochpräzisen Gesamtanalyse.

[![Derselbe schematische Linienzug wird mit neun und mit fünf übernommenen Stützpunkten dargestellt. Anfang und Ende bleiben erhalten, einige Windungen entfallen; die ursprüngliche Linie ist zum Vergleich gestrichelt eingezeichnet.]({{ '/assets/images/unit12/stuetzpunkte-generalisierung.svg' | relative_url }})]({{ '/assets/images/unit12/stuetzpunkte-generalisierung.svg' | relative_url }})

*Jedes Segment verbindet zwei Stützpunkte. Der Vergleich hält die Endpunkte konstant und reduziert die Zwischenpunkte. Mehr Stützpunkte ermöglichen mehr Details, belegen aber allein keine bessere Lagegenauigkeit.*

## Grenzen sind Modelle

Ein Polygon vermittelt häufig den Eindruck einer scharf festgelegten Grenze. In der Realität können Grenzen jedoch sehr unterschiedlich entstehen:

* rechtlich festgelegte Verwaltungs- oder Schutzgebietsgrenzen,
* aus Luftbildern interpretierte Landbedeckungsgrenzen,
* im Gelände eingemessene Objektgrenzen,
* aus Schwellenwerten abgeleitete Zonen oder
* unscharfe ökologische Übergänge.

Die Linie im Datensatz zeigt deshalb nicht automatisch, wie genau, aktuell oder eindeutig die reale Grenze ist. Dafür müssen Erhebungsmethode, Maßstab und Lagegenauigkeit geprüft werden.

## Räumliche Beziehungen

![Beobachtungspunkte und Gewässerlinien können anhand ihrer räumlichen Beziehung zu Schutzgebietspolygonen ausgewählt werden.]({{ '/assets/images/unit12/vektor-workflow.svg' | relative_url }})

Vektorgeometrien erlauben Fragen nach ihrer Lage zueinander. Wichtige räumliche Beziehungen sind:

| Beziehung | Beispiel |
|---|---|
| innerhalb | ein Beobachtungspunkt liegt innerhalb eines Schutzgebietes |
| enthält | ein Schutzgebiet enthält einen Beobachtungspunkt |
| schneidet | ein Gewässer schneidet ein Schutzgebiet |
| berührt | zwei Polygone teilen eine Grenze, überlappen aber nicht |
| überlappt | zwei Flächen besitzen einen gemeinsamen Teilbereich |
| getrennt | zwei Features besitzen keinen gemeinsamen Ort |

Die Richtung der Frage ist wichtig:

* Der Punkt liegt **innerhalb** des Polygons.
* Das Polygon **enthält** den Punkt.

Bei einem Punkt genau auf der Polygongrenze können die Ergebnisse je nach gewählter Beziehung unterschiedlich sein. In der Praxis muss die Auswahlregel deshalb ausdrücklich dokumentiert werden.

![A liegt im Polygon, B genau auf dessen Grenze und C außerhalb. Intersects wählt A und B aus; within wählt nur A. Die Unsicherheit der ursprünglichen Koordinaten bleibt bestehen.]({{ '/assets/images/unit12/punkt-auf-polygongrenze.svg' | relative_url }})

*Für unsere Punktauswahl berücksichtigt „schneidet“ (`intersects`) auch den Randpunkt. „Liegt innerhalb“ (`within`) schließt ihn aus. Die Tabelle gilt für Punkte relativ zum Polygon.*

## Räumliche Auswahl und räumliche Überlagerung

Zwei ähnliche Arbeitsschritte müssen unterschieden werden:

### Räumliche Auswahl

Eine räumliche Auswahl markiert vollständige Features anhand ihrer Beziehung zu einem zweiten Layer. Beispiel:

> Wähle alle GBIF-Punkte, die Schutzgebietspolygone schneiden.

Die Geometrien der ausgewählten Punkte werden dabei nicht verändert.

### Räumliche Überlagerung

Eine Überlagerungsoperation kann neue Geometrien erzeugen. Eine Linie kann beispielsweise an der Grenze eines Polygons geschnitten werden, sodass nur der innerhalb liegende Abschnitt übrig bleibt.

In dieser Unit liegt der Schwerpunkt zunächst auf der **Auswahl nach Position**. Komplexere Überlagerungen folgen in späteren GIS-Veranstaltungen.

Der [Vergleich von Auswahl und Zuschneiden]({{ '/unit12/unit12-03_vektoren_qgis.html#auswahl-und-ergebnis-unterscheiden' | relative_url }}) zeigt den Unterschied an derselben Linie und demselben Polygon.

## Länge und Fläche messen

Linien besitzen eine Länge, Polygone eine Fläche und einen Umfang. Verlässliche Messungen setzen ein geeignetes CRS voraus.

Geographische Koordinaten in Grad sind für direkte Meter- oder Quadratmeterberechnungen ungeeignet. Für das Gebiet um Marburg ist beispielsweise ein passendes projiziertes CRS in Metern erforderlich.

Prüfen Sie vor einer Messung:

* CRS des Layers,
* CRS beziehungsweise Berechnungseinstellungen des Projekts,
* verwendete Einheit,
* räumliche Gültigkeit des CRS und
* Genauigkeit der Ausgangsgeometrie.

> **Wichtig:** Viele Nachkommastellen in einem berechneten Flächenwert bedeuten nicht, dass die Ausgangsgrenze ebenso genau bekannt ist.

## Geometriequalität

Fehlerhafte Geometrien können räumliche Operationen und Messungen beeinflussen. Beispiele sind:

* sich selbst schneidende Polygonringe,
* ungewollte Lücken oder Überlappungen,
* doppelte Stützpunkte,
* sehr kleine Restflächen und
* unterbrochene Linien in einem erwarteten Netzwerk.

QGIS besitzt Werkzeuge zum Prüfen und Reparieren von Geometrien. Für den Einstieg genügt die Erkenntnis, dass ein sichtbarer Layer nicht automatisch geometrisch fehlerfrei ist. Reparaturen sollten nur an einer Kopie erfolgen und dokumentiert werden.

## Häufige Vektorformate

Vektordaten können in verschiedenen Formaten gespeichert werden.

### GeoPackage

Ein **GeoPackage** besitzt die Endung `.gpkg` und kann mehrere Vektor- und Rasterlayer in einer Datei speichern. Es unterstützt moderne Feldnamen und eignet sich gut für QGIS-Projekte und den Datenaustausch.

### GeoJSON

**GeoJSON** ist ein textbasiertes Format, das im Web häufig verwendet wird. Es ist gut lesbar und austauschbar, kann bei großen Datenmengen jedoch umfangreich werden.

### Shapefile

Das **Shapefile** ist ein älteres, weiterhin verbreitetes Vektorformat. Ein Shapefile besteht aus mehreren zusammengehörigen Dateien, mindestens häufig `.shp`, `.shx` und `.dbf`; die CRS-Information liegt meist in einer zusätzlichen `.prj`-Datei.

Fehlt eine dieser Dateien oder wird nur `.shp` weitergegeben, kann der Datensatz unvollständig sein. Zudem besitzt das Format Einschränkungen bei Feldnamen, Datentypen und Zeichencodierung.

> **Praxisregel:** Verwenden Sie für neue Arbeitsergebnisse nach Möglichkeit ein GeoPackage. Behandeln Sie alle Bestandteile eines erhaltenen Shapefiles als eine gemeinsame Dateneinheit.

## Kurze Übung

### 1. Geometrietyp auswählen

Wählen Sie für jede Fragestellung einen geeigneten Geometrietyp:

1. Wo mündet ein Nebenfluss in die Lahn?
2. Wie verläuft ein Gewässer?
3. Welche Fläche besitzt ein Naturschutzgebiet?
4. Welche Wanderroute verbindet zwei Orte?
5. In welchem Landkreis liegt eine Beobachtung?

### 2. Räumliche Beziehung benennen

Formulieren Sie die passende Beziehung:

1. Ein GBIF-Punkt befindet sich vollständig in einem Schutzgebiet.
2. Ein Gewässer tritt in ein Schutzgebiet ein und verlässt es wieder.
3. Zwei Gemeindegebiete besitzen eine gemeinsame Grenze.

### 3. Modellgrenzen erklären

Warum kann eine als Linie gespeicherte Straße nicht direkt zur Berechnung ihrer versiegelten Fläche verwendet werden? Welche zusätzliche Information oder Geometrie wäre nötig?

<!-- Lösungshinweise für Lehrende:
Übung 1:
1. Punkt.
2. Linie.
3. Polygon.
4. Linie.
5. Beobachtung als Punkt und Landkreis als Polygon; Antwort über räumliche Beziehung.

Übung 2:
1. Punkt innerhalb Polygon beziehungsweise Polygon enthält Punkt.
2. Linie schneidet Polygon.
3. Polygone berühren sich.

Übung 3:
- Linie besitzt keine dargestellte Breite oder Fläche.
- benötigt wird beispielsweise ein Straßenpolygon oder eine fachlich begründete Breite zur Ableitung einer Fläche.
-->

## Zusammenfassung

* Linien bestehen aus geordneten Stützpunkten und beschreiben räumliche Verläufe.
* Polygone besitzen geschlossene Ringe und beschreiben Grenzen und Flächen.
* Multipart-Geometrien können mehrere getrennte Teile in einem Feature zusammenfassen.
* Geometrietyp, Maßstab und Generalisierung werden passend zur Fragestellung gewählt.
* Grenzen in Geodaten sind Modelle mit unterschiedlicher rechtlicher, methodischer und räumlicher Genauigkeit.
* Vektorfeatures können Beziehungen wie innerhalb, enthält, schneidet oder berührt besitzen.
* Räumliche Auswahl markiert Features; Überlagerungsoperationen können neue Geometrien erzeugen.
* Längen und Flächen müssen in einem geeigneten CRS und mit angemessener Genauigkeit berechnet werden.
* GeoPackage ist für neue Arbeitsergebnisse meist geeigneter als das ältere Shapefile.

<!-- Notizen: Ab hier folgen Vermerke, welche als Gedankenstütze oder Erinnerung dienen, aber noch nicht in der vorhandenen Form veröffentlicht werden sollen. -->

<!--
Mögliche Abbildungen:
- Linie mit Stützpunkten und Segmenten
- Polygon mit äußerem Ring und Loch
- Singlepart versus Multipart
- dieselbe Straße als Linie und Polygon
- räumliche Beziehungen Punkt/Linie/Polygon

Didaktisch wichtig:
- Strichbreite und reale Objektbreite unterscheiden.
- Polygonkante nicht automatisch als exakt interpretieren.
- „innerhalb“ und „enthält“ als gerichtete Formulierungen üben.
- Auswahl nicht mit geometrischem Zuschneiden verwechseln.

Anschluss an unit12-02_geoportale.md:
- Wie finden wir geeignete Linien- und Polygondaten, und welche Metadaten müssen vor dem Einsatz geprüft werden?
-->
