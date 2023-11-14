from django.db import models

from .estado import Estado
from .rua import Rua
from .bairro import Bairro
from .cidade import Cidade
from .estado import Estado

class Endereco(models.Model):
    rua = models.ForeignKey(Rua, on_delete=models.PROTECT, null=True)
    bairro = models.ForeignKey(Bairro, on_delete=models.PROTECT, null=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT, null=True)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.rua