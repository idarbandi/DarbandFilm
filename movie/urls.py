from django.urls import path, include
from movie.views import main, movie, Search


urlpatterns = [
                  path('/main', main.as_view()),
                  path('/<int:pk>', movie.as_view(), name='movie'),
                  path('/search', Search.as_view(), name='searchbox'),
                  path('/account/financial/', include('financial.urls')),
                  path('/account/package', include('package.urls'))
              ]

