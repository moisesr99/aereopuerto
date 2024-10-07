
from django.urls import path
from gestion_vuelos import views


urlpatterns = [
    path('', views.busqueda_vuelos,name="busqueda_vuelos"),
    path('buscar/',views.buscar,name="buscar"),
]