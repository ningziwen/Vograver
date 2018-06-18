#!/usr/bin/python3
# -*- coding: UTF-8 -*-


import sys
from PyQt5.QtWidgets import QMainWindow,QDialog,QApplication,QHBoxLayout,QAbstractItemView,QTableWidgetItem,QFileDialog
from PyQt5.QtCore import Qt,QRect
from PyQt5.QtGui import QFont
from function import *
from startwords import *
from quickstartwords import *
from wordbase import *
from Resetdialog import *
from statwindow import *
import xml.etree.ElementTree as ET
import time
import random
import matplotlib
matplotlib.use("Qt5Agg") 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure  
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

class Figure_Canvas(FigureCanvas):
    def __init__(self, parent=None, width=6, height=2, dpi=100):
        fig = Figure(figsize=(width, height), dpi=100)
        FigureCanvas.__init__(self, fig) 
        self.setParent(parent)
        self.axes = fig.add_subplot(111) 
    def line(self,x,y):
        self.axes.set_xlabel(u'学习天数')  
        self.axes.set_ylabel(u'单词数')
        self.axes.plot(x, y)
    def topie(self,piedata,pielabels):
        self.axes.pie(piedata,labels=pielabels)
        
def wordstatus_fun(wordi):
    if int(wordbook[wordi][3].text)==2:
        return "简单词"
    elif int(wordbook[wordi][3].text)==1:
        return "简单词检测"
    elif int(wordbook[wordi][2].text)==-1:
        return "生词"
    elif int(wordbook[wordi][2].text)<=7 and int(wordbook[wordi][2].text)>=1:
        return "第"+wordbook[wordi][2].text+"次复习"
    elif int(wordbook[wordi][2].text)==8:
        return "已掌握"

def inituseritem(index):
    item=ET.Element("item")
    elem = ET.Element("date")
    elem.text = index
    item.append(elem)
    elem = ET.Element("new")
    elem.text = "0"
    item.append(elem)
    elem = ET.Element("c1")
    elem.text = "0"
    item.append(elem)
    elem = ET.Element("c2")
    elem.text = "0"
    item.append(elem)
    elem = ET.Element("c3")
    elem.text = "0"
    item.append(elem)
    elem = ET.Element("c4")
    elem.text = "0"
    item.append(elem)
    elem = ET.Element("c5")
    elem.text = "0"
    item.append(elem)
    elem = ET.Element("c6")
    elem.text = "0"
    item.append(elem)
    elem = ET.Element("c7")
    elem.text = "0"
    item.append(elem)
    elem = ET.Element("prekill")
    elem.text = "0"
    item.append(elem)
    elem = ET.Element("time")
    elem.text = "0"
    item.append(elem)
    return item

def get_todayitem():
    global tree_user
    global userinfo
    for item in userinfo.findall('item'):
        if item[0].text==daynowi:
            return item
    todayitem=inituseritem(daynowi)
    userinfo.append(todayitem)
    tree_user.write(userdataname,'UTF-8')
    tree_user = ET.parse(userdataname)
    userinfo= tree_user.getroot()
    return todayitem

