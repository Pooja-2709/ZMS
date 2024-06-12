from models.animal import Animal
from pb import animal_pb2, animal_pb2_grpc
from google.protobuf.json_format import MessageToDict
from service.animal_service import Animal_Service
import uuid

class Animal_Controller(animal_pb2_grpc.AnimalServiceServicer):
    
    def __init__(self, session):
        self.session = session
        self.animal_service = Animal_Service(session)
        
    def create(self, request, context):
        values = MessageToDict(request)
        animal = self.animal_service.create_animal(values=values)
        response = animal_pb2.CreateAnimalResponse(animal=animal)
        return response
    
    def update(self, request, context):
        values = MessageToDict(request)
        animal = self.animal_service.update_animal(values=values,id = request.id)
        response = animal_pb2.UpdateAnimalResponse(animal=animal)
        return response
    
    def delete(self,request,context):
        values = MessageToDict(request)
        animal = self.animal_service.delete_animal(id=request.id)
        response = animal_pb2.DeleteAnimalResponse(message=animal)
        return response
        
    
