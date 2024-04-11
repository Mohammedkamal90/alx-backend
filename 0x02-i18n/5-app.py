#!/usr/bin/env python3
"""
basic flask application
"""

from flask import Flask, g, render_template, request
from flask_babel import Babel, _
import pytz

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user(id):
    return users.get(int(id))

@app.before_request
def before_request():
    g.user = get_user(request.args.get('login_as'))

@app.route('/')
def index():
    if g.user:
        message = _("You are logged in as %(username)s.", username=g.user['name'])
    else:
        message = _("You are not logged in.")
    return render_template('5-index.html', message=message)

if __name__ == '__main__':
    app.run()
