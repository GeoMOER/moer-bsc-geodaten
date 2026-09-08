# Quellen und Bearbeitung

Abrufstand des Übungspakets: **08.09.2026**. Das Abrufdatum ist nicht mit Beobachtungsdatum, Befliegungsdatum oder fachlichem Datenstand gleichzusetzen. Exakte Abfragen stehen in `sources.json`, Eingangsprüfsummen in `pruefbericht.json`.

## Gemeinsamer Raumbezug

Projekt und Vektorausgaben: ETRS89 / UTM Zone 32N, EPSG:25832. Untersuchungsrechteck: Rechtswerte 474000–494000 m, Hochwerte 5619000–5639000 m. Es wurde für die Lehre definiert. Der Orientierungspunkt „Marburg“ verwendet gerundete Koordinaten 8,77° Ost / 50,81° Nord; er ist keine amtliche Stadtmittelpunktdefinition.

## Feuersalamander-Nachweise

Quelle: **naturgucker.de, NABU|naturgucker**, über GBIF. Datensatz: [doi:10.15468/uc1apo](https://doi.org/10.15468/uc1apo), GBIF-Datensatzschlüssel `6ac3f774-d9fb-4796-b3e9-92bf6c81c084`. Lizenz: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

Für diesen kleinen Ausschnitt wurde die öffentliche GBIF-Such-API verwendet. Der bereitgestellte Snapshot besitzt **keinen eigenen GBIF-Download-DOI**. Der genannte DOI bezeichnet den Quelldatensatz. `gbifID`, `occurrenceID`, Quellenschlüssel und Lizenz bleiben in jeder Zeile erhalten; ein einzelner Nachweis ist über `https://www.gbif.org/occurrence/<gbifID>` erreichbar.

Die räumliche Auswahl enthält 79 Nachweise von *Salamandra salamandra* aus dem Untersuchungsrechteck. Koordinaten und Unsicherheitsangaben wurden nicht verändert. Die API-Feldliste `issues` wurde als Textfeld `issue` mit Semikolontrennung übernommen. Andere Attribute wurden für das Kursformat ausgewählt, die Zeilen nach `gbifID` sortiert. Quellenvermerk für Weiterverwendung: „NABU|naturgucker via GBIF, doi:10.15468/uc1apo, CC BY 4.0; räumliche und fachliche Auswahl für GeoMOER, Abruf 08.09.2026“.

CSV: UTF-8, Komma als Trennzeichen, Punkt als Dezimalzeichen, Kopfzeile vorhanden. Die begleitende CSVT-Datei beschreibt die Datentypen. Koordinatenimport: x=`decimalLongitude`, y=`decimalLatitude`, Quell-CRS EPSG:4326. Die IDs werden als Text behandelt, `year` als Ganzzahl und Koordinaten/Unsicherheit als Dezimalzahlen.

Übungsregel: angegebene Koordinatenunsicherheit **größer null und höchstens 100 m**. Damit bleiben 56 Records; 23 Records mit 250 m Unsicherheit werden für diese Übung ausgeschlossen. Das ist eine didaktische Entscheidung für den räumlichen Vergleich, kein allgemeines GBIF-Qualitätssiegel. Alle Records tragen unter anderem Hinweise auf gerundete Koordinaten und ein angenommenes WGS84-Datum. Ein Qualitätsflag allein führt hier nicht zum Ausschluss.

## Schutzgebiete

Quelle: **Hessisches Ministerium für Landwirtschaft und Umwelt, Weinbau, Forsten, Jagd und Heimat (HMLU)**, bereitgestellt durch das HLNUG: [Geodienste Naturschutz](https://www.hlnug.de/themen/geografische-informationssysteme/geodienste/naturschutz).

Verwendet werden Naturschutzgebiete (NSG) und Fauna-Flora-Habitat-Gebiete (FFH), die das Untersuchungsrechteck schneiden. Die 22 Features werden vollständig und geometrisch unverändert übernommen; sie sind nicht am Rechteck abgeschnitten. Neue Kursfelder: `quell_id` aus Kategorie und OBJECTID, `name` aus NAME, `kategorie` als NSG/FFH, `gebiets_nr` aus NATUREG_NR beziehungsweise NATURA_NR. Die amtlichen Grenzen können über den Kartenausschnitt hinausreichen.

Nutzungsbedingungen laut Dienstbeschreibung: kostenfreie Nutzung mit Quellenangabe, keine rechtsverbindliche Auskunft; die reine Weitergabe der Daten gegen Gebühr ist ausgeschlossen. Maßgeblich ist die im Paket gespeicherte Dienstbeschreibung. Quellenvermerk: „Darstellung auf der Grundlage von Daten des Hessischen Ministeriums für Landwirtschaft und Umwelt, Weinbau, Forsten, Jagd und Heimat (HMLU)“. Bearbeitung: räumliche Featureauswahl, Auswahl und Vereinheitlichung der Attribute für GeoMOER.

Unit 12 wählt `kategorie = 'FFH'`: 10 Features. Verglichen wird mit deren gemeinsamen Geometrien; überlappende Gebiete zählen einen Beobachtungspunkt nicht mehrfach.

## Gewässer

Quelle: **Hessisches Landesamt für Naturschutz, Umwelt und Geologie (HLNUG)**, [Gewässernetz 1:25.000](https://www.hlnug.de/themen/geografische-informationssysteme/geodienste/wasser), Dienstlayer `Gewaessernetz_DLM25`. Lizenz laut Dienstbeschreibung: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

Die 412 Linienfeatures schneiden das Untersuchungsrechteck und bleiben vollständig erhalten. Kursfelder: `quell_id` aus OBJECTID, `name` aus GEWBEZ, `gewaesserzahl` aus GWZ und `ordnung` aus GEWORDN. Gezählt werden Features des Datensatzes, nicht eigenständige Flüsse. Quellenvermerk: „Darstellung auf der Grundlage von Daten des Hessischen Landesamtes für Naturschutz, Umwelt und Geologie (HLNUG)“. Bearbeitung: räumliche Featureauswahl und vereinfachtes Attributschema für GeoMOER.

## Digitales Geländemodell

Quelle: **Hessen Geodatenmanagement**, [ATKIS DGM1](https://hvbg.hessen.de/landesvermessung/geotopographie/3d-daten/digitale-gelaendemodelle), amtliches Downloadpaket „Marburg – DGM1“. Lizenz: [Datenlizenz Deutschland – Zero – Version 2.0](https://www.govdata.de/dl-de/zero-2-0), nach den [amtlichen DGM-Metadaten](https://www.geoportal.hessen.de/mapbender/php/mod_iso19139ToHtml.php?url=https%3A%2F%2Fwww.geoportal.hessen.de%2Fmapbender%2Fphp%2Fmod_dataISOMetadata.php%3FoutputFormat%3Diso19139%26id%3Ddbf48a95-b44d-48b3-a5b4-981e4c1bd8e6).

162 GeoTIFF-Kacheln wurden mosaikiert und auf das Untersuchungsrechteck mit **10 m × 10 m Zellgröße** abgebildet. Jede Ausgabezelle enthält den Mittelwert der darin verfügbaren DGM1-Werte; NoData wird dabei nicht als Höhe null behandelt. Das Ergebnis ist ein abgeleitetes Lehrprodukt, kein unverändertes amtliches DGM10. An Kachelrändern können Mittelwerte aus nur teilweise belegten Ausgabezellen entstehen.

Datei: `dgm_marburg_10m.tif`; 2000 Spalten × 2000 Zeilen; ein Band; Float32; NoData=-9999; Einheit Meter; horizontales CRS EPSG:25832; Höhenbezug **DHHN2016_NH**. Die Höhengenauigkeit wird durch die Mittelung nicht automatisch verbessert.

Die amtliche Metadatenliste vom August 2026 nennt für Marburg Befliegungen am 01.04.2021 sowie 09.03., 22.03. und 25.03.2024. Die Zuordnung zu Kacheln liegt in `dgm_kacheln.json`; das Downloadpaket ist im Portal mit Erstellungsdatum 12.06.2025 geführt. Das Paket deckt nicht alle Nachweisorte im 20-km-Rechteck ab.

Beim Abtasten wird der Wert der getroffenen 10-m-Zelle ohne weitere Interpolation übertragen. Für NoData entsteht `NULL` in `hoehe_m`. Raster- und Beobachtungsunsicherheit bleiben bestehen.

## WMS und Offlineabbildung

Verbindung: **HLNUG Schutzgebiete Hessen**. Dienstadresse:

`https://geodienste-umwelt.hessen.de/arcgis/services/inspire/schutzgebiete/MapServer/WmsServer`

Layername: `Naturschutzgebiete`; WMS 1.3.0, PNG, CRS EPSG:25832. `wms_schutzgebiete.png` wurde für das Untersuchungsrechteck mit 1000 × 1000 Pixeln abgerufen. Die transparente Abbildung dient der gemeinsamen Besprechung bei Dienstausfall. Sie ersetzt keine Vektorgeometrien. Quellen- und Nutzungsangaben entsprechen den Schutzgebietsdaten.
