from flask import Blueprint, render_template, redirect, url_for
from werkzeug.exceptions import abort

bp = Blueprint('color', __name__, url_prefix='/color')

@bp.route('/')
def color_index():
    return redirect(url_for('index.index'))

@bp.route('/<word>')
def color_redefine(word):
    for frmt in ['rgb', 'rgba', 'hex']:
        if word == frmt:
            return redirect(url_for('color.color_' + word))
    abort(404, "Color format invalid. Try 'rgb', 'rgba', or 'hex'.")

@bp.route('/rgb')
def color_rgb():
    return render_template('color/rgb.html')

@bp.route('/rgba')
def color_rgba():
    return render_template('color/rgba.html')

@bp.route('/hex')
def color_hex():
    return render_template('color/hex.html')
