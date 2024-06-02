from sqlalchemy import inspect
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
StudentBase = declarative_base()

class Student(StudentBase):
    """_summary_

    Args:
        Base (_type_): _description_
    """
    __tablename__ = 'students'
    __table_args__ = {'schema': 'meta'}
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(50))
    lastname = Column(String(50))
    

           