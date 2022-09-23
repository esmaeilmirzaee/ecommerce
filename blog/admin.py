from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from django.forms import forms
from . import models


class BlogAdminArea(admin.AdminSite):
    site_title = 'Blog Admin'
    site_header = 'Blog Admin Area'
    login_template = 'blog/admin/login.html'


blog_admin = BlogAdminArea(name='Blog Admin')


class SummerAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


blog_admin.register(models.Blog, SummerAdmin)
