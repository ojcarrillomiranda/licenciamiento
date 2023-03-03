from django.contrib import admin

from clientes.models import Cliente,ClienteLicencia

# Register your models here.
admin.site.register(Cliente)
admin.site.register(ClienteLicencia)
