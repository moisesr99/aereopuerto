from django.contrib import admin

from gestion_vuelos.models import cliente,vuelos,ticket
# Register your models here.

class clientesAdmin(admin.ModelAdmin):
    list_display=("nombre","email","telefono")
    search_fields=("nombre","telefono")
    
class filtroAdmin(admin.ModelAdmin):
    list_filter=("destino",)
    list_display=("destino","partida","fechaSAL","hora","precio")
    date_hierarchy="fechaSAL"
    
class ticketAdmin(admin.ModelAdmin):
    list_display=("numero","realizado","fecha_llegada")
    list_filter=("fecha_llegada",)
    date_hierarchy="fecha_llegada"
 
admin.site.register(cliente, clientesAdmin)
admin.site.register(vuelos,filtroAdmin)
admin.site.register(ticket,ticketAdmin)