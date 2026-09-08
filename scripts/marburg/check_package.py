#!/usr/bin/python3
"""Check an unpacked package with native QGIS tools, ideally after relocation."""
import sys,json,tempfile
from pathlib import Path
sys.path.append('/usr/share/qgis/python/plugins')
from qgis.core import QgsApplication,QgsVectorLayer,QgsRasterLayer,QgsProject,QgsExpression,QgsFeatureRequest,QgsLayoutExporter
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
print('CSV-Schema, IDs, Koordinatentransformation, beide räumlichen Auswahlen und alle 56 Höhenwerte mit nativen QGIS-Werkzeugen bestätigt.')
