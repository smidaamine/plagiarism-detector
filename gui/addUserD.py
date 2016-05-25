# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addUserDialog.ui'
#
# Created: Thu Dec 19 18:56:33 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_AddUserDialog(object):
    def setupUi(self, AddUserDialog):
        AddUserDialog.setObjectName(_fromUtf8("AddUserDialog"))
        AddUserDialog.resize(496, 401)
        AddUserDialog.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.widget = QtGui.QWidget(AddUserDialog)
        self.widget.setGeometry(QtCore.QRect(10, 340, 451, 38))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.save_Btn = QtGui.QPushButton(self.widget)
        self.save_Btn.setStyleSheet(_fromUtf8(" QPushButton {\n"
"background:-webkit-gradient(linear, left top, left bottom, color-stop(0.05, color: rgb(0, 170, 0);), color-stop(1, #1a5c66));\n"
"    background:-moz-linear-gradient(top, #599bb3 5%, #1a5c66 100%);\n"
"    background:-webkit-linear-gradient(top, #599bb3 5%, #1a5c66 100%);\n"
"    background:-o-linear-gradient(top, #599bb3 5%, #1a5c66 100%);\n"
"    background:-ms-linear-gradient(top, #599bb3 5%, #1a5c66 100%);\n"
"    background:linear-gradient(to bottom, #599bb3 5%, #1a5c66 100%);\n"
"    background-color:#77d42a;\n"
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
        self.save_Btn.setObjectName(_fromUtf8("save_Btn"))
        self.horizontalLayout_2.addWidget(self.save_Btn)
        self.cancel_Btn = QtGui.QPushButton(self.widget)
        self.cancel_Btn.setStyleSheet(_fromUtf8(" QPushButton {\n"
"background:-webkit-gradient(linear, left top, left bottom, color-stop(0.05, color: rgb(0, 170, 0);), color-stop(1, #1a5c66));\n"
"    background:-moz-linear-gradient(top, #599bb3 5%, #1a5c66 100%);\n"
"    background:-webkit-linear-gradient(top, #599bb3 5%, #1a5c66 100%);\n"
"    background:-o-linear-gradient(top, #599bb3 5%, #1a5c66 100%);\n"
"    background:-ms-linear-gradient(top, #599bb3 5%, #1a5c66 100%);\n"
"    background:linear-gradient(to bottom, #599bb3 5%, #1a5c66 100%);\n"
"    background-color:#fe1a00;\n"
"    \n"
"    border-radius:3px;\n"
"    border:1px solid #5c298f;\n"
"    color:#ffffff;\n"
"    font-family:arial;\n"
"    font-size:17px;\n"
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
        self.cancel_Btn.setObjectName(_fromUtf8("cancel_Btn"))
        self.horizontalLayout_2.addWidget(self.cancel_Btn)
        self.groupbox = QtGui.QGroupBox(AddUserDialog)
        self.groupbox.setGeometry(QtCore.QRect(10, 10, 451, 315))
        self.groupbox.setStyleSheet(_fromUtf8("font: 75 12pt \"MS Shell Dlg 2\";"))
        self.groupbox.setObjectName(_fromUtf8("groupbox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupbox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.userName_label = QtGui.QLabel(self.groupbox)
        self.userName_label.setObjectName(_fromUtf8("userName_label"))
        self.verticalLayout.addWidget(self.userName_label)
        self.firstName_label = QtGui.QLabel(self.groupbox)
        self.firstName_label.setObjectName(_fromUtf8("firstName_label"))
        self.verticalLayout.addWidget(self.firstName_label)
        self.lastName_labe = QtGui.QLabel(self.groupbox)
        self.lastName_labe.setObjectName(_fromUtf8("lastName_labe"))
        self.verticalLayout.addWidget(self.lastName_labe)
        self.passwor_lable = QtGui.QLabel(self.groupbox)
        self.passwor_lable.setObjectName(_fromUtf8("passwor_lable"))
        self.verticalLayout.addWidget(self.passwor_lable)
        self.email_Lable = QtGui.QLabel(self.groupbox)
        self.email_Lable.setObjectName(_fromUtf8("email_Lable"))
        self.verticalLayout.addWidget(self.email_Lable)
        self.univ_lable = QtGui.QLabel(self.groupbox)
        self.univ_lable.setObjectName(_fromUtf8("univ_lable"))
        self.verticalLayout.addWidget(self.univ_lable)
        self.label_4 = QtGui.QLabel(self.groupbox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.userName_edit = QtGui.QLineEdit(self.groupbox)
        self.userName_edit.setObjectName(_fromUtf8("userName_edit"))
        self.verticalLayout_2.addWidget(self.userName_edit)
        self.firstName_edit = QtGui.QLineEdit(self.groupbox)
        self.firstName_edit.setObjectName(_fromUtf8("firstName_edit"))
        self.verticalLayout_2.addWidget(self.firstName_edit)
        self.lastName_edit = QtGui.QLineEdit(self.groupbox)
        self.lastName_edit.setObjectName(_fromUtf8("lastName_edit"))
        self.verticalLayout_2.addWidget(self.lastName_edit)
        self.password_edit = QtGui.QLineEdit(self.groupbox)
        self.password_edit.setObjectName(_fromUtf8("password_edit"))
        self.verticalLayout_2.addWidget(self.password_edit)
        self.email_edit = QtGui.QLineEdit(self.groupbox)
        self.email_edit.setObjectName(_fromUtf8("email_edit"))
        self.verticalLayout_2.addWidget(self.email_edit)
        self.univ_edit = QtGui.QLineEdit(self.groupbox)
        self.univ_edit.setObjectName(_fromUtf8("univ_edit"))
        self.verticalLayout_2.addWidget(self.univ_edit)
        self.prof_edit = QtGui.QLineEdit(self.groupbox)
        self.prof_edit.setObjectName(_fromUtf8("prof_edit"))
        self.verticalLayout_2.addWidget(self.prof_edit)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(AddUserDialog)
        QtCore.QMetaObject.connectSlotsByName(AddUserDialog)

    def retranslateUi(self, AddUserDialog):
        AddUserDialog.setWindowTitle(_translate("AddUserDialog", "Dialog", None))
        self.save_Btn.setText(_translate("AddUserDialog", "Save", None))
        self.cancel_Btn.setText(_translate("AddUserDialog", "Cancel", None))
        self.groupbox.setTitle(_translate("AddUserDialog", "User Informations", None))
        self.userName_label.setText(_translate("AddUserDialog", "UserName", None))
        self.firstName_label.setText(_translate("AddUserDialog", "First Name", None))
        self.lastName_labe.setText(_translate("AddUserDialog", "Last Name", None))
        self.passwor_lable.setText(_translate("AddUserDialog", "PassWord", None))
        self.email_Lable.setText(_translate("AddUserDialog", "Email", None))
        self.univ_lable.setText(_translate("AddUserDialog", "Univ", None))
        self.label_4.setText(_translate("AddUserDialog", "Proff", None))

