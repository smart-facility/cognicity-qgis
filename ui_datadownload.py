# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_datadownload.ui'
#
# Created: Tue Aug 19 15:38:59 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_datadownload(object):
    def setupUi(self, datadownload):
        datadownload.setObjectName(_fromUtf8("datadownload"))
        datadownload.resize(400, 300)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.btnGo = QtGui.QPushButton(self.dockWidgetContents)
        self.btnGo.setGeometry(QtCore.QRect(150, 110, 114, 32))
        self.btnGo.setObjectName(_fromUtf8("btnGo"))
        datadownload.setWidget(self.dockWidgetContents)

        self.retranslateUi(datadownload)
        QtCore.QMetaObject.connectSlotsByName(datadownload)

    def retranslateUi(self, datadownload):
        datadownload.setWindowTitle(_translate("datadownload", "CogniCity - Data Download", None))
        self.btnGo.setText(_translate("datadownload", "PushButton", None))

