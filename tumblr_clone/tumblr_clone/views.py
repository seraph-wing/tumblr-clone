from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
app_name = 'home'


class LoginPage(TemplateView):
    template_name = 'login.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = "index.html"

"""
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse("login"))
        return super().get(request, *args, **kwargs)
"""
