# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'startwords.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Startwords(object):
    def setupUi(self, Startwords):
        Startwords.setObjectName("Startwords")
        Startwords.resize(775, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("english.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Startwords.setWindowIcon(icon)
        self.remember = QtWidgets.QPushButton(Startwords)
        self.remember.setGeometry(QtCore.QRect(200, 410, 101, 41))
        self.remember.setObjectName("remember")
        self.notremember = QtWidgets.QPushButton(Startwords)
        self.notremember.setGeometry(QtCore.QRect(350, 410, 101, 41))
        self.notremember.setObjectName("notremember")
        self.kill = QtWidgets.QPushButton(Startwords)
        self.kill.setGeometry(QtCore.QRect(510, 410, 101, 41))
        self.kill.setObjectName("kill")
        self.showchinesebutton = QtWidgets.QPushButton(Startwords)
        self.showchinesebutton.setEnabled(True)
        self.showchinesebutton.setGeometry(QtCore.QRect(260, 400, 271, 61))
        self.showchinesebutton.setObjectName("showchinesebutton")
        self.beginbutton = QtWidgets.QPushButton(Startwords)
        self.beginbutton.setEnabled(True)
        self.beginbutton.setGeometry(QtCore.QRect(230, 160, 331, 121))
        self.beginbutton.setObjectName("beginbutton")
        self.english = QtWidgets.QLabel(Startwords)
        self.english.setGeometry(QtCore.QRect(210, 140, 361, 171))
        self.english.setText("")
        self.english.setTextFormat(QtCore.Qt.AutoText)
        self.english.setAlignment(QtCore.Qt.AlignCenter)
        self.english.setObjectName("english")
        self.chinese = QtWidgets.QLabel(Startwords)
        self.chinese.setGeometry(QtCore.QRect(160, 140, 491, 211))
        self.chinese.setText("")
        self.chinese.setObjectName("chinese")
        self.exitbutton = QtWidgets.QPushButton(Startwords)
        self.exitbutton.setGeometry(QtCore.QRect(620, 30, 131, 51))
        self.exitbutton.setObjectName("exitbutton")
        self.wordstatus = QtWidgets.QLabel(Startwords)
        self.wordstatus.setGeometry(QtCore.QRect(160, 50, 111, 21))
        self.wordstatus.setText("")
        self.wordstatus.setObjectName("wordstatus")
        self.hardcheck = QtWidgets.QCheckBox(Startwords)
        self.hardcheck.setGeometry(QtCore.QRect(640, 470, 121, 41))
        self.hardcheck.setObjectName("hardcheck")
        self.rechoose = QtWidgets.QPushButton(Startwords)
        self.rechoose.setGeometry(QtCore.QRect(634, 510, 101, 41))
        self.rechoose.setObjectName("rechoose")
        self.action = QtWidgets.QAction(Startwords)
        self.action.setObjectName("action")

        self.retranslateUi(Startwords)
        QtCore.QMetaObject.connectSlotsByName(Startwords)

    def retranslateUi(self, Startwords):
        _translate = QtCore.QCoreApplication.translate
        Startwords.setWindowTitle(_translate("Startwords", "背单词"))
        self.remember.setText(_translate("Startwords", "记得(Z)"))
        self.notremember.setText(_translate("Startwords", "不记得(X)"))
        self.kill.setText(_translate("Startwords", "斩(C)"))
        self.showchinesebutton.setText(_translate("Startwords", "显示释义(V)"))
        self.beginbutton.setText(_translate("Startwords", "开始"))
        self.exitbutton.setText(_translate("Startwords", "结束"))
        self.hardcheck.setText(_translate("Startwords", "设为困难词"))
        self.rechoose.setText(_translate("Startwords", "撤销"))
        self.action.setText(_translate("Startwords", "文件"))

