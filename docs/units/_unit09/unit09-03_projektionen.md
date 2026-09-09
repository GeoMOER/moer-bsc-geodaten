---
title: Koordinatenreferenzsysteme & Projektionen
published: true
toc: true
header:
  image: /assets/images/unit09/hero-unit09.jpg
  image_description: "Breiter Blick auf Europa auf einer gekrümmten Erde mit feinem Koordinatengitter und markiertem Ort"
  caption: "KI-generierte Illustration, bearbeitet für diesen Kurs"
---

<!-- Introtext: An die vorherige Unterseite zu geographischen Koordinaten anknüpfen. -->

## Dieselbe Position, andere Zahlen

Auf der vorherigen Seite haben wir die Position Marburgs ungefähr durch das Koordinatenpaar `(8.77, 50.81)` beschrieben. In einem anderen Datensatz kann derselbe Ort jedoch Koordinatenwerte besitzen, die aus sechs oder sieben Ziffern bestehen. Beide Angaben können richtig sein – sie verwenden lediglich unterschiedliche **Koordinatenreferenzsysteme**.

Ein Koordinatenpaar ist daher nur dann eindeutig interpretierbar, wenn bekannt ist, auf welches räumliche Bezugssystem es sich bezieht.

> **Merksatz:** Koordinatenwerte und Koordinatenreferenzsystem gehören immer zusammen.

![Derselbe Referenzpunkt hat in WGS 84 die Winkelkoordinaten 8,77 Grad Ost und 50,81 Grad Nord; in ETRS89 UTM Zone 32N lautet das gerundete Zahlenpaar 483 795 Meter Ost und 5 628 722 Meter Nord.]({{ '/assets/images/unit09/crs-vergleich.svg' | relative_url }})

<!-- Möglicher Einstieg: Zwei unterschiedlich aussehende Koordinatenpaare desselben Ortes zeigen. -->

## Was ist ein Koordinatenreferenzsystem?

Ein **Koordinatenreferenzsystem**, kurz **CRS** nach dem englischen Begriff *Coordinate Reference System*, legt fest, wie Koordinaten mit Positionen auf der Erde verknüpft werden.

Ein CRS beschreibt unter anderem:

* welches vereinfachte Modell der Erde verwendet wird,
* wo Ursprung und Achsen des Koordinatensystems liegen,
* in welcher Einheit die Koordinaten angegeben werden und
* bei einem projizierten System, wie die Erdoberfläche auf eine Ebene übertragen wird.

Ohne diese Angaben sind Koordinaten lediglich Zahlen. Erst das CRS erlaubt einer GIS-Software, sie an der richtigen Stelle darzustellen und mit anderen Geodaten zu kombinieren.

## Die Erde ist nicht flach

Die Erde ist annähernd kugelförmig, ihre Oberfläche ist jedoch unregelmäßig. Für Berechnungen wird sie deshalb durch vereinfachte mathematische Modelle beschrieben. Häufig wird dafür ein an den Polen leicht abgeflachtes **Ellipsoid** verwendet.

Eine Karte, ein Bildschirm und ein Blatt Papier sind dagegen eben. Um die gekrümmte Erdoberfläche auf einer Ebene darzustellen, ist eine **Kartenprojektion** erforderlich.

Ein anschaulicher Vergleich ist die Schale einer Orange: Sie lässt sich nicht flach auf einen Tisch legen, ohne sie einzuschneiden, zu dehnen oder zu stauchen. Ähnlich entstehen auch bei der Übertragung der Erdoberfläche auf eine Karte unvermeidlich Verzerrungen.

<!-- Optional: Foto oder Schema einer aufgeschnittenen Orangenschale ergänzen. -->

## Jede Kartenprojektion verzerrt

Keine ebene Weltkarte kann gleichzeitig überall Form, Fläche, Entfernung und Richtung korrekt wiedergeben. Je nach Projektion werden unterschiedliche Eigenschaften möglichst gut erhalten.

