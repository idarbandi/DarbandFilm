import uuid

from django.db import models
from django.urls import reverse
from khayyam.jalali_datetime import JalaliDatetime

from user.models import MyUser


class Director(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Quality(models.Model):
    quality = models.CharField(max_length=35, null=True)

    def __str__(self):
        return self.quality


class Movie(models.Model):
    # INT = 1
    # STRING = 2
    # FLOAT = 3
    #
    # initial_choices = (
    #     (INT, 'Integer'),
    #     (STRING, 'String'),
    #     (FLOAT, 'Float'),
    #
    # )

    name = models.CharField(max_length=32)
    year = models.IntegerField(blank=True)
    rate = models.FloatField(blank=True)
    age_res = models.CharField(max_length=10)
    summary = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    awards = models.CharField(max_length=32)
    register_date = models.DateTimeField(default=JalaliDatetime.now)
    modify_date = models.DateTimeField(default=JalaliDatetime.now)
    platform = models.CharField(max_length=13, blank=True)

    def __str__(self):
        return self.name

    @property
    def distributer_by_priority(self):
        return self.distributer.all().order_by('download_rate').first()


class DirMovie(models.Model):
    dir_id = models.ForeignKey(Director, on_delete=models.PROTECT, related_name='directors')
    movie_id = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='directorsmovies')

    def __str__(self):
        return f"{self.movie_id} , {self.dir_id}"


class ActorMovie(models.Model):
    actor_id = models.ForeignKey(Actor, on_delete=models.PROTECT, related_name='moviesactors')
    movie_id = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='actorsmovies')

    def __str__(self):
        return f"{self.actor_id} , {self.movie_id}"


class Comment(models.Model):
    body = models.TextField(max_length=12000, null=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='comments')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')

    created_time = models.DateTimeField(default=str(JalaliDatetime.now()))


    def __str__(self):
        return self.body


class GenreMovie(models.Model):
    genre_id = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='moviegenres')
    movie_id = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='genresmovies')

    def __str__(self):
        return f"{self.genre_id} , {self.movie_id}"


class MovieImages(models.Model):
    image = models.ImageField(blank=True, upload_to='MovieImages/')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.movie.name


class MovieQuality(models.Model):
    quality = models.ForeignKey(Quality, related_name='movies', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='quality', on_delete=models.CASCADE)
    Download_links = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return f"{self.quality}\t{self.movie}"

