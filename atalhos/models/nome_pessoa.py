from django.db import models

class Nickname(models.Model):
    nome_da_pessoa = models.CharField(max_length=255)
    