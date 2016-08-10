import base64
import os
import json


def encode(key, clear):
    st = ''
    incr = get_key_hash(key)
    for _ in clear:
        st += chr(incr + ord(_))
    return base64.b64encode(st)


def decode(key, enc):
    st = ''
    enc = base64.b64decode(enc)
    incr = get_key_hash(key)
    for _ in enc:
        st += chr(ord(_) - incr)
    return st


def get_key():
    return os.environ.get('SECRET_KEY', 'default key')


def get_key_hash(key):
    c = 0
    for _ in key:
        c += ord(_)
    return c % 20


def encode_data(key, **kwargs):
    data = json.dumps(kwargs, ensure_ascii=False, indent=None)
    return encode(key, data)


def decode_data(key, data):
    dec = decode(key, data)
    return json.loads(dec)
