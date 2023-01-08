from flask import Blueprint, request, render_template

bp = Blueprint('color', __name__, url_prefix='/color')

@bp.route('/rgb')
def rgb_color():
    return render_template('color/rgb.html')

@bp.route('/rgba')
def rgba_color():
    return render_template('color/rgba.html')

@bp.route('/hex')
def hex_color():
    return render_template('color/hex.html')
