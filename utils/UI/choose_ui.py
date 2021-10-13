# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assets/choose_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(3300, 1900)
        self.background = QtWidgets.QLabel(Form)
        self.background.setGeometry(QtCore.QRect(0, 0, 3300, 1900))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("background.png"))
        self.background.setScaledContents(True)
        self.background.setWordWrap(True)
        self.background.setObjectName("background")
        self.logo = QtWidgets.QLabel(Form)
        self.logo.setGeometry(QtCore.QRect(860, 180, 1580, 720))
        self.logo.setStyleSheet("")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setWordWrap(True)
        self.logo.setObjectName("logo")
        self.backstage_frame = QtWidgets.QFrame(Form)
        self.backstage_frame.setGeometry(QtCore.QRect(1000, 1000, 640, 660))
        self.backstage_frame.setStyleSheet("#backstage_frame {\n"
"    background-color: #EEEEEE;\n"
"    border: 2px solid black;\n"
"    border-radius: 15px;\n"
"}")
        self.backstage_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.backstage_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.backstage_frame.setObjectName("backstage_frame")
        self.identity_frame_title = QtWidgets.QLabel(self.backstage_frame)
        self.identity_frame_title.setGeometry(QtCore.QRect(0, 0, 640, 120))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.identity_frame_title.setFont(font)
        self.identity_frame_title.setStyleSheet("background-color: #D0D0D0;\n"
"border: 2px solid black;\n"
"border-top-left-radius: 15px;\n"
"border-top-right-radius: 15px;\n"
"")
        self.identity_frame_title.setTextFormat(QtCore.Qt.PlainText)
        self.identity_frame_title.setAlignment(QtCore.Qt.AlignCenter)
        self.identity_frame_title.setObjectName("identity_frame_title")
        self.name_frame = QtWidgets.QFrame(self.backstage_frame)
        self.name_frame.setGeometry(QtCore.QRect(40, 160, 560, 140))
        self.name_frame.setStyleSheet("#name_frame {\n"
"    border: 0px;\n"
"}")
        self.name_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.name_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.name_frame.setObjectName("name_frame")
        self.name_title = QtWidgets.QLabel(self.name_frame)
        self.name_title.setGeometry(QtCore.QRect(200, 0, 160, 80))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.name_title.setFont(font)
        self.name_title.setAlignment(QtCore.Qt.AlignCenter)
        self.name_title.setObjectName("name_title")
        self.frame = QtWidgets.QFrame(self.name_frame)
        self.frame.setGeometry(QtCore.QRect(0, 80, 560, 60))
        self.frame.setStyleSheet("background-color: white;\n"
"border: 2px solid gray;\n"
"border-radius: 15px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(500, 10, 40, 40))
        self.label.setStyleSheet("background-color: white;\n"
"border:0;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("arrow.png"))
        self.label.setObjectName("label")
        self.name_frame_2 = QtWidgets.QFrame(self.backstage_frame)
        self.name_frame_2.setGeometry(QtCore.QRect(40, 340, 560, 140))
        self.name_frame_2.setStyleSheet("#name_frame_2 {\n"
"    border: 0px;\n"
"}")
        self.name_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.name_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.name_frame_2.setObjectName("name_frame_2")
        self.name_title_2 = QtWidgets.QLabel(self.name_frame_2)
        self.name_title_2.setGeometry(QtCore.QRect(200, 0, 160, 80))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.name_title_2.setFont(font)
        self.name_title_2.setAlignment(QtCore.Qt.AlignCenter)
        self.name_title_2.setObjectName("name_title_2")
        self.frame_2 = QtWidgets.QFrame(self.name_frame_2)
        self.frame_2.setGeometry(QtCore.QRect(0, 80, 560, 60))
        self.frame_2.setStyleSheet("background-color: white;\n"
"border: 2px solid gray;\n"
"border-radius: 15px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(500, 10, 40, 40))
        self.label_2.setStyleSheet("background-color: white;\n"
"border:0;")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("arrow.png"))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.backstage_frame)
        self.pushButton.setGeometry(QtCore.QRect(230, 530, 180, 70))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:#D0D0D0;\n"
"border: 2px solid gray;\n"
"border-radius: 15px;")
        self.pushButton.setObjectName("pushButton")
        self.monitor_frame = QtWidgets.QFrame(Form)
        self.monitor_frame.setGeometry(QtCore.QRect(1680, 1000, 640, 480))
        self.monitor_frame.setStyleSheet("#monitor_frame {\n"
"    background-color: #EEEEEE;\n"
"    border: 2px solid black;\n"
"    border-radius: 15px;\n"
"}")
        self.monitor_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.monitor_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.monitor_frame.setObjectName("monitor_frame")
        self.identity_frame_title_2 = QtWidgets.QLabel(self.monitor_frame)
        self.identity_frame_title_2.setGeometry(QtCore.QRect(0, 0, 640, 120))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.identity_frame_title_2.setFont(font)
        self.identity_frame_title_2.setStyleSheet("background-color: #D0D0D0;\n"
"border: 2px solid black;\n"
"border-top-left-radius: 15px;\n"
"border-top-right-radius: 15px;\n"
"")
        self.identity_frame_title_2.setTextFormat(QtCore.Qt.PlainText)
        self.identity_frame_title_2.setAlignment(QtCore.Qt.AlignCenter)
        self.identity_frame_title_2.setObjectName("identity_frame_title_2")
        self.name_frame_3 = QtWidgets.QFrame(self.monitor_frame)
        self.name_frame_3.setGeometry(QtCore.QRect(40, 160, 560, 140))
        self.name_frame_3.setStyleSheet("#name_frame_3 {\n"
"    border: 0px;\n"
"}")
        self.name_frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.name_frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.name_frame_3.setObjectName("name_frame_3")
        self.name_title_3 = QtWidgets.QLabel(self.name_frame_3)
        self.name_title_3.setGeometry(QtCore.QRect(200, 0, 160, 80))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.name_title_3.setFont(font)
        self.name_title_3.setAlignment(QtCore.Qt.AlignCenter)
        self.name_title_3.setObjectName("name_title_3")
        self.frame_3 = QtWidgets.QFrame(self.name_frame_3)
        self.frame_3.setGeometry(QtCore.QRect(0, 80, 560, 60))
        self.frame_3.setStyleSheet("background-color: white;\n"
"border: 2px solid gray;\n"
"border-radius: 15px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(500, 10, 40, 40))
        self.label_3.setStyleSheet("background-color: white;\n"
"border:0;")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("arrow.png"))
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.monitor_frame)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 350, 180, 70))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:#D0D0D0;\n"
"border: 2px solid gray;\n"
"border-radius: 15px;")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.identity_frame_title.setText(_translate("Form", "監控視窗"))
        self.name_title.setText(_translate("Form", "選擇場所"))
        self.name_title_2.setText(_translate("Form", "選擇相機"))
        self.pushButton.setText(_translate("Form", "確認"))
        self.identity_frame_title_2.setText(_translate("Form", "流量管理"))
        self.name_title_3.setText(_translate("Form", "選擇場所"))
        self.pushButton_2.setText(_translate("Form", "確認"))

