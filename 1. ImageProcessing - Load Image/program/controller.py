from PyQt5 import QtWidgets, QtGui, QtCore
from program.view import Ui_MainWindow

class controlleraplikasi(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(controlleraplikasi, self).__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.setImage) #Load


    def setImage(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if fileName:
            pixmap = QtGui.QPixmap(fileName)
            self.label.setPixmap(pixmap)
            self.label.setAlignment(QtCore.Qt.AlignCenter)