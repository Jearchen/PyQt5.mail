import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class DockWidgets(QMainWindow):
    def __init__(self,parent=None):
        super(DockWidgets,self).__init__(parent)
        layout =QHBoxLayout()
        bar =self.menuBar()
        file =bar.addMenu("File")
        file.addAction("new")
        file.addAction("save")
        file.addAction("quit")
        
        
        self.listWidget=QListWidget()
        self.listWidget.addItem("item1")        
        self.listWidget.addItem("item2")
        self.listWidget.addItem("item3")
        
        self.items=QDockWidget("Dockable",self)
        self.items.setWidget(self.listWidget)
        self.items.setFloating(False)
        ##self.items.setAllowedAreas()
        self.setCentralWidget(QTextEdit())
        self.addDockWidget(Qt.RightDockWidgetArea,self.items)
        self.setLayout(layout)
        self.setWindowTitle("Dcok例子")
if __name__=="__main__":
    app=QApplication(sys.argv)
    demo=DockWidgets()
    demo.show()
    sys.exit(app.exec_())
