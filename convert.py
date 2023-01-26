from flask import render_template, Blueprint, redirect, url_for, request
from werkzeug.exceptions import abort
global result

bp = Blueprint('convert', __name__, url_prefix='/convert')

@bp.route('/')
def convert_index():
    try:
        return render_template('convert/index.html', result=result)
    except NameError:
        result = []
        return render_template('convert/index.html', result=result)

@bp.route('/<word>')
def not_enough_args(word):
    if word == 'index':
        return redirect(url_for(convert.convert_index))
    for frmt in ['rgb', 'rgba', 'hex']:
        if word == frmt:
            return redirect(url_for('color.color_' + word))
    return render_template('convert/not_enough_args.html', word="'"+word+"'")

@bp.route('/<source>/<target>', methods=['GET', 'POST'])
def convert(source, target):
    valid_args = ['rgb', 'rgba', 'hex']
    if source in valid_args:
        valid_args.remove(source)
        if target in valid_args:
            pass
        else:
            abort(404, "Source and/or target color formats invalid. Try 'rgb', 'rgba', or 'hex'.")
    else:
        abort(404, "Source and/or target color formats invalid. Try 'rgb', 'rgba', or 'hex'.")
    if request.method == 'POST':
        result = None
        if source == 'rgb':
            result = [request.form.get('rgb_r'), request.form.get('rgb_g'), request.form.get('rgb_b')]
        return redirect(url_for('convert.convert_index'))
    return render_template('convert/convert.html', source=source, target=target)
