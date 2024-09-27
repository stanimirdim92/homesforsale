import os

from django.db.backends.postgresql.psycopg_any import IsolationLevel
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


# MIGRATIONS

# https://docs.djangoproject.com/en/dev/ref/settings/#migration-modules
MIGRATION_MODULES = {"users": "users.migrations"}
