import os
from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model

User = get_user_model()

def upload_to(instance, filename):
    return os.path.join('tienda', datetime.now().strftime('%Y/%m/%d'), filename)

# Create your models here.
class CategoriaProd(models.Model):
    nombreCatProd = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Categoría de Producto"
        verbose_name_plural = "Categorías de Productos"
    
    def __str__(self):
        return self.nombreCatProd

class Producto(models.Model):
    nomProduct = models.CharField(max_length=100, help_text='Nombre del producto')
    categorias = models.ForeignKey(CategoriaProd, on_delete=models.CASCADE, null=False, blank=False, default=1)
    precio = models.DecimalField(max_digits=10, decimal_places=2, help_text='Precio del producto')
    imagen = models.ImageField(upload_to=upload_to, null=True, blank=True, help_text='Imagen del producto frontal')
    ventas_totales = models.IntegerField(default=0)
    descuento = models.IntegerField(default=0, help_text='Descuento')
    stock = models.IntegerField(default=0, help_text='Cantidad disponible en stock')
    sku = models.CharField(max_length=20, help_text='Número único del producto')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    @property
    def precio_final(self):
        # Calcula el precio final aplicando el descuento solo si existe un descuento
        if self.descuento > 0:
            return self.precio - (self.precio * self.descuento / 100)
        return self.precio #no remplazar el precio sin descuento
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
    
    def __str__(self):
        return self.nomProduct
    

class ReporteVentas(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    total_venta = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Reporte de Ventas"
        verbose_name_plural = "Reportes de Ventas"

    def __str__(self):
        return f"{self.producto.nomProduct} vendido por {self.usuario.username}"