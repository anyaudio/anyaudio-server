## Docker Deployment

Follow these steps to have YoutubeMP3 running inside a Docker container.
This tutorial assumes you have Docker and docker-compose installed.

* Clone the repo and cd into it

```sh
$ git clone https://github.com/aviaryan/youtube-mp3-server.git && cd youtube-mp3-server
```

* Build the image

```sh
$ docker-compose build
```

* Run the app

```sh
$ docker-compose up
Recreating ymp3_web_1
Attaching to ymp3_web_1
web_1  | [2016-08-09 05:22:08 +0000] [7] [INFO] Starting gunicorn 19.6.0
web_1  | [2016-08-09 05:22:08 +0000] [7] [INFO] Listening at: http://0.0.0.0:5000 (7)
web_1  | [2016-08-09 05:22:08 +0000] [7] [INFO] Using worker: eventlet
web_1  | [2016-08-09 05:22:08 +0000] [13] [INFO] Booting worker with pid: 13
web_1  | [2016-08-09 05:22:08 +0000] [14] [INFO] Booting worker with pid: 14
web_1  | [2016-08-09 05:22:08 +0000] [15] [INFO] Booting worker with pid: 15
web_1  | [2016-08-09 05:22:08 +0000] [16] [INFO] Booting worker with pid: 16
```

* Navigate to `http://localhost:5000` to view the app.
