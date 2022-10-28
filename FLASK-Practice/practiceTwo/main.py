from flask import Flask, url_for, render_template, escape
import sqlite3

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")


'''NOTES
+ Make a sqlite database to store the location of images, as well as the content for each instructor card
'''

connection = sqlite3.connect('instructors.db')
cur = connection.cursor()

cur.execute("CREATE TABLE instructors(Name, Dept, College)")

