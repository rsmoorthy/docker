FROM debian:jessie

MAINTAINER Moorthy RS "rsmoorthy@gmail.com"

ENV DEBIAN_FRONTEND	noninteractive

RUN sed -i -e 's/^deb-src/# deb-src/' /etc/apt/sources.list

# Basic system tools
RUN apt-get update && apt-get -y install --no-install-recommends\
    vim-tiny\
	less\
	curl\
	wget\
	nano\
	iproute2 iputils-ping net-tools\
	netcat-openbsd && \
	rm -rf /var/lib/apt/lists/* &&\
	rm -rf /usr/share/doc/* && rm -rf /usr/share/man/* && rm -rf /usr/share/locale/*

# Basic dev tools
RUN apt-get update && apt-get -y install --no-install-recommends \
	git openssh-server cron logrotate supervisor && \
	mkdir /var/run/sshd && \
	echo 'root:root' | chpasswd && \
	sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
	rm -rf /var/lib/apt/lists/* && \
	rm -rf /usr/share/doc/* && rm -rf /usr/share/man/* && rm -rf /usr/share/locale/*

CMD ["bash"]
