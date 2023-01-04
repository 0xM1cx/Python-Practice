from flask import Flask, url_for, render_template, escape
import sqlite3
from datetime import datetime
from time import sleep


app = Flask(__name__)



def get_db_connection():
    conn = sqlite3.connect("instructors.db")
    conn.row_factory = sqlite3.Row
    return conn
    

@app.route('/rate')
def voting():

    conn = get_db_connection()
    profiles = conn.execute("SELECT * FROM instructors").fetchall()
    conn.close()
    
    return render_template("rate.html", profiles=profiles)



@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)

