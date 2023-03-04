from datetime import date

from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.template.loader import get_template

from clientes.models import ClienteLicencia
from licenciamiento import settings


# Create your views here.

def home(request):
    enviar_correo_automatico()
    return render(request, 'home.html')


def enviar_correo_automatico():
    correo_cliente = ClienteLicencia.objects.all().first()
    precio_base = correo_cliente.licencia.valor_base
    valor_renovacion = correo_cliente.licencia.valor_renovacion
    iva = correo_cliente.licencia.iva
    precio_renovacion = precio_base * valor_renovacion / 100 + precio_base
    total = round(precio_renovacion * iva / 100 + precio_renovacion)

    fecha = date.today()
    fecha_vencimiento = correo_cliente.licencia.fecha_caducidad
    diferencia = fecha_vencimiento - fecha

    if diferencia.days <= 121.667:  # 4 meses
        template = get_template('correo_automatico.html')
        content = template.render({'correo_cliente': correo_cliente, 'total': total})

        mensaje = EmailMultiAlternatives(
            'Su licencia esta apunto de caducar',
            'No responda este correo',
            settings.EMAIL_HOST_USER,
            [correo_cliente.cliente.correo]
        )

        mensaje.attach_alternative(content, 'text/html')
        mensaje.send()
    else:
        return
