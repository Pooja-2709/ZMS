# create a class -? table fields(attributes)
from sqlalchemy import Column, Integer, String, Time
import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine,MetaData
from database.database import engine
from sqlalchemy.dialects.postgresql import UUID
from pydantic import BaseModel
from sqlalchemy.orm import sessionmaker

ZooBase = declarative_base()
class Zoo(ZooBase):
    __tablename__ = 'zoo'
    __table_args__ = {'schema': 'meta'}
     
    id = Column(UUID(as_uuid=True), default=uuid.uuid1, primary_key=True, unique=True, index=True, nullable=False)
    name = Column(String, unique=True, index=True)
    location = Column(String)
    address = Column(String)
    openingTime = Column(String)
    closingTime = Column(String)
    contact = Column(String)
        
class ZooData(BaseModel):
    name: int
    location: str
    address: str
    openingTime: str
    closingTime: str
    contact: str