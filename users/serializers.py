from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from rest_framework import permissions, serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]

    class Meta:
        model = get_user_model()
        lookup_field = "uuid"
        extra_kwargs = {
            "url": {
                "lookup_field": "uuid",
            },
            'password': {'write_only': True},
            'id': {'read_only': True}
        }
        exclude = ['password', 'user_permissions']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        exclude = ['permissions']
