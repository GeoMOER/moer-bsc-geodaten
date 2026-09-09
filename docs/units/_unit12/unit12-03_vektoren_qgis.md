---
title: Linien und Polygone in QGIS
published: true
toc: true
header:
  image: /assets/images/unit12/hero-unit12.jpg
  image_description: "Flusslandschaft mit Schutzgebietsfläche und Beobachtungspunkten innerhalb und außerhalb des Gebietes"
  caption: "KI-generierte Illustration, bearbeitet für diesen Kurs"
---

<!-- Rückblick: Welche Inhalte aus den vorherigen Seiten werden benötigt? -->

> **Verbindlicher Praxisweg:** Die [QGIS-Kurzcheckliste für Unit 12]({{ '/material/qgis-kernpfade.html#unit12' | relative_url }}) bündelt die Attributauswahl, beide räumlichen Auswahlen und die drei zu speichernden Ergebnislayer.

## Rückblick

Wir kennen nun drei Vektorgeometrien:

- **Punkte** für einzelne Positionen,
- **Linien** für längliche Objekte,
- **Polygone** für Flächen.

Außerdem haben wir in Geoportalen nach geeigneten Datensätzen gesucht und deren Metadaten geprüft. Jetzt führen wir die Daten in QGIS zusammen.

Unsere Leitfrage lautet:

> **Welche Artenbeobachtungen und Gewässer liegen in beziehungsweise schneiden ausgewählte Schutzgebiete?**

## Projekt vorbereiten

Verwenden Sie den entpackten Ordner aus dem [Marburger Übungspaket und Anleitung]({{ '/material/marburg.html' | relative_url }}):

```text
marburg_geodaten/
  data_raw/
  data_output/
  documentation/
  unit12_vectors.qgz
```

1. Öffnen Sie QGIS und erstellen Sie ein neues Projekt.
2. Speichern Sie es als **`unit12_vectors.qgz`**.
3. Stellen Sie das seit Unit 10 verwendete Projekt-CRS ein: **`EPSG:25832`**.
4. Speichern Sie das Projekt erneut.

Für Messungen in Metern beziehungsweise Quadratmetern benötigen wir ein geeignetes **projiziertes CRS**. Für Daten in Deutschland kann – abhängig vom Untersuchungsgebiet – beispielsweise ein UTM-Koordinatensystem geeignet sein.

<!-- Lehrende: Projekt-CRS verbindlich festlegen, zum Beispiel ETRS89 / UTM Zone 32N (EPSG:25832), und mit allen bereitgestellten Daten testen. -->

## Layer laden

Laden Sie diese drei Layer:

| Layer | Geometrie | Herkunft |
|---|---|---|
| `unit11_results.gpkg/gbif_checked` | Punkt | Ergebnis aus Unit 11 oder schemaidentischer Ersatzlayer |
| `gewaesser` | Linie | `data_raw/marburg_basis.gpkg` |
| `schutzgebiete` | Polygon | `data_raw/marburg_basis.gpkg` |

Je nach Datenquelle können Sie die Layer über **Layer hinzufügen**, den **Browser** oder die **Datenquellenverwaltung** laden.

Benennen Sie die Layer im Layerfenster eindeutig, zum Beispiel:

- `GBIF – geprüfte Beobachtungen`
- `Gewässer`
- `Schutzgebiete`

## Eingangsdaten kontrollieren

Prüfen Sie jeden Layer, bevor Sie ihn weiterverarbeiten.

| Kontrolle | Punktlayer | Linienlayer | Polygonlayer |
|---|---|---|---|
| Layername | `[eintragen]` | `[eintragen]` | `[eintragen]` |
| Geometrietyp | Punkt | Linie | Polygon |
| CRS | `[eintragen]` | `[eintragen]` | `[eintragen]` |
| Anzahl Features | `[eintragen]` | `[eintragen]` | `[eintragen]` |
| wichtiges Attribut | `[eintragen]` | `[eintragen]` | `[eintragen]` |
| räumliche Ausdehnung plausibel? | ja / nein | ja / nein | ja / nein |

Zoomen Sie auf jeden Layer und öffnen Sie seine Attributtabelle. Ein formal korrekt geladener Layer kann inhaltlich trotzdem ungeeignet sein – etwa weil er ein anderes Gebiet oder einen unerwarteten Datenstand abbildet.

## Layer sinnvoll anordnen

Die Reihenfolge im Layerfenster beeinflusst, was sichtbar ist. Eine sinnvolle Reihenfolge ist:

1. Beobachtungspunkte,
2. Gewässerlinien,
3. Schutzgebietspolygone,
4. Hintergrundkarte.

Gestalten Sie die Schutzgebiete mit einer transparenten oder nur leicht gefüllten Fläche, damit darunterliegende Informationen sichtbar bleiben. Verwenden Sie für Gewässer eine gut erkennbare Linienfarbe und für Beobachtungen ein kontrastierendes Punktsymbol.

