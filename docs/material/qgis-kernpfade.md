---
title: "QGIS-Kurzchecklisten: Units 10–14"
layout: single
permalink: /material/qgis-kernpfade.html
toc: true
---

Diese Seite bündelt die **verbindlichen Praxiswege** der gemeinsamen Sitzungen. Die ausführlichen Unit-Seiten bleiben das Nachschlagewerk. Arbeiten Sie zuerst die jeweilige Kurzcheckliste ab; zusätzliche Varianten sind freiwillige Vertiefung.

Für alle Units gilt: Entpacken Sie das [Marburger Übungspaket]({{ '/material/marburg.html' | relative_url }}) vollständig, behalten Sie seine Ordnerstruktur bei und verwenden Sie `EPSG:25832` als Projekt- und Ausgabe-CRS. Eigene Ergebnisse gehören nach `data_output/`, Notizen nach `documentation/`.

<a id="unit10"></a>
## Unit 10: Lokales Projekt sichern

- [ ] Neues Projekt im Hauptordner als `unit10_einstieg.qgz` speichern.
- [ ] `data_raw/marburg_basis.gpkg/gewaesser` und `data_raw/dgm_marburg_10m.tif` laden.
- [ ] Am Gewässerlayer ein Feature in Karte und Attributtabelle verbinden.
- [ ] Datenquelle, Datenmodell, CRS und Ausdehnung beider Layer im Protokoll festhalten.
- [ ] Projekt speichern, QGIS schließen und das Projekt erneut öffnen.
- [ ] Kontrollieren, dass beide Layer ohne Reparatur der Datenpfade erreichbar sind.

**Fertig:** Das lokale Projekt öffnet sich mit Gewässerlayer und DGM. Die eigene WMS-Einrichtung gehört nicht zu diesem Kernpfad. Bei Dienstausfall verwendet die Lehrperson sofort das Material in `ersatz/`.

<a id="unit11"></a>
## Unit 11: Tabelle in geprüfte Punkte überführen

- [ ] Projekt als `unit11_punktdaten.qgz` speichern und die CSV-Struktur prüfen.
- [ ] `decimalLongitude` als x und `decimalLatitude` als y mit dem Import-CRS `EPSG:4326` verwenden.
- [ ] Lage und wichtige Attribute der 79 importierten Records prüfen.
- [ ] Mit `"coordinateUncertaintyInMeters" > 0 AND "coordinateUncertaintyInMeters" <= 100` auswählen.
- [ ] Die 56 ausgewählten Records als `data_output/unit11_results.gpkg/gbif_checked` in `EPSG:25832` exportieren und erneut laden.
- [ ] Quelle, DOI, Auswahlregel sowie ein- und ausgeschlossene Recordzahlen dokumentieren.

**Fertig:** `gbif_checked` enthält 56 Punkte im gemeinsamen Schema. Wenn Import oder Export nicht rechtzeitig gelingt, wird mit `ersatz/unit11_results.gpkg/gbif_checked` weitergearbeitet.

<a id="unit12"></a>
## Unit 12: Räumliche Auswahlen speichern

- [ ] `gbif_checked`, `gewaesser` und `schutzgebiete` laden und Geometrietyp, CRS und Featurezahl prüfen.
- [ ] Mit `"kategorie" = 'FFH'` zehn Schutzgebiete auswählen und als `schutzgebiete_auswahl` speichern.
- [ ] GBIF-Punkte mit **schneidet** gegen `schutzgebiete_auswahl` auswählen und vier Treffer als `gbif_in_schutzgebieten` speichern.
- [ ] Gewässer ebenso auswählen und 106 Treffer als `gewaesser_an_schutzgebieten` speichern.
- [ ] Alle drei Layer in `data_output/unit12_results.gpkg` erneut laden und prüfen.
- [ ] Auswahlregeln, Featurezahlen und eine Grenze der räumlichen Aussage dokumentieren.

**Fertig:** Das GeoPackage enthält die drei geprüften Ergebnislayer. Falls ein Schritt scheitert, stehen die gleichnamigen Layer in `ersatz/unit12_results.gpkg` bereit.

<a id="unit13"></a>
## Unit 13: Höhenwerte an Punkte übertragen

- [ ] DGM und `gbif_checked` laden; Zellgröße, Ausdehnung, CRS, Einheit und NoData prüfen.
- [ ] Einen gültigen Rasterwert und einen NoData-Fall abfragen.
- [ ] Rasterwerte an den Punkten abtasten und das Ergebnisfeld kontrolliert `hoehe_m` nennen.
- [ ] Das Ergebnis als `data_output/unit13_results.gpkg/gbif_mit_hoehe` speichern.
- [ ] 56 Records prüfen: 35 mit gültiger Höhe und 21 mit `NULL`.
- [ ] Je einen gültigen und fehlenden Wert kontrollieren sowie Raster- und Koordinatenunsicherheit dokumentieren.

**Fertig:** `gbif_mit_hoehe` behält alle geprüften Punkte und unterscheidet gültige Höhen von `NULL`. Bei technischen Problemen wird `ersatz/unit13_results.gpkg/gbif_mit_hoehe` verwendet.

<a id="unit14"></a>
## Unit 14: Karte vergleichen, ausarbeiten und exportieren

- [ ] `unit14_start.qgz` öffnen und sofort als `unit14_abschluss.qgz` speichern.
- [ ] Die beiden Bilder in `ersatz/` vergleichen: gleiche Intervalle und Quantile, jeweils fünf Klassen.
- [ ] Eine der beiden Methoden begründet auf `hoehe_m` anwenden; Klassengrenzen prüfen.
- [ ] Titel und Legende überarbeiten; Kartenausschnitt, Maßstab und Quellen kontrollieren.
- [ ] Als `figures/abschlusskarte_unit14.pdf` und als PNG mit 150 dpi exportieren; beide Dateien öffnen und in vorgesehener Größe prüfen.
- [ ] Partnercheck durchführen, eine begründete Korrektur einarbeiten und eine Aussagegrenze dokumentieren.

**Fertig:** Projekt, PDF, PNG und kurze Begründung liegen vor. Spätestens in Minute 45 wird zum Layout und in Minute 62 zum Export gewechselt. Falls das eigene Projekt ausfällt, wird mit `unit14_beispiel.qgz` weitergearbeitet.

## Was zur Vertiefung gehört

Eigene Portal- und Datensuchen, weitere Filter oder Auswahlbeziehungen, zusätzliche Symbolisierungen und Histogramme, das Ersetzen vorbereiteter Unit-14-Daten sowie ein vollständig neues Kartenlayout gehören nicht zu den verbindlichen Kurzpfaden.
