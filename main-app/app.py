from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Home Page</h1>"

@app.route("/user/<string:name>")
def user(name):
    return f"<h1> hello user {name}</h1>"

