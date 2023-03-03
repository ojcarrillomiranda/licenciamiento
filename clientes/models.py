from django.db import models

from licencias.models import Licencia


# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    correo = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.nombre} {self.apellido} '


class ClienteLicencia(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    licencia = models.ForeignKey(Licencia, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.cliente.nombre} {self.cliente.apellido}, Licencia Activa: {self.licencia.nombre_paquete}'
