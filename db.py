# Test connection for the intial testing of the connection
import pyodbc, os
from dotenv import load_dotenv

# Reads the key=value pairs from .env file
load_dotenv()

def get_connection():
    """
    Opens and returns a new connection to SQL Server.
    """
    # Pull connection settings from the .env file
    driver = os.environ.get("DB_DRIVER")
    server= os.environ.get("DB_SERVER")  
    db = os.environ.get("DB_NAME") 
    tru_conn = os.environ.get("TRU_CONN")
    tru_cert = os.environ.get("TRU_CERT") 
    # Full ODBC connection string 
    conn_str = (
        f"DRIVER={driver};"
        f"SERVER={server};"
        f"DATABASE={db};"
        f"{tru_conn};"
        f"{tru_cert};"
    )
    # Open the connection
    return pyodbc.connect(conn_str)