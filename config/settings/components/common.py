# Whether to append trailing slashes to URLs.
import os

# APPEND_SLASH = False

# https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = int(os.getenv('SITE_ID'))

# https://docs.djangoproject.com/en/stable/ref/settings/#std:setting-DEFAULT_AUTO_FIELD
# This must stay ID so many other 3rd party packages can work without any problems
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = "config.urls"

# https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = "config.wsgi.application"

# DEBUG

# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = os.getenv('APP_ENV') == 'production'


# https://docs.djangoproject.com/en/dev/ref/settings/#middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # 'django.middleware.cache.UpdateCacheMiddleware',  # redis https://docs.djangoproject.com/en/5.1/topics/cache/#order-of-middleware
    'django.middleware.http.ConditionalGetMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",

    'django.contrib.sessions.middleware.SessionMiddleware',  # Modify Vary header
    'django.middleware.locale.LocaleMiddleware', # Modify Vary header
    # 'django.middleware.gzip.GZipMiddleware', # Modify Vary header. BREACH?

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Associates users with requests using sessions.
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'allauth.account.middleware.AccountMiddleware',
    'allauth.usersessions.middleware.UserSessionsMiddleware',

    # 'django.middleware.cache.FetchFromCacheMiddleware',  # redis https://docs.djangoproject.com/en/5.1/topics/cache/#order-of-middleware
]

if DEBUG:
    MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware")
    # https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html#debug-toolbar-config
    DEBUG_TOOLBAR_CONFIG = {
        "DISABLE_PANELS": [
            "debug_toolbar.panels.redirects.RedirectsPanel",
            # Disable profiling panel due to an issue with Python 3.12:
            # https://github.com/jazzband/django-debug-toolbar/issues/1875
            "debug_toolbar.panels.profiling.ProfilingPanel",
        ],
        "SHOW_TEMPLATE_CONTEXT": True,
    }




STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

