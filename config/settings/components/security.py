import os
import socket

from attr.converters import to_bool

from config.settings.production import get_list

# https://docs.djangoproject.com/en/dev/ref/settings/#session-engine
SESSION_ENGINE = os.getenv('SESSION_ENGINE', default='django.contrib.sessions.backends.db')

SESSION_CACHE_ALIAS = os.getenv('SESSION_CACHE_ALIAS', default='default')

# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-secure
SESSION_COOKIE_SECURE = to_bool(os.getenv('SESSION_COOKIE_SECURE', default=False))

# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-name
SESSION_COOKIE_NAME = os.getenv("SESSION_COOKIE_NAME", default="sessionid")

# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-httponly
SESSION_COOKIE_HTTPONLY = to_bool(os.getenv('SESSION_COOKIE_HTTPONLY', default=False))

# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-path
SESSION_COOKIE_PATH = os.getenv("SESSION_COOKIE_PATH", default="/")

# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-httponly
CSRF_COOKIE_HTTPONLY = to_bool(os.getenv('CSRF_COOKIE_HTTPONLY', default=False))

# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-secure
CSRF_COOKIE_SECURE = to_bool(os.getenv('CSRF_COOKIE_SECURE', default=False))

# https://docs.djangoproject.com/en/dev/ref/settings/#x-frame-options
X_FRAME_OPTIONS = "DENY"


hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#internal-ips
INTERNAL_IPS = get_list(os.getenv("INTERNAL_IPS", default="127.0.0.1,::1"))
INTERNAL_IPS += [".".join(ip.split(".")[:-1] + ["1"]) for ip in ips]

# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = get_list(os.getenv("ALLOWED_HOSTS", default="127.0.0.1"))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('APP_KEY')
assert SECRET_KEY
assert len(SECRET_KEY) >= 32


# https://docs.djangoproject.com/en/dev/ref/settings/#secure-proxy-ssl-header
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# https://docs.djangoproject.com/en/dev/ref/settings/#secure-ssl-redirect
SECURE_SSL_REDIRECT = to_bool(os.getenv("SECURE_SSL_REDIRECT", default=False))

# https://docs.djangoproject.com/en/dev/topics/security/#ssl-https
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-seconds
SECURE_HSTS_SECONDS = int(os.getenv('SECURE_HSTS_SECONDS', default=60))

# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-include-subdomains
SECURE_HSTS_INCLUDE_SUBDOMAINS = to_bool(os.getenv(
    "SECURE_HSTS_INCLUDE_SUBDOMAINS", default=False
))

# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-preload
SECURE_HSTS_PRELOAD = to_bool(os.getenv("SECURE_HSTS_PRELOAD", default=False))

# https://docs.djangoproject.com/en/dev/ref/middleware/#x-content-type-options-nosniff
SECURE_CONTENT_TYPE_NOSNIFF = to_bool(os.getenv(
    "SECURE_CONTENT_TYPE_NOSNIFF", default=True
))

SECURE_CROSS_ORIGIN_OPENER_POLICY = "same-origin"
SECURE_REDIRECT_EXEMPT = []
SECURE_REFERRER_POLICY = "same-origin"
SECURE_SSL_HOST = os.getenv("SECURE_SSL_HOST", default=None)
