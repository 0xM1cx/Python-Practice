from flask import Flask, url_for, render_template, escape
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("instructors.db")
    conn.row_factory = sqlite3.Row
    return conn
    

@app.route('/')
def main():
    conn = get_db_connection()
    profiles = conn.execute("SELECT * FROM Instructors").fetchall()
    conn.close()
    return render_template("index.html", profiles=profiles)


'''NOTES
+ Add new entries(instructor profiles) to the databse
+ Add database values to html flask web app
+ 
'''
