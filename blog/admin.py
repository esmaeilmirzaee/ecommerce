from django.contrib import admin
from . import models


class BlogAdminArea(admin.AdminSite):
    site_header = 'Blog admin area'


class BlogAdmin(admin.AdminSite):
    site_title = 'Manage blogs'


blog_admin = BlogAdmin()
admin.site.register(models.Blog)
admin.site.register(models.Category)


# admin.site.unregister(django.contrib.sessions.models.Session)
