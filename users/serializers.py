from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        lookup_field = "uuid"
        extra_kwargs = {
            "url": {
                "lookup_field": "uuid",
            },
            'password': {'write_only': True, 'min_length': 9}
        }
        exclude = ["password", 'user_permissions']
