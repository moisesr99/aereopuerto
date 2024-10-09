from django.shortcuts import redirect
from tienda.models import Producto
from decimal import Decimal, ROUND_HALF_UP
from decimal import Decimal


class Ticket:
    def __init__(self, request):
        self.request=request
        self.session=request.session
        ticket=self.session.get("ticket")
        if not ticket:
           ticket=self.session["ticket"]={}
           
        self.ticket=ticket
        
        
    def comprar(self, vuelo):
        if(str(vuelo.id) not in self.ticket.keys()): #gregar el vuelo a la compra
            self.ticket[vuelo.id]={
                "vuelo_id":vuelo.id,
                "destino":vuelo.destino, #ciudad destino
                "partida":vuelo.partida, #ciudad origen
                "precio":vuelo.precio,
                "fechaSAL":vuelo.fechaSAL,
                "hora":vuelo.hora,
                "asientos":1,    
            }
        else:
            for key, value in self.vuelo.items():
                if key == str(vuelo.id):
                   value["asientos"]=value["asientos"]+1
                   
                   precio_con_descuento = vuelo.precio - (vuelo.precio * vuelo.descuento / 100)
                   
                   value["precio"] = str(Decimal(value["precio"])+precio_con_descuento)
                   
                   value["precio_final"] = str(Decimal(value["precio_final"] + precio_con_descuento))
                   
                   break
        self.guardar_ticket()
    
    def guardar_ticket(self):
        self.session["vuelo"]=self.vuelo
        self.session.modified=True
        
    def eliminar_vuelo(self, vuelo):
        vuelo_id = str(vuelo.id)
        if vuelo_id in self.vuelo:
            del self.vuelo[vuelo_id]
            self.guardar_ticket()
            
    def restar_asiento(self, vuelo):
        for key, value in self.vuelo.items():
            if key == str(vuelo.id):
                value["asientos"]= value["asientos"] - 1
                
                if Decimal(value["descuento"]) > 0:
                    precio_con_descuento = vuelo.precio -(vuelo.precio * vuelo.descuento /100)
                    value["precio"] = str(Decimal(value["precio"])-precio_con_descuento)
                else:
                    value["precio"] = str(Decimal(["precio"])- vuelo.precio)
                    
                if value["asientos"] < 1:
                    self.eliminar_vuelo(vuelo)
                    
                break
        self.guardar_ticket()
        

        
                
            
        
            