###已可正常使用
#coding=utf-8
import os
import sys
import time
import psutil
import os
import datetime
import D_clean
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


# global Q
# Q = ''

class Example(QWidget,QObject):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        f = open('setting.txt','r')
        wordlist = f.readlines()
        if wordlist != []:
            txtword = wordlist[0]
            txtword = txtword.replace('/', '\\')
            print('in',txtword)
        
            self.setGeometry(700,400,400,350)
            self.setWindowTitle('TEST CLEAN！')
            self.bt3=QPushButton('選資料夾',self)
            self.bt3.move(80,20)
            self.bt3.clicked.connect(self.OpenFileDialog)
            self.text=QLineEdit(txtword,self)
            self.text.setGeometry(80,50,150,30)
        else:
            self.setGeometry(300,300,500,500)
            self.setWindowTitle('TEST CLEAN！')
            self.bt3=QPushButton('選擇資料夾',self)
            self.bt3.move(80,20)
            self.bt3.clicked.connect(self.OpenFileDialog)
            self.text=QLineEdit("請選資料夾",self)
            self.text.setGeometry(80,50,150,30)

        self.tb = QTextBrowser(self)
        self.tb.move(80,120)

        self.lb = QLabel('狀態顯示:',self)
        self.lb.move(80,100)
        # self.setGeometry(500,500,500,500)
        # self.setWindowTitle('TEST Dclean')
        
        # self.lb1 = QLabel   ('路徑：',self)
        # self.lb1.move(20,20)

        # self.lb6 = QLabel(txtword,self)
        # self.lb6.move(80,20)
        # Q= self.text.text()
        
        # self.bt1 = QPushButton('修改路徑',self)
        # self.bt1.move(200,20)

        # self.bt2 = QPushButton('開始監控',self)
        # self.bt2.move(80,80)

        # self.bt3 = QPushButton('顯示狀態',self)
        # self.bt3.move(80,100)


        # self.bt1.clicked.connect(self.showDialog)
        # self.bt2.clicked.connect(lambda: self.go(Q))

        # self.bt2.clicked.connect(self.QTh)
        # self.bt3.clicked.connect(self.wordtxt)


        self.workthread=WorkThread()
        # 連接信號
        self.workthread.trigger.connect(self.wordtxt)
        # 開始線程
        self.workthread.start()

                
    def wordtxt(self):
        f = open('log.txt','r')
        wordlist = f.readlines()
        logword = wordlist[-1]
        self.tb.setText(logword)
        print('?????????')


    def OpenFileDialog(self):
        fname=QFileDialog.getExistingDirectory(self,'打開文件','./')
        if fname[0]:
            self.text.setText(fname)
            f = open('setting.txt','w')
            f.write(fname+"/")

           

class WorkThread(QThread):
    trigger = pyqtSignal()

    def __int__(self):
        super(WorkThread, self).__init__()

    def run(self):
        while True:
            time.sleep(15)
            f = open('setting.txt','r')
            wordlist = f.readlines()
            Q = wordlist[0]
            print(Q)
            D_clean.go(Q)
            # ex.wordtxt()
            # self.lolo()
            # 循环完毕后发出信号
            self.trigger.emit()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())