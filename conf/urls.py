from django.contrib import admin
from django.urls import path
from blog.admin import blog_admin
from bookstore.admin import bookstore_admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogadmin/', blog_admin.urls),
    path('bookstoreadmin/', bookstore_admin.urls),
]

admin.site.index_title = 'BookStore'
admin.site.site_header = 'ECommerce App'
admin.site.site_title = 'Site title ecommerce'
