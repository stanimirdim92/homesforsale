import os

from config.settings.production import get_list

# https://github.com/adamchainz/django-cors-headers#setup
CORS_URLS_REGEX = r"^/api/.*$"
CORS_ALLOWED_ORIGINS = get_list(os.getenv("CORS_ALLOWED_ORIGINS", default="http://127.0.0.1:8000"))
CORS_TRUSTED_ORIGINS = get_list(os.getenv("CORS_TRUSTED_ORIGINS", default="http://127.0.0.1:8000"))
