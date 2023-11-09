from django.db import models

class Bairros(models.Model):
    nome_do_bairro = models.CharField(max_length=255)
    