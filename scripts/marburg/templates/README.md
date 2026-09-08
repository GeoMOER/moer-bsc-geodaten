# Marburg und Umgebung: Übungspaket für Units 10–14

Stand: 08.09.2026. Geprüft mit QGIS 3.40.15.

Entpacken Sie das gesamte ZIP in einen beschreibbaren lokalen Ordner. Arbeiten Sie nicht direkt im ZIP. Behalten Sie die Ordnerstruktur bei: Die QGIS-Projekte verwenden relative Dateipfade.

## Einstieg

1. Öffnen Sie QGIS. Das gemeinsame Projekt- und Ausgabe-CRS ist **ETRS89 / UTM 32N, EPSG:25832**.
2. Unit 10 beginnt mit `data_raw/marburg_basis.gpkg`, Layer `gewaesser`, und `data_raw/dgm_marburg_10m.tif`.
3. Speichern Sie eigene Ergebnisse in `data_output/` und Projekte im Hauptordner dieses Pakets. Die Ausgangsdaten in `data_raw/` bleiben unverändert.
4. Ergänzen Sie `documentation/processing_notes.md` während der Übungen.

## Inhalt und Übergänge

| Unit | Eingang | Eigenes Ergebnis |
|---|---|---|
| 10 | Gewässerlayer, DGM, vorgegebener Schutzgebiets-WMS | `unit10_einstieg.qgz` |
| 11 | `data_raw/gbif_feuersalamander_marburg.csv` | `data_output/unit11_results.gpkg`, Layer `gbif_checked` |
| 12 | geprüfte GBIF-Punkte und Basis-GeoPackage | `data_output/unit12_results.gpkg`, Layer `schutzgebiete_auswahl`, `gbif_in_schutzgebieten`, `gewaesser_an_schutzgebieten` |
| 13 | geprüfte GBIF-Punkte und DGM | `data_output/unit13_results.gpkg`, Layer `gbif_mit_hoehe` mit `hoehe_m` |
| 14 | `unit14_start.qgz` mit geprüften Punkten und vorbereitetem Layout | `unit14_abschluss.qgz`; eigene PDF und PNG in `figures/`; eigener Ergebnislayer nur als Vertiefung |

## Ersatz und Beispiele

`ersatz/` enthält geprüfte Ergebnisse der Units 11–14. Sie ermöglichen die gemeinsame Weiterarbeit bei technischen Problemen. Quelle und Verwendung eines Ersatzes gehören ins Protokoll.

`unit14_start.qgz` ist ein vorbereitetes Projekt mit einfachem Layout und Ersatzdaten. Wählen und begründen Sie darin Ihre Klassifizierung. `unit14_beispiel.qgz` und `figures/abschlusskarte_beispiel.*` zeigen eine mögliche Ausarbeitung. Zwei vergleichbare Darstellungen mit gleichen Intervallen und Quantilen liegen als PNG in `ersatz/`.

`ersatz/wms_schutzgebiete.png` und `ersatz/wms_capabilities.xml` dokumentieren den verwendeten WMS. Der PNG-Ausschnitt ist eine transparente Kartenabbildung und kein analysierbarer Vektorlayer.

## Räumliche Abdeckung

Das Untersuchungsgebiet ist ein didaktisches Rechteck von 20 × 20 km um Marburg, keine Verwaltungsgrenze. Schutzgebiets- und Gewässerfeatures bleiben vollständig erhalten und können über dieses Rechteck hinausreichen. `orientierung` enthält einen gerundeten Marburg-Punkt für die Kartenbeschriftung.

Das DGM enthält die Kacheln des amtlichen Downloadpakets **Marburg**, auf 10-m-Mittelwerte reduziert. Es deckt nicht das ganze Untersuchungsrechteck ab. Weiße Bereiche sind NoData. Von 56 geprüften Nachweisen besitzen 35 einen Höhenwert; 21 bleiben in Unit 13 mit `NULL` erhalten. Unit 14 kartiert die 35 Nachweise mit gültiger Höhe. Diese zusätzliche räumliche Auswahl muss bei der Interpretation berücksichtigt werden.

Quellen, Nutzungsangaben, Schema und Bearbeitung: `documentation/quellen.md`. Kontrollwerte: `documentation/pruefwerte.md`; maschinenlesbare Prüfung: `documentation/pruefbericht.json`.
