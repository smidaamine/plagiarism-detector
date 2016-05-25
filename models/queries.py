from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from com.smidaAmineAchache.models.ModelApp import User, Documents, Setting


__author__ = 'TOSHIBA'


class Mnipul():

    #engin = create_engine('sqlite:///PLAGIA.db')
    engin = create_engine('sqlite:///PLAGIA.db')

    engin.echo = True  # Try changing this to True and see what happens

    Base = declarative_base()
    Session = sessionmaker(bind=engin)
    #Session = scoped_session(sessionmaker(bind=engin))
    session =Session()

    def addUser(self,name,first_name,last_name,password,email,univ_name,profision):
        newUser=User(name,first_name,last_name,password,email,univ_name,profision)
        self.session.add(newUser)
        self.session.commit()

    ##add document to the data base
    def addDoc(self,path,title,addBy_id,ps, state,plagiaSim):
        newDoc=Documents(path,title,addBy_id,ps, state,plagiaSim)
        self.session.add(newDoc)
        self.session.commit()


    ##select user from data base
    def selectUser_LogIN(self,usrName,passWord):
        #res = self.session.query(User).filter(User.user_name==usrName).first()
        res = self.session.query(User).filter(User.user_name==usrName).first()
        try:
            if res.password==passWord:
               # print "logIn"
                return res,True
            else:
                #print "PassWord Or user Name not ex"
                return  res,False
        except(AttributeError):
            return  res,False
    def selectAllDocs(self):
        """
        return list of all docs in data base
        """
        res=self.session.query(Documents).all()
        return res
    def getSetting(self):
        res=self.session.query(Setting).first()
        #print res
        return res
    def saveSetting(self,useInt,maxD,minPla):

        res=self.session.query(Setting).first()
        res.USE_INT=useInt
        res.MAX_DOC=maxD
        res.MIN_PLAGIA=minPla
        self.session.commit()

if __name__=="__main__":
    Mnipul()