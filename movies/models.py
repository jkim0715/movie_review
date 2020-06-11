from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    rate = models.FloatField()
    
    