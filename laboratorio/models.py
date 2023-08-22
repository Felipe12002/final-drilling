from django.db import models

# Create your models here.

class Laboratorio(models.Model):
    nombre = models.CharField(max_length = 128)

class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length = 128)
    laboratorio = models.OneToOneField(Laboratorio, on_delete = models.PROTECT)

class Producto(models.Model):
    nombre = models.CharField(max_length = 128)
    laboratorio = models.ForeignKey(Laboratorio, on_delete = models.PROTECT)
    f_fabricacion = models.DateField()
    p_costo = models.DecimalField(max_digits = 12, decimal_places = 2)
    p_venta = models.DecimalField(max_digits = 12, decimal_places = 2)