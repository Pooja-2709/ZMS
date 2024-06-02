
# from database import sqlite
from sqlalchemy.sql.expression import insert, update, delete, select
# from .paginator import Paginator


class Student_Service():

    def __init__(self, session) -> None:
        self.session = session

    def create(self, table, values):
        with self.session() as session:
            statement = insert(table).values(values)
            result = session.execute(statement)
        inserted_row = result.inserted_primary_key._mapping
        values.update(inserted_row)
        return values

    def read(self, table, conditions):
        with self.session() as session:
            statement = select(table).where(conditions)
            result = session.scalars(statement).first()
        return result.__dict__
    
    def readall(self, table, limit, offset):
        with self.session() as session:
            results = session.query(table).offset(offset).limit(limit).all()
        return results

    def update(self, table, conditions, values):
        with self.session() as session:
            statement = update(table).where(conditions).values(values)
            session.execute(statement)
        return "Updated"

    def delete(self, table, conditions):
        with self.session() as session:
            stmt = (delete(table).where(conditions))
            session.execute(stmt)
        return "Deleted"
