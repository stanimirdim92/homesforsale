# ruff: noqa

"""hfs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os

from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path, re_path
from django.views import defaults as default_views
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
    re_path(r'^rosetta/', include('rosetta.urls')),

    path('api/schema/', SpectacularAPIView.as_view(api_version=version), name='schema'),
    path('api/schema/swagger/', SpectacularSwaggerSplitView.as_view(url_name='schema'), name='swagger'),

    path(settings.ADMIN_URL, admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),

    # 3rd PARTY URLS
    path('o/', include('oauth2_provider.urls')),

    # APP URLS
    path('', include('users.urls')),

    # 3rd PARTY URLS
    path('accounts/', include('allauth.urls')),
    path("_allauth/", include("allauth.headless.urls")),

    # Media files
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]

# urlpatterns += i18n_patterns()


if settings.DEBUG:
    # Static file serving when using Gunicorn + Uvicorn for local web socket development
    urlpatterns += staticfiles_urlpatterns()

    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        urlpatterns += i18n_patterns(
            path('debug/', include('debug_toolbar.urls')),
            prefix_default_language=True
        )
