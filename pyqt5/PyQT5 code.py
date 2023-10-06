import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic,QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import pyautogui
import pyperclip
import requests
import time
from bs4 import BeautifulSoup as bs
#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("window_newnew.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)


    def initUI1(self):
        self.label.setFont(QtGui.QFont("Agency FB", 48))
        self.label.setStyleSheet(" background: red ")

        self.show()

    def initUI2(self):
        self.label_2.setFont(QtGui.QFont("Agency FB", 48))
        self.label_2.setStyleSheet(" background: red ")

        self.show()

    def initUI3(self):
        self.label_3.setFont(QtGui.QFont("Agency FB", 48))
        self.label_3.setStyleSheet(" background: red ")

        self.show()

    def initUI4(self):
        self.label_4.setFont(QtGui.QFont("Agency FB", 48))
        self.label_4.setStyleSheet(" background: red ")

        self.show()
    def initUI4(self):
        self.label_4.setFont(QtGui.QFont("Agency FB", 48))
        self.label_4.setStyleSheet(" background: red ")

        self.show()

    def initUI5(self):
        self.label_5.setFont(QtGui.QFont("Agency FB", 48))
        self.label_5.setStyleSheet(" background: red ")

        self.show()

    def initUI6(self):
        self.label_6.setFont(QtGui.QFont("Agency FB", 48))
        self.label_6.setStyleSheet(" background: red ")

        self.show()

    def initUI7(self):
        self.label.setFont(QtGui.QFont("Agency FB", 48))
        self.label.setStyleSheet(" background: blue ")

        self.show()
    def initUI8(self):
        self.label_2.setFont(QtGui.QFont("Agency FB", 48))
        self.label_2.setStyleSheet(" background: blue ")

        self.show()
    def initUI9(self):
        self.label_3.setFont(QtGui.QFont("Agency FB", 48))
        self.label_3.setStyleSheet(" background: blue ")

        self.show()
    def initUI10(self):
        self.label_4.setFont(QtGui.QFont("Agency FB", 48))
        self.label_4.setStyleSheet(" background: blue ")

        self.show()
    def initUI11(self):
        self.label_5.setFont(QtGui.QFont("Agency FB", 48))
        self.label_5.setStyleSheet(" background: blue ")

        self.show()
    def initUI12(self):
        self.label_6.setFont(QtGui.QFont("Agency FB", 48))
        self.label_6.setStyleSheet(" background: blue ")

        self.show()
    def initUI13(self):
        self.label_7.setStyleSheet(" background: red ")

        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_1:#C2
            self.initUI1()
        elif e.key() == Qt.Key_2:#C1
            self.initUI2()
        elif e.key() == Qt.Key_3:#B2
            self.initUI3()
        elif e.key() == Qt.Key_4:#B1
            self.initUI4()
        elif e.key() == Qt.Key_5:#A2
            self.initUI5()
        elif e.key() == Qt.Key_6:#A1
            self.initUI6()
        elif e.key() == Qt.Key_A:#C2
            self.initUI7()
        elif e.key() == Qt.Key_B:#C1
            self.initUI8()
        elif e.key() == Qt.Key_C:#B2
            self.initUI9()
        elif e.key() == Qt.Key_D:#B1
            self.initUI10()
        elif e.key() == Qt.Key_E:#A2
            self.initUI11()
        elif e.key() == Qt.Key_F:#A1
            self.initUI12()
        elif e.key() == Qt.Key_Z:#화재
            self.initUI13()


if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    myWindow.show()
    #pyautogui.press('3')
    #프로그램 화면을 보여는 코드'
    app.exec_()
'''
    eq = requests.get("http://192.168.61.137/")
    req_txt = req.text
    # print(req_txt)
    text = req_txt.split()
    cnt = len(text)
    for i in range(cnt):
        globals()['Var_{}'.format(i)] = text[i]
    # i번째 인덱스 문자 = Var_{i} 변수로 대입11
    print(Var_19)
    c=char(Var_19)
    if(c=='A'):
        pyautogui.press('3')'''


    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드


'''    array = [100, 100]

    while (True):  # 실시간 통신
        array.remove(array[0])
        req = requests.get("http://192.168.61.137/")
        req_txt = req.text
        # print(req_txt)
        text = req_txt.split()
        cnt = len(text)
        for i in range(cnt):
            globals()['Var_{}'.format(i)] = text[i]
        # i번째 인덱스 문자 = Var_{i} 변수로 대입11
        print(Var_19)
        num = int(Var_19)
        array.append(num)

        if (array[0] != array[1]):
            if array[1] == 1:
                pyautogui.press('1')


    array=[100,100]
    while(True):  # 실시간 통신
        array.remove(array[0])
        req = requests.get("http://192.168.61.137/")
        req_txt = req.text
        # print(req_txt)
        text = req_txt.split()
        cnt = len(text)
        for i in range(cnt):
            globals()['Var_{}'.format(i)] = text[i]
        # i번째 인덱스 문자 = Var_{i} 변수로 대입11
        print(Var_19)
        num=int(Var_19)
        array.append(num)
        if(array[0]!=array[1]):
            if array[i]=='A'or array[i]=='B':
                pyautogui.press('1')
            if array[i]=='C'or array[i]=='D':
                pyautogui.press('6')
            if array[i]=='A'or array[i]=='C':
                pyautogui.press('2')
            if array[i]=='B'or array[i]=='D':
                pyautogui.press('A')
            if array[i]=='a'or array[i]=='b'or array[i]=='c'or array[i]=='d':
                pyautogui.press('4')
            if array[i]=='e'or array[i]=='f'or array[i]=='g'or array[i]=='h':
                pyautogui.press('D')
            if array[i]=='a'or array[i]=='b'or array[i]=='e'or array[i]=='f':
                pyautogui.press('3')
            if array[i]=='c'or array[i]=='d'or array[i]=='g'or array[i]=='h':
                pyautogui.press('C')
            if array[i]=='E'or array[i]=='F':
                pyautogui.press('2')
            if array[i]=='E'or array[i]=='G':
                pyautogui.press('1')
            if array[i]=='F'or array[i]=='H':
                pyautogui.press('A')
                
            
            if num == 1:
                pyautogui.press(1)'''
