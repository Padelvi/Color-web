from flask import render_template, Blueprint, redirect, url_for

bp = Blueprint('convert', __name__, url_prefix='/convert')

@bp.route('/')
def convert_index():
    return render_template('convert/index.html')

@bp.route('/<word>')
def not_enough_args(word):
    return render_template('convert/not_enough_args.html', word="'"+word+"'")

@bp.route('/<source>/<target>')
def confirm_input():
    valid_args = ['rgb', 'rgba', 'hex']
    if source in valid_args:
        valid_args.remove(source)
        if target in valid_args:
            return redirect(url_for('convert.' + source + 'to' + target))
