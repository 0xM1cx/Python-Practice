from flask import Flask, url_for, render_template, escape, request
import sqlite3
from datetime import datetime
from time import sleep
import requests


app = Flask(__name__)



currentindex = 0
@app.route('/rate')
def rate():
    id_num = 1;
    conn = sqlite3.connect('instructors.db')
    cur = conn.cursor()
    profiles = cur.execute(f"SELECT * FROM instructors WHERE id == '{id_num}'").fetchall()
    print
    conn.close()
    
    
    return render_template("Rate.html", profiles=profiles)

@app.route('/review')
def review():
    return render_template("Reviews.html")

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)

