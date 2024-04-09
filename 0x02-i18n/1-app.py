#!/usr/bin/env python3
"""
module define Flask app with Babel extension for internationalization.
"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    configuration class for Flask app
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def index():
    """
    route for the main page

    returns:
        str: Rendered HTML content.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
