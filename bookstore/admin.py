from django.contrib import admin
from .models import Book, Profile


class BookstoreAdmin(admin.AdminSite):
    site_title = 'Bookstore admin page'


class EmailFilter(admin.SimpleListFilter):
    title = 'Email Filter'
    parameter_name = 'email'

    def lookups(self, request, model_admin):
        return (
            ('has_email', 'has_email'),
            ('no_email', 'no_email'),
        )

    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        if self.value().lower() == 'has_email':
            return queryset.exclude(user__email=None)
        if self.value().lower() == 'no_email':
            return queryset.filter(user__email='')


class Filter(admin.ModelAdmin):

    list_filter = ('is_active', 'role', 'created_at', EmailFilter, 'user__email')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        print(obj)
        # 33 is id of a user, and field inside Profile
        return obj is None or obj.pk != 33

    def has_delete_permission(self, request, obj=None):
        return False


bookstore_admin = BookstoreAdmin(name='Bookstore admin')
bookstore_admin.register(Book)
bookstore_admin.register(Profile, Filter)
