import binascii
from msilib import schema
from venv import create
from sqlalchemy import create_engine, MetaData
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from configobj import ConfigObj
import os
import base64

def decode_password(encoded_password):
    try:
        return base64.b64decode(encoded_password).decode()
    except binascii.Error as e:
        print("Error decoding password:", e)
        return None
current_directory = os.path.dirname(os.path.abspath(__file__))
config_file_path = os.path.join(current_directory, 'config.ini')
config = ConfigObj(config_file_path)
print(config)
username = config['database']['username']
databasename = config['database']['databasename']
decoded_password = decode_password(config['database']['password'])
ipaddress = config['database']['ip']
schema_name = config['database']['schema']
db_string = f"postgresql+psycopg2://{username}:{decoded_password}@{ipaddress}/{databasename}"
engine = create_engine(db_string)
metadata = MetaData(bind=engine)
engine.execute(f"Create Schema if not exists {schema_name}")
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = Session()
    try:
        yield db
        print("Connected to the database")
    except Exception as e:
        print("failed to connect to the database:",e)
    finally:
        db.close()




