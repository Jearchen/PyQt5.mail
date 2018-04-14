from  PyQt5.QtCore import pyqtSignal,QObject

#自定义信号对象
class QTypeSignal(QObject):

    #定义一个信号对象
    sendmsg= pyqtSignal(str,str)

    def __init__(self):
        super(QTypeSignal,self).__init__()
    def run(self):
    #发射信号
        self.sendmsg.emit("第一个参数","第二个参数")
        

#自定义槽对象
class QTypeSlot(QObject):
    def __init__(self):
        super(QTypeSlot,self).__init__()
    def get(self,msg1,msg2):
        print("QSlot get msg=>"+msg1+" "+msg2)


if __name__=="__main__":
    send= QTypeSignal()
    slot= QTypeSlot()


    print("信号与槽函数的绑定")
    send.sendmsg.connect(slot.get)
    send.run()
    

    print("信号与槽函数的断开连接")
    send.sendmsg.disconnect(slot.get)
    send.run()
