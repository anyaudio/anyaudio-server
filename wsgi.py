"""
wsgi entrypoint
similar to app.py
"""
from anyaudio.helpers.database import init_databases
from anyaudio.schedulers import trending, youtube_dl_upgrade
from anyaudio import app


if __name__ == '__main__':

    # Create SQLite tables
    init_databases()

    # Start schedulers
    trending_scheduler = trending.TrendingScheduler()
    trending_scheduler.start()
    youtube_dl_upgrade_scheduler = youtube_dl_upgrade.YoutubeDLUpgrader()
    youtube_dl_upgrade_scheduler.start()

    app.run()
