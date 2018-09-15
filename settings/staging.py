from base import *
import dj_database_url

DEBUG = False

# Load the ClearDB connection details from the environment variable
DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
}

STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_AC799DLHoVLESzRQViBEKl1e')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_mas6PxM1yX0PbOTnZfxFgMbP')


PAYPAL_NOTIFY_URL = 'https://we-are-social-heroku-app.herokuapp.com'
PAYPAL_RECEIVER_EMAIL = 'alex_boys30@yahoo.com'

SITE_URL = 'https://we-are-social-heroku-app.herokuapp.com'
ALLOWED_HOSTS.append('we-are-social-heroku-app.herokuapp.com')

# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}