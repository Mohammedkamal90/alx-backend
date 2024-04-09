#!/usr/bin/env python3
"""
module define basic Flask app with single route
"""

from flask import Flask, render_template

app = Flask(__name__)


def index() -> str:
    """
    Render index.html template

    Returns:
        str: Rendered HTML content.
    """
    return render_template('0-index.html')


@app.route('/')
def main() -> str:
    """
    Route for the main page.

    Returns:
        str: Rendered HTML content.
    """
    return index()


if __name__ == '__main__':
    app.run(debug=True)
