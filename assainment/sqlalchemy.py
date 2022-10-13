# Create your models here.
from sqlalchemy import create_engine
from sqlalchemy import Integer,column,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session
engine = create_engine('sqlite:///practice.db',echo=True)
Base = declarative_base()

def employe(Base):
    id = column(Integer,primary_key=True)
    name = column(String)
    age = column(Integer)
    branch = column(String)

def company(Base):
    id = column(Integer,primary_key=True)
    name = column(String(60))
results = session.query(employe,company).join(company).all()