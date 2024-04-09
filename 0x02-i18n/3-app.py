#!/usr/bin/env python3
"""
module defines a Flask app with Babel extension for internationalization
"""

from typing import Optional
from flask import Flask, render_template, request
from flask_babel import Babel, _, lazy_gettext as _l

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


def get_locale() -> Optional[str]:
    """
    determine best-matching languge for the user from request

    Returns:
        str or None: best-matching language code, or None if no language match
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.localeselector
def select_locale() -> Optional[str]:
    """
    Select locale for request based on the user's preferences

    Returns:
        str or None: selected locale, or None if no locale is selected
    """
    return get_locale()


@app.route('/')
def index() -> str:
    """
    Route for the main page.

    Returns:
        str: Rendered HTML content.
    """
    return render_template('3-index.html', title=_('home_title'), header=_('home_header'))


if __name__ == '__main__':
    app.run(debug=True)
