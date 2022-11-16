from django.views.generic import RedirectView


class checkAccount(RedirectView):

    def get(self, request, *args, **kwargs):
        downlink = kwargs.get('lnk')
        if request.user.has_account:
            self.url = downlink
        return super().get(request, *args, **kwargs)
