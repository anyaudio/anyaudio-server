FROM python:2-alpine
MAINTAINER Avi Aryan <avi.aryan123@gmail.com>

ENV INSTALL_PATH /ymp3
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY . .
# COPY requirements.txt requirements.txt
# RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/testing >> /etc/apk/repositories
RUN apk update
RUN apk add python-dev
RUN apk add libevent-dev
RUN pip install -r requirements.txt
# RUN pip install --editable .

CMD python app.py
