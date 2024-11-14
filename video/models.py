from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    url = models.CharField(max_length=100)