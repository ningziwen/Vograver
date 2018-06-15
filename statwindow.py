# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Statwindow(object):
    def setupUi(self, Statwindow):
        Statwindow.setObjectName("Statwindow")
        Statwindow.resize(802, 603)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("english.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Statwindow.setWindowIcon(icon)
        self.timetb = QtWidgets.QTableWidget(Statwindow)
        self.timetb.setGeometry(QtCore.QRect(40, 70, 331, 241))
        self.timetb.setObjectName("timetb")
        self.timetb.setColumnCount(0)
        self.timetb.setRowCount(0)
        self.linegraph = QtWidgets.QGraphicsView(Statwindow)
        self.linegraph.setGeometry(QtCore.QRect(110, 380, 571, 181))
        self.linegraph.setObjectName("linegraph")
        self.cakegraph = QtWidgets.QGraphicsView(Statwindow)
        self.cakegraph.setGeometry(QtCore.QRect(450, 70, 261, 241))
        self.cakegraph.setObjectName("cakegraph")
        self.label = QtWidgets.QLabel(Statwindow)
        self.label.setGeometry(QtCore.QRect(120, 30, 181, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Statwindow)
        self.label_2.setGeometry(QtCore.QRect(480, 30, 211, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(17)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Statwindow)
        self.label_3.setGeometry(QtCore.QRect(300, 340, 401, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(17)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.exitbutton = QtWidgets.QPushButton(Statwindow)
        self.exitbutton.setGeometry(QtCore.QRect(700, 20, 91, 31))
        self.exitbutton.setObjectName("exitbutton")

        self.retranslateUi(Statwindow)
        QtCore.QMetaObject.connectSlotsByName(Statwindow)

    def retranslateUi(self, Statwindow):
        _translate = QtCore.QCoreApplication.translate
        Statwindow.setWindowTitle(_translate("Statwindow", "数据统计"))
        self.label.setText(_translate("Statwindow", "每日单词概况"))
        self.label_2.setText(_translate("Statwindow", "每日单词属性分布"))
        self.label_3.setText(_translate("Statwindow", "每日单词数折线图"))
        self.exitbutton.setText(_translate("Statwindow", "返回"))

