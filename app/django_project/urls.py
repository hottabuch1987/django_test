from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from .yasg import urlpatterns as doc_urls
from rest_framework import schemas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    path('openapi/', schemas.get_schema_view(
        title="Your API",
        description="API for Your Project",
        version="1.0.0"
    ), name='openapi-schema'),

]

urlpatterns += doc_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
