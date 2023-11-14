from django.db import models

OPERADORAS_CHOICES = [
    ('VIVO', 'Vivo'),
    ('TIM', 'TIM'),
    ('CLARO', 'Claro'),
    ('OI', 'Oi'),
    ('NEXTEL', 'Nextel'),
    ('ALGAR', 'Algar'),
    ('SERCOMTEL', 'Sercomtel'),
    # Adicione mais operadoras conforme necessário
]

class Operadora(models.Model):
    operadora = models.CharField(max_length=255, choices=OPERADORAS_CHOICES)
                                 
    def __str__(self):
        return self.operadora
