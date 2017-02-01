from os import environ
from subprocess import call

from ymp3.helpers.database import init_databases
from ymp3.schedulers import trending, youtube_dl_upgrade


if __name__ == '__main__':

    # Create SQLite tables
    init_databases()

    # Start schedulers
    trending_scheduler = trending.TrendingScheduler()
    trending_scheduler.start()
    youtube_dl_upgrade_scheduler = youtube_dl_upgrade.YoutubeDLUpgrader()
    youtube_dl_upgrade_scheduler.start()

    # http://docs.gunicorn.org/en/stable/settings.html
    cmd = 'gunicorn ymp3:app -w 4 --worker-class eventlet --reload --log-level info'
    cmd += ' -b %s:%s' % (
        environ.get('OPENSHIFT_PYTHON_IP', '127.0.0.1'),
        environ.get('OPENSHIFT_PYTHON_PORT', '5000')
    )
    cmd += ' --worker-connections 1000 -t 150'  # 4 mins = 10 secs
    call(cmd.split())
    # app.run(
    #     host=environ.get('OPENSHIFT_PYTHON_IP', '127.0.0.1'),
    #     port=int(environ.get('OPENSHIFT_PYTHON_PORT', 5000))
    # )
