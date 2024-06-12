from sqlalchemy import Column, Integer, String, Time
import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine,MetaData
from database.database import engine
from sqlalchemy.dialects.postgresql import UUID
from pydantic import BaseModel
from sqlalchemy.orm import sessionmaker

CustomerBase = declarative_base()
class Customer(CustomerBase):
    __tablename__ = 'customer'
    __table_args__ = {'schema': 'meta'}
    
    id = Column(UUID(as_uuid=True), default=uuid.uuid1, primary_key=True, unique=True, index=True, nullable=False)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String)
    address = Column(String)
    creditcard = Column(String)
    
class CustomerData(BaseModel):
    firstname: str
    lastname: str
    email: str
    address: str
    creditcard: str
    