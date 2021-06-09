from PyQt5 import QtWidgets, QtGui, QtCore
from program.view import Ui_MainWindow
from cv2 import merge, cvtColor, COLOR_RGB2GRAY, COLOR_RGB2HSV, inRange
from numpy import fromstring, clip, uint8, array

class controlleraplikasi(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(controlleraplikasi, self).__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.setImage) #Load
        self.pushButton_2.clicked.connect(self.convert) #Convert
        self.horizontalSlider.valueChanged.connect(self.RGBManipulator) #Red
        self.horizontalSlider.setMaximum(255)
        self.horizontalSlider.setMinimum(-255)
        self.horizontalSlider_2.valueChanged.connect(self.RGBManipulator) #Green
        self.horizontalSlider_2.setMaximum(255)
        self.horizontalSlider_2.setMinimum(-255)
        self.horizontalSlider_3.valueChanged.connect(self.RGBManipulator) #Blue
        self.horizontalSlider_3.setMaximum(255)
        self.horizontalSlider_3.setMinimum(-255)
        self.horizontalSlider_5.valueChanged.connect(self.HSVManipulator) #L-H
        self.horizontalSlider_5.setMaximum(255)
        self.horizontalSlider_5.setMinimum(0)
        self.horizontalSlider_6.valueChanged.connect(self.HSVManipulator) #L-S
        self.horizontalSlider_6.setMaximum(255)
        self.horizontalSlider_6.setMinimum(0)
        self.horizontalSlider_7.valueChanged.connect(self.HSVManipulator) #L-V
        self.horizontalSlider_7.setMaximum(255)
        self.horizontalSlider_7.setMinimum(0)
        self.horizontalSlider_8.valueChanged.connect(self.HSVManipulator) #H-H
        self.horizontalSlider_8.setMaximum(255)
        self.horizontalSlider_8.setMinimum(0)
        self.horizontalSlider_9.valueChanged.connect(self.HSVManipulator) #H-S
        self.horizontalSlider_9.setMaximum(255)
        self.horizontalSlider_9.setMinimum(0)
        self.horizontalSlider_10.valueChanged.connect(self.HSVManipulator) #H-V
        self.horizontalSlider_10.setMaximum(255)
        self.horizontalSlider_10.setMinimum(0)
        

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

    def RGBManipulator(self,event):
        if self.sender() == self.horizontalSlider:
            self.red = event
            self.label_7.setNum(self.red)

        elif self.sender() == self.horizontalSlider_2:
            self.green = event
            self.label_8.setNum(self.green)

        elif self.sender() == self.horizontalSlider_3:
            self.blue = event
            self.label_9.setNum(self.blue)

        else:
            pass
        
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

    def HSVManipulator(self,event):
        if self.sender() == self.horizontalSlider_5:
            self.LoH = event
            self.label_18.setNum(self.LoH)

        elif self.sender() == self.horizontalSlider_6:
            self.LoS = event
            self.label_20.setNum(self.LoS)

        elif self.sender() == self.horizontalSlider_7:
            self.LoV = event
            self.label_22.setNum(self.LoV)

        elif self.sender() == self.horizontalSlider_8:
            self.HoH = event
            self.label_24.setNum(self.HoH)

        elif self.sender() == self.horizontalSlider_9:
            self.HoS = event
            self.label_26.setNum(self.HoS)

        elif self.sender() == self.horizontalSlider_10:
            self.HoV = event
            self.label_28.setNum(self.HoV)

        try:
            loadgambar = self.label.pixmap()
            gambar = loadgambar.toImage()
            gambar = gambar.convertToFormat(4)
            s = gambar.bits().asstring(gambar.width() * gambar.height() * 4)
            arr = fromstring(s, dtype=uint8).reshape((gambar.height(), gambar.width(), 4))
            lower_red = array([int(self.label_18.text()),int(self.label_20.text()),int(self.label_22.text())])
            upper_red = array([int(self.label_24.text()),int(self.label_26.text()),int(self.label_28.text())])
            arr = cvtColor(arr, COLOR_RGB2HSV)
            arr = inRange(arr, lower_red, upper_red)
            gambar3 = QtGui.QImage(arr.data, arr.shape[1], arr.shape[0], QtGui.QImage.Format_Indexed8)
            destroyAllWindows()
            self.label_30.setPixmap(QtGui.QPixmap.fromImage(gambar3))
            self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        except AttributeError:
            pass        

        