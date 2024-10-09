from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

# Create your models here.

class cliente (models.Model):
    nombre=models.CharField(max_length=12)  #heredar
    apellidos=models.CharField(max_length=20) #heredar
    email=models.EmailField()
    telefono=models.IntegerField()
    
    def __str__(self):
        return self.nombre
    
class vuelos (models.Model):
    destino=models.CharField(max_length=20) #heredar
    partida=models.CharField(max_length=20, verbose_name="origen") #heredar
    fechaSAL=models.DateField()
   # fechaREG=models.DateField(default='2024-01-01') #inncesario
    hora=models.TimeField()                 #heredar
    asientosDis=models.IntegerField()          
    precio = models.DecimalField(max_digits=10, decimal_places=2, help_text='Precio del producto')

    descuento = models.IntegerField(default=0, help_text='Descuento')

            
class ticket (models.Model):    #esta tabla heredara atributos de las tablas anteriorest
    numero=models.IntegerField()
    realizado=models.BooleanField(default='False')
    fecha_llegada=models.DateField(default='2024-01-01')
    nombre=cliente.nombre
   
    
    def __str__(self):
        return 'ticket numero %s' %(self.numero)
    