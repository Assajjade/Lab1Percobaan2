from django.db import models

# Create your models here.

class WatchlistAbdi(models.Model):
    watched = models.CharField(max_length=10)
    title = models.CharField(max_length=255)
    rating = models.IntegerField()
    release_date = models.CharField(max_length=50)
    review = models.TextField()
    