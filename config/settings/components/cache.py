# https://docs.djangoproject.com/en/stable/topics/cache/#redis
import os

from config.settings.production import get_list

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
