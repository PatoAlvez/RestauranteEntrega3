from django.db import models

# Create your models here.

class Entrada(models.Model):
    plato=models.CharField(max_length=40)
    cantidad=models.DateField
    bebida=models.CharField(max_length=40)
    numero_de_mesa=models.CharField(max_length=5)

class PlatoPrincipal(models.Model):
    plato=models.CharField(max_length=40)
    cantidad=models.DateField
    bebida=models.CharField(max_length=40)
    numero_de_mesa=models.CharField(max_length=5)

    def __str__(self):
        return self.plato+""+self.cantidad+""+self.bebida

class Postre(models.Model):
    postres=models.CharField(max_length=40)
    cantidad=models.DateField
    numero_de_mesa=models.CharField(max_length=5)


