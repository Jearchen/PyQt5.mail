#from PyQt5.QtCore import pyqtqSignal
from PyQt5.QtWidgets import QMainWindow,QPushButton,QApplication,QWidget,QMessageBox
import sys
app =QApplication([])
widget =QWidget()

def showMsg():
    QMessageBox.information(widget,"信息提示框","OK,弹出提示框 ")
btn= QPushButton("测试点击按钮",widget)
btn.clicked.connect(showMsg)
widget.show()
sys.exit(app.exec_())
#class WinForm(QMainWindow):
#    btnClickedSignal= pyqtSignal()
    
