from PyQt5.QtWidgets import QApplication ,QWidget
from PyQt5.QtCore import QThread,pyqtSignal
import sys
class Main(QWidget):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.thread=MyThread()
        self.thread.setIdentity("thread1")
        self.thread.sinOut.connect(myunit.outText)
        self.thread.setVal(6)
class myunit():
    def __init__(self,parent=None):
        super().__init__(parent)
    def outText(self,text):
            print(text)
class MyThread(QThread):
    sinOut=pyqtSignal(str)
    def __init__(self,parent=None):
        super(MyThread,self).__init__(parent)
        self.identity=None
    def setIdentity(self,text):
        self.identity=text

    def setVal(self,val):
        self.times=int(val)
        self.start()
    def run(self):
        while self.times>0 and self.identity:

            self.sinOut.emit(self.identity+"==>"+str(self.times))
            self.times-=1


if __name__=="__main__":
    app=QApplication(sys.argv)
    main=Main()
    main.show()
    sys.exit(app.exec_())
