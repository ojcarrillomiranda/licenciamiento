# Generated by Django 4.1.7 on 2023-03-02 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('licencias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('correo', models.CharField(max_length=255)),
                ('licencias', models.ManyToManyField(to='licencias.licencia')),
            ],
        ),
    ]
