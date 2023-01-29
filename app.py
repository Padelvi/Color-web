import os
from flask import Flask
import color, convert, index, display

app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY=os.environ.get('SECRET_KEY'),
)

app.register_blueprint(index.bp)
app.register_blueprint(color.bp)
app.register_blueprint(convert.bp)
app.register_blueprint(display.bp)

if __name__=='__main__':
    app.run(host='0.0.0.0')
