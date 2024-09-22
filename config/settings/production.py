import socket

from .base import *  # noqa

find_dotenv()
load_dotenv(join(BASE_DIR, '.env'))
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#internal-ips
INTERNAL_IPS = os.getenv("INTERNAL_IPS", default="127.0.0.1").split(",")
INTERNAL_IPS += [".".join(ip.split(".")[:-1] + ["1"]) for ip in ips]

# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", default="127.0.0.1").split(",")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('APP_KEY')
assert SECRET_KEY


# SECURITY MIDDLEWARE
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-proxy-ssl-header
# SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# https://docs.djangoproject.com/en/dev/ref/settings/#secure-ssl-redirect
SECURE_SSL_REDIRECT = to_bool(os.getenv("SECURE_SSL_REDIRECT", default=False))

# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-secure
CSRF_COOKIE_SECURE = to_bool(os.getenv('CSRF_COOKIE_SECURE', default=False))

# # https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-name
# SESSION_COOKIE_NAME = os.getenv("SESSION_COOKIE_NAME")
#
# # https://docs.djangoproject.com/en/dev/topics/security/#ssl-https
# # https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-seconds
SECURE_HSTS_SECONDS = int(os.getenv('SECURE_HSTS_SECONDS', default=60))
#
# # # https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-include-subdomains
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
