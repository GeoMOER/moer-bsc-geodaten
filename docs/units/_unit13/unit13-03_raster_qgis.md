---
title: Rasterdaten in QGIS
published: true
toc: true
header:
  image: /assets/images/unit13/hero-unit13.jpg
  image_description: "Digitales Geländemodell, das in sichtbare Rasterzellen mit markierten Beobachtungspunkten übergeht"
  caption: "KI-generierte Illustration, bearbeitet für diesen Kurs"
---

<!-- Rückblick: Welche Inhalte aus den vorherigen Seiten werden benötigt? -->

> **Verbindlicher Praxisweg:** Die [QGIS-Kurzcheckliste für Unit 13]({{ '/material/qgis-kernpfade.html#unit13' | relative_url }}) bündelt Rasterprüfung, Abtasten, Ergebniskontrolle und Ausgabe. Histogramme und weitere Rastervergleiche sind freiwillige Vertiefung.

## Rückblick

Wir wissen nun, dass ein Raster aus räumlich verorteten Zellen und Zellwerten besteht. Für seine Interpretation benötigen wir unter anderem Zellgröße, CRS, Ausdehnung, Bandbedeutung, Einheit und NoData-Definition.

In QGIS untersuchen wir diese Eigenschaften an einem digitalen Geländemodell und verbinden es anschließend mit dem geprüften GBIF-Punktlayer.

Unsere Leitfrage lautet:

> **Auf welcher Geländehöhe liegen die dokumentierten Artenbeobachtungen?**

## Daten und Projekt vorbereiten

Verwenden Sie den entpackten Ordner aus dem [Marburger Übungspaket und Anleitung]({{ '/material/marburg.html' | relative_url }}):

```text
marburg_geodaten/
  data_raw/
  data_output/
  documentation/
  unit13_raster.qgz
```

Benötigt werden:

| Datensatz | Datenmodell | Verwendung |
|---|---|---|
| digitales Geländemodell | kontinuierliches Raster | Geländehöhe |
| geprüfte GBIF-Beobachtungen | Punktvektor | Positionen der Beobachtungen |
| optional: Untersuchungsgebiet | Polygonvektor | räumliche Orientierung |

Speichern Sie ein neues QGIS-Projekt als **`unit13_raster.qgz`** und stellen Sie das seit Unit 10 verwendete Projekt-CRS ein: **`EPSG:25832`**.

<!-- Lehrende: DGM-Ausschnitt, Höhenbezug, Einheit, Zellgröße, Lizenz und EPSG-Code verbindlich dokumentieren. -->

## Rasterlayer laden

Das Lehrprodukt enthält 10-m-Mittelwerte aus den DGM1-Kacheln des amtlichen Marburger Downloadpakets. Es deckt nur einen Teil unseres 20-km-Rechtecks ab. Außerhalb der verfügbaren Kacheln steht NoData (-9999); dies ist keine Geländehöhe. Quellen, Befliegungsdaten und Bearbeitung sind in `documentation/quellen.md` und `documentation/dgm_kacheln.json` festgehalten.

1. Öffnen Sie die **Datenquellenverwaltung** oder den QGIS-Browser.
2. Wählen Sie die bereitgestellte Rasterdatei **`data_raw/dgm_marburg_10m.tif`**.
3. Fügen Sie den Rasterlayer zum Projekt hinzu.
4. Benennen Sie den Layer im Layerfenster eindeutig, zum Beispiel **`DGM – Geländehöhe`**.
5. Zoomen Sie auf den Layer.

QGIS wählt zunächst eine Standarddarstellung. Diese Darstellung ist noch keine vollständige fachliche Prüfung des Datensatzes.

## Datenquelle dokumentieren

Ergänzen Sie die Angaben anhand der bereitgestellten Metadaten:

