from django.db import models

class ZonaEstado(models.Model):
    zona_do_estado = models.CharField(max_length=255)
    
    def __str__(self):
        return self.zona_do_estado