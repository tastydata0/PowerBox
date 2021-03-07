# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Alex\Documents\virusTotal.ui',
# licensing of 'C:\Users\Alex\Documents\virusTotal.ui' applies.
#
# Created: Thu Jun 27 21:19:07 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import os

assets_path = os.path.realpath(__file__).replace("virt_ui.py", "/assets/")

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.logo = QtWidgets.QLabel(Dialog)
        self.logo.setGeometry(QtCore.QRect(95, 20, 200, 44))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(assets_path + "vt_logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.square = QtWidgets.QLabel(Dialog)
        self.square.setGeometry(QtCore.QRect(100, 70, 191, 201))
        self.square.setText("")
        self.square.setPixmap(QtGui.QPixmap(assets_path + "vt_square.png"))
        self.square.setObjectName("square")
        self.scan = QtWidgets.QLabel(Dialog)
        self.scan.setGeometry(QtCore.QRect(130, 120, 140, 100))
        self.scan.setText("")
        self.scan.setPixmap(QtGui.QPixmap(assets_path + "vt_scan.png"))
        self.scan.setScaledContents(True)
        self.scan.setObjectName("scan")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Dialog", None, -1))
