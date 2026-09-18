"""
Column mappings for each account's CSV export. 
detect_format() matches a file's header row against these to figure out which account it came from
"""

CSV_MAPPINGS = {
    "capital_one" : {
        "headers" : ["Transaction Date", "Posted Date", "Card No.", "Description", "Category", "Debit", "Credit"],
        "date_column" : "Transaction Date",
        "merchant_column" : "Description",
        "debit_column" : "Debit",
        "credit_column" : "Credit",
    },
    "Chase" : {
        "headers" : ["Details", "Posting Date", "Description", "Amount", "Type", "Balance", "Check or Slip #"],
        "date_column" : "Posting Date",
        "merchant_column" : "Description",
        "amount_column" : "Amount",
        "invert_amount" : False,
        "exclude_merchants" : [
            "AMERICAN EXPRESS ACH PMT",
            "CAPITAL ONE      MOBILE PMT",
            "UNIVERSITY OF SO PAYROLL",
            "ZELLE PAYMENT TO MARIA",
        ],
    },
    "amex" : {
        "headers" : ["Date", "Description", "Amount"],
        "date_column" : "Date",
        "merchant_column" : "Description",
        "amount_column" : "Amount",
        "invert_amount" : True, 
    },
    "schoolsfirst" : {
        "headers" : ["Date", "Description", "Check#", "Category", "Currency", "Amount", "Balance"],
        "date_column" : "Date",
        "merchant_column" : "Description",
        "amount_column" : "Amount",
        "invert_amount" : False,
        "exclude_merchants" : [
            "CAPITAL ONE",
            "AMERICAN EXPRESS CREDIT CARD",
        ],
    },
}

def detect_format(header_row):
    for format_name, format_info in CSV_MAPPINGS.items():
        if header_row == format_info["headers"]:
            return format_name
    return None