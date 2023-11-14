from django.db import models

class Nickname(models.Model):
    nome_da_pessoa = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome_da_pessoa
    