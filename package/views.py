from django.shortcuts import render
from django.views import View


class BuyPackage(View):
    template_name = 'packages.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)