# Uses get_connection() from db.py
from db import get_connection

def get_accounts():
    """
    Returns every row from the Accounts table as a list of rows.
    """
    # Get a live connection using get_connection from db.py
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Accounts")
    rows = cursor.fetchall()

    # Close the connection
    conn.close()

    return rows

def add_account(AccountName):
    """
    Inserts a new row into the Accounts table
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Accounts (AccountName) VALUES (?)",
        AccountName
    )
    conn.commit()
    conn.close()