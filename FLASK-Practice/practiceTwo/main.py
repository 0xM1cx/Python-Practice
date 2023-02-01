from flask import Flask, url_for, render_template, escape, request
import sqlite3
from datetime import datetime
from time import sleep
import requests


app = Flask(__name__)



currentindex = 0
@app.route('/rate')
def rate():
    conn = sqlite3.connect('instructors.db')
    cur = conn.cursor()
    profiles = cur.execute(f"SELECT * FROM instructors WHERE id == '{id_num}'").fetchall()
    data = []
    for x in profiles:
        data.append(x)
    conn.close()
    current = 0

    name = data[current][1]
    dept = data[current][2]
    college = data[current][3]

    
    return render_template("Rate.html", name=name, dept=dept, college=college)

@app.route('/review')
def review():
    return render_template("Reviews.html")

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)

