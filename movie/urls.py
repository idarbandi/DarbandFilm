from django.urls import path, include, re_path
from movie.views import main, movie, Search, Comment


urlpatterns = [
                  path('/main', main.as_view(), name='main'),
                  path('/<str:name>', movie.as_view(), name='movie'),
                  path('/search', Search.as_view(), name='searchbox'),
                  path('/comments/', Comment.as_view(), name='MovieComment'),
                  path('/package/', include('package.urls')),
                  re_path(r'^/account', include('account.urls'))
              ]

