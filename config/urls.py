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
from django.urls import include, path, re_path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerSplitView

from users.views import FacebookLogin, GoogleLogin

version = os.getenv('APP_VERSION', '1.0.0')

urlpatterns = [
    # DRF URLS
    # path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path("api/auth/token/", obtain_auth_token),

    # UI Language translation
    re_path(r'^rosetta/', include('rosetta.urls')),

    path('api/schema/', SpectacularAPIView.as_view(api_version=version), name='schema'),
    path('api/schema/swagger/', SpectacularSwaggerSplitView.as_view(url_name='schema'), name='swagger'),

    path(settings.ADMIN_URL, admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),

    # APP URLS
    path('', include('users.urls')),

    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/auth/facebook/', FacebookLogin.as_view(), name='login_facebook'),
    path('api/auth/google/', GoogleLogin.as_view(), name='login_google'),

    # Media files
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]

# urlpatterns += i18n_patterns()


if settings.DEBUG:
    # Static file serving when using Gunicorn + Uvicorn for local web socket development
    urlpatterns += staticfiles_urlpatterns()
    if "debug_toolbar" in settings.INSTALLED_APPS:
        urlpatterns += [path('debug/', include('debug_toolbar.urls'))]
