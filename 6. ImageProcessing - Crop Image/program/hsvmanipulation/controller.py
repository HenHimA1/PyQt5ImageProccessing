from PyQt5 import QtGui, QtCore
from cv2 import merge, cvtColor, inRange, COLOR_RGB2HSV
from numpy import fromstring, uint8, array

class hsvselector(object):
    def setupHSV(self, MainWindow):
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
            lower = array([int(self.label_18.text()),int(self.label_20.text()),int(self.label_22.text())])
            upper = array([int(self.label_24.text()),int(self.label_26.text()),int(self.label_28.text())])
            arr = cvtColor(arr, COLOR_RGB2HSV)
            arr = inRange(arr, lower, upper)
            arr = merge([arr,arr,arr,arr])
            hasil = QtGui.QImage(arr.data, arr.shape[1], arr.shape[0], QtGui.QImage.Format_RGB32).rgbSwapped().rgbSwapped()
            self.label_30.setPixmap(QtGui.QPixmap.fromImage(hasil))
            self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        except AttributeError:
            pass        

        