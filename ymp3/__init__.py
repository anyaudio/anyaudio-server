from flask import Flask
from os import environ


app = Flask(__name__)
app.config['DEBUG'] = True

DATABASE_PATH = 'SQLite.db'
LOCAL = True
if environ.get('OPENSHIFT_PYTHON_IP'):
    LOCAL = False


import views
