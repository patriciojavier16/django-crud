from django.db import models

# Create your models here.
class Students(models.Model):
    dni = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

