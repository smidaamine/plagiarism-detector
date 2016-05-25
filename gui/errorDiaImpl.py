from PyQt4.QtGui import QDialog
from com.smidaAmineAchache.gui import errorDia

__author__ = 'TOSHIBA'

class ErrorDia(QDialog,errorDia.Ui_labl_message):


    def __init__(self,parrent=None):
        super(ErrorDia,self).__init__(parrent)
        self.setupUi(self)

