# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Thu Dec 26 00:14:42 2013
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(936, 576)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setStyleSheet(_fromUtf8("color: rgb(85, 0, 255);\n"
"font: 14pt \"Consolas\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.userName_label = QtGui.QLabel(self.groupBox)
        self.userName_label.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);\n"
"font: 14pt \"MS Shell Dlg 2\";"))
        self.userName_label.setText(_fromUtf8(""))
        self.userName_label.setObjectName(_fromUtf8("userName_label"))
        self.horizontalLayout_2.addWidget(self.userName_label)
        self.gridLayout_3.addWidget(self.groupBox, 0, 1, 1, 1)
        self.status_label = QtGui.QLabel(self.centralwidget)
        self.status_label.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\"\n"
"rgb(255, 0, 0)"))
        self.status_label.setText(_fromUtf8(""))
        self.status_label.setObjectName(_fromUtf8("status_label"))
        self.gridLayout_3.addWidget(self.status_label, 0, 0, 1, 1)
        self.groupBox1 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox1.setObjectName(_fromUtf8("groupBox1"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox1)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.loadFile = QtGui.QPushButton(self.groupBox1)
        self.loadFile.setStyleSheet(_fromUtf8(" QPushButton {\n"
"background:-webkit-gradient(linear, left top, left bottom, color-stop(0.05, #599bb3), color-stop(1, #1a5c66));\n"
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
        self.loadFile.setObjectName(_fromUtf8("loadFile"))
        self.horizontalLayout.addWidget(self.loadFile)
        self.testPlagia_btn = QtGui.QPushButton(self.groupBox1)
        self.testPlagia_btn.setStyleSheet(_fromUtf8(" QPushButton {\n"
"background:-webkit-gradient(linear, left top, left bottom, color-stop(0.05, #599bb3), color-stop(1, #1a5c66));\n"
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
        self.testPlagia_btn.setObjectName(_fromUtf8("testPlagia_btn"))
        self.horizontalLayout.addWidget(self.testPlagia_btn)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox1)
        self.label_3.setStyleSheet(_fromUtf8("color: rgb(170, 0, 0);\n"
"font: 14pt \"MS Shell Dlg 2\";"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.scrollArea = QtGui.QScrollArea(self.groupBox1)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 588, 162))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_4 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.textBrows = QtGui.QTextEdit(self.scrollAreaWidgetContents)
        self.textBrows.setEnabled(True)
        self.textBrows.setStyleSheet(_fromUtf8("font: 9pt \"MS Shell Dlg 2\";"))
        self.textBrows.setObjectName(_fromUtf8("textBrows"))
        self.gridLayout_4.addWidget(self.textBrows, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.label_5 = QtGui.QLabel(self.groupBox1)
        self.label_5.setStyleSheet(_fromUtf8("color: rgb(170, 0, 0);\n"
"font: 14pt \"MS Shell Dlg 2\";"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_2.addWidget(self.label_5)
        self.scrollArea_2 = QtGui.QScrollArea(self.groupBox1)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 588, 162))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.gridLayout = QtGui.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.texBrows_original = QtGui.QTextBrowser(self.scrollAreaWidgetContents_2)
        self.texBrows_original.setEnabled(True)
        self.texBrows_original.setStyleSheet(_fromUtf8("font: 9pt \"MS Shell Dlg 2\";"))
        self.texBrows_original.setObjectName(_fromUtf8("texBrows_original"))
        self.gridLayout.addWidget(self.texBrows_original, 0, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.scrollArea_2)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 2, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox1, 1, 0, 1, 1)
        self.groupBox2 = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox2.sizePolicy().hasHeightForWidth())
        self.groupBox2.setSizePolicy(sizePolicy)
        self.groupBox2.setObjectName(_fromUtf8("groupBox2"))
        self.gridLayout_6 = QtGui.QGridLayout(self.groupBox2)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.groupBox3 = QtGui.QGroupBox(self.groupBox2)
        self.groupBox3.setTitle(_fromUtf8(""))
        self.groupBox3.setObjectName(_fromUtf8("groupBox3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBox3)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(self.groupBox3)
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(0, 0, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.plagiaResult = QtGui.QLabel(self.groupBox3)
        self.plagiaResult.setStyleSheet(_fromUtf8("color: rgb(170, 0, 0);\n"
"font: 14pt \"MS Shell Dlg 2\";"))
        self.plagiaResult.setText(_fromUtf8(""))
        self.plagiaResult.setObjectName(_fromUtf8("plagiaResult"))
        self.horizontalLayout_3.addWidget(self.plagiaResult)
        self.gridLayout_6.addWidget(self.groupBox3, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.repport_btn = QtGui.QPushButton(self.groupBox2)
        self.repport_btn.setStyleSheet(_fromUtf8(" QPushButton {\n"
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
        self.repport_btn.setObjectName(_fromUtf8("repport_btn"))
        self.horizontalLayout_4.addWidget(self.repport_btn)
        self.sava_btn = QtGui.QPushButton(self.groupBox2)
        self.sava_btn.setStyleSheet(_fromUtf8(" QPushButton {\n"
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
        self.sava_btn.setObjectName(_fromUtf8("sava_btn"))
        self.horizontalLayout_4.addWidget(self.sava_btn)
        self.gridLayout_6.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(self.groupBox2)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.Page1 = QtGui.QWidget()
        self.Page1.setObjectName(_fromUtf8("Page1"))
        self.gridLayout_5 = QtGui.QGridLayout(self.Page1)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.docs_Rsult_ListView = QtGui.QListView(self.Page1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.docs_Rsult_ListView.sizePolicy().hasHeightForWidth())
        self.docs_Rsult_ListView.setSizePolicy(sizePolicy)
        self.docs_Rsult_ListView.setObjectName(_fromUtf8("docs_Rsult_ListView"))
        self.gridLayout_5.addWidget(self.docs_Rsult_ListView, 0, 0, 1, 1)
        self.tabWidget.addTab(self.Page1, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_7 = QtGui.QGridLayout(self.tab)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.docs_Rsult_ListView_2 = QtGui.QListView(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.docs_Rsult_ListView_2.sizePolicy().hasHeightForWidth())
        self.docs_Rsult_ListView_2.setSizePolicy(sizePolicy)
        self.docs_Rsult_ListView_2.setObjectName(_fromUtf8("docs_Rsult_ListView_2"))
        self.gridLayout_7.addWidget(self.docs_Rsult_ListView_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.gridLayout_6.addWidget(self.tabWidget, 2, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox2, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 936, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuAdmin = QtGui.QMenu(self.menubar)
        self.menuAdmin.setObjectName(_fromUtf8("menuAdmin"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_File = QtGui.QAction(MainWindow)
        self.actionNew_File.setObjectName(_fromUtf8("actionNew_File"))
        self.actionADD_user = QtGui.QAction(MainWindow)
        self.actionADD_user.setObjectName(_fromUtf8("actionADD_user"))
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionSetting = QtGui.QAction(MainWindow)
        self.actionSetting.setObjectName(_fromUtf8("actionSetting"))
        self.menuFile.addAction(self.actionNew_File)
        self.menuFile.addAction(self.actionClose)
        self.menuAdmin.addAction(self.actionADD_user)
        self.menuEdit.addAction(self.actionSetting)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuAdmin.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.actionClose, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "User Name :", None))
        self.groupBox1.setTitle(_translate("MainWindow", "Doc Test", None))
        self.loadFile.setText(_translate("MainWindow", "Load File", None))
        self.testPlagia_btn.setText(_translate("MainWindow", "Start Test", None))
        self.label_3.setText(_translate("MainWindow", "Document From loacal /Web", None))
        self.label_5.setText(_translate("MainWindow", "Document Tested For Plagia", None))
        self.groupBox2.setTitle(_translate("MainWindow", "Results", None))
        self.label_2.setText(_translate("MainWindow", "Result", None))
        self.repport_btn.setText(_translate("MainWindow", "Repport", None))
        self.sava_btn.setText(_translate("MainWindow", "Save", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Page1), _translate("MainWindow", "Local", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Web", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuAdmin.setTitle(_translate("MainWindow", "Admin", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.actionNew_File.setText(_translate("MainWindow", "New File", None))
        self.actionADD_user.setText(_translate("MainWindow", "ADD user", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))
        self.actionSetting.setText(_translate("MainWindow", "Setting", None))

