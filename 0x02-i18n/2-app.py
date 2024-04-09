#!/usr/bin/env python3
"""
module define Flask app with Babel extension for internationalization
"""

from flask import Flask, render_template, request
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


@babel.localeselector
def get_locale():
    """
    determine the best-matching language for the user from the request

    Returns:
        str: The best-matching language code
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    route for the main page

    Returns:
        str: Rendered HTML content.
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
