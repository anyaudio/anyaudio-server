import requests
import traceback
import logging
from flask import jsonify, request, render_template, url_for, make_response
from subprocess import check_output, call
from base64 import b64encode, b64decode
from ymp3 import app, LOCAL

from helpers.search import get_videos, get_video_attrs
from helpers.helpers import delete_file, get_ffmpeg_path


@app.route('/')
def home():
    return render_template('/home.html')


@app.route('/d/<string:url>')
def download_file(url):
    """
    Download the file from the server.
    First downloads the file on the server using wget and then converts it using ffmpeg
    """
    try:
        vid_id, url = b64decode(url).split(' ', 1)  # zz
        m4a_path = 'static/%s.m4a' % vid_id
        mp3_path = 'static/%s.mp3' % vid_id
        # vid_id regex is filename friendly [a-zA-Z0-9_-]{11}
        command = 'wget -O %s %s' % (m4a_path, url)
        check_output(command.split())
        command = get_ffmpeg_path()
        command += ' -i %s -acodec libmp3lame -ab 128k %s -y' % (m4a_path, mp3_path)
        call(command, shell=True)  # shell=True only works, return ret_code
        data = open(mp3_path, 'r').read()
        response = make_response(data)
        # set headers
        response.headers['Content-Disposition'] = 'attachment; filename=music.mp3'
        response.headers['Content-Type'] = 'audio/mpeg'  # or audio/mpeg3
        response.headers['Content-Length'] = str(len(data))
        # remove files
        delete_file(m4a_path)
        delete_file(mp3_path)
        # stream
        return response
    except Exception:
        logging.error(traceback.format_exc())
        return 'Bad things have happened', 400


@app.route('/g/<string:vid_id>')
def get_link(vid_id):
    """
    Uses youtube-dl to fetch the direct link
    """
    command = 'youtube-dl https://www.youtube.com/watch?v=%s -f m4a/bestaudio' % vid_id
    command += ' -g'
    print command
    try:
        retval = check_output(command.split())
        retval = retval.strip()
        if not LOCAL:
            retval = b64encode(vid_id + ' ' + retval)
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
