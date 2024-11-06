from django.urls import path, reverse_lazy
from .views import Vregistro  # Importa la vista de registro
from autentificacion import views  # Importa las vistas adicionales del módulo autentificación
from django.contrib.auth import views as auth_views  # Importa las vistas de autenticación de Django

app_name = 'autentificacion'  # Define el namespace para las URLs

urlpatterns = [
    path("", Vregistro.as_view(), name="autentificar"),  # Ruta para la vista de registro
    path("cerrar_sesion/", views.cerrar_sesion, name="cerrar_sesion"),  # Ruta para cerrar sesión
    path("iniciar_sesion/", views.iniciar_sesion, name="iniciar_sesion"),  # Ruta para iniciar sesión
   
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='auth/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]

#funciona el reseteo de contraseña pero en el navegador arroja que no se encontro la url
 
 # URL para la vista de solicitud de restablecimiento de contraseña
 #   path('password_reset/', auth_views.PasswordResetView.as_view(
 #       template_name='auth/password_reset_form.html',
 #       email_template_name='auth/password_reset_email.html',
 #       success_url= reverse_lazy('password_reset/done/')  # para no duplicar la url en el navegador, sigue en error
 #   ), name='password_reset'),

    # URL para la confirmación de envío de correo de recuperación
 #   path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
 #       template_name='auth/password_reset_done.html'
 #   ), name='password_reset_done'),

    # URL para confirmar el restablecimiento de contraseña con token
 #   path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
 #       template_name='auth/password_reset_confirm.html'
 #   ), name='password_reset_confirm'),

    # URL para la confirmación final de restablecimiento de contraseña
 #   path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
 #       template_name='auth/password_reset_complete.html'
 #   ), name='password_reset_complete'),
