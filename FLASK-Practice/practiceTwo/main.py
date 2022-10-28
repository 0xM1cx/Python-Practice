from flask import Flask, url_for, render_template, escape
import sqlite3

app = Flask(__name__)



connection = sqlite3.connect('instructors.db')
cur = connection.cursor()
arr = []
for row in cur.execute("SELECT * FROM instructors"):
    arr.append(row)
    

@app.route('/')
def main(arr=arr):
    return render_template("index.html", arr=arr)


'''NOTES
+ Make a sqlite database to store the location of images, as well as the content for each instructor card
'''
