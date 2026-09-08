# Marburger Lehrdaten aufbereiten

Das verteilte Paket ist ein fester Snapshot vom 08.09.2026. Quelldaten und Auswahlregeln stehen in `sources.json`; die ursprünglichen Eingangsprüfsummen befinden sich im Paket unter `documentation/pruefbericht.json`. Die großen amtlichen Rohdaten werden nicht ins Repository aufgenommen.

## Voraussetzungen

System-Python mit QGIS, GDAL und NumPy; geprüft mit QGIS 3.40.15. Der Aufbau erfolgt ohne GUI. `fetch_sources.py` verwendet `curl` und lädt etwa 365 MB öffentliche Daten. Die abgefragten Livequellen können sich ändern; deshalb ist ein erneuter Abruf nicht automatisch identisch zum vorhandenen Snapshot.

```bash
/usr/bin/python3 scripts/marburg/fetch_sources.py /tmp/marburg-sources-new
QT_QPA_PLATFORM=offscreen /usr/bin/python3 scripts/marburg/build_package.py \
  --sources /tmp/marburg-sources-new \
  --output /tmp/marburg-package-new
```

Quell- und Ausgabeordner müssen neu oder leer sein. Temporäre GDS-Downloadadressen werden aus der öffentlichen Dateiliste neu aufgelöst. Nach Änderungen der amtlichen Metadatenliste muss deren URL in `sources.json` aktualisiert werden. Der Builder bricht bei geänderten GBIF-Ausgangszahlen bewusst ab: Daten, Kontrollwerte, Dokumentation und Kursseiten müssen dann gemeinsam überprüft werden.

Der Builder erzeugt Basislayer, CSV/CSVT, Ersatzlayer, ein gemitteltes 10-m-DGM, ein QGIS-Startprojekt, eine QPT-Vorlage sowie Kartenbeispiele als PDF/PNG. Die Texte aus `templates/` gehören zum Paket. Exporte verwenden relative Datenpfade. Quelldatensatz-DOI und Download-DOI dürfen nicht verwechselt werden; der API-Snapshot hat keinen eigenen GBIF-Download-DOI.

Die beim Aufbau geprüften Geometrien und Featurezahlen ersetzen nicht den fachlichen Probelauf mit Studierenden. Nach Änderungen an Auswahl oder Rasteraufbereitung zusätzlich die QGIS-Werkzeuge aus den Kursanleitungen gegen die Ersatzdaten prüfen und beide Projekte nach Verschieben des Paketordners erneut öffnen.

## Paket prüfen

Entpacken Sie das ZIP an einem anderen Speicherort und prüfen Sie es mit den normalen QGIS-Werkzeugen:

```bash
QT_QPA_PLATFORM=offscreen /usr/bin/python3 scripts/marburg/check_package.py /tmp/anderer-ort/marburg_geodaten
```

Die Prüfung kontrolliert CSV-Feldtypen und IDs, die Koordinatentransformation, beide räumlichen Auswahlen, alle abgetasteten Höhenwerte und die relativen Datenquellen beider Kartenprojekte. Sie rendert außerdem das verschobene Beispielprojekt in einen temporären Ordner.

## Paket erstellen

Alle Dateien unter einem gemeinsamen Ordner `marburg_geodaten/` zippen. Nicht in das ZIP gehören temporäre GDAL-Dateien (`*.aux.xml`), QGIS-Sicherungen oder Python-Caches. Der leere Ordner `data_output/` soll enthalten sein.

Die Kurswebsite verweist auf `docs/assets/data/marburg/marburg_geodaten.zip`. Daneben liegt die Beispielkarte als Vorschau. Der Einstieg erfolgt über `docs/material/marburg.md`. Das Einchecken/Veröffentlichen gehört nicht zum Builder.
