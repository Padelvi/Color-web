from flask import Blueprint, render_template, redirect, url_for, abort, flash

bp = Blueprint('display', __name__, url_prefix='/display')

@bp.route('/')
def display_index():
    return render_template('display/index.html')

@bp.route('/<word>')
def display_redefine(word):
    if word == 'index':
        return redirect(url_for('display.display_index'))
    elif word in ['rgb', 'rgba', 'hex']:
        return redirect(url_for('color.color_' + word))
    else:
        abort(404, 'Word not found')

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
    for char in hexv:
        result.append(char)
    if len(list_hexv) != 6:
        err = 'Length incorrect'
    for i in range(0, len(list_hexv)):
        list_hexv[i] == list_hexv[i].lower()
    hexv = ''.join(list_hexv)
    if err is not None:
        flash(err)
    return render_template('display/formats/hex.html', hexv=hexv)
