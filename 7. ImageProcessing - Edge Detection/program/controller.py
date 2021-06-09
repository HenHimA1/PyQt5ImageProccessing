from PyQt5 import QtWidgets, QtGui, QtCore
from program.view import Ui_MainWindow
from program.hsvmanipulation.controller import hsvselector
from program.rgbmanipulation.controller import rgbselector
from program.menubar.controller import menuBar
from program.cropimage.controller import cropImage
from program.edgedetection.controller import edgeDetection
from cv2 import merge, cvtColor, COLOR_RGB2GRAY, COLOR_RGB2HSV, inRange
from numpy import fromstring, clip, uint8, array

class controlleraplikasi(Ui_MainWindow, QtWidgets.QMainWindow, rgbselector, hsvselector, menuBar):
    def __init__(self):
        super(controlleraplikasi, self).__init__()
        self.frame = QtWidgets.QFrame()
        self.setWindowIcon(QtGui.QIcon('program/icon/original.png'))
        self.setupUi(self)
        self.pushButton.clicked.connect(self.setImage) #Load
        self.pushButton_2.clicked.connect(self.convert) #Convert
        self.pushButton_4.clicked.connect(self.CropImage) #Crop Image
        self.pushButton_3.clicked.connect(self.clearLabel)  #Clear
        self.pushButton_5.clicked.connect(self.EdgeDetection) #Edge Detection
        self.setupRGB(self)
        self.setupHSV(self)
        self.setupMenuBar(self)
        
    def clearLabel(self):
            self.label.clear()
            self.label_5.clear()
            self.label_30.clear()
            self.label_2.clear()
            self.label_31.clear()
        
            
    def CropImage(self):
        self.CI = cropImage()
        try:
            self.CI.gambarCrop.setPixmap(self.label.pixmap())
            self.CI.gambar.setPixmap(self.label.pixmap())
        except TypeError:
            pass
        self.CI.show()
        if self.CI.exec_() == self.CI.Accepted:
            name = self.CI.get_output()
            self.label_31.setPixmap(QtGui.QPixmap.fromImage(name))
            self.label_31.setAlignment(QtCore.Qt.AlignCenter)

    def EdgeDetection(self):
        self.ui = edgeDetection()
        try:
            self.ui.label.setPixmap(self.label.pixmap())
            self.ui.label_2.setPixmap(self.label.pixmap())
        except TypeError:
            pass
        self.ui.show()
        
    def setImage(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if fileName:
            pixmap = QtGui.QPixmap(fileName)
            self.label.setPixmap(pixmap)
            self.label.setAlignment(QtCore.Qt.AlignCenter)
            self.RGBManipulator(self)
            self.awalHSVManipulator(self)
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


