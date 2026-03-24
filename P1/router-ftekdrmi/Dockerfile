FROM frrouting/frr
RUN sed -i 's/bgpd=no/bgpd=yes/' /etc/frr/daemons
RUN sed -i 's/ospfd=no/ospfd=yes/' /etc/frr/daemons
RUN sed -i 's/isisd=no/isisd=yes/' /etc/frr/daemons 
CMD ["/bin/sh", "-c", "/usr/lib/frr/docker-start & exec /bin/sh"]

# the container is based on Alpine with the FRR software stack installed. This is a pre-built image.
# since the bgpd service provided under the FRR framework is disabled by default, we are enabling it.
# "" ospfd ""
# "" isid ""
# when starting FRR routing services in the background, it keeps the container running with an interactive linked BusyBox shell. The use of `exec` is critical for signal handling.
