from PyQt5 import QtWidgets, QtGui, QtCore
from program.view import Ui_MainWindow
from program.hsvmanipulation.controller import hsvselector
from program.rgbmanipulation.controller import rgbselector
from cv2 import merge, cvtColor, COLOR_RGB2GRAY, COLOR_RGB2HSV, inRange, imshow
from numpy import fromstring, clip, uint8, array
from program.cropimage.controller import cropImage

class controlleraplikasi(Ui_MainWindow, QtWidgets.QMainWindow, rgbselector, hsvselector):
    def __init__(self):
        super(controlleraplikasi, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.setImage) #Load
        self.pushButton_2.clicked.connect(self.convert) #Convert
        self.actionExit.triggered.connect(self.Exit)
        self.pushButton_4.clicked.connect(self.openWindow)
        self.pushButton_3.clicked.connect(self.clearLabel)
        self.setupRGB(self)
        self.setupHSV(self)

    def clearLabel(self):
            self.label.clear()
            self.label_5.clear()
            self.label_30.clear()
            self.label_2.clear()
            self.label_31.clear()
            
    def openWindow(self):
        self.ui = cropImage()
        try:
            self.ui.gambarCrop.setPixmap(self.label.pixmap())
            self.ui.gambar.setPixmap(self.label.pixmap())
        except TypeError:
            pass
        self.ui.show()
        if self.ui.exec_() == self.ui.Accepted:
            name = self.ui.get_output()
            self.label_31.setPixmap(QtGui.QPixmap.fromImage(name))
            self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        
    def setImage(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if fileName:
            pixmap = QtGui.QPixmap(fileName)
            self.label.setPixmap(pixmap)
            self.label.setAlignment(QtCore.Qt.AlignCenter)
            self.label_5.setPixmap(pixmap)
            self.label_5.setAlignment(QtCore.Qt.AlignCenter)
            self.label_30.setPixmap(pixmap)
            self.label_30.setAlignment(QtCore.Qt.AlignCenter)
            self.label_2.clear()

    def Exit(self):
        exit()
            
    def convert(self):
        try:
            loadgambar = self.label.pixmap()
            gambar = loadgambar.toImage()
            gambar = gambar.convertToFormat(4)
            s = gambar.bits().asstring(gambar.width() * gambar.height() * 4)
            arr = fromstring(s, dtype=uint8).reshape((gambar.height(), gambar.width(), 4))
            arr = cvtColor(arr, COLOR_RGB2GRAY)
            gambar3 = QtGui.QImage(arr.data, arr.shape[1], arr.shape[0], QtGui.QImage.Format_Indexed8)
            
            self.label_2.setPixmap(QtGui.QPixmap.fromImage(gambar3))
            self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        except AttributeError:
            pass


