from django.db import models

class Registro(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    # Agrega otros campos según tus necesidades
    
    def __str__(self):
        return self.nombre


