# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'quickstartwords.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Quickstartwords(object):
    def setupUi(self, Quickstartwords):
        Quickstartwords.setObjectName("Quickstartwords")
        Quickstartwords.resize(780, 525)
        self.english = QtWidgets.QLabel(Quickstartwords)
        self.english.setGeometry(QtCore.QRect(290, 70, 221, 41))
        self.english.setText("")
        self.english.setObjectName("english")
        self.chinese = QtWidgets.QLabel(Quickstartwords)
        self.chinese.setGeometry(QtCore.QRect(220, 160, 381, 171))
        self.chinese.setObjectName("chinese")
        self.showchinesebutton = QtWidgets.QPushButton(Quickstartwords)
        self.showchinesebutton.setGeometry(QtCore.QRect(310, 400, 151, 51))
        self.showchinesebutton.setObjectName("showchinesebutton")
        self.exitbutton = QtWidgets.QPushButton(Quickstartwords)
        self.exitbutton.setGeometry(QtCore.QRect(630, 50, 75, 23))
        self.exitbutton.setObjectName("exitbutton")

        self.retranslateUi(Quickstartwords)
        QtCore.QMetaObject.connectSlotsByName(Quickstartwords)

    def retranslateUi(self, Quickstartwords):
        _translate = QtCore.QCoreApplication.translate
        Quickstartwords.setWindowTitle(_translate("Quickstartwords", "Form"))
        self.chinese.setText(_translate("Quickstartwords", "\\"))
        self.showchinesebutton.setText(_translate("Quickstartwords", "显示释义"))
        self.exitbutton.setText(_translate("Quickstartwords", "结束"))