| Eigenschaft | Leitfrage |
|---|---|
| Fläche | Werden gleich große Gebiete auf der Karte gleich groß dargestellt? |
| Form / Winkel | Bleiben lokale Formen und Winkel möglichst ähnlich? |
| Entfernung | Können Entfernungen in bestimmten Bereichen korrekt gemessen werden? |
| Richtung | Werden Richtungen von einem Ausgangspunkt korrekt dargestellt? |

Welche Verzerrung problematisch ist, hängt von der Fragestellung ab. Eine Weltkarte zur Darstellung von Länderflächen benötigt andere Eigenschaften als eine Navigationskarte oder eine detaillierte Karte von Hessen.

> **Wichtig:** Es gibt nicht die eine „beste“ Projektion. Es gibt nur Projektionen, die für einen bestimmten Raum und Zweck besser oder schlechter geeignet sind.

![Berechneter Vergleich: Dieselben geodätischen Referenzflächen mit 1000 Kilometern Radius liegen am Äquator und bei 70 Grad Nord. World Mercator (EPSG:3395) vergrößert die polnahe Fläche stark; Equal Earth (EPSG:8857) erhält die Flächenverhältnisse und verändert die Formen.]({{ '/assets/images/unit09/projektionsvergleich.svg' | relative_url }})

Die Umrisse der Referenzflächen wurden auf WGS 84 berechnet und anschließend in die beiden genannten CRS transformiert. Die Abbildung dient dem Vergleich der Projektionswirkung; Längen dürfen daraus nicht abgelesen werden.

## Geographische und projizierte Koordinatensysteme

Grundsätzlich unterscheiden wir zwei wichtige Gruppen von Koordinatenreferenzsystemen.

### Geographische Koordinatensysteme

Ein **geographisches Koordinatensystem** beschreibt Positionen auf dem Erdmodell durch Längen- und Breitengrade.

Typische Merkmale:

* Koordinaten sind Winkel und werden in **Grad** angegeben.
* Die Werte beschreiben Winkel und keine direkten Entfernungen.
* Das System kann große Teile der Erde oder die gesamte Erde abdecken.
* Ein bekanntes Beispiel ist **WGS 84**.

### Projizierte Koordinatensysteme

Ein **projiziertes Koordinatensystem** überträgt Positionen mithilfe einer Kartenprojektion auf eine Ebene.

Typische Merkmale:

* Koordinaten besitzen lineare Einheiten, in den hier behandelten Systemen **Meter**.
* Positionen werden als x- und y-Koordinaten beziehungsweise Rechts- und Hochwerte beschrieben.
* Entfernungen und Flächen lassen sich im geeigneten System sinnvoller berechnen.
* Das System ist meist für einen bestimmten Teil der Erde optimiert.

| Merkmal | geographisch | projiziert |
|---|---|---|
| typische Koordinaten | Länge und Breite | x und y |
| typische Einheit | Grad | Meter |
| räumlicher Einsatz | häufig global | häufig regional |
| Beispiel | WGS 84 | ETRS89 / UTM Zone 32N |

## WGS 84

**WGS 84** ist ein weltweit verwendetes geodätisches Referenzsystem. Es wird unter anderem für Positionsangaben des Global Positioning System (**GPS**) verwendet.

Im geographischen CRS **WGS 84** werden Positionen durch Längen- und Breitengrade in Grad angegeben. Marburg liegt darin ungefähr bei:

> Länge `8.77° E`, Breite `50.81° N`

WGS 84 eignet sich gut für die Speicherung und den Austausch weltweiter Positionsangaben. Die Einheit Grad ist jedoch für direkte Messungen von Strecken und Flächen unpraktisch: Ein Grad Länge entspricht am Äquator einer anderen Entfernung als in Deutschland.

## UTM

