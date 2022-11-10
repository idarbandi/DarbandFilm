from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_GET
from django.views import View
from django.views.generic import DetailView, FormView, ListView

from movie.models import Movie


# Create your views here.


class main(View):
    template_name = "index.html"
    qset = Count('comment')

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"count": self.qset})


class movie(LoginRequiredMixin, DetailView):
    model = Movie
    login_url = 'http://127.0.0.1:8000/admin/login/?next=/admin/'
    template_name = 'movie.html'
    queryset = Movie.objects.all()
    context_object_name = 'feed'

    def get(self, request, *args, **kwargs):
        self.query_pk_and_slug = kwargs.get('pk')
        return super().get(request, *args, **kwargs)


class Search(ListView):
    model = Movie
    template_name = 'search.html'
    context_object_name = 'search'

    def get_queryset(self):
        qs = super().get_queryset()
        movie_name = self.request.GET.get('box', None)
        print(self.request.GET.get('box', None))
        return qs.filter(name__icontains=movie_name)
