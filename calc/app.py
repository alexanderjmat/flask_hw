# Put your app in here.
import operations 

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home_page():
    return "Welcome to the calculator page."

@app.route('/add')
def add():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f'{operations.add(a, b)}'

@app.route('/sub')
def sub():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f'{operations.sub(a, b)}'

@app.route('/mult')
def mult():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f'{operations.mult(a, b)}'

@app.route('/div')
def div():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f'{int(operations.div(a, b))}'





