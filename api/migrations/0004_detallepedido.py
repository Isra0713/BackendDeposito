# Generated by Django 4.2 on 2024-09-26 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_pedido'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id_detalle', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('id_pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.pedido')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.producto')),
            ],
        ),
    ]
