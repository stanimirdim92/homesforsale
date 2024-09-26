"""

Config ideas taken from https://github.com/cookiecutter/cookiecutter-django

Django settings for hfs project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import logging
import os
from os.path import join
from pathlib import Path

import django_stubs_ext
from attr.converters import to_bool
from django.conf.global_settings import ADMINS
from django.db.backends.postgresql.psycopg_any import IsolationLevel
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from dotenv import load_dotenv, find_dotenv
from rest_framework import ISO_8601

# Monkeypatching Django, so stubs will work for all generics,
# see: https://github.com/typeddjango/django-stubs
django_stubs_ext.monkeypatch()

def get_list(text):
    return [item.strip() for item in text.split(",")]


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent

find_dotenv()
load_dotenv(join(BASE_DIR, '.env'))

# GENERAL

# Whether to append trailing slashes to URLs.
APPEND_SLASH = False

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
DEBUG = to_bool(os.getenv('APP_DEBUG', False))

# TIMEZONE

# Local time zone. Choices are
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# though not all of them may be available with every OS.
# In Windows, this must be set to your system time zone.
# https://docs.djangoproject.com/en/dev/ref/settings/#std-setting-TIME_ZONE
TIME_ZONE = os.getenv('TIME_ZONE', 'UTC')
TIME_ZONE_CHOICES = [(tz, tz) for tz in timezone.zoneinfo.available_timezones()]

# https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True

# LANGUAGES

# https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = os.getenv("LANGUAGE_CODE", 'en-us')

# https://docs.djangoproject.com/en/dev/ref/settings/#languages
LANGUAGES = [
    ("ast", _("Asturian")),
    ("bg", _("Bulgarian")),
    ("cs", _("Czech")),
    ("da", _("Danish")),
    ("nl", _("Dutch")),
    ("de", _("German")),
    ("el", _("Greek")),
    ("en", _("English")),
    ("es", _("Spanish")),
    ("et", _("Estonian")),
    ("fi", _("Finnish")),
    ("fr", _("French")),
    ("ga", _("Irish")),
    ("hr", _("Croatian")),
    ("hu", _("Hungarian")),
    ("it", _("Italian")),
    ("lt", _("Lithuanian")),
    ("lv", _("Latvian")),
    ("pl", _("Polish")),
    ("pt", _("Portuguese")),
    ("ro", _("Romanian")),
    ("ru", _("Russian")),
    ("sk", _("Slovak")),
    ("sl", _("Slovenian")),
    ("sv", _("Swedish")),
]

# https://docs.djangoproject.com/en/dev/ref/settings/#locale-paths
LOCALE_PATHS = [str(BASE_DIR / "locale")]

# DATABASES

# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.{}'.format(os.getenv('DB_CONNECTION')),
        'NAME': os.getenv('DB_DATABASE'),
        'USER': os.getenv('DB_USERNAME'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),

        'ATOMIC_REQUESTS': True,
        'CONN_HEALTH_CHECKS': True,
        'CONN_MAX_AGE': int(os.getenv('CONN_MAX_AGE', default=60)),

        'OPTIONS': {
            'client_encoding': 'UTF8',
            "server_side_binding": True,
            "isolation_level": IsolationLevel.SERIALIZABLE,
            'options': '-c search_path=' + os.getenv('DB_SCHEMA')
        },
    }
}

# APPS

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

# MIGRATIONS

# https://docs.djangoproject.com/en/dev/ref/settings/#migration-modules
MIGRATION_MODULES = {"users": "users.migrations"}

# AUTHENTICATION

# https://docs.djangoproject.com/en/dev/ref/settings/#authentication-backends
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
]
USERSESSIONS_TRACK_ACTIVITY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-user-model
AUTH_USER_MODEL = "users.User"
# # https://docs.djangoproject.com/en/dev/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL =  "/"
# https://docs.djangoproject.com/en/dev/ref/settings/#login-url
# LOGIN_URL = "account_login"
# https://django-allauth.readthedocs.io/en/latest/account/configuration.html
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_UNKNOWN_ACCOUNTS = False
ACCOUNT_CHANGE_EMAIL = False
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_ALLOW_REGISTRATION = to_bool(os.getenv('ACCOUNT_ALLOW_REGISTRATION', True))
ACCOUNT_ADAPTER = "users.adapters.AccountAdapter"
# https://docs.allauth.org/en/latest/account/forms.html

HEADLESS_ONLY = True
HEADLESS_FRONTEND_URLS = {
    "account_confirm_email": "/account/verify-email/{key}",
    "account_reset_password": "/account/password/reset",
    "account_reset_password_from_key": "/account/password/reset/key/{key}",
    "account_signup": "/account/signup",
    "socialaccount_login_error": "/account/provider/callback",
}


# ACCOUNT_FORMS = {
#     'add_email': 'allauth.account.forms.AddEmailForm',
#     'change_password': 'allauth.account.forms.ChangePasswordForm',
#     'confirm_login_code': 'allauth.account.forms.ConfirmLoginCodeForm',
#     'login': 'allauth.account.forms.LoginForm',
#     'request_login_code': 'allauth.account.forms.RequestLoginCodeForm',
#     'reset_password': 'allauth.account.forms.ResetPasswordForm',
#     'reset_password_from_key': 'allauth.account.forms.ResetPasswordKeyForm',
#     'set_password': 'allauth.account.forms.SetPasswordForm',
#     'signup': 'users.forms.UserSignupForm',
#     'user_token': 'allauth.account.forms.UserTokenForm',
# }
# ACCOUNT_SIGNUP_FORM_CLASS = 'users.forms.UserSignupForm'

# https://docs.allauth.org/en/latest/socialaccount/configuration.html
SOCIALACCOUNT_ADAPTER = "users.adapters.SocialAccountAdapter"
# https://docs.allauth.org/en/latest/socialaccount/configuration.html
SOCIALACCOUNT_FORMS = {"signup": "users.forms.UserSocialSignupForm"}

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        "APP": {
            "client_id": "123",
            "secret": "456",
            "key": ""
        },
        # These are provider-specific settings that can only be
        # listed here:
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
        'OAUTH_PKCE_ENABLED': True,
        'EMAIL_AUTHENTICATION': True,
    },
    'facebook': {
        "APP": {
            "client_id": "123",
            "secret": "456",
            "key": ""
        },
        'METHOD': 'oauth2',  # Set to 'js_sdk' to use the Facebook connect SDK
        'SDK_URL': '//connect.facebook.net/{locale}/sdk.js',
        'SCOPE': ['email', 'public_profile'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'first_name',
            'last_name',
            'middle_name',
            'name',
            'name_format',
            'picture',
            'short_name'
        ],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': lambda request: 'en_US',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v13.0',
        'GRAPH_API_URL': 'https://graph.facebook.com/v13.0',
    },
    "openid_connect": {
        "APPS": [
            {
                "provider_id": "linkedin",
                "name": "LinkedIn",
                "client_id": "123",
                "secret": "456",
                "settings": {
                    "server_url": "https://www.linkedin.com/oauth",
                },
            }
        ]
    },
}

# PASSWORDS

# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = [
    # https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
    "django.contrib.auth.hashers.Argon2PasswordHasher",
]

# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        "OPTIONS": {
            "min_length": 9,
        },
    },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

#

# https://docs.djangoproject.com/en/dev/ref/settings/#middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # 'django.middleware.cache.UpdateCacheMiddleware',  # redis https://docs.djangoproject.com/en/5.1/topics/cache/#order-of-middleware
    "corsheaders.middleware.CorsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",

    'django.contrib.sessions.middleware.SessionMiddleware',  # Modify Vary header
    'django.middleware.locale.LocaleMiddleware', # Modify Vary header
    # 'django.middleware.gzip.GZipMiddleware', # Modify Vary header BREACH?

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Associates users with requests using sessions.
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware', # redis https://docs.djangoproject.com/en/5.1/topics/cache/#order-of-middleware

    'allauth.account.middleware.AccountMiddleware',
    'allauth.usersessions.middleware.UserSessionsMiddleware',
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

# STATIC

# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(BASE_DIR / "staticfiles")
# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = "static/"
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [str(BASE_DIR / "static")]

# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    # https://django-compressor.readthedocs.io/en/stable/quickstart.html
]
# MEDIA

# https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(BASE_DIR / "media")
# https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = "/media/"

# TEMPLATES

# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # https://docs.djangoproject.com/en/dev/ref/settings/#dirs
        "DIRS": [str(BASE_DIR / "templates")],
        # https://docs.djangoproject.com/en/dev/ref/settings/#app-dirs
        "APP_DIRS": True,
        'OPTIONS': {
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "users.context_processors.allauth_settings",
            ],
            "string_if_invalid": '!! variable "%s" is missing !!' if DEBUG else "",
        },
    },
]

# https://docs.djangoproject.com/en/dev/ref/settings/#form-renderer
FORM_RENDERER = "django.forms.renderers.TemplatesSetting"

# FIXTURES

# https://docs.djangoproject.com/en/dev/ref/settings/#fixture-dirs
FIXTURE_DIRS = (str(BASE_DIR / "fixtures"),)

# SECURITY

# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-httponly
SESSION_COOKIE_HTTPONLY = to_bool(os.getenv('SESSION_COOKIE_HTTPONLY', default=False))
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-httponly
CSRF_COOKIE_HTTPONLY = to_bool(os.getenv('CSRF_COOKIE_HTTPONLY', default=False))
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-secure
CSRF_COOKIE_SECURE = to_bool(os.getenv('CSRF_COOKIE_SECURE', default=False))

# https://docs.djangoproject.com/en/dev/ref/settings/#x-frame-options
X_FRAME_OPTIONS = "DENY"

# EMAIL

# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = os.getenv(
    "DJANGO_EMAIL_BACKEND",
    default="django.core.mail.backends.smtp.EmailBackend",
)
# https://docs.djangoproject.com/en/dev/ref/settings/#email-timeout
EMAIL_TIMEOUT = 20
EMAIL_SUBJECT_PREFIX = ""
DEFAULT_FROM_EMAIL = os.getenv("EMAIL_FROM_ADDRESS", default="webmaster@localhost")
SERVER_EMAIL = os.getenv("EMAIL_FROM_ADDRESS_ERROR", default="webmaster@localhost")
EMAIL_HOST = os.getenv("EMAIL_HOST", default="localhost")
EMAIL_PORT = os.getenv("EMAIL_PORT", default=25)
EMAIL_HOST_USER = os.getenv("EMAIL_USER", default="")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_PASSWORD", default="")
EMAIL_USE_TLS = to_bool(os.getenv("EMAIL_USE_TLS", default=False))
EMAIL_USE_SSL = to_bool(os.getenv("EMAIL_USE_SSL", default=False))

# ADMIN

# Django Admin URL.
ADMIN_URL = "admin/"
# https://docs.djangoproject.com/en/dev/ref/settings/#admins
# ADMINS = [()]
# https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

# LOGGING

# https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

# Make the `logging` Python module capture `warnings.warn()` calls
# This is needed in order to log them as JSON when DEBUG=False
logging.captureWarnings(True)
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "formatters": {
        "verbose": {
            "format": (
                "%(asctime)s %(levelname)s %(name)s %(message)s "
                "[MODULE: %(module)s |PID:%(process)d:%(threadName)s]"
            )
        },
    },
    "handlers": {
        "default": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
        "null": {
            "class": "logging.NullHandler",
        },
    },
    "root": {"level": "INFO", "handlers": ["default"]},
    "loggers": {
        "django": {"level": "ERROR", "propagate": True},
        "django.request": {
            "handlers": ["default", "mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
        "django.server": {
            "handlers": ["default", "mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
        "django.security.DisallowedHost": {
            "level": "ERROR",
            "handlers": ["default", "mail_admins"],
            "propagate": True,
        },
    },
}

# DRF
REST_FRAMEWORK = {
    # Base API policies
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        # 'rest_framework.renderers.TemplateHTMLRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        # 'rest_framework.permissions.IsAuthenticatedOrReadOnly',
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',

    # Generic view behavior
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ],
    # Schema
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',

    # Throttling
    'DEFAULT_THROTTLE_RATES': {
        'user': None,
        'anon': None,
    },
    'NUM_PROXIES': None,

    # Pagination
    'PAGE_SIZE': 50,

    # Filtering
    'SEARCH_PARAM': 'search',
    'ORDERING_PARAM': 'ordering',

    # Input and output formats
    'DATE_FORMAT': ISO_8601,
    'DATE_INPUT_FORMATS': [ISO_8601],

    'DATETIME_FORMAT': ISO_8601,
    'DATETIME_INPUT_FORMATS': [ISO_8601],

    'TIME_FORMAT': ISO_8601,
    'TIME_INPUT_FORMATS': [ISO_8601],

    # Encoding
    'UNICODE_JSON': True,
    'COMPACT_JSON': True,
    'STRICT_JSON': True,
    'COERCE_DECIMAL_TO_STRING': True,
    'UPLOADED_FILES_USE_URL': True,

    # Browsable API
    'HTML_SELECT_CUTOFF': 1000,
    'HTML_SELECT_CUTOFF_TEXT': "More than {count} items...",

    # Schemas
    'SCHEMA_COERCE_PATH_PK': True,
    'SCHEMA_COERCE_METHOD_NAMES': {
        'retrieve': 'read',
        'destroy': 'delete'
    },
}

# CORS
# https://github.com/adamchainz/django-cors-headers#setup
CORS_URLS_REGEX = r"^/api/.*$"
CORS_ALLOWED_ORIGINS = get_list(os.getenv("CORS_ALLOWED_ORIGINS", default="http://127.0.0.1:8000"))
CORS_TRUSTED_ORIGINS = get_list(os.getenv("CORS_TRUSTED_ORIGINS", default="http://127.0.0.1:8000"))

# SCHEMA DOCS
SPECTACULAR_SETTINGS = {
    'SWAGGER_UI_DIST': 'SIDECAR',  # shorthand to use the sidecar instead
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    'REDOC_DIST': 'SIDECAR',
    'TITLE': os.getenv('APP_NAME'),
    'DESCRIPTION': '',
    'VERSION': os.getenv('APP_VERSION'),
    'SERVE_INCLUDE_SCHEMA': True,
    "SERVE_PERMISSIONS": ["rest_framework.permissions.IsAuthenticated"],  # TODO add permissions?
}

# CACHE
# https://docs.djangoproject.com/en/stable/topics/cache/#redis
CACHES = {
    'default': {
        "BACKEND": os.getenv('REDIS_BACKEND', 'django.core.cache.backends.DummyCache'),
        'KEY_PREFIX': os.getenv('REDIS_PREFIX'),
        'LOCATION': get_list(os.getenv('REDIS_URL')),
        'TIMEOUT': int(os.getenv('CACHE_TIMEOUT', default=60)),
        'OPTIONS': {
            # WARNING: Shard client is still experimental, so be careful when using it in production environments.
            "CLIENT_CLASS": "django_redis.client.ShardClient",
            'db': os.getenv('REDIS_DB'),
            'parser_class': 'redis.connection.PythonParser',
            'pool_class': 'redis.BlockingConnectionPool',
            "IGNORE_EXCEPTIONS": False,
            "COMPRESSOR": "django_redis.compressors.lz4.Lz4Compressor",
            "PARSER_CLASS": "redis.connection._HiredisParser",
            "MAX_ENTRIES": int(os.getenv('CACHE_MAX_ENTRIES', default=300)),
        }
    }
}

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# SESSION

# https://docs.djangoproject.com/en/dev/ref/settings/#session-engine
SESSION_ENGINE = os.getenv('SESSION_ENGINE', default='django.contrib.sessions.backends.db')
SESSION_CACHE_ALIAS = os.getenv('SESSION_CACHE_ALIAS', default='default')
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-secure
SESSION_COOKIE_SECURE = to_bool(os.getenv('SESSION_COOKIE_SECURE', default=False))

if DEBUG:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] += [
        'rest_framework.renderers.BrowsableAPIRenderer',
    ]

    SPECTACULAR_SETTINGS['SERVE_PERMISSIONS'] = ["rest_framework.permissions.AllowAny"]
