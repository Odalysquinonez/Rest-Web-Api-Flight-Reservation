from rest_framework import generics, viewsets, filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.decorators import action
from rest_framework.response import Response

from RestSerializers.Serializers import SerializadordeReservaciones
from reservations.models import Reserva

class ListaDeReservas(generics.ListCreateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = SerializadordeReservaciones
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre_de_pasajero', 'apellido_de_pasajero']  # Ajusta los campos según tu modelo
    ordering_fields = ['pasajero__apellido']  # Campos para ordenar (ajusta según tu modelo)
    auth_classes = [BasicAuthentication]
    perm_classes = [IsAuthenticated, DjangoModelPermissions]

class DetalleDeReserva(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reserva.objects.all()
    serializer_class = SerializadordeReservaciones
    auth_classes = [BasicAuthentication]
    perm_classes = [IsAuthenticated, DjangoModelPermissions]

# VistaDeReservas
class VistaDeReservas(viewsets.ModelViewSet):  # Ahora es ModelViewSet para admitir todas las operaciones CRUD
    queryset = Reserva.objects.all()
    serializer_class = SerializadordeReservaciones
    auth_classes = [BasicAuthentication]
    perm_classes = [IsAuthenticated, DjangoModelPermissions]
    search_fields = ['apellido_de_pasajero', 'fecha_de_salida_de_vuelo']
    ordering_fields = ['id', 'vuelo_fecha_de_salida']
