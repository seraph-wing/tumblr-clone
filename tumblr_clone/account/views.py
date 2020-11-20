from django.shortcuts import render
from django.views.generic import CreateView,TemplateView
from django.views.generic.detail import DetailView
from . import forms
from django.urls import reverse_lazy
from .models import User
# Create your views here.

class AccountIndex(DetailView):
    model = User
    template_name = 'account/account_index.html'

class SignUpView(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'account/signup.html'

class LoginView(TemplateView):
    template_name = 'account/login.html'
