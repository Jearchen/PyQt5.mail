from PyQt5.QtCore import QObject,pyqtSignal
class CustSignal(QObject):
     signal6 = pyqtSignal([int,str],[str])

     def __init__(self,parent=None):
        super(CustSignal,self).__init__(parent)
        self.signal6[int,str].connect(self.signalCall6)
        self.signal6[str].connect(self.signalCall6OverLoad)
        
        self.signal6[int,str].emit(1,"text")
        self.siganl6[str].emit("text")

        def signalCall6(self,val,text):
            print("signal6 emit,value",val,text)

        def signalCall6OverLoad(self,val):
            print("signal6 OverLoad emit,value=",val)
if __name__=="__main__":
    custSignal=CustSignal()
