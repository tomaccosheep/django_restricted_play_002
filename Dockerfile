FROM ubuntu:latest
MAINTAINER Al Burns
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential libmysqlclient-dev vim iputils-ping dnsutils curl
COPY . /app
COPY ./django_restricted_play_002/settings.py /app/django_restricted_play_002/settings.py
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["/bin/bash"]
CMD ["./entrypoint.sh"]
