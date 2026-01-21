from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import index, history, contact, collection

urlpatterns = [
    path('', index, name='index'),
    path('history/', history, name='history'),
    path('contact/', contact, name='contact'),
    path('collection/', collection, name='collection'),
    path('items/', include('item.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

