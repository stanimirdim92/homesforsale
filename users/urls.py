from django.template.defaulttags import url
from django.urls import include, path
from rest_framework_extensions import routers

from .views import UserViewSet, GroupViewSet


router = routers.ExtendedDefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'groups', GroupViewSet, basename='group')

urlpatterns = [
    path('', include(router.urls)),
]
