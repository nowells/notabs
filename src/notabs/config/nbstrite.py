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

SESSION_COOKIE_NAME = 'nbstrite_notabs_sessionid'
SESSION_COOKIE_DOMAIN = 'dipsy.pbs.org'
CACHE_MIDDLEWARE_KEY_PREFIX = 'nbstrite_notabs_cache'

# SERVER_URL and MEDIA_SERVER_URL have no trailing slash.
SERVER_URL = 'http://dipsy.pbs.org'
MEDIA_SERVER_URL = 'http://dipsy.pbs.org'
# SITE_URL and MEDIA_URL have trailing slashes
SITE_URL = '%s/~nbstrite/notabs/' % SERVER_URL
MEDIA_URL = '%s/~nbstrite/notabs/media/' % MEDIA_SERVER_URL

EMAIL_HOST = ''
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
