from django.contrib.auth.models import Group
from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['url','name_last', 'email', 'groups', 'name_last', 'reference', 'uuid']
        extra_kwargs = {
            "url": {"lookup_field": "pk"},
        }


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
