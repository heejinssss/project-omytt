from django.db import models
from django.conf import settings

# Create your models here.

class Ott(models.Model):
    initial = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    signup = models.CharField(max_length=200)
    ott_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='ott_user')


class Genre(models.Model):
    name = models.CharField(max_length=50)


class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    overview = models.TextField(null=True, blank=True)
    poster_path = models.TextField(null=True, blank=True)
    released_date = models.DateField(null=True, blank=True)
    genres = models.ManyToManyField(Genre)
    backdrop_path = models.TextField(null=True, blank=True)
    popularity = models.FloatField()
    tagline = models.CharField(max_length=255)
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    video_key = models.CharField(max_length=255)

    # 좋아요 기능
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')

    def __str__(self):
        return self.title


class Tmdb(models.Model):
    tmdb_id = models.OneToOneField(Movie, on_delete=models.CASCADE, primary_key=True)
    ott_lst = models.JSONField()


# comment
class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    content = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
