from django.shortcuts import render

from licencias.models import Licencia


# Create your views here.

def lista_licencias(request):
    licencias = Licencia.objects.all()
    return render(request, 'licencias/lista.html', {'licencias': licencias})
