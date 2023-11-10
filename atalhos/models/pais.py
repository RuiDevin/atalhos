from django.db import models

class Pais(models.Model):
    pais = models.CharField(max_length=255)
    