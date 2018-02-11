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
```

* Open a new shell and run the following command.

```sh
docker-compose run postgres psql -h postgres -p 5432 -U postgres --password
# enter password as test
```

* When in psql shell, create the database and then exit using `\q`.

```sql
create database anyaudio;
```

* Close the server and then start it again. Then navigate to `http://localhost` to view the app.
