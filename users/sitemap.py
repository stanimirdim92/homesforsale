from django.contrib.auth import get_user_model
from django.contrib.sitemaps import Sitemap


class UserSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return get_user_model().objects.all()

    def lastmod(self, obj):
        return obj.time_modified
