import os

def get_files_in_folder(folder_path):
    # Initialize an empty list to store file names
    file_names = []
    try:
        # Iterate through all files in the folder
        for file_name in os.listdir(folder_path):
            # Check if the path is a file (not a directory)
            if os.path.isfile(os.path.join(folder_path, file_name)):
                # Append the file name to the list
                    file_names.append(file_name)
        return file_names
    except Exception as e:
        print(e)
        
def run(file_names):
    for i in file_names:
        try:
            command = f"python -m grpc_tools.protoc -I../protos --python_out=./pb --grpc_python_out=./pb ../protos/{i}"
            os.system(command)
        except Exception as e:
            return e
# Example usage:

folder_path = "../protos/"  # Update this with the path to your folder
files_in_folder = get_files_in_folder(folder_path)
run(files_in_folder)