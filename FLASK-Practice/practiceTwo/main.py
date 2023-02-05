from flask import Flask, url_for, render_template, escape, request
import sqlite3
from datetime import datetime
from time import sleep
import requests


app = Flask(__name__)




@app.route('/rate' )
def rate():
    return render_template("Rate.html")

@app.route('/review')
def review():
    return render_template("Reviews.html")

@app.route("/")
def index():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug = True)

