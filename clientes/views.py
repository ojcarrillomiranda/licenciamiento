from django.shortcuts import render

from clientes.models import ClienteLicencia


# Create your views here.

def lista_clientes(request):
    # clientes = Cliente.objects.all().order_by('id')
    clientes = ClienteLicencia.objects.all().order_by('id')
    return render(request, 'clientes/lista.html', {'clientes': clientes})
