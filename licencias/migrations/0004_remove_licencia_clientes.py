# Generated by Django 4.1.7 on 2023-03-03 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('licencias', '0003_licencia_clientes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='licencia',
            name='clientes',
        ),
    ]
