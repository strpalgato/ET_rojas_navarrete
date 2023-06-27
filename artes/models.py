from django.db import models

# Create your models here.

from django.db import models

class Producto(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    size = models.CharField(max_length=100) #tamaño del producto
    tecnica = models.CharField(max_length=100) #tecnica del producto
    precio = models.DecimalField(max_digits=10, decimal_places=3)
    imagen = models.ImageField(upload_to='productos/')
    def __str__(self):
        return self.nombre