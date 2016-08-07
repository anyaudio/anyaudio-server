from os import environ
from subprocess import call
from ymp3 import app, LOCAL


if __name__ == '__main__':
    call('gunicorn ymp3:app -w 4 --worker-class gevent')
    # if LOCAL:
    #     app.run(
    #         host=environ.get('OPENSHIFT_PYTHON_IP', '127.0.0.1'),
    #         port=int(environ.get('OPENSHIFT_PYTHON_PORT', 5000))
    #     )
    # else:
    #     from wsgiref.simple_server import make_server
    #     httpd = make_server(
    #         environ.get('OPENSHIFT_PYTHON_IP'),
    #         int(environ.get('OPENSHIFT_PYTHON_PORT')), app
    #     )
    #     httpd.serve_forever()
