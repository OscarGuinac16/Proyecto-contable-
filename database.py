import os
import oracledb
from dotenv import load_dotenv

load_dotenv()

def get_db():
    connection = None
    try:
        # Construir el DSN específicamente para un SID
        dsn_tns = oracledb.makedsn(
            os.environ.get("DB_HOST"), 
            os.environ.get("DB_PORT"), 
            sid=os.environ.get("DB_SID")
        )
        
        # Establecer la conexión
        connection = oracledb.connect(
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PASSWORD"),
            dsn=dsn_tns
        )
        yield connection
    finally:
        if connection:
            connection.close()