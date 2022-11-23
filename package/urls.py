from django.urls import path, include
from package.views import BuyPackage, ViewPackage

urlpatterns = [
    path('buy/', BuyPackage.as_view(), name='BuyPackage'),
    path('view/', ViewPackage.as_view(), name='ViewPackage'),
    path('purchase/', include('purchase.urls'))
]