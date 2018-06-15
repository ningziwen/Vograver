# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wordbase.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Wordbase(object):
    def setupUi(self, Wordbase):
        Wordbase.setObjectName("Wordbase")
        Wordbase.resize(724, 560)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/english.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Wordbase.setWindowIcon(icon)
        self.importbutton = QtWidgets.QPushButton(Wordbase)
        self.importbutton.setGeometry(QtCore.QRect(50, 70, 121, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.importbutton.setFont(font)
        self.importbutton.setMouseTracking(False)
        self.importbutton.setObjectName("importbutton")
        self.exportbutton = QtWidgets.QPushButton(Wordbase)
        self.exportbutton.setGeometry(QtCore.QRect(50, 140, 121, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.exportbutton.setFont(font)
        self.exportbutton.setMouseTracking(False)
        self.exportbutton.setObjectName("exportbutton")
        self.exitbutton = QtWidgets.QPushButton(Wordbase)
        self.exitbutton.setGeometry(QtCore.QRect(594, 22, 111, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.exitbutton.setFont(font)
        self.exitbutton.setMouseTracking(False)
        self.exitbutton.setObjectName("exitbutton")
        self.wordtable = QtWidgets.QTableWidget(Wordbase)
        self.wordtable.setGeometry(QtCore.QRect(200, 70, 501, 431))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.wordtable.setFont(font)
        self.wordtable.setObjectName("wordtable")
        self.wordtable.setColumnCount(0)
        self.wordtable.setRowCount(0)

        self.retranslateUi(Wordbase)
        QtCore.QMetaObject.connectSlotsByName(Wordbase)

    def retranslateUi(self, Wordbase):
        _translate = QtCore.QCoreApplication.translate
        Wordbase.setWindowTitle(_translate("Wordbase", "浏览词库"))
        self.importbutton.setText(_translate("Wordbase", "导入词库"))
        self.exportbutton.setText(_translate("Wordbase", "导出词库"))
        self.exitbutton.setText(_translate("Wordbase", "返回"))

