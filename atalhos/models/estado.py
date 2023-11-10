from django.db import models

from .zona_da_estado import ZonaEstado

class Estado(models.Model):
    nome_do_estado = models.CharField(max_length=255)
    parte_estado = models.ForeignKey(ZonaEstado, on_delete=models.PROTECT, null=True) 
    