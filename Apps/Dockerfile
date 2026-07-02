FROM debian:latest

RUN apt-get update && apt-get upgrade -y && apt-get install -y python3 python3-pip vim

COPY . /app

WORKDIR /app

CMD ["/bin/sh", "-c", "/usr/lib/frr/docker-start & exec /bin/sh"]
