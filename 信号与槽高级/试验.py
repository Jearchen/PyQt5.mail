import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class windowtest(QWidget):
    def __init__(self,parent=None):
        super(windowtest,self).__init__(parent)
        self.setWindowTitle("实验")
        self.resize(300,100)       
        self.btn1=QPushButton("按钮1")
        self.btn2=QPushButton("按钮2")
        layout=QHBoxLayout()
        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        self.setLayout(layout)
        self.signal1 =pyqtSignal()
        self.signal2 = pyqtSignal()
        self.btn1.clicked.connect(self.messageMention1)
        self.btn2.clicked.connect(self.messageMention2)
    def messageMention1(self):
        reply=QMessageBox.information(self,"点击啦","按了第一个按钮，我收到了",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        print(reply)
    def messageMention2(self):
        QMessageBox.information(self,"点击啦 ","按下了第二个按钮 ，我收到了",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
if __name__=="__main__":
    app= QApplication(sys.argv)
    win=windowtest()
    win.show()
    sys.exit(app.exec_()
             )
