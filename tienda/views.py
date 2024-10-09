from django.shortcuts import render
from tienda.models import Producto, CategoriaProd
from django.contrib.auth import get_user_model

# Create your views here.
User = get_user_model()

def tienda(request):
    productos=Producto.objects.all()
    
    return render(request,"tienda.html",{"productos":productos})




#def categoria_view(request,categoria_id):
#    filtro_categoria = CategoriaProd.objects.get(id=categoria_id)
#    prd=Producto.objects.filter(categorias=filtro_categoria)
#    return render(request,"categoria_tienda.html",{"categoria":filtro_categoria,"productos":prd})