---
title: Einführung in QGIS
published: true
toc: true
header:
  image: /assets/images/spotlight01/jekyll_github_pages.png
  image_description: "Cutout from Measured carbon dioxide concentrations in Vancouver"
  caption: "Bild: [jekyll](https://jekyllrb.com/)"
---

<!-- Introtext: Vom konzeptionellen Datenmodell zur praktischen Arbeit in einem GIS. -->

## Was ist ein GIS?

Ein **Geoinformationssystem**, kurz **GIS**, ist eine Softwareumgebung zum Erfassen, Verwalten, Darstellen, Untersuchen und Analysieren von Geodaten. Es verbindet räumliche Geometrien und Rasterwerte mit den zugehörigen Sachdaten.

Mit einem GIS können wir beispielsweise:

* Punkt-, Linien-, Polygon- und Rasterdaten gemeinsam darstellen,
* Eigenschaften einzelner Objekte untersuchen,
* Layer nach Attributen filtern und unterschiedlich symbolisieren,
* Koordinatenreferenzsysteme prüfen und transformieren,
* räumliche Beziehungen analysieren und
* Karten für die Weitergabe von Ergebnissen erstellen.

In diesem Kurs verwenden wir **QGIS**. QGIS ist ein freies und quelloffenes Geoinformationssystem, das auf verschiedenen Betriebssystemen genutzt werden kann.

> **Merksatz:** Ein GIS ist mehr als ein Zeichenprogramm für Karten. Es verknüpft räumliche Darstellung, Datenverwaltung und Analyse.

## Projekt, Layer und Datendatei

Zu Beginn müssen drei Begriffe klar voneinander unterschieden werden.

### QGIS-Projekt

Ein **QGIS-Projekt** speichert den aktuellen Arbeitsstand. Dazu gehören beispielsweise:

* die eingebundenen Layer,
* deren Reihenfolge und Darstellung,
* der aktuelle Kartenausschnitt,
* das CRS des Projekts und
* gegebenenfalls erstellte Kartenlayouts.

Die Projektdatei besitzt üblicherweise die Dateiendung `.qgz`. Sie enthält in der Regel nicht automatisch alle verwendeten Geodatensätze, sondern verweist auf deren Speicherorte.

### Layer

Ein **Layer** ist eine in QGIS eingebundene räumliche Informationsebene. Ein Projekt kann beispielsweise getrennte Layer für Straßen, Gewässer, Gemeindegrenzen und Höhenwerte enthalten.

Layer können aus lokalen Dateien, Datenbanken oder webbasierten Diensten stammen. Ihre Reihenfolge beeinflusst, was in der Kartenansicht sichtbar ist.

### Datendatei

Die **Datendatei** enthält die eigentlichen Geodaten. Eine Datei kann einen oder mehrere Layer enthalten. Beispiele sind ein GeoPackage, eine GeoJSON-Datei oder ein GeoTIFF.

| Begriff | enthält beziehungsweise beschreibt | Beispiel |
|---|---|---|
| Projekt | Arbeitsstand und Verweise | `uebung10.qgz` |
| Layer | in QGIS verwendete Informationsebene | `gemeinden` |
| Datendatei | gespeicherte Geodaten | `hessen.gpkg` |

> **Wichtig:** Wird nur die Projektdatei weitergegeben, fehlen auf einem anderen Rechner möglicherweise die zugehörigen Datendateien.

## Die QGIS-Oberfläche

Die genaue Anordnung kann je nach Betriebssystem und persönlicher Einstellung etwas unterschiedlich aussehen. Die grundlegenden Bereiche bleiben jedoch gleich.

### Menüleiste und Werkzeugleisten

Die **Menüleiste** bietet Zugriff auf die Funktionen von QGIS. Häufig verwendete Werkzeuge sind zusätzlich als Symbole in **Werkzeugleisten** erreichbar.

Am Anfang benötigen wir vor allem Werkzeuge zum:

