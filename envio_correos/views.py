from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import get_object_or_404, redirect
from django.template.loader import get_template
from datetime import date

from clientes.models import ClienteLicencia
from licenciamiento import settings


# Create your views here.

def enviar_correo(request, id):
    correo_cliente = get_object_or_404(ClienteLicencia, pk=id)
    precio_base = correo_cliente.licencia.valor_base
    valor_renovacion = correo_cliente.licencia.valor_renovacion
    iva = correo_cliente.licencia.iva
    precio_renovacion = precio_base * valor_renovacion / 100 + precio_base
    total = round(precio_renovacion * iva / 100 + precio_renovacion)

    fecha = date.today()
    fecha_vencimiento = correo_cliente.licencia.fecha_caducidad
    diferencia = fecha_vencimiento - fecha

    if diferencia.days <= 122:  # 4 meses
        template = get_template('correo.html')
        content = template.render({'correo_cliente': correo_cliente, 'total': total})

        mensaje = EmailMultiAlternatives(
            'Su licencia esta apunto de caducar',
            'No responda este correo',
            settings.EMAIL_HOST_USER,
            [correo_cliente.cliente.correo]
        )

        mensaje.attach_alternative(content, 'text/html')
        mensaje.send()
        messages.success(request, 'El correo se envio con exito')
    else:
        messages.error(request, 'La fecha de caducidad aun no se cumple')
    return redirect('lista_clientes')
