# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LXI_QT.ui'
#
# Created: Wed Jun  7 17:56:29 2023
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindo(object):
    def setupUi(self, MainWindo):
        MainWindo.setObjectName("MainWindo")
        MainWindo.setWindowModality(QtCore.Qt.WindowModal)
        MainWindo.resize(1388, 781)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindo.sizePolicy().hasHeightForWidth())
        MainWindo.setSizePolicy(sizePolicy)
        MainWindo.setMinimumSize(QtCore.QSize(1380, 716))
        MainWindo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtGui.QWidget(MainWindo)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1371, 81))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.widget.setObjectName("widget")
        self.label = QtGui.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 10, 151, 61))
        self.label.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/new/VV-1 - Copy.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.line_6 = QtGui.QFrame(self.widget)
        self.line_6.setGeometry(QtCore.QRect(0, -10, 1381, 15))
        self.line_6.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.line_6.setFrameShadow(QtGui.QFrame.Plain)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 84, 1381, 15))
        self.line.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.line.setFrameShadow(QtGui.QFrame.Plain)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.maintab = QtGui.QTabWidget(self.centralwidget)
        self.maintab.setGeometry(QtCore.QRect(0, 90, 1383, 641))
        self.maintab.setMinimumSize(QtCore.QSize(1383, 611))
        self.maintab.setStyleSheet("background-color: rgb(8, 8, 8);\n"
"background-color: rgb(255, 255, 255);")
        self.maintab.setObjectName("maintab")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.widget_2 = QtGui.QWidget(self.tab)
        self.widget_2.setGeometry(QtCore.QRect(0, 20, 1371, 511))
        self.widget_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_2.setObjectName("widget_2")
        self.frame_display = QtGui.QFrame(self.widget_2)
        self.frame_display.setGeometry(QtCore.QRect(690, 18, 671, 491))
        self.frame_display.setFrameShape(QtGui.QFrame.Box)
        self.frame_display.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_display.setObjectName("frame_display")
        self.listView = QtGui.QListView(self.frame_display)
        self.listView.setGeometry(QtCore.QRect(-610, 410, 256, 192))
        self.listView.setObjectName("listView")
        self.label_details = QtGui.QLabel(self.frame_display)
        self.label_details.setGeometry(QtCore.QRect(2, 2, 669, 488))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.label_details.setFont(font)
        self.label_details.setFrameShape(QtGui.QFrame.Box)
        self.label_details.setText("")
        self.label_details.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_details.setMargin(3)
        self.label_details.setIndent(0)
        self.label_details.setObjectName("label_details")
        self.scrollArea_LXI = QtGui.QScrollArea(self.widget_2)
        self.scrollArea_LXI.setGeometry(QtCore.QRect(10, 240, 672, 115))
        self.scrollArea_LXI.setMinimumSize(QtCore.QSize(651, 82))
        self.scrollArea_LXI.setStyleSheet("")
        self.scrollArea_LXI.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea_LXI.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_LXI.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_LXI.setWidgetResizable(True)
        self.scrollArea_LXI.setObjectName("scrollArea_LXI")
        self.scrollAreaWidgetContents_5 = QtGui.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 672, 115))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButton_LXI = QtGui.QPushButton(self.scrollAreaWidgetContents_5)
        self.pushButton_LXI.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_LXI.setFont(font)
        self.pushButton_LXI.setStyleSheet("QPushButton\n"
"                             {\n"
"                            \n"
"    background-color : lightblue\n"
"                            }\n"
"\n"
"      QPushButton::pressed\n"
"                             {\n"
"                         \n"
"    background-color: rgb(66, 133, 200);\n"
"                             }\n"
"")
        self.pushButton_LXI.setAutoDefault(False)
        self.pushButton_LXI.setDefault(False)
        self.pushButton_LXI.setFlat(False)
        self.pushButton_LXI.setObjectName("pushButton_LXI")
        self.verticalLayout_5.addWidget(self.pushButton_LXI)
        self.frame_LXI = QtGui.QFrame(self.scrollAreaWidgetContents_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_LXI.sizePolicy().hasHeightForWidth())
        self.frame_LXI.setSizePolicy(sizePolicy)
        self.frame_LXI.setMinimumSize(QtCore.QSize(650, 41))
        self.frame_LXI.setStyleSheet("")
        self.frame_LXI.setFrameShape(QtGui.QFrame.Box)
        self.frame_LXI.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_LXI.setObjectName("frame_LXI")
        self.pushButton_open_LXI = QtGui.QPushButton(self.frame_LXI)
        self.pushButton_open_LXI.setGeometry(QtCore.QRect(10, 10, 75, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(13)
        sizePolicy.setHeightForWidth(self.pushButton_open_LXI.sizePolicy().hasHeightForWidth())
        self.pushButton_open_LXI.setSizePolicy(sizePolicy)
        self.pushButton_open_LXI.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.pushButton_open_LXI.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_open_LXI.setStyleSheet("background-color: rgb(126, 126, 126);")
        self.pushButton_open_LXI.setAutoDefault(False)
        self.pushButton_open_LXI.setDefault(True)
        self.pushButton_open_LXI.setFlat(True)
        self.pushButton_open_LXI.setObjectName("pushButton_open_LXI")
        self.label_LXI = QtGui.QLabel(self.frame_LXI)
        self.label_LXI.setGeometry(QtCore.QRect(91, 16, 551, 16))
        self.label_LXI.setStyleSheet("")
        self.label_LXI.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_LXI.setText("")
        self.label_LXI.setObjectName("label_LXI")
        self.verticalLayout_5.addWidget(self.frame_LXI)
        self.scrollArea_LXI.setWidget(self.scrollAreaWidgetContents_5)
        self.scrollArea_PCI = QtGui.QScrollArea(self.widget_2)
        self.scrollArea_PCI.setGeometry(QtCore.QRect(10, 10, 672, 115))
        self.scrollArea_PCI.setMinimumSize(QtCore.QSize(651, 82))
        self.scrollArea_PCI.setStyleSheet("")
        self.scrollArea_PCI.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea_PCI.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_PCI.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_PCI.setWidgetResizable(True)
        self.scrollArea_PCI.setObjectName("scrollArea_PCI")
        self.scrollAreaWidgetContents_4 = QtGui.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 672, 115))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_PCI = QtGui.QPushButton(self.scrollAreaWidgetContents_4)
        self.pushButton_PCI.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_PCI.setFont(font)
        self.pushButton_PCI.setStyleSheet("QPushButton\n"
"                             {\n"
"                            \n"
"    background-color : lightblue\n"
"                            }\n"
"\n"
"      QPushButton::pressed\n"
"                             {\n"
"                         \n"
"    background-color: rgb(66, 133, 200);\n"
"                             }\n"
"\n"
"")
        self.pushButton_PCI.setAutoDefault(False)
        self.pushButton_PCI.setDefault(True)
        self.pushButton_PCI.setFlat(False)
        self.pushButton_PCI.setObjectName("pushButton_PCI")
        self.verticalLayout_2.addWidget(self.pushButton_PCI)
        self.frame_PCI = QtGui.QFrame(self.scrollAreaWidgetContents_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_PCI.sizePolicy().hasHeightForWidth())
        self.frame_PCI.setSizePolicy(sizePolicy)
        self.frame_PCI.setMinimumSize(QtCore.QSize(650, 41))
        self.frame_PCI.setFrameShape(QtGui.QFrame.Box)
        self.frame_PCI.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_PCI.setObjectName("frame_PCI")
        self.pushButton_open_PCI = QtGui.QPushButton(self.frame_PCI)
        self.pushButton_open_PCI.setGeometry(QtCore.QRect(10, 10, 75, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(13)
        sizePolicy.setHeightForWidth(self.pushButton_open_PCI.sizePolicy().hasHeightForWidth())
        self.pushButton_open_PCI.setSizePolicy(sizePolicy)
        self.pushButton_open_PCI.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.pushButton_open_PCI.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_open_PCI.setStyleSheet("background-color: rgb(209, 209, 209);")
        self.pushButton_open_PCI.setAutoDefault(False)
        self.pushButton_open_PCI.setDefault(True)
        self.pushButton_open_PCI.setFlat(True)
        self.pushButton_open_PCI.setObjectName("pushButton_open_PCI")
        self.label_PCI = QtGui.QLabel(self.frame_PCI)
        self.label_PCI.setGeometry(QtCore.QRect(91, 16, 551, 20))
        self.label_PCI.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_PCI.setText("")
        self.label_PCI.setObjectName("label_PCI")
        self.verticalLayout_2.addWidget(self.frame_PCI)
        self.scrollArea_PCI.setWidget(self.scrollAreaWidgetContents_4)
        self.scrollArea_PXI = QtGui.QScrollArea(self.widget_2)
        self.scrollArea_PXI.setGeometry(QtCore.QRect(10, 125, 672, 115))
        self.scrollArea_PXI.setMinimumSize(QtCore.QSize(651, 82))
        self.scrollArea_PXI.setStyleSheet("")
        self.scrollArea_PXI.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea_PXI.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_PXI.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_PXI.setWidgetResizable(True)
        self.scrollArea_PXI.setObjectName("scrollArea_PXI")
        self.scrollAreaWidgetContents_3 = QtGui.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 672, 115))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_PXI = QtGui.QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButton_PXI.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_PXI.setFont(font)
        self.pushButton_PXI.setStyleSheet("QPushButton\n"
"                             {\n"
"                            \n"
"    background-color : lightblue\n"
"                            }\n"
"\n"
"      QPushButton::pressed\n"
"                             {\n"
"                         \n"
"    background-color: rgb(66, 133, 200);\n"
"                             }\n"
"")
        self.pushButton_PXI.setAutoDefault(True)
        self.pushButton_PXI.setDefault(False)
        self.pushButton_PXI.setFlat(False)
        self.pushButton_PXI.setObjectName("pushButton_PXI")
        self.verticalLayout_3.addWidget(self.pushButton_PXI)
        self.frame_pxi = QtGui.QFrame(self.scrollAreaWidgetContents_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_pxi.sizePolicy().hasHeightForWidth())
        self.frame_pxi.setSizePolicy(sizePolicy)
        self.frame_pxi.setMinimumSize(QtCore.QSize(650, 41))
        self.frame_pxi.setStyleSheet("")
        self.frame_pxi.setFrameShape(QtGui.QFrame.Box)
        self.frame_pxi.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_pxi.setObjectName("frame_pxi")
        self.pushButton_open_PXI = QtGui.QPushButton(self.frame_pxi)
        self.pushButton_open_PXI.setGeometry(QtCore.QRect(10, 10, 75, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(13)
        sizePolicy.setHeightForWidth(self.pushButton_open_PXI.sizePolicy().hasHeightForWidth())
        self.pushButton_open_PXI.setSizePolicy(sizePolicy)
        self.pushButton_open_PXI.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.pushButton_open_PXI.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_open_PXI.setStyleSheet("background-color: rgb(209, 209, 209);")
        self.pushButton_open_PXI.setAutoDefault(False)
        self.pushButton_open_PXI.setDefault(True)
        self.pushButton_open_PXI.setFlat(True)
        self.pushButton_open_PXI.setObjectName("pushButton_open_PXI")
        self.label_PXI = QtGui.QLabel(self.frame_pxi)
        self.label_PXI.setGeometry(QtCore.QRect(100, 10, 541, 21))
        self.label_PXI.setStyleSheet("")
        self.label_PXI.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_PXI.setText("")
        self.label_PXI.setObjectName("label_PXI")
        self.verticalLayout_3.addWidget(self.frame_pxi)
        self.scrollArea_PXI.setWidget(self.scrollAreaWidgetContents_3)
        self.label_2 = QtGui.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(10, 354, 663, 154))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 218, 218);")
        self.label_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_2.setObjectName("label_2")
        self.line_2 = QtGui.QFrame(self.widget_2)
        self.line_2.setGeometry(QtCore.QRect(672, 19, 2, 501))
        self.line_2.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtGui.QFrame(self.widget_2)
        self.line_3.setGeometry(QtCore.QRect(18, 20, 2, 581))
        self.line_3.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtGui.QFrame(self.widget_2)
        self.line_4.setGeometry(QtCore.QRect(19, 20, 657, 2))
        self.line_4.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtGui.QFrame(self.widget_2)
        self.line_5.setGeometry(QtCore.QRect(17, 509, 657, 2))
        self.line_5.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.progressBar = QtGui.QProgressBar(self.tab)
        self.progressBar.setGeometry(QtCore.QRect(0, 574, 1401, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.pushButton_refresh = QtGui.QPushButton(self.tab)
        self.pushButton_refresh.setGeometry(QtCore.QRect(20, 550, 75, 23))
        self.pushButton_refresh.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.pushButton_refresh.setAutoDefault(False)
        self.pushButton_refresh.setDefault(True)
        self.pushButton_refresh.setFlat(True)
        self.pushButton_refresh.setObjectName("pushButton_refresh")
        self.lineEdit_search = QtGui.QLineEdit(self.tab)
        self.lineEdit_search.setGeometry(QtCore.QRect(120, 550, 222, 21))
        self.lineEdit_search.setInputMask("")
        self.lineEdit_search.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_search.setDragEnabled(False)
        self.lineEdit_search.setReadOnly(False)
        self.lineEdit_search.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.pushButton_add = QtGui.QPushButton(self.tab)
        self.pushButton_add.setGeometry(QtCore.QRect(360, 550, 75, 23))
        self.pushButton_add.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.pushButton_add.setDefault(True)
        self.pushButton_add.setFlat(True)
        self.pushButton_add.setObjectName("pushButton_add")
        self.frame_3 = QtGui.QFrame(self.tab)
        self.frame_3.setGeometry(QtCore.QRect(-10, 0, 1371, 21))
        self.frame_3.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"background-color: rgb(240, 80, 0);")
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_4 = QtGui.QPushButton(self.frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setDefault(False)
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_5 = QtGui.QPushButton(self.frame_3)
        self.pushButton_5.setDefault(False)
        self.pushButton_5.setFlat(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.pushButton_6 = QtGui.QPushButton(self.frame_3)
        self.pushButton_6.setDefault(False)
        self.pushButton_6.setFlat(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_3.addWidget(self.pushButton_6)
        spacerItem = QtGui.QSpacerItem(1141, 16, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.maintab.addTab(self.tab, "")
        self.t1 = QtGui.QWidget()
        self.t1.setObjectName("t1")
        self.frame_4 = QtGui.QFrame(self.t1)
        self.frame_4.setGeometry(QtCore.QRect(9, 9, 1381, 25))
        self.frame_4.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"background-color: rgb(240, 80, 0);")
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_state = QtGui.QPushButton(self.frame_4)
        self.pushButton_state.setDefault(False)
        self.pushButton_state.setFlat(True)
        self.pushButton_state.setObjectName("pushButton_state")
        self.horizontalLayout_4.addWidget(self.pushButton_state)
        self.pushButton_settings = QtGui.QPushButton(self.frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_settings.sizePolicy().hasHeightForWidth())
        self.pushButton_settings.setSizePolicy(sizePolicy)
        self.pushButton_settings.setDefault(False)
        self.pushButton_settings.setFlat(True)
        self.pushButton_settings.setObjectName("pushButton_settings")
        self.horizontalLayout_4.addWidget(self.pushButton_settings)
        spacerItem1 = QtGui.QSpacerItem(1141, 16, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.pushButton_CLEARCARD = QtGui.QPushButton(self.t1)
        self.pushButton_CLEARCARD.setGeometry(QtCore.QRect(1250, 550, 101, 21))
        self.pushButton_CLEARCARD.setCursor(QtCore.Qt.PointingHandCursor)
        self.pushButton_CLEARCARD.setMouseTracking(True)
        self.pushButton_CLEARCARD.setStyleSheet("background-color: rgb(153, 153, 153);")
        self.pushButton_CLEARCARD.setObjectName("pushButton_CLEARCARD")
        self.maintab.addTab(self.t1, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.scrollArea = QtGui.QScrollArea(self.tab_2)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 1201, 521))
        self.scrollArea.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollArea.setFrameShape(QtGui.QFrame.Box)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setMidLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -249, 2020, 1020))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_tab_main = QtGui.QFrame(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_tab_main.sizePolicy().hasHeightForWidth())
        self.frame_tab_main.setSizePolicy(sizePolicy)
        self.frame_tab_main.setMinimumSize(QtCore.QSize(2000, 1000))
        self.frame_tab_main.setMouseTracking(True)
        self.frame_tab_main.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_tab_main.setFrameShape(QtGui.QFrame.Box)
        self.frame_tab_main.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_tab_main.setLineWidth(1)
        self.frame_tab_main.setObjectName("frame_tab_main")
        self.verticalLayout_4.addWidget(self.frame_tab_main)
        self.verticalLayout.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.frame_tabd_3 = QtGui.QFrame(self.tab_2)
        self.frame_tabd_3.setGeometry(QtCore.QRect(1200, 0, 161, 521))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_tabd_3.sizePolicy().hasHeightForWidth())
        self.frame_tabd_3.setSizePolicy(sizePolicy)
        self.frame_tabd_3.setMinimumSize(QtCore.QSize(0, 1))
        self.frame_tabd_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_tabd_3.setFrameShape(QtGui.QFrame.Box)
        self.frame_tabd_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_tabd_3.setLineWidth(2)
        self.frame_tabd_3.setObjectName("frame_tabd_3")
        self.pushButton_CLEARCARD1_5 = QtGui.QPushButton(self.frame_tabd_3)
        self.pushButton_CLEARCARD1_5.setGeometry(QtCore.QRect(40, 490, 101, 21))
        self.pushButton_CLEARCARD1_5.setCursor(QtCore.Qt.PointingHandCursor)
        self.pushButton_CLEARCARD1_5.setMouseTracking(True)
        self.pushButton_CLEARCARD1_5.setStyleSheet("background-color: rgb(153, 153, 153);")
        self.pushButton_CLEARCARD1_5.setObjectName("pushButton_CLEARCARD1_5")
        self.groupBox_5 = QtGui.QGroupBox(self.frame_tabd_3)
        self.groupBox_5.setGeometry(QtCore.QRect(6, 10, 151, 121))
        self.groupBox_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.groupBox_5.setObjectName("groupBox_5")
        self.pushButton_12 = QtGui.QPushButton(self.groupBox_5)
        self.pushButton_12.setGeometry(QtCore.QRect(30, 23, 30, 30))
        self.pushButton_12.setAutoDefault(False)
        self.pushButton_12.setDefault(True)
        self.pushButton_12.setFlat(True)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtGui.QPushButton(self.groupBox_5)
        self.pushButton_13.setGeometry(QtCore.QRect(90, 23, 30, 30))
        self.pushButton_13.setAutoDefault(False)
        self.pushButton_13.setDefault(True)
        self.pushButton_13.setFlat(True)
        self.pushButton_13.setObjectName("pushButton_13")
        self.label_intervel_5 = QtGui.QLabel(self.groupBox_5)
        self.label_intervel_5.setGeometry(QtCore.QRect(30, 60, 101, 20))
        self.label_intervel_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_intervel_5.setObjectName("label_intervel_5")
        self.label_type_5 = QtGui.QLabel(self.frame_tabd_3)
        self.label_type_5.setGeometry(QtCore.QRect(10, 140, 141, 331))
        self.label_type_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_type_5.setObjectName("label_type_5")
        self.frame_subt_3 = QtGui.QFrame(self.tab_2)
        self.frame_subt_3.setGeometry(QtCore.QRect(0, 520, 1361, 61))
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
        self.pushButton_closecard_4 = QtGui.QPushButton(self.frame_subt_3)
        self.pushButton_closecard_4.setGeometry(QtCore.QRect(1230, 20, 101, 21))
        self.pushButton_closecard_4.setCursor(QtCore.Qt.PointingHandCursor)
        self.pushButton_closecard_4.setMouseTracking(True)
        self.pushButton_closecard_4.setStyleSheet("background-color: rgb(153, 153, 153);")
        self.pushButton_closecard_4.setObjectName("pushButton_closecard_4")
        self.pushButton_CLEARsub_3 = QtGui.QPushButton(self.frame_subt_3)
        self.pushButton_CLEARsub_3.setGeometry(QtCore.QRect(1110, 20, 101, 21))
        self.pushButton_CLEARsub_3.setCursor(QtCore.Qt.PointingHandCursor)
        self.pushButton_CLEARsub_3.setMouseTracking(True)
        self.pushButton_CLEARsub_3.setStyleSheet("background-color: rgb(153, 153, 153);")
        self.pushButton_CLEARsub_3.setObjectName("pushButton_CLEARsub_3")
        self.maintab.addTab(self.tab_2, "")
        MainWindo.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindo)
        self.statusbar.setObjectName("statusbar")
        MainWindo.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindo)
        self.maintab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindo)

    def retranslateUi(self, MainWindo):
        MainWindo.setWindowTitle(QtGui.QApplication.translate("MainWindo", "General SFP", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_LXI.setText(QtGui.QApplication.translate("MainWindo", "LXI (Simulated)", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_open_LXI.setText(QtGui.QApplication.translate("MainWindo", "open", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_PCI.setText(QtGui.QApplication.translate("MainWindo", "PCI (Simulated)", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_open_PCI.setText(QtGui.QApplication.translate("MainWindo", "open", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_PXI.setText(QtGui.QApplication.translate("MainWindo", "PXI (Simulated)", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_open_PXI.setText(QtGui.QApplication.translate("MainWindo", "open", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindo", "                                     Loading", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_refresh.setText(QtGui.QApplication.translate("MainWindo", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_search.setPlaceholderText(QtGui.QApplication.translate("MainWindo", "-- enter IP here --", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_add.setText(QtGui.QApplication.translate("MainWindo", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("MainWindo", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("MainWindo", "PXI Simulation", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_6.setText(QtGui.QApplication.translate("MainWindo", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.maintab.setTabText(self.maintab.indexOf(self.tab), QtGui.QApplication.translate("MainWindo", "main", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_state.setText(QtGui.QApplication.translate("MainWindo", "state", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_settings.setText(QtGui.QApplication.translate("MainWindo", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_CLEARCARD.setText(QtGui.QApplication.translate("MainWindo", "Clear card", None, QtGui.QApplication.UnicodeUTF8))
        self.maintab.setTabText(self.maintab.indexOf(self.t1), QtGui.QApplication.translate("MainWindo", "Tab 1", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_CLEARCARD1_5.setText(QtGui.QApplication.translate("MainWindo", "Clear card", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("MainWindo", "Multiuser Moniter", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_12.setText(QtGui.QApplication.translate("MainWindo", "ON", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_13.setText(QtGui.QApplication.translate("MainWindo", "OFF", None, QtGui.QApplication.UnicodeUTF8))
        self.label_intervel_5.setText(QtGui.QApplication.translate("MainWindo", "Intervel : 1000ms", None, QtGui.QApplication.UnicodeUTF8))
        self.label_type_5.setText(QtGui.QApplication.translate("MainWindo", "type:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_closecard_4.setText(QtGui.QApplication.translate("MainWindo", "Close card", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_CLEARsub_3.setText(QtGui.QApplication.translate("MainWindo", "clear sub", None, QtGui.QApplication.UnicodeUTF8))
        self.maintab.setTabText(self.maintab.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindo", "Page", None, QtGui.QApplication.UnicodeUTF8))

import pic_rc
