from django.db import models

from .estado import Estado
from .rua import Rua

class Endereco(models.Model):
    endereço = models.ForeignKey(Estado, on_delete=models.PROTECT, null=True)
    rua = models.ForeignKey(Rua, on_delete=models.PROTECT, null=True)
    
    def __str__(self):
        return self.endereço