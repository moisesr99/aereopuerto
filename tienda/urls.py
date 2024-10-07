from django.urls import path
from tienda import views

urlpatterns = [
    path('', views.tienda,name="tienda"),
    path('categoria/<int:categoria_id>/',views.categoria_view, name="categoria"),
    
]