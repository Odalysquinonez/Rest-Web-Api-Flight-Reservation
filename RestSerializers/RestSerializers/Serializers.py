# flight_reservation/serializers.py
from rest_framework import serializers

from flight.models import VueloPersonalizado
from passenger.models import Pasajero
from reservations.models import Reserva


class SerializadorVueloPersonalizado(serializers.ModelSerializer):
    class Meta:
        model = VueloPersonalizado
        fields = '__all__'

class SerializadorPasajero(serializers.ModelSerializer):
    class Meta:
        model = Pasajero
        fields = '__all__'

class SerializadordeReservaciones(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'