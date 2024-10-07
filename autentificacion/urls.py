from django.urls import path
from .views import Vregistro  # Si cerrar_sesion está en views de autentificacion, no necesitas importarla aquí
from autentificacion import views

app_name = 'autentificacion'  # Define el namespace

urlpatterns = [
    path("", Vregistro.as_view(), name="autentificar"),
    path("cerrar_sesion/", views.cerrar_sesion, name="cerrar_sesion"),  # Referencia la vista desde views
    path("iniciar_sesion/", views.iniciar_sesion, name="iniciar_sesion"),
]
