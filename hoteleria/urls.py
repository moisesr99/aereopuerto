from django.urls import path
from hoteleria import views


urlpatterns = [
    path('', views.busqueda_hoteles,name="busqueda_hoteles"),
    path('buscarH/',views.buscarH,name="buscarH"),
]

