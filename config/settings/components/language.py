
from django.utils.translation import gettext_lazy as _

from config.settings.production import BASE_DIR

# https://docs.djangoproject.com/en/dev/ref/settings/#language-code
# LANGUAGE_CODE = os.getenv("LANGUAGE_CODE", 'en')
#
# # https://docs.djangoproject.com/en/dev/ref/settings/#languages
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
