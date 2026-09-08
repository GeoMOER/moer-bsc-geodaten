#!/usr/bin/python3
"""Build the Marburg teaching package offline from the documented source snapshot.

Run with the system Python providing QGIS and GDAL, QT_QPA_PLATFORM=offscreen.
The output directory must be new or empty. See README.md for source acquisition.
"""
import argparse
import csv
import hashlib
import json
import math
from pathlib import Path
import shutil
from datetime import datetime, timedelta
import xml.etree.ElementTree as ET
from zipfile import ZipFile, ZIP_DEFLATED

import numpy as np
from osgeo import gdal
from qgis.core import (
    Qgis, QgsApplication, QgsCoordinateReferenceSystem, QgsCoordinateTransform,
    QgsFeature, QgsField, QgsFillSymbol, QgsGeometry, QgsGraduatedSymbolRenderer,
    QgsLayoutExporter, QgsLayoutItemLabel, QgsLayoutItemLegend, QgsLayoutItemMap,
    QgsLayoutItemScaleBar, QgsLayoutPoint, QgsLayoutSize, QgsLineSymbol,
    QgsMarkerSymbol, QgsPrintLayout, QgsProject, QgsRasterLayer,
    QgsRectangle, QgsRendererRange, QgsSingleBandGrayRenderer,
    QgsContrastEnhancement, QgsVectorFileWriter, QgsVectorLayer, QgsReadWriteContext, QgsPathResolver,
    QgsPalLayerSettings, QgsTextFormat, QgsVectorLayerSimpleLabeling,
)
from qgis.PyQt.QtCore import QMetaType
from qgis.PyQt.QtGui import QColor, QFont
from qgis.PyQt.QtXml import QDomDocument

BBOX = (474000, 5619000, 494000, 5639000)
DATASET = '6ac3f774-d9fb-4796-b3e9-92bf6c81c084'
FIELDS = ['gbifID','occurrenceID','scientificName','species','basisOfRecord',
          'eventDate','year','decimalLongitude','decimalLatitude',
          'coordinateUncertaintyInMeters','datasetKey','license','issue']
