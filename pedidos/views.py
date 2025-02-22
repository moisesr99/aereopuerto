from django.contrib import messages
from .models import Pedido, LineaPedido
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
#reportlab para generar PDF
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO
from reportlab.pdfgen import canvas
#openpyxl para generar EXCEL
from openpyxl.styles import Font, Alignment
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font,PatternFill,Side
#VISTAS
from carro.carro import Carro
from gestion_vuelos.models import vuelos
from pedidos.models import LineaPedido, Pedido

@login_required(login_url="/login/iniciar_sesion/")
def procesar_pedido(request):  # Pedidos para la app de tienda
    pedido = Pedido.objects.create(user=request.user)
    carro = Carro(request)
    lineas_pedido = []
    total_pedido = sum(linea.total_pedido for linea in lineas_pedido)

    for key, value in carro.carro.items():  # Recorrer todos los productos
        lineas_pedido.append(LineaPedido(
            producto_id=key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido=pedido,
            
            
        ))

    LineaPedido.objects.bulk_create(lineas_pedido)

    # Enviar correo de confirmación
    enviar_mail(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombreusuario=request.user.username,
        emailusuario=request.user.email
    )

    # Generar PDF de pedido y agregarlo a la respuesta, aun no funciona
    pdf_response = generar_pdf_pedido(request, pedido_id=pedido.id) #deberia descargar el pdf en automatico en la pagina

    messages.success(request, "El pedido se ha creado correctamente")
    return render(request, "confirmar_pedido.html", {
        "pedido": pedido,
        "lineas_pedido": lineas_pedido,
        "pdf_response": pdf_response,
        "total_pedido":total_pedido
    })
#INICIA GENERACION DE PDF
def generar_pdf_pedido(request, pedido_id): 
    # Extrae el pedido y sus detalles
    pedido = Pedido.objects.get(id=pedido_id, user=request.user)
    lineas_pedido = LineaPedido.objects.filter(pedido=pedido)
    nombreusuario = request.user.username

    # Configura el nombre del archivo y la respuesta
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="pedido_{pedido_id}.pdf"'

    # Configura el buffer y el documento
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)

    # Estilos
    styles = getSampleStyleSheet()
    elements = []

    # Título del documento
    elements.append(Paragraph(f"Detalles del Pedido #{pedido_id}", styles['Title']))
    elements.append(Paragraph(f"Cliente: {nombreusuario}", styles['Normal']))

    # Crear los datos de la tabla
    data = [
        ["Producto", "ID Producto", "Cantidad", "Precio Unitario", "Sub-total"]
    ]

    total = 0
    for linea in lineas_pedido:
        if linea.producto.descuento > 0:
            precio_final = linea.producto.precio_final
        else:
            precio_final = linea.producto.precio
        sub_total = linea.cantidad * precio_final
        total += sub_total

        data.append([
            linea.producto.nomProduct,
            linea.producto_id,
            linea.cantidad,
            f"${precio_final:.2f}",
            f"${sub_total:.2f}"
        ])

    # Agrega el total de la compra
    data.append(["", "", "", "TOTAL", f"${total:.2f}"])

    # Configura la tabla y el estilo
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements.append(table)
    
    

    # Genera el contenido del PDF
    doc.build(elements)

    # Guarda el PDF en el buffer y lo envía en la respuesta
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

#TERMINA GENERACION DE PDF
#INCIA GENERACION DE EXCEL
def generar_excel_pedido(request, pedido_id):
    # Extrae el pedido y sus detalles
    pedido = Pedido.objects.get(id=pedido_id, user=request.user)
    lineas_pedido = LineaPedido.objects.filter(pedido=pedido)
    nombreusuario = request.user.username

    # Crear libro de trabajo y hoja
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = f"Pedido_{pedido_id}"

    # Nombre de las columnas
    headers = ["Producto", "ID Producto", "Cantidad", "Precio Unitario", "Sub-total"]
    sheet.append(headers)

    # Estilos para los encabezados
    for cell in sheet[1]:
        cell.font = Font(bold=True)
        cell.alignment = Alignment(horizontal="center")

    # Insertando datos
    total = 0
    for linea in lineas_pedido:
        precio_final = linea.producto.precio_final if linea.producto.descuento > 0 else linea.producto.precio
        sub_total = linea.cantidad * precio_final
        total += sub_total
        
        # Agregar los datos de cada línea de pedido
        sheet.append([
            linea.producto.nomProduct,
            linea.producto_id,
            linea.cantidad,
            f"${precio_final:.2f}",
            f"${sub_total:.2f}"
        ])

    # Agregar el total
    sheet.append(["", "", "", "TOTAL", f"${total:.2f}"])

    # Ajustar el ancho de columnas
    for column_cells in sheet.columns:
        length = max(len(str(cell.value)) for cell in column_cells)
        sheet.column_dimensions[column_cells[0].column_letter].width = length + 2

    # Preparar la respuesta HTTP
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = f'attachment; filename="pedido_{pedido_id}.xlsx"'

    # Guardar el archivo en el objeto response
    wb.save(response)

    return response

    
#TERMINA GENERACION DE EXCEL



def enviar_mail(**kwargs):
    if Carro:
        asunto="PEDIDO REALIZADO, GRACIAS"
        mensaje=render_to_string("email/pedido.html",{
            "pedido":kwargs.get("pedido"),
            "lineas_pedido":kwargs.get("lineas_pedido"),
            "nombreusuario":kwargs.get("nombreusuario"),
            "email":kwargs.get("emailusuario")
        })
        
        mensaje_texto=strip_tags(mensaje)
        from_email="moises.ramirezr@fgr.org.mx"
        to=kwargs.get("emailusuario")
        
        send_mail(asunto,mensaje_texto,from_email,[to],html_message=mensaje)    

@login_required(login_url='/login/iniciar_sesion')
def procesar_vuelo(request):
    vuelo=vuelos.objects.create(user=request.user)
    carro=Carro(request)
    lineas_pedido=list()
    for key,value in carro.carro.items(): #recorrer todos los productos
        lineas_pedido.append(LineaPedido(
            
            producto_id=key,
            cantidad=value["cantidad"],
            user=request.user,
            vuelo=vuelo
            
        ))
    
    LineaPedido.objects.bulk_create(lineas_pedido)
    enviar_mail_vuelos(vuelo=vuelo,
                lineas_pedido=lineas_pedido,
                nombreusuario=request.user.username,
                emailusuario=request.user.email
                )
    messages.success(request,"el vuelo se ha creado correctamente")
    
    return render(request, "gracias.html")

def enviar_mail_vuelos(**kwargs):
    asunto="PEDIDO REALIZADO, GRACIAS"
    mensaje=render_to_string("email/pedido.html",{
        "vuelo":kwargs.get("vuelo"),
        "lineas_pedido":kwargs.get("lineas_pedido"),
        "nombreusuario":kwargs.get("nombreusuario")
    })
    
    mensaje_texto=strip_tags(mensaje)
    from_email="moises.ramirezr@fgr.org.mx"
    to=kwargs.get("emailusuario")
    
    send_mail(asunto,mensaje_texto,from_email,[to],html_message=mensaje)
    
    


    