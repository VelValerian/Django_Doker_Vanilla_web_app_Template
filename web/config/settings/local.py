from .base import *

# 🛠️ LOCAL DEVELOPMENT SETTINGS
DEBUG = True

ALLOWED_HOSTS = ['*']

# 🛡️ SECURITY OVERWRITES (NOT FOR PRODUCTION)
AUTH_PASSWORD_VALIDATORS = []

# 🧬 DEBUG TOOLS
INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = ['127.0.0.1', 'localhost']
