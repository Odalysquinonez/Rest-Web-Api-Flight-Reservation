# Generated by Django 5.0.1 on 2024-01-23 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vuelo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('numero', models.CharField(max_length=10)),
                ('aerolinea', models.CharField(max_length=150)),
                ('c_destino', models.CharField(max_length=80)),
                ('c_arribo', models.CharField(max_length=80)),
                ('f_salida', models.DateTimeField()),
            ],
            options={
                'db_table': 'Vuelo',
            },
        ),
    ]
