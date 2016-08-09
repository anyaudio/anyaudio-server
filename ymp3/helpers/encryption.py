import base64
import os
# http://stackoverflow.com/a/16321853/2295672


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
