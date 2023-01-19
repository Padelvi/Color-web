from flask import Flask, redirect, url_for, render_template
from werkzeug.exceptions import abort
import color, convert

app = Flask(__name__)
app.register_blueprint(color.bp)
app.register_blueprint(convert.bp)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<word>')
def redefine(word):
    if word == 'color':
        return redirect(url_for('color.color_index'))
    elif word == 'convert':
        return redirect(url_for('convert.convert_index'))
    else:
        abort(404)
