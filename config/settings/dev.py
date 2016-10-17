from .base import *
import sys

DEBUG = True

INTERNAL_IPS = ('127.0.0.1', '10.0.2.2')

# Writes the e-mail that would be sent to standard output. Don't
# use this in production!
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# ADMINS = (
#     ('Your Name', 'username@example.com'),
# )

MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware', )
INSTALLED_APPS += (
    'debug_toolbar',
)
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

# Test settings
if 'test' in sys.argv:

    SOUTH_TESTS_MIGRATE = False
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
    }

    PASSWORD_HASHERS = (
        'django.contrib.auth.hashers.MD5PasswordHasher',
        'django.contrib.auth.hashers.SHA1PasswordHasher',
    )

try:
    LOCAL_SETTINGS_LOADED
except NameError:
    try:
        from .local import *
    except ImportError:
        SECRET_KEY = '<replace-this-with-a-new-random-string-or-put-the-secret-key-in-local-settings>'
