# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_data.ui'
#
# Created: Tue Aug 19 16:45:10 2014
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
        datadownload.resize(301, 479)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.tabWidget = QtGui.QTabWidget(self.dockWidgetContents)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 281, 432))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_download = QtGui.QWidget()
        self.tab_download.setObjectName(_fromUtf8("tab_download"))
        self.comboBox_layers = QtGui.QComboBox(self.tab_download)
        self.comboBox_layers.setGeometry(QtCore.QRect(10, 20, 251, 26))
        self.comboBox_layers.setObjectName(_fromUtf8("comboBox_layers"))
        self.label_datalayer = QtGui.QLabel(self.tab_download)
        self.label_datalayer.setGeometry(QtCore.QRect(10, 0, 71, 16))
        self.label_datalayer.setObjectName(_fromUtf8("label_datalayer"))
        self.label_startdate = QtGui.QLabel(self.tab_download)
        self.label_startdate.setGeometry(QtCore.QRect(10, 60, 121, 16))
        self.label_startdate.setObjectName(_fromUtf8("label_startdate"))
        self.dateEdit_start = QtGui.QDateEdit(self.tab_download)
        self.dateEdit_start.setGeometry(QtCore.QRect(10, 80, 111, 31))
        self.dateEdit_start.setObjectName(_fromUtf8("dateEdit_start"))
        self.btn_download = QtGui.QPushButton(self.tab_download)
        self.btn_download.setGeometry(QtCore.QRect(0, 370, 114, 32))
        self.btn_download.setObjectName(_fromUtf8("btn_download"))
        self.label_startime = QtGui.QLabel(self.tab_download)
        self.label_startime.setGeometry(QtCore.QRect(140, 60, 121, 16))
        self.label_startime.setObjectName(_fromUtf8("label_startime"))
        self.label_enddate = QtGui.QLabel(self.tab_download)
        self.label_enddate.setGeometry(QtCore.QRect(10, 120, 121, 16))
        self.label_enddate.setObjectName(_fromUtf8("label_enddate"))
        self.dateEdit_end = QtGui.QDateEdit(self.tab_download)
        self.dateEdit_end.setGeometry(QtCore.QRect(10, 140, 111, 31))
        self.dateEdit_end.setObjectName(_fromUtf8("dateEdit_end"))
        self.label_endtime = QtGui.QLabel(self.tab_download)
        self.label_endtime.setGeometry(QtCore.QRect(140, 120, 121, 16))
        self.label_endtime.setObjectName(_fromUtf8("label_endtime"))
        self.btn_exit = QtGui.QPushButton(self.tab_download)
        self.btn_exit.setGeometry(QtCore.QRect(110, 370, 114, 32))
        self.btn_exit.setObjectName(_fromUtf8("btn_exit"))
        self.line = QtGui.QFrame(self.tab_download)
        self.line.setGeometry(QtCore.QRect(10, 220, 251, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_format = QtGui.QLabel(self.tab_download)
        self.label_format.setGeometry(QtCore.QRect(10, 240, 81, 16))
        self.label_format.setObjectName(_fromUtf8("label_format"))
        self.comboBox_format = QtGui.QComboBox(self.tab_download)
        self.comboBox_format.setGeometry(QtCore.QRect(10, 260, 251, 26))
        self.comboBox_format.setObjectName(_fromUtf8("comboBox_format"))
        self.lcdNumber_numfiles = QtGui.QLCDNumber(self.tab_download)
        self.lcdNumber_numfiles.setGeometry(QtCore.QRect(10, 200, 101, 20))
        self.lcdNumber_numfiles.setProperty("intValue", 0)
        self.lcdNumber_numfiles.setObjectName(_fromUtf8("lcdNumber_numfiles"))
        self.label_numfiles = QtGui.QLabel(self.tab_download)
        self.label_numfiles.setGeometry(QtCore.QRect(10, 180, 261, 16))
        self.label_numfiles.setObjectName(_fromUtf8("label_numfiles"))
        self.lineEdit_downloaddir = QtGui.QLineEdit(self.tab_download)
        self.lineEdit_downloaddir.setGeometry(QtCore.QRect(13, 310, 193, 21))
        self.lineEdit_downloaddir.setObjectName(_fromUtf8("lineEdit_downloaddir"))
        self.label_downloaddir = QtGui.QLabel(self.tab_download)
        self.label_downloaddir.setGeometry(QtCore.QRect(10, 290, 131, 16))
        self.label_downloaddir.setObjectName(_fromUtf8("label_downloaddir"))
        self.btn_opendir = QtGui.QPushButton(self.tab_download)
        self.btn_opendir.setGeometry(QtCore.QRect(204, 305, 61, 32))
        self.btn_opendir.setObjectName(_fromUtf8("btn_opendir"))
        self.checkBox_addlayers = QtGui.QCheckBox(self.tab_download)
        self.checkBox_addlayers.setGeometry(QtCore.QRect(11, 343, 143, 20))
        self.checkBox_addlayers.setObjectName(_fromUtf8("checkBox_addlayers"))
        self.comboBox_starttime = QtGui.QComboBox(self.tab_download)
        self.comboBox_starttime.setGeometry(QtCore.QRect(140, 83, 119, 26))
        self.comboBox_starttime.setObjectName(_fromUtf8("comboBox_starttime"))
        self.comboBox_endtime = QtGui.QComboBox(self.tab_download)
        self.comboBox_endtime.setGeometry(QtCore.QRect(140, 144, 119, 26))
        self.comboBox_endtime.setObjectName(_fromUtf8("comboBox_endtime"))
        self.tabWidget.addTab(self.tab_download, _fromUtf8(""))
        self.tab_options = QtGui.QWidget()
        self.tab_options.setObjectName(_fromUtf8("tab_options"))
        self.label1_api = QtGui.QLabel(self.tab_options)
        self.label1_api.setGeometry(QtCore.QRect(10, 0, 181, 16))
        self.label1_api.setObjectName(_fromUtf8("label1_api"))
        self.lineEdit_api = QtGui.QLineEdit(self.tab_options)
        self.lineEdit_api.setGeometry(QtCore.QRect(10, 20, 251, 21))
        self.lineEdit_api.setPlaceholderText(_fromUtf8(""))
        self.lineEdit_api.setObjectName(_fromUtf8("lineEdit_api"))
        self.checkBox_geojson = QtGui.QCheckBox(self.tab_options)
        self.checkBox_geojson.setEnabled(False)
        self.checkBox_geojson.setGeometry(QtCore.QRect(10, 50, 241, 20))
        self.checkBox_geojson.setChecked(True)
        self.checkBox_geojson.setObjectName(_fromUtf8("checkBox_geojson"))
        self.tabWidget.addTab(self.tab_options, _fromUtf8(""))
        datadownload.setWidget(self.dockWidgetContents)

        self.retranslateUi(datadownload)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(datadownload)

    def retranslateUi(self, datadownload):
        datadownload.setWindowTitle(_translate("datadownload", "CogniCity - Data Download", None))
        self.comboBox_layers.setToolTip(_translate("datadownload", "Required layer to download", None))
        self.label_datalayer.setText(_translate("datadownload", "Data Layer", None))
        self.label_startdate.setText(_translate("datadownload", "Start Date", None))
        self.btn_download.setText(_translate("datadownload", "Download", None))
        self.label_startime.setText(_translate("datadownload", "Start Time", None))
        self.label_enddate.setText(_translate("datadownload", "End Date", None))
        self.label_endtime.setText(_translate("datadownload", "End Time", None))
        self.btn_exit.setText(_translate("datadownload", "Exit", None))
        self.label_format.setText(_translate("datadownload", "File Format", None))
        self.comboBox_format.setToolTip(_translate("datadownload", "Required layer to download", None))
        self.label_numfiles.setText(_translate("datadownload", "Estimated number of files to download", None))
        self.label_downloaddir.setText(_translate("datadownload", "Download Directory", None))
        self.btn_opendir.setText(_translate("datadownload", "Open", None))
        self.checkBox_addlayers.setText(_translate("datadownload", "Add layers to QGIS", None))
        self.comboBox_starttime.setToolTip(_translate("datadownload", "Required layer to download", None))
        self.comboBox_endtime.setToolTip(_translate("datadownload", "Required layer to download", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_download), _translate("datadownload", "Download", None))
        self.label1_api.setText(_translate("datadownload", "CogniCity Data API Location", None))
        self.lineEdit_api.setText(_translate("datadownload", "http://petajakarta.org/banjir/data/api/v1/", None))
        self.checkBox_geojson.setText(_translate("datadownload", "Use GeoJSON format for transfer", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_options), _translate("datadownload", "Options", None))

