from django.urls import path
from pedidos import views

urlpatterns = [
    path('', views.procesar_pedido,name="pedidos"),
    path('vuelos/',views.procesar_vuelo,name='procesar_vuelo'),
    
    
]