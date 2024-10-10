from django.shortcuts import render, redirect

from carro.ticket import Ticket
from gestion_vuelos.models import vuelos
from .carro import Carro
from tienda.models import Producto


# Create your views here.
## funciones para la app tienda
def agregar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect("tienda")

def eliminar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect("tienda")

def restar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect("tienda")

def limpiar_carro(request, producto_id):
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

