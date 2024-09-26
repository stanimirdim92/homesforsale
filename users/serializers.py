from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import serializers

from users.models import Address

User = get_user_model()


class AddressSerializer(serializers.ModelSerializer[Address]):
    class Meta:
        model = Address
        lookup_field = "id"
        fields = ['id', 'address_line_1', 'address_line_2', 'city', 'state', 'postal_code', 'country']
        extra_kwargs = {
            "url": {
                "lookup_field": "id",
            },
            'id': {'read_only': True},
        }


class UserSerializer(serializers.ModelSerializer[User]):
    addresses = AddressSerializer(many=True, read_only=True, required=False)
    exclude = ['password', 'user_permissions', 'id']

    class Meta:
        model = User
        fields = [
            'addresses', 'groups',
            'uuid', 'is_active', 'email',
            'title', 'name_first', 'name_middle', 'name_last', 'company_name',
            'entity_type', 'phone_number', 'timezone', 'language', 'currency',
            'time_created', 'time_modified', 'time_deleted',
        ]
        lookup_field = "uuid"
        extra_kwargs = {
            'password': {'write_only': True},
            'id': {'read_only': True},
            'uuid': {'read_only': True},
            'time_created': {'read_only': True},
            'time_modified': {'read_only': True},
        }
        # exclude = ['password', 'user_permissions', 'id']


class GroupSerializer(serializers.HyperlinkedModelSerializer[Group]):
    class Meta:
        model = Group
        exclude = ['permissions']
