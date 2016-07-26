# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fullscreen.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 595)
        MainWindow.setWindowOpacity(0.5)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background: white")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.butExit = QtWidgets.QPushButton(self.centralwidget)
        self.butExit.setGeometry(QtCore.QRect(650, 500, 99, 27))
        self.butExit.setObjectName("butExit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.butExit.setText(_translate("MainWindow", "PushButton"))

