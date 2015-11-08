FROM rsmoorthy/debian

MAINTAINER Moorthy RS "rsmoorthy@gmail.com"

ENV DEBIAN_FRONTEND	noninteractive
ENV APACHE_RUN_USER  root
ENV APACHE_RUN_GROUP root
ENV APACHE_PID_FILE  /var/run/apache2.pid
ENV APACHE_RUN_DIR   /var/run/apache2
ENV APACHE_LOCK_DIR  /var/lock/apache2
ENV APACHE_LOG_DIR   /var/log/apache2
ENV APACHE_USER_UID 0

# PHP && Apache
RUN apt-get update && apt-get -y install --no-install-recommends\
    php5\
    php5-curl\
    php5-gd\
    php5-imap\
    php5-imagick\
    php-pear\
    mcrypt\
    php5-mcrypt\
    php5-mongo\
    php5-redis\
    php5-memcached\
    php5-sybase\
    php5-sqlite\
    php5-mysql\
    imagemagick\
    apache2-mpm-prefork\
    apache2-utils\
    mpack\
    libuuid1 uuid-dev uuid-runtime\
	libyaml-dev\
    libapache2-mod-php5 &&\
    rm -rf /var/lib/apt/lists/* &&\
    a2enmod rewrite actions &&\
    php5enmod mcrypt &&\
    php5enmod mongo &&\
    pear install --alldeps Mail &&\
	curl --insecure -OL https://github.com/rsmoorthy/php5-uuid/releases/download/1.0-1/php5-uuid_1.0-1.deb && \
	dpkg -i php5-uuid_1.0-1.deb && \
	rm php5-uuid_1.0-1.deb && \
	curl --insecure -OL https://github.com/rsmoorthy/php5-yaml/releases/download/1.0-1/php5-yaml_1.0-1.deb && \
	dpkg -i php5-yaml_1.0-1.deb && \
	rm php5-yaml_1.0-1.deb && \
    rm -rf /usr/share/doc/* &&\
    rm -rf /usr/share/man/* &&\
    rm -rf /usr/share/locale/* &&\
    echo "ServerName localhost" >> /etc/apache2/apache2.conf

# Config files.
COPY conf/apache/000-default.conf /etc/apache2/sites-available/
COPY conf/php5/apache2/php.ini /etc/php5/apache2/php.ini
COPY conf/php5/cli/php.ini /etc/php5/cli/php.ini
COPY script/index.php /var/www/index.php

COPY conf/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 22 80

CMD ["/usr/bin/supervisord"]
