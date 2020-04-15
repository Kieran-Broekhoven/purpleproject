#from httpd:latest
FROM python:3.8

# RUN apt-get -y update && \
#     DEBIAN_FRONTEND=noninteractive apt-get install -y python3-pip apache2 \
#     libapache2-mod-php mailutils libapache2-mod-wsgi-py3 python3-dev build-essential libssl-dev
RUN apt-get -y update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y python3-pip python3-dev uwsgi \
    uwsgi-plugin-python3 libpcre3-dev libssl-dev python3-mysqldb mailutils build-essential

RUN python3.8 -m pip install --upgrade pip
RUN python3.8 -m pip install --upgrade flask pprint django requests beautifulsoup4 brow pymysql \
    mysqlclient uWSGI Werkzeug uwsgi pyopenssl mysqlclient

# COPY 000-default.conf /etc/apache2/sites-available/000-default.conf
COPY code/static/img/ /var/www/static/img/
COPY code/static/fonts/ /var/www/static/fonts/
COPY code/static/header.html /var/www/static/header.html
COPY code/api/ /api
# RUN python3.8 /api/manage.py collectstatic --noinput
COPY code/static/js/ /var/www/static/js/
COPY code/static/css/ /var/www/static/css/
# RUN chmod 777 /api/db.sqlite3
COPY code/html/ /var/www/html/
COPY code/html/ /usr/local/apache2/htdocs/

EXPOSE 80

# CMD /api/setenv.sh && service apache2 restart && tail -f /var/log/apache2/error.log
CMD uwsgi --wsgi-file /api/purpleproject/wsgi.py --processes 5 --master \
    --http 0.0.0.0:80 --callable application --static-map /static=/var/www/static
# CMD apachectl -DFOREGROUND
