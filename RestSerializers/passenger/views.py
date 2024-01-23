from rest_framework import generics, viewsets, filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.response import Response
from rest_framework import status

from RestSerializers.Serializers import SerializadorPasajero
from passenger.models import Pasajero

# Vista de Pasajeros APIView
class VistaPasajeros(generics.ListCreateAPIView):
    queryset = Pasajero.objects.all()
    serializer_class = SerializadorPasajero
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre', 'apellido']
    ordering_fields = ['apellido']  # Campos para ordenar
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# DetallePasajero APIView
class DetallePasajero(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pasajero.objects.all()
    serializer_class = SerializadorPasajero
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Pasajero.DoesNotExist:
            return Response({"detail": "Pasajero no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# PasajeroViewSet
class PasajeroViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Pasajero.objects.all()
    serializer_class = SerializadorPasajero
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_object(self):
        try:
            return super().get_object()
        except Pasajero.DoesNotExist:
            return Response({"detail": "Pasajero no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
