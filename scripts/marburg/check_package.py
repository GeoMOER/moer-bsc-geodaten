#!/usr/bin/python3
"""Check an unpacked package and rehearse its binding QGIS classroom paths."""
import shutil,sys,json,tempfile,time
from pathlib import Path
from zipfile import ZipFile
sys.path.append('/usr/share/qgis/python/plugins')
from qgis.core import (Qgis,QgsApplication,QgsCoordinateReferenceSystem,
                       QgsLayoutExporter,QgsProject,QgsRasterLayer,QgsVectorLayer)
from qgis.PyQt.QtCore import QUrl
from qgis.analysis import QgsNativeAlgorithms
QgsApplication.setPrefixPath('/usr',True)
app=QgsApplication([],False,tempfile.mkdtemp(prefix='qgis-marburg-profile-'));app.initQgis()
QgsApplication.processingRegistry().addProvider(QgsNativeAlgorithms())
import processing
base=Path(sys.argv[1]).resolve()
report=json.loads((base/'documentation/pruefbericht.json').read_text())
csv=QgsVectorLayer(QUrl.fromLocalFile(str(base/'data_raw/gbif_feuersalamander_marburg.csv')).toString()+'?type=csv&delimiter=,&xField=decimalLongitude&yField=decimalLatitude&crs=EPSG:4326&detectTypes=yes','csv','delimitedtext')
assert csv.isValid() and csv.featureCount()==79
selected=processing.run('native:extractbyexpression',{'INPUT':csv,'EXPRESSION':'"coordinateUncertaintyInMeters" > 0 AND "coordinateUncertaintyInMeters" <= 100','OUTPUT':'memory:'})['OUTPUT']
projected=processing.run('native:reprojectlayer',{'INPUT':selected,'TARGET_CRS':'EPSG:25832','OUTPUT':'memory:'})['OUTPUT']
expected=QgsVectorLayer(str(base/'ersatz/unit11_results.gpkg')+'|layername=gbif_checked','checked','ogr')
assert [(f.name(),f.type()) for f in projected.fields()]==[(f.name(),f.type()) for f in expected.fields() if f.name()!='fid']
byid={f['gbifID']:f for f in expected.getFeatures()}
assert set(byid)=={f['gbifID'] for f in projected.getFeatures()}
assert all(f.geometry().distance(byid[f['gbifID']].geometry())<1e-6 for f in projected.getFeatures())
polygons=QgsVectorLayer(str(base/'ersatz/unit12_results.gpkg')+'|layername=schutzgebiete_auswahl','areas','ogr')
location=processing.run('native:extractbylocation',{'INPUT':expected,'PREDICATE':[0],'INTERSECT':polygons,'OUTPUT':'memory:'})['OUTPUT']
assert location.featureCount()==4
rivers=QgsVectorLayer(str(base/'data_raw/marburg_basis.gpkg')+'|layername=gewaesser','rivers','ogr')
location=processing.run('native:extractbylocation',{'INPUT':rivers,'PREDICATE':[0],'INTERSECT':polygons,'OUTPUT':'memory:'})['OUTPUT']
assert location.featureCount()==106
sampled=processing.run('native:rastersampling',{'INPUT':expected,'RASTERCOPY':str(base/'data_raw/dgm_marburg_10m.tif'),'COLUMN_PREFIX':'hoehe_','OUTPUT':'memory:'})['OUTPUT']
assert 'hoehe_1' in sampled.fields().names()
from qgis.core import QgsVariantUtils
checks={r['gbifID']:r['hoehe_m'] for r in report['height_samples']}
for f in sampled.getFeatures():
 value=f['hoehe_1'];want=checks[f['gbifID']]
 assert (want is None and QgsVariantUtils.isNull(value)) or (want is not None and abs(value-want)<1e-5),(f['gbifID'],value,want)

# Work in another copy so the check never adds classroom outputs to its input.
work_root=Path(tempfile.mkdtemp(prefix='marburg-classroom-paths-'))
work=work_root/'marburg_geodaten'
shutil.copytree(base,work)

