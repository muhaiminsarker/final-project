# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template
from model import dictionaryReturner

# -- Initialization section --
app = Flask(__name__)
# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/australia')

def australia():
    myDict = dictionaryReturner()
    return render_template("template.html", continent= myDict, numbers = numbers)