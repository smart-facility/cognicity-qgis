from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *

QgsApplication.setPrefixPath("/Applications/MacPorts//QGIS.app/Contents/MacOS", True)

# initialise Qt resources from file resources.py
import resources

class cognicity:
  def __init__(self, iface):
    # save reference to QGIS interface
    self.iface = iface

  def initGui(self):
    # create action to start plugin configuration
    self.action = QAction(QIcon(":/plugins/cognicity-qgis/icon.png"), "Download Data", self.iface.mainWindow())
    self.action.setObjectName("testAction")
    self.action.setWhatsThis("Config")
    self.action.setStatusTip("CogniCity - Download Data")
    self.action.setToolTip('CogniCity - Download Data')
    QObject.connect(self.action, SIGNAL("triggered()"), self.run)

    # add toolbar button and menu item
    self.iface.addToolBarIcon(self.action)
    self.iface.addPluginToMenu("&CogniCity", self.action)


    # connect to signal renderComplete
    QObject.connect(self.iface.mapCanvas(), SIGNAL("renderComplete(QPainter *)"), self.renderCogniCity)

  def unload(self):
    # remove the plugin menu item and icon
    self.iface.removePluginMenu("&CogniCity", self.action)
    self.iface.removeToolBarIcon(self.action)

    # disconnect from canvas
    QObject.disconnect(self.iface.mapCanvas(), SIGNAL("renderComplete(QPainter *)"), self.renderCogniCity)

  def run(self):
    # create and show dialog
    print "CogniCity: run called"

  def renderCogniCity(self, painter):
    # use painter for drawing on map canvas
    print "CogniCity: renderTest called"
