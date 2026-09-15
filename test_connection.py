# Test connection for the intial testing of the connection
import pyodbc, os
from dotenv import load_dotenv

load_dotenv()

driver = os.environ.get("DB_DRIVER")
server= os.environ.get("DB_SERVER")  
db = os.environ.get("DB_NAME") 
tru_conn = os.environ.get("TRU_CONN")
tru_cert = os.environ.get("TRU_CERT") 

conn_str = (
    f"DRIVER={driver};"
    f"SERVER={server};"
    f"DATABASE={db};"
    f"{tru_conn};"
    f"{tru_cert};"
)

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

cursor.execute("SELECT * FROM Bank")  
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
