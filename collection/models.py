from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=150)
    description=models.CharField(max_length=200)
    genres=models.CharField(max_length=200)
    uuid=models.UUIDField(unique=True)

class Collection(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    description=models.TextField(max_length=200)
    movies = models.ManyToManyField(Movie)