class Statwindow(QMainWindow,Ui_Statwindow):  
    def __init__(self): 
        super(Statwindow, self).__init__()  
        self.setupUi(self)
        self.setWindowFlags(Qt.CustomizeWindowHint) 
        layout = QHBoxLayout()  
        layout.addWidget(self.timetb)  
        self.setLayout(layout)  
        self.exitbutton.clicked.connect(self.exit_fun)
        self.timetb.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def openitself(self):
        self.show()
        self.timetb.setColumnCount(11)
        self.timetb.setRowCount(len(userinfo)-1) 
        self.timetb.setHorizontalHeaderLabels(['日期','生词数量','第1次复习数量','第2次复习数量','第3次复习数量','第4次复习数量','第5次复习数量','第6次复习数量','第7次复习数量','简单词检验数量','学习时间']) 
        for j in range(11):
            for i in range(len(userinfo)-1):
                if j==0:
                    self.timetb.setItem(i,j,QTableWidgetItem(time.strftime("%Y-%m-%d", time.localtime(float(userinfo[0].text)+(int(userinfo[i+1][0].text)-1)*(24*60*60)))))
                elif j==10:
                    self.timetb.setItem(i,j,QTableWidgetItem(userinfo[i+1][j].text+'s'))
                else:
                    self.timetb.setItem(i,j,QTableWidgetItem(userinfo[i+1][j].text))
        linec=Figure_Canvas()
        x=[]
        y=[]
        for i in range(len(userinfo)-1):
            x.append(int(userinfo[i+1][0].text))
            s=0
            for j in range(9):
                s=s+int(userinfo[i+1][j+1].text)
            y.append(s)
        linec.line(x,y)
        linescene = QtWidgets.QGraphicsScene()
        linescene.addWidget(linec)
        self.linegraph.setScene(linescene)
        if len(userinfo)!= 1:
            piec=Figure_Canvas()     
            piedata=[]
            pielabels=[]
            labeldict={1:u'生词',2:u'第1次复习',3:u'第2次复习',4:u'第3次复习',5:u'第4次复习',6:u'第5次复习',7:u'第6次复习',8:u'第7次复习',9:u'简单词检验'}
            for j in range(9):
                if int(userinfo[len(userinfo)-1][j+1].text)>0:
                    piedata.append(int(userinfo[len(userinfo)-1][j+1].text))
                    pielabels.append(labeldict[j+1])
            piec.topie(piedata,pielabels)
            piescene = QtWidgets.QGraphicsScene()
            piescene.addWidget(piec)
            self.cakegraph.setScene(piescene)   
    def exit_fun(self):
        self.hide()

class Resetdialog(QDialog,Ui_Resetdialog):
    def __init__(self): 
        super(Resetdialog, self).__init__()  
        self.setupUi(self)  
    
    def openitself(self):
        self.show()

class Quickstartwords(QMainWindow,Ui_Quickstartwords):  
    def __init__(self): 
        super(Quickstartwords, self).__init__()  
        self.setupUi(self) 
        self.showchinesebutton.clicked.connect(self.showchinese)
        self.exitbutton.clicked.connect(self.exititself)
        
    def openitself(self):
        self.show()
        self.k=0
        self.sel=list(range(len(wordbook)))
        random.shuffle(self.sel)
        while self.flag==1:
            self.english.setText(wordbook[self.sel[self.k]][0].text)
            self.k=self.k+1
            time.sleep(2)
            if self.k>len(wordbook)-1:
                self.showchinesebutton.hide()
                self.english.setText("没有单词啦")
                self.chinese.hide()
                break
    
    def showchinese(self):
        if self.flag==1:
            self.flag=0
            self.chinese.setText(wordbook[self.k][1].text)
            self.showchinesebutton.setText("继续")
        if self.flag==0:
            self.flag=1
            self.chinese.setText(wordbook[self.k][1].text)
            self.showchinesebutton.setText("显示释义")
    
    def exititself(self):
        self.flag==0
        self.hide()
        

class Function(QMainWindow,Ui_Function):  
    def __init__(self): 
        super(Function, self).__init__()  
        self.setupUi(self) 
        self.begintime=float(userinfo[0].text)
        self.resetdata.clicked.connect(self.resetdata_fun)
        self.newwords.setText("10")
        self.reviewwords.setText("10")
        self.newwords.textChanged.connect(self.newwordsout)
        self.reviewwords.textChanged.connect(self.reviewwordsout)
        self.start.clicked.connect(self.hideitself)
        self.scanwords.clicked.connect(self.hideitself)
        self.statwords.clicked.connect(self.hideitself)
#        self.quickstart.clicked.connect(self.hideitself)  
                                      
    def resetdata_fun(self):
        global tree_user
        global userinfo
        userinfo[0].text=str(int(time.time())-(int(time.time())&(24*3600)))
        for item in userinfo.findall('item'):
            userinfo.remove(item)
        tree_user.write(userdataname,'UTF-8')
        tree_user = ET.parse(userdataname)
        userinfo= tree_user.getroot()
        
    def newwordsout(self):
        global maxnewwords
        maxnewwords=int(self.newwords.text())-1
    def reviewwordsout(self):
        global maxreviewwords
        maxreviewwords=int(self.reviewwords.text())-1
    def openitself(self):
        self.show()
    def hideitself(self):
        self.hide()
            
