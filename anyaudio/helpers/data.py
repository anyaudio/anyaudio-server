import os

trending_playlist = [
    ('Popular', 'https://www.youtube.com/playlist?list=PLFgquLnL59alCl_2TQvOiD5Vgm1hCaGSI'),
    ('Latest', 'https://www.youtube.com/playlist?list=PLFgquLnL59akA2PflFpeQG9L01VFg90wS'),
    ('India', 'https://www.youtube.com/playlist?list=PLFgquLnL59alF0GjxEs0V_XFCe7LM3ReH'),
    ('Weekly', 'https://www.youtube.com/playlist?list=PLFgquLnL59alW3xmYiWRaoz0oM3H17Lth'),
    ('Electronic', 'https://www.youtube.com/playlist?list=PLFPg_IUxqnZNnACUGsfn50DySIOVSkiKI'),
    ('Popular Music Videos', 'https://www.youtube.com/playlist?list=PLFgquLnL59alCl_2TQvOiD5Vgm1hCaGSI'),
    ('New Music This Week', 'https://www.youtube.com/playlist?list=PLFgquLnL59alW3xmYiWRaoz0oM3H17Lth'),
    ('Top Tracks', 'https://www.youtube.com/playlist?list=PLFgquLnL59alcyTM2lkWJU34KtfPXQDaX'),
    ('Hip Hop and R&B Hotlist', 'https://www.youtube.com/playlist?list=PLFgquLnL59amBBTCULGWSotJu2CkioYkj'),
    ('Pop Hotlist', 'https://www.youtube.com/playlist?list=PLFgquLnL59altZg1f_Kr1kGUYE6j-NE0M'),
    ('Most Viewed', 'https://www.youtube.com/playlist?list=PL8A83124F1D79BD4F')
]

user_agents = [
    'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    'Googlebot/2.1 (+http://www.google.com/bot.html)',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'
    ' Ubuntu Chromium/49.0.2623.108 Chrome/49.0.2623.108 Safari/537.36',
    'Gigabot/3.0 (http://www.gigablast.com/spider.html)',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; pt-BR) AppleWebKit/533.3 '
    '(KHTML, like Gecko)  QtWeb Internet Browser/3.7 http://www.QtWeb.net',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/41.0.2228.0 Safari/537.36',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, '
    'like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.4pre) '
    'Gecko/20070404 K-Ninja/2.1.3',
    'Mozilla/5.0 (Future Star Technologies Corp.; Star-Blade OS; x86_64; U; '
    'en-US) iNet Browser 4.7',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.13) '
    'Gecko/20080414 Firefox/2.0.0.13 Pogo/2.0.0.13.6866',
    'WorldWideweb (NEXT)'
]

table_creation_sqlite_statements = [
    '''create table if not exists trending_songs(id_ text, title_ text, thumb_ text, uploader_ text, length_ text, views_ text, get_url_ text, playlist_ text, description text)''',
]
