from django.urls import path, include, re_path
from movie.views import main, movie, Search, comment


urlpatterns = [
                  path('/main', main.as_view()),
                  path('/<int:pk>', movie.as_view(), name='movie'),
                  path('/search', Search.as_view(), name='searchbox'),
                  path('/comments/', comment.as_view(), name='MovieComment'),
                  path('/package/', include('package.urls')),
                  re_path(r'^/account', include('account.urls'))
              ]

