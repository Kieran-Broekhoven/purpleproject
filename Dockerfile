#from httpd:latest
FROM ubuntu:18.04

RUN apt-get -y update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y python3.7 python3-pip apache2 php \
    libapache2-mod-php ssmtp mailutils libapache2-mod-wsgi-py3 python3-dev

RUN pip3 install flask pprint django

# RUN a2enmod php

COPY 000-default.conf /etc/apache2/sites-available/000-default.conf
COPY code/static /var/www/static
COPY code/api/ /api
COPY code/html/ /var/www/html/
COPY code/html/ /usr/local/apache2/htdocs/

EXPOSE 80
CMD service apache2 restart && tail -f /var/log/apache2/error.log
