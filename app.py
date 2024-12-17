#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)

# Routes
@app.route('/')
def index():
    return render_template('index.html', title="Home")

@app.route('/page')
def page():
    return render_template('page.html', title="Page")

if __name__ == '__main__':
    app.run(debug=True)
