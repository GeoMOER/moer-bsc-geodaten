---
title: "Übungsdaten: Marburg und Umgebung"
layout: single
permalink: /material/marburg.html
toc: true
---

Für Units 10–14 verwenden wir ein gemeinsames Datenpaket aus Marburg und Umgebung. Sie arbeiten damit vom ersten QGIS-Projekt über räumliche Auswahlen und Höhenwerte bis zur Abschlusskarte.

**[Übungspaket herunterladen (ZIP)]({{ '/assets/data/marburg/marburg_geodaten.zip' | relative_url }})**

Stand: **08.09.2026**. Paket und Kartenprojekte sind mit **QGIS 3.40.15** geprüft. Verwenden Sie für die Kursanleitungen QGIS 3.40. Das Paket enthält bereits geprüfte Ersatzdaten und benötigt nach dem Download für die Kernübungen keinen weiteren Datenabruf; den WMS betrachten wir zusätzlich live oder anhand des mitgelieferten Ersatzbilds.

## So beginnen Sie

1. Entpacken Sie das gesamte ZIP in einen beschreibbaren lokalen Ordner. Arbeiten Sie nicht direkt im ZIP.
2. Behalten Sie die Ordnerstruktur bei. Speichern Sie neue QGIS-Projekte im Hauptordner `marburg_geodaten/` und eigene Geodaten in `data_output/`.
3. Verwenden Sie als Projekt- und Ausgabe-CRS **ETRS89 / UTM Zone 32N (`EPSG:25832`)**.
4. Öffnen Sie `documentation/processing_notes.md` als begleitendes Arbeitsprotokoll. Quellen und Bearbeitung stehen in `documentation/quellen.md`.

Die Originaldateien in `data_raw/` bleiben unverändert. Die bereitgestellten Ersatzdateien in `ersatz/` ermöglichen die gemeinsame Weiterarbeit, wenn ein eigener Arbeitsschritt noch nicht gelungen ist. Notieren Sie ihre Verwendung im Protokoll.

Die [QGIS-Kurzchecklisten für Units 10–14]({{ '/material/qgis-kernpfade.html' | relative_url }}) zeigen die verbindlichen Arbeitsschritte, erwarteten Kontrollwerte und vorbereiteten Ausweichwege auf einer Seite.

## Was verwenden wir in welcher Unit?

| Unit | Material | Gemeinsamer Arbeitsschritt |
|---|---|---|
| [10]({{ '/unit10/unit10-00_overview.html' | relative_url }}) | `marburg_basis.gpkg`, Layer `gewaesser`, und `dgm_marburg_10m.tif` in `data_raw/` | Layer laden, Attribute und CRS prüfen, Projekt speichern |
| [11]({{ '/unit11/unit11-00_overview.html' | relative_url }}) | `data_raw/gbif_feuersalamander_marburg.csv` und gleichnamige CSVT-Datei | Nachweise importieren, Unsicherheit beurteilen und `gbif_checked` speichern |
| [12]({{ '/unit12/unit12-00_overview.html' | relative_url }}) | `gbif_checked` und die Basislayer `schutzgebiete` und `gewaesser` | FFH-Gebiete auswählen; Punkte und Gewässer räumlich zuordnen |
| [13]({{ '/unit13/unit13-00_overview.html' | relative_url }}) | `gbif_checked` und das DGM | Höhenwerte nach `hoehe_m` übertragen und fehlende Werte erklären |
| [14]({{ '/unit14/unit14-00_overview.html' | relative_url }}) | `unit14_start.qgz`, vorbereitete Punktdaten und Layout | Klassifizierung begründen, Karte überarbeiten und exportieren |

## Untersuchungsgebiet und Grenzen der Daten

Das Untersuchungsgebiet ist ein **20 × 20 km großes Rechteck um Marburg**. In EPSG:25832 reicht es von 474000 bis 494000 m Ost und von 5619000 bis 5639000 m Nord. Das Rechteck wurde für die Lehre gewählt und ist keine Verwaltungsgrenze.

Das Basis-GeoPackage enthält 12 Naturschutzgebiete, 10 FFH-Gebiete und 412 Gewässerfeatures, deren Geometrien dieses Rechteck schneiden. Die Features bleiben vollständig erhalten und können darüber hinausreichen. Der Layer `untersuchungsgebiet` zeigt das Rechteck; `orientierung` enthält einen gerundeten Marburg-Punkt zur Kartenbeschriftung.

Die 79 Feuersalamander-Nachweise stammen aus **NABU&#124;naturgucker über GBIF**. Wir verwenden einen dokumentierten API-Snapshot; er besitzt keinen eigenen GBIF-Download-DOI. Der DOI in der Quellenangabe bezeichnet den Quelldatensatz. Mit der Übungsregel „angegebene Koordinatenunsicherheit größer null und höchstens 100 m“ bleiben 56 Nachweise. Diese Auswahl ist kein allgemeiner Qualitätsstandard.

