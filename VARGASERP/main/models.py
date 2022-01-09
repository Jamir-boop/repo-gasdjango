from django.db import models

# Create your models here.
class Proveedor(models.Model):
    codigo = models.CharField(max_length=250)
    ruc = models.CharField(max_length=250)
    nombre = models.CharField(max_length=250)
    contacto = models.CharField(max_length=250)
    observaciones = models.CharField(max_length=250)

class Stock(models.Model):
    id_proveedor = models.IntegerField
    marca = models.CharField(max_length=250)
    unidades_inicial = models.IntegerField
    unidades_disponible = models.IntegerField
    fecha_ingreso = models.DateField
    costo_unitario = models.FloatField
    costo_total = models.FloatField
    estado = models.CharField(max_length=250)
    encargado = models.CharField(max_length=250)

class Venta(models.Model):
    id_vale = models.IntegerField
    id_stock = models.IntegerField
    id_cliente = models.IntegerField
    nombre_cliente = models.CharField(max_length=250)
    dni_cliente = models.CharField(max_length=250)
    pago_parcial = models.FloatField
    deuda = models.FloatField
    precio_venta = models.FloatField
    observaciones = models.CharField(max_length=250)
    marca = models.CharField(max_length=250)
    unidades = models.IntegerField
    pago_rotal = models.FloatField
    fecha = models.DateField
    encargado = models.CharField(max_length=250)

class Egresos(models.Model):
    categoria = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=250)
    costos= models.CharField(max_length=250)

class Vale(models.Model):
    id_cliente = models.IntegerField
    valor = models.FloatField
    unidades = models.IntegerField
    id_venta = models.IntegerField

class Cliente(models.Model):
    nombre = models.CharField(max_length=250)
    contacto = models.CharField(max_length=250)
    dni = models.CharField(max_length=8)
    observacion = models.CharField(max_length=250)
