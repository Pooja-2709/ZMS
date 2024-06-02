from sqlalchemy.sql.expression import insert, update, delete, select 
from models.zoo import Zoo

# from .paginator import Paginator

class Zoo_Service:
    def __init__(self, session):
            self.session = session    
    def create_zoo(self,values):
        try:
            with self.session() as session, session.begin():
            # Instantiate the Zoo model with correct attributes
                new_zoo = Zoo(
                    name=values['Name'],
                    location=values['Location'],
                    address=values['Address'],
                    openingTime=values['Opening'],
                    closingTime=values['Closing'],
                    contact=values['Contact']
                )
                
                session.add(new_zoo)
                session.commit()
            uuid_str = str(new_zoo.id)            
      
            zoo_dict = {
                'id': uuid_str,
                'Name': new_zoo.name,
                'Location': new_zoo.location,
                'Address': new_zoo.address,
                'Opening': new_zoo.openingTime,
                'Closing': new_zoo.closingTime,
                'Contact': new_zoo.contact
            }
                        
            return zoo_dict
        except Exception as e:
            print(e)

    def get_by_id(self, id):
        try:
            identity = str(id)
            with self.session() as session:
                record = session.query(Zoo).filter(Zoo.id == identity).first()
                if record:
                    zoo_dict = {
                        'id' : str(record.id),
                        'Name' : record.name,
                        'Location' : record.location,
                        'Address' : record.address,
                        'Opening' : record.openingTime,
                        'Closing' : record.closingTime,
                        'Contact' : record.contact                      
                    }
                    return zoo_dict
        except Exception as e:
            print(e)

    
    def searchall(self,request):
        records = []
        with self.session() as session:
            results = session.query(Zoo).all()
            for record in results:
                zoo_dict = {
                        'id': str(record.id),
                        'Name': record.name,
                        'Location': record.location,
                        'Address': record.address,
                        'Opening': record.openingTime,
                        'Closing': record.closingTime,
                        'Contact': record.contact
                    }
                records.append(zoo_dict)
        return records
    
    def update_zoo(self,values,id):
        try:
            identity = str(id)
            with self.session() as session, session.begin():
                statement = update(Zoo).where(Zoo.id == identity).values(
                    id = identity,
                    name = values['Name'],
                    location =  values['Location'],
                    address  = values['Address'],
                    openingTime =  values['Opening'],
                    closingTime = values['Closing'],
                    contact = values['Contact']
                )
                session.execute(statement)
              
                zoo_dict = {
                    'id': identity,
                    'Name': values['Name'],
                    'Location': values['Location'],
                    'Address': values['Address'],
                    'Opening': values['Opening'],
                    'Closing': values['Closing'],
                    'Contact': values['Contact']
                }
                print("Record is updated")
                return zoo_dict
            
        except Exception as e:
            print(e)
    
    def delete_zoo(self,id):
        identity = str(id)
        with self.session() as session:
            statement = delete(Zoo).where(Zoo.id == identity)
            session.execute(statement)
        return "Record is deleted" 
    
    
      
