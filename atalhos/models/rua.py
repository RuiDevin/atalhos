from django.db import models

class Rua(models.Model):
    nome_da_rua = models.CharField(max_length=255)
    numero = models.CharField(max_length=255, null=True)
    ponto_de_referencia = models.TextField(max_length=255, null=True)
    
    def __str__(self):
        return self.nome_da_rua