Das **Universal Transverse Mercator System**, kurz **UTM**, teilt die Erde in 60 jeweils 6 Längengrade breite Zonen. Für jede Zone wird eine passende Projektion verwendet. Dadurch bleiben die Verzerrungen innerhalb einer Zone vergleichsweise klein.

Deutschland liegt überwiegend in den UTM-Zonen 32 und 33. Marburg befindet sich in **Zone 32N**.

UTM-Koordinaten werden in Metern angegeben. Dadurch können Entfernungen innerhalb der geeigneten Zone anschaulich interpretiert und berechnet werden. Für amtliche Geodaten in Deutschland wird häufig **ETRS89 / UTM** verwendet.

> **Achtung:** „UTM“ allein reicht als Angabe nicht aus. Auch Zone, Nord- oder Südhalbkugel und geodätisches Referenzsystem müssen bekannt sein.

<!-- Optional: Weltkarte mit den UTM-Zonen und Hervorhebung der Zonen 32N und 33N ergänzen. -->

## EPSG-Codes

Die vollständigen Namen von Koordinatenreferenzsystemen können lang und ähnlich klingen. In GIS-Anwendungen werden CRS deshalb häufig durch einen standardisierten **EPSG-Code** identifiziert.

| EPSG-Code | Koordinatenreferenzsystem | Einheit | typischer Einsatz |
|---:|---|---|---|
| `EPSG:4326` | WGS 84 | Grad | GPS-Positionen und weltweite Geodaten |
| `EPSG:25832` | ETRS89 / UTM Zone 32N | Meter | regionale Geodaten in West- und Mitteldeutschland |
| `EPSG:25833` | ETRS89 / UTM Zone 33N | Meter | regionale Geodaten in Ostdeutschland |
| `EPSG:3857` | WGS 84 / Pseudo-Mercator | Meter | Darstellung in vielen Webkarten |

Ein EPSG-Code ist eine eindeutige Kennung. Er ist keine Qualitätsbewertung und sagt nicht, dass ein CRS für jede Fragestellung geeignet ist.

**Web Mercator** (`EPSG:3857`) ist für die schnelle Darstellung vieler Kartenkacheln im Internet praktisch. Daraus folgt nicht, dass die darüber dargestellten Fachdaten ursprünglich in diesem CRS gespeichert sein müssen. Für genaue Flächen- oder Entfernungsmessungen ist Web Mercator insbesondere über größere Gebiete nicht die erste Wahl.

<!-- Die konkreten EPSG-Beispiele vor Veröffentlichung bei Änderungen des regionalen Anwendungsbeispiels prüfen. -->

## Welches CRS ist geeignet?

Die Wahl eines CRS hängt vor allem von drei Fragen ab:

1. **Wo liegt das Untersuchungsgebiet?**  
   Ein regional optimiertes CRS sollte zum räumlichen Ausschnitt passen.

2. **Was soll mit den Daten geschehen?**  
   Für eine reine Darstellung gelten andere Anforderungen als für die Berechnung von Flächen oder Entfernungen.

3. **Mit welchen weiteren Daten sollen sie kombiniert werden?**  
   Gemeinsam verwendete Layer müssen räumlich korrekt aufeinander bezogen werden können.

Als einfache Orientierung für diesen Kurs gilt:

* Für globale Positionsangaben in Längen- und Breitengraden begegnet uns häufig `EPSG:4326`.
* Für regionale Analysen rund um Marburg ist ein geeignetes projiziertes CRS in Metern, beispielsweise `EPSG:25832`, meist sinnvoller.
* Das CRS eines vorhandenen Datensatzes sollte zunächst aus dessen Metadaten übernommen und nicht geraten werden.

## CRS zuweisen oder Daten transformieren?

Bei der Arbeit mit Geodaten sind zwei Vorgänge zu unterscheiden:

### CRS zuweisen

