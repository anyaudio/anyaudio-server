import re
from os import environ
from ymp3 import logger
from networking import open_page
from encryption import get_key, encode_data
from helpers import html_unescape


def get_trending_videos(html):
    """
    Get trending youtube videos from html
    """
    regex = '<tr.*?data-video-id="(.*?)".*?src="(.*?)".*?<a cl.*?>(.*?)</a>.*?by.*?>(.*?)</a>.*?<span .*?>(.*?)</'

    raw_results = re.findall(
        regex,
        html,
        re.DOTALL
    )[:int(environ.get('PLAYLIST_VIDEOS_LIMIT', 100))]

    vids = []
    for raw_result in raw_results:
        try:
            vids.append(
                {
                    'id': raw_result[0],
                    'thumb': 'http://img.youtube.com/vi/{0}/0.jpg'.format(raw_result[0]),
                    'title': html_unescape(raw_result[2].strip().decode('utf-8')),
                    'uploader': raw_result[3].decode('utf8'),
                    'length': raw_result[4],
                    'views': get_views(video_id=raw_result[0]),
                    'get_url': encode_data(get_key(), id=raw_result[0], title=raw_result[2].strip())
                }
            )
        except Exception as e:
            logger.info(
                'Getting trending video failed. Message: %s, Video: %s' % (
                    str(e), raw_result[0]
                )
            )
    return vids


def get_views(video_id):
    url = 'https://www.youtube.com/watch?v={0}'.format(video_id)
    content = open_page(url)
    return re.findall(
        '<div class="watch-view-count">(.*?) ',
        content,
    )[0]
