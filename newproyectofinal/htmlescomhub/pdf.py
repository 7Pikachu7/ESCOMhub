from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer, Table, TableStyle
from reportlab.lib.units import inch

def crear_pdf(nombre_archivo):
    doc = SimpleDocTemplate(nombre_archivo, pagesize=letter)
    estilos = getSampleStyleSheet()
    
    # Estilo personalizado para el título
    estilo_titulo = ParagraphStyle(
        'Titulo',
        parent=estilos['Heading1'],
        fontSize=24,
        textColor=colors.HexColor("#2E86C1"),
        alignment=1,  # Centrado
        spaceAfter=20,
    )
    
    # Estilo para el cuerpo del texto
    estilo_cuerpo = estilos['BodyText']
    estilo_cuerpo.alignment = 1  # Centrado
    
    elementos = []
    
    # Título
    titulo = Paragraph("¡Gracias por comprar en <b>ESCOMHUB</b>!", estilo_titulo)
    elementos.append(titulo)
    
    # Imagen (puedes poner cualquier imagen en la ruta especificada)
    ruta_imagen = "images/logo.png"
  # Cambia por la ruta de tu imagen
    try:
        imagen = Image(ruta_imagen)
        imagen.drawHeight = 2 * inch
        imagen.drawWidth = 5 * inch
        imagen.hAlign = 'CENTER'
        elementos.append(imagen)
    except:
        # Si no encuentra la imagen, no falla
        elementos.append(Paragraph("Imagen no disponible.", estilo_cuerpo))
    
    elementos.append(Spacer(1, 20))
    
    # Mensaje adicional
    mensaje = Paragraph(
        "Esperamos que disfrutes tu compra.<br/>"
        "Si tienes dudas o necesitas ayuda, contáctanos en <b>soporte@escomhub.com</b>.<br/><br/>"
        "¡Vuelve pronto!",
        estilo_cuerpo
    )
    elementos.append(mensaje)
    
    elementos.append(Spacer(1, 40))
    
    # Pie de página con estilo de tabla para decorar
    datos_pie = [['ESCOMHUB', 'Calidad y Tecnología a tu alcance']]
    tabla_pie = Table(datos_pie, colWidths=[3*inch, 3*inch])
    tabla_pie.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#2E86C1")),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
    ]))
    elementos.append(tabla_pie)
    
    # Crear PDF
    doc.build(elementos)
    print(f"PDF creado: {nombre_archivo}")

if __name__ == "__main__":
    crear_pdf("Gracias_ESCOMHUB.pdf")
