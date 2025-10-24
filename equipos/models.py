from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    fecha_ingreso = models.DateField()
    ubicacion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} ({self.categoria})"
