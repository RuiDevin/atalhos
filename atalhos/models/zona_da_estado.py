from django.db import models

class ZonaEstado(models.Model):
    zona_do_estado = models.CharField(max_length=255)
    