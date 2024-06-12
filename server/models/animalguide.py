from sqlalchemy import Column, Integer, String, Time
import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine,MetaData
from database.database import engine
from sqlalchemy.dialects.postgresql import UUID
from pydantic import BaseModel
from sqlalchemy.orm import sessionmaker

AnimalguideBase = declarative_base()
class Animalguide(AnimalguideBase):
    __tablename__ = 'animalguide'
    __table_args__ = {'schema': 'meta'}
    
    id = Column(UUID(as_uuid=True), default=uuid.uuid1, primary_key=True, unique=True, index=True, nullable=False)
    zoointro = Column(String)
    updatedyear = Column(Integer)
    

class AnimalguideData(BaseModel):
    zoointro: str
    updatedyear: int
    
    