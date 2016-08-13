import re

from encryption import get_key, encode_data
from HTMLParser import HTMLParser
from networking import open_page

INF = float("inf")


def get_videos(html):
    """
    separate videos in html
    """
    first = html.find('yt-lockup-tile')
    html = html[first + 2:]
    vid = []
    while True:
        pos = html.find('yt-lockup-tile')
        if pos == -1:
            pos = INF
        vid.append(html[:pos + 2])
        html = html[pos + 3:]
        if pos == INF:
            break
    return vid


def get_video_attrs(html):
    """
    get video attributes from html
    """
    result = {}
    # get video id and description
    regex = 'yt\-lockup\-title.*?href.*?watch\?v\=(.*?[^\"]+)'
    regex += '.*? title\=\"(.*?[^\"]+)'
    temp = re.findall(regex, html)
    if len(temp) and len(temp[0]) == 2:
        result['id'] = temp[0][0]
        result['title'] = temp[0][1]
    # length
    length_regex = 'video\-time.*?\>([^\<]+)'
    temp = re.findall(length_regex, html)
    if len(temp) > 0:
        result['length'] = temp[0].strip()
    # uploader
    upl_regex = 'yt\-lockup\-byline.*?\>.*?\>([^\<]+)'
    temp = re.findall(upl_regex, html)
    if len(temp) > 0:
        result['uploader'] = temp[0].strip()
    # time ago
    time_regex = 'yt\-lockup\-meta\-info.*?\>.*?\>([^\<]+).*?([0-9\,]+)'
    temp = re.findall(time_regex, html)
    if len(temp) and len(temp[0]) == 2:
        result['time'] = temp[0][0]
        result['views'] = temp[0][1]
    # thumbnail
    if 'id' in result:
        thumb = 'http://img.youtube.com/vi/%s/0.jpg' % result['id']
        result['thumb'] = thumb
    else:
        return None
    # check if all items present. If not present, usually some problem in parsing
    if len(result) != 7:
        return None
    # check length
    try:
        dur = int(result['length'].replace(':', '').strip())  # 20 mins
        if dur > 2000:
            return None
    except:
        pass
    # return
    result['get_url'] = '/g?url=' + encode_data(get_key(), id=result['id'], title=result['title'])
    return result


def get_trending_videos(html):
    """
    Get trending youtube videos from html
    """
    regex = '<tr.*?data-video-id="(.*?)".*?src="(.*?)".*?<a cl.*?>(.*?)</a>.*?by.*?>(.*?)</a>.*?<span .*?>(.*?)</'

    raw_results = re.findall(
        regex,
        html,
        re.DOTALL
    )

    vids = []
    for raw_result in raw_results:
        vids.append(
            {
                'id': raw_result[0],
                'thumb': raw_result[1],
                'title': html_unescape(raw_result[2].strip().decode('utf-8')),
                'uploader': raw_result[3].decode('utf8'),
                'length': raw_result[4],
                'views': get_views(video_id = raw_result[0]),
                'get_url': encode_data(get_key(), id = raw_result[0], title=raw_result[2].strip())
            }
        )
    return vids


def get_views(video_id):
    url = 'https://www.youtube.com/watch?v={0}'.format(video_id)
    content = open_page(url)

    return re.findall(
        '<div class="watch-view-count">(.*?) ',
        content,
    )[0]


def html_unescape(text):
    try:
        title = HTMLParser().unescape(text)
    except Exception:
        title = text
    return title
