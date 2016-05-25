# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created: Mon Dec 16 23:06:54 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
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
        self.gridLayout = QtGui.QGridLayout(LoginDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(LoginDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtGui.QLabel(LoginDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.userName_Text = QtGui.QLineEdit(LoginDialog)
        self.userName_Text.setObjectName(_fromUtf8("userName_Text"))
        self.verticalLayout.addWidget(self.userName_Text)
        self.password_ttext = QtGui.QLineEdit(LoginDialog)
        self.password_ttext.setInputMask(_fromUtf8(""))
        self.password_ttext.setObjectName(_fromUtf8("password_ttext"))
        self.verticalLayout.addWidget(self.password_ttext)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.cancelBtn = QtGui.QPushButton(LoginDialog)
        self.cancelBtn.setObjectName(_fromUtf8("cancelBtn"))
        self.horizontalLayout_2.addWidget(self.cancelBtn)
        self.logInBtn = QtGui.QPushButton(LoginDialog)
        self.logInBtn.setObjectName(_fromUtf8("logInBtn"))
        self.horizontalLayout_2.addWidget(self.logInBtn)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.retranslateUi(LoginDialog)
        QtCore.QObject.connect(self.cancelBtn, QtCore.SIGNAL(_fromUtf8("clicked()")),self.cancel )
        QtCore.QObject.connect(self.logInBtn, QtCore.SIGNAL(_fromUtf8("clicked()")),self.logIn)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)

    def retranslateUi(self, LoginDialog):
        LoginDialog.setWindowTitle(_translate("LoginDialog", "Dialog", None))
        self.label.setText(_translate("LoginDialog", "UerName", None))
        self.label_2.setText(_translate("LoginDialog", "PassWord", None))
        self.cancelBtn.setText(_translate("LoginDialog", "Cancel", None))
        self.logInBtn.setText(_translate("LoginDialog", "LogIn", None))

    def logIn(self):

        qu=Mnipul()
        userName=str(self.userName_Text.text())
        passWord=str(self.password_ttext.text())
        #if the user exicet  log in or not
        res,logS=qu.selectUser_LogIN(userName,passWord)
        if not logS :
            pass
        else:

            LoginDialog.close()
            form.setUsername(userName)
            form.show()
            form.userName_label.setText(userName)
            form.userId=res.id




    def cancel(self):
        print "cancel"


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    LoginDialog = QtGui.QDialog()
    form = MainWindow()
    ui = Ui_LoginDialog()
    ui.setupUi(LoginDialog)
    LoginDialog.show()
    sys.exit(app.exec_())

