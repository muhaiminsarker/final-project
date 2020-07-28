# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template
from model import australiaReturner, antarcticaReturner, africaReturner, SAReturner

# -- Initialization section --
app = Flask(__name__)
# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/australia')

def australia():
    myDict = australiaReturner()
    return render_template("template.html", continent= myDict)

@app.route('/antarctica')

def antarctica():
    myDict = antarcticaReturner()
    return render_template("template.html", continent= myDict)

@app.route('/africa')

def africa():
    myDict = africaReturner()
    return render_template("template.html", continent= myDict)

@app.route('/southAmerica')

def SA():
    myDict = SAReturner()
    return render_template("template.html", continent= myDict)