class Wordbase(QMainWindow,Ui_Wordbase):
    def __init__(self):  
        super(Wordbase, self).__init__()  
        self.setupUi(self)
        self.setWindowFlags(Qt.CustomizeWindowHint) 
        layout = QHBoxLayout()  
        layout.addWidget(self.wordtable)  
        self.setLayout(layout)  
        self.exitbutton.clicked.connect(self.exit_fun)
        self.wordtable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.importbutton.clicked.connect(self.importmsg)
        self.exportbutton.clicked.connect(self.exportmsg)
        
    def importmsg(self):
        global tree_word
        global wordbook
        importfilename,importfiletype= QFileDialog.getOpenFileName(self,  
                                    "选取文件",  
                                    "C:/",  
                                    "XML Files (*.xml)")
        if importfilename!="":
            tree_word = ET.parse(importfilename)
            wordbook= tree_word.getroot()
            tree_word.write(worddataname,'UTF-8')
    def exportmsg(self):
        exportfilename, ok = QFileDialog.getSaveFileName(self,  
                                    "文件保存",  
                                    "C:/",  
                                    "XML Files (*.xml)") 
        if exportfilename!="":
            tree_word.write(exportfilename,'UTF-8')
    def openitself(self):
        self.show()
        self.wordtable.setColumnCount(5)
        self.wordtable.setRowCount(len(wordbook)) 
        self.wordtable.setHorizontalHeaderLabels(['单词','含义','状态','距下一次大约复习时间','是否为困难词']) 
        for j in range(5):
            for i in range(len(wordbook)):
                if j==0:
                    self.wordtable.setItem(i,j,QTableWidgetItem(wordbook[i][0].text))
                elif j==1:
                    self.wordtable.setItem(i,j,QTableWidgetItem(wordbook[i][1].text))
                elif j==2:
                    self.wordtable.setItem(i,j,QTableWidgetItem(wordstatus_fun(i)))
                elif j==3:
                    if int(wordbook[i][3].text)==2:
                        self.wordtable.setItem(i,j,QTableWidgetItem("~"))
                    elif int(wordbook[i][2].text)==-1:
                        self.wordtable.setItem(i,j,QTableWidgetItem("~"))
                    elif int(wordbook[i][2].text)==8:
                        self.wordtable.setItem(i,j,QTableWidgetItem("~"))
                    else:
                        timepassed=time.time()-float(wordbook[i][5].text)
                        if int(wordbook[i][3].text)==1:
                            timeremained=killtime-timepassed
                        else:
                            timeremained=timedict[int(wordbook[i][2].text)]-timepassed
                        if timeremained>=0:
                            inttimeremained=int(timeremained)
                            hourremained=inttimeremained//3600
                            self.wordtable.setItem(i,j,QTableWidgetItem(str(hourremained)+"h"))
                        else:
                            self.wordtable.setItem(i,j,QTableWidgetItem("0h"))
                elif j==4:
                     self.wordtable.setItem(i,j,QTableWidgetItem(wordbook[i][4].text))  
    def exit_fun(self):
        self.hide()
        
        
