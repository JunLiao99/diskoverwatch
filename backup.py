#coding=utf-8
import os
import sys
import time
import psutil
import os
import datetime
import D_clean
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QInputDialog, QTextBrowser, QLineEdit, QFileDialog)


# global Q
# Q = ''

class Example(QWidget):
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
        
            self.setGeometry(700,400,300,150)
            self.setWindowTitle('TEST CLEAN！')
            self.bt3=QPushButton('選資料夾',self)
            self.bt3.move(80,20)
            self.bt3.clicked.connect(self.OpenFileDialog)
            self.text=QLineEdit(txtword,self)
            self.text.setGeometry(80,50,150,30)
        else:
            self.setGeometry(300,300,500,500)
            self.setWindowTitle('TEST CLEAN！')
            self.bt3=QPushButton('選資料夾',self)
            self.bt3.move(80,20)
            self.bt3.clicked.connect(self.OpenFileDialog)
            self.text=QLineEdit("選資料夾",self)
            self.text.setGeometry(80,50,150,30)

        # self.setGeometry(500,500,500,500)
        # self.setWindowTitle('TEST Dclean')
        
        # self.lb1 = QLabel   ('路徑：',self)
        # self.lb1.move(20,20)

        # self.lb6 = QLabel(txtword,self)
        # self.lb6.move(80,20)
        # Q= self.text.text()
        
        # self.bt1 = QPushButton('修改路徑',self)
        # self.bt1.move(200,20)

        self.bt2 = QPushButton('開始監控',self)
        self.bt2.move(80,80)

        self.show()

        # self.bt1.clicked.connect(self.showDialog)
        # self.bt2.clicked.connect(lambda: self.go(Q))
        self.bt2.clicked.connect(self.go)
        
    # def showDialog(self):
    #     sender = self.sender()
    #     if sender == self.bt1:
    #         text, ok = QInputDialog.getText(self, '修改路徑', '路徑：')
    #         if ok:
    #             self.lb6.setText(text)
    #             Q= self.lb6.text()
    #             self.lb6 = QLabel(Q,self)
    #             print(Q,':2')
    #             self.initUI()
    def go(self):
        sender = self.sender()
        if sender == self.bt2:
            # while True:
            f = open('setting.txt','r')
            wordlist = f.readlines()
            Q = wordlist[0]
            print(Q)
            D_clean.go(Q)
                # time.sleep(10)


    def OpenFileDialog(self):
        fname=QFileDialog.getExistingDirectory(self,'打開文件','./')
        if fname[0]:
            self.text.setText(fname)
            f = open('setting.txt','w')
            f.write(fname+"/")
            # wordlist = f.readlines()
            # txtword = wordlist[0]
            # print(txtword)
           
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())