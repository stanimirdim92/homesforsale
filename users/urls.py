from django.urls import include, path
from rest_framework_extensions import routers

from .views import UserViewSet, GroupViewSet, AddressViewSet

router = routers.ExtendedDefaultRouter()
router.register(r'api/v1/users', UserViewSet, basename='user')
router.register(r'api/v1/addresses', AddressViewSet, basename='addresses')
router.register(r'api/v1/groups', GroupViewSet, basename='group')

urlpatterns = [
    path('', include(router.urls)),
]
