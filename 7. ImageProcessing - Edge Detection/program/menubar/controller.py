from PyQt5 import QtGui, QtCore, QtWidgets

class menuBar(object):
    def setupMenuBar(self, MainWindow):
        self.actionExit.triggered.connect(self.Exit) #Exit
        self.actionBackground_Color.triggered.connect(self.BGcolor) #BGcolor

    def Exit(self):
        exit()

    def BGcolor(self):
        bgcolor = QtWidgets.QColorDialog.getColor()
        if bgcolor.isValid():
            self.setStyleSheet('QWidget { background-color: %s}' % bgcolor.name())
    