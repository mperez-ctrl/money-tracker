from flask import Blueprint, render_template, request, redirect, url_for
from queries.accounts import get_accounts, add_account

# Blueprint is a mini version of the flask app
accounts_bp = Blueprint("accounts", __name__)

@accounts_bp.route("/accounts", methods=["GET", "POST"])
def list_accounts():
    if request.method == "POST":
        name = request.form["BankName"]
        add_account(name)
        return redirect(url_for("accounts.list_accounts"))
    
    # Call the query function to get rows
    accounts = get_accounts()
    # Give rows to template
    return render_template("accounts.html", accounts=accounts)