NUMERIC = {'year':QMetaType.Type.Int, 'decimalLongitude':QMetaType.Type.Double,
           'decimalLatitude':QMetaType.Type.Double,
           'coordinateUncertaintyInMeters':QMetaType.Type.Double}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sources', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    src, out = args.sources.resolve(), args.output.resolve()
    if out.exists() and any(out.iterdir()):
        parser.error('Output directory must be new or empty.')
    for d in ['data_raw','data_output','ersatz','documentation','figures','vorlagen']:
        (out/d).mkdir(parents=True, exist_ok=True)
    app = QgsApplication([], False)
    app.initQgis()
    gdal.UseExceptions()
    project = QgsProject.instance()
    crs = QgsCoordinateReferenceSystem('EPSG:25832')
    project.setCrs(crs)
    project.setFilePathStorage(Qgis.FilePathType.Relative)
    transform = QgsCoordinateTransform(QgsCoordinateReferenceSystem('EPSG:4326'), crs, project)
    rectangle = QgsRectangle(*BBOX)
    area = QgsGeometry.fromRect(rectangle)
    report = {'qgis_version':Qgis.QGIS_VERSION, 'bbox_epsg25832':BBOX}

    def memory(name, geometry, fields):
        layer = QgsVectorLayer(f'{geometry}?crs=EPSG:25832', name, 'memory')
        provider = layer.dataProvider()
        provider.addAttributes([QgsField(n, typ) for n,typ in fields])
        layer.updateFields()
        return layer

    def add(layer, geom, attrs):
        feature = QgsFeature(layer.fields())
        feature.setGeometry(geom)
        feature.setAttributes(attrs)
        assert layer.dataProvider().addFeatures([feature])[0]

    def save(layer, filename, name):
        path = out/filename
        options = QgsVectorFileWriter.SaveVectorOptions()
        options.driverName = 'GPKG'
        options.layerName = name
        options.actionOnExistingFile = (QgsVectorFileWriter.CreateOrOverwriteLayer if path.exists()
                                       else QgsVectorFileWriter.CreateOrOverwriteFile)
        result = QgsVectorFileWriter.writeAsVectorFormatV3(layer,str(path),project.transformContext(),options)
        if result[0] != QgsVectorFileWriter.NoError:
            raise RuntimeError(result)
        loaded = QgsVectorLayer(f'{path}|layername={name}',name,'ogr')
        assert loaded.isValid() and loaded.featureCount() == layer.featureCount()
        assert loaded.crs().authid() == 'EPSG:25832'
        assert all(f.geometry().isGeosValid() for f in loaded.getFeatures())
        return loaded

    def subset(layer, name, predicate):
        result = memory(name, 'MultiPolygon' if layer.geometryType()==Qgis.GeometryType.Polygon
                        else 'MultiLineString' if layer.geometryType()==Qgis.GeometryType.Line else 'Point',
                        [(f.name(),f.type()) for f in layer.fields()])
        for f in layer.getFeatures():
            if predicate(f): add(result,f.geometry(),f.attributes())
        return result

    boundary = memory('untersuchungsgebiet','Polygon',[('name',QMetaType.Type.QString)])
    add(boundary,area,['Marburg und Umgebung – 20 × 20 km, didaktischer Ausschnitt'])
    save(boundary,'data_raw/marburg_basis.gpkg','untersuchungsgebiet')
    orientation=memory('orientierung','Point',[('name',QMetaType.Type.QString)])
    center=QgsGeometry.fromWkt('POINT (8.77 50.81)');center.transform(transform)
    add(orientation,center,['Marburg'])
    orientation=save(orientation,'data_raw/marburg_basis.gpkg','orientierung')
    protected = memory('schutzgebiete','MultiPolygon',[
        ('quell_id',QMetaType.Type.QString),('name',QMetaType.Type.QString),
        ('kategorie',QMetaType.Type.QString),('gebiets_nr',QMetaType.Type.QString)])
    for filename,category in [('nsg','NSG'),('ffh','FFH')]:
        source = QgsVectorLayer(str(src/f'{filename}.geojson'),filename,'ogr')
        assert source.isValid() and source.featureCount()>0
        for f in source.getFeatures():
            geom=f.geometry()
            if not geom.intersects(area): continue
            geom.convertToMultiType()
            add(protected,geom,[f'{category}:{f["OBJECTID"]}',f['NAME'],category,f['NATUREG_NR' if category=='NSG' else 'NATURA_NR']])
    save(protected,'data_raw/marburg_basis.gpkg','schutzgebiete')
    rivers = memory('gewaesser','MultiLineString',[
        ('quell_id',QMetaType.Type.QString),('name',QMetaType.Type.QString),
        ('gewaesserzahl',QMetaType.Type.QString),('ordnung',QMetaType.Type.Int)])
    source = QgsVectorLayer(str(src/'gewaesser.geojson'),'gewaesser','ogr')
    assert source.isValid() and source.featureCount()>0
    for f in source.getFeatures():
        geom=f.geometry()
        if not geom.intersects(area):continue
        geom.convertToMultiType()
        add(rivers,geom,[str(f['OBJECTID']),f['GEWBEZ'],f['GWZ'],f['GEWORDN']])
    save(rivers,'data_raw/marburg_basis.gpkg','gewaesser')
    report['base_features']={'schutzgebiete':protected.featureCount(),'gewaesser':rivers.featureCount()}

    # A fixed, single-source selection. Never alter coordinates or invent records.
    response=json.loads((src/'gbif.json').read_text())
    assert response['endOfRecords'] and len(response['results'])==response['count']
    points=memory('gbif_raw','Point',[(n,NUMERIC.get(n,QMetaType.Type.QString)) for n in FIELDS])
    selected_rows=[]
    for record in response['results']:
        if record['datasetKey'] != DATASET:continue
        assert '/by/4.0/' in record['license']
        lon,lat=record['decimalLongitude'],record['decimalLatitude']
        geom=QgsGeometry.fromWkt(f'POINT ({lon} {lat})')
        geom.transform(transform)
        if not area.intersects(geom):continue
        row={n:record.get(n) for n in FIELDS}
        row['gbifID']=str(record['key'])
        row['issue']=';'.join(record.get('issues',[]))
        selected_rows.append(row)
        add(points,geom,[row[n] for n in FIELDS])
    selected_rows.sort(key=lambda r:r['gbifID'])
    with (out/'data_raw/gbif_feuersalamander_marburg.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=FIELDS)
        writer.writeheader();writer.writerows(selected_rows)
    (out/'data_raw/gbif_feuersalamander_marburg.csvt').write_text(','.join(
        '"Integer"' if n=='year' else '"Real"' if n in NUMERIC else '"String"' for n in FIELDS)+'\n')
    checked=subset(points,'gbif_checked',lambda f:0 < f['coordinateUncertaintyInMeters'] <= 100)
    checked=save(checked,'ersatz/unit11_results.gpkg','gbif_checked')
    report['gbif']={'raw':points.featureCount(),'checked':checked.featureCount(),
                    'rule':'0 < coordinateUncertaintyInMeters <= 100',
                    'excluded':points.featureCount()-checked.featureCount()}
    assert points.featureCount()==79 and checked.featureCount()==56, 'Source snapshot changed; review exercise.'

    selection=subset(protected,'schutzgebiete_auswahl',lambda f:f['kategorie']=='FFH')
    save(selection,'ersatz/unit12_results.gpkg','schutzgebiete_auswahl')
    union=QgsGeometry.unaryUnion([f.geometry() for f in selection.getFeatures()])
    p12=subset(checked,'gbif_in_schutzgebieten',lambda f: f.geometry().intersects(union))
    r12=subset(rivers,'gewaesser_an_schutzgebieten',lambda f: f.geometry().intersects(union))
    save(p12,'ersatz/unit12_results.gpkg','gbif_in_schutzgebieten')
    save(r12,'ersatz/unit12_results.gpkg','gewaesser_an_schutzgebieten')
    report['unit12']={x.name():x.featureCount() for x in [selection,p12,r12]}
    assert 0 < p12.featureCount() < checked.featureCount()
    assert 0 < r12.featureCount() < rivers.featureCount()

    archive=src/'dgm_marburg.zip'
    with ZipFile(archive) as z:
        tiles=[f'/vsizip/{archive}/{n}' for n in z.namelist() if n.lower().endswith('.tif')]
    assert tiles,'DGM archive has no GeoTIFFs'
    vrt=gdal.BuildVRT('',tiles)
    raster_path=out/'data_raw/dgm_marburg_10m.tif'
    raster=gdal.Warp(str(raster_path),vrt,format='GTiff',dstSRS='EPSG:25832',
        outputBounds=BBOX,xRes=10,yRes=10,resampleAlg='average',dstNodata=-9999,
        outputType=gdal.GDT_Float32,creationOptions=['COMPRESS=DEFLATE','PREDICTOR=3','TILED=YES'])
    raster.SetMetadata({'SOURCE':'Hessen DGM1, Downloadpaket Marburg',
                        'PROCESSING':'10 m cell averages derived from 1 m pixels; NoData ignored in averaging',
                        'VERTICAL_REFERENCE':'DHHN2016_NH; height in metres',
                        'LICENSE':'dl-de/zero-2-0'})
    raster.GetRasterBand(1).SetUnitType('m')
    raster.FlushCache()
    values=raster.GetRasterBand(1).ReadAsArray()
    gt=raster.GetGeoTransform()
    valid=values[values!=-9999]
    report['dgm']={'source_tiles':len(tiles),'shape':list(values.shape),
                   'cell_size_m':10,'nodata':-9999,'min':float(valid.min()),'max':float(valid.max()),
                   'valid_cells':int(valid.size),'nodata_cells':int((values==-9999).sum())}
    def sample(point):
        col=math.floor((point.x()-gt[0])/gt[1]);row=math.floor((point.y()-gt[3])/gt[5])
        if not (0<=row<values.shape[0] and 0<=col<values.shape[1]):return None
        value=float(values[row,col])
        return None if value==-9999 else value
    elevated=memory('gbif_mit_hoehe','Point',[(f.name(),f.type()) for f in checked.fields()]+[('hoehe_m',QMetaType.Type.Double)])
    for f in checked.getFeatures():add(elevated,f.geometry(),f.attributes()+[sample(f.geometry().asPoint())])
    elevated=save(elevated,'ersatz/unit13_results.gpkg','gbif_mit_hoehe')
    final=subset(elevated,'gbif_mit_hoehe_final',lambda f: sample(f.geometry().asPoint()) is not None)
    final=save(final,'ersatz/unit14_results.gpkg','gbif_mit_hoehe_final')
    report['unit13']={'features':elevated.featureCount(),'valid_height':final.featureCount(),
                       'null_height':elevated.featureCount()-final.featureCount()}
    assert final.featureCount()>=10
    report['height_samples']=[{'gbifID':f['gbifID'],'hoehe_m':sample(f.geometry().asPoint())}
                              for f in elevated.getFeatures()]
    raster=None;vrt=None

    for source,target in [('wms_nsg.png','wms_schutzgebiete.png'),('schutz_wms.xml','wms_capabilities.xml'),('wasser_wms.xml','wasser_capabilities.xml')]:
        shutil.copyfile(src/source,out/'ersatz'/target)
    from qgis.PyQt.QtGui import QImage
    assert not QImage(str(out/'ersatz/wms_schutzgebiete.png')).isNull(), 'WMS image is not valid'
    with ZipFile(src/'dgm_metadata.xlsx') as archive_metadata:
        ns={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
        strings=[''.join(a.itertext()) for a in ET.fromstring(archive_metadata.read('xl/sharedStrings.xml')).findall('s:si',ns)]
        tile_metadata=[]
        for row in ET.fromstring(archive_metadata.read('xl/worksheets/sheet1.xml')).findall('.//s:row',ns):
            cells={}
            for c in row.findall('s:c',ns):
                v=c.find('s:v',ns)
                cells[''.join(ch for ch in c.get('r') if ch.isalpha())]=(strings[int(v.text)] if c.get('t')=='s' and v is not None else (v.text if v is not None else ''))
            if cells.get('D')=='Marburg':
                tile_metadata.append({'kachel':cells['A'],'befliegung':(datetime(1899,12,30)+timedelta(days=float(cells['B']))).date().isoformat(),'sensor':cells.get('C')})
    (out/'documentation/dgm_kacheln.json').write_text(json.dumps(tile_metadata,indent=2,ensure_ascii=False)+'\n')

    # A portable, offline map project and layout, plus two teaching comparisons.
    project.clear();project.setCrs(crs);project.setFilePathStorage(Qgis.FilePathType.Relative)
    dem=QgsRasterLayer(str(raster_path),'Geländehöhe – DGM, 10 m','gdal')
    assert dem.isValid()
    gray=QgsSingleBandGrayRenderer(dem.dataProvider(),1)
    contrast=QgsContrastEnhancement(dem.dataProvider().dataType(1))
    contrast.setContrastEnhancementAlgorithm(QgsContrastEnhancement.StretchToMinimumMaximum)
    contrast.setMinimumValue(float(valid.min()));contrast.setMaximumValue(float(valid.max()))
    gray.setContrastEnhancement(contrast)
    gray.setOpacity(0.30);dem.setRenderer(gray)
    final.setName('Geländehöhe am Nachweisort [m]')
    project.addMapLayer(dem);project.addMapLayer(final)
    orientation.setRenderer(__import__('qgis.core',fromlist=['QgsSingleSymbolRenderer']).QgsSingleSymbolRenderer(
        QgsMarkerSymbol.createSimple({'name':'cross','color':'#333333','size':'2'})))
    labeling=QgsPalLayerSettings();labeling.fieldName='name'
    text_format=QgsTextFormat();text_format.setFont(QFont('Noto Sans',10));text_format.setSize(10)
    labeling.setFormat(text_format);orientation.setLabeling(QgsVectorLayerSimpleLabeling(labeling));orientation.setLabelsEnabled(True)
    project.addMapLayer(orientation)
    project.viewSettings().setDefaultViewExtent(__import__('qgis.core',fromlist=['QgsReferencedRectangle']).QgsReferencedRectangle(rectangle,crs))
    layout=QgsPrintLayout(project);layout.initializeDefaults();layout.setName('abschlusskarte_unit14')
    layout.pageCollection().pages()[0].setPageSize('A4',QgsLayoutItemPage.Landscape)
    project.layoutManager().addLayout(layout)
    def label(text,x,y,w,h,size=10):
        item=QgsLayoutItemLabel(layout);item.setText(text);item.setFont(QFont('Noto Sans',size))
        layout.addLayoutItem(item);item.attemptMove(QgsLayoutPoint(x,y));item.attemptResize(QgsLayoutSize(w,h))
        return item
    title=label('Feuersalamander-Nachweise bei Marburg',10,6,280,15,18)
    label('Dokumentierte Beobachtungen und Geländehöhe am Nachweisort',10,21,280,8,10)
    map_item=QgsLayoutItemMap(layout);layout.addLayoutItem(map_item)
    map_item.attemptMove(QgsLayoutPoint(10,35));map_item.attemptResize(QgsLayoutSize(160,160))
    map_item.setCrs(crs);map_item.setLayers([orientation,final,dem]);map_item.setKeepLayerSet(True);map_item.zoomToExtent(rectangle)
    map_item.setFrameEnabled(True)
    label('GELÄNDEHÖHE AM NACHWEISORT',181,34,106,8,10)
    method_label=label('Quantile · 5 Klassen',181,43,105,8,10)
    legend=QgsLayoutItemLegend(layout);layout.addLayoutItem(legend);legend.setTitle('')
    legend.setLinkedMap(map_item);legend.setAutoUpdateModel(False)
    root=legend.model().rootGroup();root.clear();root.addLayer(final)
    legend.setStyleFont(QgsLegendStyle.SymbolLabel,QFont('Noto Sans',10))
    legend.setStyleFont(QgsLegendStyle.Subgroup,QFont('Noto Sans',9))
    legend.attemptMove(QgsLayoutPoint(181,54));legend.attemptResize(QgsLayoutSize(103,50))
    label(f'{final.featureCount()} Nachweise mit gültigem Höhenwert\n'
          f'{report["unit13"]["null_height"]} weitere geprüfte Nachweise ohne\nHöhenwert in diesem DGM-Ausschnitt.\n'
          'Leere Kartenbereiche belegen keine\nAbwesenheit der Art.',181,112,106,33,9)
    label('QUELLEN UND BEARBEITUNG',181,149,106,7,10)
    label('NABU|naturgucker via GBIF · CC BY 4.0\ndoi:10.15468/uc1apo · Abruf 08.09.2026\n'
          'DGM1: Hessen Geodatenmanagement\nDatenlizenz Deutschland Zero 2.0\n'
          '10-m-Mittelwerte; Höhen: DHHN2016_NH\nETRS89 / UTM 32N · EPSG:25832\n'
          'Auswahl und Darstellung: GeoMOER',181,157,108,39,8)
    scale=QgsLayoutItemScaleBar(layout);layout.addLayoutItem(scale);scale.setStyle('Single Box')
    scale.setLinkedMap(map_item);scale.setUnits(Qgis.DistanceUnit.Kilometers)
    scale.setUnitsPerSegment(2);scale.setNumberOfSegments(2);scale.setNumberOfSegmentsLeft(0);scale.setUnitLabel('km')
    scale.setFont(QFont('Noto Sans',8));scale.applyDefaultSize()
    scale.setUnits(Qgis.DistanceUnit.Kilometers);scale.setUnitLabel('km')
    scale.setUnitsPerSegment(2);scale.setNumberOfSegments(2)
    scale.attemptMove(QgsLayoutPoint(12,197))
    heights=np.array([f['hoehe_m'] for f in final.getFeatures()])
    colors=['#ffffcc','#c2e699','#78c679','#31a354','#006837']
    def classify(method):
        bounds=np.quantile(heights,np.linspace(0,1,6)) if method=='Quantile' else np.linspace(heights.min(),heights.max(),6)
        ranges=[]
        for i,color in enumerate(colors):
            symbol=QgsMarkerSymbol.createSimple({'name':'circle','color':color,'outline_color':'#263c32','outline_width':'0.18','size':'2.5'})
            prefix='' if i==0 else '> '
            text=f'{prefix}{bounds[i]:.1f} – {bounds[i+1]:.1f}'
            ranges.append(QgsRendererRange(float(bounds[i]),float(bounds[i+1]),symbol,text))
        final.setRenderer(QgsGraduatedSymbolRenderer('hoehe_m',ranges))
        method_label.setText(f'{method} · 5 Klassen')
        legend.model().refreshLayerLegend(root.findLayer(final.id()));legend.adjustBoxSize()
        final.triggerRepaint();layout.refresh()
        report.setdefault('class_boundaries',{})[method]=bounds.tolist()
    def export_png(path):
        settings=QgsLayoutExporter.ImageExportSettings();settings.dpi=150;settings.exportMetadata=False
        assert QgsLayoutExporter(layout).exportToImage(str(path),settings)==QgsLayoutExporter.Success
    for method,filename in [('Gleiche Intervalle','klassifizierung_intervalle.png'),('Quantile','klassifizierung_quantile.png')]:
        classify(method);export_png(out/'ersatz'/filename)
    export_png(out/'figures/abschlusskarte_beispiel.png')
    pdf=QgsLayoutExporter.PdfExportSettings();pdf.dpi=150
    assert QgsLayoutExporter(layout).exportToPdf(str(out/'figures/abschlusskarte_beispiel.pdf'),pdf)==QgsLayoutExporter.Success
    project.setFileName(str(out/'unit14_beispiel.qgz'));assert project.write()
    # Start with a simple symbol; students make and justify the classification.
    final.setRenderer(__import__('qgis.core',fromlist=['QgsSingleSymbolRenderer']).QgsSingleSymbolRenderer(
        QgsMarkerSymbol.createSimple({'color':'#267568','outline_color':'#163d35','size':'2.5'})))
    method_label.setText('Klassifizierung wählen und begründen')
    legend.model().refreshLayerLegend(root.findLayer(final.id()));layout.refresh()
    project.setFileName(str(out/'unit14_start.qgz'));assert project.write()
    template_context=QgsReadWriteContext()
    template_context.setPathResolver(QgsPathResolver(str(out/'vorlagen/abschlusskarte.qpt')))
    assert layout.saveAsTemplate(str(out/'vorlagen/abschlusskarte.qpt'),template_context)
    # The snapshot is intentionally dated; hashes identify its exact input files.
    report['source_sha256']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in
        [src/'gbif.json',src/'nsg.geojson',src/'ffh.geojson',src/'gewaesser.geojson',src/'dgm_marburg.zip']}
    template_dir=Path(__file__).resolve().parent/'templates'
    for name in ['quellen.md','processing_notes.md','pruefwerte.md']:
        shutil.copyfile(template_dir/name,out/'documentation'/name)
    shutil.copyfile(template_dir/'README.md',out/'README.md')
    shutil.copyfile(Path(__file__).resolve().parent/'sources.json',out/'documentation/sources.json')
    (out/'documentation/pruefbericht.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ['height_samples','source_sha256']},indent=2,ensure_ascii=False))


if __name__ == '__main__':
    from qgis.core import QgsLayoutItemPage,QgsLegendStyle
    main()
