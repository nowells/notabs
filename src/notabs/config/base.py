import os

# Absolute path to the directory that holds the project's python module.
SITE_ROOT = os.path.realpath(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Absolute path to the directory that holds the project python path.
PROJECT_ROOT = os.path.realpath(os.path.abspath(os.path.join(SITE_ROOT, '..')))
# Absolute path to the directory that holds the deployed project.
DEPLOYED_ROOT = os.path.realpath(os.path.abspath(os.path.join(PROJECT_ROOT, '..')))
# Absolute path to the directory that holds media.
MEDIA_ROOT = os.path.realpath(os.path.abspath(os.path.join(DEPLOYED_ROOT, 'media')))

# Debug Settings
DEBUG = True
TEMPLATE_DEBUG = DEBUG
ADMINS = (
    ('WebTech', 'webtech@pbs.org'),
)
INTERNAL_IPS = (
)

MANAGERS = ADMINS

# Database Configuration
DATABASE_ENGINE = ''
DATABASE_NAME = ''
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''
DATABASE_OPTIONS = {}
# For MySQL you should set
# DATABASE_OPTIONS = {
#    'sql_mode': 'TRADITIONAL,STRICT_ALL_TABLES,ANSI',
#    'charset': 'utf8',
#    'init_command': 'SET storage_engine=INNODB',
# }

# Local time zone for this installation. All choices can be found here:
# http://www.postgresql.org/docs/current/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'en-us'
USE_I18N = False
SITE_ID = 1

# SERVER_URL and MEDIA_SERVER_URL have no trailing slash.
SERVER_URL = ''
MEDIA_SERVER_URL = ''
# SITE_URL and MEDIA_URL have a trailing slash.
SITE_URL = '%s/' % SERVER_URL
MEDIA_URL = '%s/media/' % MEDIA_SERVER_URL

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
ADMIN_MEDIA_PREFIX = '/django-admin-media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'tka7*l^pz0cd25iiaselhi^q8)+co#j5u5n1y+u!ut^#%!b0fx'

# Email Config
DEFAULT_FROM_EMAIL = 'no-reply@pbs.org'
EMAIL_HOST = 'localhost'
EMAIL_HOST_PASSWORD = ''
EMAIL_HOST_USER = ''
EMAIL_PORT = 25
EMAIL_SUBJECT_PREFIX = ''
EMAIL_USE_TLS = False
SEND_BROKEN_LINK_EMAILS = False
SERVER_EMAIL = 'webtech@pbs.org'

# General Config
DATE_FORMAT = 'm/d/Y'

# Session Configuration
SESSION_COOKIE_AGE = 60 * 60 * 24 * 7 * 2 # 2 weeks in seconds
SESSION_COOKIE_DOMAIN = '.pbs.org'
SESSION_COOKIE_NAME = 'notabs_sessionid'
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_SAVE_EVERY_REQUEST = False

# Caching Configuration
CACHE_BACKEND = 'dummy:///'
CACHE_KEY_PREFIX = ''
CACHE_SECONDS = 3600 # 1 hour in seconds
CACHE_MIDDLEWARE_KEY_PREFIX = ''
CACHE_MIDDLEWARE_SECONDS = 3600 # 1 hour in seconds

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'pbs.django.apps.notifications.NotificationMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.core.context_processors.debug',
    'django.core.context_processors.auth',
    'pbs.django.apps.notifications.notifications',
    'notabs.core.context_processors.site_config',
)

ROOT_URLCONF = 'notabs.urls'

TEMPLATE_DIRS = (
    '%s/templates' % SITE_ROOT,
)

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sitemaps',
    'django.contrib.markup',
    'django.contrib.humanize',
    'django.contrib.comments',
    'pbs.django.apps.deployment',
    'pbs.django.apps.notifications',
    'jellyroll',
    'tagging',
    'threadedcomments',
    'basic.blog',
    'basic.inlines',
    'basic.books',
    'basic.people',
)

DEPLOYED_MEDIA_ROOT = 'deployed'

###########################################
## Legacy Settings - Remove as appropriate
ROOT_PATH = SITE_ROOT
