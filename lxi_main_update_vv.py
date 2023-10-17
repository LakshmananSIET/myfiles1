from __future__ import print_function
from pilxi import *
import threading
import sys
import pilxi
import socket
import time
from collections import OrderedDict
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtGui import QApplication, QMainWindow, QPushButton, QVBoxLayout, QFrame, QWidget,QLabel
from LXI_QT_update import *


class VVEE(Ui_MainWindo):
    def __init__(self, window):
        super(VVEE, self).__init__()
        self.setupUi(window)
      
        self.mdi = QtGui.QMdiArea()
        self.count = 0
        self.cardsf=0
        self.rescheck=1
        self.cardsub=0
        self.t = 3
        self.af=0
        self.newlist=[]
        self.rows=4
        self.lcdinf=[]
        self.close=[]
        self.columns=10
        self.SW=0
        self.tt=0
        self.ff=0
        self.mm=1
        self.m=4
        self.finalbutton=[]
        self.tabmain=[]
        self.cardcf=0
        self.ipGet=0
        self.cards=3
        self.subinfo=[]
        self.subinFoAdv=[]
        self.output=[]
        self.subinfo_main=[]
        self.row_main=[]
        self.column_main=[]
        self.busf=[]
        self.devicef=[]
        self.cardf=[]
        self.subunitinf=[]
        self.serial=[]
        self.frames1=[]
        self.button1=[]
        self.column=[]
        self.listind=[]
        self.description=[]
        self.pushButton_LXIt=[]
        self.row=[]
        self.ipind=[]
        self.tabadd=[]
        self.maintab.tabBar().setVisible(False)
        self.maintab.setCurrentIndex(0)

       
        self.pushButton_add.clicked.connect(self.line2)
        self.pushButton_refresh.clicked.connect(self.second_ip)
   
        
        window.show()
        self.first()
        print("wellcome")
        self.second_ip()


    def second_ip(self):
        self.first()
        self.no=1
        self.tt==0
        self.rescheck=1
        self.subinfo=[]
        self.output=[]
        self.subunitinf=[]
        self.finalbutton=[]
        # self.tabadd=[]
        self.CARDRES=0
        self.subinfo_main=[]
        self.row_main=[]
        self.column_main=[]
        self.busf=[]
        self.devicef=[]
        self.cardf=[]
        self.serial=[]
        self.lcdinf=[]
        self.button1=[]
        self.column=[]
        self.listind=[]
        self.description=[]
        self.row=[]
        self.ipind=[]
        self.b_input_var1=[]
       
        self.deleteFrames()
        self.completed = 0
        while self.completed < 100:
 
            self.completed += 0.00001
            self.progressBar.setValue(self.completed)

        base = pi_base()


        listeningport = 9999

        timeout = 2000

        err,val = base.EchoBroadcast(listeningport ,timeout)
        if (err !=0):
            print ("err ", err)
            self.pushButton_LXI.setText("No LXI Devices found")
            # self.ip_chech()
            self.first()
            
            return
            print("hii")
         
        else:
            self.pushButton_LXI.hide()
            print ("Number of LXI's availabe:  ", val)

        #Get the number of LXIs available
        ret = base.GetAvailableLXICount()

        #Information for LXIs in the range
        for x in range(0,ret):
            err, listenport, listenport, clientcount, opencardcount, description, address = base.GetAvailableLXIEntryEx(x)
            print ("IP Address: ", address.decode("utf-8"), "Description:  ", description.decode("utf-8"))
            if self.tt==0:
                
                    description= description.split(",")
                    self.description.append(description)
                    # self.pushButton_LXI.setText("LXI "+str( description[0])+"S/N: "+str( description[1]))
                    self.b_input_var1.append(address)
                   
            if self.tt==1:
                print(self.ip_address1)
                print("user ip")
                if address==self.ip_address1:
                  
                    description=  description.split(",")
                    self.description.append(description)
                    # self.pushButton_LXI.setText("LXI "+str( description[0])+"S/N: "+str( description[1]))
                    self.b_input_var1.append(address)
                    self.tt=0
                    break
            

        
        for index,  b_input_var in enumerate(self.b_input_var1):
        
        
                
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print(b_input_var)
            print()
            print()
            # Initialize the comm module
            comm = pi_comm(0, b_input_var, 1024, 1000)

            # Gets the version of ServerBridge
            ver = comm.SbVersion()
            print("Serverbridge Version on LXI:", ver)

            # Gets the the card count
            err, count = comm.CountFreeCards()
            err, bus, slot = comm.FindFreeCards(count)
            print("Error:", err, "Card count:", count)
            # self.af=count

            print("--------------------------------")

            cardnum = 0
            # If during init the value of mode is zero them the paramA and paramB can be treated as bus and slot
            # If the value of mode is non-zero then ParamA will be cardnum and paramB will be accessType

            mode = 0  # Last two parameters treated as bus and slot
            while cardnum < count:
                self.listind.append(cardnum)
                self.ipind.append(index)
                card = pi_card(0, b_input_var, 1024, 1000, mode, bus[cardnum], slot[cardnum])

                err, cid = card.CardId()
                if err != 0:
                    print(err)
                    ret, errmsg = card.ErrorCodeToMessage(err)
                    print("Error: ", errmsg, "-", err)

                print("Bus ", bus[cardnum], "Slot ", slot[cardnum])
                self.busf.append(bus[cardnum])
                self.devicef.append(slot[cardnum])
                print("ID = ", cid.decode("utf-8"))
                cid=cid.split(",")
                print(cid[0])
                self.cardf.append(cid[0])
                print(cid[1])
                self.serial.append(cid[1])
                e, ins, outs = card.EnumerateSubs()
                print("subunits: ", ins, "input, ", outs, "output")
                sf="subunits: "+str(ins)+"  input "+str(outs)+"  output"
                self.subunitinf.append(sf)
                self.output.append(int(outs))
                print("--------------------------------")
                sub = 1
                while sub <= outs:

                    err, inf = card.SubType(sub, 1)
                    if err != 0:
                        print(err)
                        ret, errmsg = card.ErrorCodeToMessage(err)
                        print("Error: ", errmsg, "-", err)
                    else:
                        print("subunit ", sub, " = ", inf)
                        self.subinfo.append(inf)
                        print(inf.split('(')[0])
                        if inf.split('(')[0] =="RES":
                            self.CARDRES=cardnum
                        err, subType, rows, cols = card.SubInfo(sub, 1)
                        print("-----------------------------------------------------")
                        print(subType)
                        print(sub)
                        self.row.append(int(rows))
                        print(rows)
                        self.column.append(int(cols))
                        print(cols)
                   
                        sub = sub + 1

                cardnum = cardnum + 1
              
             

                print(".................................................................................")

                unique_words = list(OrderedDict.fromkeys(self.subinfo))
                print(unique_words)
                self.subinFoAdv.append(unique_words)
                print(".................................................................................")

                self.subinfo_main.append(self.subinfo)
                self.row_main.append(self.row)
                self.column_main.append(self.column)   
                self.subinfo=[]    
                self.row=[]
                self.column=[] 
    
                card.CloseCards()
                
            print(self.subinfo_main)
            print(self.row_main)
            print(self.column_main)
            print(self.output)
            print(self.listind)
            print(self.ipind)
            print(self.subinFoAdv)
            print( self.subunitinf)
            comm.Disconnect()
        self.af=len(self.output)

        self.scroll()
        # self.resiter_control()
    def deleteFrames(self):
        print("/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        for self.pushButton_LXI1 in self.pushButton_LXIt:
            # if self.frame is not self.frame_LXI:  # Skip deleting self.frame_LXI
            self.pushButton_LXI1.setParent(None)
            self.pushButton_LXI1.deleteLater()
        self.pushButton_LXIt = []

        for self.frame in self.frames1:
            # if self.frame is not self.frame_LXI:  # Skip deleting self.frame_LXI
            self.frame.setParent(None)
            self.frame.deleteLater()
        self.frames1 = []
        self.deletebutton()

        
        if len(self.tabadd)>0:
            print(self.tabmain)
            print(self.tabadd)
            for  i in range(len(self.tabadd)-1,-1,-1):
            # if self.frame is not self.frame_LXI:  # Skip deleting self.frame_LXI
                print(i,"/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
                tab_to_delete = self.tabadd[i]
                self.tabWidgetlax.removeTab(i)
                self.tabadd.remove(tab_to_delete)
                tab_to_delete.deleteLater()
            self.tabmain= []
            self.tabadd= []



    
    def buttonHead(self,i):
            self.pushButton_LXI1 = QtGui.QPushButton(self.scrollAreaWidgetContents_5)
            self.pushButton_LXI1.setMinimumSize(QtCore.QSize(0, 40))
            font = QtGui.QFont()
            font.setWeight(75)
            font.setBold(True)
            self.pushButton_LXI1.setFont(font)
            self.pushButton_LXI1.setStyleSheet("QPushButton\n"
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
            self.pushButton_LXI1.setAutoDefault(False)
            self.pushButton_LXI1.setDefault(False)
            self.pushButton_LXI1.setFlat(False)
            self.pushButton_LXI1.setObjectName("pushButton_LXI")
            self.pushButton_LXI1.setProperty("mbtn", i + 1)
            self.pushButton_LXI1.clicked.connect(lambda btn= self.pushButton_LXI1: self.mainButtonClick1(btn))
            t=str(self.description[i][0])
            t1=str(self.description[i][1])
            self.pushButton_LXI1.setText("LXI   "+str(t[1:-1])+"   S/N   "+str(t1[1:-1])+"   IP:   "+str(self.b_input_var1[i]))
            self.verticalLayout_5.addWidget(self.pushButton_LXI1)
            self.pushButton_LXIt.append(self.pushButton_LXI1)

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
    
    # def deleteFrames(self):
    #     for self.frame in self.frames1:
    #         if self.frame is not self.frame_LXI:  # Skip deleting self.frame_LXI
    #             self.frame.setParent(None)
    #             self.frame.deleteLater()
    #     self.frames1 = []

    def deletebutton(self):
        print(self.finalbutton)
        for self.button1 in self.finalbutton:
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
            self.second_ip()           
        else:
             self.message_ip_not()

        
   
       

    def printf(self):
        print("Button clicked")

    def handleButtonClick(self, button):
        self.button_id = button.property("id")
        print(" mini Button clicked:", self.button_id)

        # self.deletebutton()
       
       
        self.tabcreat()
   
    def tabbuttonclear(self, button):
        print(self.close)
        self.button = button.property("btn_clear")
        print(" mini Button clicked:", self.button)
        # self.deletebutton()
        self.button=self.button.split(",")
        self.clearsub()
     
    def tabbuttonclose(self, button):
        self.button = button.property("btn")
        print(" mini Button clicked:", self.button)
        print(self.close)
        for i in  self.close:
            self.button=i
            self.button=self.button.split(",")
            print("close card///////////////////////////")
            print(self.button)
            print( self.button_id)
            print(self.subinfo_main[ self.button_id-1])
            self.clearsub()
        self.maintab.setCurrentIndex(0)
        self.close=[]
          
    

    def mainButtonClick1(self,button):
        self.button_id_main = button.property("mbtn")
        i=self.button_id_main-1
        print(" mini Button clicked:", self.button_id_main)
        t=str(self.description[i][0])
        t1=str(self.description[i][1])
     
        self.label_details.setText("Model: "+str(t[1:-1])+"\n\n"+"Serial Number: "+str(t1[1:-1])+"\n\n"+"IP address: "+str(self.b_input_var1[i]))
         

    def tabbuttonClick1(self, button):
        self.inf=0
        self.button_id3 = button.property("btn_no")
        print(" Button clicked:::::::::::", self.button_id3)
        self.button_id3=self.button_id3.split(",")
        self.inf=self.button_id3[0]
        print(self.inf)
        self.rc=self.button_id3[1]
        self.inf= self.inf.split(".")
        print(self.inf)
        print(self.rc)
        print(self.subinfo_main[ int(self.inf[0])-1][ int(self.inf[1])-1])       
        n=self.subinfo_main[ int(self.inf[0])-1][ int(self.inf[1])-1].split('(')[0] 
        print(n)                                                         
        self.mm=1
        self.callbutton()

   

                
    def callbutton(self):
        
        if self.cardsub==1 :
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< card close<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            n1=int(self.ipind[int(self.button[0])-1])
            b_input_var= self.b_input_var1[n1]
        else:
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< button <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            n=int(self.inf[0])
            print(n)
            n1=int(self.ipind[n-1])
            b_input_var= self.b_input_var1[n1]
            s=int(self.inf[1])
            c=int(self.inf[0])
            print(c)
            print(s)
        
        # b_input_var='192.168.0.139'
            
        print(b_input_var)

# Initialize the comm module
        comm = pi_comm(0, b_input_var, 1024, 1000)

        # Gets the version of ServerBridge
        ver = comm.SbVersion()
        print("Serverbridge Version on LXI:", ver)

        # Gets the the card count
        err, count = comm.CountFreeCards()
        err, bus, slot = comm.FindFreeCards(count)
        print("Error:", err, "Card count:", count)

        print("--------------------------------")
        
        # s=int(self.inf[1])
        # c=int(self.inf[0])
        # print(c)
        # print(s)
       
        if self.cardsub==1 :
             
             c=int(self.button[0])
             cardnum =self.listind[c-1]
        else:
             cardnum =self.listind[c-1]
        print(cardnum)
        # info=self.subinfo_main[self.button_id-1][i-1]
        # cardnum = self.button_id-1
        # If during init the value of mode is zero them the paramA and paramB can be treated as bus and slot
        # If the value of mode is non-zero then ParamA will be cardnum and paramB will be accessType

        mode = 0  # Last two parameters treated as bus and slot
        # while cardnum < count:
        card = pi_card(0, b_input_var, 1024, 1000, mode, bus[cardnum], slot[cardnum])

        err, cid = card.CardId()
        if err != 0:
            print(err)
            ret, errmsg = card.ErrorCodeToMessage(err)
            print("Error: ", errmsg, "-", err)

        print("Bus ", bus[cardnum], "Slot ", slot[cardnum])
        print("ID = ", cid.decode("utf-8"))
        e, ins, outs = card.EnumerateSubs()
        print("subunits: ", ins, "input, ", outs, "output")

        print("--------------------------------")
      
        if self.cardsub==1 :
             
             s=int(self.button[1])
             sub=s
        else:
               sub = s
        print(sub)
        # while sub <= outs:

        err, inf = card.SubType(sub, 1)
        if err != 0:
            print(err)
            ret, errmsg = card.ErrorCodeToMessage(err)
            print("Error: ", errmsg, "-", err)
        else:
            print("subunit ", sub, " = ", inf)

        err, subType, rows, cols = card.SubInfo(sub, 1)
        if err != 0:
            print(err)
            ret, errmsg = card.ErrorCodeToMessage(err)
            print("Error: ", errmsg, "-", err)
        
      
 
          
        
        if self.cardcf==1:
            print("clear")
            print(sub)
            err = card.ClearSub(sub)
            if err != 0:
                print(err)
                ret, errmsg = card.ErrorCodeToMessage(err)
                print("Error: ", errmsg)

            card.CloseCards()
            comm.Disconnect()

            # for self.button1 in self.finalbutton:
            # if len(self.finalbutton)==0:
            print(len(self.finalbutton))
            for self.pushButton_tab in self.finalbutton[int(self.button[1])-1]:
                    if self.pushButton_tab.isChecked():
                        print("Button is checked")
                        self.pushButton_tab.setCheckable(False)
                        self.pushButton_tab.setCheckable(True)
            # self.deletebutton()
            # self.column=[]
            # self.row=[]     
            self.cardcf=0
            print("Clearing outputs and closing card...")
         
            self.maintab.setCurrentIndex(0)
            exit
        else:
            if self.cardsub==1 : 
                print("clear")
                print(sub)
                err = card.ClearSub(sub)
                if err != 0:
                    print(err)
                    ret, errmsg = card.ErrorCodeToMessage(err)
                    print("Error: ", errmsg)

                card.CloseCards()
                comm.Disconnect()
                 

                self.cardsub=0
                print(len(self.finalbutton))
                for self.pushButton_tab in self.finalbutton[int(self.button[1])-1]:
                    if self.pushButton_tab.isChecked():
                        print("Button is checked")
                        self.pushButton_tab.setCheckable(False)
                        self.pushButton_tab.setCheckable(True)
                self.newlist=[]
                # rt=(str(cardnum+1)+","+str(sub))
                print(self.button)
                self.rm=len(self.row)
                print(self.rm)
                for i in range(0,self.rm):
                    if self.row[i]== self.button:
                         self.newlist.append(i)
                print(self.newlist)  
                for i in self.newlist:
                    for j in range(0,self.rm):
                        if self.row[j]== self.button:
                            self.row.pop(j)
                            self.column.pop(j)
                            break
                        
                   
                     
                print(self.row)
                print(self.column)
                

            else:
                i=0
                # self.rc= self.rc.split(".")
                rr=self.inf
                cc=self.rc
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
                            rcv= self.column[i].split(".")
                            rv=int(rcv[0])
                            rc=int(rcv[1])
                            print(rv,rc)
                            x=rc

                            self.infotext=self.subinfo_main[c-1][sub-1]
                            n=self.infotext.split('(')[0] 
                            if n=="SWITCH" or "MUX":
                                self.SW=1
                            if n=="MATRIX":
                                self.SW=0
                            print(cardnum)
                            print(sub)
                            print(n)  
                            if self.SW==0:
                                err = card.OpCrosspoint(sub,rv, rc, 0)
                                print("sw")
                            if self.SW==1:
                                err = card.OpBit(sub,x,0)  
                            # card.SetCrosspointRange(subunit, self.row[i], self.column[i],self.column[i], state)
                            # card.OpCrosspoint(subunit, self.row[i], self.column[i], state)
                            # print(state)
                            self.mm=0
                            self.row.pop(i)
                            self.column.pop(i)
                            break
                    
                # print(self.row)
                # print(self.column)
                if self.mm==1:
                    self.row.append(self.inf)
                    self.column.append(self.rc)
                # print(len(self.row))
                # print(len(self.column))
            
            
                for i in range(0,len(self.row)):
                        self.ff=1
                        # print(self.row)
                        # print(self.column)
                        # print(i)
                        if self.row[i] ==rr:
                            print(",,,,,,,,,,,,,,,,,,add,,,,,,,,,,,,,,,,,,,,,,")
                            # print("Switching range",self.row[i], "-","on row", self.column[i])
                            rcv= self.column[i].split(".")
                            print(rcv)
                            rv=int(rcv[0])
                            rc=int(rcv[1])
                            print(rv,rc)
                            state = 1
                            x=rc
                            self.infotext=self.subinfo_main[c-1][sub-1]
                            n=self.infotext.split('(')[0] 
                            if n=="SWITCH":
                                self.SW=1
                            if n=="MATRIX":
                                self.SW=0
                            print(n)  
                            print(cardnum)
                            print(sub)
                            if self.SW==0:
                                err = card.OpCrosspoint(sub,rv, rc, 1)
                                print("sw")
                            if self.SW==1:
                                err = card.OpBit(sub,x,1)
                                print("nosw")                  
           
    def clearc(self):
          self.cardcf=1
          print(self.finalbutton)
          self.callbutton()
    def clearsub(self):  
         self.cardsub=1 
        #  self.cardsf=num  
        #  print(self.finalbutton) 
         self.callbutton()  
      
       
    def handleButtonClick1(self, button): 
        self.button_id1 = button.property("id1")  

        # self.frame = button.parent()
        # self.pushButton1 = self.frame.findChild(QPushButton)
        for i in range(0,self.af):
          if self.button_id1==i+1:
            print("Button clicked111:", self.button_id1)
            self.label_details.setText("Model:  "+str(self.cardf[i])+"\n\n"+"Revision:  1.00\n\n"+"Bus:  "+str(self.busf[i])+"\n\nDevice:  "+str(self.devicef[i])+"\n\n"+str(self.subunitinf[i])+"\n\nSubunit types: "+str((', '.join(self.subinFoAdv[i])))+"\n\n\n\nSerial Number: "+str(self.serial[i]))
         

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
    
        self.addFrames()
        
    def  addFrames(self):
       
                    t=0
                    for i in range(0,self.af):
                                    
                                    if self.listind[i]==0:
                                         self.buttonHead(t)
                                         t=t+1
                                    
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
                                    # for t in self.subinFoAdv[i]:
                                    #     m=m+t
                                    # print(m)
                                    # self.pushButton.setText("Model:"+str(self.cardf[i])+"  S/N:"+str(self.serial[i])+" "+str((', '.join(self.subinFoAdv[i]))) )   
                                    self.pushButton.setText(str(('   '.join(self.subinFoAdv[i]))))
                                    self.pushButton.setToolTip("Model: "+str(self.cardf[i])+"  S/N: "+str(self.serial[i]))
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
                    print("end")
   
            # self.maintab.setCurrentIndex(2)
    def tabcreat(self):
        print("tab")
        if len(self.tabmain)>0: 
            for i in range(0,len(self.tabmain)):
                if self.tabmain[i]==self.button_id:
                
                    k=i+3
                    print(k,"[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                    self.maintab.setCurrentIndex(k)
                
                        
                    return
                else:
                    pass

        # self.new_window = QMainWindow()
        
        # self.new_window.setWindowTitle("New Window") 
        # self.lax =QtGui.QWidget(self.new_window)   
        self.lax = QtGui.QWidget()
        self.lax.setObjectName("lax0")
        self.lax.setStyleSheet('''
             QTabWidget::pane {
                background-color: #F5F5F5;
                border: 1px solid #C0C0C0;
                border-radius: 4px;
                padding: 2px;
            }
            QTabBar::tab {
                background-color: #E0E0E0;
                color: #333333;
                border: 1px solid #C0C0C0;
                padding: 4px;
                margin-right: 2px;
                border-top-left-radius: 8px;
                border-top-right-radius: 8px;
            }
            QTabBar::tab:selected {
                background-color: #FFFFFF;
                color: #000000;
                border-bottom-color: none;
            }
        ''')
        self.tabadd.append(self.lax)
        self.tabWidgetlax = QtGui.QTabWidget(self.lax)
        self.tabWidgetlax.setGeometry(QtCore.QRect(0, 0, 1370, 550))
        self.tabWidgetlax.setObjectName("tabWidgetlax")
        self.tabmain.append(self.button_id)
     
       
        # self.setCentralWidget(self.mdi)
       
        t=self.output[self.button_id-1]
        for i in range(1,t+1):
            self.infotext=self.subinfo_main[self.button_id-1][i-1]
            self.lax1 = QtGui.QWidget()
            self.lax1.setObjectName("lax %s"%i)
            self.lax1.setStyleSheet('''
             QTabWidget::pane {
                background-color: #F5F5F5;
                border: 1px solid #C0C0C0;
                border-radius: 4px;
                padding: 2px;
            }
            QTabBar::tab {
                background-color: #E0E0E0;
                color: #333333;
                border: 1px solid #C0C0C0;
                padding: 4px;
                margin-right: 2px;
                border-top-left-radius: 8px;
                border-top-right-radius: 8px;
            }
            QTabBar::tab:selected {
                background-color: #FFFFFF;
                color: #000000;
                border-bottom-color: none;
            }
        ''')
            self.tabWidgetlax.addTab(self.lax1, "")
            # info=self.subinfo_main[self.button_id-1][i-1]
            # self.tabWidgetlax.setTabText(self.tabWidgetlax.indexOf(self.lax1), QtGui.QApplication.translate("MainWindo", ""+str(info), None, QtGui.QApplication.UnicodeUTF8))
            ########################################
            self.scrollArea = QtGui.QScrollArea(self.lax1)
            self.scrollArea.setGeometry(QtCore.QRect(0, 0, 1201, 521))
            self.scrollArea.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.scrollArea.setFrameShape(QtGui.QFrame.Box)
            self.scrollArea.setLineWidth(0)
            self.scrollArea.setMidLineWidth(0)
            self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
            self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
            self.scrollArea.setWidgetResizable(True)
            self.scrollArea.setObjectName("scrollArea")
            self.scrollAreaWidgetContents_3 = QtGui.QWidget()
            self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 2020, 1020))
            self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
            self.verticalLayout_8 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_3)
            self.verticalLayout_8.setSpacing(0)
            self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout_8.setObjectName("verticalLayout_8")
            self.frame_3 = QtGui.QFrame(self.scrollAreaWidgetContents_3)
            self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
            self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
            self.frame_3.setObjectName("frame_3")
            self.verticalLayout_9 = QtGui.QVBoxLayout(self.frame_3)
            self.verticalLayout_9.setObjectName("verticalLayout_9")
            self.frame_tab_main_3 = QtGui.QFrame(self.frame_3)
            sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.frame_tab_main_3.sizePolicy().hasHeightForWidth())
            self.frame_tab_main_3.setSizePolicy(sizePolicy)
            self.frame_tab_main_3.setMinimumSize(QtCore.QSize(2000, 1000))
            self.frame_tab_main_3.setMouseTracking(True)
            self.frame_tab_main_3.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.frame_tab_main_3.setFrameShape(QtGui.QFrame.Box)
            self.frame_tab_main_3.setFrameShadow(QtGui.QFrame.Raised)
            self.frame_tab_main_3.setLineWidth(1)
            self.frame_tab_main_3.setObjectName("frame_tab_main_3")
            self.verticalLayout_9.addWidget(self.frame_tab_main_3)
            self.verticalLayout_8.addWidget(self.frame_3)
            self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
            self.frame_tabd_3 = QtGui.QFrame(self.lax1)
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
            self.pushButton_CLEARCARD1 = QtGui.QPushButton(self.frame_tabd_3)
            self.pushButton_CLEARCARD1.setGeometry(QtCore.QRect(40, 440, 101, 21))
            self.pushButton_CLEARCARD1.setCursor(QtCore.Qt.PointingHandCursor)
            self.pushButton_CLEARCARD1.setMouseTracking(True)
            self.pushButton_CLEARCARD1.setStyleSheet("background-color: rgb(153, 153, 153);")
            self.pushButton_CLEARCARD1.setObjectName("pushButton_CLEARCARD1")
            m=(str(self.button_id)+","+str(i))
            self.close.append(m)
            self.pushButton_CLEARCARD1.setProperty("btn_clear",m )
            self.pushButton_CLEARCARD1.clicked.connect(lambda btn= self.pushButton_CLEARCARD1: self.tabbuttonclear(btn))
            self.groupBox_5 = QtGui.QGroupBox(self.frame_tabd_3)
            self.groupBox_5.setGeometry(QtCore.QRect(6, 10, 151, 121))
            self.groupBox_5.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.groupBox_5.setObjectName("groupBox_5")
            self.pushButton_on = QtGui.QPushButton(self.groupBox_5)
            self.pushButton_on.setGeometry(QtCore.QRect(30, 23, 30, 30))
            self.pushButton_on.setAutoDefault(False)
            self.pushButton_on.setDefault(True)
            self.pushButton_on.setFlat(True)
            self.pushButton_on.setObjectName("pushButton_on")
            self.pushButton_of = QtGui.QPushButton(self.groupBox_5)
            self.pushButton_of.setGeometry(QtCore.QRect(90, 23, 30, 30))
            self.pushButton_of.setAutoDefault(False)
            self.pushButton_of.setDefault(True)
            self.pushButton_of.setFlat(True)
            self.pushButton_of.setObjectName("pushButton_of")
            self.label_intervel = QtGui.QLabel(self.groupBox_5)
            self.label_intervel.setGeometry(QtCore.QRect(30, 60, 101, 20))
            self.label_intervel.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.label_intervel.setObjectName("label_intervel")
            self.label_type = QtGui.QLabel(self.frame_tabd_3)
            self.label_type.setGeometry(QtCore.QRect(10, 140, 141,290))
            self.label_type.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
            self.label_type.setObjectName("label_type")
            self.pushButton= QtGui.QPushButton(self.frame_tabd_3)
            self.pushButton.setGeometry(QtCore.QRect(40, 480, 101, 21))
            self.pushButton.setCursor(QtCore.Qt.PointingHandCursor)
            self.pushButton.setMouseTracking(True)
            self.pushButton.setStyleSheet("background-color: rgb(153, 153, 153);")
            self.pushButton.setObjectName("pushButton_CloseCARD1")

            self.pushButton.setProperty("btn",m )
            self.pushButton.clicked.connect(lambda btn= self.pushButton: self.tabbuttonclose(btn))
            
         

            



    
            






           
            self.pushButton_CLEARCARD1.setText(QtGui.QApplication.translate("MainWindow", "Clear card", None, QtGui.QApplication.UnicodeUTF8))
            self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Close card", None, QtGui.QApplication.UnicodeUTF8))
            self.groupBox_5.setTitle(QtGui.QApplication.translate("MainWindow", "Multiuser Moniter", None, QtGui.QApplication.UnicodeUTF8))
            self.pushButton_on.setText(QtGui.QApplication.translate("MainWindow", "ON", None, QtGui.QApplication.UnicodeUTF8))
            self.pushButton_of.setText(QtGui.QApplication.translate("MainWindow", "OFF", None, QtGui.QApplication.UnicodeUTF8))
            self.label_intervel.setText(QtGui.QApplication.translate("MainWindow", "Intervel : 1000ms", None, QtGui.QApplication.UnicodeUTF8))
           
            # self.label_type.setText(QtGui.QApplication.translate("MainWindow", "type:", None, QtGui.QApplication.UnicodeUTF8))
            self.tabWidgetlax.addTab(self.lax1, "")
            self.tabWidgetlax.setTabText(self.tabWidgetlax.indexOf(self.lax1), QtGui.QApplication.translate("MainWindo", ""+str(self.infotext), None, QtGui.QApplication.UnicodeUTF8))
            # self.new_window.setCentralWidget(self.lax)
            # self.new_window.setAttribute(QtCore.Qt.WA_DeleteOnClose, False)  # Prevent the window from closing automatically
            # self.new_window.show()

            ##########################
            n=""
            n=self.infotext.split('(')[0] 
            print("/??????????????????")
            # if n=="MATRIXR" or n=="SWITCH": 
            #     print(n)   
            #     print("msm")    
            if n=="RES":
                print(n)
                self.resiter_control(i)
            # if n=="BATT":
            #      print(n)
            #      self.batt_control(i)
            else:
                if n=="SWITCH":
                    self.SW=1
                else:
                     self.SW=0
                print(n)   
                self.buttoncreate(i)
        
              
        # sub = QtGui.QMdiSubWindow(self.mdi)
        # sub.setWidget(self.lax)
        # sub.setWindowTitle("Subwindow" + str(self.count))
        # self.mdi.addSubWindow(sub)
        # sub.show()
        self.maintab.addTab(self.lax, "")  
        self.maintab.setTabText(self.maintab.indexOf(self.lax), QtGui.QApplication.translate("MainWindo", "Model:"+str(self.cardf[self.button_id-1]), None, QtGui.QApplication.UnicodeUTF8))   
        # self.windowAction()

        for i in range(0,len(self.tabmain)):
            print(self.tabmain)
            if self.tabmain[i]==self.button_id:
                k=i+3
                print(k,"[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                self.maintab.setCurrentIndex(k)
                    
       

  
  
    def windowAction(self):
        # print("Triggered:", action.text())

        # if action.text() == "New":
        self.count += 1
        sub = QMdiSubWindow()

        # Create a new tab widget for each subwindow
        #  self.tabWidgetlax = QTabWidget()

        # Create a new tab and add it to the tab widget
        # tab = QTextEdit()
        self.tabWidgetlax.addTab(self.lax,"Subwindow ")

        sub.setWidget( self.tabWidgetlax)
        sub.setWindowTitle("Subwindow" + str(self.count))
        self.mdi.addSubWindow(sub)
        sub.show()

  
  
  
  
  
  
  
  
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


    def buttoncreate(self,m):
        tf=1
        self.label_type.setText(str(m)+"."+str(self.infotext)+"\n\n"+"status: OK")
        self.rows=self.row_main[self.button_id-1][m-1]
        self.columns=self.column_main[self.button_id-1][m-1]
        self.button1=[]
        if  self.rows==1:
             tf=0
        
        print("button")
        c22=140
        r1=100
        r2=60
        # c=1230
        # r=550
        for i in range(1,self.rows+1):
            c2=100
           
            c1=100
            r1=r1+40
            r2=r2+40
            print(i)
            for j in range(1,self.columns+1):
                    if c1>1230:
                        # self.frame_tab_main.setMinimumSize(QtCore.QSize(c1+50, r1))
                        print()
                      
                    if r1>550:
                    
                    #     self.frame_tab_main.setMinimumSize(QtCore.QSize(c1, r1+50))
                        print("hoi")
                    # # name=(self.t+str(self.button_id))
                    t=(str(self.button_id)+"."+str(m)+","+str(i)+"."+str(j))

                    # print(name)
                    # self.pushButton_tab = QtGui.QPushButton(self.t1)
                    self.pushButton_tab = QtGui.QPushButton(self.frame_tab_main_3)

                    self.pushButton_tab.setGeometry(QtCore.QRect(c1, r1, 40, 40))
                    self.pushButton_tab.setStyleSheet("background-color: rgb(104, 104, 104);")
                    self.pushButton_tab.setCursor(QtCore.Qt.PointingHandCursor)
                    self.pushButton_tab.setAutoDefault(True)
                    self.pushButton_tab.setObjectName("pushButton")
                    self.pushButton_tab.setProperty("btn_no",t )
                    self.pushButton_tab.clicked.connect(lambda btn= self.pushButton_tab: self.tabbuttonClick1(btn))
                    self.pushButton_tab.setCheckable(True)
                    if tf==0:
                        self.pushButton_tab.setText(str(j))   
                   
                    self.button1.append(self.pushButton_tab)
                    c1=c1+40
                    if i==1 and tf==1:
                        self.label_47 = QtGui.QLabel(self.frame_tab_main_3)
                        self.label_47.setGeometry(QtCore.QRect(c2,r2, 40, 40))
                        font = QtGui.QFont()
                        font.setPointSize(12)
                        font.setWeight(75)
                        font.setBold(True)
                        self.label_47.setFont(font)
                        # self.label_47.setFrameShape(NoFrame)
                        self.label_47.setText("Y"+str(j))
                        self.label_47.setStyleSheet("")
                        self.label_47.setFrameShape(QtGui.QFrame.NoFrame)
                        self.label_47.setAlignment(QtCore.Qt.AlignCenter)
                        self.label_47.setObjectName("label_47")
                        c2=c2+40
                        # print(r2,c2)
                    if j==1 and tf==1:
                        
                        self.label_47 = QtGui.QLabel(self.frame_tab_main_3)
                        self.label_47.setGeometry(QtCore.QRect(60,c22, 40, 40))
                        font = QtGui.QFont()
                        font.setPointSize(12)
                        font.setWeight(75)
                        font.setBold(True)
                        self.label_47.setFont(font)
                        # self.label_47.setFrameShape(NoFrame)
                        self.label_47.setText("X"+str(i))
                        self.label_47.setStyleSheet("")
                        self.label_47.setFrameShape(QtGui.QFrame.NoFrame)
                        self.label_47.setAlignment(QtCore.Qt.AlignCenter)
                        self.label_47.setObjectName("label_47")
                        c22=c22+40
                        print(c22)
                    # print(c1,r1)
        self.finalbutton.append(self.button1)
                #########################################################################################
    def batt_control(self):
              
        n1=int(self.ipind[self.button_id-1])
        b_input_var= self.b_input_var1[n1]

        base = pi_base(0, b_input_var,1024,1000)

        ver = base.Version()
        e, count = base.CountFreeCards()


        print ("--------------------------------")

        bus = 9
        slot = 13
        card = pi_card(0, b_input_var,1024,1000,bus,slot)

        err, cid = card.CardId()
        print("Version ", ver)
        print ("Bus", bus, " Device", slot)
        print ("ID = ", cid)
        e, ins, outs = card.EnumerateSubs()
        print ("subunits: ", ins, "input, ", outs, "output")
            
        sub = 1
        while sub <= outs:
            e, inf = card.SubType(sub, 1)
            print ("subunit ",sub, " = ", inf)
            sub = sub + 1
            
        print ("\n--------------------------------")

        # Setting Voltage to 2 Volts on Sub-Unit 1
        err = card.BattSetVoltage(1,2)
        err, volts = card.BattGetVoltage(1)

        # Setting Current to 100mA on Sub-Unit 1
        err = card.BattSetCurrent(1,0.1)
        err, current = card.BattGetCurrent(1)

        #Sets the output enable pattern of battery simulator
        err = card.BattSetEnable(1,1)
        err, pattern = card.BattGetEnable(1)

        #Obtains the present state of a hardware interlock
        #0 = interlock is "down"
        #1 = interlock is "up"
        err, state = card.BattReadInterlockState(1)

        print ("Voltage =", volts, "Volts")
        print ("Current =", current, "Amps")
        print ("Pattern =", pattern)
        print ("State =", state)


        print ("\n--------------------------------")


    def resiter_control(self,i):
        n1=int(self.ipind[self.button_id-1])
        b_input_var= self.b_input_var1[n1]
                
        if sys.version_info > (3, 0, 0):
            input_var =b_input_var
        else:
            input_var = b_input_var
        b_input_var = str.encode(input_var)

        # b_input_var = "192.168.2.131"

        # Initialize the comm module
        comm = pi_comm(0, b_input_var, 1024, 1000)

        # Gets the version of ServerBridge
        ver = comm.SbVersion()
        print("Serverbridge Version on LXI:", ver)

        # Gets the number of usable cards in an array and the card count
        err, card_array, card_count = comm.GetUsableCards(0)
        print("Error:", err, "Card count:", card_count)

        if err != 0:
            exit(0)

        card_num =self.CARDRES
        # If during init the value of mode is zero them the paramA and paramB can be treated as bus and slot
        # If the value of mode is non-zero then ParamA will be cardnum and paramB will be accessType


        mode = 1  # Last two parameters treated as list of cards and accessType
        accessType = 1  # Shared access

        # for card_num in range(0, card_count):
        print("\n--------------------------------")
        card = pi_card(0, b_input_var, 1024, 1000, mode, card_array[card_num], accessType)

        err, cid = card.CardId()
        if err != 0:
            ret, errmsg = card.ErrorCodeToMessage(err)
            print("Error: ", errmsg, "-", err)
            card.CloseCards()
          

        print("Card ", card_array[card_num])
        print("ID = ", cid)
        e, ins, outs = card.EnumerateSubs()
        print("subunits: ", ins, "input, ", outs, "output")
        sub=i
        # for sub in range(1, outs):
        print("\n --- Subunit ", sub, " ---")
        # Make sure this is a resistor card
        err, sub_type, rows, cols = card.SubInfo(sub, 1)
        if err != 0:
            ret, errmsg = card.ErrorCodeToMessage(err)
            print("Error: ", errmsg, "-", err)
            card.CloseCards()
           
        if sub_type != 7:
            card.CloseCards()
          

        # Resistor Subunit Specific Information
        err, minres, maxres, refres, precpc, precdelta, int1, int1delta, caps = card.ResInfo(sub)
        if err != 0:
            ret, errmsg = card.ErrorCodeToMessage(err)
            print("Error: ", errmsg, "-", err)
        if self.rescheck==1:
            print("Minimum resistance: ", minres)
            print("Maximum resistance: ", maxres)
            print("Reference resistance: ", refres)
            print("Percentage precision : ", precpc)
            print("Precision offset (ohms): ", precdelta)
            print("Max deviation (ohms)", int1delta)
            print("\n")
            self.label_type.setText(str(i)+"."+str(self.infotext)+"\n\n"+"Minimum resistance: "+str(minres)+"\n\n"+"Maximum resistance:"+str(maxres)+"\n\n"+"Reference resistance: "+str(refres)+"\n\n"+"Percentage precision : "+str(precpc)+"\n\n"+"Precision offset (ohms):"+str(precdelta)+"\n\n"+"Max deviation (ohms)"+str(int1delta)+"\n\n")
            self.lcdNumber = QtGui.QLCDNumber(self.lax1)
            self.lcdNumber.setGeometry(QtCore.QRect(290, 50, 631, 91))
            self.lcdNumber.setStyleSheet("background-color: rgb(0, 0, 0);\n"
    "color: rgb(85, 255, 0);")
            self.lcdNumber.setLineWidth(3)
            self.lcdNumber.setMidLineWidth(0)
            self.lcdNumber.setNumDigits(14)
            self.lcdNumber.setSegmentStyle(QtGui.QLCDNumber.Filled)
            self.lcdNumber.setProperty("lcd_num",i )
            self.lcdNumber.setObjectName("lcdNumber")
            self.lcdinf.append(self.lcdNumber)
            

            self.dial = QtGui.QDial(self.lax1)
            self.dial.setGeometry(QtCore.QRect(120, 200, 381, 231))
            self.dial.setStyleSheet("background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(255, 255, 255, 255), stop:0.373979 rgba(255, 255, 255, 255), stop:0.373991 rgba(33, 30, 255, 255), stop:0.624018 rgba(33, 30, 255, 255), stop:0.624043 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
    "color: qlineargradient(spread:pad, x1:0.920455, y1:0.351, x2:0.943, y2:0.83, stop:0.267045 rgba(85, 170, 255, 239), stop:0.710227 rgba(34, 255, 255, 223));")
            self.dial.setMinimum(int(minres))
            self.dial.setMaximum(int(maxres))
            self.dial.setSingleStep(5)
            self.dial.setPageStep(100)
            self.dial.setProperty("res_no",i )
            self.dial.setSliderPosition(2)
            self.dial.setInvertedControls(False)
            self.dial.setWrapping(False)
            self.dial.setNotchesVisible(True)
            self.dial.setObjectName("dial")
            
            self.dial.valueChanged.connect(lambda value, lcd=self.lcdNumber: self. on_dial_changed(value, lcd))
        # self.dial.valueChanged.connect(self.on_dial_changed)
        if self.rescheck==0:
            
            err = card.ResSetResistance(sub, 0, self.resvalue- int1delta)
            print("Resistance Set! ", self.resvalue - int1delta)
            if err != 0:
                ret, errmsg = card.ErrorCodeToMessage(err)
                print("Error: ", errmsg, "-", err)

            # Setting a resistance
            err, res = card.ResGetResistance(sub)
            if err != 0:
                ret, errmsg = card.ErrorCodeToMessage(err)
                print("Error: ", errmsg, "-", err)
                card.CloseCards()
               

            print("Resistance Retrieved! ", res)

            card.CloseCards()

            comm.Disconnect() 
            self.rescheck=1
    def on_dial_changed(self, value,lcd):
        num=lcd
        print(num)
        lcd.display(value)
        self.resvalue=value
        self.rescheck=0
        time.sleep(0.5) 
        for i in range(0,len(self.lcdinf)):
             if num==self.lcdinf[i]:
                print(i)
                self.resiter_control(i+1)
                  
        # self.resiter_control(num)

        


app = QApplication(sys.argv)
mainWindow = QMainWindow()
ui = VVEE(mainWindow)
mainWindow.show()
sys.exit(app.exec_())
