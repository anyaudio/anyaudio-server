import requests
from flask import Flask, jsonify, request, render_template, url_for
from subprocess import check_output
from base64 import b64encode, b64decode
from os import environ

from helpers.search import get_videos, get_video_attrs


app = Flask(__name__)
app.config['DEBUG'] = True

LOCAL = True
if environ.get('OPENSHIFT_PYTHON_IP'):
    LOCAL = False

COMMAND = 'youtube-dl https://www.youtube.com/watch?v=%s -f 140/m4a/bestaudio'


@app.route('/')
def home():
    return render_template('/home.html')


@app.route('/d/<string:url>')
def download_file(url):
    """
    Download the file
    """
    # command = COMMAND % vid_id
    # command += ' --ffmpeg-location `echo $OPENSHIFT_REPO_DIR../../dependencies/ffmpeg`'
    # command += ' --audio-format mp3 --extract-audio'
    print url
    return b64decode(url)


@app.route('/g/<string:vid_id>')
def get_link(vid_id):
    """
    Uses youtube-dl to fetch the direct link
    """
    command = COMMAND % vid_id
    command += ' -g'
    print command
    try:
        retval = check_output(command.split())
        retval = retval.strip()
        if not LOCAL:
            retval = b64encode(retval)
            retval = url_for('download_file', url=retval)
        return jsonify({'status': 0, 'url': retval})
    except Exception:
        return jsonify({'status': 1, 'url': None})


@app.route('/search')
def search():
    """
    Search youtube and return results
    """
    search_term = request.args.get('q')
    link = 'https://www.youtube.com/results?search_query=%s' % search_term
    link += '&sp=EgIQAQ%253D%253D'  # for only video
    r = requests.get(
        link,
        allow_redirects=True
    )
    vids = get_videos(r.content)
    ret_vids = []
    for _ in vids:
        temp = get_video_attrs(_)
        if temp:
            ret_vids.append(temp)
    return jsonify(ret_vids)


if __name__ == '__main__':
    app.run(
        host=environ.get('OPENSHIFT_PYTHON_IP', '127.0.0.1'),
        port=int(environ.get('OPENSHIFT_PYTHON_PORT', 5000))
    )
