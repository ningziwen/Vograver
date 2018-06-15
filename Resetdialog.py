# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resetdialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Resetdialog(object):
    def setupUi(self, Resetdialog):
        Resetdialog.setObjectName("Resetdialog")
        Resetdialog.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("english.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Resetdialog.setWindowIcon(icon)
        self.buttonBox = QtWidgets.QDialogButtonBox(Resetdialog)
        self.buttonBox.setGeometry(QtCore.QRect(20, 190, 251, 21))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Resetdialog)
        self.label.setGeometry(QtCore.QRect(70, 70, 271, 81))
        self.label.setAcceptDrops(False)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")

        self.retranslateUi(Resetdialog)
        self.buttonBox.accepted.connect(Resetdialog.accept)
        self.buttonBox.rejected.connect(Resetdialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Resetdialog)

    def retranslateUi(self, Resetdialog):
        _translate = QtCore.QCoreApplication.translate
        Resetdialog.setWindowTitle(_translate("Resetdialog", "确认信息"))
        self.label.setText(_translate("Resetdialog", "此选项会清空所有学习记录并重置为当前日期开始新的学习记录！是否继续？"))