Wenn ein geeignetes Kategorienfeld vorhanden ist, können Sie Schutzgebiete oder Gewässer **kategorisiert** symbolisieren. Prüfen Sie zuvor, welche Werte tatsächlich im Feld vorkommen.

<!-- Lehrende: Konkrete Feldnamen und sinnvolle Kategorien nach Auswahl der Datensätze ergänzen. -->

## Nach Attributen auswählen

Eine Attributauswahl nutzt Angaben aus der Tabelle. Damit können wir beispielsweise:

- nur Naturschutzgebiete einer bestimmten Kategorie auswählen,
- nur Gewässer eines bestimmten Typs anzeigen,
- Beobachtungen aus einem bestimmten Zeitraum auswählen.

1. Öffnen Sie die Attributtabelle des Polygonlayers.
2. Untersuchen Sie die Werte des vorgegebenen Feldes **`kategorie`**.
3. Wählen Sie mit einem Ausdruck die Kategorie **FFH** aus.
4. Prüfen Sie die Auswahl sowohl in der Tabelle als auch auf der Karte.

Ein beispielhafter Ausdruck sieht so aus:

```text
"kategorie" = 'FFH'
```

Die Auswahl umfasst 10 FFH-Features. Exportieren Sie **nur die ausgewählten Features** nach `data_output/unit12_results.gpkg` als `schutzgebiete_auswahl`. Laden Sie diesen Layer und verwenden Sie ihn in den folgenden räumlichen Auswahlen als Vergleichslayer.

## Längen und Flächen bestimmen

Dieser zusätzliche Arbeitsschritt ist freiwillige Vertiefung. Für die Kernübung gehen wir direkt zur räumlichen Auswahl über.

Linien besitzen eine Länge; Polygone besitzen Fläche und Umfang. Diese Größen können wir mit dem Werkzeug **Geometrieattribute hinzufügen** berechnen.

1. Öffnen Sie die **Verarbeitungswerkzeuge**.
2. Suchen Sie nach **Geometrieattribute hinzufügen**.
3. Wählen Sie den Gewässerlayer als Eingabelayer.
4. Verwenden Sie das im Kurs vorgegebene CRS beziehungsweise die vorgegebenen Maßeinheiten.
5. Speichern Sie das Ergebnis im Ordner `data_output/` oder in einem GeoPackage.
6. Wiederholen Sie den Vorgang für die Schutzgebiete.

Kontrollieren Sie anschließend die neuen Attributfelder.

> Zahlen sind nur dann sinnvoll interpretierbar, wenn CRS und Einheit passen. Längen in Grad sind keine Längen in Metern.

## Räumlich auswählen

Eine räumliche Auswahl verwendet nicht die Attributwerte, sondern die **Lage der Geometrien zueinander**.

Wir nutzen das Werkzeug **Nach Position selektieren**. Es benötigt:

- einen Eingabelayer, dessen Features ausgewählt werden,
- eine räumliche Beziehung,
- einen Vergleichslayer.

### Beobachtungen in Schutzgebieten

1. Öffnen Sie **Nach Position selektieren**.
2. Wählen Sie die GBIF-Beobachtungen als Eingabelayer.
3. Verwenden Sie die räumliche Beziehung **schneidet** (`intersects`).
4. Wählen Sie `schutzgebiete_auswahl` als Vergleichslayer.
5. Führen Sie das Werkzeug aus.
6. Öffnen Sie die Attributtabelle des Punktlayers und zeigen Sie nur ausgewählte Features an.

Wir verwenden hier zunächst **schneidet**, weil damit auch ein Punkt auf einer Polygongrenze erfasst wird. Die strengere Beziehung **liegt innerhalb** kann Randfälle anders behandeln.

Notieren Sie:

- Anzahl aller Beobachtungen: **`[eintragen]`**
- Anzahl ausgewählter Beobachtungen: **`[eintragen]`**
- Anteil ausgewählter Beobachtungen: **`[eintragen]`**

### Gewässer, die Schutzgebiete schneiden

Wiederholen Sie die räumliche Auswahl:

1. Gewässer als Eingabelayer,
2. **schneidet** als räumliche Beziehung,
3. `schutzgebiete_auswahl` als Vergleichslayer.

Notieren Sie:

- Anzahl aller Gewässer-Features: **`[eintragen]`**
- Anzahl ausgewählter Gewässer-Features: **`[eintragen]`**

Ein ausgewähltes Linien-Feature kann ein Schutzgebiet nur kurz berühren oder vollständig hindurchführen. Die Auswahl beantwortet daher zunächst nur, **ob** eine räumliche Beziehung besteht – nicht, wie groß der betroffene Linienabschnitt ist.

## Auswahl und Ergebnis unterscheiden

Eine Auswahl markiert vorhandene Features nur vorübergehend. Sie erzeugt noch keinen neuen Datensatz.

Wenn Sie die ausgewählten Features dauerhaft speichern möchten:

