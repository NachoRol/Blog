from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateTimeField(null=True,blank=True)
    pais_actual = models.ForeignKey(Pais, on_delete=models.PROTECT)
    

# Create your models here.
