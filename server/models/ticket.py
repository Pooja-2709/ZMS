from sqlalchemy import Column, Integer, String, Time
import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine,MetaData
from database.database import engine
from sqlalchemy.dialects.postgresql import UUID
from pydantic import BaseModel
from sqlalchemy.orm import sessionmaker

TicketBase = declarative_base()
class Ticket(TicketBase):
    __tablename__ = 'ticket'
    __table_args__ = {'schema': 'meta'}
    
    id = Column(UUID(as_uuid=True), default=uuid.uuid1, primary_key=True, unique=True, index=True, nullable=False)
    date = Column(String)
    price = Column(Integer)
    
class TicketData(BaseModel):
    date: str
    price: int