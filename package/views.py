from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from account.models import account


class BuyPackage(LoginRequiredMixin, View):
    template_name = 'packages.html'
    login_url = 'http://127.0.0.1:8000/admin/login/?next=/admin/'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ViewPackage(View):
    template_name = 'packages.html'

    def get(self, request, *args, **kwargs):
        Account = account.objects.get(user=request.user)
        return render(request, self.template_name, {"account": Account.package})
