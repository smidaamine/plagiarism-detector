from urllib import urlopen
from PyQt4.QtGui import QMainWindow, QFileDialog, QStandardItemModel, QStandardItem
from com.smidaAmineAchache.gui import addDocImpl
from com.smidaAmineAchache.gui import errorDiaImpl
from com.smidaAmineAchache.gui.addUserDiImpl import AddUserDia
from com.smidaAmineAchache.gui.settingDiaImp import SettingDiaIm
from com.smidaAmineAchache.models.queries import Mnipul
from com.smidaAmineAchache.nlp.nlpFunctions import NlpFunc
from com.smidaAmineAchache.plagia.PlagiaUtil import PlagiaUtils
from com.smidaAmineAchache.plagia.PlagiaUtil import Websearch,convert_pdf_To_Txt,cleanHtml

__author__ = 'TOSHIBA'
from PyQt4 import QtCore
import mainWindow

import re



class MainWindow(QMainWindow,mainWindow.Ui_MainWindow):
    ## user Log Name
    userName=""
    ##
    userId=""
    ##File path (file want to scan)
    fileToScan=""
    ##trigram sequences (file we want to scan)
    trigToScan=[]
    ngram=[]

    ## object of the class NlpFunc
    nlpFunc=NlpFunc()
    ##object for data base manipulation
    dataM=Mnipul()
    ##list of all docs in data Base
    docsData=""
    plagiaFunc=PlagiaUtils()
    ##Qlist for all document tested
    setting=""
    textPlagia={}
    result={}
    resultWeb={}
    webUtil=Websearch()
    ##list of dic trigaram from the web key: is the wed address
    ##and value is tuple (trigram,text)
    docWebTrigram={}
    ##all trigram mach
    resultList=[]
    ## repport generated
    repportGen={}


    def __init__(self,parrent=None):
        super(MainWindow,self).__init__(parrent)
        self.setupUi(self)
        QtCore.QObject.connect(self.loadFile, QtCore.SIGNAL(mainWindow._fromUtf8("clicked()")), self.loadFile_btn_Kliked)
        QtCore.QObject.connect(self.testPlagia_btn, QtCore.SIGNAL(mainWindow._fromUtf8("clicked()")), self.plagiaStrat_btn)
        QtCore.QObject.connect(self.repport_btn, QtCore.SIGNAL(mainWindow._fromUtf8("clicked()")), self.repport)
        QtCore.QObject.connect(self.sava_btn, QtCore.SIGNAL(mainWindow._fromUtf8("clicked()")), self.saveFile)

        QtCore.QObject.connect(self.actionNew_File, QtCore.SIGNAL(mainWindow._fromUtf8("triggered()")), self.loadFile_btn_Kliked)
        QtCore.QObject.connect(self.actionADD_user, QtCore.SIGNAL(mainWindow._fromUtf8("triggered()")), self.addUser)
        QtCore.QObject.connect(self.actionSetting, QtCore.SIGNAL(mainWindow._fromUtf8("triggered()")), self.setting)
        #QtCore.QObject.connect(self.docs_Rsult_ListView, QtCore.SIGNAL(mainWindow._fromUtf8("clicked()")), self.listViewChange)
        QtCore.QObject.connect(self.docs_Rsult_ListView, QtCore.SIGNAL(mainWindow._fromUtf8("clicked(QModelIndex)")), self.listViewChange)
        QtCore.QObject.connect(self.docs_Rsult_ListView_2, QtCore.SIGNAL(mainWindow._fromUtf8("clicked(QModelIndex)")), self.listViewWebChange)

        self.userName_label.setText(self.userName)
        self.dialogDoc=addDocImpl.AddDocD()

        self.addUserDia=AddUserDia()
        self.settingD=SettingDiaIm()
        self.dialogMe=errorDiaImpl.ErrorDia()
        self.modelList=QStandardItemModel(self.docs_Rsult_ListView)
        self.modelListWeb=QStandardItemModel(self.docs_Rsult_ListView_2)
        self.setting=self.dataM.getSetting()
        self.sava_btn.setEnabled(False)
        self.repport_btn.setEnabled(False)



    ##save btn action
    def saveFile(self):
        self.dialogDoc.show()

    ##report btn action
    def repport(self):
        filename = QFileDialog.getSaveFileName(self, 'Save File', '.')
        keyL="Number of Files found In local data Base"
        keyWeb="Number of files from the web"
        if len(filename)!=0:
            fname = open(filename, 'w')

            txt=keyL+" "+str(self.repportGen.get(keyL))
            txt=txt+"\n" +keyWeb+" " +str(self.repportGen.get(keyWeb))


            for key in sorted(self.repportGen,key=self.repportGen.get):
                if key != keyL and keyWeb:
                    txt=txt+"\n"+self.repportGen[key]

            fname.write(txt)
            fname.close()
            #print self.repportGen

        #print "amine   "



    ## Load Btn method

    def loadFile_btn_Kliked(self):
        ##load file that we want and generats trigrames
        self.fileToScan=QFileDialog.getOpenFileName()
        fileTemp=open("tempFilePdf.txt","w")
        if(re.search(".+\.pdf",self.fileToScan)):
            #print  self.fileToScan
            pdf2Txt=convert_pdf_To_Txt(path=self.fileToScan)
            #print pdf2Txt
            fileTemp.write(pdf2Txt)
            fileTemp.close()
            self.fileToScan="tempFilePdf.txt"
        elif (re.search(".+\.txt",self.fileToScan)):
            pass
        else:
            self.dialogMe.label.setText("Pls Select a .txt or .pdf File" )
            self.dialogMe.show()
            return



        if len(self.fileToScan)!=0:
            text=open(self.fileToScan).read().strip()
            self.trigToScan=self.nlpFunc.processText(text,3)
            self.ngram=self.nlpFunc.processText(text,5)

            self.texBrows_original.setText(text)



        #self.dataM.addDoc(2,"C:\\Users\\TOSHIBA\\Desktop\\Projet-Tal\\TALN-projet\\DATA\\doc-1.txt",datetime.date(1988,12,01),"admin",self.userName)


    def plagiaStrat_btn(self):

        listdocs=self.loadFiles_data()

        #resultList={}
        for doc in listdocs:


            docTxt=open(doc.path).read()
            temp,matchWords=self.plagiaFunc.jaccardSimilarity(self.trigToScan,self.nlpFunc.processText(docTxt,3))
            #self.resultList[doc.path]=temp
            self.result[doc.path]=(temp,matchWords)
            self.plagiaResult.setText(str(temp))
            #self.dialogDoc.plagiaLvl_edit.setText(str(temp))
            #self.dialogDoc.plagiaLvl_edit.setEnabled(False)
            #self.dialogDoc.show()
            self.dialogDoc.pathEdit.setText(self.fileToScan)
            self.dialogDoc.pathEdit.setEnabled(False)
            self.dialogDoc.addByEdit.setText(self.userName)
            self.dialogDoc.addByEdit.setEnabled(False)
        if self.setting.USE_INT==1:

            for gram in self.ngram:
                if self.plagiaWeb(" ".join(gram))!=0:
                    break

            ##web
            docCount=0
            for key  in self.docWebTrigram:
                webtemp=open("DATA\\webTemp\\"+str(docCount)+".txt","w")
                webtemp.write(self.docWebTrigram[key][1])
                ## get the text
                docTxt=self.docWebTrigram[key][1]
                temp,matchWords=self.plagiaFunc.jaccardSimilarity(self.trigToScan,self.docWebTrigram[key][0])
                #resultList[key]=temp
                self.resultWeb[key]=(temp,matchWords)
                self.plagiaResult.setText(str(temp))
              #  self.dialogDoc.plagiaLvl_edit.setText(str(temp))
             #   self.dialogDoc.plagiaLvl_edit.setEnabled(False)
                #self.dialogDoc.show()
                self.dialogDoc.pathEdit.setText(self.fileToScan)
                self.dialogDoc.pathEdit.setEnabled(False)
                self.dialogDoc.addByEdit.setText(self.userName)
                self.dialogDoc.addByEdit.setEnabled(False)
                webtemp.close()
                docCount+=1

            self.setListViewWeb(self.resultWeb)

        self.sava_btn.setEnabled(True)
        self.repport_btn.setEnabled(True)



        self.setListView(self.result)
        self.texBrows_original.setHtml(open(self.fileToScan).read())



    def plagiaWeb(self,query):

        """
        send requet and get pdf file  if we find
        """

        trigram={}
        pdfFile=""
        urls=self.webUtil.Websarch(query,self.setting.MAX_DOC)
        for url in urls:
            #self.status_label.clear()
            #self.status_label.setText("Download:"+url)

            #self.repaint()

            if re.search(".+\.pdf",url):
                tempwebFile=open("WebtempFile.txt","wb")
                #print "this is url"+url
                pdfFile,key=self.webUtil.readPdfWeb(url)
                if pdfFile!=None:
                    try:
                        pdfFile=convert_pdf_To_Txt(pdfFile)
                        #print "*******************************************************"
                        #print pdfFile
                        #print "********************************************************"

                        tempwebFile.write(pdfFile)
                        tempwebFile.close()
                        self.docWebTrigram[key]=(self.nlpFunc.processText(pdfFile,3),pdfFile)
                    except:
                        print "error"

            if re.search(".+\.html",url):
                page = urlopen(url).read()
                tempwebFile=open("WebtempFile.txt","wb")
                if len(page)!=0:
                    page=cleanHtml(page)
                    tempwebFile.write(page)
                    tempwebFile.close()
                    self.docWebTrigram[url]=(self.nlpFunc.processText(page,3),page)



        self.status_label.setText("END.")
        return len(trigram.keys()),"len keys /*/*//*/*/*"




    def colorTextMach(self,text,listWord):
        """
        color tex that match trigramme
        """
        text=text.strip()
        for word in listWord:
            for i in range(3):
                if "[NUM]" not in word:
                    pattern=word[i]+u"([a-zA-Z]*)(\b*)"
                    #pattern='^(?=.*?\b'+word[0]+'(\b+))(?=.*?\b'+word[1]+'\b+)(?=.*?\b'+word[2]+'\b+).*$'
                    tw=str(word[i])
                    w=u" <strong style=\"background-color: #FFFF00\">"+tw+u"</strong> "
                    text=re.sub(pattern.encode("utf-8"),w.encode("utf-8"),text)

        return text


    def listViewChange(self,index):
        """
        brows text whe user  select document from list view
        """
        self.textBrows.clear()
        key= str(index.data().toString())

        path=re.findall("(DATA\\\\.+.txt)",key)

        value=re.findall("(\d+.\d+)$",key)
        #print value[0]
        self.plagiaResult.setText(value[0])



        colorTxt=self.colorTextMach(open(path[0]).read(),self.result[path[0]][1])
        colorTextPlg=self.colorTextMach(open(self.fileToScan).read(),self.result[path[0]][1])
        self.textBrows.setHtml(colorTxt)
        self.texBrows_original.setHtml(colorTextPlg)

    def listViewWebChange(self,index):
            """
            brows text whe user  select document from list view
            """
            self.textBrows.clear()
            key= str(index.data().toString())

            path=re.findall("(.+.pdf)",key)
            value=re.findall("(\d+.\d+)$",key)
            #print value[0]
            self.plagiaResult.setText(value[0])


            #print self.docWebTrigram[path[0]][1]

            colorTxt=self.colorTextMach(self.docWebTrigram[path[0]][1],self.resultWeb[path[0]][1])

            colorTextPlg=self.colorTextMach(open(self.fileToScan).read(),self.resultWeb[path[0]][1])
            self.textBrows.setHtml(colorTxt)
            self.texBrows_original.setHtml(colorTextPlg)

    def setListView(self,listDic):
        """
        add element to the list view
        """
        index=0
        self.modelList.clear()
        nbDoc=0
        for keys in sorted(listDic,key=listDic.get,reverse=True):
            if listDic[keys][0] >self.setting.MIN_PLAGIA/100.0 and index <self.setting.MAX_DOC:
                nbDoc+=1
                self.repportGen["Number of Files found In local data Base"]=nbDoc
                te=str(keys)+"  "+str(round(listDic[keys][0],2)*100)
                self.repportGen[keys]="LOCAL:"+str(nbDoc)+'-'+te+" %"

                itme=QStandardItem(te)
                self.modelList.appendRow(itme)
                self.docs_Rsult_ListView.setModel(self.modelList)
                index=index+1

    def setListViewWeb(self,listDic):
        """
        add element to the list view
        """
        index=0
        self.modelListWeb.clear()
        nbDoc=0
        for keys in sorted(listDic,key=listDic.get,reverse=True):
            if listDic[keys][0] >0.0 and index <self.setting.MAX_DOC:
                nbDoc+=1
                self.repportGen["Number of files from the web"]=nbDoc
                te=str(keys)+"  "+str(round(listDic[keys][0],2)*100)
                self.repportGen[keys]="WEB:"+str(nbDoc)+'-'+te+" %"
                itme=QStandardItem(te)
                self.modelListWeb.appendRow(itme)
                self.docs_Rsult_ListView_2.setModel(self.modelListWeb)
                index=index+1


    ##load all files from data Base
    def loadFiles_data(self):
        return self.dataM.selectAllDocs()



     ##setter User Name
    def setUsername(self,userName):
        self.userName=userName


    ##add new user
    def addUser(self):
        #self.dataM.addUser()
        self.addUserDia.show()

    ##setting
    def setting(self):

        if self.setting.USE_INT==1:
            self.settingD.useInter_check.setChecked(True)
        else :self.settingD.useInter_check.setChecked(False)
        self.settingD.maxDc_spinV.setValue(self.setting.MAX_DOC)
        self.settingD.minPla_SpinV.setValue(self.setting.MIN_PLAGIA)
        self.settingD.show()







