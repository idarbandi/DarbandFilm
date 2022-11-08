from movie.models import Movie
from django import template

register = template.Library()


@register.simple_tag
def feed():
    return Movie.objects.all()