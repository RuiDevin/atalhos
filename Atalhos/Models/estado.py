from django.db import models

class Estado(models.Model):
    nome_do_estado = models.CharField(max_length=255)
    