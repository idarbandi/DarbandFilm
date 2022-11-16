from django.urls import path
from account.views import checkAccount


urlpatterns = [
    path('/download', checkAccount.as_view(), name='download_qualify'),

]