from db import get_connection

def get_transactions_for_account(account_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT TransactionDate, Merchant, Amount FROM Transactions WHERE AccountID = ?",
        account_id
    )
    rows = cursor.fetchall()
    conn.close()
    return rows

def add_transaction(account_id, date, merchant, amount, category_id=None, subcategory_id=None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO Transactions
            (AccountID, TransactionDate, Merchant, CategoryID, SubcategoryID, Amount, CreatedAt)
        VALUES (?, ?, ?, ?, ?, ?, GETDATE())
        """,
        account_id, date, merchant, category_id, subcategory_id, amount
    )
    conn.commit()
    conn.close()


