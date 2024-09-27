"""For more information on this file, see.
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see.
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from os.path import join
from pathlib import Path

import django_stubs_ext
from dotenv import find_dotenv, load_dotenv
from split_settings.tools import include

# Monkeypatching Django, so stubs will work for all generics,
# see: https://github.com/typeddjango/django-stubs
django_stubs_ext.monkeypatch()


def get_list(text):
    return [item.strip() for item in text.split(",")]


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent

find_dotenv()
load_dotenv(join(BASE_DIR, '.env'))

include(
    'components/admin.py',
    'components/apps.py',
    'components/auth.py',
    'components/cache.py',
    'components/common.py',
    'components/cors.py',
    'components/database.py',
    'components/drf.py',
    'components/language.py',
    'components/logging.py',
    'components/mail.py',
    'components/security.py',
    'components/static.py',
    'components/templates.py',
    'components/time.py',
)
