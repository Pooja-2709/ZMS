from sqlalchemy.sql.expression import insert, update, delete, select
from models.animal import Animal
import uuid
class Animal_Service: 
    def __init__(self,session):
        self.session = session  
             
    def create_animal(self, values,session):
        try:
            zooid_ = uuid.UUID(values['zooid'])
            print(zooid_)
            with self.session() as session, session.begin():
                new_animal = Animal(
                    name = values['name'],
                    gender = values['gender'],
                    cageid = values['cageid'],
                    zooid =zooid_,
                    animalkindid = values['animalkindid'],
                    feedtime = values['feedtime']                                      
                )
                print('100')
                print(new_animal)
                session.add(new_animal)
                session.commit()
                
            animal_dict = {
                'id': str(new_animal.id),
                'name': new_animal.name,
                'gender': new_animal.gender,
                'cageid': new_animal.cageid,
                'zooid': str(new_animal.zooid),
                'animalkindid': new_animal.animalkindid,
                'feedtime': new_animal.feedtime                
            }
            print("record is created")
            return animal_dict
        except Exception as e:
            print(e)
            
    def update_animal(self,values,id):
        try:
            identity = str(id)
            with self.session() as session, session.begin():
                statement = update(Animal).where(Animal.id==identity).values(
                    id = identity,
                    name = values['name'],
                    gender = values['gender'],
                    cageid = values['cageid'],
                    zooid = str(values['zooid']),
                    animalkindid = values['animalkindid'],
                    feedtime = values['feedtime']
                )
                session.execute(statement)
                print("1")
                animal_dict = {
                    'id': identity,
                    'name': values['name'],
                    'gender': values['gender'],
                    'cageid': values['cageid'],
                    'zooid': values['zooid'],
                    'animalkindid': values['animalkindid'],
                    'feedtime': values['feedtime']
                }
                print('record is updated')
                return animal_dict
        except Exception as e:
            print(e)
            
    def delete_animal(self, id):
        identity = str(id)
        with self.session() as session:
            statement = delete(Animal).where(Animal.id == identity)
            session.execute(statement)
        return "record is deleted"
    