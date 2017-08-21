FROM ubuntu:16.04

ENV DEBIAN_FRONTEND	noninteractive
MAINTAINER Moorthy "github.com/rsmoorthy"

RUN sed -i -e 's/^deb-src/# deb-src/' /etc/apt/sources.list
RUN dpkg --add-architecture i386 && apt-get update && \
	apt -y install --no-install-recommends software-properties-common

RUN add-apt-repository -y ppa:ubuntu-wine/ppa && apt update

RUN apt-get update && apt-get -y install --no-install-recommends\
    vim-tiny\
	less\
	curl\
	wget\
	nano\
	iproute2 iputils-ping net-tools\
	netcat-openbsd \
	x11vnc fluxbox matchbox wine1.8 winetricks \
	xvfb xterm \
	openbox python python-numpy geany menu python-xdg xdotool

# RUN apt-get -y install --no-install-recommends wine-gecko2.34 wine-gecko2.34:i386 wine-mono4.5.4 wine-mono0.0.8

RUN wget -o /usr/share/wine/wine_gecko-2.40-x86.msi http://dl.winehq.org/wine/wine-gecko/2.40/wine_gecko-2.40-x86.msi && \
	wget -o /usr/share/wine/wine_gecko-2.40-x86_64.msi http://dl.winehq.org/wine/wine-gecko/2.40/wine_gecko-2.40-x86_64.msi

# RUN wget -o /root/tally9_install.exe http://tallymirror.tallysolutions.com/download_centre/R5.4.6_Gold/TE9/Full/setup.exe

RUN locale-gen en_IN
ENV LANG en_IN
ENV LANGUAGE en_IN:en

RUN mkdir /root/noVNC

ADD noVNC /root/noVNC/

COPY start.sh /root/

COPY install_tally.sh /root/

COPY menu.xml /etc/xdg/openbox/

EXPOSE 5900 6080 9000

ENV DISPLAY=:0

CMD ["/root/start.sh"]
