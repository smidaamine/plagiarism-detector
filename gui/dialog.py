# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created: Thu Dec 19 20:12:35 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QLineEdit
from com.smidaAmineAchache.gui.mainWindowImpl import MainWindow
from com.smidaAmineAchache.models.queries import Mnipul

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName(_fromUtf8("LoginDialog"))
        LoginDialog.resize(452, 195)
        LoginDialog.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.gridLayout = QtGui.QGridLayout(LoginDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.logInBtn = QtGui.QPushButton(LoginDialog)
        self.logInBtn.setStyleSheet(_fromUtf8(" QPushButton {\n"
"background:-webkit-gradient(linear, left top, left bottom, color-stop(0.05, color: rgb(0, 170, 0);), color-stop(1, #1a5c66));\n"
"    background:-moz-linear-gradient(top, #599bb3 5%, #1a5c66 100%);\n"
"    background:-webkit-linear-gradient(top, #599bb3 5%, #1a5c66 100%);\n"
"    background:-o-linear-gradient(top, #599bb3 5%, #1a5c66 100%);\n"
"    background:-ms-linear-gradient(top, #599bb3 5%, #1a5c66 100%);\n"
"    background:linear-gradient(to bottom, #599bb3 5%, #1a5c66 100%);\n"
"    background-color:#007dc1;\n"
"    \n"
"    border-radius:3px;\n"
"    border:1px solid #5c298f;\n"
"    color:#ffffff;\n"
"    font-family:arial;\n"
"    font-size:19px;\n"
"    padding:6px 24px;\n"
"    text-decoration:none;\n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"    background:-webkit-gradient(linear, left top, left bottom, color-stop(0.05, #1a5c66), color-stop(1, #599bb3));\n"
"    background:-moz-linear-gradient(top, #1a5c66 5%, #599bb3 100%);\n"
"    background:-webkit-linear-gradient(top, #1a5c66 5%, #599bb3 100%);\n"
"    background:-o-linear-gradient(top, #1a5c66 5%, #599bb3 100%);\n"
"    background:-ms-linear-gradient(top, #1a5c66 5%, #599bb3 100%);\n"
"    background:linear-gradient(to bottom, #1a5c66 5%, #599bb3 100%);\n"
"    background-color:#1a5c66;\n"
"}\n"
"QPushButton:active {\n"
"    position:relative;\n"
"    top:1px;\n"
"}\n"
""))
        self.logInBtn.setObjectName(_fromUtf8("logInBtn"))
        self.horizontalLayout_2.addWidget(self.logInBtn)
        self.cancelBtn = QtGui.QPushButton(LoginDialog)
        self.cancelBtn.setStyleSheet(_fromUtf8(" QPushButton {\n"
"background:-webkit-gradient(linear, left top, left bottom, color-stop(0.05, color: rgb(0, 170, 0);), color-stop(1, #1a5c66));\n"
"    background:-moz-linear-gradient(top, #599bb3 5%, #1a5c66 100%);\n"
"    background:-webkit-linear-gradient(top, #599bb3 5%, #1a5c66 100%);\n"
"    background:-o-linear-gradient(top, #599bb3 5%, #1a5c66 100%);\n"
"    background:-ms-linear-gradient(top, #599bb3 5%, #1a5c66 100%);\n"
"    background:linear-gradient(to bottom, #599bb3 5%, #1a5c66 100%);\n"
"    background-color:#a73f2d;\n"
"    \n"
"    border-radius:3px;\n"
"    border:1px solid #5c298f;\n"
"    color:#ffffff;\n"
"    font-family:arial;\n"
"    font-size:19px;\n"
"    padding:6px 24px;\n"
"    text-decoration:none;\n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"    background:-webkit-gradient(linear, left top, left bottom, color-stop(0.05, #1a5c66), color-stop(1, #599bb3));\n"
"    background:-moz-linear-gradient(top, #1a5c66 5%, #599bb3 100%);\n"
"    background:-webkit-linear-gradient(top, #1a5c66 5%, #599bb3 100%);\n"
"    background:-o-linear-gradient(top, #1a5c66 5%, #599bb3 100%);\n"
"    background:-ms-linear-gradient(top, #1a5c66 5%, #599bb3 100%);\n"
"    background:linear-gradient(to bottom, #1a5c66 5%, #599bb3 100%);\n"
"    background-color:#1a5c66;\n"
"}\n"
"QPushButton:active {\n"
"    position:relative;\n"
"    top:1px;\n"
"}\n"
""))
        self.cancelBtn.setObjectName(_fromUtf8("cancelBtn"))
        self.horizontalLayout_2.addWidget(self.cancelBtn)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.groupbox = QtGui.QGroupBox(LoginDialog)
        self.groupbox.setStyleSheet(_fromUtf8("\n"
"font: 75 10pt \"MS Shell Dlg 2\";"))
        self.groupbox.setObjectName(_fromUtf8("groupbox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupbox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.userName_label = QtGui.QLabel(self.groupbox)
        self.userName_label.setObjectName(_fromUtf8("userName_label"))
        self.verticalLayout_2.addWidget(self.userName_label)
        self.password_lable = QtGui.QLabel(self.groupbox)
        self.password_lable.setObjectName(_fromUtf8("password_lable"))
        self.verticalLayout_2.addWidget(self.password_lable)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.userName_Text = QtGui.QLineEdit(self.groupbox)
        self.userName_Text.setObjectName(_fromUtf8("userName_Text"))
        self.verticalLayout.addWidget(self.userName_Text)
        self.password_ttext = QtGui.QLineEdit(self.groupbox)
        self.password_ttext.setInputMask(_fromUtf8(""))
        self.password_ttext.setObjectName(_fromUtf8("password_ttext"))
        self.verticalLayout.addWidget(self.password_ttext)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addWidget(self.groupbox, 0, 0, 1, 1)
        self.password_ttext.setEchoMode(QLineEdit.Password)

        self.retranslateUi(LoginDialog)

        QtCore.QObject.connect(self.cancelBtn, QtCore.SIGNAL(_fromUtf8("clicked()")),LoginDialog.close )
        QtCore.QObject.connect(self.logInBtn, QtCore.SIGNAL(_fromUtf8("clicked()")),self.logIn)

        QtCore.QMetaObject.connectSlotsByName(LoginDialog)

    def retranslateUi(self, LoginDialog):
        LoginDialog.setWindowTitle(_translate("LoginDialog", "Dialog", None))
        self.logInBtn.setText(_translate("LoginDialog", "LogIn", None))
        self.cancelBtn.setText(_translate("LoginDialog", "Cancel", None))
        self.groupbox.setTitle(_translate("LoginDialog", "LogIn ", None))
        self.userName_label.setText(_translate("LoginDialog", "UerName", None))
        self.password_lable.setText(_translate("LoginDialog", "PassWord", None))

    def logIn(self):

        qu=Mnipul()
        #qu.addUser("amine","Mohamed amine","Smida","123","smidaAmineAchache@gmail.com","Usthb","Student")

        userName=str(self.userName_Text.text())
        passWord=str(self.password_ttext.text())
        #if the user exicet  log in or not
        res,logS=qu.selectUser_LogIN(userName,passWord)
        if not logS :
            self.groupbox.setTitle("Bad User Name Or PassWord")
            self.groupbox.setStyleSheet("color: rgb(255, 0, 0);")
            pass
        else:

            LoginDialog.close()
            form.setUsername(userName)
            form.show()
            form.userName_label.setText(userName)







if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    LoginDialog = QtGui.QDialog()
    form = MainWindow()
    ui = Ui_LoginDialog()
    ui.setupUi(LoginDialog)
    LoginDialog.show()
    sys.exit(app.exec_())

