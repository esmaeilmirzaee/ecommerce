from django.contrib import admin
from . import models


class BlogAdminArea(admin.AdminSite):
    site_header = 'Blog admin area'


class BlogAdmin(admin.AdminSite):
    site_title = 'Manage blogs'


class BlogModel(admin.ModelAdmin):
    # fields = ['title', 'author', 'published_at']

    fieldsets = (
        ('Section 1',
         {
             'fields': ('title', 'content',),
             'description': 'Some helps'
         }),
        ('Section 2',
         {
             'fields': ('status',),
         })
    )


blog_admin = BlogAdmin()
admin.site.register(models.Blog, BlogModel)
admin.site.register(models.Category)
