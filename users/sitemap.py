from django.contrib.auth import get_user_model
from django.contrib.sitemaps import Sitemap
User = get_user_model()


class UserSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return User.objects.all()

    def lastmod(self, obj):
        return obj.time_modified
