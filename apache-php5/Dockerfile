FROM ubuntu:15.04

MAINTAINER Moorthy RS "rsmoorthy@gmail.com"

ENV APACHE_RUN_USER  www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_PID_FILE  /var/run/apache2.pid
ENV APACHE_RUN_DIR   /var/run/apache2
ENV APACHE_LOCK_DIR  /var/lock/apache2
ENV APACHE_LOG_DIR   /var/log/apache2
ENV APACHE_USER_UID 0

RUN sed -i -e 's/^deb-src/# deb-src/' /etc/apt/sources.list && \
	apt-get update

RUN DEBIAN_FRONTEND=noninteractive apt-get -y install --no-install-recommends\
    vim-tiny\
	less\
	curl\
	netcat-openbsd\
    wget\
    build-essential && \
	rm -rf /var/lib/apt/lists/* && rm -rf /usr/share/doc/* && rm -rf /usr/share/man/* && rm -rf /usr/share/locale/*

# PHP && Apache
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install --no-install-recommends\
    php5\
    php5-curl\
    php5-gd\
    php5-dev\
    php5-imap\
    php5-imagick\
    php-pear\
    mcrypt\
    php5-mcrypt\
    php5-mongo\
    imagemagick\
    apache2-mpm-prefork\
    apache2-utils\
    mpack\
    libuuid1 uuid-dev uuid-runtime\
	libyaml-dev\
    libapache2-mod-php5 &&\
    rm -rf /var/lib/apt/lists/* &&\
    a2enmod rewrite &&\
    a2enmod actions &&\
    pear install --alldeps Mail &&\
    yes "" | pecl install uuid &&\
    echo 'extension=uuid.so' | tee /etc/php5/mods-available/uuid.ini &&\
    php5enmod uuid &&\
    yes "" | pecl install yaml &&\
    echo 'extension=yaml.so' | tee /etc/php5/mods-available/yaml.ini &&\
    php5enmod yaml &&\
    php5enmod mcrypt &&\
    php5enmod mongo &&\
    rm -rf /usr/share/doc/* &&\
    rm -rf /usr/share/man/* &&\
    rm -rf /usr/share/locale/* &&\
    echo "ServerName localhost" >> /etc/apache2/apache2.conf

#RUN add-apt-repository ppa:ecometrica/servers && apt-get update -qq && DEBIAN_FRONTEND=noninteractive apt-get -yqq install --no-install-recommends\
#	wkhtmltopdf &&\
#    rm -rf /var/lib/apt/lists/* &&\
#    rm -rf /usr/share/doc/* &&\
#    rm -rf /usr/share/man/* &&\
#    rm -rf /usr/share/locale/*

#RUN apt-get update -qq && wget -O wkhtmltox.deb http://download.gna.org/wkhtmltopdf/0.12/0.12.2.1/wkhtmltox-0.12.2.1_linux-trusty-amd64.deb && dpkg -i wkhtmltox.deb || true && \
#	apt-get -yqq -f install --no-install-recommends && \
#	rm wkhtmltox.deb && \
#    rm -rf /var/lib/apt/lists/* && rm -rf /usr/share/doc/* && rm -rf /usr/share/man/* && rm -rf /usr/share/locale/*

RUN apt-get -y install \
	git openssh-server cron logrotate supervisor && \
	mkdir /var/run/sshd && \
	echo 'root:journo' | chpasswd && \
	sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
	rm -rf /var/lib/apt/lists/* && rm -rf /usr/share/doc/* && rm -rf /usr/share/man/* && rm -rf /usr/share/locale/*


# Config files.
COPY conf/apache/000-default /etc/apache2/sites-enabled/000-default
COPY conf/php5/apache2/php.ini /etc/php5/apache2/php.ini
COPY conf/php5/cli/php.ini /etc/php5/cli/php.ini
COPY script/start.bash /root/start.bash
COPY script/index.php /var/www/index.php

COPY conf/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 22 80

CMD ["/usr/bin/supervisord"]
#CMD ["/bin/bash"]
