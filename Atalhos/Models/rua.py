from django.db import models

class Rua(models.Model):
    nome_da_rua = models.CharField(max_length=255)
    