# Django settings for django-replicate project.
import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "./"))

sys.path.append(os.path.join(PROJECT_ROOT, 'modules'))
sys.path.append(os.path.join(PROJECT_ROOT, 'customization_apps'))
sys.path.append(os.path.join(PROJECT_ROOT, 'apps'))
sys.path.append(os.path.join(PROJECT_ROOT, 'shared_apps'))
sys.path.append(os.path.join(PROJECT_ROOT, '3rd_party_apps'))

PROJECT_TITLE = 'Django Replication'
PROJECT_NAME = 'django_replication'

DEBUG = False
DEVELOPMENT = False
TEMPLATE_DEBUG = DEBUG
ADMINS = (
	# ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(PROJECT_ROOT, "%s.sqlite" % PROJECT_NAME),     # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Puerto_Rico'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'site_media/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/site_media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = MEDIA_URL + 'admin_media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'o-66z7uh34_-rv_^u&6i0n0djz%lc^dlis+e*d2u2(ull$yw9&'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.load_template_source',
	'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
	# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
	# Always use forward slashes, even on Windows.
	# Don't forget to use absolute paths, not relative paths.
	'templates',
)

INSTALLED_APPS = [
    'grappelli',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.admin',
	'replicate',
]

GRAPPELLI_ADMIN_TITLE = PROJECT_TITLE

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.core.context_processors.auth",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    'django.core.context_processors.request',
    "grappelli.context_processors.admin_template_path",
    'django.contrib.messages.context_processors.messages',
]

#REPLICATE_LOG_FILENAME = 
#Default is /tmp/django_replicate.log

#REPLICATE_CHECKSCHEDULES_FREQUENCY
#Default is 45 seconds

try:
    from settings_local import *
except ImportError:
    pass

if DEVELOPMENT:
    INTERNAL_IPS = ('127.0.0.1',)
    try:
        import rosetta
        INSTALLED_APPS.append('rosetta')
    except ImportError:
        print "rosetta is not installed"

    try:
        import django_extensions
        INSTALLED_APPS.append('django_extensions')
    except ImportError:
        print "django_extensions is not installed"

    try:
        import debug_toolbar
#        INSTALLED_APPS.append('debug_toolbar')
    except ImportError:
        print "debug_toolbar is not installed"

    TEMPLATE_CONTEXT_PROCESSORS.append("django.core.context_processors.debug")

    WSGI_AUTO_RELOAD = True
    if 'debug_toolbar' in INSTALLED_APPS:
        MIDDLEWARE_CLASSES.append('debug_toolbar.middleware.DebugToolbarMiddleware')
        DEBUG_TOOLBAR_CONFIG={
            'INTERCEPT_REDIRECTS' : False,
        }
