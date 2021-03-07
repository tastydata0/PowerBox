# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Alex\Documents\powerbox.ui',
# licensing of 'C:\Users\Alex\Documents\powerbox.ui' applies.
#
# Created: Wed Jun 12 17:08:56 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import speech_recognition as sr
import os


pause = False
assets_path = os.path.realpath(__file__).replace("ui.py", "/assets/")

class Ui_Dialog(object):


    def clear_log_button_clicked(self):
        self.textEdit.clear()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def set_pause_state(self, new_statement):
        global pause
        icon3 = QtGui.QIcon()

        if( new_statement):
            icon3.addPixmap(QtGui.QPixmap(assets_path + "run.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        else:
            icon3.addPixmap(QtGui.QPixmap(assets_path + "pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setIconSize(QtCore.QSize(48, 48))

        pause = new_statement
        self.core_set_property( 'pause', new_statement )

    def pause_toggle(self,x):
        global pause

        self.set_pause_state(not pause)

    def line_hotkeys_toggle(self):

        self.core_set_property( 'line_hotkeys_enabled', self.checkBox.isChecked() )

    def change_volume(self,x):
        global volume

        volume = x
        self.label_8.setText( 'Громкость ( {0} )'.format(volume) )
        self.core_set_property( 'volume', volume )

    def change_city(self,x):
        global city

        city = x
        if(self.core_city_is_avaliable(city)):
            self.label_5.setPixmap(QtGui.QPixmap(assets_path + "right.png"))
        else:
            self.label_5.setPixmap(None)

        self.core_set_property( 'city', city )


    def add_notification( self, time, message ):
        self.listWidget.addItem( "[ {0} ] - {1}".format(time, message) )


    def append_log( self, message ):
        self.textEdit.append(message)


    def setupUi( self, Dialog, core_set_property, core_city_is_avaliable ):
        global assets_path

        self.core_set_property = core_set_property
        self.core_city_is_avaliable = core_city_is_avaliable
        Dialog.setObjectName( "Dialog" )
        Dialog.resize(560, 530)
        Dialog.setMinimumSize(QtCore.QSize(560, 530))
        Dialog.setMaximumSize(QtCore.QSize(560, 530))
        font = QtGui.QFont()
        font.setPointSize(8)
        Dialog.setFont(font)
        Dialog.setMouseTracking(False)
        Dialog.setTabletTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(assets_path + "powerbox.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setWindowOpacity(1.0)
        Dialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        Dialog.setStyleSheet("QDialog {\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(211, 236, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: none;\n"
"    background:transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background:rgb(212, 212, 212)\n"
"}\n"
"QPushButton:pressed {\n"
"    background:rgb(195, 195, 195)\n"
"}\n"
"QTableWidget {\n"
"    border: none;\n"
"}\n"
"QScrollArea {\n"
"    background:white;\n"
"    color:white;\n"
"    background-color:white;\n"
"}")
        Dialog.setModal(True)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(30, 150, 500, 340))
        self.tabWidget.setObjectName("tabWidget")
        self.functions = QtWidgets.QWidget()
        self.functions.setObjectName("functions")
        self.tableWidget = QtWidgets.QTableWidget(self.functions)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 491, 318))
        self.tableWidget.setMinimumSize(QtCore.QSize(491, 311))
        self.tableWidget.setMaximumSize(QtCore.QSize(491, 16777215))
        self.tableWidget.setMouseTracking(True)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setProperty("showDropIndicator", True)
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideRight)
        self.tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.DashLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(15)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(15)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(10, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(11, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(12, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(13, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(14, 0, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(50)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(50)
        self.tableWidget.verticalHeader().setSortIndicatorShown(True)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        self.tabWidget.addTab(self.functions, "")
        self.log = QtWidgets.QWidget()
        self.log.setObjectName("log")
        self.textEdit = QtWidgets.QTextEdit(self.log)
        self.textEdit.setGeometry(QtCore.QRect(10, 8, 451, 311))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setWeight(40)
        #font.setBold(True)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("QTextEdit {\n"
"    border: none;\n"
"}")
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.log)
        self.pushButton.setGeometry(QtCore.QRect(462, 0, 32, 32))
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(assets_path + "delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(20, 20))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.clear_log_button_clicked)
        self.tabWidget.addTab(self.log, "")
        self.settings = QtWidgets.QWidget()
        self.settings.setObjectName("settings")
        self.groupBox = QtWidgets.QGroupBox(self.settings)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 221, 61))
        self.groupBox.setObjectName("groupBox")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(10, 22, 201, 22))
        for index, name in enumerate(sr.Microphone.list_microphone_names()):
                    self.comboBox.addItem(name)
        self.comboBox.setObjectName("comboBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.settings)
        self.groupBox_2.setGeometry(QtCore.QRect(240, 75, 221, 61))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 22, 91, 16))
        self.label_4.setObjectName("label_4")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox.setGeometry(QtCore.QRect(130, 22, 70, 17))
        self.checkBox.setChecked(True)
        self.checkBox.setTristate(False)
        self.checkBox.setObjectName("checkBox")
        self.checkBox.stateChanged.connect(self.line_hotkeys_toggle)
        self.groupBox_3 = QtWidgets.QGroupBox(self.settings)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 75, 221, 61))
        self.groupBox_3.setObjectName("groupBox_3")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit.setGeometry(QtCore.QRect(10, 22, 169, 22))
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setObjectName("lineEdit")
        #self.lineEdit.installEventFilter(self)
        self.lineEdit.textEdited.connect(self.change_city)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(183, 17, 31, 31))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(assets_path + "right.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")


        #self.label_6 = QtWidgets.QLabel(Dialog)
        #self.label_6.setGeometry(QtCore.QRect(0, -40, 791, 611))
        #self.label_6.setText("")
        #self.label_6.setPixmap(QtGui.QPixmap(":/bg/image036.png"))
        #self.label_6.setScaledContents(True)
        #self.label_6.setObjectName("label_6")


        self.label_7 = QtWidgets.QLabel(self.settings)
        self.label_7.setGeometry(QtCore.QRect(0, 120, 501, 261))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(assets_path + "ffbg.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")

        self.horizontalSlider = QtWidgets.QSlider(Dialog)
        self.horizontalSlider.setGeometry(QtCore.QRect(340, 130, 160, 22))
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setProperty("value", 90)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.valueChanged.connect(self.change_volume)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(340, 110, 101, 16))
        self.label_8.setObjectName("label_8")

        self.groupBox_4 = QtWidgets.QGroupBox(self.settings)
        self.groupBox_4.setGeometry(QtCore.QRect(240, 10, 221, 61))
        self.groupBox_4.setObjectName("groupBox_4")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_2.setGeometry(QtCore.QRect(10, 22, 201, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.tabWidget.addTab(self.settings, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.listWidget = QtWidgets.QListWidget(self.tab)
        self.listWidget.setGeometry(QtCore.QRect(-1, -1, 496, 316))
        self.listWidget.setObjectName("listWidget")
        self.tabWidget.addTab(self.tab, "")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 109, 109))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(assets_path + "powerboxBright.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(170, 20, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(171, 60, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setWeight(75)
        font.setItalic(False)
        font.setUnderline(False)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel {\n"
"    color: rgb(38, 96, 140);\n"
"}")
        self.label_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_3.setScaledContents(False)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")

        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setWeight(75)
        font.setUnderline(False)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel {\n"
"    color: rgb(38, 96, 140);\n"
"}")
        self.label_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_3.setScaledContents(False)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 40, 60, 60))
        self.pushButton_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(assets_path + "pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.pause_toggle)




#-------------\



#--------------/
        self.retranslateUi(Dialog)
        self.comboBox.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Dialog", None, -1))
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.verticalHeaderItem(0).setText(QtWidgets.QApplication.translate("Dialog", "Время", None, -1))
        self.tableWidget.verticalHeaderItem(1).setText(QtWidgets.QApplication.translate("Dialog", "Погода", None, -1))
        self.tableWidget.verticalHeaderItem(2).setText(QtWidgets.QApplication.translate("Dialog", "Открытие строки", None, -1))
        self.tableWidget.verticalHeaderItem(3).setText(QtWidgets.QApplication.translate("Dialog", "Выход из сеанса (Win + L)", None, -1))
        self.tableWidget.verticalHeaderItem(4).setText(QtWidgets.QApplication.translate("Dialog", "Копирование сказанного", None, -1))
        self.tableWidget.verticalHeaderItem(5).setText(QtWidgets.QApplication.translate("Dialog", "Завершение работы", None, -1))
        self.tableWidget.verticalHeaderItem(6).setText(QtWidgets.QApplication.translate("Dialog", "Отмена завершения работы", None, -1))
        self.tableWidget.verticalHeaderItem(7).setText(QtWidgets.QApplication.translate("Dialog", "Перезагрузка", None, -1))
        self.tableWidget.verticalHeaderItem(8).setText(QtWidgets.QApplication.translate("Dialog", "Отмена перезагрузки", None, -1))
        self.tableWidget.verticalHeaderItem(9).setText(QtWidgets.QApplication.translate("Dialog", "Напоминание", None, -1))
        self.tableWidget.verticalHeaderItem(10).setText(QtWidgets.QApplication.translate("Dialog", "Удаление всех напоминаний", None, -1))
        self.tableWidget.verticalHeaderItem(11).setText(QtWidgets.QApplication.translate("Dialog", "Математ. операции", None, -1))
        self.tableWidget.verticalHeaderItem(12).setText(QtWidgets.QApplication.translate("Dialog", "Написание текста", None, -1))
        self.tableWidget.verticalHeaderItem(13).setText(QtWidgets.QApplication.translate("Dialog", "Поиск в Интернете", None, -1))
        self.tableWidget.verticalHeaderItem(14).setText(QtWidgets.QApplication.translate("Dialog", "Объяснение слова / термина", None, -1))
        self.tableWidget.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("Dialog", "Ключевые фразы", None, -1))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.item(0, 0).setText(QtWidgets.QApplication.translate("Dialog", "сколько времени, текущее время, который час", None, -1))
        self.tableWidget.item(1, 0).setText(QtWidgets.QApplication.translate("Dialog", "какая погода, погода на сегодня", None, -1))
        self.tableWidget.item(2, 0).setText(QtWidgets.QApplication.translate("Dialog", "открыть строку, открыть поиск", None, -1))
        self.tableWidget.item(3, 0).setText(QtWidgets.QApplication.translate("Dialog", "заблокировать, выйти из сеанса", None, -1))
        self.tableWidget.item(4, 0).setText(QtWidgets.QApplication.translate("Dialog", "скопировать <слова для копирования>", None, -1))
        self.tableWidget.item(5, 0).setText(QtWidgets.QApplication.translate("Dialog", "завершение работы, выключить компьютер", None, -1))
        self.tableWidget.item(6, 0).setText(QtWidgets.QApplication.translate("Dialog", "отмена завершения работы, отмена, не выключать компьютер", None, -1))
        self.tableWidget.item(7, 0).setText(QtWidgets.QApplication.translate("Dialog", "перезагрузить, перезагрузка компьютера", None, -1))
        self.tableWidget.item(8, 0).setText(QtWidgets.QApplication.translate("Dialog", "отмена, не выключать компьютер", None, -1))
        self.tableWidget.item(9, 0).setText(QtWidgets.QApplication.translate("Dialog", "напомнить <напоминание> в <время>,                    создать напоминание <напоминание> в <время>", None, -1))
        self.tableWidget.item(10, 0).setText(QtWidgets.QApplication.translate("Dialog", "убрать напоминания, отменить напоминания", None, -1))
        self.tableWidget.item(11, 0).setText(QtWidgets.QApplication.translate("Dialog", "сколько будет <математ. выражение>, посчитай <математ. выражение>", None, -1))
        self.tableWidget.item(12, 0).setText(QtWidgets.QApplication.translate("Dialog", "напечатай <запрос>, напиши <запрос>, напечатать <запрос>, написать <запрос>", None, -1))
        self.tableWidget.item(13, 0).setText(QtWidgets.QApplication.translate("Dialog", "искать в браузере <запрос>, искать в интернете <запрос>, поиск в интернете <запрос>", None, -1))
        self.tableWidget.item(14, 0).setText(QtWidgets.QApplication.translate("Dialog", "что такое <запрос>, значение слова <запрос>, кто такой <запрос>", None, -1))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.functions), QtWidgets.QApplication.translate("Dialog", "Функции", None, -1))
        self.textEdit.setHtml(QtWidgets.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:15pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.log), QtWidgets.QApplication.translate("Dialog", "Лог", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("Dialog", "Устройство записи", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("Dialog", "Сочетание клавиш для вызова строки", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Dialog", "Shift + Пробел", None, -1))
        self.checkBox.setText(QtWidgets.QApplication.translate("Dialog", "Активно", None, -1))
        self.groupBox_3.setTitle(QtWidgets.QApplication.translate("Dialog", "Город ( для погоды )", None, -1))
        self.lineEdit.setText(QtWidgets.QApplication.translate("Dialog", "Симферополь", None, -1))
        self.groupBox_4.setTitle(QtWidgets.QApplication.translate("Dialog", "Голос", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings), QtWidgets.QApplication.translate("Dialog", "Настройки", None, -1))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtWidgets.QApplication.translate("Dialog", "Напоминания", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Dialog", "PowerBox", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Dialog", "Everything you need.", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("Dialog", "Громкость ( 90 )", None, -1))
