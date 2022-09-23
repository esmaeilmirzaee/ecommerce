from django.contrib import admin
from .models import Book, Profile


class BookstoreAdmin(admin.AdminSite):
    site_title = 'Bookstore admin page'


class Filter(admin.ModelAdmin):
    list_display = ('id', 'email', 'created_at', 'role', 'is_active',)
    list_filter = ('is_active', 'role', 'created_at',)


class EmailFilter(admin.SimpleListFilter):
    title = ''
    parameter_name = ''

    def lookups(self, request, model_admin):
        return

    def queryset(self, request, queryset):
        return


bookstore_admin = BookstoreAdmin(name='Bookstore admin')
bookstore_admin.register(Book)
bookstore_admin.register(Profile, Filter)
