# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(345, 277)
        font = QtGui.QFont()
        font.setKerning(True)
        Dialog.setFont(font)
        Dialog.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        Dialog.setWhatsThis("")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(9, 9, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gambarCrop = QtWidgets.QLabel(Dialog)
        self.gambarCrop.setFrameShape(QtWidgets.QFrame.Box)
        self.gambarCrop.setAlignment(QtCore.Qt.AlignCenter)
        self.gambarCrop.setObjectName("gambarCrop")
        self.verticalLayout.addWidget(self.gambarCrop)
        self.gambar = QtWidgets.QLabel(Dialog)
        self.gambar.setEnabled(True)
        self.gambar.setAcceptDrops(False)
        self.gambar.setWhatsThis("")
        self.gambar.setAccessibleDescription("")
        self.gambar.setInputMethodHints(QtCore.Qt.ImhNone)
        self.gambar.setObjectName("gambar")
        self.verticalLayout.addWidget(self.gambar)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.TombolOk = QtWidgets.QPushButton(Dialog)
        self.TombolOk.setObjectName("TombolOk")
        self.horizontalLayout.addWidget(self.TombolOk)
        self.TombolCancel = QtWidgets.QPushButton(Dialog)
        self.TombolCancel.setObjectName("TombolCancel")
        self.horizontalLayout.addWidget(self.TombolCancel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gambar.hide()
        self.gambarCrop.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Crop Image"))
        self.gambarCrop.setText(_translate("Dialog", "Original Image"))
        self.gambar.setText(_translate("Dialog", "TextLabel"))
        self.TombolOk.setText(_translate("Dialog", "Ok"))
        self.TombolCancel.setText(_translate("Dialog", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