class Startwords(QMainWindow,Ui_Startwords):  
    def __init__(self):  
        super(Startwords, self).__init__()  
        self.setupUi(self) 
        self.setWindowFlags(Qt.CustomizeWindowHint) 
        self.i=0
        self.nowi=0
        self.backi=0
        self.showchinesebutton.hide()
        self.remember.hide()
        self.notremember.hide()
        self.english.hide()
        self.chinese.hide()
        self.kill.hide()
        self.rechoose.hide()
        self.beginbutton.clicked.connect(self.showenglish)
        self.showchinesebutton.clicked.connect(self.showchinese)
        self.remember.clicked.connect(self.remember_fun)
        self.remember.clicked.connect(self.showenglish)
        self.notremember.clicked.connect(self.notremember_fun)
        self.notremember.clicked.connect(self.showenglish)
        self.kill.clicked.connect(self.kill_fun)
        self.kill.clicked.connect(self.showenglish)
        self.exitbutton.clicked.connect(self.exit_fun)
        self.hardcheck.stateChanged.connect(self.changehard)
        self.rechoose.clicked.connect(self.rechoose_fun)
        self.showchinesebutton.setShortcut(chr(32))
        self.remember.setShortcut('Z')
        self.notremember.setShortcut('X')
        self.kill.setShortcut('C')
        
    def openitself(self): 
        global wordbooktmp
        self.show()
        self.i=0
        self.nowi=0
        self.showchinesebutton.hide()
        self.remember.hide()
        self.notremember.hide()
        self.english.hide()
        self.chinese.hide()
        self.kill.hide()
        self.beginbutton.show()
        self.hardcheck.hide()
        self.i=self.i-1
        self.starttime=time.time()
        self.count=[0,0,0,0,0,0,0,0,0]
        
        
    def ifshow(self):
        if int(wordbook[self.i][2].text)==-1 and (self.count[0]>maxnewwords):
            return False
        if (int(wordbook[self.i][3].text)==1 or (int(wordbook[self.i][2].text)<=7 and int(wordbook[self.i][2].text)>=1)) and (sum(self.count[1:9])>maxreviewwords):
            return False
        tick=time.time()
        timepassed=tick-float(wordbook[self.i][5].text)
        if int(wordbook[self.i][3].text)==2:
            return False
        elif int(wordbook[self.i][3].text)==1:
            if timepassed>=killtime:
                self.count[8]=self.count[8]+1
                return True
            else:
                return False
        elif int(wordbook[self.i][2].text)==8:
            return False
        elif int(wordbook[self.i][2].text)<=7 and int(wordbook[self.i][2].text)>=1:
            if timepassed>=timedict[int(wordbook[self.i][2].text)]:
                self.count[int(wordbook[self.i][2].text)]=self.count[int(wordbook[self.i][2].text)]+1
                return True
            else: 
                return False
        elif int(wordbook[self.i][2].text)==-1:
            self.count[0]=self.count[0]+1
            return True
    
    def changehard(self, state):
        if state == Qt.Checked:
            wordbook[self.nowi][4].text='1'
        else:
            wordbook[self.nowi][4].text='0'
    
    def showenglish(self):
        self.english.show()
        self.english.setFont(QFont("Roman times",20,QFont.Bold))  
        self.beginbutton.hide()
        self.english.setGeometry(QRect(210, 20, 371, 91))
        self.showchinesebutton.show()
        self.remember.hide()
        self.notremember.hide()
        self.kill.hide()
        self.hardcheck.hide()
        self.chinese.setText("")
        if self.i==-1:
            self.rechoose.hide()
        else:
            self.rechoose.show()
        self.backi=self.i
        flag=0
        while(1):
            self.i=self.i+1 
            if self.i>len(wordbook)-1:
                flag=1
                break
            if self.ifshow()==True:
                break
        if flag==0:
            self.english.setText(wordbook[self.i][0].text)
            self.nowi=self.i
            self.wordstatus.setText(wordstatus_fun(self.nowi))
        else:
            self.wordstatus.hide()
            self.showchinesebutton.hide()
            self.rechoose.hide()
            self.english.setText("没有单词啦")
            
        
    def showchinese(self):
        self.wordtmp=[wordbook[self.i][2].text,wordbook[self.i][3].text,wordbook[self.i][4].text,wordbook[self.i][5].text]
        self.counttmp=self.count
        self.hardcheck.show()
        self.rechoose.hide()
        if wordbook[self.nowi][4].text=='1':
            self.hardcheck.setCheckState(Qt.Checked)
        else:
            self.hardcheck.setCheckState(Qt.Unchecked)
        self.chinese.show()
        self.english.setFont(QFont("Roman times",10,QFont.Bold)) 
        self.english.setGeometry(QRect(280, 50, 231, 51))
        self.showchinesebutton.hide()
        self.remember.show()
        self.notremember.show()
        self.kill.show()
        self.chinese.setText(wordbook[self.nowi][1].text)
        
    def remember_fun(self):
        self.showchinesebutton.hide()
        self.remember.hide()
        self.notremember.hide()
        self.kill.hide()
        if int(wordbook[self.nowi][2].text)==-1:
            wordbook[self.nowi][2].text='1'
            wordbook[self.nowi][5].text=str(time.time())
        if int(wordbook[self.nowi][2].text)>=1 and int(wordbook[self.nowi][2].text)<=7:
            wordbook[self.nowi][2].text=str(int(wordbook[self.nowi][2].text)+1)
            wordbook[self.nowi][5].text=str(time.time())
        if int(wordbook[self.nowi][3].text)==1:
            wordbook[self.nowi][3].text='2'
            wordbook[self.nowi][5].text=str(time.time())
            
    def notremember_fun(self):
        self.showchinesebutton.hide()
        self.remember.hide()
        self.notremember.hide()
        self.kill.hide()
        if int(wordbook[self.nowi][3].text)==1:
            wordbook[self.nowi][3].text='0'
            wordbook[self.nowi][5].text=str(time.time())
        
    def kill_fun(self):
        self.showchinesebutton.hide()
        self.remember.hide()
        self.notremember.hide()
        self.kill.hide()
        if int(wordbook[self.nowi][3].text)==0:
            wordbook[self.nowi][3].text='1'
            wordbook[self.nowi][5].text=str(time.time())
        
        
    def rechoose_fun(self):
        global wordbook
        self.i=self.backi
        wordbook[self.i][2].text=self.wordtmp[0]
        wordbook[self.i][3].text=self.wordtmp[1]
        wordbook[self.i][4].text=self.wordtmp[2]
        wordbook[self.i][5].text=self.wordtmp[3]
        self.count=self.counttmp
        self.i=self.i-1
        self.showenglish()
        
    def exit_fun(self):
        global tree_word
        global wordbook
        global tree_user
        global userinfo
        tree_word.write(worddataname,'UTF-8')
        tree_word = ET.parse(worddataname)
        wordbook= tree_word.getroot()
        self.hide()
        self.exittime=time.time()
        flag=0
        for todayitem in userinfo.findall('item'):
            if todayitem[0].text==daynowi:
                flag=1
                for j in range(1,10):
                    todayitem[j].text=str(int(todayitem[j].text)+self.count[j-1])
                todayitem[10].text=str(int(todayitem[10].text)+int(self.exittime-self.starttime))
                tree_user.write(userdataname,'UTF-8')
                tree_user = ET.parse(userdataname)
                userinfo= tree_user.getroot()
                break
        if flag==0:
            todayitem=inituseritem(daynowi)
            for j in range(1,10):
                todayitem[j].text=str(int(todayitem[j].text)+self.count[j-1])
            todayitem[10].text=str(int(todayitem[10].text)+int(self.exittime-self.starttime))
            userinfo.append(todayitem)
            tree_user.write(userdataname,'UTF-8')
            tree_user = ET.parse(userdataname)
            userinfo= tree_user.getroot() 
        
