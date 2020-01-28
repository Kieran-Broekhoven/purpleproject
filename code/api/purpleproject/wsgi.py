import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'purpleproject.settings')
sys.path.insert(0, '/api/')

application = get_wsgi_application()
# import os
# import sys
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'purpleproject.settings')
# sys.path.append('/var/www/middleware')
# sys.path.append('/api')

# from purpleproject import settings
# # from django.core.wsgi import get_wsgi_application
# from django.core.handlers.wsgi import WSGIHandler

# class WSGIEnvironment(WSGIHandler):
#     def __call__(self, environ, start_response):
#         os.environ['DEBUG'] = environ.get('DEBUG')
#         return super(WSGIEnvironment, self).__call__(environ, start_response)

# application = WSGIEnvironment()