from django.db import models
from django.conf import settings
from movies.models import Movie
# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now =True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')

    # movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now =True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comments')