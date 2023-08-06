from django.db import models
from django.contrib.auth.models import User

class AnimeData(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.CharField(max_length=200)
    release_year = models.IntegerField()
    catch_phrase = models.CharField(max_length=100)

class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField(AnimeData, related_name='favorite_users')
    watched = models.ManyToManyField(AnimeData, related_name='watched_users')

class CustomerReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anime = models.ForeignKey(AnimeData, on_delete=models.CASCADE)
    star = models.IntegerField()
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
