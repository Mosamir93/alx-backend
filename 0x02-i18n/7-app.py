#!/usr/bin/env python3
"""Get_locale mmodule."""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Optional, Dict
from pytz import timezone, UnknownTimeZoneError


class Config(object):
    """
    Configuration for Babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Optional[Dict]:
    """Returns a user dictionary or None if the ID
    cannot be found or if login_as was not passed."""
    id = request.args.get("login_as", type=int)
    return users.get(id, None)


@app.before_request
def before_request() -> None:
    """Uses get_user to find a user if any, and
    set it as a global on flask.g.user"""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """Determines the best match with our supported languages."""
    locale = request.args.get('locale')
    if not locale and g.user:
        locale = g.user.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.args.get(
        'lang'
        ) or request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """Determine the best time zone for the user."""
    tz = request.args.get('timezone')
    if not tz and g.user:
        tz = g.user.get('timezone')
    try:
        return timezone(tz)
    except UnknownTimeZoneError:
        return timezone(app.config['BABEL_DEFAULT_TIMEZONE'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Handles / route
    """
    return render_template('7-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
