from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from blog.admin import blog_admin

urlpatterns = [
    path('admin/', blog_admin.urls),
]

admin.site.index_title = 'BookStore'
admin.site.site_header = 'ECommerce App'
admin.site.site_title = 'Site title ecommerce'


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
