import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Database Configuration
db_path = os.path.abspath(os.path.join(os.path.realpath(os.path.dirname(__file__)), '..', '..', '..', 'db'))
DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = '%s/database.db' % db_path
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''
DATABASE_OPTIONS = {}

SESSION_COOKIE_NAME = 'notabs_sessionid'
SESSION_COOKIE_DOMAIN = 'www.notabs.com'
CACHE_MIDDLEWARE_KEY_PREFIX = 'notabs_cache'

# SERVER_URL and MEDIA_SERVER_URL have no trailing slash.
SERVER_URL = 'http://www.notabs.com'
MEDIA_SERVER_URL = 'http://www.notabs.com'
# SITE_URL and MEDIA_URL have trailing slashes
SITE_URL = '%s/' % SERVER_URL
MEDIA_URL = '%s/media/' % MEDIA_SERVER_URL

EMAIL_HOST = ''
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
