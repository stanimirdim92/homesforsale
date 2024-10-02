import os

from django.utils import timezone

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
