from os import environ
from subprocess import call


if __name__ == '__main__':
    # http://docs.gunicorn.org/en/stable/settings.html
    cmd = 'gunicorn ymp3:app -w 4 --worker-class eventlet --reload'
    cmd += ' -b %s:%s' % (
        environ.get('OPENSHIFT_PYTHON_IP', '127.0.0.1'),
        environ.get('OPENSHIFT_PYTHON_PORT', '5000')
    )
    cmd += ' -t 90'  # 4 mins = 10 secs
    call(cmd.split())
    # app.run(
    #     host=environ.get('OPENSHIFT_PYTHON_IP', '127.0.0.1'),
    #     port=int(environ.get('OPENSHIFT_PYTHON_PORT', 5000))
    # )
