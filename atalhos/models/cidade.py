from django.db import models

from .zona_da_cidade import ZonaCidade

class Cidade(models.Model):
    nome_do_cidade = models.CharField(max_length=255)
    parte_cidade = models.ForeignKey(ZonaCidade, on_delete=models.PROTECT, null=True)   

    def __str__(self):
        return self.nome_do_cidade   