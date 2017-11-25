import traceback
import requests
from flask import Response

from anyaudio import logger
from flask import jsonify, request, render_template, url_for
from anyaudio import app, LOCAL

from anyaudio.helpers.search import get_videos, get_video_attrs, get_suggestions, \
    get_search_results_html, make_search_api_response
from anyaudio.helpers.helpers import get_filename_from_title, \
    record_request, get_download_link_youtube, make_error_response, generate_data
from anyaudio.helpers.encryption import get_key, encode_data, decode_data
from anyaudio.helpers.data import trending_playlist
from anyaudio.helpers.database import get_trending, get_api_log


@app.route('/api/v1/d')
@record_request
def download_file():
    """
    Download the file from the server.
    First downloads the file on the server using wget and then converts it using ffmpeg
    """
    try:
        url = request.args.get('url')
        # decode info from url
        data = decode_data(get_key(), url)
        vid_id = data['id']
        url = data['url']
        filename = get_filename_from_title(data['title'], ext='')
        m4a_path = 'static/%s.m4a' % vid_id
        # ^^ vid_id regex is filename friendly [a-zA-Z0-9_-]{11}

        # Handle partial request
        range_header = request.headers.get('Range', None)
        if range_header:
            from_bytes, until_bytes = range_header.replace('bytes=', '').split('-')
            if not until_bytes:
                until_bytes = int(from_bytes) + int(1024 * 1024 * 1)  # 1MB * 1 = 1MB
            headers = {'Range': 'bytes=%s-%s' % (from_bytes, until_bytes)}
            resp = requests.get(url, headers=headers, stream=True)
            rv = Response(generate_data(resp), 206, mimetype='audio/mp4', direct_passthrough=True)
            rv.headers.add('Content-Range', resp.headers.get('Content-Range'))
            rv.headers.add('Content-Disposition', 'attachment; filename="%s"' % filename)
            rv.headers.add('Content-Length', resp.headers['Content-Length'])
            return rv

        resp = requests.get(url, stream=True)
        filename += '.m4a'
        response = Response(generate_data(resp), mimetype='audio/mp4')
        # set headers
        # http://stackoverflow.com/questions/93551/how-to-encode-the-filename-
        response.headers.add('Content-Disposition', 'attachment; filename="%s"' % filename)
        response.headers.add('Content-Length', resp.headers['Content-Length'])
        return response
    except Exception as e:
        logger.info('Error %s' % str(e))
        logger.info(traceback.format_exc())
        return 'Bad things have happened', 500


@app.route('/api/v1/g')
@record_request
def get_link():
    """
    Uses youtube-dl to fetch the direct link
    """
    try:
        url = request.args.get('url')

        data = decode_data(get_key(), url)
        vid_id = data['id']
        title = data['title']
        retval = get_download_link_youtube(vid_id, 'm4a/bestaudio')
        if not LOCAL:
            retval = encode_data(get_key(), id=vid_id, title=title, url=retval, length=data['length'])
            retval = url_for('download_file', url=retval)

        ret_dict = {
            'status': 200,
            'requestLocation': '/api/v1/g',
            'url': retval
        }
        return jsonify(ret_dict)
    except Exception as e:
        logger.info(traceback.format_exc())
        return make_error_response(msg=str(e), endpoint='/api/v1/g')


@app.route('/api/v1/search')
@record_request
def search():
    """
    Search youtube and return results
    """
    try:
        search_term = request.args.get('q')
        raw_html = get_search_results_html(search_term)
        vids = get_videos(raw_html)
        ret_vids = []
        for _ in vids:
            temp = get_video_attrs(_)
            if temp:
                temp['get_url'] = '/api/v1' + temp['get_url']
                temp['stream_url'] = '/api/v1' + temp['stream_url']
                temp['suggest_url'] = temp['get_url'].replace('/g?', '/suggest?', 1)
                ret_vids.append(temp)
        ret_dict = make_search_api_response(search_term, ret_vids, '/api/v1/search')
    except Exception as e:
        return make_error_response(msg=str(e), endpoint='/api/v1/search')

    return jsonify(ret_dict)


@app.route('/api/v1/trending')
@record_request
def get_latest():
    """
    Get trending songs
    """
    try:
        max_count = int(request.args.get('number', '25'))
        if max_count <= 0:
            max_count = 1
        if max_count > 100:
            max_count = 100
    except ValueError:
        max_count = 25

    try:
        offset = int(request.args.get('offset', '0'))
        if offset < 0:
            offset = 0
        if offset > 100:
            offset = 100
    except ValueError:
        offset = 0

    _type = request.args.get('type', 'popular').split(',')

    ret_meta = {
        "count": max_count,
        "offset": offset,
        "type": ""
    }

    result_dict = {}
    for i in _type:
        if i in [_[0] for _ in trending_playlist]:
            ret_meta["type"] += i + ","
            result_dict[i] = get_trending(i, max_count, offset, get_url_prefix='/api/v1/g?url=')

    if len(ret_meta["type"]) > 0:
        ret_meta["type"] = ret_meta["type"][:-1]

    ret_dict = {
        'metadata': ret_meta,
        'results': result_dict
    }

    return jsonify(ret_dict)


