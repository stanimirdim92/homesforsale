from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from rest_framework import permissions, serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.utils.serializer_helpers import ReturnDict

from users.models import Address

User = get_user_model()


class AddressSerializer(serializers.ModelSerializer[Address]):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]

    class Meta:
        model = Address
        lookup_field = "id"
        fields = '__all__'
        extra_kwargs = {
            "url": {
                "lookup_field": "id",
            },
            'id': {'read_only': True}
        }


class UserSerializer(serializers.HyperlinkedModelSerializer[User]):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    addresses = serializers.SerializerMethodField(source="get_addresses")

    def get_addresses(self, obj) -> ReturnDict | None:        # Check if the request has a query param `include_addresses=true`
        request = self.context.get('request', None)
        if request and request.query_params.get('include'):
            if 'address' in request.query_params['include'].split(','):
                # Return serialized addresses if the query param is true
                return AddressSerializer(Address.objects.filter(user_id=obj), many=True, read_only=True, required=False).data

        # Otherwise, return None or an empty list (depends on your preference)
        return None

    class Meta:
        model = User
        fields = [
            'addresses',
            'uuid', 'is_active',
            'title', 'name_first', 'name_middle', 'name_last', 'company_name',
            'entity_type', 'phone_number', 'timezone',  'language', 'currency',
            'time_created', 'time_modified', 'time_deleted',
        ]
        lookup_field = "uuid"
        extra_kwargs = {
            "url": {
                "lookup_field": "uuid",
                'addresses': {'lookup_field': 'user'}
            },
            'password': {'write_only': True},
            'id': {'read_only': True}
        }
        # exclude = ['password', 'user_permissions']


class GroupSerializer(serializers.HyperlinkedModelSerializer[Group]):
    class Meta:
        model = Group
        exclude = ['permissions']
