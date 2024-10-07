from django.urls import path
from blog import views

urlpatterns = [
    path('', views.crear_post,name="crear_post"),
    path('publicar/',views.publicar,name="publicar"),
    path('categoria/<int:categoria_id>/',views.categoria_view, name="categoria"),
    
]
