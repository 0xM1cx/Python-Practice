from flask import Flask, escape, url_for, render_template, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/cipher")
@app.route("/<name>")
def sample(name=None):
    return render_template("CaesarCipher.html", username=name)