Beim **Zuweisen** wird einer GIS-Software mitgeteilt, in welchem CRS die vorhandenen Koordinaten bereits gespeichert sind. Die Koordinatenwerte selbst werden dabei nicht verändert.

Das ist nur dann richtig, wenn das CRS bekannt ist, aber in den Daten oder Metadaten fehlt beziehungsweise falsch eingetragen wurde.

### Daten transformieren

Beim **Transformieren** oder **Reprojizieren** werden die Koordinaten von einem bekannten CRS in ein anderes CRS umgerechnet. Dabei ändern sich die Zahlenwerte, die Position auf der Erde bleibt jedoch gleich.

| Vorgang | Koordinatenwerte | räumliche Position | Zweck |
|---|---|---|---|
| CRS zuweisen | bleiben gleich | wird neu interpretiert | vorhandenes CRS korrekt angeben |
| transformieren | ändern sich | bleibt gleich | Daten in ein anderes CRS überführen |

> **Häufiger Fehler:** Ein falsches CRS lässt sich nicht dadurch reparieren, dass nacheinander verschiedene Systeme ausprobiert werden. Zuerst muss anhand der Datenquelle, der Metadaten und der Werte ermittelt werden, welches CRS die Koordinaten tatsächlich besitzen.

[![Zuweisen ergänzt bei unveränderten Zahlen das aus Metadaten bekannte EPSG:4326. Transformieren nach EPSG:25832 rechnet 8,77 und 50,81 Grad in gerundet 483 795 und 5 628 722 Meter um. Gradwerte nur als Meter zu etikettieren ist falsch.]({{ '/assets/images/unit09/zuweisen-transformieren.svg' | relative_url }})]({{ '/assets/images/unit09/zuweisen-transformieren.svg' | relative_url }})

*Verfolgen Sie Zahlen und CRS-Angabe getrennt: Beim korrekten Zuweisen bleibt das Zahlenpaar erhalten; beim Transformieren bleibt der Ort erhalten. Das Zahlenbeispiel verwendet x, y und ist auf ganze Meter gerundet.*

## Typische CRS-Probleme erkennen

Ein fehlendes, falsch zugewiesenes oder ungeeignetes CRS kann sich unterschiedlich bemerkbar machen:

* Ein Layer erscheint an einer offensichtlich falschen Stelle.
* Zwei Layer desselben Gebietes liegen nicht übereinander.
* Ein Layer ist nicht sichtbar, weil er weit außerhalb des Kartenausschnitts liegt.
* Entfernungen oder Flächen besitzen unplausible Werte.
* Koordinaten in Grad werden irrtümlich wie Meter behandelt.
* Die Karte zeigt starke Verzerrungen für das Untersuchungsgebiet.

In solchen Fällen sollten zunächst folgende Informationen geprüft werden:

1. Welche Zahlenbereiche besitzen die Koordinaten?
2. Welche Einheit wird verwendet?
3. Welches CRS nennen Datenquelle und Metadaten?
4. Passt der räumliche Gültigkeitsbereich des CRS zum Untersuchungsgebiet?
5. Wurde das CRS nur zugewiesen oder wurden die Daten tatsächlich transformiert?

## Kurze Übung

### 1. Koordinaten zuordnen

Zwei Datensätze enthalten einen Punkt in der Nähe von Marburg:

* Datensatz A: `(8.77, 50.81)`
* Datensatz B: `(483000, 5629000)`

Welche Einheit und welche Art von Koordinatenreferenzsystem vermuten Sie jeweils? Welche zusätzliche Information benötigen Sie, bevor Sie die Punkte zuverlässig verwenden können?

### 2. Ein CRS auswählen

Welches der auf dieser Seite genannten CRS erscheint für die folgenden Zwecke grundsätzlich am geeignetsten?

1. Speicherung weltweiter GPS-Beobachtungen in Längen- und Breitengraden
2. Berechnung von Entfernungen zwischen Untersuchungsflächen rund um Marburg
3. Darstellung einer Hintergrundkarte in einem Webkartendienst

