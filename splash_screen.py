
# with open("D:\QT\lxi_files\maya.txt","a") as file:
  
#     print(file.append("hii lax "))
#     file.close()

# import sys
# from PySide.QtCore import Qt, QTimer
# from PySide.QtGui import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget

# import sys
# from PySide import QtGui, QtCore

# class SplashScreen(QtGui.QMainWindow):
#     def __init__(self):
#         super(SplashScreen, self).__init__()  # Provide the class and instance as arguments
#         self.setWindowTitle("Splash Screen")
#         self.central_widget = QtGui.QWidget()
#         self.layout = QtGui.QVBoxLayout()
#         self.label = QtGui.QLabel("Splash Screen\nLoading...")
#         self.layout.addWidget(self.label)
#         self.central_widget.setLayout(self.layout)
#         self.setCentralWidget(self.central_widget)

# class MainWindow(QtGui.QMainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()  # Provide the class and instance as arguments
#         self.setWindowTitle("Main Window")
#         self.central_widget = QtGui.QWidget()
#         self.layout = QtGui.QVBoxLayout()
#         self.label = QtGui.QLabel("Main Window")
#         self.layout.addWidget(self.label)
#         self.central_widget.setLayout(self.layout)
#         self.setCentralWidget(self.central_widget)

# if __name__ == "__main__":
#     app = QtGui.QApplication(sys.argv)

#     splash_screen = SplashScreen()
#     splash_screen.show()
   
#     # Simulate some initialization delay (e.g., 3 seconds)
#     QtCore.QTimer.singleShot(3000, splash_screen.close)

#     main_window = MainWindow()
#     main_window.show()

#     sys.exit(app.exec_())
import matplotlib.pyplot as plt

# Sample data for multiple waves
x = [0, 1.1400000000000023, ]
y1 =[1, 1]  # Sample y-values for the first wave
y2 = [0 ,53.900000000000006]  # Sample y-values for the second wave
y3 = [2, 2]  # Sample y-values for the third wave

# Create a line plot for each wave
plt.plot(x, y1 , label='Wave 1')
plt.plot(y2,y3 ,label='Wave 2')
# plt.plot(x, y3, label='Wave 3')

# Adding labels, title, legend, and grid
plt.xlabel('X-axis')
plt.ylabel('Amplitude')
plt.title('Multiple Waves from Lists')
plt.legend()
plt.grid(True)

# Display the plot
plt.show()
