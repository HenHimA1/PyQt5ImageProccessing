from PyQt5 import QtWidgets, QtGui, QtCore
from program.view import Ui_MainWindow
from cv2 import merge, cvtColor, COLOR_RGB2GRAY
from numpy import fromstring, clip, uint8

class controlleraplikasi(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(controlleraplikasi, self).__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.setImage) #Load
        self.pushButton_2.clicked.connect(self.convert) #Convert
        self.horizontalSlider.valueChanged.connect(self.enhanceImage) #Red
        self.horizontalSlider.setMaximum(255)
        self.horizontalSlider.setMinimum(-255)
        self.horizontalSlider_2.valueChanged.connect(self.enhanceImage) #Green
        self.horizontalSlider_2.setMaximum(255)
        self.horizontalSlider_2.setMinimum(-255)
        self.horizontalSlider_3.valueChanged.connect(self.enhanceImage) #Blue
        self.horizontalSlider_3.setMaximum(255)
        self.horizontalSlider_3.setMinimum(-255)


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

    def enhanceImage(self,event):
        if self.sender() == self.horizontalSlider:
            self.red = event
            self.label_7.setNum(self.red)

        elif self.sender() == self.horizontalSlider_2:
            self.green = event
            self.label_8.setNum(self.green)

        elif self.sender() == self.horizontalSlider_3:
            self.blue = event
            self.label_9.setNum(self.blue)
        
        try:
            loadgambar = self.label.pixmap()
            gambar = loadgambar.toImage()
            gambar = gambar.convertToFormat(4)
            s = gambar.bits().asstring(gambar.width() * gambar.height() * 4)
            arr = fromstring(s, dtype=uint8).reshape((gambar.height(), gambar.width(), 4))
            b = clip((arr[:,:,0]).astype('int32')+round(int(self.label_9.text())),0,255).astype('uint8')
            g = clip((arr[:,:,1]).astype('int32')+round(int(self.label_8.text())),0,255).astype('uint8')
            r = clip((arr[:,:,2]).astype('int32')+round(int(self.label_7.text())),0,255).astype('uint8')
            arr = merge([b,g,r,arr[:,:,3]])
            gambar3 = QtGui.QImage(arr.data, arr.shape[1], arr.shape[0], QtGui.QImage.Format_RGB32).rgbSwapped().rgbSwapped()
            self.label_5.setPixmap(QtGui.QPixmap.fromImage(gambar3))
            self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        except AttributeError:
            pass        

        