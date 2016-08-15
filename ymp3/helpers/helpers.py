import os
from ymp3 import LOCAL
from youtube_dl import YoutubeDL
from HTMLParser import HTMLParser


FILENAME_EXCLUDE = '<>:"/\|?*;'
# semi-colon is terminator in header


def delete_file(path):
    """
    safely delete file. Needed in case of Asynchronous threads
    """
    try:
        os.remove(path)
    except Exception:
        pass


def get_ffmpeg_path():
    if os.environ.get('FFMPEG_PATH'):
        return os.environ.get('FFMPEG_PATH')
    elif not LOCAL:  # openshift
        return 'ffmpeg/ffmpeg'
    else:
        return 'ffmpeg'  # hoping that it is set in PATH


def get_video_info_ydl(vid_id):
    """
    Gets video info using YoutubeDL
    """
    ydl = YoutubeDL()
    try:
        info_dict = ydl.extract_info(vid_id, download=False)
        return info_dict
    except:
        return {}


def get_filename_from_title(title):
    """
    Creates a filename from title
    """
    if not title:
        return 'music.mp3'
    title = HTMLParser().unescape(title)
    for _ in FILENAME_EXCLUDE:
        title = title.replace(_, ' ')  # provide readability with space
    return title[:40] + '.mp3'  # TODO - smart hunt


def html_unescape(text):
    """
    Remove &409D; type unicode symbols and convert them to real unicode
    """
    try:
        title = HTMLParser().unescape(text)
    except Exception:
        title = text
    return title
