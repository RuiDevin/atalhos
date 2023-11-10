from django.db import models

from .rua import Rua

class Bairro(models.Model):
    nome_do_bairro = models.CharField(max_length=255)
    nome_da_rua = models.ForeignKey(Rua, on_delete=models.PROTECT, null=True)
    
    def __str__(self):
        return self.nome_do_bairro