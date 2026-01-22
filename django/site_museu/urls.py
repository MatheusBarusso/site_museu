from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import index, history, contact, collection, events

urlpatterns = [
    path('', index, name='index'),
    path('sobre/', history, name='history'),
    path('contato/', contact, name='contact'),
    path('acervo/', collection, name='collection'),
    path('eventos/', events, name='events'),
    path('items/', include('item.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

