# Generated by Django 4.1.7 on 2023-03-03 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_remove_cliente_licencias'),
        ('licencias', '0002_alter_licencia_fecha_caducidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='licencia',
            name='clientes',
            field=models.ManyToManyField(to='clientes.cliente'),
        ),
    ]
