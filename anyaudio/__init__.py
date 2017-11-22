import logging
from flask import Flask
from os import environ
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['DEBUG'] = True

DATABASE_PATH = 'SQLite.db'
LOCAL = True
if environ.get('OPENSHIFT_PYTHON_IP'):
    LOCAL = False

# Logger
logger = logging.getLogger('anyaudio-server')
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(
    '%(relativeCreated)6d %(threadName)s %(message)s'
))
logger.addHandler(handler)
logger.setLevel(logging.INFO)


@app.after_request
def after_request(response):
    response.headers.add('Accept-Ranges', 'bytes')
    return response


import views
