from django.contrib import admin
from django.forms import forms
from . import models


class BlogAdminConf(admin.AdminSite):
    site_title = 'Blog Admin'
    site_header = 'Blog Admin Area'
    login_template = 'blog/admin/login.html'


blog_admin = BlogAdminConf(name='Blog Admin')
