# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request, Markup
from datetime import datetime
from model import dictionaryReturner
import os

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
    numbers = [0,1,2,3,4,5,6,7]
    return render_template("template.html", continent= myDict, numbers = numbers)