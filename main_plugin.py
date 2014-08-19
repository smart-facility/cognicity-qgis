from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from data_dock import data_dock

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

  def unload(self):
    # remove the plugin menu item and icon
    self.iface.removePluginMenu("&CogniCity", self.action)
    self.iface.removeToolBarIcon(self.action)

  def run(self):
    # create and show dock widget
    self.dock_window = datadownloadDialog(self)
    self.iface.mainWindow().addDockWidget(Qt.RightDockWidgetArea, self.dock_window)
