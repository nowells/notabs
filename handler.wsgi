import os, sys
sys.path.insert(0, '/fs/lib/python')
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 've/lib/python2.5/site-packages'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'notabs.settings'
os.environ['SERVER_IDENTIFIER'] = 'www'

import django.core.handlers.wsgi

_application = django.core.handlers.wsgi.WSGIHandler()

def application(environ, start_response):
    environ['PATH_INFO'] = environ['SCRIPT_NAME'] + environ['PATH_INFO']
    return _application(environ, start_response)