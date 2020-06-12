from django.db import models

from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=255)


class Movie(models.Model):
    title = models.CharField( max_length=255)
    original_title = models.CharField( max_length=255)
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    adult = models.BooleanField()
    overview = models.TextField()
    original_language = models.CharField( max_length=255)
    poster_path = models.CharField( max_length=255, null= True)
    backdrop_path = models.CharField( max_length=255, null= True)
    genres = models.ManyToManyField(Genre, related_name='genre_movies')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_movies")


class MovieComment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    rate = models.FloatField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_movie_comment")
