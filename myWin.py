import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

from PyQt5 import uic##**패키지 디자이너 ui 연동 라이브러리

form_class =uic.loadUiType("UI/mainUi.ui")[0]
#큐티 디자이너 에서 만든 ui 불러옴

class Mywin(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self) #제작해 놓은 ui불러오기
        self.setWindowTitle('연습 프로그램') #윈도우 타이틀
        self.setWindowIcon(QIcon('IMG/naver3.png'))#윈도우 아이콘
        self.statusBar().showMessage('Test Program 버전0.5 2023-11-01')
        
        self.btn1.clicked.connect(self.btn1_clicked) #버튼1이 클릭되면 메서드 btn1_clicked 호출
        self.btn2.clicked.connect(self.btn2_clicked)#버튼2이 클릭되면 메서드 btn2_clicked 호출
        self.btn3.clicked.connect(self.btn3_clicked)  # 버튼3이 클릭되면 메서드 btn3_clicked 호출
        self.btn4.clicked.connect(self.btn4_clicked)  # 버튼4이 클릭되면 메서드 btn4_clicked 호출
        self.btn5.clicked.connect(self.btn5_clicked)  # 리셋버튼이 출력되면 메서드 호출


        self.lineEdit.textChanged.connect(self.changePrint)
        #라인에디트창에 텍스트가 변경될때 마다 changePrint가 실행된다

        self.lineEdit.returnPressed.connect(self.changePrint)
        #라인에디터 창에 텍스트가 입력중 (라인 에디터가 선택중)에 엔터키가 클릭되면 changePrint 함수가 샐행



    def btn1_clicked(self):#버튼 1번이 클릭되었을 때 실행될 메서드
        #print("버튼 1번이 실행 되었습니다!!!")
        self.lineEdit.setText("버튼 1번이 실행 되었습니다!!!")
        #라인에디트에  setText()가로 안의 문자열이 출력됨



    def btn2_clicked(self):#버튼2번이 클릭되었을때 실행될 메서드
        #print("버튼 2번이 실행 되었습니다!!!")
        self.textEdit.append("버튼 2번이 클릭되었습니다!!!")


    def btn3_clicked(self):#버튼3번이 클릭되었을때 실행될 메서드
        user_text = self.lineEdit.text()# 사용자가 입력한 텔스트 가져옴
        print(user_text)

    def btn4_clicked(self):#버튼3번이 클릭되었을때 실행될 메서드
        user_intro = self.textEdit.toPlainText()# 사용자가 입력한 텔스트 가져옴
        print(user_intro)
        
    def btn5_clicked(self):#버튼3번이 클릭되었을때 실행될 메서드
        self.textEdit.clear()


    def changePrint(self):
        user_text = self.lineEdit.text()  # 사용자가 입력한 텔스트 가져옴
        print(user_text)



if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex = Mywin()
    ex.show()
    sys.exit(app.exec_())