# ruff: noqa

"""hfs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""
import os

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerSplitView
from allauth.account.decorators import secure_admin_login

admin.autodiscover()
admin.site.login = secure_admin_login(admin.site.login)

version = os.getenv('APP_VERSION', '1.0.0')

urlpatterns = [
    # DRF URLS
    # path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path("api/auth/token/", obtain_auth_token),

    # UI Language translation
    path('rosetta/', include('rosetta.urls')),

    path('api/schema/', SpectacularAPIView.as_view(api_version=version), name='schema'),
    path('api/schema/swagger/', SpectacularSwaggerSplitView.as_view(url_name='schema'), name='swagger'),

    path(settings.ADMIN_URL, admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),

    # APP URLS
    path('', include('users.urls')),

    # 3rd PARTY URLS
    path('accounts/', include('allauth.urls')),
    path("_accounts/", include("allauth.headless.urls")),

]
# urlpatterns += i18n_patterns()


urlpatterns += (static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    if "debug_toolbar" in settings.INSTALLED_APPS:
        urlpatterns += [path('debug/', include('debug_toolbar.urls'))]
