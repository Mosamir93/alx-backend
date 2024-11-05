#!/usr/bin/env python3
"""A basic Flask app setup."""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """A / route index."""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