| Merkmal | Angabe |
|---|---|
| genauer Titel | `[eintragen]` |
| Herausgeber | `[eintragen]` |
| dargestellte Größe | Geländehöhe |
| Einheit | `[eintragen]` |
| Zellgröße | `[eintragen]` |
| CRS | `[eintragen]` |
| Datenstand | `[eintragen]` |
| Höhenbezug | `[eintragen]` |
| NoData-Wert | `[eintragen]` |
| Lizenz | `[eintragen]` |
| Quelle/URL | `[eintragen]` |

Digitale Geländemodelle des Landes Hessen werden durch das [Hessen Geodatenmanagement](https://hvbg.hessen.de/landesvermessung/geotopographie/3d-daten/digitale-gelaendemodelle) beschrieben und im Rahmen des hessischen Open-Data-Angebots bereitgestellt. Für die Übung wird ein vorbereiteter Ausschnitt verwendet, damit alle mit demselben Datenstand arbeiten.

## Rastereigenschaften prüfen

Öffnen Sie mit einem Doppelklick auf den Layer seine **Eigenschaften**. Untersuchen Sie insbesondere die Bereiche **Information**, **Quelle** und **Symbolisierung**.

Notieren Sie:

| Eigenschaft | Ergebnis |
|---|---|
| Breite in Spalten | `[eintragen]` |
| Höhe in Zeilen | `[eintragen]` |
| Anzahl Bänder | `[eintragen]` |
| Datentyp | `[eintragen]` |
| Zellgröße x | `[eintragen]` |
| Zellgröße y | `[eintragen]` |
| räumliche Ausdehnung | `[eintragen]` |
| CRS | `[eintragen]` |
| Minimum | `[eintragen]` |
| Maximum | `[eintragen]` |
| NoData definiert? | ja / nein; Wert: `[eintragen]` |

Prüfen Sie anschließend:

1. Passen Minimum und Maximum grundsätzlich zur Geländehöhe im Untersuchungsgebiet?
2. Sind x- und y-Zellgröße gleich?
3. Ist die Einheit des CRS für die angegebene Zellgröße geeignet?
4. Deckt das Raster das erwartete Gebiet ab?

Wenn Werte oder Ausdehnung unplausibel erscheinen, setzen Sie die Analyse zunächst nicht fort.

## Zellstruktur sichtbar machen

Zoomen Sie sehr weit in das Raster hinein, bis einzelne Zellen erkennbar werden.

Beobachten Sie:

* Die Zellgrenzen verlaufen regelmäßig.
* Innerhalb einer Rasterzelle gilt ein gespeicherter Wert.
* Die Darstellung kann geglättet erscheinen, obwohl das zugrunde liegende Raster aus diskreten Zellen besteht.

Je nach Darstellungsoption kann QGIS beim Zoomen Werte interpoliert anzeigen. Die gespeicherten Zellwerte bleiben dadurch unverändert.

## Zellwerte abfragen

Aktivieren Sie das Werkzeug **Objekte abfragen** beziehungsweise **Identify Features** und klicken Sie an mehrere Stellen in das Raster.

Notieren Sie drei Beispiele:

| Position oder Ort | Wert in Band 1 | Einheit | plausibel? |
|---|---:|---|---|
| `[eintragen]` | `[eintragen]` | `[eintragen]` | ja / nein |
| `[eintragen]` | `[eintragen]` | `[eintragen]` | ja / nein |
| `[eintragen]` | `[eintragen]` | `[eintragen]` | ja / nein |

Klicken Sie außerdem außerhalb des gültigen Datenbereichs oder in eine NoData-Zelle, falls eine solche Stelle im bereitgestellten Raster vorhanden ist. Vergleichen Sie die Ausgabe mit einem gültigen Höhenwert von null beziehungsweise einem niedrigen Wert.

## Höhenwerte darstellen

Für ein einbändiges kontinuierliches Höhenraster eignet sich die Darstellungsart **Einkanal-Pseudofarbe** beziehungsweise **Singleband pseudocolor**.

1. Öffnen Sie **Layereigenschaften → Symbolisierung**.
2. Wählen Sie die Darstellung **Einkanal-Pseudofarbe**.
3. Verwenden Sie Band 1.
4. Laden oder berechnen Sie Minimum und Maximum für den relevanten Datenausschnitt.
5. Wählen Sie einen gut lesbaren sequentiellen Farbverlauf.
6. Lassen Sie die Farben zunächst kontinuierlich interpolieren.
7. Übernehmen Sie die Darstellung.

Beschreiben Sie:

- Welche Farbe steht für niedrige Werte?
- Welche Farbe steht für hohe Werte?
- Sind lokale Höhenunterschiede gut erkennbar?
- Verändert die Farbskala die gespeicherten Werte?

Die letzte Antwort lautet **nein**: Die Symbolisierung verändert nur die sichtbare Darstellung.

<!-- Lehrende: Eine farbenblindheitsfreundliche Farbskala vorgeben oder mehrere Varianten vergleichen lassen. Die systematische Kartenfarblehre folgt in Unit 14. -->

## Histogramm untersuchen

Der ausführliche Histogrammvergleich ist freiwillige Vertiefung. In der Kernübung gehen wir nach der Darstellung zum Hinzufügen und Abtasten der GBIF-Punkte über.

Öffnen Sie in den Rastereigenschaften den Bereich **Histogramm**. Falls nötig, lassen Sie das Histogramm berechnen.

Beantworten Sie:

1. In welchem Höhenbereich liegen besonders viele Zellen?
2. Gibt es nur wenige sehr niedrige oder sehr hohe Werte?
3. Könnten extreme Werte oder ein falsch behandelter NoData-Code die Darstellung beeinflussen?

Das Histogramm beschreibt die Verteilung der Zellwerte. Es sagt noch nicht, wo diese Werte im Raum liegen.

## GBIF-Punkte hinzufügen

Laden Sie den geprüften GBIF-Punktlayer aus Unit 11 und legen Sie ihn über das Höhenraster.

Kontrollieren Sie:

1. Liegen die Punkte im Gebiet des Rasters?
2. Besitzen Punktlayer und Raster ein bekanntes CRS?
3. Ist die räumliche Überlagerung plausibel?
4. Sind Punkte vorhanden, die außerhalb der gültigen Rasterwerte liegen?

Gestalten Sie die Punkte so, dass sie sich deutlich vom Raster abheben.

## Rasterwerte an Punkten abtasten

Mit dem Werkzeug **Rasterwerte abtasten** beziehungsweise **Sample raster values** übertragen wir den Höhenwert der jeweils getroffenen Rasterzelle in die Attributtabelle eines neuen Punktlayers.

1. Öffnen Sie die **Verarbeitungswerkzeuge**.
2. Suchen Sie nach **Rasterwerte abtasten**.
3. Wählen Sie den geprüften GBIF-Punktlayer als Eingabelayer.
4. Wählen Sie das DGM als Rasterlayer.
5. Verwenden Sie als Spaltenpräfix beispielsweise **`hoehe_`**.
6. Speichern Sie das Ergebnis im GeoPackage:

   ```text
   data_output/unit13_results.gpkg
   ```

7. Verwenden Sie den Layernamen:

   ```text
   gbif_mit_hoehe
   ```

8. Führen Sie das Werkzeug aus und öffnen Sie die Attributtabelle des Ergebnislayers.

Bei einem einbändigen Raster wird ein neues Feld für Band 1 angelegt. Mit QGIS 3.40 und dem Präfix `hoehe_` heißt es **`hoehe_1`**. Prüfen Sie den tatsächlichen Feldnamen. Das verbindliche Feld für die Übergabe an Unit 14 heißt **`hoehe_m`**. Benennen Sie `hoehe_1` in `hoehe_m` um und behalten Sie den Typ Dezimalzahl bei. Dafür können Sie das Werkzeug **Felder überarbeiten** verwenden: Ändern Sie nur diesen Feldnamen und erhalten Sie die übrigen Felder. Falls Sie stattdessen ein neues Feld berechnen, entfernen Sie anschließend das überflüssige Zwischenfeld `hoehe_1`. Dokumentieren Sie den Schritt, damit eigenes Ergebnis und Ersatzlayer dasselbe Schema besitzen.

Für den bereitgestellten Snapshot erwarten wir 35 gültige Höhenwerte und 21 `NULL`-Werte. Alle 56 Punkte bleiben im Ergebnis dieser Unit erhalten. Fehlende Werte werden nicht durch null ersetzt.

> Der Punkt wird durch das Werkzeug nicht verschoben. Er erhält lediglich den Wert der Rasterzelle an seiner Position als zusätzliches Attribut.

## Ergebnis kontrollieren

In der Sitzung prüfen wir einen Punkt mit gültiger Höhe und einen Punkt ohne Höhenwert gemeinsam. Die Kontrolle weiterer Punkte ist freiwillige Vertiefung:

1. Wählen Sie einen Punkt in der Karte aus.
2. Lesen Sie seinen neuen Höhenwert in der Attributtabelle ab.
3. Fragen Sie das Raster an derselben Position mit **Objekte abfragen** ab.
4. Vergleichen Sie beide Werte.

Notieren Sie:

| Punkt-ID | abgetasteter Höhenwert | direkt abgefragter Rasterwert | stimmt überein? |
|---|---:|---:|---|
| `[eintragen]` | `[eintragen]` | `[eintragen]` | ja / nein |
| `[eintragen]` | `[eintragen]` | `[eintragen]` | ja / nein |
| `[eintragen]` | `[eintragen]` | `[eintragen]` | ja / nein |
| `[eintragen]` | `[eintragen]` | `[eintragen]` | ja / nein |
| `[eintragen]` | `[eintragen]` | `[eintragen]` | ja / nein |

Suchen Sie außerdem nach fehlenden Höhenwerten. Ein fehlender Wert kann beispielsweise entstehen, wenn ein Punkt außerhalb des Rasters oder auf einer NoData-Zelle liegt.

## Ergebnisse beschreiben

Ermitteln Sie für die gültigen abgetasteten Höhenwerte:

- kleinsten Wert,
- größten Wert,
- einen typischen mittleren Wert, beispielsweise den Median,
- Anzahl der Punkte ohne gültigen Höhenwert.

Verwenden Sie dafür die Attributtabelle, die Feldstatistik oder die im Kurs vorgegebene Methode.

Formulieren Sie anschließend eine vorsichtige Aussage:

> Die dokumentierten Beobachtungen im verwendeten Datenausschnitt liegen zwischen `[Minimum]` und `[Maximum]` Metern Geländehöhe. Diese Aussage bezieht sich auf die vorliegenden Beobachtungspunkte und den verwendeten DGM-Datensatz.

## Unsicherheiten beachten

Der abgetastete Höhenwert ist nicht automatisch die exakt gemessene Höhe des beobachteten Organismus. Zu berücksichtigen sind unter anderem:

* Zellgröße und Genauigkeit des DGM,
* Entstehungsmethode und Datenstand des Höhenmodells,
* Koordinatenunsicherheit der GBIF-Beobachtung,
* mögliche Rundung der Koordinaten,
* Lage eines Punktes nahe einer starken Geländekante,
* NoData-Bereiche und
* Unterschied zwischen Gelände- und Oberflächenhöhe.

Eine Beobachtung mit einer Koordinatenunsicherheit von mehreren Kilometern kann nicht sinnvoll einer einzelnen sehr kleinen DGM-Zelle als exakt bekanntem Ort zugeordnet werden.

## Häufige Probleme

| Problem | Mögliche Ursache | Kontrolle oder Lösung |
|---|---|---|
| Raster erscheint schwarz oder einfarbig | ungeeignete Min-/Max-Werte oder Darstellung | Statistik laden und Symbolisierung prüfen |
| Raster und Punkte liegen nicht übereinander | falsches oder fehlendes CRS | CRS und Ausdehnung beider Layer prüfen |
| Werte wirken unplausibel | Einheit, Höhenbezug oder Datensatz falsch verstanden | Metadaten kontrollieren |
| extreme Werte verzerren Farbskala | NoData-Code oder Ausreißer einbezogen | NoData und Histogramm prüfen |
| neues Höhenfeld fehlt | falscher Ergebnislayer geöffnet | Ausgabe des Werkzeugs und Attributtabelle kontrollieren |
| einige Punkte besitzen keinen Höhenwert | außerhalb des Rasters oder auf NoData | Positionen der betroffenen Punkte prüfen |
| Punktzahl hat sich verändert | falscher Eingabelayer oder nachträglicher Filter | Eingabe und Verarbeitungshistorie prüfen |

## Kurzübung

Beantworten Sie mit den bereitgestellten Daten:

1. Welche Zellgröße besitzt das DGM?
2. Welchen Wertebereich deckt es ab?
3. Wie viele GBIF-Punkte erhalten einen gültigen Höhenwert?
4. Welcher Punkt besitzt den niedrigsten, welcher den höchsten Wert?
5. Welche Unsicherheit ist für Ihre Interpretation besonders wichtig?

Speichern Sie das Projekt und den Ergebnislayer `gbif_mit_hoehe`.

## Zusammenfassung

* Raster müssen vor der Analyse anhand ihrer Metadaten und Layerinformationen geprüft werden.
* Einzelne Zellwerte können mit dem Abfragewerkzeug kontrolliert werden.
* Eine Pseudofarbdarstellung macht kontinuierliche Höhenunterschiede sichtbar, verändert aber nicht die Daten.
* Das Histogramm beschreibt die Verteilung der Rasterwerte.
* Mit **Rasterwerte abtasten** können Rasterwerte an Punktpositionen als neue Attribute gespeichert werden.
* Fehlende Ergebnisse können durch Punkte außerhalb des Rasters oder NoData-Zellen entstehen.
* DGM- und Punktunsicherheit begrenzen die Genauigkeit der fachlichen Aussage.

## Weiterführende Informationen

* [QGIS-Dokumentation: Rastereigenschaften](https://docs.qgis.org/latest/en/docs/user_manual/working_with_raster/raster_properties.html)
* [QGIS-Dokumentation: Rasterwerte abtasten](https://docs.qgis.org/latest/en/docs/user_manual/processing_algs/qgis/rasteranalysis.html#sample-raster-values)
* [Hessen Geodatenmanagement: Digitale Geländemodelle](https://hvbg.hessen.de/landesvermessung/geotopographie/3d-daten/digitale-gelaendemodelle)
* [Hessen Geodatenmanagement: Open Data](https://hvbg.hessen.de/geoinformation/open-data)

<!-- Notizen: Ab hier folgen Vermerke, welche als Gedankenstütze oder Erinnerung dienen, aber noch nicht in der vorhandenen Form veröffentlicht werden sollen. -->

<!--
TODO Lehrende vor Durchführung:
- DGM-Ausschnitt und GBIF-Ersatzlayer festlegen und gemeinsam testen.
- Projekt-CRS, DGM-CRS, Zellgröße, Einheit und Höhenbezug ergänzen.
- Dateinamen und Download-/Quellenlink eintragen.
- tatsächlichen deutschen Namen des Abtastwerkzeugs in der eingesetzten QGIS-Version prüfen.
- Feldnamen des Ergebnislayers und erwartete Punktzahlen kontrollieren.
- Beispielwerte für Minimum, Maximum, Median und fehlende Werte ermitteln.
- Screenshots für Rasterinformation, Zellabfrage, Symbolisierung, Histogramm und Abtastwerkzeug ergänzen.
- Prüfen, ob Feldstatistik oder ein zuvor eingeführter Tabellenworkflow für die Ergebniszusammenfassung verwendet werden soll.
-->
