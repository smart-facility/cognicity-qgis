from PyQt4 import QtCore, QtGui
from ui_data import Ui_datadownload
# create the dialog for zoom to point


class data_dock(QtGui.QDockWidget, Ui_datadownload):
    def __init__(self, parent):
        QtGui.QDockWidget.__init__(self, parent.iface.mainWindow())

        # Set up the user interface
        self.setupUi(self)

        QtCore.QObject.connect(self.btnGo,QtCore.SIGNAL("pressed()"),self.handleButton)

    def handleButton(self):
      msgBox.setWindowTitle('go!');
