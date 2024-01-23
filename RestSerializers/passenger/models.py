from django.db import models

class Pasajero(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=156)
    telefono = models.CharField(max_length=10)

    class Meta:
        db_table = 'Pasajero'

    def __str__(self):
        return f'Nombre: {self.nombre} | Apellido: {self.apellido} | Email: {self.email} | Teléfono: {self.telefono}'
