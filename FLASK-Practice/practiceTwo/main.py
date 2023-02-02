from flask import Flask, url_for, render_template, escape, request
import sqlite3
from datetime import datetime
from time import sleep
import requests


app = Flask(__name__)



currentindex = 0
@app.route('/rate' )
def rate():
    conn = sqlite3.connect('instructors.db')
    cur = conn.cursor()
    id = 0
    profiles = cur.execute(f"SELECT * FROM instructors WHERE id == '{id}'").fetchone()
    data = []
    
    conn.close()
    current = 0

    name = data[current][1]
    dept = data[current][2]
    college = data[current][3]

    # name=name, dept=dept, college=college
    return render_template("Rate.html")

@app.route('/review')
def review():
    return render_template("Reviews.html")

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)

