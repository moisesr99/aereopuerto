"""aereopuerto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inicio.urls')), #links para app principal
    path('vuelos/', include('gestion_vuelos.urls')), #linkear urls de la app gestion_vuelos
    path('hoteles/',include('hoteleria.urls')), #segunda app hoteleria
    path('blog/',include('blog.urls')), #tercera app blog
    path('tienda/',include('tienda.urls')), #cuarta app tienda
    path('carro/',include('carro.urls')), #app carro
    path('login/',include('autentificacion.urls')), #app para logear
  
    ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  