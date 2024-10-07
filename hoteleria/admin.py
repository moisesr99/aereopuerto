from django.contrib import admin
from hoteleria.models import Hoteles

# Register your models here.
class hoteladmin(admin.ModelAdmin):
    readonly_fields=('created','update')
    list_display=("id","nombreHotel","habitacionesDIS","estado","pais")
    search_fields=("nombre","estado","id")
    list_filter=("estado","pais","ciudad")

admin.site.register(Hoteles, hoteladmin)