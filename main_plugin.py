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
    self.dock = None

  def initGui(self):
    # create action to start plugin configuration
    self.action = QAction(QIcon(":/plugins/cognicity-qgis/icon.png"), "Download Data", self.iface.mainWindow())
    self.action.setObjectName("testAction")
    self.action.setWhatsThis("Config")
    self.action.setStatusTip("CogniCity - Download Data")
    self.action.setToolTip('CogniCity - Download Data')
    self.action.setCheckable(True)
    QObject.connect(self.action, SIGNAL("triggered(bool)"), self.toggleDock)

    # add toolbar button and menu item
    self.iface.addToolBarIcon(self.action)
    self.iface.addPluginToMenu("&CogniCity", self.action)

    # add the datadock
    self.dock = data_dock(self.iface)
    self.iface.mainWindow().addDockWidget(Qt.RightDockWidgetArea, self.dock)
    self.dock.hide()

    # listen for change events if users closes window
    QObject.connect(self.dock, SIGNAL("closed"), self.closeDock)

  #def closeEvent(self, event):
  #  print 'closed'

  def unload(self):
    # remove the plugin menu item and icon
    self.iface.removePluginMenu("&CogniCity", self.action)
    self.iface.removeToolBarIcon(self.action)

  def toggleDock(self, checked):
    # show dock widget
    if checked == True:
      self.dock.show()
    else:
      self.dock.hide()

  def closeDock(self):
    # dock closed independantly of menu/buttons
      print 'caught!'
      self.dock.hide()
      self.action.setChecked(False)
