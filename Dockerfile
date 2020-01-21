#from httpd:latest
FROM python:3.7

RUN apt-get -y update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y python3-pip apache2 \
    libapache2-mod-php mailutils libapache2-mod-wsgi-py3 python3-dev build-essential libssl-dev

RUN python3.7 -m pip install flask pprint django requests beautifulsoup4 brow pymysql mysqlclient

COPY 000-default.conf /etc/apache2/sites-available/000-default.conf
COPY code/static /var/www/static
COPY code/api/ /api
# RUN chmod 777 /api/db.sqlite3
COPY code/html/ /var/www/html/
COPY code/html/ /usr/local/apache2/htdocs/
# RUN python3.7 /api/manage.py collectstatic --noinput

EXPOSE 80
# CMD service apache2 restart && tail -f /var/log/apache2/error.log
CMD apachectl -DFOREGROUND
