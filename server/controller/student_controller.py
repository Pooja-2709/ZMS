from models.student import Student
from service.Student_service import Student_Service
from pb import student_pb2, student_pb2_grpc
from google.protobuf.json_format import MessageToDict


class Student_Controller(student_pb2_grpc.StudentServicer):

    def __init__(self, session):
        self.student_service = Student_Service(session)

    def create(self, request, context):
        print("api is here")
        values = MessageToDict(request)
        student = self.student_service.create(table=Student, values=values)
        return student_pb2.CreateReply(id=student["id"], name=student["name"], lastname=student["lastname"])

    def read(self, request, context):
        student = self.student_service.read(
            table=Student, conditions=Student.id == request.id)
        return student_pb2.ReadReply(id=student["id"], name=student["name"], lastname=student["lastname"])

    def readall(self, request, context):
        results = self.student_service.readall(table=Student, limit=request.limit, offset=request.offset)
        students = []
        for r in results:
            students.append(student_pb2.ReadReply(
                id=r.id,
                name=r.name,
                lastname=r.lastname                
            ))
        
        return student_pb2.ReadAllReply(replies=students)

    def update(self, request, context):
        values = MessageToDict(request)
        message = self.student_service.update(
            table=Student, conditions=Student.id == request.id, values=values)
        return student_pb2.UpdateReply(message=message)

    def delete(self, request, context):
        message = self.student_service.delete(
            table=Student, conditions=Student.id == request.id)
        return student_pb2.DeleteReply(message=message)
