# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\P\bmjc\hhx1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(665, 437)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ok = QtWidgets.QPushButton(self.centralwidget)
        self.ok.setGeometry(QtCore.QRect(340, 10, 75, 23))
        self.ok.setObjectName("ok")
        self.lineEdit_mulu = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_mulu.setGeometry(QtCore.QRect(40, 10, 91, 20))
        self.lineEdit_mulu.setObjectName("lineEdit_mulu")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(550, 10, 88, 20))
        self.dateEdit.setDate(QtCore.QDate(2020, 2, 11))
        self.dateEdit.setObjectName("dateEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 41, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 10, 61, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_riqi = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_riqi.setGeometry(QtCore.QRect(220, 10, 111, 20))
        self.lineEdit_riqi.setObjectName("lineEdit_riqi")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 50, 631, 341))
        self.plainTextEdit.setObjectName("plainTextEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 665, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ok.setText(_translate("MainWindow", "开始替换"))
        self.lineEdit_mulu.setText(_translate("MainWindow", "6"))
        self.label.setText(_translate("MainWindow", "目录："))
        self.label_2.setText(_translate("MainWindow", "输入日期："))
        self.lineEdit_riqi.setText(_translate("MainWindow", "2020-02-11"))
