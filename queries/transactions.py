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

def add_transaction(account_id, date, merchant, amount, category_id=None, subcategory_id=None, pay_period_week=None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO Transactions
            (AccountID, TransactionDate, Merchant, CategoryID, SubcategoryID, Amount, PayPeriodWeek, CreatedAt)
        VALUES (?, ?, ?, ?, ?, ?, ?, GETDATE())
        """,
        account_id, date, merchant, category_id, subcategory_id, amount, pay_period_week
    )
    conn.commit()
    conn.close()

def get_pay_period_week(transaction_date):
    """
    Returns the PayPeriodWeek whose 14-day period (PayDate - 13 through PayDate) contians tansaction_date.
    Returns None if no period in the table covers that date
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT PayPeriodWeek
        FROM PayPeriods
        WHERE ? BETWEEN DATEADD(day, -13, PayDate) AND PayDate 
        """,
        transaction_date
    )
    row = cursor.fetchone()
    conn.close()

    return row.PayPeriodWeek if row else None


