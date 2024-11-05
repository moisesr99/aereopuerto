from http.client import HTTPResponse
from django.shortcuts import render, get_object_or_404
from aereopuerto import settings
from pedidos.models import Pedido
from tienda.models import Producto, CategoriaProd
from django.contrib.auth import get_user_model
from django.views import View

# Create your views here.
User = get_user_model()

def tienda(request):
    productos=Producto.objects.all()
    categorias = CategoriaProd.objects.all()
    
    return render(request,"tienda.html",{"productos":productos,"categorias":categorias})


class ConfirmacionPedidoView(View):
    def get(self, request, pedido_id):
        pedido = get_object_or_404(Pedido, id=pedido_id, user=request.user)
        lineas_pedido = pedido.lineapedido_set.all()
        total_pedido = sum(linea.total_pedido for linea in lineas_pedido)
        context = {
            'pedido': pedido,
            'lineas_pedido': lineas_pedido,
            'total_pedido': total_pedido,
            
        }
        return render(request, 'confirmacion_pedido.html', context)

# Definimos la clase vista tiendaCategoria
class tiendaCategoria(View):
    def get(self, request, categoria_id=None):
        try:
            # Obtenemos el parámetro de consulta 'q' de la URL
            query = request.GET.get('q', '')
            
            # Obtenemos todas las categorías y productos
            categorias = CategoriaProd.objects.all()
            productos = Producto.objects.all()

            # Filtramos los productos por categoría si se proporciona categoria_id
            if categoria_id:
                categoria = get_object_or_404(CategoriaProd, id=categoria_id)
                productos = productos.filter(categorias=categoria)
            else:
                categoria = None

            # Filtramos los productos por el término de búsqueda si se proporciona una consulta
            if query:
                productos = productos.filter(nomProduct__icontains=query)

            # Calculamos el precio con descuento para cada producto
           #se movio directamente al models 

            # Creamos el contexto con las categorías, productos y otros datos
            context = {
                'categoria': categoria,
                'productos': productos,
                'categorias': categorias,
                'query': query,
                'MEDIA_URL': settings.MEDIA_URL,
            }
            
            # Renderizamos la plantilla HTML con el contexto
            return render(request, "tienda_categoria.html", context)

        except Exception as e:
            # Si ocurre un error, devolvemos una respuesta con el estado 500 y el mensaje de error
            return HTTPResponse(status=500, content=str(e))

#def categoria_view(request,categoria_id):
#    filtro_categoria = CategoriaProd.objects.get(id=categoria_id)
#    prd=Producto.objects.filter(categorias=filtro_categoria)
#    return render(request,"categoria_tienda.html",{"categoria":filtro_categoria,"productos":prd})