* Öffnen und Speichern von Projekten,
* Hinzufügen von Daten,
* Vergrößern und Verkleinern des Kartenausschnitts,
* Verschieben der Karte,
* Auswählen von Features und
* Abfragen von Objektinformationen.

### Browser

Der **Browser** zeigt Datenquellen an, die QGIS öffnen kann. Dazu gehören Ordner und Dateien auf dem Rechner, GeoPackages, Datenbanken sowie eingerichtete Webdienste.

Viele Datensätze können aus dem Browser durch Doppelklick oder per Drag-and-drop in das Projekt geladen werden.

### Layer-Bereich

Der **Layer-Bereich** listet alle Layer des aktuellen Projekts auf. Hier können Layer:

* ein- und ausgeblendet,
* umbenannt,
* gruppiert,
* in ihrer Reihenfolge verändert und
* aus dem Projekt entfernt werden.

Das Entfernen eines Layers aus dem Projekt löscht normalerweise nicht die ursprüngliche Datendatei.

### Kartenansicht

Die **Kartenansicht** zeigt die sichtbaren Layer. Der dargestellte Ausschnitt kann verschoben, vergrößert und verkleinert werden. Die Kartenansicht ist keine eigene Datendatei, sondern eine aktuelle Darstellung der eingebundenen Daten.

### Statusleiste

Die **Statusleiste** enthält unter anderem Informationen zu Maßstab, Mauskoordinaten und dem CRS des Projekts. Diese Angaben helfen dabei, die aktuelle Darstellung räumlich einzuordnen.

<!-- Optional: Aktuellen Screenshot der QGIS-Oberfläche mit Beschriftung der fünf Bereiche ergänzen. -->

## Einen Arbeitsordner vorbereiten

Eine klare Dateiablage verhindert viele spätere Probleme. Legen Sie für die Übung einen eigenen Ordner an, beispielsweise:

```text
unit10_qgis/
  data/
  output/
  unit10_qgis.qgz
```

* In `data` liegen unveränderte Ausgangsdaten.
* In `output` werden neu erzeugte Dateien gespeichert.
* Die Projektdatei liegt im übergeordneten Arbeitsordner.

Verwenden Sie eindeutige Dateinamen und vermeiden Sie es, Eingabedaten versehentlich zu überschreiben.

## Ein neues Projekt anlegen

1. Starten Sie QGIS.
2. Erstellen Sie ein neues, leeres Projekt.
3. Speichern Sie es sofort unter einem aussagekräftigen Namen im vorbereiteten Arbeitsordner.
4. Prüfen Sie in der Statusleiste beziehungsweise in den Projekteigenschaften das **Projekt-CRS**.
5. Speichern Sie das Projekt während der Arbeit regelmäßig.

Das Projekt-CRS bestimmt, in welchem Koordinatenreferenzsystem die Layer gemeinsam in der Kartenansicht dargestellt werden. QGIS kann Layer mit unterschiedlichen bekannten CRS für die Anzeige dynamisch in das Projekt-CRS transformieren.

> **Achtung:** Die dynamische Darstellung verändert nicht automatisch das CRS der ursprünglichen Datendatei.

## Lokale Daten laden

QGIS bietet mehrere Wege, lokale Geodaten zu öffnen. Zwei besonders wichtige sind:

* über den **Browser** und
* über den **Datenquellenmanager**.

### Über den Browser

1. Navigieren Sie im Browser zum Arbeitsordner.
2. Öffnen Sie den Ordner `data`.
3. Prüfen Sie, welche Datensätze QGIS erkennt.
4. Ziehen Sie einen Datensatz in die Kartenansicht oder doppelklicken Sie auf den gewünschten Layer.

### Über den Datenquellenmanager

1. Öffnen Sie den Datenquellenmanager.
2. Wählen Sie passend zum Datensatz beispielsweise **Vektor** oder **Raster**.
3. Wählen Sie die Datei aus.
4. Fügen Sie den gewünschten Layer dem Projekt hinzu.

