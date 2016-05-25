# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addDoc.ui'
#
# Created: Fri Dec 20 17:26:38 2013
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(419, 361)
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(9, 319, 381, 35))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.saveBtn = QtGui.QPushButton(self.layoutWidget)
        self.saveBtn.setStyleSheet(_fromUtf8(" QPushButton {\n"
"background:-webkit-gradient(linear, left top, left bottom, color-stop(0.05, color: rgb(0, 170, 0);), color-stop(1, #1a5c66));\n"
"    background:-moz-linear-gradient(top, #599bb3 5%, #1a5c66 100%);\n"
"    background:-webkit-linear-gradient(top, #599bb3 5%, #1a5c66 100%);\n"
"    background:-o-linear-gradient(top, #599bb3 5%, #1a5c66 100%);\n"
"    background:-ms-linear-gradient(top, #599bb3 5%, #1a5c66 100%);\n"
"    background:linear-gradient(to bottom, #599bb3 5%, #1a5c66 100%);\n"
"    background-color:#599bb3;\n"
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
        self.saveBtn.setObjectName(_fromUtf8("saveBtn"))
        self.horizontalLayout_2.addWidget(self.saveBtn)
        self.cancel_btn = QtGui.QPushButton(self.layoutWidget)
        self.cancel_btn.setStyleSheet(_fromUtf8(" QPushButton {\n"
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
        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
        self.horizontalLayout_2.addWidget(self.cancel_btn)
        self.layoutWidget1 = QtGui.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(11, 224, 371, 91))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_6 = QtGui.QLabel(self.layoutWidget1)
        self.label_6.setStyleSheet(_fromUtf8("font: 75 10pt \"MS Shell Dlg 2\";"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout.addWidget(self.label_6)
        self.textEdit = QtGui.QTextEdit(self.layoutWidget1)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.horizontalLayout.addWidget(self.textEdit)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(11, 11, 371, 211))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setStyleSheet(_fromUtf8("font: 75 10pt \"MS Shell Dlg 2\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setStyleSheet(_fromUtf8("font: 75 10pt \"MS Shell Dlg 2\";"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setStyleSheet(_fromUtf8("font: 75 10pt \"MS Shell Dlg 2\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setStyleSheet(_fromUtf8("font: 75 10pt \"MS Shell Dlg 2\";"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.pathEdit = QtGui.QLineEdit(self.groupBox)
        self.pathEdit.setObjectName(_fromUtf8("pathEdit"))
        self.verticalLayout_2.addWidget(self.pathEdit)
        self.addByEdit = QtGui.QLineEdit(self.groupBox)
        self.addByEdit.setObjectName(_fromUtf8("addByEdit"))
        self.verticalLayout_2.addWidget(self.addByEdit)
        self.plagiaLvl_edit = QtGui.QLineEdit(self.groupBox)
        self.plagiaLvl_edit.setObjectName(_fromUtf8("plagiaLvl_edit"))
        self.verticalLayout_2.addWidget(self.plagiaLvl_edit)
        self.titleEdit = QtGui.QLineEdit(self.groupBox)
        self.titleEdit.setObjectName(_fromUtf8("titleEdit"))
        self.verticalLayout_2.addWidget(self.titleEdit)
        self.statEdit = QtGui.QLineEdit(self.groupBox)
        self.statEdit.setObjectName(_fromUtf8("statEdit"))
        self.verticalLayout_2.addWidget(self.statEdit)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.saveBtn.setText(_translate("Dialog", "Save", None))
        self.cancel_btn.setText(_translate("Dialog", "Cancel", None))
        self.label_6.setText(_translate("Dialog", "PS      ", None))
        self.groupBox.setTitle(_translate("Dialog", "Dcument Informatins", None))
        self.label.setText(_translate("Dialog", "Path/id", None))
        self.label_5.setText(_translate("Dialog", "ADD by", None))
        self.label_3.setText(_translate("Dialog", "Palagia LvL", None))
        self.label_2.setText(_translate("Dialog", "Title", None))
        self.label_4.setText(_translate("Dialog", "State", None))

