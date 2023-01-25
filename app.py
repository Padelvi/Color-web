from flask import Flask, redirect, url_for, render_template
from werkzeug.exceptions import abort
import color, convert, index

app = Flask(__name__)
app.register_blueprint(index.bp)
app.register_blueprint(color.bp)
app.register_blueprint(convert.bp)

if __name__=='__main__':
    app.run(host='0.0.0.0')
