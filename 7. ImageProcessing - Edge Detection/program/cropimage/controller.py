from PyQt5 import QtWidgets, QtGui, QtCore
from program.cropimage.view import Ui_Dialog
from numpy import fromstring, uint8
from cv2 import rectangle, imshow, merge

class cropImage(Ui_Dialog, QtWidgets.QDialog):
    def __init__(self):
        super(cropImage, self).__init__()
        self.setWindowIcon(QtGui.QIcon('program/icon/original.png'))
        self.setupUi(self)
        self.TombolCancel.clicked.connect(self.Cancel)
        self.TombolOk.clicked.connect(self.Exit)
        
    def Cancel(self):
        QtWidgets.QDialog.reject(self)

    def Exit(self):
        try:
            gambaredit = self.gambar.pixmap().toImage()
            gambar = gambaredit.convertToFormat(4)
            s = gambar.bits().asstring(gambar.width() * gambar.height() * 4)
            arr = fromstring(s, dtype=uint8).reshape((gambar.height(), gambar.width(), 4))
            RoI = [(x_start, y_start), (x_end, y_end)]
            arr = arr[RoI[0][1]:RoI[1][1], RoI[0][0]:RoI[1][0]]
            arr = merge([arr[:,:,0],arr[:,:,1],arr[:,:,2],arr[:,:,3]])
            gambar3 = QtGui.QImage(arr.data, arr.shape[1], arr.shape[0], QtGui.QImage.Format_RGB32).rgbSwapped().rgbSwapped()
            self._output = gambar3    
            QtWidgets.QDialog.accept(self)
        except AttributeError:
            QtWidgets.QDialog.reject(self)
            
    def mousePressEvent(self, event):
        global x_start, y_start, x_end, y_end
        if event.button() == QtCore.Qt.LeftButton:
            x_start = event.x()
            y_start = event.y()
            
    def mouseMoveEvent(self, event):
        try:
            global x_start, y_start, x_end, y_end
            x_end = event.x()
            y_end = event.y()
            gambaredit = self.gambar.pixmap()
            gambaredit = gambaredit.toImage()
            gambar = gambaredit.convertToFormat(4)
            s = gambar.bits().asstring(gambar.width() * gambar.height() * 4)
            arr = fromstring(s, dtype=uint8).reshape((gambar.height(), gambar.width(), 4))
            rectangle(arr, (x_start, y_start), (x_end, y_end), (0, 0, 0), 1)
            gambar3 = QtGui.QImage(arr.data, arr.shape[1], arr.shape[0], QtGui.QImage.Format_RGB32).rgbSwapped().rgbSwapped()
            self.gambarCrop.setPixmap(QtGui.QPixmap.fromImage(gambar3))
            self.gambarCrop.setAlignment(QtCore.Qt.AlignCenter)
        except AttributeError:
            pass
        
    def mouseReleaseEvent(self, event):
        try:
            pass
        except AttributeError:
            pass

    def get_output(self):
        return self._output
