from django.contrib import admin
from pedidos.models import Pedido, LineaPedido

# Register your models here.

class fechasPedidos(admin.ModelAdmin):
    readonly_fields=('create_at', 'update')

    
class PedidosAdmin(admin.ModelAdmin):
    readonly_fields=('create_at', 'update')
    search_fields=("id","usuario_id")
    list_filter=("id",)
    
admin.site.register(Pedido ,fechasPedidos)
admin.site.register(LineaPedido, PedidosAdmin)