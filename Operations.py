from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Model import *



def insert(fname,lname):
    engine = create_engine('sqlite:///usercrud.db')

    Base.metadata.bind = engine

    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    new_person = Users(name=fname,surname=lname)
    session.add(new_person)
    session.commit()


def getById(id):
    engine = create_engine('sqlite:///usercrud.db')

    Base.metadata.bind = engine

    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    user= session.query(Users).get(id)
    return {'id':user.id,'name':user.name,'surname':user.surname}


def listAll():
    engine = create_engine('sqlite:///usercrud.db')

    Base.metadata.bind = engine

    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    userlist= session.query(Users).all()
    nuserlist=[]
    for user in userlist:
        nuserlist.append({'id':user.id,'name':user.name,'surname':user.surname})

    return nuserlist;



