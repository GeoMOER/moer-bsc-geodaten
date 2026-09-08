# Bearbeitungsprotokoll: Marburg und Umgebung

Name: [eintragen] · Datum: [eintragen]

Gemeinsames Projekt-/Ausgabe-CRS: EPSG:25832. Ausgangsdaten und Nutzungsangaben: `quellen.md`. Paketstand: 08.09.2026. Bei Verwendung von Ersatzdaten die betreffende Unit und den Grund notieren.

## Unit 10: Projekt und Daten

| Prüfung | Ergebnis |
|---|---|
| Projektdatei | `unit10_einstieg.qgz` |
| Vektor | `data_raw/marburg_basis.gpkg`, Layer `gewaesser` |
| Raster | `data_raw/dgm_marburg_10m.tif` |
| Datenmodelle und Layer-CRS geprüft | [eintragen] |
| WMS | HLNUG Schutzgebiete Hessen, Layer `Naturschutzgebiete`; URL in `quellen.md` |
| WMS-Zugriffsdatum / Offlineersatz verwendet | [eintragen] |
| Projekt nach erneutem Öffnen vollständig | [eintragen] |

## Unit 11: Nachweise prüfen

Quelle: NABU|naturgucker via GBIF, doi:10.15468/uc1apo, CC BY 4.0. API-Snapshot ohne eigenen Download-DOI. Datei: `data_raw/gbif_feuersalamander_marburg.csv`.

Import: UTF-8; Komma; x=`decimalLongitude`, y=`decimalLatitude`; EPSG:4326. Ausgabe: EPSG:25832.

| Entscheidung / Kontrolle | Ergebnis |
|---|---|
| Anzahl importierter Records | [eintragen] |
| Regel | `coordinateUncertaintyInMeters > 0 AND coordinateUncertaintyInMeters <= 100` |
| Fachliche Begründung und Grenze der Regel | [eintragen] |
| Anzahl ausgewählter / ausgeschlossener Records | [eintragen] |
| Ausgabe | `data_output/unit11_results.gpkg`, Layer `gbif_checked` |
| Export erneut geladen und geprüft | [eintragen] |
| Angemessene Aussage zur Punktkarte | [eintragen] |
| Ersatzdaten verwendet | [eintragen] |

## Unit 12: Räumliche Auswahl

Eingang: `gbif_checked`, Schutzgebiete und Gewässer aus `marburg_basis.gpkg`. Quellen: HMLU / HLNUG; vollständige Vermerke in `quellen.md`.

| Auswahl | Regel | Featurezahl |
|---|---|---:|
| Schutzgebiete | `"kategorie" = 'FFH'` | [eintragen] |
| GBIF-Punkte | schneidet `schutzgebiete_auswahl` | [eintragen] |
| Gewässer | schneidet `schutzgebiete_auswahl` | [eintragen] |

Ausgabe: `data_output/unit12_results.gpkg` mit `schutzgebiete_auswahl`, `gbif_in_schutzgebieten`, `gewaesser_an_schutzgebieten`.

Exportprüfung: [eintragen] · Fachliche Einschränkung am Grenzfall: [eintragen] · Ersatzdaten: [eintragen]

## Unit 13: Höhenwerte übertragen

DGM: Hessen Geodatenmanagement, DGM1-Paket Marburg, für diesen Kurs auf 10 m gemittelt. Einheit m, Höhenbezug DHHN2016_NH, horizontales CRS EPSG:25832, NoData=-9999. Die Rasterabdeckung ist kleiner als das Untersuchungsrechteck.

| Kontrolle | Ergebnis |
|---|---|
| Punkteingang | `gbif_checked` aus Unit 11 |
| Werkzeug / erzeugtes Höhenfeld | [eintragen] |
| Übernahme nach `hoehe_m` als Dezimalzahl | [eintragen] |
| Anzahl gültiger / fehlender Höhenwerte | [eintragen] |
| Kontrollpunkt: GBIF-ID und direkt abgefragter Rasterwert | [eintragen] |
| NoData-Beispiel: GBIF-ID und Erklärung | [eintragen] |
| Aussagegrenzen durch Raster- und Koordinatenunsicherheit | [eintragen] |
| Ausgabe | `data_output/unit13_results.gpkg`, Layer `gbif_mit_hoehe` |
| Ersatzdaten verwendet | [eintragen] |

## Unit 14: Abschlusskarte

Kartenfrage: Wo liegen dokumentierte Feuersalamander-Nachweise, und welchen Höhenklassen sind sie zugeordnet? Zielgruppe: fachlich interessierte Personen ohne Kenntnis des Datensatzes.

| Entscheidung / Kontrolle | Ergebnis |
|---|---|
| Kartierte Auswahl | `"hoehe_m" IS NOT NULL` |
| Anzahl dargestellter / wegen NoData nicht dargestellter Records | [eintragen] |
| Punktlayer | vorbereiteter Ersatz `ersatz/unit14_results.gpkg/gbif_mit_hoehe_final`; eigener Ergebnislayer nur bei freiwilliger Vertiefung |
| Klassifizierung / Klassenzahl / Klassengrenzen | [eintragen] |
| Begründung der Methode und Farbpalette | [eintragen] |
| Bewusst nicht dargestellte Inhalte | [eintragen] |
| Fachliche Grenze der Kartenaussage | [eintragen] |
| Überarbeitung nach Partnercheck | [eintragen] |
| PDF / PNG geöffnet und geprüft | [eintragen] |

Arbeitsprojekt: `unit14_abschluss.qgz`. Exporte: `figures/abschlusskarte_unit14.pdf` und `figures/abschlusskarte_unit14.png`. Quellenangaben des vorbereiteten Layouts erhalten, prüfen und bei Bedarf ergänzen.
