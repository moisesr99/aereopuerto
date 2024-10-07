
from django.urls import path
from inicio import views


urlpatterns = [
    path('', views.home,name="home"),#pagina de inicio
    path('contactanos/',views.contactar,name="contactanos"), #path('url',view.nombre de la vista,name='nombre para el httpresponsive' )
]