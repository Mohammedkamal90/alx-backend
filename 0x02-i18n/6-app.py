#!/usr/bin/env python3
"""
basic flask application
"""

def get_locale() -> str:
    """
    Gets locale from user settings or request header
    """
    options = [
        request.args.get('locale', '').strip(),
        g.user.get('locale', None) if g.user else None,
        request.accept_languages.best_match(app.config['LANGUAGES']),
        Config.BABEL_DEFAULT_LOCALE
    ]
    for locale in options:
        if locale and locale in Config.LANGUAGES:
            return locale
    return Config.BABEL_DEFAULT_LOCALE
