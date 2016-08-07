from os import environ
from subprocess import call


if __name__ == '__main__':
    # http://docs.gunicorn.org/en/stable/settings.html
    cmd = 'gunicorn ymp3:app -w 4 --worker-class eventlet'
    cmd += ' -b %s:%s' % (
        environ.get('OPENSHIFT_PYTHON_IP', '127.0.0.1'),
        environ.get('OPENSHIFT_PYTHON_PORT', '5000')
    )
    call(cmd.split())