Begründen Sie Ihre Auswahl jeweils mit Einheit, räumlichem Einsatzbereich und Verwendungszweck.

### 3. Projektionen vergleichen

Betrachten Sie die Projektionsdarstellungen auf dieser Seite. Optional kann die Lehrperson zusätzlich dieselben Weltgeodaten in zwei Projektionen demonstrieren.

* Welche Regionen erscheinen besonders stark vergrößert oder verkleinert?
* Welche Formen unterscheiden sich sichtbar?
* Welche Karte würde sich für einen Vergleich von Länderflächen besser eignen?

<!-- Lösungshinweise für Lehrende:
Übung 1:
- A deutet auf ein geographisches CRS mit Gradwerten hin, beispielsweise WGS 84. Ohne CRS- und Achsenangabe bleibt dies eine Vermutung.
- B deutet auf ein projiziertes CRS mit Meterwerten hin, möglicherweise UTM. Zone und Referenzsystem müssen zusätzlich bekannt sein.

Übung 2:
- weltweite GPS-Beobachtungen: EPSG:4326
- regionale Entfernungen rund um Marburg: EPSG:25832
- Hintergrundkarte eines üblichen Webkartendienstes: EPSG:3857
- Die Auswahl ist an den hier beschriebenen vereinfachten Szenarien orientiert; konkrete Anforderungen können ein anderes CRS erfordern.

Übung 3:
- Ergebnis hängt von den ausgewählten Projektionen ab.
- Für Flächenvergleiche ist eine flächentreue Projektion geeigneter als Web Mercator.
-->

## Zusammenfassung

* Ein Koordinatenreferenzsystem legt fest, wie Koordinaten mit Positionen auf der Erde verknüpft werden.
* Bei der Übertragung der gekrümmten Erdoberfläche auf eine Ebene entstehen immer Verzerrungen.
* Geographische CRS verwenden Winkelkoordinaten; projizierte CRS verwenden lineare Koordinaten.
* WGS 84 ist ein global verbreitetes Referenzsystem; UTM arbeitet mit regionalen Zonen.
* EPSG-Codes identifizieren Koordinatenreferenzsysteme eindeutig.
* Das geeignete CRS hängt von Untersuchungsgebiet, Fragestellung und gewünschter Berechnung ab.
* Beim Zuweisen eines CRS bleiben Koordinatenwerte gleich; beim Transformieren werden sie umgerechnet.
* CRS-Angaben sollten aus verlässlichen Metadaten übernommen und nicht durch Ausprobieren geraten werden.

<!-- Notizen: Ab hier folgen Vermerke, welche als Gedankenstütze oder Erinnerung dienen, aber noch nicht in der vorhandenen Form veröffentlicht werden sollen. -->

<!--
Möglicher Einstieg im Seminar:
- Koordinaten von Marburg in EPSG:4326 und EPSG:25832 nebeneinanderstellen.
- Frage: Wie können beide Zahlenpaare denselben Ort beschreiben?

Mögliche Demonstrationen:
- Globus beziehungsweise Orange gedanklich oder tatsächlich „abwickeln“
- Grönland in Web Mercator und einer flächentreuen Weltkarte vergleichen
- denselben Punkt in WGS 84 und ETRS89 / UTM Zone 32N anzeigen
- einen Layer mit falsch zugewiesenem CRS demonstrieren
- Zuweisen und Transformieren direkt gegenüberstellen

Didaktische Begrenzung:
- keine Projektionsformeln
- Geoid, Ellipsoid und Datum nur so weit erläutern, wie sie für das Verständnis eines CRS nötig sind
- keine vollständige Systematik von Projektionsfamilien

Anschluss an Unit 10:
- Wie erkennt und verwaltet QGIS die CRS verschiedener Layer und des Kartenprojekts?
-->
