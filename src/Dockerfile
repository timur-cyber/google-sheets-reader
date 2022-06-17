FROM python:3.9-slim-buster

RUN mkdir /src
WORKDIR /src
ADD requirements.txt /src

RUN apt-get update \
    && apt-get -y install libpq-dev python-dev gcc
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ADD . /src
EXPOSE 5001
ENTRYPOINT ["gunicorn","--bind","0.0.0.0:5001","wsgi:app"]