from django.urls import path
from .views import agregar_producto, eliminar_producto, limpiar_carro, restar_producto


app_name = 'carro'  # Define el namespace

urlpatterns = [
    path("agregar/<int:producto_id>/", agregar_producto.as_view(), name="agregar"),
    path("eliminar/<int:producto_id>/",eliminar_producto.as_view(), name="eliminar"),
    path("restar/<int:producto_id>/",restar_producto.as_view(), name="restar"),
    path("limpiar/",limpiar_carro.as_view(), name="vaciar"),
]
