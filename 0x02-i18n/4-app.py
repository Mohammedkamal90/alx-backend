#!/usr/bin/env python3
"""
basic Flask application with internationalization support.
"""

from flask import Flask, request, render_template
from flask_babel import Babel


class Config:
    """
    Application configuration class.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_locale() -> str:
    """
    Get locale from request object. If the locale parameter is present
    in the URL and is a supported locale, return it; otherwise, return
    the best-matching language from the Accept-Language header.
    """
    locale = request.args.get('locale', '').strip()
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """
    Render a basic HTML template.
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()