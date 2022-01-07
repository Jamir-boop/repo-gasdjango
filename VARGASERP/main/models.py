from django.db import models

# Create your models here.
class TestAdmin(models.Model):
    nombre = models.CharField(max_length=250)
    estado = models.BooleanField(default=True)