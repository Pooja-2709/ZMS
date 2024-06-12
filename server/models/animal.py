from sqlalchemy import Column, Integer, String, Time
import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine,MetaData, ForeignKey
from database.database import engine
from sqlalchemy.dialects.postgresql import UUID
from pydantic import BaseModel
from sqlalchemy.orm import sessionmaker
from models.zoo import Zoo
from models.animalkind import Animalkind


AnimalBase = declarative_base()
class Animal(AnimalBase):
    __tablename__ = 'animal'
    __table_args__ = {'schema': 'meta'}
    
    id =Column(UUID(as_uuid=True), default=uuid.uuid1, primary_key=True, unique=True, index=True, nullable=False)
    name = Column(String)
    gender = Column(String)
    cageid = Column(Integer)
    zooid = Column(UUID(as_uuid=True), ForeignKey(Zoo.id), nullable=False) 
    animalkindid = Column(String, ForeignKey(Animalkind.id), nullable=False)
    feedtime = Column(String)
    
class AnimalData(BaseModel):   
    name: str 
    gender: str
    cageid: int
    feedtime: str
    