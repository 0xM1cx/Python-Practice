from flask import Flask, url_for, render_template, escape, request
import sqlite3
from datetime import datetime
from time import sleep
import requests


app = Flask(__name__)



def get_db_connection():
    conn = sqlite3.connect("instructors.db")
    conn.row_factory = sqlite3.Row
    return conn
    
currentindex = 0
@app.route('/rate')
def voting():
    id_num = 1;
    conn = get_db_connection()
    profiles = conn.execute(f"SELECT * FROM instructors WHERE id == '{id_num}'").fetchall()
    conn.close()
    
    
    return render_template("rate.html", profiles=profiles)



@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)

