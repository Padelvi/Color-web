from flask import Blueprint, render_template, redirect, url_for, abort

bp = Blueprint('color', __name__, url_prefix='/color')

@bp.route('/')
def color_index():
    return redirect(url_for('index.index'))

@bp.route('/<word>')
def color_redefine(word):
    for frmt in ['rgb', 'rgba', 'hex']:
        if word == frmt:
            return redirect(url_for('color.color_' + word))
    if word == 'display':
        return redirect(url_for('index.index'))
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

@bp.route('/rgb/<int:r>/<int:g>/<int:b>')
def display_rgb(r,g,b):
    return render_template('display/formats/rgb.html', r=r, g=g, b=b)

@bp.route('/rgba/<int:ra>/<int:ga>/<int:ba>/<int:a>')
def display_rgba(ra,ga,ba,a):
    return render_template('display/formats/rgba.html', ra=ra, ga=ga, ba=ba, a=a)

@bp.route('/hex/<raw_hexv>')
def display_hex(raw_hexv):
    err = None
    list_hexv = []
    for char in raw_hexv:
        list_hexv.append(char)
    for i in range(0, len(list_hexv)):
        list_hexv[i] == list_hexv[i].lower()
    hexv = ''.join(list_hexv)
    return render_template('display/formats/hex.html', hexv=hexv)
