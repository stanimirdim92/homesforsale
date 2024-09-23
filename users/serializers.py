from django.contrib.admin.utils import lookup_field
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import permissions, serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import SerializerMethodField
from rest_framework.utils.serializer_helpers import ReturnDict

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

    def get_addresses(self, obj) -> ReturnDict | None:  # Check if the request has a query param `include_addresses=true`
        request = self.context.get('request', None)
        if request is None:
            raise ValidationError("Request context is missing.")

        include_addresses = request.query_params.get('include')
        if include_addresses and 'address' in include_addresses.split(','):
            return AddressSerializer(Address.objects.filter(user_id=obj), context={'request': request}, many=True).data

        return None

    addresses = serializers.SerializerMethodField(source="get_addresses", read_only=True, required=False)
    exclude = ['password', 'user_permissions', 'id']
    class Meta:
        model = User
        # fields = [
        #     'addresses',
        #     'uuid', 'is_active',
        #     'title', 'name_first', 'name_middle', 'name_last', 'company_name',
        #     'entity_type', 'phone_number', 'timezone',  'language', 'currency',
        #     'time_created', 'time_modified', 'time_deleted',
        # ]
        lookup_field = "uuid"
        extra_kwargs = {
            'password': {'write_only': True},
            'id': {'read_only': True},
            'uuid': {'read_only': True},
            'time_created': {'read_only': True},
            'time_modified': {'read_only': True},
        }
        exclude = ['password', 'user_permissions', 'id']


class GroupSerializer(serializers.HyperlinkedModelSerializer[Group]):
    class Meta:
        model = Group
        exclude = ['permissions']
