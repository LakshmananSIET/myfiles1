
from __future__ import print_function
from pilxi import *
import threading
import sys
import pilxi
import socket
import time
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtGui import QApplication, QMainWindow, QPushButton, QVBoxLayout, QFrame, QWidget,QLabel
from LXI_QT import *


class VVEE(Ui_MainWindo):
    def __init__(self, window):
        super(VVEE, self).__init__()
        self.setupUi(window)
        self.no=0
        self.size = 1
        self.cardsub=0
        self.t = 3
        self.af=0
        self.rows=4
        self.columns=10
        self.tt=0
        self.ff=0
        self.mm=1
        self.cardcf=0
        self.ipGet=0
        self.cards=3
        self.busf=[]
        self.devicef=[]
        self.cardf=[]
        self.serial=[]
        self.frames1=[]
        self.button1=[]
        self.column=[]
        self.row=[]
        self.maintab.tabBar().setVisible(False)
        self.maintab.setCurrentIndex(0)
        # self.pushButton.hide()
        self.pushButton_add.clicked.connect(self.line2)
        self.pushButton_refresh.clicked.connect(self.reff)
        self.pushButton_closecard_4.clicked.connect(self.clearc)
        self.pushButton_CLEARCARD1_5.clicked.connect(self.clearsub)
        self.pushButton_CLEARsub_3.clicked.connect(self.clearsub)
        # self.maintab.tabBar().setVisible(False)
        window.show()
        self.first()
        self.reff()

        # self.label_2.hide()
    def first(self) :
            self.pushButton_open_LXI.hide()
            self.label_LXI.setGeometry(QtCore.QRect(11, 16, 620, 20))
            self.label_LXI.setText("--no cards found--")
            self.pushButton_open_PXI.hide()
            self.label_PXI.setGeometry(QtCore.QRect(11, 16, 620, 20))
            self.label_PXI.setText("--no cards found--")
            self.pushButton_open_PCI.hide()
            self.label_PCI.setGeometry(QtCore.QRect(11, 16, 620, 20))
            self.label_PCI.setText("--no cards found--")
    def get_ip_address(self):
            hostname = socket.gethostname()
            self.ip_address = socket.gethostbyname(hostname)
            


    def get_ip_address1(self):
        try:
           self.ip_address=self.ip_address.split(".")
           
           i=150
           while(i!=0):
               self.ip_address1=(str(self.ip_address[0])+"."+str(self.ip_address[1])+"."+str(self.ip_address[2])+"."+str(i))
               if self.ipGet==1:
                    self.ipGet=0
                    break
               self.line1()
               i=i-1
                
                
             
        except:
           print("pass")
           pass

   
        
    def reff(self):
        self.tt=0
        self.ipGet=0
        self.completed = 0
        self.label_details.setText("")
        self.deleteFrames()
        self.label_2.show()

        while self.completed < 100:
 
            self.completed += 0.0001
            self.progressBar.setValue(self.completed)
        # self.disc()
        self.get_ip_address()
        self.get_ip_address1()
        
   
        self.label_2.hide()   
    
        print("ref")
    
    def deleteFrames(self):
        for self.frame in self.frames1:
            if self.frame is not self.frame_LXI:  # Skip deleting self.frame_LXI
                self.frame.setParent(None)
                self.frame.deleteLater()
        self.frames1 = []

    def deletebutton(self):
        for self.pushButton_tab in self.button1:
            # if self.frame is not self.frame_LXI:  # Skip deleting self.frame_LXI
                self.pushButton_tab.setParent(None)
                self.pushButton_tab.deleteLater()
        self.button1 = []

    def line2(self):

        
        
        self.completed = 0
        self.ip_address1 =self.lineEdit_search.text()

        # Default listening port 9999
        if len(self.ip_address1) >0:
            self.deleteFrames()
              
            while self.completed < 100:
                self.completed += 0.0001
                self.progressBar.setValue(self.completed)
            self.tt=1    
            self.line1()             
        else:
             self.message_ip_not()

        
    def line1(self):

        
        try: 
           
            print(str(self.ip_address1))
            session = pilxi.Pi_Session(self.ip_address1)
            self.ip_subtype=self.ip_address1
            cards = session.FindFreeCards()
            index = 1
          
            if len(cards) > 0:
                self.af=len(cards)
                print("Found cards:")
                self.busf=[]
                self.devicef=[]
                self.cardf=[]
                self.serial=[]
                self.frames1=[]

                self.ipGet=1
                for cardLocation in cards:

                    bus, device = cardLocation
                    card = session.OpenCard(bus, device)

                    cardID = card.CardId()

                    cardID=cardID.split(",")

                    print(index)
                
                    print(bus)
                    self.busf.append(bus)
                    print(device)
                    
                    self.devicef.append(device)
                    print(cardID[0])
                    self.cardf.append(cardID[0])
                    print(cardID[1])
                    self.serial.append(cardID[1])
                    index += 1
                

                self.scroll()
                self.addFrames()
           
                # self.ip_chech()
                     

         
        except:
             print("Found no cards.")
             if self.tt==1:
                   self.ip_chech()
                  
             pass        
       

    def printf(self):
        print("Button clicked")

    def handleButtonClick(self, button):
        self.button_id = button.property("id")
        print(" mini Button clicked:", self.button_id)

        self.deletebutton()
        self.subunitType()
        self.maintab.setCurrentIndex(2)

    def tabbuttonClick1(self, button):
        self.button_id3 = button.property("btn_no")
        print(" Button clicked:", self.button_id3)
                                                                                                # for self.pushButton_tab in self.button1:
                                                                                                #     if self.pushButton_tab.isChecked():
                                                                                                #         print("Button is checked")
                                                                                                #         # self.pushButton_tab.setCheckable(False)
                                                                                                #         self.close=0
                                                                                                #         self.pushButton.setStyleSheet("background-color: rgb(117, 223, 255);")
                                                                                                 #         break
                                                                                                #     else:
                                                                                                #         self.close=1
                                                                                                
                                                                                                #         print("Button is not checked")
        self.mm=1
        self.callbutton()

    def callbutton(self):
        
        
      
        if __name__ == "__main__":
            print("pilxi wrapper version: {}".format(pilxi.__version__))
            # Connect to a chassis using an IP address.
            # The ClientBridge driver can also connect to local PXI chassis by passing
            # 'PXI' in place of the IP.
            IP_Address =  self.ip_subtype

            bus = self.busf[self.button_id-1]
            device = self.devicef[self.button_id-1]
            
            port = 1024
            timeout = 1000

          
            
            subunit = 1

            # print("Sample program for Pickering LXI/PXI 40-584-001 2x128 Matrix cards using PILXI ClientBridge Python Wrapper")
            # print("Connecting to chassis at ", IP_Address)

            # Open a session with LXI device
            session = pilxi.Pi_Session(IP_Address, port, timeout)

            try:
                # Open the card
                card = session.OpenCard(bus, device)

            except pilxi.Error as ex:
                print("Error occurred: {}".format(ex.message))
                exit()

            # Get the card ID and an error code
            cardId = card.CardId()

            # print("Successfully connected to card at bus", bus, "device", device)
            # print("Card ID: ", cardId)

            # print("Clearing subunit", subunit)
            # card.ClearSub() de-energises all outputs on a specified subunit
            card.ClearSub(subunit)
            
            
            if self.cardcf==1:
                for self.pushButton_tab in self.button1:
                    if self.pushButton_tab.isChecked():
                        print("Button is checked")
                        self.pushButton_tab.setCheckable(False)
                self.deletebutton()
                self.column=[]
                self.row=[]     
                self.cardcf=0
                print("Clearing outputs and closing card...")
                card.ClearSub(subunit)

                # Close the card before exiting the program
                card.Close()

                # Close the LXI session
                session.Close()
                self.maintab.setCurrentIndex(0)
                exit
            else:
                if self.cardsub==1 : 
                    card.ClearSub(subunit)
                    self.cardsub=0
                    for self.pushButton_tab in self.button1:
                        if self.pushButton_tab.isChecked():
                            print("Button is checked")
                            self.pushButton_tab.setCheckable(False)
                            self.pushButton_tab.setCheckable(True)

                else:
                    i=0
                    self.button_id3=self.button_id3.split(",")
                    rr=int(self.button_id3[0])
                    cc=int(self.button_id3[1])
                    print(rr)
                    print(cc)
                    if self.ff==1:
                        self.ff=1

                        for i in range(0,len(self.row)):
                        
                            # print(i)
                            # print(self.row[i])
                            # print(rr)
                            # print(self.column[i])
                            # print(cc)
                            if self.column[i] ==cc and self.row[i] ==rr:

                                print(",,,,,,,,,,,,,,,,,,,,,delete,,,,,,,,,,,,,,,,,")
                                # print("row=",self.row[i], "-","col=", self.column[i])
                                state = 0
                                card.SetCrosspointRange(subunit, self.row[i], self.column[i],self.column[i], state)
                                # card.OpCrosspoint(subunit, self.row[i], self.column[i], state)
                                # print(state)
                                self.mm=0
                                self.row.pop(i)
                                self.column.pop(i)
                                break
                        
                    # print(self.row)
                    # print(self.column)
                    if self.mm==1:
                        self.row.append(int(self.button_id3[0]))
                        self.column.append(int(self.button_id3[1]))
                    # print(len(self.row))
                    # print(len(self.column))
                
                
                    for i in range(0,len(self.row)):
                            self.ff=1
                            # print(self.row)
                            # print(self.column)
                            # print(i)
                            
                            print(",,,,,,,,,,,,,,,,,,add,,,,,,,,,,,,,,,,,,,,,,")
                            # print("Switching range",self.row[i], "-","on row", self.column[i])

                            state = 1
                            card.SetCrosspointRange(subunit, self.row[i], self.column[i],self.column[i], state)
                            # card.OpCrosspoint(subunit, self.row[i], self.column[i], state)
                    # print(state)
                
                


                
                            
           
    def clearc(self):
          self.cardcf=1
          self.callbutton()
    def clearsub(self):  
         self.cardsub=1    
         self.callbutton()  
      
       
    def handleButtonClick1(self, button): 
        self.button_id1 = button.property("id1")  

        # self.frame = button.parent()
        # self.pushButton1 = self.frame.findChild(QPushButton)
        for i in range(0,self.af):
          if self.button_id1==i+1:
            print("Button clicked111:", self.button_id1)
            self.label_details.setText("Model:  "+str(self.cardf[i])+"\n\n"+"Revision:  1.00\n\n"+"Bus:  "+str(self.busf[i])+"\n\nDevice:  "+str(self.devicef[i]))
         

    # def btext(self) :  
    #     self.button_id1=1
    #     self.pushButton1 = self.frame.findChild(QPushButton)
    #     for i in range(5):
    #       if self.button_id1==i:
    #         print("Button clicked!!:", self.button_id1)
    #         self.pushButton1.setText("device"+str(i)) 
    #         self.button_id1+=1
     
    def scroll(self):
        self.label_2.hide()
        if self.t==1:
           
            self.frame_PCI.hide()
            self.pushButton_open_LXI.hide()
            self.label_LXI.setGeometry(QtCore.QRect(11, 16, 620, 20))
            self.label_LXI.setText("--no cards found--")
            self.pushButton_open_PXI.hide()
            self.label_PXI.setGeometry(QtCore.QRect(11, 16, 620, 20))
            self.label_PXI.setText("--no cards found--")
            self.scrollArea_PCI.setGeometry(QtCore.QRect(10, 10, 671, 270))  
            self.scrollArea_PXI.setGeometry(QtCore.QRect(10, 280, 671, 115))
            self.scrollArea_LXI.setGeometry(QtCore.QRect(10, 395, 671, 115))
        if self.t==2:
            self.frame_pxi.hide()
            self.pushButton_open_PCI.hide()
            self.label_PCI.setGeometry(QtCore.QRect(11, 16, 620, 20))
            self.label_PCI.setText("--no cards found--")
            self.pushButton_open_LXI.hide()
            self.label_LXI.setGeometry(QtCore.QRect(11, 16, 620, 20))
            self.label_LXI.setText("--no cards found--")
            self.scrollArea_PCI.setGeometry(QtCore.QRect(10, 10, 671, 115))  
            self.scrollArea_PXI.setGeometry(QtCore.QRect(10, 125, 671, 270))
            self.scrollArea_LXI.setGeometry(QtCore.QRect(10, 395, 671, 115))
        if self.t==3:
            self.frame_LXI.hide()
            self.pushButton_open_PCI.hide()
            self.label_PCI.setGeometry(QtCore.QRect(11, 16, 620, 20))
            self.label_PCI.setText("--no cards found--")
            self.pushButton_open_PXI.hide()
            self.label_PXI.setGeometry(QtCore.QRect(11, 16, 620, 20))
            self.label_PXI.setText("--no cards found--")
            self.scrollArea_PCI.setGeometry(QtCore.QRect(10, 10, 671, 115))  
            self.scrollArea_PXI.setGeometry(QtCore.QRect(10, 125, 671, 115))
            self.scrollArea_LXI.setGeometry(QtCore.QRect(10, 240, 671, 270))
    
    # def listcard(self):
        
    def  addFrames(self):
       
                     
                    for i in range(0,self.af):
                                    
                                    
                                    
                                    self.frame = QFrame()
                                    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
                                    sizePolicy.setHorizontalStretch(0)
                                    sizePolicy.setVerticalStretch(0)
                                    sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
                                    self.frame.setSizePolicy(sizePolicy)
                                    self.frame.setMinimumSize(QtCore.QSize(652, 40))
                                    self.frame.setFrameShape(QtGui.QFrame.Box)
                                    self.frame.setFrameShadow(QtGui.QFrame.Raised)
                                    self.frame.setObjectName("self.frame_LXI"+str(i)) 
                                    self.frames1.append(self.frame)
                                    self.verticalLayout_5.addWidget(self.frame)

                                    print( self.frames1)


                                    
                                    self.pushButton = QPushButton(self.frame)
                                    self.pushButton.setGeometry(QtCore.QRect(0, 0, 652, 40))
                                    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
                                    sizePolicy.setHorizontalStretch(0)
                                    sizePolicy.setVerticalStretch(13)
                                    sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
                                    self.pushButton.setSizePolicy(sizePolicy)
                                    self.pushButton.setStyleSheet("background-color: rgb(117, 223, 255);")
                                    self.pushButton.setAutoDefault(False)
                                    self.pushButton.setDefault(True)
                                    self.pushButton.setFlat(True)
                                    self.pushButton.setObjectName("self.pushButton_open_LXI1" + str(i))
                                    self.pushButton.setText("Model:"+str(self.cardf[i])+"  S/N:"+str(self.serial[i]))    
                                    self.pushButton.setProperty("id1", i + 1)
                                    self.pushButton.clicked.connect(lambda btn=self.pushButton: self.handleButtonClick1(btn))

                                    self.pushButton = QPushButton(self.frame)
                                    self.pushButton.setGeometry(QtCore.QRect(10, 10, 75, 23))
                                    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
                                    sizePolicy.setHorizontalStretch(0)
                                    sizePolicy.setVerticalStretch(13)
                                    sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
                                    self.pushButton.setSizePolicy(sizePolicy)
                                    self.pushButton.setStyleSheet("background-color: rgb(209, 209, 209);")
                                    self.pushButton.setAutoDefault(False)
                                    self.pushButton.setObjectName("self.self.pushButton_open_LXI1" + str(i))
                                    self.pushButton.setProperty("id", i + 1)
                                    self.pushButton.clicked.connect(lambda btn=self.pushButton: self.handleButtonClick(btn))
                                    self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "open", None, QtGui.QApplication.UnicodeUTF8))

                                    self.frame.show()
                                    # self.frames.append(self.frame)
    
    def subunitType(self):
        
         if __name__ == "__main__":

            print("pilxi wrapper version: {}".format(pilxi.__version__))    
            IP_Address =  self.ip_subtype

            bus = self.busf[self.button_id-1]
            device = self.devicef[self.button_id-1]
            print(IP_Address)
            print(bus)
            print(device)

            try:
             
                session = pilxi.Pi_Session(IP_Address)

                card = session.OpenCard(bus, device)

            except pilxi.Error as ex:
                print("Error occurred: {}".format(ex.message))
                exit()

            print("Sample program for manipulating subunit states on Pickering Matrix Cards using the PILXI Python Wrapper")
            print()

            cardId = card.CardId()

            print("Successfully connected to specified card.")
            print("Card ID: ", cardId)

       
            subunit = 1
            

    
            typeNum, rows, columns = card.SubInfo(subunit, True)
            subType = card.SubType(subunit, 1)
            print("Rows: {}\nColumns: {}".format(rows, columns))
            print("Card subunit type: {}".format(subType))
            self.rows=rows
            self.columns=columns
            self.buttoncreate()
            # self.maintab.setCurrentIndex(2)

    def message_ip_not(self):
           
            msg = QMessageBox()
            msg.setWindowTitle('IP_ADDRESS')
            msg.setText('-- enter ip here --')
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()

    def ip_chech(self):
           
            msg = QMessageBox()
            msg.setWindowTitle('IP_ADDRESS')
            msg.setText('-- connection time out--')
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()


    def buttoncreate(self):
        self.button1=[]
    
        print("button")
     
        r1=70
        # c=1230
        # r=550
        for i in range(1,self.rows+1):
         
            c1=20
            r1=r1+40
            print(i)
            for j in range(1,self.columns+1):
                    # print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
                    # print(c1)
                    # print(r1)
                    # print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
                    # if c1>1230:
                    #     self.frame_tab_main.setMinimumSize(QtCore.QSize(c1+50, r1))
                      
                    # if r1>550:
                    
                    #     self.frame_tab_main.setMinimumSize(QtCore.QSize(c1, r1+50))
                    # # name=(self.t+str(self.button_id))
                    t=(str(i)+","+str(j))
                    # print(name)
                    # self.pushButton_tab = QtGui.QPushButton(self.t1)
                    self.pushButton_tab = QtGui.QPushButton(self.frame_tab_main)

                    self.pushButton_tab.setGeometry(QtCore.QRect(c1, r1, 40, 40))
                    self.pushButton_tab.setStyleSheet("background-color: rgb(104, 104, 104);")
                    self.pushButton_tab.setCursor(QtCore.Qt.PointingHandCursor)
                    self.pushButton_tab.setAutoDefault(True)
                    self.pushButton_tab.setObjectName("pushButton")
                    self.pushButton_tab.setProperty("btn_no",t )
                    self.pushButton_tab.clicked.connect(lambda btn= self.pushButton_tab: self.tabbuttonClick1(btn))
                    self.pushButton_tab.setCheckable(True)
                    self.pushButton_tab.setText(str(i)+"."+str(j))   
                    self.button1.append(self.pushButton_tab)
                    c1=c1+40
    
                 
                 





app = QApplication(sys.argv)
mainWindow = QMainWindow()
ui = VVEE(mainWindow)
mainWindow.show()
sys.exit(app.exec_())
