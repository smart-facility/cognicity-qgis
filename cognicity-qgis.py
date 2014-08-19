#!/opt/local/bin/python

# cognicity-qgis.py
# QGIS plugin to connect to cognicity data API instance.

from qgis.core import *
import qgis.utils

QgsApplication.setPrefixPath("/Applications/MacPorts//QGIS.app/Contents/MacOS", True)
QgsApplication.initQgis()

layer = QgsVectorLayer('http://petajakarta.org/banjir/data/api/v1/aggregates/live', 'l1','ogr');
if not layer.isValid():
  print 'Layer failed to load'


error = QgsVectorFileWriter.writeAsVectorFormat(layer, '/tmp/data1.geojson', 'utf-8', None, "GeoJSON");

if error == QgsVectorFileWriter.NoError:
  print 'Success!'

# Connect to API end point
# Select data to download (drop down list)
# Select time period (greyed out if live)
# Select download DIR
# Select download format
# Add layers to map?
# Info bar - expected number of downloads, downloading 1 of 6, converting
