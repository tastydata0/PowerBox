import sys
from PySide2 import QtCore, QtGui, QtWidgets
from powerline import Ui_Form


def init():
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
