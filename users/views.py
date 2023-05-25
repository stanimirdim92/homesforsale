from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response

from users.serializers import UserSerializer, GroupSerializer
from rest_framework.decorators import action
from rest_framework.views import APIView


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = get_user_model().objects.all().order_by('-time_created')
    serializer_class = UserSerializer
    lookup_field = "uuid"

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
