from django.urls import include, path
from rest_framework_extensions import routers

from .views import AddressViewSet, GroupViewSet, UserViewSet

router = routers.ExtendedDefaultRouter()
router.register(r'api/v1/addresses', AddressViewSet)
router.register(r'api/v1/users', UserViewSet)
router.register(r'api/v1/groups', GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
