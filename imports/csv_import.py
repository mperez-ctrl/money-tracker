import csv
from datetime import datetime
from decimal import Decimal
from imports.csv_mappings import CSV_MAPPINGS, detect_format
from imports.merchant_rules import auto_categorize
from queries.transactions import get_transactions_for_account, add_transaction

def parse_date(date_str):
    for fmt in ("%Y-%m-%d", "%m/%d/%Y"):
        try:
            return datetime.strptime(date_str, fmt).date()
        except ValueError:
            continue
    raise ValueError(f"Unrecognized date format: {date_str}")

def import_csv(file_path, account_id):
    """
    Reads an account CSV, autodetects its format, normalizes each row, skips anything already in the database for this account, and inserts the rest.
    Return (imported_count, skipped_count)
    """
    with open(file_path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        format_name = detect_format(reader.fieldnames)

        if format_name is None:
            raise ValueError(f"Unregcognize CSV format - headers were: {reader.fieldnames}")

        format_info = CSV_MAPPINGS[format_name]

        # Build a set of of all transactions already in the database to check for duplicates
        existing_keys = set()
        for row in get_transactions_for_account(account_id):
            txn_date = row.TransactionDate
            if hasattr(txn_date, "date"): # normalize datetime to date
                txn_date = txn_date.date()
            existing_keys.add((txn_date, row.Merchant, Decimal(str(row.Amount))))

        imported_count = 0
        skipped_count = 0
        excluded_count = 0

        for row in reader:
            date_str = row[format_info["date_column"]].strip()
            if not date_str: 
                continue # skip blank trailing rows

            date = parse_date(date_str)
            merchant = row[format_info["merchant_column"]].strip()

            exclude_list = format_info.get("exclude_merchants", [])
            merchant_upper = merchant.upper()
            if any(pattern.upper() in merchant_upper for pattern in exclude_list):
                excluded_count += 1
                continue

            if "debit_column" in format_info:
                debit = row[format_info["debit_column"]].strip().replace(",","")
                credit = row[format_info["credit_column"]].strip().replace(",","")
                if debit:
                    amount = -Decimal(debit)
                elif credit:
                    amount = Decimal(credit)
                else:
                    continue
            else:
                amount_str = row[format_info["amount_column"]].strip().replace(",","")
                amount = Decimal(amount_str)
                if format_info.get("invert_amount"):
                    amount = -amount

            key = (date, merchant, amount)
            if key in existing_keys:
                skipped_count +=1
                continue

            category_id, subcategory_id = auto_categorize(merchant)
            add_transaction(account_id, date, merchant, amount, category_id, subcategory_id)
            imported_count += 1
    return imported_count, skipped_count, excluded_count

