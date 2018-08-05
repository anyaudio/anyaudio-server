# AnyAudio

Download any song that this world ever heard, and that too in your favorite format MP3.

A rich public API is also included.

[![Join the chat at https://gitter.im/Any-Audio/anyaudio-server](https://badges.gitter.im/iiitv/algos.svg)](https://gitter.im/Any-Audio/anyaudio-server?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Build Status](https://travis-ci.org/anyaudio/anyaudio-server.svg?branch=master)](https://travis-ci.org/anyaudio/anyaudio-server)

[Android App](https://github.com/bxute/musicgenie)

[![Launch on OpenShift](http://launch-shifter.rhcloud.com/button.svg)](https://openshift.redhat.com/app/console/application_type/custom?cartridges%5B%5D=python-2.7&initial_git_url=https%3A%2F%2Fgithub.com%2Faviaryan%2Fyoutube%2Dmp3%2Dserver.git&name=youtube%2Dmp3%2Dserver)

## Running

```
pipenv run app
```

## API

See [API v1 documentation](docs/api/v1/API-v1.md)


## Deployment on Openshift instructions

See [docs/OPENSHIFT.md](docs/OPENSHIFT.md)


## Deployment using Docker instructions

See [docs/DOCKER.md](docs/DOCKER.md)

## External Dependencies
* `ffmpeg`

	Make sure that you have `ffmpeg` and its path is set properly in `run.sh`

## Running tests

```bash
make test
# or
# python -m unittest discover tests
```