if __name__ == '__main__':

   worddataname="wholedata.xml"
   userdataname="userdata.xml"
   tree_word = ET.parse(worddataname)
   tree_user=ET.parse(userdataname)
   wordbook= tree_word.getroot()
   userinfo=tree_user.getroot()
   daynowi=str(int(time.time()-float(userinfo[0].text))//(24*3600))
   timedict={1:0.5*60*60,2:1*60*60,3:3*60*60,4:10*60*60,5:24*60*60,6:48*60*60,7:96*60*60}
   killtime=36*60*60
   maxnewwords=10
   maxreviewwords=10
   app = QApplication(sys.argv)
   function=Function()
   startwords=Startwords()
   wordbase=Wordbase()
   resetdialog=Resetdialog()
   quickstartwords=Quickstartwords()
   statwindow=Statwindow()
   function.show()
   function.start.clicked.connect(startwords.openitself)
   function.scanwords.clicked.connect(wordbase.openitself)
   function.resetdata.clicked.connect(resetdialog.openitself)
   function.statwords.clicked.connect(statwindow.openitself)
   startwords.exitbutton.clicked.connect(function.openitself)
   resetdialog.buttonBox.accepted.connect(function.resetdata_fun)
#   function.quickstart.clicked.connect(quickstartwords.openitself)
   quickstartwords.exitbutton.clicked.connect(function.openitself)
   statwindow.exitbutton.clicked.connect(function.openitself)
   wordbase.exitbutton.clicked.connect(function.openitself) 
    
   sys.exit(app.exec_())
 
   