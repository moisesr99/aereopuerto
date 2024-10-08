from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

from carro.carro import Carro
from pedidos.models import LineaPedido, Pedido

# Create your views here.
@login_required(login_url="/login/iniciar_sesion/")
def procesar_pedido(request):
    pedido=Pedido.objects.create(user=request.user)
    carro=Carro(request)
    lineas_pedido=list()
    for key,value in carro.carro.items(): #recorrer todos los productos
        lineas_pedido.append(LineaPedido(
            
            producto_id=key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido=pedido
            
        ))
    
    LineaPedido.objects.bulk_create(lineas_pedido)
    enviar_mail(pedido=pedido,
                lineas_pedido=lineas_pedido,
                nombreusuario=request.user.username,
                emailusuario=request.user.email
                )
    messages.success(request,"el pedido se ha creado correctamente")
    
    return render(request, "gracias.html")

def enviar_mail(**kwargs):
    asunto="PEDIDO REALIZADO, GRACIAS"
    mensaje=render_to_string("email/pedido.html",{
        "pedido":kwargs.get("pedido"),
        "lineas_pedido":kwargs.get("lineas_pedido"),
        "nombreusuario":kwargs.get("nombreusuario")
    })
    
    mensaje_texto=strip_tags(mensaje)
    from_email="moises.ramirezr@fgr.org.mx"
    to=kwargs.get("emailusuario")
    
    send_mail(asunto,mensaje_texto,from_email,[to],html_message=mensaje)
    
    


    