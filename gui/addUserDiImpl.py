__author__ = 'SMIDA'

from PyQt4.QtGui import QDialog
from PyQt4 import QtCore

from com.smidaAmineAchache.models.queries import Mnipul
import addUserD


class AddUserDia(QDialog,addUserD.Ui_AddUserDialog):
    dataM=Mnipul()

    def __init__(self,parrent=None):
        super(AddUserDia,self).__init__(parrent)
        self.setupUi(self)
        QtCore.QObject.connect(self.save_Btn, QtCore.SIGNAL(addUserD._fromUtf8("clicked()")),self.saveUser )
        QtCore.QObject.connect(self.cancel_Btn, QtCore.SIGNAL(addUserD._fromUtf8("clicked()")),self.cancel )


    def saveUser(self):

        name=str(self.userName_edit.text())
        first_name=str(self.firstName_edit.text())
        last_name=str(self.lastName_edit.text())
        password=str(self.password_edit.text())
        email=str(self.email_edit.text())
        univ_name=str(self.univ_edit.text())
        profision=str(self.prof_edit.text())

        try:
            self.dataM.addUser(name,first_name,last_name,password,email,univ_name,profision)
            self.close()
        except:
            print "kllk"

    def cancel(self):
        self.close()
