# Generated by Django 4.2 on 2024-09-25 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_cliente', models.CharField(max_length=255)),
                ('direccion_cliente', models.CharField(max_length=255)),
                ('telefono_cliente', models.CharField(max_length=15)),
                ('correo_cliente', models.EmailField(max_length=255)),
            ],
        ),
    ]
