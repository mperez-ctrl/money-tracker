# SELECT * FROM Bank
# Uses get_connection() from db.py
from db import get_connection

def get_banks():
    """
    Returns every row from the Bank table as a list of rows.
    """
    # Get a live connection using get_connection from db.py
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Bank")
    rows = cursor.fetchall()

    # Close the connection
    conn.close()

    return rows