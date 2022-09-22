from operator import mod
from platform import release
from turtle import title
from django.db import models
from logging.handlers import RotatingFileHandler

# Create your models here.

class WatchlistAbdi(models.Model):
    watched = models.CharField(max_length=10)
    title = models.CharField(max_length=255)
    rating = models.IntegerField()
    release_date = models.CharField(max_length=50)
    review = models.TextField()
    