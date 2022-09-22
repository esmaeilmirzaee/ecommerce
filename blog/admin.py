from django.contrib import admin
from . import models


class BlogAdmin(admin.AdminSite):
    site_title = 'Manage blogs'


blog_admin = BlogAdmin()
blog_admin.register(models.Post)
