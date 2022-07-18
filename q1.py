# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'q1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import sys
from q2 import *

class Ui_q1(QtWidgets.QWidget):
    def __init__(self, name):
        super().__init__()
        self.name=name
        self.count=60
        self.total=0
    def setupUi(self, q1):
        q1.setObjectName("q1")
        q1.resize(640, 378)
        self.centralwidget = QtWidgets.QWidget(q1)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 70, 396, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ques = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.ques.setObjectName("ques")
        self.verticalLayout.addWidget(self.ques)
        self.r1 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.r1.setObjectName("r1")
        self.verticalLayout.addWidget(self.r1)
        self.r2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.r2.setObjectName("r2")
        self.verticalLayout.addWidget(self.r2)
        self.r3 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.r3.setObjectName("r3")
        self.verticalLayout.addWidget(self.r3)
        self.r4 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.r4.setObjectName("r4")
        self.verticalLayout.addWidget(self.r4)
        self.pause = QtWidgets.QPushButton(self.centralwidget)
        self.pause.setGeometry(QtCore.QRect(70, 220, 71, 21))
        self.pause.setStyleSheet("background-color: rgb(125, 121, 255);\n"
"border-color: rgb(0, 85, 127);\n"
"font: 75 9pt \"Arial\";\n"
"color:rgb(255, 255, 255);\n"
"")
        self.pause.setObjectName("pause")
        self.resume = QtWidgets.QPushButton(self.centralwidget)
        self.resume.setGeometry(QtCore.QRect(160, 220, 71, 21))
        self.resume.setStyleSheet("background-color: rgb(125, 121, 255);\n"
"border-color: rgb(0, 85, 127);\n"
"font: 75 9pt \"Arial\";\n"
"color:rgb(255, 255, 255);")
        self.resume.setObjectName("resume")
        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setGeometry(QtCore.QRect(250, 220, 71, 21))
        self.next.setStyleSheet("background-color: rgb(125, 121, 255);\n"
"border-color: rgb(0, 85, 127);\n"
"font: 75 9pt \"Arial\";\n"
"color:rgb(255, 255, 255);\n"
"selection-color: rgb(211, 197, 255);")
        self.next.setObjectName("next")
        self.Tlabel = QtWidgets.QLabel(self.centralwidget)
        self.Tlabel.setGeometry(QtCore.QRect(330, 40, 61, 20))
        self.Tlabel.setMinimumSize(QtCore.QSize(0, 20))
        self.Tlabel.setStyleSheet("")
        self.Tlabel.setObjectName("Tlabel")
        self.T2 = QtWidgets.QLineEdit(self.centralwidget)
        self.T2.setGeometry(QtCore.QRect(380, 40, 61, 20))
        self.T2.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.T2.setObjectName("T2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 40, 111, 20))
        self.label.setObjectName("label")
        self.T1 = QtWidgets.QLineEdit(self.centralwidget)
        self.T1.setGeometry(QtCore.QRect(100, 40, 91, 20))
        self.T1.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.T1.setObjectName("T1")
        q1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(q1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 18))
        self.menubar.setObjectName("menubar")
        q1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(q1)
        self.statusbar.setObjectName("statusbar")
        q1.setStatusBar(self.statusbar)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.ShowTime)
        self.timer.start(1000)
        self.retranslateUi(q1)
        QtCore.QMetaObject.connectSlotsByName(q1)

    def retranslateUi(self, q1):
        _translate = QtCore.QCoreApplication.translate
        q1.setWindowTitle(_translate("q1", "screen2q1"))
        self.ques.setText(_translate("q1", "1. Who developed Python Programming Language?"))
        self.r1.setText(_translate("q1", "a) Wick van Rossum"))
        self.r2.setText(_translate("q1", "b) Rasmus Lerdorf"))
        self.r3.setText(_translate("q1", "c) Guido van Rossum"))
        self.r4.setText(_translate("q1", "d) Niene Stom"))
        self.pause.setText(_translate("q1", "Pause"))
        self.resume.setText(_translate("q1", "Resume"))
        self.next.setText(_translate("q1", "Next"))
        self.Tlabel.setText(_translate("q1", "TIMER"))
        self.label.setText(_translate("q1", "NAME"))
        self.next.clicked.connect(self.opque)
        self.next.clicked.connect(q1.close)

    def ShowTime(self):
        if self.count > 0:
            self.count = self.count - 1
        S1 = str(self.count // 60)
        S2 = str(self.count % 60)
        S3 = S1 + "." + S2
        self.T1.setText(str(self.name))
        self.T2.setText(str(S3))
    def opque(self):
        if self.r3.isChecked() == True:
            self.total = self.total + 1
        self.queswin = QtWidgets.QMainWindow()
        self.ui = Ui_q2(self.name, self.count, self.total)
        self.ui.setupUi(self.queswin)
        self.queswin.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    q1 = QtWidgets.QMainWindow()
    ui = Ui_q1()
    ui.setupUi(q1)
    q1.show()
    sys.exit(app.exec_())