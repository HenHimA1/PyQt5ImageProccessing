from PyQt5 import QtGui, QtCore
from cv2 import merge
from numpy import fromstring, clip, uint8

class rgbselector(object):
    def setupRGB(self, MainWindow):
        self.horizontalSlider.valueChanged.connect(self.RGBManipulator) #Red
        self.horizontalSlider.setMaximum(255)
        self.horizontalSlider.setMinimum(-255)
        self.horizontalSlider_2.valueChanged.connect(self.RGBManipulator) #Green
        self.horizontalSlider_2.setMaximum(255)
        self.horizontalSlider_2.setMinimum(-255)
        self.horizontalSlider_3.valueChanged.connect(self.RGBManipulator) #Blue
        self.horizontalSlider_3.setMaximum(255)
        self.horizontalSlider_3.setMinimum(-255)        

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