from django.urls import path

from . import views

app_name='item'

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
    path('eventos/<int:pk>/', views.event_detail, name = 'event_detail'),
]