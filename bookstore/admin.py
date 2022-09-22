from django.contrib import admin
from .models import Book


class BookstoreAdmin(admin.AdminSite):
    site_title = 'Bookstore admin page'


bookstore_admin = BookstoreAdmin(name='Bookstore admin')
bookstore_admin.register(Book)
