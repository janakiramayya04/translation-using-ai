from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,Text,JSON
Base=declarative_base()

class TranslationTask(Base):
    __tablename__="translation_tasks"
    id=Column(Integer,primary_key=True,index=True)
    text=Column(Text,nullable=False)
    languages=Column(JSON,nullable=False)
    status=Column(String(50),default="on progress")
    translations=Column(JSON,default={})

    
    