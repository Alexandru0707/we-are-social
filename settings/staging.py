from base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', '<your STRIPE_PUBLISHABLE key>')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', '<your STRIPE SECRET key>')

# Paypal environment variables
PAYPAL_NOTIFY_URL = 'https://291e2d8f.ngrok.io/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'aaron@codeinstitute.net'

SITE_URL = 'https://your-heroku-app.herokuapp.com'
ALLOWED_HOSTS.append('your-heroku-app.herokuapp.com')

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