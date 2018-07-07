# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'function.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Function(object):
    def setupUi(self, Function):
        Function.setObjectName("Function")
        Function.resize(800, 586)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("english.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Function.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Function)
        self.centralwidget.setObjectName("centralwidget")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(260, 30, 311, 131))
        self.start.setObjectName("start")
        self.quickstart = QtWidgets.QPushButton(self.centralwidget)
        self.quickstart.setGeometry(QtCore.QRect(260, 180, 311, 131))
        self.quickstart.setObjectName("quickstart")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(170, 330, 501, 191))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 70, 171, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 120, 141, 16))
        self.label_2.setObjectName("label_2")
        self.newwords = QtWidgets.QLineEdit(self.groupBox)
        self.newwords.setGeometry(QtCore.QRect(30, 90, 113, 20))
        self.newwords.setObjectName("newwords")
        self.reviewwords = QtWidgets.QLineEdit(self.groupBox)
        self.reviewwords.setGeometry(QtCore.QRect(30, 140, 113, 20))
        self.reviewwords.setObjectName("reviewwords")
        self.scanwords = QtWidgets.QPushButton(self.groupBox)
        self.scanwords.setGeometry(QtCore.QRect(330, 22, 141, 61))
        self.scanwords.setObjectName("scanwords")
        self.statwords = QtWidgets.QPushButton(self.groupBox)
        self.statwords.setGeometry(QtCore.QRect(330, 100, 141, 61))
        self.statwords.setObjectName("statwords")
        self.resetdata = QtWidgets.QPushButton(self.groupBox)
        self.resetdata.setGeometry(QtCore.QRect(30, 30, 121, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setBold(True)
        font.setWeight(75)
        self.resetdata.setFont(font)
        self.resetdata.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.resetdata.setObjectName("resetdata")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(160, 40, 111, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setObjectName("label_3")
        Function.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Function)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Function.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Function)
        self.statusbar.setObjectName("statusbar")
        Function.setStatusBar(self.statusbar)

        self.retranslateUi(Function)
        QtCore.QMetaObject.connectSlotsByName(Function)

    def retranslateUi(self, Function):
        _translate = QtCore.QCoreApplication.translate
        Function.setWindowTitle(_translate("Function", "Vograver"))
        self.start.setText(_translate("Function", "开始背单词"))
        self.quickstart.setText(_translate("Function", "极速刷词"))
        self.groupBox.setTitle(_translate("Function", "配置"))
        self.label.setText(_translate("Function", "每天最多生词数"))
        self.label_2.setText(_translate("Function", "每天最多复习词数"))
        self.scanwords.setText(_translate("Function", "浏览词库"))
        self.statwords.setText(_translate("Function", "数据统计"))
        self.resetdata.setText(_translate("Function", "开始/重置学习"))
        self.label_3.setText(_translate("Function", "（初次使用请点击）"))

