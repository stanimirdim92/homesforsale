from django.template.defaulttags import url
from django.urls import include, path
from rest_framework_extensions import routers

from .views import UserViewSet


router = routers.ExtendedDefaultRouter()
router.register(r'api/v1/users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
