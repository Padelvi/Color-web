from flask import Flask, redirect, url_for, render_template
from werkzeug.exceptions import abort
import color, convert

app = Flask(__name__)
app.register_blueprint(color.bp)
app.register_blueprint(convert.bp)

@app.route('/')
def index():
    return 'Hello'

@app.route('/<word>')
def redefine(word):
    if word not in ['convert', 'color']:
        return render_template('notfound.html')
