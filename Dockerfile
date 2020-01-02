from httpd:latest
#FROM ubuntu:18.04

#RUN apt-get -y update && apt-get install -y apache2 httpd

#COPY 000-default.conf /etc/apache2/sites-available/000-default.conf
COPY code/ /var/www/html/
COPY code/ /usr/local/apache2/htdocs/

#EXPOSE 80
#CMD service apache2 restart && bash
#tail -f /var/log/apache/error.log
