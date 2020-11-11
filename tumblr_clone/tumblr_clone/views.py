from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

class LoginPage(TemplateView):
    template_name ='login_test.html'

class LogoutPage(TemplateView):
    template_name ='logout_test.html'
