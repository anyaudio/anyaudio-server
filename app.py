import requests
from flask import Flask, jsonify, request, render_template
from subprocess import check_output
from os import environ

from helpers.search import get_videos, get_video_attrs


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def home():
    return render_template('/home.html')


@app.route('/g/<string:vid_id>')
def get_link(vid_id):
    """
    Uses youtube-dl to fetch the direct link
    """
    command = 'youtube-dl https://www.youtube.com/watch?v=%s -f 140/m4a/bestaudio -g' % vid_id
    try:
        retval = check_output(command.split())
        retval = retval.strip()
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
