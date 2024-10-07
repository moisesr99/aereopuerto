from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from hoteleria.models import Hoteles
from django.contrib import messages
from datetime import date, datetime
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

def busqueda_hoteles(request):
    return render(request, "hotel.html")

def buscarH(request):
    
    if request.GET.get("HT_dest") and request.GET.get("HT_entrada") and request.GET.get("HT_salida") and request.GET.get("adultos"):
        Hotel_Destino = request.GET.get("HT_dest")
        Hotel_Habitaciones = request.GET.get("adultos")
        Hotel_FechaEnt_str = request.GET.get("HT_entrada")
        Hotel_FechaSal_str = request.GET.get("HT_salida")
        
        Hotel_FechaEnt = datetime.strptime(Hotel_FechaEnt_str, '%Y-%m-%d').date() if Hotel_FechaEnt_str else None
        Hotel_FechaSal = datetime.strptime(Hotel_FechaSal_str, '%Y-%m-%d').date() if Hotel_FechaSal_str else None
        
        if len(Hotel_Destino) > 25 :
            messages.error(request, 'Texto de busqueda "Destino" demadiaso largo')
            return redirect('busqueda_hoteles')
        
        elif Hotel_FechaEnt>= Hotel_FechaSal:
            messages.error(request, "La fecha de salida no puede ser anterior o igual a la fecha de salida")
            return redirect('busqueda_hoteles')  # Redirige a la página de busqueda
            
        elif Hotel_FechaEnt < date.today():
            messages.error(request, "La fecha de 'ENTRADA' no puede ser anterior al dia actual: ")
            return redirect('busqueda_hoteles')  # Redirige a la página de busqueda
        
        else:
            hotel_busc = Hoteles.objects.filter(ciudad__icontains=Hotel_Destino, habitacionesDIS__gt=Hotel_Habitaciones )#, fechaREG__icontains=VueloFechaReg)
            return render(request, "resultados_busqueda_hoteles.html", {"hoteles": hotel_busc, "query": Hotel_Destino, "personas": Hotel_Habitaciones })                
    
    else:
        #print("prueba") 
        messages.error(request, "No has introducido nada")
        return redirect('busqueda_hoteles')  # Redirige a la página de búsqueda