from django.db import models

# Create your models here.

class Hoteles(models.Model):  # Renombrar la clase para seguir la convención de nombres en mayúsculas
    id = models.BigAutoField(primary_key=True)
    nombreHotel = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='hoteles')
    habitaciones = models.IntegerField()
    habitacionesDIS = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)
    calle = models.CharField(max_length=30)
    pais = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=20)
    
    
    
    def __str__(self):
        return self.nombreHotel


class Cliente(models.Model):  # Renombrar la clase para seguir la convención de nombres en mayúsculas
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    estatus = models.BooleanField()
    
    def __str__(self):
        return self.nombre


class Reservacion(models.Model):  # Renombrar la clase para seguir la convención de nombres en mayúsculas
    id = models.BigAutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hoteles, on_delete=models.CASCADE)  # Agregar relación con hotel
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    numero_habitacion = models.IntegerField()  # Corrección de error tipográfico
    
    def __str__(self):
        return f'reservacion a nombre de {self.cliente} en el hotel {self.hotel.nombreHotel}'
