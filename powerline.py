# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Alex\Documents\powerline.ui',
# licensing of 'C:\Users\Alex\Documents\powerline.ui' applies.
#
# Created: Sat Jun  1 11:38:16 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import os

class Ui_Form(object):
    items_count = 0
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.ApplicationModal)
        Form.resize(521, 59)
        Form.setMouseTracking(False)
        Form.setFocusPolicy(QtCore.Qt.NoFocus)
        Form.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        Form.setAcceptDrops(False)
        Form.setWindowTitle("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("powerboxBright.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setWindowOpacity(1.0)
        Form.setToolTip("")
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("QWidget {\n"
"    background: white;    \n"
"}")
        Form.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(69, -11, 431, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(28)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{ \n"
"    border: none;\n"
"}")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 2, 51, 51))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background:rgb(247, 247, 247);\n"
"}\n"
"QPushButton:pressed {\n"
"    background:rgb(236, 236, 236);\n"
"}")
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/logo/powerboxBright.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(41, 41))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        pass

