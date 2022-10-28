from flask import Flask, escape, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome!!! User"

@app.route('/about')
def about():
    return "<h1>About Me</h1>"

@app.route('/user/<name>')
def user(name):
    return f"Welcome {escape(name)}"

with app.test_request_context():
    print(url_for('user', name="Shawn"))
    print(url_for('about'))
    print(url_for('index'))