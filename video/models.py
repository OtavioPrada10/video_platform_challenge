from django.db import models

class Categoria(models.Model):
    title = models.CharField(max_length=30)
    cor = models.CharField(max_length=20)

class Video(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    categoria_id = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    