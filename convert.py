from flask import render_template, Blueprint

bp = Blueprint('convert', __name__, url_prefix='/convert')

@bp.route('/<word>')
def not_enough_args():
    return render_template('convert/not_enough_args.html')

@bp.route('/<source>/<target>')
def confirm_input():
    valid_args = ['rgb', 'rgba', 'hex']
    if source in valid_args:
        valid_args.remove(source)
        if target in valid_args:
            return redirect(url_for('convert.'+ source + 'to' + target))