Nach dem Laden erscheint der Layer im Layer-Bereich und – sofern Position und CRS korrekt sind – in der Kartenansicht.

## In der Karte navigieren

Für die erste Orientierung genügen wenige Werkzeuge:

* **Verschieben:** Kartenausschnitt bewegen, ohne die Daten zu verändern.
* **Vergrößern und Verkleinern:** Maßstab der Darstellung ändern.
* **Auf Layer zoomen:** Kartenausschnitt auf die räumliche Ausdehnung eines Layers setzen.
* **Gesamtausdehnung anzeigen:** alle sichtbaren Daten in der Kartenansicht erfassen.

Wenn ein geladener Layer nicht sichtbar erscheint, zoomen Sie zunächst auf seine Ausdehnung. Bleibt er an einer unplausiblen Stelle, prüfen Sie Datenquelle und CRS.

## Layer organisieren

Die Reihenfolge im Layer-Bereich entspricht einer Stapelung von oben nach unten. Oben liegende Flächen- oder Rasterlayer können darunterliegende Layer verdecken.

Probieren Sie aus:

1. Layer mit dem Kontrollkästchen ein- und auszublenden,
2. die Reihenfolge per Drag-and-drop zu verändern,
3. einen Layer sinnvoll umzubenennen und
4. mehrere zusammengehörige Layer in einer Gruppe zu organisieren.

Ein umbenannter Layer erhält im Projekt lediglich einen neuen Anzeigenamen. Der Name der ursprünglichen Datendatei wird dadurch nicht verändert.

## Features und Attribute untersuchen

Bei einem Vektorlayer können Sie räumliche Objekte und ihre Sachdaten gemeinsam untersuchen.

### Objektinformationen abfragen

Aktivieren Sie den gewünschten Layer und verwenden Sie das Werkzeug zum **Abfragen von Objekten**. Klicken Sie anschließend auf ein Feature in der Karte. QGIS zeigt die zugehörigen Attribute an.

### Attributtabelle öffnen

Öffnen Sie über das Kontextmenü eines Vektorlayers die **Attributtabelle**. Prüfen Sie:

* Wie viele Zeilen und Spalten enthält die Tabelle?
* Welche Spalte könnte als eindeutige ID dienen?
* Welche Datentypen besitzen die Attribute?
* Welches Tabellenobjekt gehört zu einem ausgewählten Feature?

Die Auswahl ist miteinander verknüpft: Ein in der Karte ausgewähltes Feature kann in der Tabelle hervorgehoben werden und umgekehrt.

## Eigenschaften und CRS eines Layers prüfen

Öffnen Sie die Eigenschaften eines Layers und suchen Sie nach Informationen zu:

* Datenquelle und Speicherort,
* Geometrietyp beziehungsweise Rastertyp,
* räumlicher Ausdehnung,
* Koordinatenreferenzsystem,
* Attributfeldern oder Rasterbändern und
* Darstellung beziehungsweise Symbolisierung.

Notieren Sie den EPSG-Code des Layers und vergleichen Sie ihn mit dem Projekt-CRS. Unterschiedliche CRS sind nicht automatisch ein Fehler, solange sie korrekt definiert sind und QGIS sie für die Darstellung transformieren kann.

## Praktische Übung

Verwenden Sie die in der Lehrveranstaltung bereitgestellten Daten.

1. Legen Sie den beschriebenen Arbeitsordner an.
2. Erstellen und speichern Sie ein neues QGIS-Projekt.
3. Laden Sie mindestens einen Vektor- und einen Rasterlayer.
4. Ordnen Sie die Layer so an, dass beide sinnvoll sichtbar sind.
5. Zoomen Sie auf die Ausdehnung des Vektorlayers.
6. Öffnen Sie dessen Attributtabelle und wählen Sie ein Feature aus.
7. Fragen Sie dasselbe Feature in der Kartenansicht ab.
8. Notieren Sie für beide Layer:
   * Namen,
   * Datenquelle,
   * Datenmodell,
   * CRS beziehungsweise EPSG-Code und
   * räumliche Ausdehnung.
