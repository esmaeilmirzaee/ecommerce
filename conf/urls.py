from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from bookstore.admin import bookstore_admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookstore/', bookstore_admin.urls),
    path('editor', include('django_summernote.urls')),
]

admin.site.index_title = 'BookStore'
admin.site.site_header = 'ECommerce App'
admin.site.site_title = 'Site title ecommerce'


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
