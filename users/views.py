from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from users.models import Address
from users.serializers import UserSerializer, GroupSerializer, AddressSerializer

User = get_user_model()


@extend_schema(tags=['Users'])
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.prefetch_related('addresses')
    serializer_class = UserSerializer
    lookup_field = "uuid"

    @action(detail=True)
    def me(self, request):
        serializer = UserSerializer(request.user,context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


@extend_schema(tags=['Address'])
class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    lookup_field = "id"



@extend_schema(tags=['Groups'])
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