Das Geländemodell enthält **10-m-Mittelwerte aus den DGM1-Kacheln des Marburger Downloadpakets**. Es ist ein abgeleitetes Lehrprodukt und deckt nicht das ganze Untersuchungsrechteck ab. Der Höhenbezug ist DHHN2016_NH; Höhen werden in Metern angegeben. Außerhalb der verfügbaren Kacheln steht NoData (-9999).

Von den 56 geprüften Nachweisen erhalten 35 einen Höhenwert. Die übrigen 21 bleiben in Unit 13 mit `NULL` erhalten. Für die Höhenklassenkarte in Unit 14 verwenden wir nur die 35 Nachweise mit gültiger Höhe. Diese räumliche Einschränkung gehört zur Interpretation; fehlende Punkte auf der Karte belegen keine Abwesenheit der Art.

## Vorbereitetes Kartenprojekt

Öffnen Sie `unit14_start.qgz`, speichern Sie eine Arbeitskopie als `unit14_abschluss.qgz` und verwenden Sie das darin enthaltene Layout `abschlusskarte_unit14`. Das Projekt enthält die geprüften Ersatzdaten mit gültigen Höhenwerten. Sie wählen die Klassifizierung und überarbeiten Titel, Legende und Aussage. Die Verwendung eigener Ergebnisse und das Ersetzen der vorbereiteten Datenquelle sind freiwillige Vertiefung; folgen Sie dafür dem [Abschnitt Kartenlayout]({{ '/unit14/unit14-03_kartenlayout.html' | relative_url }}).

Zwei Kartenbilder im Ordner `ersatz/` zeigen dieselben Nachweise mit gleichen Intervallen beziehungsweise Quantilen. Das Projekt `unit14_beispiel.qgz` und die PDF/PNG in `figures/` zeigen eine mögliche Ausarbeitung.

![Beispielkarte: Feuersalamander-Nachweise bei Marburg, nach Geländehöhe klassifiziert; die weiße Umgebung liegt außerhalb der DGM-Abdeckung.]({{ '/assets/data/marburg/abschlusskarte_beispiel.png' | relative_url }})

[Beispielkarte als PDF]({{ '/assets/data/marburg/abschlusskarte_beispiel.pdf' | relative_url }})

## WMS für Unit 10

Verbindungsname: **HLNUG Schutzgebiete Hessen**

```text
https://geodienste-umwelt.hessen.de/arcgis/services/inspire/schutzgebiete/MapServer/WmsServer
```

Wählen Sie den Layer **`Naturschutzgebiete`**. Die [amtliche Dienstübersicht](https://www.hlnug.de/themen/geografische-informationssysteme/geodienste/naturschutz) enthält die Beschreibung und den GetCapabilities-Link. Bei Dienstausfall verwenden wir `ersatz/wms_schutzgebiete.png`, `ersatz/wms_capabilities.xml` und die Quellenbeschreibung im Paket. Das transparente PNG ist ein Kartenbild und kein Vektordatensatz.

## Quellen und Nutzungsangaben

- **Nachweise:** [NABU&#124;naturgucker, doi:10.15468/uc1apo](https://doi.org/10.15468/uc1apo), CC BY 4.0; räumliche und fachliche Auswahl für GeoMOER.
- **Schutzgebiete:** [HMLU / HLNUG](https://www.hlnug.de/themen/geografische-informationssysteme/geodienste/naturschutz); kostenfreie Nutzung mit Quellenvermerk nach den im Paket dokumentierten Dienstbedingungen.
- **Gewässer:** [HLNUG, Gewässernetz 1:25.000](https://www.hlnug.de/themen/geografische-informationssysteme/geodienste/wasser), CC BY 4.0; räumliche Auswahl und vereinfachtes Attributschema.
- **Geländemodell:** [Hessen Geodatenmanagement, DGM1](https://hvbg.hessen.de/landesvermessung/geotopographie/3d-daten/digitale-gelaendemodelle), Datenlizenz Deutschland Zero 2.0 gemäß den [amtlichen Metadaten](https://www.geoportal.hessen.de/mapbender/php/mod_iso19139ToHtml.php?url=https%3A%2F%2Fwww.geoportal.hessen.de%2Fmapbender%2Fphp%2Fmod_dataISOMetadata.php%3FoutputFormat%3Diso19139%26id%3Ddbf48a95-b44d-48b3-a5b4-981e4c1bd8e6); für die Lehre mosaikiert und auf 10 m gemittelt.

Die vollständigen Quellenvermerke, Befliegungsdaten, Datentypen, Auswahlregeln und Kontrollwerte liegen im Ordner `documentation/`. Das Abrufdatum ist nicht mit dem Erfassungsdatum der Daten gleichzusetzen.
