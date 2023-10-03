from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello, Flask!</h1> <h2>這是標題二</h2> "

@app.route("/hello_world")
def hello_world():
    return "<h1>Hello, World!</h1>"
