from django.shortcuts import redirect
from tienda.models import Producto
from decimal import Decimal, ROUND_HALF_UP
from decimal import Decimal

class Carro:
    def __init__(self,request):
        self.request=request
        self.session=request.session
        carro=self.session.get("carro")
        if not carro:
           carro=self.session["carro"]={}
           
        self.carro=carro
            
    def agregar(self, producto):
        if(str(producto.id) not in self.carro.keys()):
            self.carro[producto.id]={
            "producto_id":producto.id,
            "nombre":producto.nomProduct,
            "precio":str(producto.precio),
            "cantidad":1,
            "imagen":producto.imagen.url,
            "descuento":producto.descuento,
            "precio_final": str(producto.precio - (producto.precio * producto.descuento / 100)),
            "stock":producto.stock,
            }
        else:
             # Si el producto ya está en el carrito, se actualiza la cantidad y el precio
            for key, value in self.carro.items():
                if key == str(producto.id):
                    # Se incrementa la cantidad del producto
                    value["cantidad"] = value["cantidad"] + 1
                    
                    # Precio unitario actualizado con descuento aplicado
                    precio_con_descuento = producto.precio - (producto.precio * producto.descuento / 100)
                    
                    # Actualiza el precio total sumando el precio con descuento
                    value["precio"] = str(Decimal(value["precio"]) + precio_con_descuento)
                    
                    # Actualiza el precio final total (aunque este valor puede depender de cómo se quiera mostrar en la vista)
                    value["precio_final"] = str(Decimal(value["precio_final"]) + precio_con_descuento)
                    
                    break
        self.guardar_carro()
        
    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified=True
        
    def eliminar(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.carro:
            del self.carro[producto_id]
            self.guardar_carro()
    
    def restar_producto(self, producto):
        for key, value in self.carro.items():
            if key == str(producto.id):
                # Restar una unidad del producto
                value["cantidad"] = value["cantidad"] - 1

                # Calcular el precio considerando si hay descuento o no
                if Decimal(value["descuento"]) > 0:
                    # Si hay descuento, recalculamos el precio con descuento
                    precio_con_descuento = producto.precio - (producto.precio * producto.descuento / 100)
                    value["precio"] = str(Decimal(value["precio"]) - precio_con_descuento)
                else:
                    # Si no hay descuento, restamos el precio unitario directamente
                    value["precio"] = str(Decimal(value["precio"]) - producto.precio)
                
                # Si la cantidad es menor que 1, eliminamos el producto del carrito
                if value["cantidad"] < 1:
                    self.eliminar(producto)
                
                break

    # Guardar los cambios en el carrito
        self.guardar_carro()

        
        ###
        #producto_id = str(producto.id)
        #if producto_id in self.carro:
        #    self.carro[producto_id]["stock"] -= 1
        #    if self.carro[producto_id]["stock"] < 1:
        #        self.eliminar(producto)
        #    else:
        #        self.guardar_carro()
        ###

    def obtener_cantidad(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.carro:
            return self.carro[producto_id]['cantidad']
        return 0

    def vaciar_carro(self):
        self.session["carro"]={}
        self.session.modified=True
        
        ###
        #self.carro = {}
        #self.guardar_carro()
        ###