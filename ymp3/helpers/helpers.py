import os
from ymp3 import LOCAL


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
