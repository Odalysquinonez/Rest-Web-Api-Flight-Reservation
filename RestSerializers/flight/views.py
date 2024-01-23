from rest_framework import generics, viewsets, filters, status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.response import Response

from RestSerializers.Serializers import SerializadorVueloPersonalizado
from flight.models import VueloPersonalizado

# Vista API para la lista de vuelos personalizados
class ListaVuelosPersonalizados(generics.ListCreateAPIView):
    queryset = VueloPersonalizado.objects.all()
    serializer_class = SerializadorVueloPersonalizado
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['numero_vuelo', 'aerolinea']
    ordering_fields = ['numero_vuelo']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Vista API para los detalles de un vuelo personalizado
class DetalleVueloPersonalizado(generics.RetrieveUpdateDestroyAPIView):
    queryset = VueloPersonalizado.objects.all()
    serializer_class = SerializadorVueloPersonalizado
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except VueloPersonalizado.DoesNotExist:
            return Response({"detail": "Vuelo personalizado no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Conjunto de vistas para vuelos personalizados
class ConjuntoVuelosPersonalizados(viewsets.ModelViewSet):
    http_method_names = ['get', 'head', 'options', 'put', 'patch', 'delete']
    queryset = VueloPersonalizado.objects.all()
    serializer_class = SerializadorVueloPersonalizado
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_object(self):
        try:
            return super().get_object()
        except VueloPersonalizado.DoesNotExist:
            raise Response({"detail": "Vuelo personalizado no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            raise Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
