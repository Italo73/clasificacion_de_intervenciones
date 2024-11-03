# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('reuniones.html', views.reuniones, name='reuniones'),
    path('nuevo_reporte.html', views.nuevo_reporte, name='nuevo_reporte'),
]