# from PySide.QtGui import *
# from PySide.QtCore import *
# import sys


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()

#         self.tab_widget = QTabWidget(self)
#         self.setCentralWidget(self.tab_widget)

#         self.create_main_tab()

#     def create_main_tab(self):
#         main_tab = QWidget()
#         layout = QVBoxLayout()
#         self.line_edit = QLineEdit()
#         self.start_button = QPushButton("Start")
#         self.start_button.clicked.connect(self.create_buttons)
#         layout.addWidget(self.line_edit)
#         layout.addWidget(self.start_button)
#         main_tab.setLayout(layout)

#         self.tab_widget.addTab(main_tab, "Main Tab")

#     def create_buttons(self):
#         num_buttons = int(self.line_edit.text())

#         for i in range(num_buttons):
#             new_tab = QTabWidget()
#             new_tab.setTabPosition(QTabWidget.West)
#             self.tab_widget.addTab(new_tab, "New Tab {}".format(i + 1))

#             for j in range(4):
#                 subtab = QWidget()
#                 layout = QVBoxLayout()
#                 label = QLabel("Subtab Content {}".format(j + 1))
#                 layout.addWidget(label)
#                 subtab.setLayout(layout)
#                 new_tab.addTab(subtab, "Subtab {}".format(j + 1))

#     def create_subtab(self):
#         sender_button = self.sender()
#         subtab_widget = self.tab_widget.currentWidget().currentWidget()
#         new_subtab = QWidget()
#         layout = QVBoxLayout()
#         label = QLabel("Subtab Content")
#         layout.addWidget(label)
#         new_subtab.setLayout(layout)
#         subtab_widget.addTab(new_subtab, "Subtab {}".format(subtab_widget.count() + 1))


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

# from PySide.QtGui import *
# from PySide.QtCore import *
# import sys


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()

#         self.tab_widget = QTabWidget(self)
#         self.setCentralWidget(self.tab_widget)

#         self.create_main_tab()

#     def create_main_tab(self):
#         main_tab = QWidget()
#         layout = QVBoxLayout()
#         self.line_edit = QLineEdit()
#         self.start_button = QPushButton("Start")
#         self.start_button.clicked.connect(self.create_buttons)
#         layout.addWidget(self.line_edit)
#         layout.addWidget(self.start_button)
#         main_tab.setLayout(layout)

#         self.tab_widget.addTab(main_tab, "Main Tab")

#     def create_buttons(self):
#         num_buttons = int(self.line_edit.text())
#         button_layout = QVBoxLayout()

#         for i in range(num_buttons):
#             button = QPushButton("Button {}".format(i + 1))
#             button.setFixedSize(80, 40)
#             button.clicked.connect(self.create_new_tab)
#             button_layout.addWidget(button)

#         new_tab = QWidget()
#         new_tab.setLayout(button_layout)

#         self.tab_widget.addTab(new_tab, "New Tab")

#     def create_new_tab(self):
#         sender_button = self.sender()
#         new_tab = QTabWidget()
#         subtab = QWidget()
#         layout = QVBoxLayout()
#         line_edit = QLineEdit()
#         start_button = QPushButton("Start 2")
#         start_button.clicked.connect(self.create_subtab)
#         layout.addWidget(line_edit)
#         layout.addWidget(start_button)
#         subtab.setLayout(layout)
#         new_tab.addTab(subtab, "{} Subtab".format(sender_button.text()))
#         self.tab_widget.addTab(new_tab, "{} - New Tab".format(sender_button.text()))

#     def create_subtab(self):
#         sender_button = self.sender()
#         subtab_widget = self.tab_widget.currentWidget().currentWidget()
#         new_subtab = QWidget()
#         layout = QVBoxLayout()
#         label = QLabel("Subtab Content")
#         layout.addWidget(label)
#         new_subtab.setLayout(layout)
#         subtab_widget.addTab(new_subtab, "Subtab {}".format(subtab_widget.count() + 1))


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())
from PySide.QtGui import QApplication, QMainWindow, QWidget, QTabWidget, QVBoxLayout, QPushButton, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.lax = QWidget(self)
        self.lax.setObjectName("lax0")

        self.tabWidgetlax = QTabWidget(self.lax)
        self.tabWidgetlax.setGeometry(0, 0, 1370, 550)
        self.tabWidgetlax.setObjectName("tabWidgetlax")

        self.button_add = QPushButton("Add Tab")
        self.button_add.clicked.connect(self.addTab)

        self.button_delete_all = QPushButton("Delete All Tabs")
        self.button_delete_all.clicked.connect(self.deleteAllTabs)

        layout = QVBoxLayout()
        layout.addWidget(self.tabWidgetlax)
        layout.addWidget(self.button_add)
        layout.addWidget(self.button_delete_all)
        self.lax.setLayout(layout)

        self.setCentralWidget(self.lax)
        self.setWindowTitle('Dynamic Tabs')

    def addTab(self):
        new_tab = QWidget()
        label = QLabel("New Tab")
        new_tab.layout = QVBoxLayout()
        new_tab.layout.addWidget(label)
        new_tab.setLayout(new_tab.layout)
        self.tabWidgetlax.addTab(new_tab, "Tab")

    def deleteAllTabs(self):
        while self.tabWidgetlax.count() > 0:
            tab_index = self.tabWidgetlax.count() - 1
            print(tab_index)
            tab_to_delete = self.tabWidgetlax.widget(tab_index)
            self.tabWidgetlax.removeTab(tab_index)
            tab_to_delete.deleteLater()


if __name__ == '__main__':
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()
