FROM alpine:latest
RUN apk add --no-cache busybox
CMD ["/bin/sh"]

# it's a base of system. we followed the recommendation highlighted in the document
# it installs the busybox package without unnecessarily bloating the container (without caching the package).
# this command, which is linked to BusyBox, will be executed at the start of the container.
