from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return f"{self.nombre.capitalize()}"

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True,blank=True)
    pais_actual = models.ForeignKey(Pais, on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.apellido.upper()},{self.nombre.capitalize()}"
    

# Create your models here.
