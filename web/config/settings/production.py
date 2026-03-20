import os
from .base import *

# 🛡️ PRODUCTION SETTINGS (HARDENED)
DEBUG = False

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

# 🧬 SECURITY OVERWRITES
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# 🔧 STATIC & MEDIA (PRODUCTION STRATEGY)
# Раздача через Nginx/CDN с хешированием имен файлов для кеширования.
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.ManifestStaticFilesStorage",
    },
}

# 🛠️ AXES PRODUCTION LOGIC
AXES_BEHIND_REVERSE_PROXY = True
AXES_IP_EXTRACTOR = 'axes.helpers.get_ip'
