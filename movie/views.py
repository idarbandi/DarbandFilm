from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import  JsonResponse
from django.views.generic import DetailView, ListView, CreateView

from movie.forms import MovieCommentForm
from movie.models import Movie, Comment


class main(ListView):
    template_name = 'index.html'
    model = Movie
    paginate_by = 3
    context_object_name = 'movie'


class movie(LoginRequiredMixin, DetailView):
    model = Movie
    login_url = 'http://127.0.0.1:8000/admin/login/?next=/admin/'
    template_name = 'movie.html'
    queryset = Movie.objects.all()
    slug_field = 'name'
    slug_url_kwarg = 'name'
    context_object_name = 'feed'
    extra_context = None

    def get(self, request, *args, **kwargs):
        self.query_pk_and_slug = kwargs.get('pk')
        return super().get(request, *args, **kwargs)


class Search(ListView):
    model = Movie
    template_name = 'index.html'
    context_object_name = 'search'

    def get_queryset(self):
        qs = super().get_queryset()
        movie_name = self.request.GET.get('box', None)
        print(self.request.GET.get('box', None))
        return qs.filter(name__icontains=movie_name)


class Comment(CreateView):
    model = Comment
    form_class = MovieCommentForm
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        userless = form.save(commit=False)
        userless.movie = Movie.objects.get(name=self.request.POST.get("movie"))
        userless.user = self.request.user
        userless.save()
        return super().form_valid(form)