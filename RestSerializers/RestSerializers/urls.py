"""
URL configuration for RestSerializers project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path

from flight.views import ListaVuelosPersonalizados, DetalleVueloPersonalizado
from passenger.views import DetallePasajero, VistaPasajeros
from reservations.views import ListaDeReservas, DetalleDeReserva

urlpatterns = [
    path('lista_vuelos/', ListaVuelosPersonalizados.as_view(), name='lista_vuelos'),
    path('detalle_vuelo/<int:pk>/', DetalleVueloPersonalizado.as_view(), name='detalle_vuelo'),
    path('lista_pasajeros/', VistaPasajeros.as_view(), name='lista_pasajero'),
    path('detalle_pasajero/<int:pk>/', DetallePasajero.as_view(), name='detalle_pasajero'),
    path('lista_reserva/', ListaDeReservas.as_view(), name='lista_reserva'),
    path('detalle_reserva/<int:pk>/', DetalleDeReserva.as_view(), name='detalle_reserva'),
    path('admin/', admin.site.urls),
]
