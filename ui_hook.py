from PySide2 import QtCore, QtGui, QtWidgets
from ui import Ui_Dialog
import sys
import numpy

ui = None
Dialog = None
app = None


def pre_init( core_set_property, core_city_is_avaliable ):
    global ui
    global app
    global Dialog

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog, core_set_property, core_city_is_avaliable )


def update_notifications(database_path):
    dict = numpy.load( database_path + ".npy", allow_pickle=True ).item()
    for i in dict.items():
        add_notification(i[0],i[1])

def add_notification(time, message):
    ui.add_notification(time,message)



def init():
    Dialog.show()
    app.exec_()


def append_log(message):
    ui.append_log(message)
