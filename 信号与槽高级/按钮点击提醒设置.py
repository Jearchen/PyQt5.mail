import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class window(QWidget):
    def __init__(self,parent=None):
        super(window,self).__init__(parent)
        self.setWindowTitle("QMessage例子")
        self.resize(300,200)                
        ##self.signal1 =pyqtSignal()
        ##self.signal2 = pyqtSignal()        
        self.btn1=QPushButton("按钮1")
        ##self.btn2=QPushButton("按钮2")        
        ##self.btn1.clicked.connect(self.messageMention1)
        ##self.btn2.clicked.connect(self.messageMention2)
        layout =QVBoxLayout()
        layout.addWidget(self.btn1)
        ##layout.addWidget(self.btn2)
        self.setLayout= (layout)
    ##def messageMention1(self):
    ##        print("##")
    ##        reply=QMessageBox.information(self,"点击啦","按了第一个按钮，我收到了",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
     ##       print(reply)
    ##def messageMention2(self):
    ##        QMessageBox.information(self,"点击啦 ","按下了第二个按钮 ，我收到了",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
if __name__=="__main__":
    app = QApplication(sys.argv)
    myshow=window()
    myshow.show()
    sys.exit(app.exec_())