# Unit 10: create a local project, use relative paths, close it and reopen it.
started=time.perf_counter()
project=QgsProject.instance();project.clear()
project.setCrs(QgsCoordinateReferenceSystem('EPSG:25832'))
project.setFilePathStorage(Qgis.FilePathType.Relative)
unit10_vector=QgsVectorLayer(str(work/'data_raw/marburg_basis.gpkg')+'|layername=gewaesser','Gewässer','ogr')
unit10_raster=QgsRasterLayer(str(work/'data_raw/dgm_marburg_10m.tif'),'DGM – Geländehöhe','gdal')
assert unit10_vector.isValid() and unit10_vector.featureCount()==412
assert unit10_raster.isValid() and unit10_raster.crs().authid()=='EPSG:25832'
project.addMapLayer(unit10_raster);project.addMapLayer(unit10_vector)
unit10_project=work/'unit10_einstieg.qgz'
project.setFileName(str(unit10_project));assert project.write()
with ZipFile(unit10_project) as archive:
 qgs_name=next(name for name in archive.namelist() if name.endswith('.qgs'))
 qgs_text=archive.read(qgs_name).decode('utf-8')
 assert str(work) not in qgs_text and 'data_raw/marburg_basis.gpkg' in qgs_text
project.clear();assert project.read(str(unit10_project))
assert len(project.mapLayers())==2 and all(layer.isValid() for layer in project.mapLayers().values())
unit10_seconds=time.perf_counter()-started
print(f'Unit 10 Trockenlauf: lokales Projekt mit Vektor und Raster gespeichert und erneut geöffnet ({unit10_seconds:.2f} s).')

for name in ['unit14_start.qgz','unit14_beispiel.qgz']:
 project=QgsProject.instance();project.clear();assert project.read(str(base/name))
 assert len(project.mapLayers())==3
 for layer in project.mapLayers().values():
  assert layer.isValid(),(name,layer.source())
  assert str(base) in layer.source(),(name,layer.source())
 layout=project.layoutManager().layoutByName('abschlusskarte_unit14');assert layout
 print(name,'relative Datenquellen nach Verschieben gültig; Layout vorhanden')
settings=QgsLayoutExporter.ImageExportSettings();settings.dpi=80;settings.exportMetadata=False
assert QgsLayoutExporter(layout).exportToImage(str(Path(tempfile.mkdtemp(prefix='marburg-render-'))/'check.png'),settings)==QgsLayoutExporter.Success

# Unit 14: save the prepared project as a classroom copy and export both products.
started=time.perf_counter()
project.clear();assert project.read(str(work/'unit14_start.qgz'))
point_layers=[layer for layer in project.mapLayers().values()
              if isinstance(layer,QgsVectorLayer) and 'hoehe_m' in layer.fields().names()]
assert len(point_layers)==1 and point_layers[0].featureCount()==35
assert all(not QgsVariantUtils.isNull(feature['hoehe_m']) for feature in point_layers[0].getFeatures())
layout=project.layoutManager().layoutByName('abschlusskarte_unit14');assert layout
unit14_project=work/'unit14_abschluss.qgz'
project.setFileName(str(unit14_project));assert project.write()
image_settings=QgsLayoutExporter.ImageExportSettings();image_settings.dpi=150;image_settings.exportMetadata=False
pdf_settings=QgsLayoutExporter.PdfExportSettings();pdf_settings.dpi=150
png_path=work/'figures/abschlusskarte_unit14.png'
pdf_path=work/'figures/abschlusskarte_unit14.pdf'
exporter=QgsLayoutExporter(layout)
assert exporter.exportToImage(str(png_path),image_settings)==QgsLayoutExporter.Success
assert exporter.exportToPdf(str(pdf_path),pdf_settings)==QgsLayoutExporter.Success
assert png_path.stat().st_size>0 and pdf_path.stat().st_size>0
project.clear();assert project.read(str(unit14_project))
assert len(project.mapLayers())==3 and all(layer.isValid() for layer in project.mapLayers().values())
unit14_seconds=time.perf_counter()-started
print(f'Unit 14 Trockenlauf: 35 Höhenwerte, Arbeitskopie, Layout, PDF und PNG mit 150 dpi geprüft ({unit14_seconds:.2f} s).')
print('CSV-Schema, IDs, Koordinatentransformation, beide räumlichen Auswahlen und alle 56 Höhenwerte mit nativen QGIS-Werkzeugen bestätigt.')
