from django.db import models

class Cidade(models.Model):
    nome_cidade = models.CharField(max_length=255)