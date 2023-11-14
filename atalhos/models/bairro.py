from django.db import models

class Bairro(models.Model):
    nome_do_bairro = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome_do_bairro