import redis

from anyaudio import logger

redis_client = redis.StrictRedis()

def get_or_create_video_download_link(video_id, format, callback):
    key = 'video:download:%s:%s' % (video_id, format)
    download_url = redis_client.get(key)
    if not download_url:
        logger.info('[Redis] cache miss for %s' % key)
        download_url = callback(video_id, format)
        redis_client.set(key, download_url, ex=60 * 60 * 6)  # Expires in 6 hours
    else:
        logger.info('[Redis] cache hit for %s' % key)
        download_url = download_url.decode('utf-8')
    return download_url