9. Speichern Sie das Projekt und schließen Sie QGIS.
10. Öffnen Sie das Projekt erneut und prüfen Sie, ob alle Layer weiterhin gefunden werden.

<!-- Vor Veröffentlichung konkrete Daten, Downloadpfad und erwartete Layernamen ergänzen. -->

## Typische Probleme

| Problem | mögliche Ursache | erster Prüfschritt |
|---|---|---|
| Layer wird nicht angezeigt | Kartenausschnitt liegt an anderer Stelle | auf Layerausdehnung zoomen |
| Layer liegt an falscher Position | CRS fehlt oder ist falsch zugewiesen | Layer-CRS und Metadaten prüfen |
| Projekt zeigt ein rotes Ausrufezeichen | Datendatei wurde verschoben oder umbenannt | Datenpfad reparieren |
| Attributtabelle lässt sich nicht öffnen | gewählter Layer ist kein Vektorlayer | Datenmodell prüfen |
| ein Layer verdeckt andere | ungünstige Layerreihenfolge | Reihenfolge im Layer-Bereich ändern |
| Änderungen fehlen nach Neustart | Projekt wurde nicht gespeichert | Projekt erneut speichern |

## Zusammenfassung

* QGIS verbindet räumliche Darstellung, Datenverwaltung und Analyse.
* Ein Projekt speichert den Arbeitsstand und verweist auf die verwendeten Datenquellen.
* Layer sind räumliche Informationsebenen innerhalb eines Projekts.
* Browser, Layer-Bereich, Kartenansicht, Werkzeugleisten und Statusleiste bilden die wichtigsten Teile der Oberfläche.
* Vektor- und Rasterdaten können über Browser oder Datenquellenmanager geladen werden.
* Bei Vektorlayern sind Features in der Karte mit Zeilen der Attributtabelle verknüpft.
* Das CRS von Layer und Projekt sollte geprüft, aber nicht miteinander verwechselt werden.
* Eine klare Ordnerstruktur und regelmäßiges Speichern verhindern viele typische Fehler.

## Weiterführende Informationen

* [QGIS-Benutzerhandbuch](https://docs.qgis.org/latest/en/docs/user_manual/)
* [QGIS-Oberfläche](https://docs.qgis.org/latest/en/docs/user_manual/introduction/qgis_gui.html)
* [Daten in QGIS öffnen](https://docs.qgis.org/latest/en/docs/user_manual/managing_data_source/opening_data.html)
* [Arbeiten mit QGIS-Projekten](https://docs.qgis.org/latest/en/docs/user_manual/introduction/project_files.html)

<!-- Notizen: Ab hier folgen Vermerke, welche als Gedankenstütze oder Erinnerung dienen, aber noch nicht in der vorhandenen Form veröffentlicht werden sollen. -->

<!--
Didaktische Hinweise:
- Oberfläche nicht vollständig erklären, sondern die benötigten Werkzeuge direkt anwenden lassen.
- Begriffe Projekt, Layer und Datendatei konsequent unterscheiden.
- Attributtabelle an einen bereits aus der Tabellenarbeit bekannten Datensatz anbinden.
- WMS und weitere Online-Dienste erst auf der nächsten Seite behandeln.

Benötigte Screenshots:
- beschriftete QGIS-Oberfläche
- Browser und Layer-Bereich
- Datenquellenmanager für Vektor und Raster
- Layer-Eigenschaften mit hervorgehobenem CRS

Vor Veröffentlichung ergänzen:
- konkrete Übungsdaten
- erwartetes Projekt-CRS
- betriebssystemspezifische Hinweise nur bei tatsächlichem Bedarf

Anschluss an unit10-03_datenquellen.md:
- Bisher lagen die Daten lokal vor. Wie können Daten aus Geoportalen gefunden und über Webdienste direkt in QGIS eingebunden werden?
-->