from database.database import engine
from models.zoo import ZooBase
from models.student import StudentBase
from models.animalkind import AnimalkindBase

from models.student import StudentBase
from concurrent import futures
import grpc
from sqlalchemy.orm import sessionmaker, scoped_session
from pb import zoo_pb2_grpc
from pb import student_pb2_grpc
from controller.zoo_controller import Zoo_Controller
from controller.student_controller import Student_Controller

def serve():
    try:
        port = '50051'
        grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        session = create_session()
        print("2")
        student_pb2_grpc.add_StudentServicer_to_server(
        Student_Controller(session), grpc_server)
        
        zoo_pb2_grpc.add_ZooServiceServicer_to_server(
            Zoo_Controller(session), grpc_server)
        
        grpc_server.add_insecure_port('[::]:' + port)
        grpc_server.start()
        print("Server started, listening on " + port)
        grpc_server.wait_for_termination()
    except Exception as e:
        print(e)
    
def create_session():
    try:
        session_factory = sessionmaker(bind=engine,
                                   autoflush=True,
                                   autocommit=True,
                                   expire_on_commit=False)
        session_maker = scoped_session(session_factory)
        StudentBase.metadata.create_all(bind=engine)
        ZooBase.metadata.create_all(bind=engine)
        AnimalkindBase.metadata.create_all(bind=engine)
        print("1")
        return session_maker
    except Exception as e:
        raise e


if __name__ == '__main__':
    serve()
    