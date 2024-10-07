from django.contrib import admin
from tienda.models import Producto, CategoriaProd

# Register your models here.

class CategoriaProdAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    search_fields=("nomProduct","categorias","id","sku")
    list_filter=("categorias",)

admin.site.register(CategoriaProd, CategoriaProdAdmin)
admin.site.register(Producto, ProductoAdmin)
