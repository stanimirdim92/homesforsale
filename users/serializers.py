from django.contrib.auth.models import Group
from rest_framework import serializers
from django.contrib.auth import get_user_model


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


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        exclude = ['permissions']
