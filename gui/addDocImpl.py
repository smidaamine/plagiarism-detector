from PyQt4.QtGui import QDialog
from com.smidaAmineAchache.models.queries import Mnipul

__author__ = 'TOSHIBA'

from PyQt4 import QtCore
import AddDoc
class AddDocD(QDialog,AddDoc.Ui_Dialog):
    dataM=Mnipul()

    def __init__(self,parrent=None):
        super(AddDocD,self).__init__(parrent)
        self.setupUi(self)
        QtCore.QObject.connect(self.saveBtn, QtCore.SIGNAL(AddDoc._fromUtf8("clicked()")),self.getEns )
        QtCore.QObject.connect(self.cancel_btn, QtCore.SIGNAL(AddDoc._fromUtf8("clicked()")),self.cancel )


    def getEns(self):
        listData=[]
        path=str(self.pathEdit.text())
        title=str(self.titleEdit.text())
        state=str(self.statEdit.text())
        addby=str(self.addByEdit.text())
        ps=str(self.textEdit.toPlainText())
        plagiaSim=str(self.plagiaLvl_edit.text())
        fileTemp=open(path)
        pathNew="DATA\\Doc"+str(1+len(self.dataM.selectAllDocs()))+".txt"
        fileNew=open(pathNew,'w')
        fileNew.write(fileTemp.read())
        fileNew.close()
        fileTemp.close()
        self.dataM.addDoc(pathNew,title,addby,ps,state,plagiaSim)
        self.close()

        return listData
    def cancel(self):
        self.close()