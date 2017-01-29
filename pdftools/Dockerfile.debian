FROM rsmoorthy/apache-php5

MAINTAINER Moorthy RS "rsmoorthy@gmail.com"

#RUN add-apt-repository ppa:ecometrica/servers && apt-get update -qq && DEBIAN_FRONTEND=noninteractive apt-get -yqq install --no-install-recommends\
#	wkhtmltopdf &&\
#    rm -rf /var/lib/apt/lists/* &&\
#    rm -rf /usr/share/doc/* &&\
#    rm -rf /usr/share/man/* &&\
#    rm -rf /usr/share/locale/*

RUN apt-get update && wget -O wkhtmltox.deb http://download.gna.org/wkhtmltopdf/0.12/0.12.2.1/wkhtmltox-0.12.2.1_linux-trusty-amd64.deb && dpkg -i wkhtmltox.deb || true && \
	apt-get -y -f install && \
	rm wkhtmltox.deb && \
    rm -rf /var/lib/apt/lists/* && rm -rf /usr/share/doc/* && rm -rf /usr/share/man/* && rm -rf /usr/share/locale/*

# Config files.
COPY pdf_service.php /var/www/index.php
COPY bootstrap.min.css /tmp
COPY bootstrap.min.js /tmp
