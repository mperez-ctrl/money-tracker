from flask import Flask

# create instance of flask
app = Flask(__name__)

@app.route("/")
def func():
    return 'Hi!'

# start server
if __name__ == "__main__":
    app.run(debug=True)