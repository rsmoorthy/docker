FROM ubuntu:16.04

ENV DEBIAN_FRONTEND	noninteractive
MAINTAINER Moorthy "github.com/rsmoorthy"

RUN sed -i -e 's/^deb-src/# deb-src/' /etc/apt/sources.list
RUN dpkg --add-architecture i386 && apt-get update && \
	apt -y install --no-install-recommends software-properties-common wget apt-transport-https

RUN wget https://dl.winehq.org/wine-builds/Release.key && apt-key add Release.key && \
	rm Release.key && \
	add-apt-repository 'https://dl.winehq.org/wine-builds/ubuntu/'

RUN apt-get update && apt-get -y install --no-install-recommends\
    vim\
	less\
	curl\
	nano\
	iproute2 iputils-ping net-tools\
	netcat-openbsd \
	x11vnc fluxbox matchbox winehq-stable winetricks \
	xvfb xterm \
	openbox python python-numpy geany menu python-xdg xdotool

# RUN apt-get -y install --no-install-recommends wine-gecko2.34 wine-gecko2.34:i386 wine-mono4.5.4 wine-mono0.0.8
RUN mkdir -p /root/.cache/wine && cd /root/.cache/wine && \
	wget -O /root/.cache/wine/wine_gecko-2.47-x86.msi http://dl.winehq.org/wine/wine-gecko/2.47/wine_gecko-2.47-x86.msi && \
	wget -O /root/.cache/wine/wine_gecko-2.47-x86_64.msi http://dl.winehq.org/wine/wine-gecko/2.47/wine_gecko-2.47-x86_64.msi && \
	wget -O /root/.cache/wine/wine-mono-4.6.4.msi http://dl.winehq.org/wine/wine-mono/4.6.4/wine-mono-4.6.4.msi


ENV LANG en_IN
ENV LANGUAGE en_IN:en
RUN apt-get -y --no-install-recommends install locales
RUN locale-gen en_IN

RUN mkdir /root/noVNC

COPY novnc.tgz /root/
RUN cd /root && tar zxvf novnc.tgz
#ADD noVNC /root/noVNC/

COPY start.sh /root/
COPY sevents.sh /root/
COPY install_tally.sh /root/
COPY menu.xml /etc/xdg/openbox/
COPY Narration.txt /root/
COPY Journal.txt /root/
COPY typekeys.py /root/
COPY web.py /root/

EXPOSE 5900 6080 9000 8080

ENV DISPLAY=:0

CMD ["/root/start.sh"]
