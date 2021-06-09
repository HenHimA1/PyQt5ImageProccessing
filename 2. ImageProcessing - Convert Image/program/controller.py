from PyQt5 import QtWidgets, QtGui, QtCore
from program.view import Ui_MainWindow
from cv2 import COLOR_RGB2GRAY, cvtColor, merge
from numpy import fromstring, uint8

class controlleraplikasi(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(controlleraplikasi, self).__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.setImage) #Load
        self.pushButton_2.clicked.connect(self.convert) #Convert

    def setImage(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if fileName:
            pixmap = QtGui.QPixmap(fileName)
            self.label.setPixmap(pixmap)
            self.label.setAlignment(QtCore.Qt.AlignCenter)
            self.label_2.clear()
            

    def convert(self):
        try:
            loadgambar = self.label.pixmap()
            gambar = loadgambar.toImage()
            gambar = gambar.convertToFormat(4)
            s = gambar.bits().asstring(gambar.width() * gambar.height() * 4)
            arr = fromstring(s, dtype=uint8).reshape((gambar.height(), gambar.width(), 4))
            arr = cvtColor(arr, COLOR_RGB2GRAY)
            arr = merge([arr,arr,arr,arr])
            gambar3 = QtGui.QImage(arr.data, arr.shape[1], arr.shape[0], QtGui.QImage.Format_RGB32).rgbSwapped().rgbSwapped()
            
            self.label_2.setPixmap(QtGui.QPixmap.fromImage(gambar3))
            self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        except AttributeError:
            pass