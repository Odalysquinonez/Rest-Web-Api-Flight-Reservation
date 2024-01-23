from django.db import models
from django.utils import timezone

class VueloPersonalizado(models.Model):
    id = models.AutoField(primary_key=True)
    numero = models.CharField(max_length=10)
    aerolinea = models.CharField(max_length=150)
    c_destino = models.CharField(max_length=80)
    c_arribo = models.CharField(max_length=80)
    f_salida = models.DateTimeField()

    class Meta:
        db_table = 'Vuelo'

    def __str__(self):
        sitio_fecha_partida = timezone.localtime(self.f_salida)
        return f'Número: {self.numero} | Aerolínea: {self.aerolinea} | Destino: {self.c_destino} | ' \
               f'Arribo: {self.c_arribo} | Fecha Salida: {sitio_fecha_partida}'