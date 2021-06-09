from PyQt5 import QtWidgets, QtGui, QtCore
from program.edgedetection.view import Ui_Dialog
from numpy import fromstring, uint8, array
from cv2 import rectangle, imshow, merge, Canny, Laplacian, CV_8U, cvtColor, COLOR_BGR2GRAY, filter2D

class edgeDetection(Ui_Dialog, QtWidgets.QDialog):
    def __init__(self):
        super(edgeDetection, self).__init__()
        self.setWindowIcon(QtGui.QIcon('program/icon/original.png'))
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Exit)
        self.pushButton_2.clicked.connect(self.Cancel)
        self.comboBox.currentTextChanged.connect(self.setupEdgeDetection)
        
    def setupEdgeDetection(self, event):
        try:
            gambaredit = self.label.pixmap().toImage()
            gambar = gambaredit.convertToFormat(4)
            s = gambar.bits().asstring(gambar.width() * gambar.height() * 4)
            arr = fromstring(s, dtype=uint8).reshape((gambar.height(), gambar.width(), 4))
            if event == 'Canny':
                arr = Canny(arr, 50, 100)
                arr = merge([arr, arr, arr, arr])
            elif event == 'Laplacian':
                arr = cvtColor(arr, COLOR_BGR2GRAY)
                arr = Laplacian(arr, CV_8U, ksize=3)
                arr = merge([arr, arr, arr, arr])
            elif event == 'Prewitt':
                arr = cvtColor(arr, COLOR_BGR2GRAY)
                kernelx = array([[1,1,1],[0,0,0],[-1,-1,-1]])
                arr = filter2D(arr, -1, kernelx)
                arr = merge([arr, arr, arr, arr])
                
            gambar3 = QtGui.QImage(arr.data, arr.shape[1], arr.shape[0], QtGui.QImage.Format_RGB32).rgbSwapped().rgbSwapped()
            self.label_2.setPixmap(QtGui.QPixmap.fromImage(gambar3))
            self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        except AttributeError:
            pass
        
    def Cancel(self):
        QtWidgets.QDialog.reject(self)

    def Exit(self):
        QtWidgets.QDialog.accept(self)
            