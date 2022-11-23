from movie.forms import MovieCommentForm
from django import template

register = template.Library()


@register.simple_tag
def comment():
    return MovieCommentForm
