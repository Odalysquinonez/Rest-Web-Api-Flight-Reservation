# Generated by Django 5.0.1 on 2024-01-23 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pasajero',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=156)),
                ('telefono', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'Pasajero',
            },
        ),
    ]
