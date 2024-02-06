from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

@app.route("/hello")
def hello_world2():
    return 'Hello World!'

@app.route("/name")
def name():
    return 'Ayush'

@app.route("/name/<myname>")
def myname(myname):
    return f'Hello, I am {myname}!'

@app.route("/age/<value>")
def hello_world4(value):
    return f'My age is {value}!'

@app.route("/info/<name>/<age>")
def info(name, age):
    return f'I am {name}. My age is {age}'
