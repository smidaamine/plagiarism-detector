# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'errorDia.ui'
#
# Created: Mon Dec 23 20:17:01 2013
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

class Ui_labl_message(object):
    def setupUi(self, labl_message):
        labl_message.setObjectName(_fromUtf8("labl_message"))
        labl_message.resize(389, 161)
        labl_message.setStyleSheet(_fromUtf8("\n"
"background-color: rgb(255, 255, 255);"))
        self.gridLayout = QtGui.QGridLayout(labl_message)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(labl_message)
        self.label.setStyleSheet(_fromUtf8("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 255);"))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtGui.QPushButton(labl_message)
        self.pushButton.setStyleSheet(_fromUtf8(" QPushButton {\n"
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
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(labl_message)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), labl_message.close)
        QtCore.QMetaObject.connectSlotsByName(labl_message)

    def retranslateUi(self, labl_message):
        labl_message.setWindowTitle(_translate("labl_message", "Dialog", None))
        self.pushButton.setText(_translate("labl_message", "Ok", None))