1. Klicken Sie mit der rechten Maustaste auf den Layer.
2. Wählen Sie **Exportieren → Ausgewählte Objekte speichern als …**.
3. Verwenden Sie `data_output/unit12_results.gpkg`.
4. Geben Sie dem neuen Layer einen eindeutigen Namen.

Geeignete Namen sind beispielsweise:

- `gbif_in_schutzgebieten`
- `gewaesser_an_schutzgebieten`

Prüfen Sie nach dem Export, ob Featureanzahl, Geometrie und CRS plausibel sind.

## Ergebnisse vorsichtig interpretieren

Die räumliche Auswahl liefert ein technisch eindeutiges Ergebnis. Die fachliche Aussage kann dennoch unsicher sein.

Beachten Sie unter anderem:

- Eine GBIF-Koordinate kann ungenau sein.
- Die Schutzgebietsgrenze ist ein räumliches Modell und kann generalisiert sein.
- Datenstände der Layer können voneinander abweichen.
- Ein Beobachtungspunkt im Schutzgebiet beweist keinen ursächlichen Zusammenhang.
- Ein Linien-Feature kann mehrfach oder nur zu einem kleinen Teil ein Gebiet schneiden.

Besonders bei Punkten nahe einer Grenze sollte die Koordinatenunsicherheit aus Unit 11 berücksichtigt werden.

## Häufige Probleme

| Problem | Mögliche Ursache | Kontrolle oder Lösung |
|---|---|---|
| Layer liegen nicht übereinander | falsches oder fehlendes CRS | CRS der Layer und des Projekts prüfen |
| Polygon verdeckt andere Layer | deckende Füllung oder falsche Reihenfolge | Transparenz und Layerreihenfolge ändern |
| keine Features werden ausgewählt | falsche Layer oder räumliche Beziehung | Eingabe- und Vergleichslayer kontrollieren |
| Längen oder Flächen sind unplausibel | ungeeignetes CRS oder falsche Einheit | projiziertes CRS und Maßeinheit prüfen |
| Auswahl verschwindet | Auswahl wurde aufgehoben oder Projekt nicht gespeichert | benötigte Features exportieren |
| Feldname aus der Anleitung fehlt | anderer Datenstand oder Datensatz | Attributtabelle und Metadaten prüfen |

## Kurzübung

Beantworten Sie mit den bereitgestellten Daten:

1. Wie viele Artenbeobachtungen schneiden mindestens ein Schutzgebiet?
2. Wie viele Gewässer-Features schneiden mindestens ein Schutzgebiet?
3. Welche Attribute helfen Ihnen, die ausgewählten Features fachlich zu verstehen?
4. Welche Unsicherheit schränkt Ihre Antwort am stärksten ein?

Speichern Sie das QGIS-Projekt und exportieren Sie die beiden Auswahlergebnisse in ein GeoPackage.

## Zusammenfassung

- Punkte, Linien und Polygone können als getrennte Layer gemeinsam untersucht werden.
- Attributauswahlen verwenden Tabellenwerte; räumliche Auswahlen verwenden die Lage der Geometrien.
- Mit **Nach Position selektieren** lassen sich Features anhand räumlicher Beziehungen auswählen.
- Eine Auswahl ist zunächst temporär und muss für ein dauerhaftes Ergebnis exportiert werden.
- CRS, Datenqualität und räumliche Genauigkeit bestimmen, wie verlässlich das Ergebnis interpretiert werden kann.

## Weiterführende Informationen

- [QGIS-Dokumentation: Nach Position selektieren](https://docs.qgis.org/latest/en/docs/user_manual/processing_algs/qgis/vectorselection.html)
- [QGIS-Dokumentation: Geometrieattribute hinzufügen](https://docs.qgis.org/latest/en/docs/user_manual/processing_algs/qgis/vectorgeometry.html)
- [QGIS-Dokumentation: Eigenschaften von Vektorlayern](https://docs.qgis.org/latest/en/docs/user_manual/working_with_vector/vector_properties.html)

<!-- Notizen: Ab hier folgen Vermerke, welche als Gedankenstütze oder Erinnerung dienen, aber noch nicht in der vorhandenen Form veröffentlicht werden sollen. -->

<!--
TODO Lehrende vor Durchführung:
- Projektion und EPSG-Code verbindlich festlegen.
- Dateinamen und Feldnamen an die tatsächlich bereitgestellten Daten anpassen.
- Erwartete Featurezahlen für die Kontrollpunkte ermitteln.
- Screenshots für Layerreihenfolge, Symbolisierung, Geometrieattribute und räumliche Auswahl ergänzen.
- Prüfen, ob die deutsche QGIS-Oberfläche das Werkzeug in der eingesetzten Version als „Nach Position selektieren“ oder leicht abweichend bezeichnet.
- Optional eine bereits geprüfte GeoPackage-Datei als Ausweichlösung bereitstellen.
-->
