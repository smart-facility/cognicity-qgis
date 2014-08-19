from PyQt4 import QtCore, QtGui
from ui_data import Ui_datadownload
# create the dialog for zoom to point


class data_dock(QtGui.QDockWidget, Ui_datadownload):
    def __init__(self, iface):
        QtGui.QDockWidget.__init__(self, iface.mainWindow())

        # Set up the user interface
        self.setupUi(self)
        self.setObjectName("data_dock") # used by main window to save/restore state
        self.iface = iface
        QtCore.QObject.connect(self.btn_download,QtCore.SIGNAL("pressed()"),self.handleButton)

    def handleButton(self):
      QMessafeBox.alert(self, 'go')

    def closeEvent(self, event):

        print 'here...'
        self.emit(QtCore.SIGNAL('closed'), "Hello World")
