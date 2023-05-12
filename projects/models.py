from django.db import models

# Create your models here.
class Project(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = models.IntegerField()
    created_at =  models.DateTimeField(auto_now_add=True)

                