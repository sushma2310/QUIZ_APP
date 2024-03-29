# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resultwin.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import sys
from screen1 import *

class Ui_result(QtWidgets.QWidget):
    def __init__(self, name, count, total):
        super().__init__()
        self.name=name
        self.count=60
        self.total=total
    def setupUi(self, result):
        result.setObjectName("result")
        result.resize(732, 499)
        self.centralwidget = QtWidgets.QWidget(result)
        self.centralwidget.setObjectName("centralwidget")
        self.T3 = QtWidgets.QLineEdit(self.centralwidget)
        self.T3.setGeometry(QtCore.QRect(190, 70, 81, 31))
        self.T3.setStyleSheet("background-color: rgb(125, 121, 255);\n"
"border-color: rgb(0, 85, 127);\n"
"color:rgb(255, 255, 255);\n"
"")
        self.T3.setObjectName("T3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 261, 21))
        self.label_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(70, 160, 81, 31))
        self.back.setStyleSheet("background-color: rgb(125, 121, 255);\n"
"border-color: rgb(0, 85, 127);\n"
"color:rgb(255, 255, 255);")
        self.back.setObjectName("back")
        result.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(result)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 732, 18))
        self.menubar.setObjectName("menubar")
        result.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(result)
        self.statusbar.setObjectName("statusbar")
        result.setStatusBar(self.statusbar)

        self.retranslateUi(result)
        QtCore.QMetaObject.connectSlotsByName(result)

    def retranslateUi(self, result):
        _translate = QtCore.QCoreApplication.translate
        result.setWindowTitle(_translate("result", "MainWindow"))
        self.label_2.setText(_translate("result", "TOTAL SCORE"))
        self.back.setText(_translate("result", "BACK"))
        self.T3.setText(str(self.total))
        self.back.clicked.connect(self.opques)
        self.back.clicked.connect(result.close)
    def opques(self):
    
        self.queswin = QtWidgets.QMainWindow()
        self.ui = Ui_homewin()
        self.ui.setupUi(self.queswin)
        self.queswin.show()

        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    result = QtWidgets.QMainWindow()
    ui = Ui_result()
    ui.setupUi(result)
    result.show()
    sys.exit(app.exec_())
