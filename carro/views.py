from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from carro.ticket import Ticket
from gestion_vuelos.models import vuelos
from .carro import Carro
from django.views import View
from tienda.models import Producto


# Create your views here.
## funciones para la app tienda
class agregar_producto(View):
    def post(self, request, producto_id):
        carro=Carro(request)
        producto=get_object_or_404(Producto, id=producto_id) # Obtiene el producto o lanza un error 404 si no existe.
        
        cantidad_disponible = producto.stock
        cantidad_en_carro = carro.obtener_cantidad(producto)
        
        if cantidad_en_carro < cantidad_disponible:
            carro.agregar(producto=producto)
            messages.success(request, f'Producto {producto.nomProduct} agregado al carrito')
        else:
            messages.error(request, f'lo sentimos, no hay suficiente cantidad disponible')
            
        return redirect("tienda")

class eliminar_producto(View):
    def post(self,request, producto_id):
        carro=Carro(request)
        producto=Producto.objects.get(id=producto_id)
        carro.eliminar(producto=producto)
        return redirect("tienda")

class restar_producto(View):
    def post(self,request, producto_id):
        carro=Carro(request)
        producto=Producto.objects.get(id=producto_id)
        carro.restar_producto(producto)
        return redirect("tienda")


class limpiar_carro(View):
    def post(self,request):
        carro=Carro(request)
        carro.vaciar_carro()
        return redirect("tienda")

## funciones ára la app gestion_vuelos

def agregar_vuelo(request, vuelo_id):
    ticket=Ticket(request)
    vuelo=vuelos.objects.get(id=vuelo_id)
    ticket.comprar(vuelo=vuelo)
    return redirect("buscar")

def eliminar_vuelo(request, vuelo_id):
    ticket=Ticket(request)
    vuelo=vuelos.objects.get(id=vuelo_id)
    ticket.comprar(vuelo=vuelo)
    return redirect("buscar")

def agregar_vuelo(request, vuelo_id):
    ticket=Ticket(request)
    vuelo=vuelos.objects.get(id=vuelo_id)
    ticket.comprar(vuelo=vuelo)
    return redirect("buscar")

