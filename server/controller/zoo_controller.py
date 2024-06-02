from models.zoo import Zoo
from pb import zoo_pb2, zoo_pb2_grpc
from service.zoo_service import Zoo_Service
from google.protobuf.json_format import MessageToDict
from service.zoo_service import Zoo_Service
import uuid

class Zoo_Controller(zoo_pb2_grpc.ZooServiceServicer):
    
    def __init__(self, session):
        self.session = session
        self.zoo_service = Zoo_Service(session)
        
    def create(self, request, context):
        values = MessageToDict(request)
        zoo = self.zoo_service.create_zoo(values=values)
        response = zoo_pb2.CreateZooResponse(
            zoo=zoo)
        return response
    
    def search(self,request,context):
        values = MessageToDict(request)
        zoo = self.zoo_service.searchall(request=request)
        response = zoo_pb2.ReadAllZooResponse(
            records=zoo)
        return response
    
    def update(self, request, context):
        values = MessageToDict(request)
        zoo = self.zoo_service.update_zoo(values = values, id=request.id)
        response = zoo_pb2.UpdateZooResponse(zoo=zoo)    
        return response
    
    def delete(self,request,context):
        values = MessageToDict(request)
        zoo = self.zoo_service.delete_zoo(id=request.id)
        response = zoo_pb2.DeleteZooResponse(message=zoo)  
        return response
    
    def get(self, request, context):
        values = MessageToDict(request)
        zoo = self.zoo_service.get_by_id(id=request.id)
        response = zoo_pb2.GetZooResponse(zoo=zoo)
        return response    