from django.db import models
from khayyam.jalali_datetime import JalaliDatetime


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


class Comment(models.Model):
    body = models.TextField(max_length=120, null=True)

    def __str__(self):
        return self.body


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


class MovieComments(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='movies')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"{self.comment}\t{self.movie}"


class MovieQuality(models.Model):
    quality = models.ForeignKey(Quality, related_name='movies', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='quality', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.quality}\t{self.movie}"
