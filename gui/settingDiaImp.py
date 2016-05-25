__author__ = 'TOSHIBA'
from PyQt4.QtGui import QDialog
from PyQt4 import QtCore

from com.smidaAmineAchache.models.queries import Mnipul
import settingDia


class SettingDiaIm(QDialog,settingDia.Ui_Dialog):
    dataM=Mnipul()

    def __init__(self,parrent=None):
        super(SettingDiaIm,self).__init__(parrent)
        self.setupUi(self)
        QtCore.QObject.connect(self.save_btn, QtCore.SIGNAL(settingDia._fromUtf8("clicked()")),self.saveSetting )
        QtCore.QObject.connect(self.cancel_btn, QtCore.SIGNAL(settingDia._fromUtf8("clicked()")),self.cancel )
        self.useInter_check.clicked.connect(self.saveSetting)
        self.maxDc_spinV.setRange(0,200)
        self.minPla_SpinV.setRange(0,100)



    def saveSetting(self):

        if self.useInter_check.isChecked():
            useInt=1
            print useInt
        else:

            useInt=0
            print useInt
        maxDoc=int(self.maxDc_spinV.text())
        minPla=int(self.minPla_SpinV.text())
        self.dataM.saveSetting(useInt,maxDoc,minPla)
        self.close()


    def cancel(self):
        self.close()