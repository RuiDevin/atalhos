from django.db import models

from .zona_da_cidade import ZonaCidade

class Cidade(models.Model):
    nome_do_estado = models.CharField(max_length=255)
    parte_cidade = models.ForeignKey(ZonaCidade, on_delete=models.PROTECT, null=True) 
    