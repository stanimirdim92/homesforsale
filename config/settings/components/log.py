import logging

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
                "[%(asctime)s] %(levelname)s %(name)s %(message)s "
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
