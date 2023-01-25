from flask import Blueprint, redirect, url_for, render_template
from werkzeug.exceptions import abort

bp = Blueprint('index', __name__, url_prefix='/')

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/<word>')
def redefine(word):
    if word == 'convert':
        return redirect(url_for('convert.convert_index'))
    elif word in ['rgb', 'rgba', 'hex', 'index']:
        return redirect(url_for('color.color_' + word))
    else:
        abort(404)
