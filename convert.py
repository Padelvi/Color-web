from flask import render_template, Blueprint, redirect, url_for, request, abort
from click import echo

bp = Blueprint('convert', __name__, url_prefix='/convert')

@bp.route('/')
def convert_index():
    source = request.args.get('source')
    target = request.args.get('target')
    echo(source)
    echo(target)
    if source == target:
        abort(404, 'Source and target color formats equal')
    if source == 'rgb':
        rgb_r = request.args.get('rgb_r')
        rgb_g = request.args.get('rgb_g')
        rgb_b = request.args.get('rgb_b')
        rgb = [rgb_r, rgb_g, rgb_b]
        for num in rgb:
            try:
                num = int(num)
            except ValueError:
                abort(404, 'Invalid values. All numbers should be integers between 0 and 255.')
            if num > 255 or num < 0:
                abort(404, 'Invalid values. All numbers should be integers between 0 and 255.')
        echo(rgb)
        return render_template('convert/index.html', source=source, rgb=rgb)
    if source =='rgba':
        rgba_ra = request.args.get('rgba_ra')
        rgba_ga = request.args.get('rgba_ga')
        rgba_ba = request.args.get('rgba_ba')
        rgba_a = request.args.get('rgba_a')
        rgba = [rgba_ra, rgba_ga, rgba_ba]
        for num in rgba:
            try:
                num = int(num)
            except ValueError:
                abort(404, 'Invalid values. All numbers should be integers between 0 and 255.')
            if num > 255 or num < 0:
                abort(404, 'Invalid values. All numbers should be integers between 0 and 255.')
        echo(rgba)
        try:
            rgba_a = int(rgba_a)
        except ValueError:
            abort(404, 'Invalid value. a value should be an integer between 0 and 100')
        if rgba_a > 100 or rgba_a < 0:
            abort(404, 'Invalid value. a value should be an integer between 0 and 100')
        rgba.append(rgba_a)
        echo(rgba)
        return render_template('convert/index.html', source=source, rgba=rgba)
    if source == 'hex':
        hexv = request.args.get('hexv')
        list_hexv = []
        for char in hexv:
            low = char.lower()
            if low not in ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f']:
                abort(404, 'Some character incorrect')
            list_hexv.append(low)
        if len(list_hexv) != 6:
            if len(list_hexv) == 3:
                list_hexv.clear()
                for char in hexv:
                    list_hexv.append(char.lower())
                    list_hexv.append(char.lower())
            else:
                abort(404, 'Length incorrect')
        hexv = ''.join(list_hexv)
        echo(hexv)
        return render_template('convert/index.html', source=source, hexv=hexv)

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
        if source == 'rgb':
            rgb_r = request.form.get('rgb_r')
            rgb_g = request.form.get('rgb_g')
            rgb_b = request.form.get('rgb_b')
            return redirect(url_for('convert.convert_index', source=source, rgb_r=rgb_r, rgb_g=rgb_g, rgb_b=rgb_b, target=target))
        if source == 'rgba':
            rgba_ra = request.form.get('rgba_ra')
            rgba_ga = request.form.get('rgba_ga')
            rgba_ba = request.form.get('rgba_ba')
            rgba_a = request.form.get('rgba_a')
            return redirect(url_for('convert.convert_index', source=source, rgba_ra=rgba_ra, rgba_ga=rgba_ga, rgba_ba=rgba_ba, rgba_a=rgba_a, target=target))
        if source == 'hex':
            hexv = request.form.get('hexv')
            return redirect(url_for('convert.convert_index', source=source, hexv=hexv, target=target))
    return render_template('convert/convert.html', source=source, target=target)
