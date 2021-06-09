# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crop.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(210, 104)
        font = QtGui.QFont()
        font.setKerning(True)
        Dialog.setFont(font)
        Dialog.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        Dialog.setWhatsThis("")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(0, 0, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gambarCrop = QtWidgets.QLabel(Dialog)
        self.gambarCrop.setText("")
        self.gambarCrop.setObjectName("gambarCrop")
        self.verticalLayout.addWidget(self.gambarCrop)
        self.gambar = QtWidgets.QLabel(Dialog)
        self.gambar.setEnabled(True)
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
        self.gambar.setText(_translate("Dialog", "TextLabel"))
        self.TombolOk.setText(_translate("Dialog", "Ok"))
        self.TombolCancel.setText(_translate("Dialog", "Cancel"))

