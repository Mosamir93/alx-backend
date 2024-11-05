#!/usr/bin/env python3
"""A basic Flask app setup."""
from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """Config class that has a LANGUAGES class attribute."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
Babel = Babel(app)


@app.route('/')
def index():
    """A / route index."""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
