from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
]

admin.site.index_title = 'BookStore'
admin.site.site_header = 'ECommerce App'
admin.site.site_title = 'Site title ecommerce'
