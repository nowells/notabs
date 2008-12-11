DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Database Configuration
import os
db_path = os.path.dirname(os.path.abspath(__file__+'/..'))
DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = '%s/database.db' % db_path
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''
DATABASE_OPTIONS = {}

SESSION_COOKIE_NAME = 'soup_notabs_sessionid'
SESSION_COOKIE_DOMAIN = 'soup.pbs.org'
CACHE_MIDDLEWARE_KEY_PREFIX = 'soup_notabs_cache'

# SERVER_URL and MEDIA_SERVER_URL have no trailing slash.
SERVER_URL = 'http://soup.pbs.org'
MEDIA_SERVER_URL = 'http://soup.pbs.org'
# SITE_URL and MEDIA_URL have trailing slashes
SITE_URL = '%s/notabs/' % SERVER_URL
MEDIA_URL = '%s/notabs/media/' % MEDIA_SERVER_URL

EMAIL_HOST = 'localhost'
EMAIL_PORT = 2600
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
