from flask import Flask, jsonify
from subprocess import check_output
from os import environ

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def home():
    return 'Hello'


@app.route('/g/<string:vid_id>')
def get_link(vid_id):
    """
    Uses youtube-dl to fetch the direct link
    """
    command = 'youtube-dl https://www.youtube.com/watch?v=%s -f bestaudio -g' % vid_id
    try:
        retval = check_output(command.split())
        retval = retval.strip()
        return jsonify({'status': 0, 'url': retval})
    except Exception:
        return jsonify({'status': 1, 'url': None})


if __name__ == '__main__':
    app.run(
        host=environ.get('OPENSHIFT_PYTHON_IP', '127.0.0.1'),
        port=environ.get('OPENSHIFT_PYTHON_PORT', 5000)
    )
