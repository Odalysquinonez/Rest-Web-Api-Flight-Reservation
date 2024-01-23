from django.db import models

from flight.models import VueloPersonalizado
from passenger.models import Pasajero


class Reserva(models.Model):
    reserva_id = models.IntegerField(primary_key=True)
    vuelo_reservado = models.OneToOneField(VueloPersonalizado, on_delete=models.CASCADE)
    pasajero_reservado = models.OneToOneField(Pasajero, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Reserva'

