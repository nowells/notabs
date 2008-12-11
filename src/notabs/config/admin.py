DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Database Configuration
DATABASE_ENGINE = ''
DATABASE_NAME = ''
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''

SESSION_COOKIE_NAME = 'notabs_sessionid'
CACHE_MIDDLEWARE_KEY_PREFIX = 'notabs_cache'

# SERVER_URL and MEDIA_SERVER_URL have no trailing slash.
SERVER_URL = 'http://admin.online.pbs.org'
MEDIA_SERVER_URL = 'http://admin.online.pbs.org'
# SITE_URL and MEDIA_URL have trailing slashes
SITE_URL = '%s/notabs/' % SERVER_URL
MEDIA_URL = '%s/notabs/media/' % MEDIA_SERVER_URL

EMAIL_HOST = 'smtp.pbs.org'
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