@app.route('/logs')
def get_log_page():
    """
    View application logs
    """
    user_key = request.args.get('key')

    if not user_key or user_key != get_key():
        return render_template('/unauthorized.html')

    try:
        offset = int(request.args.get('offset', '0'))
        if offset < 0:
            offset = 0
    except Exception:
        offset = 0

    try:
        number = int(request.args.get('number', '10'))
        if number < 1:
            number = 1
    except Exception:
        number = 0

    result = get_api_log(number, offset)

    if offset - number < 0:
        prev_link = None
    else:
        prev_link = '/logs?key={0}&number={1}&offset={2}'.format(
            user_key,
            number,
            offset - number
        )

    next_link = '/logs?key={0}&number={1}&offset={2}'.format(
        user_key,
        number,
        offset + number
    )

    day_path = result['day_path']
    day_sum = sum([x[1] for x in day_path])

    month_path = result['month_path']
    month_sum = sum([x[1] for x in month_path])

    all_path = result['all_path']
    all_sum = sum([x[1] for x in all_path])

    return render_template(
        '/log_page.html', logs=result['logs'], number=number, offset=offset, prev_link=prev_link, next_link=next_link,
        day_path=day_path, day_sum=day_sum, month_path=month_path, month_sum=month_sum, all_path=result['all_path'],
        all_sum=all_sum, popular_queries=result['popular_query']

    )


@app.route('/api/v1/playlists')
def get_playlists():
    count = len(trending_playlist)
    result = []
    for item in trending_playlist:
        result.append(
            {
                "playlist": item[0],
                "url": item[1]
            }
        )

    response = {
        'status': 200,
        'requestLocation': '/api/v1/playlists',
        "metadata": {
            "count": count
        },
        "results": result
    }

    return jsonify(response)


@app.route('/api/v1/stream')
@record_request
def stream():
    url = request.args.get('url')
    stream_settings = {
        'lo': 'webm[abr<=64]/webm[abr<=80]/m4a[abr<=64]/[abr<=96]/m4a',
        'md': 'webm[abr>=64][abr<=96]/[abr>=64][abr<=96]/webm[abr>=96][abr<=128]/webm/m4a',
        'hi': 'webm/m4a'
    }
    try:
        req = decode_data(get_key(), url)
        vid_id = req['id']
        quality = req.get('quality', 'md')
        url = get_download_link_youtube(
            vid_id,
            stream_settings[quality]
        )
    except Exception as e:
        return make_error_response(msg=str(e), endpoint='api/v1/stream')
    return jsonify(
        status=200,
        url=url_for(
            'stream_handler',
            url=encode_data(get_key(), url=url)
        )
    )


@app.route('/api/v1/stream_handler')
@record_request
def stream_handler():
    url = request.args.get('url')

    try:
        url = decode_data(get_key(), url)['url']
    except Exception:
        return 'Bad URL', 400

    mime = 'audio/mp4'
    if url.find('mime=audio%2Fwebm') > -1:
        mime = 'audio/webm'

    range_header = request.headers.get('Range', None)
    if range_header:
        from_bytes, until_bytes = range_header.replace('bytes=', '').split('-')
        if not until_bytes:
            until_bytes = int(from_bytes) + int(1024 * 1024 * 1)  # 1MB * 1 = 1MB
        headers = {'Range': 'bytes=%s-%s' % (from_bytes, until_bytes)}
        r = requests.get(url, headers=headers)
        data = r.content
        rv = Response(data, 206, mimetype=mime, direct_passthrough=True)
        rv.headers.add('Content-Range', r.headers.get('Content-Range'))
        return rv

    r = requests.get(url, stream=True)

    return Response(generate_data(r), mimetype=mime)


@app.route('/api/v1/suggest')
@record_request
def suggest_songs():
    try:
        url = request.args.get('url')

        decoded_data = decode_data(get_key(), url)

        vid_id = decoded_data["id"]

        vids = get_suggestions(vid_id)

        count = len(vids)

        return jsonify(
            {
                "status": 200,
                "request_location": "/api/v1/suggest",
                "metadate": {
                    "count": count
                },
                "results": vids
            }
        )

    except Exception as e:
        return make_error_response(msg=str(e), endpoint='/api/v1/suggest')
