from PyQt5 import QtWidgets
from program.view import Ui_MainWindow
from program.controller import controlleraplikasi
import sys


app = QtWidgets.QApplication(sys.argv)
ui = controlleraplikasi()
ui.show()
sys.exit(app.exec_())