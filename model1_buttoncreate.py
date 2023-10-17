# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'model1_buttoncreate.ui'
#
# Created: Wed Jun 21 14:33:16 2023
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1781, 752)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.maintab = QtGui.QTabWidget(self.centralwidget)
        self.maintab.setGeometry(QtCore.QRect(0, 0, 1383, 641))
        self.maintab.setMinimumSize(QtCore.QSize(1383, 611))
        self.maintab.setStyleSheet("background-color: rgb(8, 8, 8);\n"
"background-color: rgb(255, 255, 255);")
        self.maintab.setObjectName("maintab")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.frame_subt_3 = QtGui.QFrame(self.tab_2)
        self.frame_subt_3.setGeometry(QtCore.QRect(0, 520, 1361, 41))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_subt_3.sizePolicy().hasHeightForWidth())
        self.frame_subt_3.setSizePolicy(sizePolicy)
        self.frame_subt_3.setMinimumSize(QtCore.QSize(500, 41))
        self.frame_subt_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_subt_3.setFrameShape(QtGui.QFrame.Box)
        self.frame_subt_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_subt_3.setObjectName("frame_subt_3")
        self.pushButton_CLEARsub_3 = QtGui.QPushButton(self.frame_subt_3)
        self.pushButton_CLEARsub_3.setGeometry(QtCore.QRect(1110, 10, 101, 21))
        self.pushButton_CLEARsub_3.setCursor(QtCore.Qt.PointingHandCursor)
        self.pushButton_CLEARsub_3.setMouseTracking(True)
        self.pushButton_CLEARsub_3.setStyleSheet("background-color: rgb(153, 153, 153);")
        self.pushButton_CLEARsub_3.setObjectName("pushButton_CLEARsub_3")
        self.pushButton_closecard = QtGui.QPushButton(self.frame_subt_3)
        self.pushButton_closecard.setGeometry(QtCore.QRect(1240, 10, 101, 21))
        self.pushButton_closecard.setCursor(QtCore.Qt.PointingHandCursor)
        self.pushButton_closecard.setMouseTracking(True)
        self.pushButton_closecard.setStyleSheet("background-color: rgb(153, 153, 153);")
        self.pushButton_closecard.setObjectName("pushButton_closecard")
        self.maintab.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1781, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.maintab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_CLEARsub_3.setText(QtGui.QApplication.translate("MainWindow", "clear sub", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_closecard.setText(QtGui.QApplication.translate("MainWindow", "Close card", None, QtGui.QApplication.UnicodeUTF8))
        self.maintab.setTabText(self.maintab.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Page", None, QtGui.QApplication.UnicodeUTF8))

import try_rc
