#!/usr/bin/env python3

from flask import Flask, render_template
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables [eg. os.getenv('SECRET_KEY')]
load_dotenv()

# Routes
@app.route('/')
def index():
    return render_template('index.html', title="Home")

@app.route('/page')
def page():
    return render_template('page.html', title="Page")

if __name__ == '__main__':
    app.run(debug=True)
