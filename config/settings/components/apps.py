from config.settings.components.common import DEBUG

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "django.forms",
]

THIRD_PARTY_APPS = [
    "django_extensions",
    "django_filters",
    "drf_spectacular",
    "drf_spectacular_sidecar",
    "rosetta",
    "phonenumber_field",
    "robots",

    # "django_celery_beat",
    # "crispy_forms",

    "corsheaders",
    "rest_framework",
    "rest_framework.authtoken",

    "allauth",
    "allauth.account",
    "allauth.headless",
    "allauth.mfa",
    "allauth.usersessions",
    "allauth.socialaccount",
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.openid_connect',
]

LOCAL_APPS = [
    'users'
]

# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

if DEBUG:
    # http://whitenoise.evans.io/en/latest/django.html#using-whitenoise-in-development
    INSTALLED_APPS = [*INSTALLED_APPS, 'sslserver', "whitenoise.runserver_nostatic", 'debug_toolbar']
