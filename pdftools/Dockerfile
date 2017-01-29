FROM ubuntu:15.04

MAINTAINER Moorthy RS "rsmoorthy@gmail.com"

#RUN add-apt-repository ppa:ecometrica/servers && apt-get update -qq && DEBIAN_FRONTEND=noninteractive apt-get -yqq install --no-install-recommends\
#	wkhtmltopdf &&\
#    rm -rf /var/lib/apt/lists/* &&\
#    rm -rf /usr/share/doc/* &&\
#    rm -rf /usr/share/man/* &&\
#    rm -rf /usr/share/locale/*

RUN sed -i -e 's/^deb-src/# deb-src/' /etc/apt/sources.list && apt-get update && \
	apt-get install -y --no-install-recommends wget curl poppler-utils && \
	apt-get install -y php5-cli && \
	wget -O wkhtmltox.deb http://download.gna.org/wkhtmltopdf/0.12/0.12.2.1/wkhtmltox-0.12.2.1_linux-trusty-amd64.deb && dpkg -i wkhtmltox.deb || true && \
	apt-get -y -f install && \
	rm wkhtmltox.deb && \
    rm -rf /var/lib/apt/lists/* && rm -rf /usr/share/doc/* && rm -rf /usr/share/man/* && rm -rf /usr/share/locale/*

# Config files.
COPY pdf_service.php /var/www/index.php
COPY MTCORSVA.TTF /usr/local/share/fonts/MTCORSVA.TTF
COPY php.ini /etc/php5/cli/php.ini
COPY bootstrap.min.css /tmp
COPY bootstrap.min.js /tmp

EXPOSE 80

CMD /usr/bin/php -S 0.0.0.0:80 /var/www/index.php
