# Generated by Django 5.0.1 on 2024-01-23 17:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0002_vuelopersonalizado'),
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='vuelo_reservado',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='flight.vuelopersonalizado'),
        ),
    ]
