from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from gestion_vuelos.models import vuelos
from django.contrib import messages
from datetime import date, datetime


from gestion_vuelos.forms import FormularioContacto



def busqueda_vuelos(request):
    return render(request, "busqueda_vuelos.html")

def buscar(request):
    if request.GET.get("vlPart") and request.GET.get("vlDest") and request.GET.get("vlSalida"):
        vueloPartida = request.GET.get("vlPart")
        vueloDestino = request.GET.get("vlDest")
        VueloFechaSal_str = request.GET.get("vlSalida")
        VueloFechaReg_str = request.GET.get("vlRegreso")
        
        VueloFechaSal = datetime.strptime(VueloFechaSal_str, '%Y-%m-%d').date() if VueloFechaSal_str else None


        if len(vueloPartida) > 20 or len(vueloDestino) > 20:
            messages.error(request, "Texto de búsqueda demasiado largo")
            return redirect('busqueda_vuelos')  # Redirige a la página de Inicio
        
        elif vueloPartida == vueloDestino:
                messages.error(request, "El Origen y el destino no pueden ser el mismo")
                return redirect('busqueda_vuelos')  # Redirige a la página  Inicio
        
        elif request.GET.get("vlRegreso") :
            VueloFechaReg = datetime.strptime(VueloFechaReg_str, '%Y-%m-%d').date()if VueloFechaReg_str else None

            if VueloFechaSal >= VueloFechaReg:
                messages.error(request, "La fecha de Retorno no puede ser anterior o igual a la fecha de salida")
                return redirect('busqueda_vuelos')  # Redirige a la página de 
        
            else:
                vuelo_busc = vuelos.objects.filter(partida__icontains=vueloPartida, destino__icontains=vueloDestino, fechaSAL__icontains=VueloFechaSal )#, fechaREG__icontains=VueloFechaReg)
                vuelo_regreso = vuelos.objects.filter(partida__icontains=vueloDestino, destino__icontains=vueloPartida, fechaSAL__icontains=VueloFechaReg)
                return render(request, "resultados_busqueda.html", {"vuelos": vuelo_busc, "vuelos_regreso": vuelo_regreso, "query": vueloPartida, "query2": vueloDestino, "fecha1": VueloFechaSal, "fecha2": VueloFechaReg})                
        
        elif VueloFechaSal < date.today():
            messages.error(request, "La fecha de Salida no puede ser anterior al dia actual: ")
            return redirect('busqueda_vuelos')  # Redirige a la página de 
                
            

        else:
            vuelo_busc = vuelos.objects.filter(partida__icontains=vueloPartida, destino__icontains=vueloDestino, fechaSAL__icontains=VueloFechaSal)
            return render(request, "resultados_busqueda.html", {"vuelos": vuelo_busc, "query": vueloPartida, "query2": vueloDestino,"query3":VueloFechaSal})

    else:
        messages.error(request, "No has introducido nada")
        return redirect('busqueda_vuelos')  # Redirige a la página de búsqueda
    
    
