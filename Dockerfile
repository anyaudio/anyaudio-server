FROM python:2-alpine
MAINTAINER Avi Aryan <avi.aryan123@gmail.com>

ENV INSTALL_PATH /anyaudio
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

# update needed for wget
# update tar .. --strip-componenets not available in current version
# install permanent deps
RUN apk --update add --no-cache ca-certificates wget tar xz postgresql-dev
RUN update-ca-certificates

COPY requirements.txt requirements.txt

# install deps
RUN apk update
RUN apk add --no-cache --virtual build-dependencies gcc python-dev libevent-dev linux-headers musl-dev \
	&& pip install -r requirements.txt \
	&& apk del build-dependencies

# install ffmpeg
COPY scripts/set_ffmpeg.sh scripts/set_ffmpeg.sh
RUN ash scripts/set_ffmpeg.sh

# copy remaining files
COPY . .

CMD python app.py
