from django.db import models

# Create your models here.

class Licencia(models.Model):
    tipo_licencia = models.CharField(max_length=255)
    nombre_paquete = models.CharField(max_length=255)
    fecha_creacion = models.DateField(auto_now=True)
    fecha_caducidad = models.DateField()
    valor_base = models.IntegerField()
    iva = models.IntegerField(default=19)
    valor_renovacion = models.IntegerField(default=25)
    valor_anual = models.IntegerField(default=10)


    def __str__(self):
        return f'{self.nombre_paquete}'

