from sqlalchemy import Column, Integer, String, Time
import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine,MetaData
from database.database import engine
from sqlalchemy.dialects.postgresql import UUID
from pydantic import BaseModel
from sqlalchemy.orm import sessionmaker

AnimalDetailBase = declarative_base()
class AnimalDetail(AnimalDetailBase):
    __tablename__ = 'animaldetail'
    __table_args__ = {'schema': 'meta'}
    
    id = Column(UUID(as_uuid=True), default=uuid.uuid1, primary_key=True, unique=True, index=True, nullable=False)
    height = Column(String)
    weight = Column(String)
    age = Column(Integer)
    
class AnimalDetailData(BaseModel):
    height: str
    weight: str
    age: int
    