# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'q5.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import sys
from resultwin import *

class Ui_q5(QtWidgets.QWidget):
    def __init__(self, name, count, total):
        super().__init__()
        self.name=name
        self.count=60
        self.total=total
    def setupUi(self, q5):
        q5.setObjectName("q5")
        q5.resize(638, 386)
        self.centralwidget = QtWidgets.QWidget(q5)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 70, 481, 126))
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
        self.push = QtWidgets.QPushButton(self.centralwidget)
        self.push.setGeometry(QtCore.QRect(50, 220, 71, 21))
        self.push.setStyleSheet("background-color: rgb(125, 121, 255);\n"
"border-color: rgb(0, 85, 127);\n"
"font: 75 9pt \"Arial\";\n"
"color:rgb(255, 255, 255);\n"
"")
        self.push.setObjectName("push")
        self.resume = QtWidgets.QPushButton(self.centralwidget)
        self.resume.setGeometry(QtCore.QRect(140, 220, 61, 21))
        self.resume.setStyleSheet("background-color: rgb(125, 121, 255);\n"
"border-color: rgb(0, 85, 127);\n"
"font: 75 9pt \"Arial\";\n"
"color:rgb(255, 255, 255);\n"
"")
        self.resume.setObjectName("resume")
        self.nextend = QtWidgets.QPushButton(self.centralwidget)
        self.nextend.setGeometry(QtCore.QRect(220, 220, 61, 21))
        self.nextend.setStyleSheet("background-color: rgb(125, 121, 255);\n"
"border-color: rgb(0, 85, 127);\n"
"font: 75 9pt \"Arial\";\n"
"color:rgb(255, 255, 255);\n"
"")
        self.nextend.setObjectName("nextend")
        self.Tlabel = QtWidgets.QLabel(self.centralwidget)
        self.Tlabel.setGeometry(QtCore.QRect(280, 40, 211, 20))
        self.Tlabel.setObjectName("timer")
        self.T2 = QtWidgets.QLineEdit(self.centralwidget)
        self.T2.setGeometry(QtCore.QRect(350, 40, 61, 20))
        self.T2.setStyleSheet("")
        self.T2.setObjectName("T2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 40, 111, 20))
        self.label.setObjectName("label")
        self.T1 = QtWidgets.QLineEdit(self.centralwidget)
        self.T1.setGeometry(QtCore.QRect(100, 40, 91, 20))
        self.T1.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.T1.setObjectName("T1")
        q5.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(q5)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 638, 18))
        self.menubar.setObjectName("menubar")
        q5.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(q5)
        self.statusbar.setObjectName("statusbar")
        q5.setStatusBar(self.statusbar)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.ShowTime)
        self.timer.start(1000)
        self.retranslateUi(q5)
        QtCore.QMetaObject.connectSlotsByName(q5)

    def retranslateUi(self, q5):
        _translate = QtCore.QCoreApplication.translate
        q5.setWindowTitle(_translate("q5", "screen2q5"))
        self.ques.setText(_translate("q5", "5. Is Python code compiled or interpreted?"))
        self.r1.setText(_translate("q5", "a) Python code is both compiled and interpreted"))
        self.r2.setText(_translate("q5", "b) Python code is neither compiled nor interpreted"))
        self.r3.setText(_translate("q5", "c) Python code is only compiled"))
        self.r4.setText(_translate("q5", "d) Python code is only interpreted"))
        self.push.setText(_translate("q5", "Pause"))
        self.resume.setText(_translate("q5", "Resume"))
        self.nextend.setText(_translate("q5", "Next"))
        self.Tlabel.setText(_translate("q5", "TIMER"))
        self.label.setText(_translate("q5", "NAME"))
        self.nextend.clicked.connect(self.opques)
        self.nextend.clicked.connect(q5.close)

    def ShowTime(self):
        if self.count > 0:
            self.count = self.count - 1
        S1 = str(self.count // 60)
        S2 = str(self.count % 60)
        S3 = S1 + "." + S2
        self.T1.setText(str(self.name))
        self.T2.setText(str(S3))
    def opques(self):

        if self.r2.isChecked() == True:
            self.total = self.total + 1

        self.queswin = QtWidgets.QMainWindow()
        self.ui = Ui_result(self.name, self.count, self.total)
        self.ui.setupUi(self.queswin)
        self.queswin.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    q5 = QtWidgets.QMainWindow()
    ui = Ui_q5()
    ui.setupUi(q5)
    q5.show()
    sys.exit(app.exec_())
