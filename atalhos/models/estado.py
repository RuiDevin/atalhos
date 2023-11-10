from django.db import models

from .zona_da_estado import ZonaEstado
from .cidade import Cidade 

class Estado(models.Model):
    nome_do_estado = models.CharField(max_length=255)
    parte_estado = models.ForeignKey(ZonaEstado, on_delete=models.PROTECT, null=True)
    cidade_do_estado = models.ForeignKey(Cidade, on_delete=models.PROTECT, null=True) 
    
    def __str__(self):
        return self.nome_do_estado