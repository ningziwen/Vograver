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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Administrator/.designer/backup/english.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Quickstartwords.setWindowIcon(icon)
        self.english = QtWidgets.QLabel(Quickstartwords)
        self.english.setGeometry(QtCore.QRect(260, 50, 291, 61))
        self.english.setText("")
        self.english.setObjectName("english")
        self.chinese = QtWidgets.QLabel(Quickstartwords)
        self.chinese.setGeometry(QtCore.QRect(160, 130, 481, 231))
        self.chinese.setObjectName("chinese")
        self.showchinesebutton = QtWidgets.QPushButton(Quickstartwords)
        self.showchinesebutton.setGeometry(QtCore.QRect(310, 400, 151, 51))
        self.showchinesebutton.setObjectName("showchinesebutton")
        self.exitbutton = QtWidgets.QPushButton(Quickstartwords)
        self.exitbutton.setGeometry(QtCore.QRect(630, 50, 75, 23))
        self.exitbutton.setObjectName("exitbutton")
        self.wholebutton = QtWidgets.QPushButton(Quickstartwords)
        self.wholebutton.setGeometry(QtCore.QRect(300, 130, 181, 61))
        self.wholebutton.setObjectName("wholebutton")
        self.hardbutton = QtWidgets.QPushButton(Quickstartwords)
        self.hardbutton.setGeometry(QtCore.QRect(300, 220, 181, 61))
        self.hardbutton.setObjectName("hardbutton")
        self.hardcheck = QtWidgets.QCheckBox(Quickstartwords)
        self.hardcheck.setGeometry(QtCore.QRect(570, 400, 121, 41))
        self.hardcheck.setObjectName("hardcheck")

        self.retranslateUi(Quickstartwords)
        QtCore.QMetaObject.connectSlotsByName(Quickstartwords)

    def retranslateUi(self, Quickstartwords):
        _translate = QtCore.QCoreApplication.translate
        Quickstartwords.setWindowTitle(_translate("Quickstartwords", "Form"))
        self.chinese.setText(_translate("Quickstartwords", "\\"))
        self.showchinesebutton.setText(_translate("Quickstartwords", "显示释义/继续(Space)"))
        self.exitbutton.setText(_translate("Quickstartwords", "结束"))
        self.wholebutton.setText(_translate("Quickstartwords", "刷全部单词"))
        self.hardbutton.setText(_translate("Quickstartwords", "仅刷困难词"))
        self.hardcheck.setText(_translate("Quickstartwords", "设为困难词(H)"))

