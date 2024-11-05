from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from carro.carro import Carro

# Create your views here.
def home(request):
    carro=Carro(request)
    
    return render(request, "inicio.html")

#validacion manual del formulario contacto
def contactar (request):
    if request.method=="POST":
        subject=request.POST["asunto"]
        message=request.POST["mensaje"]+" "+request.POST["email"]
        email_from=settings.EMAIL_HOST_USER
        recipient_list=["moises.rojasr99@gmail.com"]
        
        if subject and message and email_from:
            send_mail(subject, message, email_from, recipient_list)
            return render(request,"gracias.html")
        else:
            messages.error(request, "No has introducido nada")
            return render(request, "contacto.html")
            
    return render(request, "contacto.html")

#validacion usando formularios django
#def contactar (request):
#    if request.method=="POST":
#        miFormulario=FormularioContacto(request.POST)
#        
#        if miFormulario.is_valid():
#            infForm=miFormulario.cleaned_data
#            
#            send_mail(
#                infForm['asunto'],
#                infForm['mensaje'],
#                settings.EMAIL_HOST_USER,  # Usa la dirección de correo autenticada
#                # infForm.get('email',''), #error
#                ['moises.rojasr99@gmail.com'],
#                fail_silently=False)
#            return render(request,"gracias.html")
            #return redirect("/contacto/?valido")
#    else:
#        miFormulario=FormularioContacto()
#    
#    return render(request,"formulario_contacto.html",{"form":miFormulario})
