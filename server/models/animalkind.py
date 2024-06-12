# create a class -? table fields(attributes)
from sqlalchemy import Column, Integer, String, Time
import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine,MetaData, ForeignKey
from database.database import engine
from sqlalchemy.dialects.postgresql import UUID
from pydantic import BaseModel
from sqlalchemy.orm import sessionmaker

AnimalkindBase = declarative_base()
class Animalkind(AnimalkindBase):
    __tablename__ = 'animalkind'
    __table_args__ = {'schema': 'meta'}
    
    id = Column(String, primary_key=True, unique=True,nullable=False)
    name = Column(String, unique=True, index=True)
    region = Column(String)
    physicalcharacteristics = Column(String)
    diet = Column(String)
    population = Column(Integer)
        
class AnimalkindData(BaseModel):
    region: str
    kindname: str
    physicalcharacteristics: str
    diet: str
    population: str