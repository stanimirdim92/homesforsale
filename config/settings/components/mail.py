# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
import os

from attr.converters import to_bool

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
