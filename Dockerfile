FROM python:2-alpine
MAINTAINER Avi Aryan <avi.aryan123@gmail.com>

ENV INSTALL_PATH /ymp3
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY . .

# install deps
RUN apk update
RUN apk add --no-cache --virtual build-dependencies gcc python-dev libevent-dev linux-headers musl-dev \
	&& pip install -r requirements.txt \
	&& apk del build-dependencies

# update tar .. --strip-componenets not available in current version
RUN apk --update add --no-cache tar
# install ffmpeg
# wget, tar etc already present
RUN ash scripts/set_ffmpeg.sh

CMD python app.py
