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

    conn = get_db_connection()
    profiles = conn.execute("SELECT * FROM instructors").fetchall()
    conn.close()
    
    global currentindex
    currentindex = currentindex + 1
    # next_item = request.form.get('next_item')
    # next_item_index = int(request.form.get('next_item_index', 0))
    # data = conn.query(column='Nauka').offset(next_item_index).limit(1).all()[0]
    # data = conn.execute("SELCT * FROM instructors WHERE College LIKE '%COE%'")
    return render_template("rate.html", profiles=profiles, currentindex=currentindex)



@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)

