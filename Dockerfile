# Dockerfile
FROM python:3.6

# We need wget to set up the PPA and xvfb to have a virtual screen and unzip to install the Chromedriver
RUN apt-get update -y
RUN apt-get install -y wget xvfb unzip

# install nodejs
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - \
&& apt-get install -y nodejs

RUN mkdir /app

ADD . /app
WORKDIR /app

RUN set -x \
 && ln -sf /usr/local/bin/python /bin/python \
 && pip install --upgrade pipenv \
 && pipenv install --system

RUN npm install && npm install -g gulp-cli

EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
