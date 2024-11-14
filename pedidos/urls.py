from django.urls import path
from pedidos import views
from .views import generar_pdf_pedido

urlpatterns = [
    path('', views.procesar_pedido,name="pedidos"),
    path('vuelos/',views.procesar_vuelo,name='procesar_vuelo'),
     path('generar_pdf_pedido/<int:pedido_id>/', views.generar_pdf_pedido, name='generar_pdf_pedido'),
     path('generar_excel_pedido/<int:pedido_id>/',views.generar_excel_pedido,name='generar_excel_pedido'),
    #path('reporte/<int:pedido_id>/', generar_pdf_pedido, name='generar_pdf_pedido'),
    
    
]