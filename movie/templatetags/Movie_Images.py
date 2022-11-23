from django import template

from movie.models import MovieImages

register = template.Library()


@register.simple_tag
def images():
    return MovieImages.objects.all()
