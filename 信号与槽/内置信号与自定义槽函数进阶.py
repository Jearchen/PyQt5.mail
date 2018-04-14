from PyQt5.QtWidgets import *
import sys
class WinForm(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("内置的信号与自定义槽函数实例")
        self.resize(330,50)
        btn= QPushButton("关闭",self)
        btn.clicked.connect(self.btn_close)
    def btn_close(self):
        self.close()
if __name__=="__main__":
    app= QApplication(sys.argv)
    win=WinForm()
    win.show()
    sys.exit(app.exec_())
