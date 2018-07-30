import json
import sqlite3
from anyaudio import DATABASE_PATH

from ..helpers.data import table_creation_sqlite_statements


def init_databases():
    init_sqlite_database()


def get_sqlite_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    return conn, conn.cursor()


def init_sqlite_database():
    conn, cursor = get_sqlite_connection()

    for statement in table_creation_sqlite_statements:
        cursor.execute(statement)

    conn.commit()
    conn.close()


def save_trending_songs(playlist_name, songs):
    conn, cursor = get_sqlite_connection()

    try:
        sql = 'insert into trending_songs values(?,?,?,?,?,?,?,?,?)'

        data = [
            (
                song['id'],
                song['title'],
                song['thumb'],
                song['uploader'],
                song['length'],
                song['views'],
                song['get_url'],
                playlist_name,
                song['description'].decode('utf-8')
            ) for song in songs
        ]

        cursor.executemany(sql, data)
        conn.commit()

    except Exception:
        import traceback
        traceback.print_exc()
        pass
    conn.close()


def get_trending(type='popular', count=25, offset=0, get_url_prefix=''):
    conn, cursor = get_sqlite_connection()

    sql = 'select * from trending_songs where playlist_ = ? limit ? offset ?'

    rows = cursor.execute(sql, (type, count, offset))

    vids = []
    for row in rows:
        vids.append(
            {
                'id': row[0],
                'title': row[1],
                'thumb': row[2],
                'uploader': row[3],
                'length': row[4],
                'views': row[5],
                'get_url': get_url_prefix + row[6],
                'stream_url': (get_url_prefix + row[6]).replace('/g?', '/stream?', 1),
                'description': row[8],
                'suggest_url': (get_url_prefix + row[6]).replace('/g?', '/suggest?', 1),
            }
        )

    conn.close()

    return vids


def clear_trending(pl_name):
    conn, cur = get_sqlite_connection()

    sql = 'delete from trending_songs where playlist_ = ?'

    cur.execute(sql, (pl_name,))

    conn.commit()
    conn.close()

