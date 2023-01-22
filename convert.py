from flask import render_template, Blueprint, redirect, url_for
from werkzeug.exceptions import abort

bp = Blueprint('convert', __name__, url_prefix='/convert')

@bp.route('/')
def convert_index():
    return render_template('convert/index.html')

@bp.route('/<word>')
def not_enough_args(word):
    for frmt in ['rgb', 'rgba', 'hex']:
        if word == frmt:
            return redirect(url_for('color.color_' + word))
    return render_template('convert/not_enough_args.html', word="'"+word+"'")

@bp.route('/<source>/<target>')
def confirm_input(source, target):
    valid_args = ['rgb', 'rgba', 'hex']
    if source in valid_args:
        valid_args.remove(source)
        if target in valid_args:
            return source + ' to ' + target
        else:
            abort(404, "Target color format invalid. Try 'rgb', 'rgba', or 'hex'.")
    else:
        if target in valid_args:
            abort(404, "Source color format invalid. Try 'rgb', 'rgba', or 'hex'.")
        else:
            abort(404, "Both color formats invalid. Try 'rgb', 'rgba', or 'hex'.")
