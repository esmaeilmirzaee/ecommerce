from django.contrib import admin
from django.forms import forms
from . import models


class BlogForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        self.fields['title'].help_text = 'Enter a new title'

    class Meta:
        model = models.Blog
        exclude = ('slug',)


class BlogFormAdmin(admin.ModelAdmin):
    form = BlogForm()


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
admin.site.register(models.Blog, BlogFormAdmin)
admin.site.register(models.Category)
