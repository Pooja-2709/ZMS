import os

def get_files_in_folder(folder_path):
    '''function to get all .proto files in a given folder'''
    file_names = []
    try:
        # list all the files in the given direct
        for file_name in os.listdir(folder_path):
            # check if the file is regular file and ends with .proto
            if os.path.isfile(os.path.join(folder_path, file_name)) and file_name.endswith('.proto'):
                file_names.append(file_name) #add the file name to the list
        return file_names
    except Exception as e:
        print(e)
        return []

def run(file_names, proto_path, pb_path):
    '''function to run the protoc command to generate python files from .proto files'''
    for proto_file in file_names:
        try:
            command = f"python -m grpc_tools.protoc -I{proto_path} --python_out={pb_path} --grpc_python_out={pb_path} {os.path.join(proto_path, proto_file)}"
            os.system(command)
        except Exception as e:
            print(e)

def modify_imports(pb_path):
    '''function to modify import statements in the generated python files'''
    for root, _, files in os.walk(pb_path):
        for file in files:
            
            if file.endswith('_pb2.py') or file.endswith('_pb2_grpc.py'):
                file_path = os.path.join(root,file) #create the full path of each file ex:- ./pb/example_pb2.py
                try:
                    with open(file_path, 'r') as f: #open the file in the read mode
                        lines = f.readlines() #read all lines into a list
                                                
                    with open(file_path, 'w') as f: #open the file in write mode
                        for line in lines:
                            if line.startswith('import'):
                                line = 'from pb ' + line
                            f.write(line) #write the modified line back to the file
                            
                except exception as e:
                    print(e)
if __name__ == "__main__":
    proto_path = "../protos/"  # Update this with the path to your .proto files
    pb_path = "./pb"  # Update this with the path to your pb directory

    proto_files = get_files_in_folder(proto_path)
    run(proto_files, proto_path, pb_path)
    modify_imports(pb_path)