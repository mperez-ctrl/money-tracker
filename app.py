from flask import Flask
from routes.accounts import accounts_bp

# Create the Flask app instance
app = Flask(__name__)

# Attach the accounts blueprint's routes to this app
app.register_blueprint(accounts_bp)

if __name__ == "__main__":
    app.run(debug=True)