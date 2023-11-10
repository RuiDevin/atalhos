from django.db import models

class ZonaCidade(models.Model):
    zona_da_cidade = models.CharField(max_length=255)
    
    def __str__(self):
        return self.zona_da_cidade