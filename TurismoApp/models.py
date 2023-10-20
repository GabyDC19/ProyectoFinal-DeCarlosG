from django.db import models

# Create your models here.
class inicio (models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    fecha_de_entrega = models.DateField()

class paquetes(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()
    cantidad = models.IntegerField()

class tailandia(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    fecha_de_entrega = models.DateField()

class natal(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    fecha_de_entrega = models.DateField()
    
