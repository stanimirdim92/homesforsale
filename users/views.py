from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from users.models import Address
from users.serializers import UserSerializer, GroupSerializer, AddressSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "uuid"

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user,context={"request": request}, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    lookup_field = "id"

class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
