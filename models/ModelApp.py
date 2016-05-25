__author__ = 'TOSHIBA'


from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


engin = create_engine('sqlite:///PLAGIA.db')

engin.echo = True  # Try changing this to True and see what happens

Base = declarative_base()

class User(Base):
    __tablename__ ="USER"
    user_name=Column(String(40),primary_key=True)
    first_name=Column(String(40))
    last_name=Column(String(40))
    password=Column(String(40))
    email=Column(String(40),unique=True)
    univ_name=Column(String(100))
    profision=Column(String(100))
    roll=Column(String(20))

    def __init__(self,userName,first_name,last_name,password,email,univ_name,profision,roll="USER"):
        """"""
        self.user_name=userName
        self.first_name=first_name
        self.last_name=last_name
        self.password=password
        self.email=email
        self.univ_name=univ_name
        self.profision=profision
        self.roll=roll


class Documents(Base):
    __tablename__="PAPERS"
    path=Column(String(400), primary_key=True)
    title = Column(String)
    state = Column(String)
    ps=Column(String(500))

    addBy_id = Column(Integer, ForeignKey("USER.user_name"))

    plagiaSim=Column(Integer)

    #----------------------------------------------------------------------
    def __init__(self, path,title,addBy_id,ps, state="null",plagiaSim=0):
        """"""
        self.path=path
        self.title = title

        self.ps=ps
        self.state = state
        self.addBy_id=addBy_id
        self.plagiaSim=plagiaSim



class Setting(Base):
    __tablename__="SETTING"
    id=Column(Integer,primary_key=True)
    USE_INT=Column(Integer)
    MAX_DOC=Column(Integer)
    MIN_PLAGIA=Column(Integer)
    def __init__(self,useInt,maxDoc,minPla,id=1):
        self.id=id
        self.USE_INT=useInt
        self.MAX_DOC=maxDoc
        self.MIN_PLAGIA=minPla


# create tables
Base.metadata.create_all(engin)

##add=Mnipul()
##add.selectUser_LogIN("amine","12345")
#
#add.addUser(1,"amine","smida","amine","12345","smida@gmail.com","usthb","prof")