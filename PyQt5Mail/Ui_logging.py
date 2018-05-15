# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\jearchen\Desktop\qttest\eric6\PyQt5Mail\logging.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(200, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(widget.sizePolicy().hasHeightForWidth())
        widget.setSizePolicy(sizePolicy)
        widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        widget.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(widget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(widget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.username = QtWidgets.QLineEdit(widget)
        font = QtGui.QFont()
        font.setFamily("System")
        font.setBold(True)
        font.setWeight(75)
        
        self.username.setFont(font)
        self.username.setObjectName("username")
        self.verticalLayout.addWidget(self.username)
        self.userpass = QtWidgets.QLineEdit(widget)
        self.userpass.setObjectName("userpass")
        
        self.verticalLayout.addWidget(self.userpass)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.logbutton = QtWidgets.QPushButton(widget)
        self.logbutton.setObjectName("logbutton")
        self.gridLayout.addWidget(self.logbutton, 1, 0, 1, 1)

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "登录界面 "))
        self.label.setText(_translate("widget", "登录名"))
        self.label_2.setText(_translate("widget", "密码"))
        self.logbutton.setText(_translate("widget", "登录"))
