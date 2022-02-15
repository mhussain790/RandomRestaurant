from flask import Flask, render_template, json, redirect, url_for
from flask.helpers import flash
from flask_mysqldb import MySQL
from flask import request
from flask_bootstrap import Bootstrap
import os

# Configuration

app = Flask(__name__, template_folder='templates')
Bootstrap(app)


@app.route('/')
def root():
    return render_template('index.html')


# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9113))
    #                                 ^^^^
    #              You can replace this number with any valid port

    app.run(port=port, debug=True)
