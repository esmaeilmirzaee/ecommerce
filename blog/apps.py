from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


# Altering admin
class BlogAdminConfig(AdminConfig):
    default_site = 'blog.admin.BlogAdmin'


class BlogConfig(AppConfig):
    name = 'blog'
