FROM debian:latest

RUN apt-get update && apt-get upgrade -y && apt-get install -y python3 python3-pip vim

RUN apt-get install -y iproute2 net-tools iputils-ping tcpdump

COPY . /app

WORKDIR /app

CMD ["/bin/sh", "-c", "exec /bin/sh"]
