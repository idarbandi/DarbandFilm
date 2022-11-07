from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, FormView

from movie.models import Movie


# Create your views here.


class main(View):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class movie(LoginRequiredMixin, DetailView, FormView):
    model = Movie
    template_name = 'movie.html'
    queryset = Movie.objects.all()


class Search(View):
    pass
