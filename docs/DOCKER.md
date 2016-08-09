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
$ docker run -p 5000:5000 ymp3_web
# docker-compose up has some issues
```

* Navigate to `http://localhost:5000` to view the app.
