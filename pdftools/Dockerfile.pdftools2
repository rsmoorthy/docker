FROM rsmoorthy/apache-php5

MAINTAINER Moorthy RS "rsmoorthy@gmail.com"

#	wget -O wkhtmltox.deb http://download.gna.org/wkhtmltopdf/0.12/0.12.2.1/wkhtmltox-0.12.2.1_linux-trusty-amd64.deb && dpkg -i wkhtmltox.deb || true && \
RUN sed -i -e 's/^deb-src/# deb-src/' /etc/apt/sources.list && apt-get update && \
	apt-get install -y --no-install-recommends wget curl poppler-utils && \
	wget -O wkhtmltox.deb http://download.gna.org/wkhtmltopdf/0.12/0.12.2.1/wkhtmltox-0.12.2.1_linux-jessie-amd64.deb && dpkg -i wkhtmltox.deb || true && \
	apt-get -y -f install && \
	rm wkhtmltox.deb && \
    rm -rf /var/lib/apt/lists/* && rm -rf /usr/share/doc/* && rm -rf /usr/share/man/* && rm -rf /usr/share/locale/*

# Config files.
COPY pdf_service.php /var/www/index.php
COPY MTCORSVA.TTF /usr/local/share/fonts/MTCORSVA.TTF
COPY php.ini /etc/php5/cli/php.ini
COPY bootstrap.min.css /tmp
COPY bootstrap.min.js /tmp

# COPY conf/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 80

CMD /bin/bash -c "source /etc/apache2/envvars && exec /usr/sbin/apache2 -DFOREGROUND"
# CMD /usr/bin/php -S 0.0.0.0:80 /var/www/index.php
