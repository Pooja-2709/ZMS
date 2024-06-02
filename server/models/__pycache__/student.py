from sqlalchemy import inspect
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy import Column, String, Integer

# Instead of using declarative_base as above, we can create it from our own class:
@as_declarative()
class Base:
    """

     _summary_ The base class which our objects will be defined on.
    """
    __abstract__ = True

    def _asdict(self):
        """
        _asdict _summary_

        _extended_summary_

        Returns:
            _type_: _description_
        """

        return {
            c.key: getattr(self, c.key)
            for c in inspect(self).mapper.column_attrs
        }

    def __tablename__(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.__name__


class Student(Base):
    """_summary_

    Args:
        Base (_type_): _description_
    """
    __tablename__ = 'students'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(50))
    lastname = Column(String(50))
    

           