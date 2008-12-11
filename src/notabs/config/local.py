DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Database Configuration
import os
db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'db'))
DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = '%s/database.db' % db_path
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''
DATABASE_OPTIONS = {}

SESSION_COOKIE_NAME = 'local_notabs_sessionid'
SESSION_COOKIE_DOMAIN = '127.0.0.1'
CACHE_MIDDLEWARE_KEY_PREFIX = 'local_notabs_cache'

# SERVER_URL and MEDIA_SERVER_URL have no trailing slash.
SERVER_URL = 'http://127.0.0.1:8000'
MEDIA_SERVER_URL = 'http://127.0.0.1:8000'
# SITE_URL and MEDIA_URL have trailing slashes
SITE_URL = '%s/' % SERVER_URL
MEDIA_URL = '%s/media/' % MEDIA_SERVER_URL

EMAIL_HOST = ''
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
