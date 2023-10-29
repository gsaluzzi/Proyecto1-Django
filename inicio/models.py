from django.db import models

# class Paleta(models.Model):
#     marca = models.CharField(max_length=30)
#     descripcion = models.TextField()
#     anio = models.IntegerField()


class Celular(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    anio = models.IntegerField()
    
    def __str__(self):
        return f'{self.id} - {self.marca} - {self.anio}'
    

class Tablet(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    anio = models.IntegerField()

