from django import template
from movie.models import  Trailer

register = template.Library()


@register.simple_tag
def trailer():
    return Trailer.objects.all()